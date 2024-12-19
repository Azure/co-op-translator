import logging
import os
from pathlib import Path
import asyncio
from tqdm.asyncio import tqdm
from co_op_translator.core.llm import (
    markdown_translator,
    text_translator,
)
from co_op_translator.core.vision import (
    image_translator,
)
from co_op_translator.config.constants import (
    SUPPORTED_IMAGE_EXTENSIONS,
    EXCLUDED_DIRS,
)
from co_op_translator.utils.common.file_utils import (
    read_input_file,
    handle_empty_document,
    get_filename_and_extension,
    filter_files,
    generate_translated_filename,
    delete_translated_images_by_language_code,
    delete_translated_markdown_files_by_language_code,
)
from co_op_translator.utils.common.task_utils import worker
from co_op_translator.utils.llm.markdown_utils import compare_line_breaks

logger = logging.getLogger(__name__)

class ProjectTranslator:
    def __init__(self, language_codes, root_dir='.', markdown_only=False):
        self.language_codes = language_codes.split()
        self.root_dir = Path(root_dir).resolve()
        self.translations_dir = self.root_dir / 'translations'
        self.image_dir = self.root_dir / 'translated_images'
        self.markdown_only = markdown_only

        # Use factory methods to create appropriate translators
        self.text_translator = text_translator.TextTranslator.create()
        try:
            if not markdown_only:  # Only create image translator if not in markdown-only mode
                self.image_translator = image_translator.ImageTranslator.create(default_output_dir=self.image_dir, root_dir=self.root_dir)
            else:
                logger.info("Skipping image translator initialization in markdown-only mode")
                self.image_translator = None
        except ValueError as e:
            logger.info("Switching to markdown-only mode due to missing Computer Vision configuration")
            self.markdown_only = True  # Auto-switch to markdown-only mode
            self.image_translator = None
        self.markdown_translator = markdown_translator.MarkdownTranslator.create(self.root_dir)

    async def translate_image(self, image_path, language_code):
        """
        Translate an image and handle file permissions or path errors.
        """
        image_path = Path(image_path).resolve()
        if not self.image_translator:
            logger.info(f"Image translation skipped for {image_path} due to missing Computer Vision configuration")
            return str(image_path)  # Return original image path when translation is not available
            
        if image_path.exists() and image_path.is_file():
            logger.info(f"Image exists: {image_path}")
            if os.access(image_path, os.R_OK):
                logger.info(f"Read permission granted for: {image_path}")
            else:
                logger.warning(f"Read permission denied for: {image_path}")
        else:
            logger.error(f"Image does not exist or is not a valid file: {image_path}")
        
        try:
            translated_image_path = self.image_translator.translate_image(image_path, language_code, self.image_dir)
            logger.info(f"Translated image {image_path} to {language_code} and saved to {translated_image_path}")
        except Exception as e:
            logger.error(f"Failed to translate image {image_path}: {e}", exc_info=True)

    async def translate_markdown(self, file_path, language_code):
        """
        Translate a markdown file to the specified language.
        
        Args:
            file_path (Path): Path to the markdown file.
            language_code (str): The target language code.
        """
        file_path = Path(file_path).resolve()
        try:
            document = read_input_file(file_path)
            if not document:
                relative_path = file_path.relative_to(self.root_dir)
                output_file = self.translations_dir / language_code / relative_path
                handle_empty_document(file_path, output_file)
                return

            # First attempt at translation
            translated_content = await self.markdown_translator.translate_markdown(document, language_code, file_path, markdown_only=self.markdown_only)
            if not translated_content:
                logger.error(f"Translation failed for {file_path}: Empty translation result")
                return

            # Check if translation format is broken (e.g., line breaks mismatch)
            if compare_line_breaks(document, translated_content):
                logger.warning(f"Translation failed for {file_path}. Retrying...")
                # Retry translation
                translated_content = await self.markdown_translator.translate_markdown(document, language_code, file_path, markdown_only=self.markdown_only)
                if not translated_content:
                    logger.error(f"Retry translation failed for {file_path}: Empty translation result")
                    return

            relative_path = file_path.relative_to(self.root_dir)
            translated_path = self.translations_dir / language_code / relative_path
            translated_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                with open(translated_path, "w", encoding='utf-8') as f:
                    f.write(translated_content)
                logger.info(f"Translated {file_path} to {language_code} and saved to {translated_path}")
            except Exception as e:
                logger.error(f"Failed to write translation to {translated_path}: {e}")

        except Exception as e:
            logger.error(f"Failed to translate {file_path}: {e}")

    async def translate_all_markdown_files(self, update=False):
        """
        Translate all markdown files sequentially, with optional update mode to refresh translations.
        """
        logger.info("Starting markdown translation tasks...")

        # Step 1: If update is True, delete all existing translated markdown files
        if update:
            for language_code in self.language_codes:
                delete_translated_markdown_files_by_language_code(language_code, self.translations_dir)
                logger.info(f"Deleted all translated markdown files for language: {language_code}")

        # Step 2: Collect markdown files for translation
        markdown_files = filter_files(self.root_dir, EXCLUDED_DIRS)
        tasks = []

        for md_file_path in markdown_files:
            md_file_path = md_file_path.resolve()

            if md_file_path.suffix == '.md':
                for language_code in self.language_codes:
                    relative_path = md_file_path.relative_to(self.root_dir)
                    translated_md_path = self.translations_dir / language_code / relative_path

                    if not update and translated_md_path.exists():
                        logger.info(f"Skipping already translated markdown file: {translated_md_path}")
                        continue

                    logger.info(f"Translating markdown file: {md_file_path} for language: {language_code}")
                    # Create a task for each markdown file translation
                    tasks.append(lambda md_file_path=md_file_path, language_code=language_code: 
                                self.translate_markdown(md_file_path, language_code))

        if tasks:  # Check if there are tasks to process
            # Step 3: Process markdown translations sequentially using the sequential API request queue
            await self.process_api_requests_sequential(tasks, "Translating markdown files")
        else:
            logger.warning("No markdown files found for translation.")

    async def translate_all_image_files(self, update=False):
        """
        Translate all image files, with optional update mode to refresh translations.
        """
        logger.info("Starting image translation tasks...")

        # Step 1: If update is True, delete all existing translated images
        if update:
            for language_code in self.language_codes:
                delete_translated_images_by_language_code(language_code, self.image_dir)
                logger.info(f"Deleted all translated images for language: {language_code}")

        # Step 2: Collect image files for translation
        image_files = filter_files(self.root_dir, EXCLUDED_DIRS)
        tasks = []

        for image_file_path in image_files:
            image_file_path = image_file_path.resolve()

            if get_filename_and_extension(image_file_path)[1] in SUPPORTED_IMAGE_EXTENSIONS:
                for language_code in self.language_codes:
                    translated_filename = generate_translated_filename(image_file_path, language_code, self.root_dir)
                    translated_image_path = Path(self.image_dir) / translated_filename

                    if not update and translated_image_path.exists():
                        logger.info(f"Skipping already translated image: {translated_image_path}")
                        continue

                    logger.info(f"Translating image: {image_file_path} for language: {language_code}")
                    tasks.append(self.translate_image(image_file_path, language_code))

        # Step 3: Process image translations using API request queue
        await self.process_api_requests_parallel(tasks, "Translating images")

    async def translate_project_async(self, images=False, markdown=False, update=False):
        """
        Translate the entire project, including both markdown and image files.
        
        Args:
            images (bool): Flag to indicate if images should be translated.
            markdown (bool): Flag to indicate if markdown files should be translated.
            update (bool): Flag to indicate if existing translations should be updated.
        """
        logger.info("Starting project translation tasks...")

        if not images and not markdown:
            images = True
            markdown = True
        
        # Add tasks for image translation
        if images:
            await self.translate_all_image_files(update=update)

        # Add tasks for markdown translation
        if markdown:
            await self.translate_all_markdown_files(update=update)

    def translate_project(self, images=False, markdown=False, update=False):
        """
        Public method to start the project translation.

        Args:
            images (bool): Whether to translate images.
            markdown (bool): Whether to translate markdown files.
            update (bool): Whether to update existing translations.
        """
        asyncio.run(self.translate_project_async(images=images, markdown=markdown, update=update))

    async def check_and_retry_translations(self):
        """
        Check translated files for errors and retry translation if needed.
        Display a single progress bar for both checking and retry processes.
        """
        total_files_checked = 0
        files_to_translate = []

        # Collect all markdown files
        markdown_files = [file for file in filter_files(self.root_dir, EXCLUDED_DIRS) if file.suffix == '.md']
        all_markdown_files = [(file, language_code) for file in markdown_files for language_code in self.language_codes]

        total_files = len(all_markdown_files)
        
        if total_files == 0:
            logger.warning("No markdown files found for checking.")
            return

        logger.info("Checking translated files for errors...")

        # Step 1: Check all markdown files and collect files that need translation
        with tqdm(total=total_files, desc="Checking files", unit="file") as progress_bar:
            for md_file_path, language_code in all_markdown_files:
                md_file_path = Path(md_file_path).resolve()
                total_files_checked += 1

                # Find the path of the translated file
                relative_path = md_file_path.relative_to(self.root_dir)
                translated_md_file_path = self.translations_dir / language_code / relative_path

                if not translated_md_file_path.exists():
                    logger.warning(f"Translated file does not exist: {translated_md_file_path}")
                    files_to_translate.append((md_file_path, language_code))
                    progress_bar.update(1)
                    continue

                # Read the content of both original and translated files
                original_content = read_input_file(md_file_path)
                translated_content = read_input_file(translated_md_file_path)

                # Check if line breaks are mismatched
                if compare_line_breaks(original_content, translated_content):
                    files_to_translate.append((md_file_path, language_code))
                    logger.warning(f"Detected formatting issue in {translated_md_file_path}")

                # Update the progress bar after each file is checked
                progress_bar.update(1)

        # Step 2: Translate missing or mismatched files
        if files_to_translate:
            logger.info(f"Starting translation for {len(files_to_translate)} files...")

            # Create a progress bar for translations
            with tqdm(total=len(files_to_translate), desc="Translating files", unit="file") as translation_progress_bar:
                for md_file_path, language_code in files_to_translate:
                    logger.info(f"Translating {md_file_path} to {language_code}...")

                    # Translate the file
                    await self.translate_markdown(md_file_path, language_code)

                    # Update the progress bar for translation process
                    translation_progress_bar.update(1)

            logger.info(f"Total files translated: {len(files_to_translate)}")
        else:
            logger.info("No formatting issues found in the translated files.")

        logger.info(f"Total files checked: {total_files_checked}")

    async def process_api_requests_parallel(self, tasks, task_desc):
        """
        Process API requests using a queue system for better resource management (Parallel).
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return

        task_queue = asyncio.Queue()

        # Step 1: Populate the queue with tasks
        for task in tasks:
            task_queue.put_nowait(task)

        # Step 2: Create a progress bar
        with tqdm(total=len(tasks), desc=task_desc) as progress_bar:
            # Step 3: Create worker tasks to process the queue
            workers = [asyncio.create_task(worker(task_queue, progress_bar)) for _ in range(5)]

            # Step 4: Wait until all tasks are processed
            await task_queue.join()

            # Ensure all workers have completed
            for worker_task in workers:
                worker_task.cancel()

    async def process_api_requests_sequential(self, tasks, task_desc):
        """
        Process API requests sequentially, one after another (Sequential).
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return

        total_tasks = len(tasks)

        with tqdm(total=total_tasks, desc=task_desc) as progress_bar:
            for task in tasks:
                await task()  # Execute each task sequentially
                progress_bar.update(1)  # Update progress bar
