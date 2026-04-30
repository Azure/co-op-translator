from __future__ import annotations

import logging
import os
import re
from pathlib import Path

logger = logging.getLogger(__name__)


def update_readme_translation_links(
    markdown_string: str,
    language_code: str,
    translations_dir: Path,
) -> str:
    """Update README translation navigation links in markdown content.

    Processes links that point to other language versions of README files
    (e.g., translations/ko/README.md, translations/es/README.md) and updates
    them to maintain correct relative paths in translated files.

    Args:
        markdown_string (str): The markdown content to process
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations

    Returns:
        str: Updated markdown content with corrected README translation links
    """
    logger.info("Updating README translation navigation links in the markdown file")

    translation_link_pattern = (
        r"(\[.*?\])\((?:\.?/)?translations/([a-zA-Z\-]+)/README\.md\)"
    )

    def replace_link(match):
        alt_text_with_brackets = match.group(1)
        other_language_code = match.group(2)
        logger.info(
            f"Found language code in link: {other_language_code} with alt text '{alt_text_with_brackets}'"
        )

        other_translated_md_path = (
            translations_dir / other_language_code / "README.md"
        ).resolve()
        logger.debug(
            f"Other translated markdown path (absolute): {other_translated_md_path}"
        )

        current_translated_md_path = (
            translations_dir / language_code / "README.md"
        ).resolve()
        current_md_dir = current_translated_md_path.parent
        logger.debug(f"Current markdown directory (current_md_dir): {current_md_dir}")

        try:
            relative_dir = os.path.relpath(
                other_translated_md_path.parent, current_md_dir
            ).replace(os.path.sep, "/")
            relative_path_to_translation = f"{relative_dir}/README.md"
            logger.info(
                f"Relative path to {other_language_code} translation: {relative_path_to_translation}"
            )

            new_translation_link_markup = (
                f"{alt_text_with_brackets}({relative_path_to_translation})"
            )
            logger.info(
                f"Updated translation link markdown: {new_translation_link_markup}"
            )
            return new_translation_link_markup
        except Exception as e:
            logger.error(
                f"Error updating translation links for {other_language_code}: {e}"
            )
            return match.group(0)

    markdown_string = re.sub(translation_link_pattern, replace_link, markdown_string)

    return markdown_string
