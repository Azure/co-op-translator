from __future__ import annotations

import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def reset_translation_directories(
    translations_dir: Path, image_dir: Path, language_codes: list
):
    """
    Remove existing translation and translated_images directories if they exist,
    and then create new ones.

    Args:
        translations_dir (Path): The directory where translations are stored.
        image_dir (Path): The directory where translated images are stored.
        language_codes (list): A list of language codes for creating language-specific directories.
    """
    # Remove existing directories
    if translations_dir.exists():
        shutil.rmtree(translations_dir)
        logger.info(f"Removed existing translations directory: {translations_dir}")

    if image_dir.exists():
        shutil.rmtree(image_dir)
        logger.info(f"Removed existing translated_images directory: {image_dir}")

    # Create new directories for each language
    for lang_code in language_codes:
        lang_dir = translations_dir / lang_code
        lang_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory for {lang_code}: {lang_dir}")

        image_lang_dir = image_dir / lang_code
        image_lang_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created image directory for {lang_code}: {image_lang_dir}")


def delete_translated_images_by_language_code(language_code: str, image_dir: Path):
    """
    Delete all translated images in the given directory that have the specified language code in their filenames.

    Args:
        language_code (str): The language code to filter files by (e.g., 'ko').
        image_dir (Path): The directory where translated images are stored (e.g., './translated_images').
    """
    """
    Delete the entire image directory for the specified language code, including all its contents.

    Args:
        language_code (str): The language code whose image folder should be deleted (e.g., 'ko').
        image_dir (Path): The directory where translated images are stored (e.g., './translated_images').
    """
    image_lang_dir = Path(image_dir) / language_code

    if not image_lang_dir.exists():
        logger.warning(
            f"Directory {image_lang_dir} does not exist. No images to delete."
        )
        return

    shutil.rmtree(image_lang_dir)
    logger.info(
        f"Deleted the image directory and all files for language: {language_code}"
    )


def delete_translated_markdown_files_by_language_code(
    language_code: str, translations_dir: Path, lang_subdir: Path | None = None
):
    """
    Delete the entire directory for the specified language code, including all its contents.

    Args:
        language_code (str): The language code whose folder should be deleted (e.g., 'ko').
        translations_dir (Path): The directory where translated markdown files are stored.
    """
    # Construct the path to the directory for the specific language
    language_dir = translations_dir / language_code
    if lang_subdir:
        language_dir = language_dir / Path(lang_subdir)

    if not language_dir.exists():
        logger.warning(
            f"Directory {language_dir} does not exist. No markdown files to delete."
        )
        return

    # Remove the entire directory and its contents
    shutil.rmtree(language_dir)
    logger.info(f"Deleted the directory and all files for language: {language_code}")
