from pathlib import Path
import logging
from typing import List
from tqdm import tqdm
import re
import json
import os
import asyncio

from co_op_translator.utils.common.file_utils import (
    read_input_file,
    filter_files,
    delete_translated_images_by_language_code,
    delete_translated_markdown_files_by_language_code,
    get_filename_and_extension,
    generate_translated_filename,
    handle_empty_document,
)
from co_op_translator.utils.common.metadata_utils import calculate_file_hash
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.project.directory_manager import DirectoryManager
from co_op_translator.config.constants import SUPPORTED_IMAGE_EXTENSIONS
from co_op_translator.utils.common.task_utils import worker
from co_op_translator.utils.llm.markdown_utils import compare_line_breaks

logger = logging.getLogger(__name__)


class TranslationManager:
    """
    Manages the translation of markdown and image files.
    """

    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path,
        image_dir: Path,
        language_codes: list[str],
        excluded_dirs: list[str],
        supported_image_extensions: list[str],
        markdown_translator: MarkdownTranslator,
        image_translator=None,
        markdown_only: bool = False,
    ):
        """
        Initialize TranslationManager.

        Args:
            root_dir: Root directory containing original files
            translations_dir: Directory for translated files
            image_dir: Directory for translated images
            language_codes: List of target language codes
            excluded_dirs: List of directories to exclude
            supported_image_extensions: List of supported image extensions
            markdown_translator: Translator instance for markdown files
            image_translator: Translator instance for image files
            markdown_only: Whether to only translate markdown files
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs
        self.supported_image_extensions = supported_image_extensions
        self.markdown_translator = markdown_translator
        self.image_translator = image_translator
        self.markdown_only = markdown_only
        self.directory_manager = DirectoryManager(
            root_dir, translations_dir, language_codes, excluded_dirs
        )

    async def translate_image(
        self, image_path: Path, language_code: str, fast_mode: bool = False
    ) -> str:
        """
        Translate an image and handle file permissions or path errors.

        Args:
            image_path (Path): Path to the image file
            language_code (str): Target language code
            fast_mode (bool): Whether to use faster translation method

        Returns:
            str: The translated image path if successful, otherwise the original path
        """
        image_path = Path(image_path).resolve()
        if not self.image_translator:
            logger.info(
                f"Image translation skipped for {image_path} due to missing Computer Vision configuration"
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
            translated_image_path = self.image_translator.translate_image(
                image_path, language_code, self.image_dir, fast_mode=fast_mode
            )
            logger.info(
                f"Translated image {image_path} to {language_code} and saved to {translated_image_path}"
            )
            return str(translated_image_path)
        except Exception as e:
            logger.error(f"Failed to translate image {image_path}: {e}", exc_info=True)
            return str(image_path)

    async def translate_markdown(self, file_path: Path, language_code: str) -> str:
        """
        Translate a markdown file to the specified language.

        Args:
            file_path (Path): Path to the markdown file.
            language_code (str): The target language code.

        Returns:
            str: The path to translated markdown file if successful, otherwise empty string
        """
        file_path = Path(file_path).resolve()
        try:
            document = read_input_file(file_path)
            if not document:
                relative_path = file_path.relative_to(self.root_dir)
                output_file = self.translations_dir / language_code / relative_path
                handle_empty_document(file_path, output_file)
                return str(output_file)

            # First attempt at translation
            translated_content = await self.markdown_translator.translate_markdown(
                document, language_code, file_path, markdown_only=self.markdown_only
            )
            if not translated_content:
                logger.error(
                    f"Translation failed for {file_path}: Empty translation result"
                )
                return ""

            # Check if translation format is broken (e.g., line breaks mismatch)
            if compare_line_breaks(document, translated_content):
                logger.warning(f"Translation failed for {file_path}. Retrying...")
                # Retry translation
                translated_content = await self.markdown_translator.translate_markdown(
                    document, language_code, file_path, markdown_only=self.markdown_only
                )
                if not translated_content:
                    logger.error(
                        f"Retry translation failed for {file_path}: Empty translation result"
                    )
                    return ""

            relative_path = file_path.relative_to(self.root_dir)
            translated_path = self.translations_dir / language_code / relative_path
            translated_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                with open(translated_path, "w", encoding="utf-8") as f:
                    f.write(translated_content)
                logger.info(
                    f"Translated {file_path} to {language_code} and saved to {translated_path}"
                )
                return str(translated_path)
            except Exception as e:
                logger.error(f"Failed to write translation to {translated_path}: {e}")
                return ""

        except Exception as e:
            logger.error(f"Failed to translate {file_path}: {e}")
            return ""

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        """
        Translate all markdown files in the project directory.

        Args:
            update (bool): If True, update existing translations. Defaults to False.

        Returns:
            tuple[int, list[str]]: A tuple containing:
                - Number of files modified
                - List of error messages
        """
        modified_count = 0
        errors = []

        # Step 1: If update is True, delete all existing translated markdown files
        if update:
            for language_code in self.language_codes:
                delete_translated_markdown_files_by_language_code(
                    language_code, self.translations_dir
                )
                logger.info(
                    f"Deleted all translated markdown files for language: {language_code}"
                )

        # Step 2: Collect markdown files for translation
        markdown_files = filter_files(self.root_dir, self.excluded_dirs)
        tasks = []

        for md_file_path in markdown_files:
            md_file_path = md_file_path.resolve()

            if md_file_path.suffix == ".md":
                for language_code in self.language_codes:
                    relative_path = md_file_path.relative_to(self.root_dir)
                    translated_md_path = (
                        self.translations_dir / language_code / relative_path
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

        if tasks:  # Check if there are tasks to process
            # Step 3: Process markdown translations sequentially using the sequential API request queue
            results = await self.process_api_requests_sequential(
                tasks, "🛠️  Translating markdown files"
            )
            modified_count = sum(
                1 for r in results if r
            )  # Count successful translations
            errors = [
                f"Failed to translate {task.__name__}"
                for task, result in zip(tasks, results)
                if not result
            ]
        else:
            logger.warning("No markdown files found for translation.")

        return modified_count, errors

    async def translate_all_image_files(
        self, update: bool = False, fast_mode: bool = False
    ) -> tuple[int, list[str]]:
        """
        Translate all image files, with optional update mode to refresh translations.

        Args:
            update (bool): If True, update existing translations. Defaults to False.

        Returns:
            tuple[int, list[str]]: A tuple containing:
                - Number of files modified
                - List of error messages
        """
        modified_count = 0
        errors = []

        logger.info("Starting image translation tasks...")

        # Step 1: If update is True, delete all existing translated images
        if update:
            for language_code in self.language_codes:
                delete_translated_images_by_language_code(language_code, self.image_dir)
                logger.info(
                    f"Deleted all translated images for language: {language_code}"
                )

        # Step 2: Collect image files for translation
        image_files = filter_files(self.root_dir, self.excluded_dirs)
        tasks = []

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
                    translated_image_path = Path(self.image_dir) / translated_filename

                    if not update and translated_image_path.exists():
                        logger.info(
                            f"Skipping already translated image: {translated_image_path}"
                        )
                        continue

                    logger.info(
                        f"Translating image: {image_file_path} for language: {language_code}"
                    )
                    tasks.append(
                        self.translate_image(
                            image_file_path, language_code, fast_mode=fast_mode
                        )
                    )

        if tasks:
            # Step 3: Process image translations using API request queue
            results = await self.process_api_requests_parallel(
                tasks, f"{'🏎️  (fast mode)' if fast_mode else '🖼️ '} Translating images"
            )
            modified_count = sum(
                1 for r in results if r != str(image_file_path)
            )  # Count successful translations
            errors = [
                f"Failed to translate {task.__name__}"
                for task, result in zip(tasks, results)
                if result == str(image_file_path)
            ]
        else:
            logger.warning("No image files found for translation.")

        return modified_count, errors

    async def check_outdated_files(self, update: bool = False) -> tuple[int, List[str]]:
        """
        Check for outdated translated files by comparing metadata hash values and retranslate if needed.

        Args:
            update (bool): Whether to update existing translations regardless of hash values

        Returns:
            tuple[int, List[str]]: Number of retranslated files and list of errors
        """
        modified_count = 0
        errors = []

        # Find all markdown files in root directory
        markdown_files = [
            f
            for f in filter_files(self.root_dir, self.excluded_dirs)
            if f.suffix.lower() == ".md"
        ]

        # Create progress bar
        with tqdm(total=len(markdown_files) * len(self.language_codes)) as pbar:
            # Process each markdown file
            for md_file in markdown_files:
                try:
                    # Calculate relative path from root
                    relative_path = md_file.relative_to(self.root_dir)

                    # Translate to each language
                    for lang_code in self.language_codes:
                        try:
                            # Calculate target path
                            target_path = (
                                self.translations_dir / lang_code / relative_path
                            )

                            # Skip if target doesn't exist
                            if not target_path.exists():
                                pbar.update(1)
                                continue

                            # Read target file content and extract metadata
                            target_content = target_path.read_text(encoding="utf-8")

                            # Create current metadata for comparison
                            current_metadata = self.markdown_translator.create_metadata(
                                md_file, lang_code
                            )
                            current_hash = current_metadata.get("file_hash")

                            # Extract metadata from the target file using metadata_utils
                            metadata_match = re.search(
                                r"<!--\s*translation-metadata\s*(.*?)\s*-->",
                                target_content,
                                re.DOTALL,
                            )
                            if not metadata_match:
                                logger.warning(f"No metadata found in {target_path}")
                                pbar.update(1)
                                continue

                            try:
                                stored_metadata = json.loads(metadata_match.group(1))
                            except json.JSONDecodeError:
                                logger.warning(f"Invalid metadata in {target_path}")
                                pbar.update(1)
                                continue

                            # Get stored hash from metadata
                            stored_hash = stored_metadata.get("file_hash")
                            if not stored_hash:
                                logger.warning(
                                    f"No file hash in metadata of {target_path}"
                                )
                                pbar.update(1)
                                continue

                            # Compare hashes and retranslate if different
                            if update or stored_hash != current_hash:
                                # Read original content
                                content = md_file.read_text(encoding="utf-8")

                                # Translate content
                                translated_content = (
                                    await self.markdown_translator.translate_markdown(
                                        content, lang_code, md_file, self.markdown_only
                                    )
                                )

                                # Write translated content
                                target_path.write_text(
                                    translated_content, encoding="utf-8"
                                )
                                modified_count += 1
                                logger.info(
                                    f"Retranslated {md_file} to {lang_code} due to content changes"
                                )

                        except Exception as e:
                            error_msg = f"Error checking/retranslating {md_file} to {lang_code}: {str(e)}"
                            logger.error(error_msg)
                            errors.append(error_msg)

                        finally:
                            pbar.update(1)

                except Exception as e:
                    error_msg = f"Error processing {md_file}: {str(e)}"
                    logger.error(error_msg)
                    errors.append(error_msg)
                    pbar.update(len(self.language_codes))

        return modified_count, errors

    async def translate_project_async(
        self,
        images: bool = False,
        markdown: bool = False,
        update: bool = False,
        fast_mode: bool = False,
    ) -> tuple[int, list[str]]:
        """
        Asynchronously translate the project.

        The translation process follows these steps:
        1. Remove orphaned files
        2. Synchronize directory structure with source
        3. Identify outdated translations
        4. Perform translation on required files

        Args:
            images (bool): Whether to translate images. Defaults to False.
            markdown (bool): Whether to translate markdown files. Defaults to False.
            update (bool): Whether to update existing translations. Defaults to False.
            fast_mode (bool): Whether to use faster translation method. Defaults to False.

        Returns:
            tuple[int, list[str]]: A tuple containing:
                - Total number of files modified
                - List of error messages
        """
        logger.info("Starting project translation...")
        total_modified = 0
        all_errors = []

        try:
            # 1. Remove orphaned files first
            logger.info("Removing orphaned files...")
            with tqdm(total=1, desc="🧹 Cleaning orphaned files") as cleanup_progress:
                removed_count = self.directory_manager.cleanup_orphaned_translations(
                    markdown=markdown, images=images
                )
                cleanup_progress.set_postfix_str(
                    "None" if removed_count == 0 else f"Removed: {removed_count}"
                )
                cleanup_progress.update(1)

            # 2. Then synchronize directory structure
            logger.info("Synchronizing directory structure...")
            with tqdm(total=1, desc="📁 Synchronizing directories") as sync_progress:
                created, removed, _ = self.directory_manager.sync_directory_structure()
                sync_progress.set_postfix_str(
                    "None"
                    if (created == 0 and removed == 0)
                    else f"Created: {created}, Removed: {removed}"
                )
                sync_progress.update(1)

            # 3. Identify files requiring updates
            if markdown:
                with tqdm(total=1, desc="🔍 Checking translations") as check_progress:
                    outdated_files = self.get_outdated_translations()
                    check_progress.set_postfix_str(
                        "None"
                        if not outdated_files
                        else f"Found: {len(outdated_files)}"
                    )
                    check_progress.update(1)

                if outdated_files:
                    await self.retranslate_outdated_files(outdated_files)

            # 4. Perform translation
            if markdown:
                md_modified, md_errors = await self.translate_all_markdown_files(
                    update=update
                )
                total_modified += md_modified
                all_errors.extend(md_errors)

            if images and not self.markdown_only:
                img_modified, img_errors = await self.translate_all_image_files(
                    update=update, fast_mode=fast_mode
                )
                total_modified += img_modified
                all_errors.extend(img_errors)

        except Exception as e:
            logger.error(f"Error during translation: {e}")
            all_errors.append(str(e))

        logger.info(f"Translation completed. Modified {total_modified} files.")
        if all_errors:
            logger.warning(f"Encountered {len(all_errors)} errors during translation")

        return total_modified, all_errors

    def get_outdated_translations(self) -> List[tuple[Path, Path]]:
        """
        Identify translations that need updates by comparing metadata.

        Returns:
            List[tuple[Path, Path]]: List of (original file, translation file) tuples that need updates
        """
        outdated_files = []
        all_translation_files = []

        for lang_code in self.language_codes:
            translation_dir = self.translations_dir / lang_code
            if not translation_dir.exists():
                continue
            for md_file in translation_dir.rglob("*.md"):
                all_translation_files.append((lang_code, md_file))

        if not all_translation_files:
            return []

        for lang_code, trans_file in all_translation_files:
            try:
                relative_path = trans_file.relative_to(
                    self.translations_dir / lang_code
                )
                original_file = self.root_dir / relative_path

                if not original_file.exists():
                    continue

                # Compare metadata
                if self._is_translation_outdated(original_file, trans_file):
                    outdated_files.append((original_file, trans_file))
            except ValueError:
                logger.warning(f"Error calculating relative path for {trans_file}")
                continue

        return outdated_files

    async def retranslate_outdated_files(
        self, outdated_files: List[tuple[Path, Path]]
    ) -> None:
        """
        Retranslate the given outdated files.
        Args:
            outdated_files: List of (original_file, translation_file) tuples to retranslate
        """
        if not outdated_files:
            return

        files_to_translate = []
        for original_file, translation_file in outdated_files:
            try:
                relative_path = translation_file.relative_to(self.translations_dir)
                lang_code = relative_path.parts[0]

                if lang_code not in self.language_codes:
                    logger.warning(
                        f"Unknown language code in path: {lang_code}, skipping {translation_file}"
                    )
                    continue

                files_to_translate.append((original_file, lang_code))
            except (ValueError, IndexError) as e:
                logger.error(
                    f"Failed to extract language code from {translation_file}: {e}"
                )
                continue

        with tqdm(
            total=len(files_to_translate), desc="🔄 Retranslating outdated files"
        ) as progress_bar:
            for original_file, language_code in files_to_translate:
                await self.translate_markdown(original_file, language_code)
                progress_bar.update(1)
                progress_bar.set_postfix_str(f"Current: {original_file.name}")

    async def check_and_retry_translations(self):
        """
        Check translated files for errors and retry translation if needed.
        Display a single progress bar for both checking and retry processes.
        """
        total_files_checked = 0
        files_to_translate = []

        # Collect all markdown files
        markdown_files = [
            file
            for file in filter_files(self.root_dir, self.excluded_dirs)
            if file.suffix == ".md"
        ]
        all_markdown_files = [
            (file, language_code)
            for file in markdown_files
            for language_code in self.language_codes
        ]

        total_files = len(all_markdown_files)

        if total_files == 0:
            logger.warning("No markdown files found for checking.")
            return

        logger.info("Checking translated files for errors...")

        # Step 1: Check all markdown files and collect files that need translation
        with tqdm(
            total=total_files, desc="Checking files", unit="file"
        ) as progress_bar:
            for md_file_path, language_code in all_markdown_files:
                md_file_path = Path(md_file_path).resolve()
                total_files_checked += 1

                # Find the path of the translated file
                relative_path = md_file_path.relative_to(self.root_dir)
                translated_md_file_path = (
                    self.translations_dir / language_code / relative_path
                )

                if not translated_md_file_path.exists():
                    logger.warning(
                        f"Translated file does not exist: {translated_md_file_path}"
                    )
                    files_to_translate.append((md_file_path, language_code))
                    progress_bar.update(1)
                    continue

                # Read the content of both original and translated files
                original_content = read_input_file(md_file_path)
                translated_content = read_input_file(translated_md_file_path)

                # Check if line breaks are mismatched
                if compare_line_breaks(original_content, translated_content):
                    files_to_translate.append((md_file_path, language_code))
                    logger.warning(
                        f"Detected formatting issue in {translated_md_file_path}"
                    )

                # Update the progress bar after each file is checked
                progress_bar.update(1)

        # Step 2: Translate missing or mismatched files
        if files_to_translate:
            logger.info(f"Starting translation for {len(files_to_translate)} files...")

            # Create a progress bar for translations
            with tqdm(
                total=len(files_to_translate), desc="Translating files", unit="file"
            ) as translation_progress_bar:
                for md_file_path, language_code in files_to_translate:
                    logger.info(f"Translating {md_file_path} to {language_code}...")

                    # Translate the file
                    await self.translate_markdown(
                        file_path=md_file_path,
                        language_code=language_code,
                    )

                    # Update the progress bar for translation process
                    translation_progress_bar.update(1)

            logger.info(f"Total files translated: {len(files_to_translate)}")
        else:
            logger.info("No formatting issues found in the translated files.")

        logger.info(f"Total files checked: {total_files_checked}")

    async def process_api_requests_parallel(self, tasks, task_desc) -> list:
        """
        Process API requests using a queue system for better resource management (Parallel).
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return []

        task_queue = asyncio.Queue()

        # Step 1: Populate the queue with tasks
        for task in tasks:
            task_queue.put_nowait(task)

        # Step 2: Create a progress bar
        with tqdm(total=len(tasks), desc=task_desc) as progress_bar:
            # Step 3: Create worker tasks to process the queue
            workers = [
                asyncio.create_task(worker(task_queue, progress_bar)) for _ in range(5)
            ]

            # Step 4: Wait until all tasks are processed
            await task_queue.join()

            # Get results from completed tasks
            results = [task.result() for task in workers]

            # Ensure all workers have completed
            for worker_task in workers:
                worker_task.cancel()

        return results

    async def process_api_requests_sequential(self, tasks, task_desc) -> list:
        """
        Process API requests sequentially, one after another (Sequential).
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return []

        total_tasks = len(tasks)

        results = []
        with tqdm(total=total_tasks, desc=task_desc) as progress_bar:
            for task in tasks:
                result = await task()  # Execute each task sequentially
                results.append(result)
                progress_bar.update(1)  # Update progress bar

        return results

    def _is_translation_outdated(
        self, original_file: Path, translation_file: Path
    ) -> bool:
        """
        Check if a translation needs to be updated by comparing original file's hash with the hash in translation metadata.

        Args:
            original_file (Path): Path to the original file
            translation_file (Path): Path to the translation file

        Returns:
            bool: True if the translation needs to be updated, False otherwise
        """
        if not translation_file.exists():
            return True

        try:
            # Read translation file and find metadata comment
            content = translation_file.read_text(encoding="utf-8")
            metadata_match = re.search(
                r"<!--\s*CO_OP_TRANSLATOR_METADATA:\s*(.*?)\s*-->",
                content,
                re.DOTALL,
            )
            if not metadata_match:
                return True

            try:
                metadata = json.loads(metadata_match.group(1))
            except json.JSONDecodeError:
                return True

            # Compare original file's hash with metadata
            original_hash = calculate_file_hash(original_file)
            stored_hash = metadata.get("original_hash")

            if not stored_hash:
                return True

            return stored_hash != original_hash

        except Exception:
            return True
