from __future__ import annotations

import json
import logging
from pathlib import Path

from co_op_translator.utils.common.file_utils import (
    filter_files,
    handle_empty_document,
    read_input_file,
)
from co_op_translator.utils.common.metadata_utils import (
    is_notebook_up_to_date,
    save_text_metadata_for_source,
)
from co_op_translator.utils.markdown.notebook_path_rewriter import (
    rewrite_notebook_paths,
)
from co_op_translator.utils.markdown.path_rewriter import MarkdownPathRewritePolicy

logger = logging.getLogger(__name__)


class ProjectNotebookTranslationMixin:
    def _rewrite_notebook_paths_for_target(
        self,
        content: str,
        file_path: Path,
        translated_path: Path,
        language_code: str,
    ) -> str:
        notebook_translation_types = ["markdown", "notebook"]
        if "images" in self.translation_types:
            notebook_translation_types.append("images")

        return rewrite_notebook_paths(
            content,
            source_path=file_path,
            target_path=translated_path,
            policy=MarkdownPathRewritePolicy(
                language_code=language_code,
                root_dir=self.root_dir,
                translations_dir=self.translations_dir,
                translated_images_dir=self.image_dir,
                translation_types=notebook_translation_types,
                lang_subdir=self.lang_subdir,
            ),
        )

    async def _append_notebook_disclaimer(
        self, content: str, language_code: str
    ) -> str:
        if not self.add_disclaimer:
            return content

        disclaimer_text = await self.markdown_translator.generate_disclaimer(
            language_code
        )
        if not disclaimer_text:
            return content

        notebook = json.loads(content)
        start_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER START -->"
        end_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER END -->"
        disclaimer_block = f"---\n\n{start_marker}\n{disclaimer_text}\n{end_marker}"
        notebook.setdefault("cells", []).append(
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [disclaimer_block + "\n"],
            }
        )
        return json.dumps(notebook, ensure_ascii=False, indent=1)

    async def translate_notebook(self, file_path: Path, language_code: str) -> str:
        """Translate a Jupyter notebook file to the specified language."""

        file_path = Path(file_path).resolve()
        try:
            document = read_input_file(file_path)
            if not document:
                relative_path = file_path.relative_to(self.root_dir)
                output_file = self._get_language_root(language_code) / relative_path
                handle_empty_document(file_path, output_file)
                return str(output_file)

            relative_path = file_path.relative_to(self.root_dir)
            translated_path = self._get_language_root(language_code) / relative_path
            translated_content = await self.notebook_translator.translate_notebook(
                document,
                language_code,
                source_path=file_path,
            )
            translated_content = self._rewrite_notebook_paths_for_target(
                translated_content,
                file_path,
                translated_path,
                language_code,
            )
            translated_content = await self._append_notebook_disclaimer(
                translated_content,
                language_code,
            )
            if not translated_content:
                logger.error(
                    f"Translation failed for {file_path}: Empty translation result"
                )
                return ""

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
                raise

        except Exception as e:
            logger.error(f"Failed to translate {file_path}: {e}")
            return ""

    async def translate_all_notebook_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all Jupyter notebook files in the project directory."""

        modified_count = 0
        errors = []

        if not self.notebook_translator:
            logger.info("Notebook translator not available, skipping notebook files")
            return modified_count, errors

        if update:
            for language_code in self.language_codes:
                translation_dir = self._get_language_root(language_code)
                if translation_dir.exists():
                    for ext in self.supported_notebook_extensions:
                        for notebook_file in translation_dir.rglob(f"*{ext}"):
                            notebook_file.unlink()
                            logger.info(f"Deleted translated notebook: {notebook_file}")

        notebook_files = []
        for ext in self.supported_notebook_extensions:
            notebook_files.extend(filter_files(self.root_dir, self.excluded_dirs, ext))

        tasks = []
        task_info = []

        for notebook_file_path in notebook_files:
            notebook_file_path = notebook_file_path.resolve()

            for language_code in self.language_codes:
                relative_path = notebook_file_path.relative_to(self.root_dir)
                translated_notebook_path = (
                    self._get_language_root(language_code) / relative_path
                )

                if translated_notebook_path.exists() and not update:
                    if is_notebook_up_to_date(
                        notebook_file_path, translated_notebook_path
                    ):
                        logger.info(
                            f"Skipping up-to-date notebook: {translated_notebook_path}"
                        )
                        continue

                    logger.info(
                        f"Notebook is outdated, will retranslate: {notebook_file_path} -> {translated_notebook_path}"
                    )

                logger.info(
                    f"Translating notebook file: {notebook_file_path} for language: {language_code}"
                )
                tasks.append(
                    lambda notebook_file_path=notebook_file_path, language_code=language_code: self.translate_notebook(
                        notebook_file_path, language_code
                    )
                )
                task_info.append((str(notebook_file_path), language_code))

        if tasks:
            results = await self.process_api_requests_sequential(
                tasks,
                "Translating notebook files",
                file_info=task_info,
                stage_key="translating_notebook_files",
            )
            modified_count = sum(1 for r in results if r)
            errors = [
                f"Failed to translate notebook file: {file_path} (lang: {lang_code})"
                for (file_path, lang_code), result in zip(task_info, results)
                if not result
            ]
        else:
            logger.warning("No notebook files found for translation.")

        return modified_count, errors
