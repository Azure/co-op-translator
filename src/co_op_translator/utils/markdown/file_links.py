from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from urllib.parse import urlparse

from co_op_translator.config.constants import (
    SUPPORTED_IMAGE_EXTENSIONS,
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.common.file_utils import get_filename_and_extension

logger = logging.getLogger(__name__)


def update_untranslated_file_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
    use_translated_notebook: bool = True,
) -> str:
    """Update links to untranslated files to point to original source files.

    Processes links to files that are not translated (videos, documents, PDFs, etc.)
    and updates their paths to maintain correct relative links from translated markdown
    files back to the original source files.

    Skips:
    - Web URLs (http, https, mailto)
    - Image files (handled by update_image_links)
    - Markdown files (always translated)
    - Notebook files (if use_translated_notebook=True, they are translated; if False, processed here)

    Args:
        markdown_string (str): The markdown content to process
        md_file_path (Path): Path to the markdown file being processed
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations
        root_dir (Path): Root directory of the project
        use_translated_notebook (bool): Whether to use translated notebooks (False = process notebook links here)

    Returns:
        str: Updated markdown content with corrected untranslated file links
    """
    file_pattern = r"\[(.*?)\]\((.*?)\)"
    file_matches = re.findall(file_pattern, markdown_string)

    for alt_text, link in file_matches:
        parsed_url = urlparse(link)
        path = parsed_url.path

        # Keep same-document links untouched. Some LLMs occasionally emit
        # empty/current-page links while preserving TOCs; treating those as
        # files rewrites them to the source directory path.
        if path in ("", ".", "./") or (
            path == "/" and (parsed_url.fragment or parsed_url.query)
        ):
            logger.info(f"Skipping same-document link {link}")
            continue

        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.info(f"Skipped {link} as it is an email or web URL")
            continue

        original_filename, file_ext = get_filename_and_extension(path)

        if file_ext in SUPPORTED_IMAGE_EXTENSIONS:
            logger.info(f"Skipping image file {link}")
            continue

        if file_ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            logger.info(f"Skipping markdown file {link}")
            continue

        if file_ext in SUPPORTED_NOTEBOOK_EXTENSIONS and use_translated_notebook:
            logger.info(f"Skipping notebook file {link}")
            continue

        logger.info(f"Processing untranslated file link {link}")
        try:
            translated_md_dir = (
                translations_dir
                / language_code
                / md_file_path.relative_to(root_dir).parent
            )
            original_linked_file_path = (md_file_path.parent / path).resolve()

            updated_link = os.path.relpath(
                original_linked_file_path, translated_md_dir
            ).replace(os.path.sep, "/")

            old_file_markup = f"[{alt_text}]({link})"
            new_file_markup = f"[{alt_text}]({updated_link})"
            markdown_string = markdown_string.replace(old_file_markup, new_file_markup)

            logger.info(f"Updated untranslated file link: {new_file_markup}")

        except Exception as e:
            logger.error(f"Error processing untranslated file link {link}: {e}")
            continue

    return markdown_string
