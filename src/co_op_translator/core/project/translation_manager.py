from pathlib import Path
import logging
from typing import List
from tqdm import tqdm
import re
import json

from co_op_translator.utils.common.file_utils import filter_files
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator

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
        markdown_translator: MarkdownTranslator,
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
            markdown_translator: Translator instance for markdown files
            markdown_only: Whether to only translate markdown files
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs
        self.markdown_translator = markdown_translator
        self.markdown_only = markdown_only

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, List[str]]:
        """
        Translate all markdown files in the project directory.

        Args:
            update: Whether to update existing translations

        Returns:
            tuple[int, List[str]]: Number of translated files and list of errors
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
                    # Read markdown content
                    content = md_file.read_text(encoding="utf-8")

                    # Calculate relative path from root
                    relative_path = md_file.relative_to(self.root_dir)

                    # Translate to each language
                    for lang_code in self.language_codes:
                        try:
                            # Calculate target path
                            target_path = (
                                self.translations_dir / lang_code / relative_path
                            )

                            # Check if translation is needed
                            if not update and target_path.exists():
                                pbar.update(1)
                                continue

                            # Ensure target directory exists
                            target_path.parent.mkdir(parents=True, exist_ok=True)

                            # Translate content
                            translated_content = (
                                await self.markdown_translator.translate_markdown(
                                    content, lang_code, md_file, self.markdown_only
                                )
                            )

                            # Write translated content
                            target_path.write_text(translated_content, encoding="utf-8")
                            modified_count += 1
                            logger.info(f"Translated {md_file} to {lang_code}")

                        except Exception as e:
                            error_msg = (
                                f"Error translating {md_file} to {lang_code}: {str(e)}"
                            )
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

    async def translate_all_image_files(
        self, update: bool = False
    ) -> tuple[int, List[str]]:
        """
        Translate all image files in the project directory.

        Args:
            update: Whether to update existing translations

        Returns:
            tuple[int, List[str]]: Number of translated files and list of errors
        """
        if self.markdown_only:
            return 0, []

        modified_count = 0
        errors = []

        # Find all image files in root directory
        image_files = [
            f
            for f in filter_files(self.root_dir, self.excluded_dirs)
            if f.suffix.lower() in [".png", ".jpg"]
        ]

        # Create progress bar
        with tqdm(total=len(image_files) * len(self.language_codes)) as pbar:
            # Process each image file
            for img_file in image_files:
                try:
                    # Calculate relative path from root
                    relative_path = img_file.relative_to(self.root_dir)

                    # Translate to each language
                    for lang_code in self.language_codes:
                        try:
                            # Calculate target path
                            target_path = (
                                self.translations_dir / lang_code / relative_path
                            )

                            # Check if translation is needed
                            if not update and target_path.exists():
                                pbar.update(1)
                                continue

                            # Ensure target directory exists
                            target_path.parent.mkdir(parents=True, exist_ok=True)

                            # TODO: Implement image translation
                            # For now, just copy the image
                            import shutil

                            shutil.copy2(img_file, target_path)
                            modified_count += 1
                            logger.info(f"Copied {img_file} to {target_path}")

                        except Exception as e:
                            error_msg = (
                                f"Error translating {img_file} to {lang_code}: {str(e)}"
                            )
                            logger.error(error_msg)
                            errors.append(error_msg)

                        finally:
                            pbar.update(1)

                except Exception as e:
                    error_msg = f"Error processing {img_file}: {str(e)}"
                    logger.error(error_msg)
                    errors.append(error_msg)
                    pbar.update(len(self.language_codes))

        return modified_count, errors

    async def check_outdated_files(self, update: bool = False) -> tuple[int, List[str]]:
        """
        Check for outdated translated files by comparing metadata hash values and retranslate if needed.

        Args:
            update: Whether to update existing translations regardless of hash values

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
                            target_path = self.translations_dir / lang_code / relative_path

                            # Skip if target doesn't exist
                            if not target_path.exists():
                                pbar.update(1)
                                continue

                            # Read target file content and extract metadata
                            target_content = target_path.read_text(encoding="utf-8")
                            
                            # Create current metadata for comparison
                            current_metadata = self.markdown_translator.create_metadata(md_file, lang_code)
                            current_hash = current_metadata.get("file_hash")
                            
                            # Extract metadata from the target file using metadata_utils
                            metadata_match = re.search(r"<!--\s*translation-metadata\s*(.*?)\s*-->", target_content, re.DOTALL)
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
                                logger.warning(f"No file hash in metadata of {target_path}")
                                pbar.update(1)
                                continue

                            # Compare hashes and retranslate if different
                            if update or stored_hash != current_hash:
                                # Read original content
                                content = md_file.read_text(encoding="utf-8")

                                # Translate content
                                translated_content = await self.markdown_translator.translate_markdown(
                                    content, lang_code, md_file, self.markdown_only
                                )

                                # Write translated content
                                target_path.write_text(translated_content, encoding="utf-8")
                                modified_count += 1
                                logger.info(f"Retranslated {md_file} to {lang_code} due to content changes")

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
        self, images: bool = False, markdown: bool = False, update: bool = False
    ) -> tuple[int, List[str]]:
        """
        Translate project files asynchronously.

        Args:
            images: Whether to translate images
            markdown: Whether to translate markdown files
            update: Whether to update existing translations

        Returns:
            tuple[int, List[str]]: Total number of translated files and list of errors
        """
        total_modified = 0
        all_errors = []

        if markdown:
            modified, errors = await self.translate_all_markdown_files(update)
            total_modified += modified
            all_errors.extend(errors)

        if images and not self.markdown_only:
            modified, errors = await self.translate_all_image_files(update)
            total_modified += modified
            all_errors.extend(errors)

        return total_modified, all_errors
