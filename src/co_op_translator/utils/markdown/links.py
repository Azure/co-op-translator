from __future__ import annotations

import logging
from pathlib import Path

from co_op_translator.utils.markdown.file_links import update_untranslated_file_links
from co_op_translator.utils.markdown.image_links import update_image_links
from co_op_translator.utils.markdown.readme_links import update_readme_translation_links

logger = logging.getLogger(__name__)


def update_links(
    md_file_path: Path,
    markdown_string: str,
    language_code: str,
    root_dir: Path,
    translations_dir: Path | None = None,
    translated_images_dir: Path | None = None,
    translation_types: list[str] = None,
    target_path: Path | None = None,
    use_translated_markdown_links: bool | None = None,
) -> str:
    logger.info("Updating links in the markdown file")

    # Default translation types if not specified
    if translation_types is None:
        translation_types = ["markdown", "notebook", "images"]

    if translations_dir is None:
        translations_dir = root_dir / "translations"
    if translated_images_dir is None:
        translated_images_dir = root_dir / "translated_images"
    if use_translated_markdown_links is None:
        use_translated_markdown_links = "markdown" in translation_types

    # Update image links
    markdown_string = update_image_links(
        markdown_string,
        md_file_path,
        language_code,
        translations_dir,
        translated_images_dir,
        root_dir,
        use_translated_images="images" in translation_types,
        target_path=target_path,
    )

    # Update links to untranslated files (videos, docs, etc.) to point to original files
    markdown_string = update_untranslated_file_links(
        markdown_string,
        md_file_path,
        language_code,
        translations_dir,
        root_dir,
        use_translated_notebook="notebook" in translation_types,
        use_translated_markdown=use_translated_markdown_links,
        target_path=target_path,
    )

    # Update README translation navigation links (language switcher links)
    markdown_string = update_readme_translation_links(
        markdown_string, language_code, translations_dir
    )

    return markdown_string
