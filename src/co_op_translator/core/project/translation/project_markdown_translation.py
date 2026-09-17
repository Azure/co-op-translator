from __future__ import annotations

import logging
import tempfile
from pathlib import Path

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.core.llm.markdown_translator import (
    TranslationContentFilterError,
    TranslationIncompleteError,
)
from co_op_translator.core.project.translation.incremental_markdown import (
    build_incremental_markdown,
)
from co_op_translator.core.project.translation.memory import TranslationUpdate
from co_op_translator.utils.common.file_utils import (
    filter_files,
    handle_empty_document,
    read_input_file,
)
from co_op_translator.utils.common.metadata_utils import (
    save_text_failure_metadata_for_source,
    save_text_metadata_for_source,
    should_retry_text_failure_for_source,
)
from co_op_translator.utils.markdown.path_rewriter import (
    MarkdownPathRewritePolicy,
    rewrite_markdown_paths,
)
from co_op_translator.utils.markdown.processing import compare_line_breaks

logger = logging.getLogger(__name__)


class ProjectMarkdownTranslationMixin:
    async def _append_markdown_disclaimer(
        self, content: str, language_code: str
    ) -> str:
        if not self.add_disclaimer:
            return content

        disclaimer = await self.markdown_translator.generate_disclaimer(language_code)
        if not disclaimer:
            return content

        start_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER START -->"
        end_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER END -->"
        disclaimer_block = f"{start_marker}\n{disclaimer}\n{end_marker}"
        return content + "\n\n---\n\n" + disclaimer_block

    def _rewrite_markdown_paths_for_target(
        self,
        content: str,
        file_path: Path,
        translated_path: Path,
        language_code: str,
    ) -> str:
        return rewrite_markdown_paths(
            content,
            source_path=file_path,
            target_path=translated_path,
            policy=MarkdownPathRewritePolicy(
                language_code=language_code,
                root_dir=self.root_dir,
                translations_dir=self.translations_dir,
                translated_images_dir=self.image_dir,
                translation_types=self.translation_types,
                lang_subdir=self.lang_subdir,
            ),
        )

    def _write_markdown_translation(
        self, translated_path: Path, translated_content: str
    ) -> None:
        translated_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=translated_path.parent,
                prefix=f".{translated_path.name}.",
                suffix=".tmp",
                delete=False,
            ) as temp_file:
                temp_file.write(translated_content)
                temp_path = Path(temp_file.name)

            temp_path.replace(translated_path)
        finally:
            if temp_path and temp_path.exists():
                try:
                    temp_path.unlink()
                except Exception:
                    logger.debug("Failed to remove temporary file: %s", temp_path)

    def _should_record_markdown_failure(self, error: Exception) -> bool:
        if isinstance(
            error, (TranslationIncompleteError, TranslationContentFilterError)
        ):
            return True

        if not isinstance(error, RuntimeError):
            return False

        error_message = str(error)
        return any(
            message in error_message
            for message in (
                "Markdown translation returned empty content",
                "Markdown translation retry returned empty content",
                "Markdown translation retry produced incomplete content",
            )
        )

    async def _translate_markdown_full(
        self,
        document: str,
        file_path: Path,
        translated_path: Path,
        language_code: str,
    ) -> str:
        translated_content = await self.markdown_translator.translate_markdown(
            document,
            language_code,
            source_path=file_path,
        )
        translated_content = self._rewrite_markdown_paths_for_target(
            translated_content,
            file_path,
            translated_path,
            language_code,
        )
        if not translated_content:
            raise RuntimeError(
                f"Markdown translation returned empty content for {file_path}"
            )

        if not compare_line_breaks(document, translated_content):
            return translated_content

        logger.warning("Translation failed for %s. Retrying...", file_path)
        translated_content = await self.markdown_translator.translate_markdown(
            document,
            language_code,
            source_path=file_path,
        )
        translated_content = self._rewrite_markdown_paths_for_target(
            translated_content,
            file_path,
            translated_path,
            language_code,
        )
        if not translated_content:
            raise RuntimeError(
                f"Markdown translation retry returned empty content for {file_path}"
            )
        if compare_line_breaks(document, translated_content):
            raise RuntimeError(
                f"Markdown translation retry produced incomplete content for {file_path}"
            )
        return translated_content

    async def _try_incremental_markdown(
        self,
        document: str,
        file_path: Path,
        translated_path: Path,
        language_code: str,
    ) -> TranslationUpdate | None:
        provider = getattr(self, "translation_state_provider", None)
        if provider is None or not translated_path.exists():
            return None

        try:
            baseline = provider.load_baseline(
                source_path=file_path,
                translation_path=translated_path,
                language_code=language_code,
            )
        except Exception as error:
            logger.warning(
                "Translation baseline lookup failed for %s: %s. Using full translation.",
                file_path,
                error,
            )
            return TranslationUpdate(
                content="", mode="full", fallback_reason="baseline_lookup_failed"
            )

        if baseline is None:
            return TranslationUpdate(
                content="", mode="full", fallback_reason="baseline_unavailable"
            )

        current_target = translated_path.read_text(encoding="utf-8")

        async def translate_block(block: str) -> str:
            result = await self.markdown_translator.translate_markdown(
                block,
                language_code,
                source_path=file_path,
            )
            return self._rewrite_markdown_paths_for_target(
                result,
                file_path,
                translated_path,
                language_code,
            )

        try:
            return await build_incremental_markdown(
                baseline=baseline,
                current_source=document,
                current_target=current_target,
                translate_block=translate_block,
            )
        except Exception as error:
            logger.warning(
                "Incremental translation failed for %s: %s. Using full translation.",
                file_path,
                error,
            )
            return TranslationUpdate(
                content="", mode="full", fallback_reason="incremental_error"
            )

    def _record_translation_candidate(
        self,
        *,
        file_path: Path,
        translated_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        provider = getattr(self, "translation_state_provider", None)
        record_candidate = getattr(provider, "record_candidate", None)
        if not callable(record_candidate):
            return
        try:
            record_candidate(
                source_path=file_path,
                translation_path=translated_path,
                language_code=language_code,
                source_text=source_text,
                target_text=target_text,
                update=update,
            )
        except Exception as error:
            logger.warning(
                "Failed to record translation candidate for %s: %s",
                file_path,
                error,
            )

    async def translate_markdown(
        self,
        file_path: Path,
        language_code: str,
        *,
        incremental: bool = True,
    ) -> str:
        """Translate a markdown file to the specified language."""

        file_path = Path(file_path).resolve()
        try:
            document = read_input_file(file_path)
            relative_path = file_path.relative_to(self.root_dir)
            translated_path = self._get_language_root(language_code) / relative_path

            if not document:
                handle_empty_document(file_path, translated_path)
                return str(translated_path)

            update = (
                await self._try_incremental_markdown(
                    document,
                    file_path,
                    translated_path,
                    language_code,
                )
                if incremental
                else None
            )

            if update is not None and update.mode == "incremental":
                translated_content = update.content
                logger.info(
                    "Incrementally translated %s: preserved=%d translated=%d added=%d deleted=%d",
                    file_path,
                    update.preserved_units,
                    update.translated_units,
                    update.added_units,
                    update.deleted_units,
                )
            else:
                if update is not None:
                    logger.info(
                        "Falling back to full translation for %s: %s",
                        file_path,
                        update.fallback_reason,
                    )
                translated_content = await self._translate_markdown_full(
                    document,
                    file_path,
                    translated_path,
                    language_code,
                )
                update = TranslationUpdate(
                    content=translated_content,
                    mode="full",
                    fallback_reason=(
                        update.fallback_reason if update is not None else None
                    ),
                )

            translated_content = await self._append_markdown_disclaimer(
                translated_content, language_code
            )

            try:
                self._write_markdown_translation(translated_path, translated_content)
                logger.info(
                    f"Translated {file_path} to {language_code} and saved to {translated_path}"
                )
                lang_dir = self._get_language_root(language_code)
                save_text_metadata_for_source(
                    lang_dir,
                    file_path,
                    language_code,
                    root_dir=self.root_dir,
                )
                self._record_translation_candidate(
                    file_path=file_path,
                    translated_path=translated_path,
                    language_code=language_code,
                    source_text=document,
                    target_text=translated_content,
                    update=update,
                )
                return str(translated_path)
            except Exception as e:
                logger.error(f"Failed to write translation to {translated_path}: {e}")
                return ""

        except Exception as e:
            logger.error(f"Failed to translate {file_path}: {e}")
            if not self._should_record_markdown_failure(e):
                return ""

            try:
                lang_dir = self._get_language_root(language_code)
                save_text_failure_metadata_for_source(
                    lang_dir,
                    file_path,
                    language_code,
                    root_dir=self.root_dir,
                    error=e,
                )
                logger.warning(
                    "Recorded failed markdown translation for %s in %s",
                    file_path,
                    lang_dir / ".co-op-translator.json",
                )
            except Exception as metadata_error:
                logger.warning(
                    "Failed to record markdown translation failure for %s: %s",
                    file_path,
                    metadata_error,
                )
            return ""

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all markdown files in the project directory."""

        modified_count = 0
        errors = []

        markdown_files = filter_files(self.root_dir, self.excluded_dirs)
        tasks = []
        task_info = []

        for md_file_path in markdown_files:
            md_file_path = md_file_path.resolve()

            if md_file_path.suffix.lower() not in SUPPORTED_MARKDOWN_EXTENSIONS:
                continue

            for language_code in self.language_codes:
                relative_path = md_file_path.relative_to(self.root_dir)
                translated_md_path = (
                    self._get_language_root(language_code) / relative_path
                )

                if not update and not should_retry_text_failure_for_source(
                    self._get_language_root(language_code),
                    md_file_path,
                    language_code,
                ):
                    logger.info(
                        "Skipping previously failed markdown file until source or "
                        "translator changes: %s",
                        md_file_path,
                    )
                    continue

                if not update and translated_md_path.exists():
                    logger.info(
                        f"Skipping already translated markdown file: {translated_md_path}"
                    )
                    continue

                logger.info(
                    f"Translating markdown file: {md_file_path} for language: {language_code}"
                )
                tasks.append(
                    lambda md_file_path=md_file_path, language_code=language_code: self.translate_markdown(
                        md_file_path, language_code, incremental=not update
                    )
                )
                task_info.append((str(md_file_path), language_code))

        if tasks:
            results = await self.process_api_requests_sequential(
                tasks,
                "Translating markdown files",
                file_info=task_info,
                stage_key="translating_markdown_files",
            )
            modified_count = sum(1 for r in results if r)
            errors = [
                f"Failed to translate markdown file: {file_path} (lang: {lang_code})"
                for (file_path, lang_code), result in zip(task_info, results)
                if not result
            ]
        else:
            logger.warning("No markdown files found for translation.")

        return modified_count, errors
