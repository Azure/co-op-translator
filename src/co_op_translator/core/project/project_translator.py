import logging
from pathlib import Path
import asyncio
from co_op_translator.core.llm import (
    markdown_translator,
    text_translator,
)
from co_op_translator.core.vision import (
    image_translator,
)
from co_op_translator.config.constants import (
    EXCLUDED_DIRS,
    SUPPORTED_IMAGE_EXTENSIONS,
)

from .directory_manager import DirectoryManager
from .translation_manager import TranslationManager

logger = logging.getLogger(__name__)


class ProjectTranslator:
    """Manages translation of project content across multiple languages.

    Coordinates translation of markdown documents and images, directory management,
    and tracking of translation status across the project.
    """

    def __init__(self, language_codes, root_dir=".", markdown_only=False):
        """Initialize project translation environment.

        Sets up translators and managers needed for project translation operations.

        Args:
            language_codes: Space-separated list of target language codes
            root_dir: Root directory of the project to translate
            markdown_only: Whether to process only markdown files and skip images
        """
        self.language_codes = language_codes.split()
        self.root_dir = Path(root_dir).resolve()
        self.translations_dir = self.root_dir / "translations"
        self.image_dir = self.root_dir / "translated_images"
        self.markdown_only = markdown_only

        # Initialize text translator
        self.text_translator = text_translator.TextTranslator.create()

        # Initialize image translator if not in markdown-only mode
        try:
            if not markdown_only:
                self.image_translator = image_translator.ImageTranslator.create(
                    default_output_dir=self.image_dir, root_dir=self.root_dir
                )
            else:
                logger.info(
                    "Skipping image translator initialization in markdown-only mode"
                )
                self.image_translator = None
        except ValueError as e:
            logger.info(
                "Switching to markdown-only mode due to missing Computer Vision configuration"
            )
            self.markdown_only = True  # Auto-switch to markdown-only mode
            self.image_translator = None

        self.markdown_translator = markdown_translator.MarkdownTranslator.create(
            self.root_dir
        )

        # Initialize directory and translation managers
        self.directory_manager = DirectoryManager(
            self.root_dir, self.translations_dir, self.language_codes, EXCLUDED_DIRS
        )
        self.translation_manager = TranslationManager(
            self.root_dir,
            self.translations_dir,
            self.image_dir,
            self.language_codes,
            EXCLUDED_DIRS,
            SUPPORTED_IMAGE_EXTENSIONS,
            self.markdown_translator,
            self.image_translator,
            self.markdown_only,
        )

    def translate_project(
        self, images=False, markdown=False, update=False, fast_mode=False
    ):
        """Start the project translation process synchronously.

        Serves as a public entry point that delegates to the async translation manager.

        Args:
            images: Whether to translate images
            markdown: Whether to translate markdown files
            update: Whether to update existing translations
            fast_mode: Whether to use faster translation method
        """
        asyncio.run(
            self.translation_manager.translate_project_async(
                images=images, markdown=markdown, update=update, fast_mode=fast_mode
            )
        )

    async def check_and_retry_translations(self):
        """Check for outdated translations and translate missing content.

        Performs a three-step process:
        1. Identifies and updates outdated translations
        2. Translates all markdown files that need translation
        3. Translates all image files that need translation (when available)

        Returns:
            Tuple containing (total_translated_count, combined_errors_list)
        """
        # Check outdated files first
        modified_count, errors = await self.translation_manager.check_outdated_files()
        logger.info(f"Found {modified_count} outdated files")
        if errors:
            logger.warning(f"Errors during checking outdated files: {errors}")

        # Translate all markdown files
        (
            markdown_count,
            markdown_errors,
        ) = await self.translation_manager.translate_all_markdown_files()
        logger.info(f"Translated {markdown_count} markdown files")
        if markdown_errors:
            logger.warning(f"Errors during markdown translation: {markdown_errors}")

        # Translate images if image translator is available
        (
            image_count,
            image_errors,
        ) = await self.translation_manager.translate_all_image_files()
        logger.info(f"Translated {image_count} image files")
        if image_errors:
            logger.warning(f"Errors during image translation: {image_errors}")

        return (
            modified_count + markdown_count + image_count,
            errors + markdown_errors + image_errors,
        )
