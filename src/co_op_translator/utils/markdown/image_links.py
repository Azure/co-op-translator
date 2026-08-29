from __future__ import annotations

import logging
import os
from pathlib import Path
from urllib.parse import urlparse

from co_op_translator.config.constants import SUPPORTED_IMAGE_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    generate_translated_filename,
    get_actual_image_path,
    get_filename_and_extension,
)
from co_op_translator.utils.markdown.link_placeholders import (
    markdown_image_destination_spans,
)
from co_op_translator.utils.markdown.url_paths import replace_url_path

logger = logging.getLogger(__name__)


def get_translated_markdown_dir(
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
    lang_subdir: Path | None = None,
    target_path: Path | None = None,
) -> Path:
    """Return the directory containing the translated markdown file."""
    if target_path is not None:
        return Path(target_path).parent.resolve()

    language_root = translations_dir / language_code
    if lang_subdir:
        language_root = language_root / Path(lang_subdir)

    try:
        _ = md_file_path.relative_to(language_root)
        return md_file_path.parent.resolve()
    except Exception:
        return (language_root / md_file_path.relative_to(root_dir).parent).resolve()


def build_translated_image_link(
    path: str,
    md_file_path: Path,
    language_code: str,
    translated_md_dir: Path,
    translated_images_dir: Path,
    root_dir: Path,
) -> str:
    """Build a translated image link relative to the translated markdown file."""
    base_names = {
        translated_images_dir.name,
        "translated_images",
        "translated_images_fast",
    }
    parts = path.split("/")
    rel_path = os.path.relpath(translated_images_dir.resolve(), translated_md_dir)

    if len(parts) >= 3 and parts[-3] in base_names and parts[-2] == language_code:
        return os.path.join(rel_path, language_code, parts[-1]).replace(
            os.path.sep, "/"
        )

    if path.startswith("/"):
        actual_image_path = get_actual_image_path(path, md_file_path, root_dir)
    else:
        actual_image_path = get_actual_image_path(path, md_file_path)

    new_filename = generate_translated_filename(
        actual_image_path, language_code, root_dir
    )
    return os.path.join(rel_path, language_code, new_filename).replace(os.path.sep, "/")


def update_image_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    translated_images_dir: Path,
    root_dir: Path,
    use_translated_images: bool = True,
    target_path: Path | None = None,
) -> str:
    """
    Update image links in markdown content based on mode and Azure AI Service availability.

    Args:
        markdown_string (str): The markdown content to process
        md_file_path (Path): Path to the markdown file being processed
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations
        translated_images_dir (Path): Directory containing translated images
        root_dir (Path): Root directory of the project
        use_translated_images (bool): Whether to use translated images (False = use original images)

    Returns:
        str: Updated markdown content with modified image links
    """
    if use_translated_images:
        logger.info("Using translated image links")
    else:
        logger.info("Using original image links")

    replacements: list[tuple[int, int, str]] = []
    for start, end in markdown_image_destination_spans(markdown_string):
        link = markdown_string[start:end]
        parsed_url = urlparse(link)
        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.info(f"Skipped {link} as it is an email or web URL")
            continue

        path = parsed_url.path
        original_filename, file_ext = get_filename_and_extension(path)

        if file_ext in SUPPORTED_IMAGE_EXTENSIONS:
            logger.info(f"Processing image file {link}")

            try:
                # We'll resolve actual_image_path later based on the path type
                # Target translated markdown directory structure: translations/<lang>/<relative_path_to_parent>
                # The translated file will be saved at: translations_dir / language_code / (md_file_path relative to root_dir)
                # Its directory is:
                translated_md_dir = get_translated_markdown_dir(
                    md_file_path,
                    language_code,
                    translations_dir,
                    root_dir,
                    target_path=target_path,
                )

                if not use_translated_images:
                    # Link to original image when using original images
                    # For root-relative paths (starting with '/'), keep them unchanged
                    if path.startswith("/"):
                        logger.info(
                            f"Root-relative path detected in original images mode: {path}"
                        )
                        # Keep the original root-relative path as is
                        updated_link = path
                        logger.info(
                            f"Keeping original root-relative path: {updated_link}"
                        )
                    else:
                        # Handle regular relative paths
                        original_linked_file_path = (
                            md_file_path.parent / path
                        ).resolve()
                        updated_link = os.path.relpath(
                            original_linked_file_path, translated_md_dir
                        ).replace(os.path.sep, "/")
                        logger.info(f"Using original image link: {updated_link}")
                else:
                    try:
                        updated_link = build_translated_image_link(
                            path,
                            md_file_path,
                            language_code,
                            translated_md_dir,
                            translated_images_dir,
                            root_dir,
                        )
                        logger.info(f"Using translated image link: {updated_link}")
                    except Exception as e:
                        logger.error(f"Error processing image path {path}: {e}")
                        # Fallback to original path if there's an error
                        updated_link = path
                        logger.warning(f"Falling back to original path: {updated_link}")

                replacements.append(
                    (start, end, replace_url_path(parsed_url, updated_link))
                )

            except Exception as e:
                logger.error(f"Error processing image {link}: {e}")
                logger.info(f"Skipping image {link}")
                continue

    for start, end, updated_link in reversed(replacements):
        markdown_string = markdown_string[:start] + updated_link + markdown_string[end:]

    return markdown_string
