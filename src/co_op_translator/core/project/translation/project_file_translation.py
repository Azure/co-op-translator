from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from PIL import Image

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    delete_translated_images_by_language_code,
    delete_translated_markdown_files_by_language_code,
    filter_files,
    generate_translated_filename,
    get_filename_and_extension,
    handle_empty_document,
    read_input_file,
)
from co_op_translator.utils.common.metadata_utils import (
    is_image_up_to_date,
    is_notebook_up_to_date,
    save_image_metadata,
    save_text_metadata_for_source,
)
from co_op_translator.utils.markdown.processing import compare_line_breaks
from co_op_translator.utils.markdown.path_rewriter import (
    MarkdownPathRewritePolicy,
    rewrite_markdown_paths,
)
from co_op_translator.utils.markdown.notebook_path_rewriter import (
    rewrite_notebook_paths,
)
from co_op_translator.utils.vision.image_utils import save_optimized_image

logger = logging.getLogger(__name__)


class ProjectFileTranslationMixin:
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

    def _get_translated_image_path(self, image_path: Path, language_code: str) -> Path:
        translated_filename = generate_translated_filename(
            image_path, language_code, self.root_dir
        )
        return Path(self.image_dir) / language_code / translated_filename

    def _save_original_image_translation(
        self, image_path: Path, translated_path: Path, language_code: str
    ) -> str:
        translated_path.parent.mkdir(parents=True, exist_ok=True)
        original_image = Image.open(image_path)
        save_optimized_image(original_image, translated_path)
        save_image_metadata(
            translated_path,
            image_path,
            language_code,
            self.root_dir,
            image_dir=Path(self.image_dir),
        )
        return str(translated_path)

    async def translate_image(
        self, image_path: Path, language_code: str, fast_mode: bool = False
    ) -> str:
        """Translate an image to the target language.

        Handles file permission checks and errors during translation process.

        Args:
            image_path: Path to the image file
            language_code: Target language code
            fast_mode: Whether to use faster translation method

        Returns:
            Translated image path if successful, otherwise the original path
        """
        image_path = Path(image_path).resolve()
        translated_image_path = self._get_translated_image_path(
            image_path, language_code
        )
        if not self.image_translator:
            logger.info(
                f"Image translation skipped for {image_path} due to missing Azure AI Service configuration"
            )
            return str(
                image_path
            )  # Return original image path when translation is not available

        if image_path.exists() and image_path.is_file():
            logger.info(f"Image exists: {image_path}")
            if os.access(image_path, os.R_OK):
                logger.info(f"Read permission granted for: {image_path}")
            else:
                logger.warning(f"Read permission denied for: {image_path}")
                return str(image_path)
        else:
            logger.error(f"Image does not exist or is not a valid file: {image_path}")
            return str(image_path)

        try:
            if translated_image_path.exists() and is_image_up_to_date(
                image_path, translated_image_path, self.image_dir
            ):
                logger.info(
                    f"Skipping image translation; up-to-date output exists: {translated_image_path}"
                )
                return str(translated_image_path)

            translated_image = self.image_translator.translate_image(
                image_path, language_code, fast_mode=fast_mode
            )
            translated_image_path.parent.mkdir(parents=True, exist_ok=True)
            save_optimized_image(translated_image, translated_image_path)
            save_image_metadata(
                translated_image_path,
                image_path,
                language_code,
                self.root_dir,
                image_dir=Path(self.image_dir),
            )

            logger.info(
                f"Translated image {image_path} to {language_code} and saved to {translated_image_path}"
            )
            return str(translated_image_path)
        except Exception as e:
            logger.error(f"Failed to translate image {image_path}: {e}", exc_info=True)
            try:
                return self._save_original_image_translation(
                    image_path, translated_image_path, language_code
                )
            except Exception:
                logger.error(
                    f"Failed to save fallback image translation for {image_path}",
                    exc_info=True,
                )
                return str(image_path)

    async def translate_markdown(self, file_path: Path, language_code: str) -> str:
        """Translate a markdown file to the specified language.

        Handles empty documents, translation failures, and line break inconsistencies.

        Args:
            file_path: Path to the markdown file
            language_code: Target language code

        Returns:
            Path to translated markdown file if successful, otherwise empty string
        """
        file_path = Path(file_path).resolve()
        try:
            document = read_input_file(file_path)
            relative_path = file_path.relative_to(self.root_dir)
            translated_path = self._get_language_root(language_code) / relative_path

            if not document:
                handle_empty_document(file_path, translated_path)
                return str(translated_path)

            # Translate content first, then rewrite project-relative paths for the output target.
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

            # Validate translation format and line break consistency
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
                # Save centralized text metadata for this source notebook in the language directory
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

    async def translate_notebook(self, file_path: Path, language_code: str) -> str:
        """Translate a Jupyter notebook file to the specified language.

        Handles empty documents and translation failures.

        Args:
            file_path: Path to the notebook file
            language_code: Target language code

        Returns:
            Path to translated notebook file if successful, otherwise empty string
        """
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
                # Save centralized text metadata for this source file in the language directory
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

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all markdown files in the project directory.

        Optionally updates existing translations if requested.

        Args:
            update: Whether to update existing translations

        Returns:
            Tuple containing (number_of_modified_files, error_messages_list)
        """
        modified_count = 0
        errors = []

        # Delete existing translations when update mode is enabled
        if update:
            for language_code in self.language_codes:
                delete_translated_markdown_files_by_language_code(
                    language_code, self.translations_dir, self.lang_subdir
                )
                logger.info(
                    f"Deleted all translated markdown files for language: {language_code}"
                )

        # Discover markdown files requiring translation
        markdown_files = filter_files(self.root_dir, self.excluded_dirs)
        tasks = []
        task_info = []  # Store (file_path, language_code) for error reporting

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
                # Create a task for each markdown file translation
                tasks.append(
                    lambda md_file_path=md_file_path, language_code=language_code: self.translate_markdown(
                        md_file_path, language_code
                    )
                )
                task_info.append((str(md_file_path), language_code))

        if tasks:  # Check if there are tasks to process
            # Process translations sequentially to avoid rate limiting
            results = await self.process_api_requests_sequential(
                tasks, "🛠️  Translating markdown files"
            )
            modified_count = sum(
                1 for r in results if r
            )  # Count successful translations
            errors = [
                f"Failed to translate markdown file: {file_path} (lang: {lang_code})"
                for (file_path, lang_code), result in zip(task_info, results)
                if not result
            ]
        else:
            logger.warning("No markdown files found for translation.")

        return modified_count, errors

    async def translate_all_notebook_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all Jupyter notebook files in the project directory.

        Optionally updates existing translations if requested.

        Args:
            update: Whether to update existing translations

        Returns:
            Tuple containing (number_of_modified_files, error_messages_list)
        """
        modified_count = 0
        errors = []

        if not self.notebook_translator:
            logger.info("Notebook translator not available, skipping notebook files")
            return modified_count, errors

        # Delete existing translations when update mode is enabled
        if update:
            for language_code in self.language_codes:
                # Find and delete translated notebook files
                translation_dir = self._get_language_root(language_code)
                if translation_dir.exists():
                    for ext in self.supported_notebook_extensions:
                        for notebook_file in translation_dir.rglob(f"*{ext}"):
                            notebook_file.unlink()
                            logger.info(f"Deleted translated notebook: {notebook_file}")

        # Discover notebook files requiring translation using supported_notebook_extensions
        notebook_files = []
        for ext in self.supported_notebook_extensions:
            notebook_files.extend(filter_files(self.root_dir, self.excluded_dirs, ext))

        tasks = []
        task_info = []  # Store (file_path, language_code) for error reporting

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
                    else:
                        logger.info(
                            f"Notebook is outdated, will retranslate: {notebook_file_path} -> {translated_notebook_path}"
                        )

                logger.info(
                    f"Translating notebook file: {notebook_file_path} for language: {language_code}"
                )
                # Create a task for each notebook file translation
                tasks.append(
                    lambda notebook_file_path=notebook_file_path, language_code=language_code: self.translate_notebook(
                        notebook_file_path, language_code
                    )
                )
                task_info.append((str(notebook_file_path), language_code))

        if tasks:  # Check if there are tasks to process
            # Process translations sequentially to avoid rate limiting
            results = await self.process_api_requests_sequential(
                tasks, "📓 Translating notebook files"
            )
            modified_count = sum(
                1 for r in results if r
            )  # Count successful translations
            errors = [
                f"Failed to translate notebook file: {file_path} (lang: {lang_code})"
                for (file_path, lang_code), result in zip(task_info, results)
                if not result
            ]
        else:
            logger.warning("No notebook files found for translation.")

        return modified_count, errors

    async def translate_all_image_files(
        self, update: bool = False, fast_mode: bool = False
    ) -> tuple[int, list[str]]:
        """Process and translate all image files in the project directory.

        Optionally updates existing translations and uses a faster mode if specified.

        Args:
            update: Whether to update existing translations
            fast_mode: Whether to use faster translation method

        Returns:
            Tuple containing (number_of_modified_files, error_messages_list)
        """
        modified_count = 0
        errors = []

        logger.info("Starting image translation tasks...")

        # Delete existing image translations when update mode is enabled
        if update:
            for language_code in self.language_codes:
                delete_translated_images_by_language_code(language_code, self.image_dir)
                logger.info(
                    f"Deleted all translated images for language: {language_code}"
                )

        # Discover image files requiring translation
        image_files = filter_files(self.root_dir, self.excluded_dirs)
        tasks = []
        task_info = []  # Store (file_path, language_code) for error reporting

        for image_file_path in image_files:
            image_file_path = image_file_path.resolve()

            if (
                get_filename_and_extension(image_file_path)[1]
                in self.supported_image_extensions
            ):
                for language_code in self.language_codes:
                    translated_filename = generate_translated_filename(
                        image_file_path, language_code, self.root_dir
                    )
                    # New canonical path includes the language as a subdirectory
                    translated_image_path = (
                        Path(self.image_dir) / language_code / translated_filename
                    )

                    # Skip if file exists and is up-to-date (outdated images handled separately)
                    if translated_image_path.exists() and not update:
                        if is_image_up_to_date(
                            image_file_path, translated_image_path, self.image_dir
                        ):
                            logger.info(
                                f"Skipping up-to-date image: {translated_image_path}"
                            )
                            continue
                        # Note: outdated images should have been handled by retranslate_outdated_images()
                        # If we reach here, the image was modified after the outdated check
                        logger.info(
                            f"Image metadata mismatch detected: {image_file_path} -> {translated_image_path}"
                        )

                    logger.info(
                        f"Translating image: {image_file_path} for language: {language_code}"
                    )
                    tasks.append(
                        self.translate_image(
                            image_file_path, language_code, fast_mode=fast_mode
                        )
                    )
                    task_info.append((str(image_file_path), language_code))

        if tasks:
            # Process image translations in parallel for efficiency
            results = await self.process_api_requests_parallel(
                tasks, f"{'🏎️  (fast mode)' if fast_mode else '🖼️ '} Translating images"
            )
            modified_count = sum(
                1
                for (file_path, _lang_code), result in zip(task_info, results)
                if result != file_path
            )  # Count successful translations
            errors = [
                f"Failed to translate image file: {file_path} (lang: {lang_code})"
                for (file_path, lang_code), result in zip(task_info, results)
                if result == file_path
            ]
        else:
            logger.warning("No image files found for translation.")

        return modified_count, errors
