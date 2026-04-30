from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from urllib.parse import urlparse

from co_op_translator.config.constants import SUPPORTED_IMAGE_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    generate_translated_filename,
    get_actual_image_path,
    get_filename_and_extension,
)

logger = logging.getLogger(__name__)


def get_translated_markdown_dir(
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
    lang_subdir: Path | None = None,
) -> Path:
    """Return the directory containing the translated markdown file."""
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
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    image_matches = re.findall(image_pattern, markdown_string)

    if use_translated_images:
        logger.info("Using translated image links")
    else:
        logger.info("Using original image links")

    for alt_text, link in image_matches:
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

                old_image_markup = f"![{alt_text}]({link})"
                new_image_markup = f"![{alt_text}]({updated_link})"
                markdown_string = markdown_string.replace(
                    old_image_markup, new_image_markup
                )

            except Exception as e:
                logger.error(f"Error processing image {link}: {e}")
                logger.info(f"Skipping image {link}")
                continue

    # Also update HTML <img> tags inside markdown
    html_img_pattern = re.compile(
        r"<img\s+[^>]*src=([\"\'])(.*?)\1[^>]*>", re.IGNORECASE
    )

    def _replace_img_src(match: re.Match) -> str:
        src = match.group(2)
        parsed_url = urlparse(src)
        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in src
            or src.endswith((".com", ".org", ".net"))
        ):
            return match.group(0)

        path = parsed_url.path
        _, file_ext = get_filename_and_extension(path)
        if file_ext not in SUPPORTED_IMAGE_EXTENSIONS:
            return match.group(0)

        try:
            translated_md_dir = get_translated_markdown_dir(
                md_file_path,
                language_code,
                translations_dir,
                root_dir,
            )

            if not use_translated_images:
                # Link to original image when using original images
                if path.startswith("/"):
                    updated_src = path
                else:
                    original_linked_file_path = (md_file_path.parent / path).resolve()
                    updated_src = os.path.relpath(
                        original_linked_file_path, translated_md_dir
                    ).replace(os.path.sep, "/")
            else:
                updated_src = build_translated_image_link(
                    path,
                    md_file_path,
                    language_code,
                    translated_md_dir,
                    translated_images_dir,
                    root_dir,
                )
        except Exception as e:
            logger.error(f"Error processing HTML <img> path {src}: {e}")
            updated_src = src

        # Replace only the src value inside this tag while preserving other attributes
        full_tag = match.group(0)
        rel_start = match.start(2) - match.start(0)
        rel_end = match.end(2) - match.start(0)
        return full_tag[:rel_start] + updated_src + full_tag[rel_end:]

    markdown_string = html_img_pattern.sub(_replace_img_src, markdown_string)

    return markdown_string
