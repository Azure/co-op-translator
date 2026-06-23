from __future__ import annotations

import logging
from pathlib import Path

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    delete_translated_markdown_files_by_language_code,
    filter_files,
    handle_empty_document,
    read_input_file,
)
from co_op_translator.utils.common.metadata_utils import save_text_metadata_for_source
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

    async def translate_markdown(self, file_path: Path, language_code: str) -> str:
        """Translate a markdown file to the specified language."""

        file_path = Path(file_path).resolve()
        try:
            document = read_input_file(file_path)
            relative_path = file_path.relative_to(self.root_dir)
            translated_path = self._get_language_root(language_code) / relative_path

            if not document:
                handle_empty_document(file_path, translated_path)
                return str(translated_path)

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
                logger.error(
                    f"Translation failed for {file_path}: Empty translation result"
                )
                raise RuntimeError(
                    f"Markdown translation returned empty content for {file_path}"
                )

            if compare_line_breaks(document, translated_content):
                logger.warning(f"Translation failed for {file_path}. Retrying...")
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
                    logger.error(
                        f"Retry translation failed for {file_path}: Empty translation result"
                    )
                    raise RuntimeError(
                        f"Markdown translation retry returned empty content for {file_path}"
                    )

            translated_content = await self._append_markdown_disclaimer(
                translated_content, language_code
            )

            translated_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                with open(translated_path, "w", encoding="utf-8") as f:
                    f.write(translated_content)
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
                return str(translated_path)
            except Exception as e:
                logger.error(f"Failed to write translation to {translated_path}: {e}")
                return ""

        except Exception as e:
            logger.error(f"Failed to translate {file_path}: {e}")
            raise

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all markdown files in the project directory."""

        modified_count = 0
        errors = []

        if update:
            for language_code in self.language_codes:
                delete_translated_markdown_files_by_language_code(
                    language_code, self.translations_dir, self.lang_subdir
                )
                logger.info(
                    f"Deleted all translated markdown files for language: {language_code}"
                )

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
                        md_file_path, language_code
                    )
                )
                task_info.append((str(md_file_path), language_code))

        if tasks:
            results = await self.process_api_requests_sequential(
                tasks, "🛠️  Translating markdown files"
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
