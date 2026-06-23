"""Frontmatter parsing and translation utilities.

This module provides deterministic frontmatter handling by:
1. Parsing YAML frontmatter from markdown content
2. Filtering fields based on preserve/translate configuration
3. Merging translated fields back with preserved fields
4. Reconstructing markdown with updated frontmatter

This approach ensures that technical fields (slug, id, order, etc.) are NEVER
accidentally translated by the LLM, providing 100% stability for metadata.
"""

import re
import os
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from urllib.parse import urlparse
import yaml
from importlib import resources
from co_op_translator.utils.markdown.image_links import (
    build_translated_image_link,
    get_translated_markdown_dir,
)

logger = logging.getLogger(__name__)


class FrontmatterConfig:
    """Manages frontmatter field translation configuration."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initialize frontmatter configuration.

        Args:
            config_path: Optional path to custom configuration file.
                        If None, uses the default bundled configuration.
        """
        self.preserve_fields: List[str] = []
        self.translate_fields: List[str] = []
        self._load_config(config_path)

    def _load_config(self, config_path: Optional[Path] = None) -> None:
        """Load frontmatter configuration from YAML file.

        Args:
            config_path: Optional path to custom configuration file
        """
        try:
            if config_path and config_path.exists():
                with open(config_path, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
            else:
                # Load default bundled configuration
                with (
                    resources.files("co_op_translator.config")
                    .joinpath("frontmatter_config.yml")
                    .open("r", encoding="utf-8") as f
                ):
                    config = yaml.safe_load(f)

            if config and "frontmatter" in config:
                fm_config = config["frontmatter"]
                self.preserve_fields = fm_config.get("preserve", [])
                self.translate_fields = fm_config.get("translate", [])
                logger.debug(
                    f"Loaded frontmatter config: {len(self.preserve_fields)} preserve fields, "
                    f"{len(self.translate_fields)} translate fields"
                )
            else:
                logger.warning(
                    "Frontmatter configuration is empty or invalid. Using empty field lists."
                )
        except Exception as e:
            logger.warning(
                f"Failed to load frontmatter configuration: {e}. Using empty field lists."
            )

    def should_preserve(self, field_name: str) -> bool:
        """Check if a field should be preserved (not translated).

        Args:
            field_name: Name of the frontmatter field

        Returns:
            True if field should be preserved, False otherwise
        """
        return field_name in self.preserve_fields

    def should_translate(self, field_name: str) -> bool:
        """Check if a field should be translated.

        Args:
            field_name: Name of the frontmatter field

        Returns:
            True if field should be translated, False otherwise
        """
        return field_name in self.translate_fields


class FrontmatterParser:
    """Parses and reconstructs YAML frontmatter in markdown documents."""

    # Regex pattern for YAML frontmatter (must be at the start of the document)
    FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

    def __init__(self, config: Optional[FrontmatterConfig] = None):
        """Initialize frontmatter parser.

        Args:
            config: Optional frontmatter configuration. If None, uses default config.
        """
        self.config = config or FrontmatterConfig()

    def extract_frontmatter(self, content: str) -> Tuple[Optional[Dict[str, Any]], str]:
        """Extract YAML frontmatter from markdown content.

        Args:
            content: Full markdown document content

        Returns:
            Tuple of (frontmatter_dict, body_content)
            - frontmatter_dict: Parsed YAML frontmatter as dict, or None if not found
            - body_content: Markdown content without frontmatter
        """
        match = self.FRONTMATTER_PATTERN.match(content)
        if not match:
            return None, content

        frontmatter_yaml = match.group(1)
        body = content[match.end() :]

        try:
            frontmatter = yaml.safe_load(frontmatter_yaml)
            if not isinstance(frontmatter, dict):
                logger.warning(
                    f"Frontmatter is not a dictionary: {type(frontmatter)}. Treating as no frontmatter."
                )
                return None, content
            return frontmatter, body
        except yaml.YAMLError as e:
            logger.warning(
                f"Failed to parse frontmatter YAML: {e}. Treating as no frontmatter."
            )
            return None, content

    def split_fields(
        self, frontmatter: Dict[str, Any]
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Split frontmatter fields into preserve and translate groups.

        Args:
            frontmatter: Full frontmatter dictionary

        Returns:
            Tuple of (preserve_fields, translate_fields)
            - preserve_fields: Fields that should not be translated
            - translate_fields: Fields that should be translated
        """
        preserve = {}
        translate = {}

        for key, value in frontmatter.items():
            if self.config.should_preserve(key):
                preserve[key] = value
            elif self.config.should_translate(key):
                translate[key] = value
            else:
                # Unknown field: preserve by default for safety
                logger.debug(
                    f"Unknown frontmatter field '{key}' not in config. Preserving by default."
                )
                preserve[key] = value

        return preserve, translate

    def merge_fields(
        self, preserve_fields: Dict[str, Any], translated_fields: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Merge preserved and translated fields back into a single frontmatter dict.

        Args:
            preserve_fields: Fields that were preserved (not translated)
            translated_fields: Fields that were translated

        Returns:
            Merged frontmatter dictionary
        """
        # Start with preserved fields, then add translated fields
        # This ensures preserved fields take precedence in case of conflicts
        merged = preserve_fields.copy()
        merged.update(translated_fields)
        return merged

    def reconstruct_content(
        self, frontmatter: Optional[Dict[str, Any]], body: str
    ) -> str:
        """Reconstruct markdown content with frontmatter.

        Args:
            frontmatter: Frontmatter dictionary (or None if no frontmatter)
            body: Markdown body content

        Returns:
            Full markdown content with frontmatter
        """
        if not frontmatter:
            return body

        # Serialize frontmatter to YAML
        try:
            frontmatter_yaml = yaml.dump(
                frontmatter,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
            )
            return f"---\n{frontmatter_yaml}---\n{body}"
        except Exception as e:
            logger.error(
                f"Failed to serialize frontmatter to YAML: {e}. Returning body only."
            )
            return body

    def extract_translatable_fields_as_markdown(
        self, translate_fields: Dict[str, Any]
    ) -> str:
        """Convert translatable fields to a markdown format for LLM translation.

        This creates a simple markdown representation of the fields that the LLM
        can translate naturally.

        Args:
            translate_fields: Dictionary of fields to translate

        Returns:
            Markdown-formatted string of translatable fields
        """
        if not translate_fields:
            return ""

        lines = []
        for key, value in translate_fields.items():
            if isinstance(value, str):
                # Simple string field
                lines.append(f"**{key}**: {value}")
            elif isinstance(value, list):
                # List field (e.g., multiple descriptions)
                lines.append(f"**{key}**:")
                for item in value:
                    if isinstance(item, str):
                        lines.append(f"- {item}")
            elif isinstance(value, dict):
                # Nested dict (rare, but handle gracefully)
                lines.append(f"**{key}**: {yaml.dump(value, allow_unicode=True)}")
            else:
                # Other types: convert to string
                lines.append(f"**{key}**: {str(value)}")

        return "\n".join(lines)

    def parse_translated_fields_from_markdown(
        self, translated_markdown: str, original_fields: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Parse translated fields from LLM-generated markdown.

        This attempts to extract the translated values from the markdown format
        created by extract_translatable_fields_as_markdown.

        Args:
            translated_markdown: LLM-translated markdown content
            original_fields: Original translatable fields (for structure reference)

        Returns:
            Dictionary of translated fields
        """
        translated = {}

        # Pattern to match field lines: **field_name**: value
        field_pattern = re.compile(r"^\*\*(.+?)\*\*:\s*(.*)$", re.MULTILINE)

        for match in field_pattern.finditer(translated_markdown):
            field_name = match.group(1).strip()
            field_value = match.group(2).strip()

            if field_name in original_fields:
                # Preserve the original type
                original_value = original_fields[field_name]
                if isinstance(original_value, str):
                    translated[field_name] = field_value
                elif isinstance(original_value, list):
                    # For lists, we need to extract list items
                    # This is a simplified approach; may need enhancement
                    translated[field_name] = [field_value]
                else:
                    # For other types, use string representation
                    translated[field_name] = field_value

        return translated


class QuickLinksFrontmatterParser(FrontmatterParser):
    """Frontmatter parser that promotes quickLinks nested strings for translation."""

    QUICKLINKS_FIELD_NAME = "quickLinks"
    QUICKLINKS_TRANSLATABLE_FIELDS = ("title", "description")
    QUICKLINKS_KEY_PATTERN = re.compile(r"^quickLinks\[(\d+)\]\.(\w+)$")

    def split_fields(
        self, frontmatter: Dict[str, Any]
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        preserve, translate = super().split_fields(frontmatter)

        quicklinks = frontmatter.get(self.QUICKLINKS_FIELD_NAME)
        if isinstance(quicklinks, list):
            preserve[self.QUICKLINKS_FIELD_NAME] = quicklinks
            translate.update(self._collect_quicklinks_translation_fields(quicklinks))

        return preserve, translate

    def merge_fields(
        self, preserve_fields: Dict[str, Any], translated_fields: Dict[str, Any]
    ) -> Dict[str, Any]:
        preserve_copy = dict(preserve_fields)
        translated_copy = dict(translated_fields)

        self._apply_nested_field_translations(preserve_copy, translated_copy)
        return super().merge_fields(preserve_copy, translated_copy)

    def _collect_quicklinks_translation_fields(
        self, quicklinks: List[Any]
    ) -> Dict[str, str]:
        pseudo_fields: Dict[str, str] = {}
        for index, item in enumerate(quicklinks):
            if not isinstance(item, dict):
                continue

            for field in self.QUICKLINKS_TRANSLATABLE_FIELDS:
                value = item.get(field)
                if isinstance(value, str):
                    pseudo_key = f"{self.QUICKLINKS_FIELD_NAME}[{index}].{field}"
                    pseudo_fields[pseudo_key] = value
        return pseudo_fields

    def _apply_nested_field_translations(
        self,
        preserve_fields: Dict[str, Any],
        translated_fields: Dict[str, Any],
    ) -> None:
        quicklinks = preserve_fields.get(self.QUICKLINKS_FIELD_NAME)
        if not isinstance(quicklinks, list):
            return

        keys_to_remove: List[str] = []
        for key, value in list(translated_fields.items()):
            match = self.QUICKLINKS_KEY_PATTERN.match(key)
            if not match:
                continue

            index = int(match.group(1))
            field_name = match.group(2)

            if field_name not in self.QUICKLINKS_TRANSLATABLE_FIELDS:
                keys_to_remove.append(key)
                continue

            if 0 <= index < len(quicklinks):
                item = quicklinks[index]
                if isinstance(item, dict):
                    item[field_name] = value
            keys_to_remove.append(key)

        for key in keys_to_remove:
            translated_fields.pop(key, None)


# Singleton instance for global use
_default_parser: Optional[FrontmatterParser] = None


def get_frontmatter_parser(
    config_path: Optional[Path] = None,
) -> FrontmatterParser:
    """Get or create the default frontmatter parser instance.

    Args:
        config_path: Optional path to custom configuration file

    Returns:
        FrontmatterParser instance
    """
    global _default_parser
    if _default_parser is None or config_path is not None:
        _default_parser = QuickLinksFrontmatterParser(FrontmatterConfig(config_path))
    return _default_parser


def ensure_quicklinks_frontmatter_parser() -> QuickLinksFrontmatterParser:
    """Ensure the global parser supports translating quickLinks nested fields."""

    global _default_parser

    parser = get_frontmatter_parser()
    if isinstance(parser, QuickLinksFrontmatterParser):
        return parser

    config = getattr(parser, "config", None)
    _default_parser = QuickLinksFrontmatterParser(config=config)
    return _default_parser


# List of frontmatter fields that typically contain file paths or URLs
PATH_FIELDS = [
    "image",
    "cover",
    "thumbnail",
    "featured_image",
    "og_image",
    "twitter_image",
    "icon",
    "canonical_url",
    "url",
    "permalink",
]


def adjust_frontmatter_links(
    frontmatter: Dict[str, Any],
    md_file_path: Path,
    language_code: str,
    root_dir: Path,
    translations_dir: Path,
    translated_images_dir: Path,
    translation_types: List[str],
    lang_subdir: Path | None = None,
    target_path: Path | None = None,
) -> Dict[str, Any]:
    """Adjust file paths in frontmatter fields to point to correct locations.

    This follows the same logic as markdown-only mode: links point to original
    files, with relative paths adjusted based on the translated file's location.

    Args:
        frontmatter: Frontmatter dictionary with potential file paths
        md_file_path: Path to the original markdown file
        language_code: Target language code
        root_dir: Root directory of the project
        translations_dir: Directory containing translations
        translated_images_dir: Directory containing translated images
        translation_types: List of file types being translated

    Returns:
        Frontmatter dictionary with adjusted paths
    """
    if not frontmatter:
        return frontmatter

    adjusted = frontmatter.copy()
    use_translated_images = "images" in translation_types

    # Calculate translated markdown directory
    try:
        translated_md_dir = get_translated_markdown_dir(
            md_file_path,
            language_code,
            translations_dir,
            root_dir,
            lang_subdir=lang_subdir,
            target_path=target_path,
        )
    except ValueError:
        logger.warning(
            f"Cannot calculate relative path for '{md_file_path}' from root '{root_dir}'. "
            f"Skipping frontmatter link adjustment."
        )
        return adjusted

    for field in PATH_FIELDS:
        if field not in adjusted:
            continue

        value = adjusted[field]
        if not isinstance(value, str):
            continue

        # Skip web URLs and email addresses
        parsed_url = urlparse(value)
        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in value
            or value.endswith((".com", ".org", ".net"))
        ):
            logger.debug(f"Skipping web URL in frontmatter field '{field}': {value}")
            continue

        path = parsed_url.path
        if not path:
            continue

        # Determine if this is an image field
        is_image_field = any(
            img_keyword in field.lower()
            for img_keyword in ["image", "cover", "thumbnail", "icon"]
        )

        try:
            if path.startswith("/"):
                # Root-relative path
                if is_image_field and use_translated_images:
                    # For images with translation enabled, point to translated images
                    # This requires resolving the actual image path
                    actual_image_path = root_dir / path.lstrip("/")
                    if actual_image_path.exists():
                        adjusted[field] = build_translated_image_link(
                            path,
                            md_file_path,
                            language_code,
                            translated_md_dir,
                            translated_images_dir,
                            root_dir,
                        )
                        logger.debug(
                            f"Adjusted root-relative image path in '{field}': {value} -> {adjusted[field]}"
                        )
                    else:
                        # Keep original if file doesn't exist
                        logger.debug(
                            f"Root-relative path not found, keeping original in '{field}': {value}"
                        )
                else:
                    # For non-images or when not using translated images, keep root-relative path
                    logger.debug(f"Keeping root-relative path in '{field}': {value}")
            else:
                # Regular relative path
                original_linked_file_path = (md_file_path.parent / path).resolve()

                if is_image_field and use_translated_images:
                    # Point to translated image
                    if original_linked_file_path.exists():
                        adjusted[field] = build_translated_image_link(
                            path,
                            md_file_path,
                            language_code,
                            translated_md_dir,
                            translated_images_dir,
                            root_dir,
                        )
                        logger.debug(
                            f"Adjusted relative image path in '{field}': {value} -> {adjusted[field]}"
                        )
                    else:
                        # Fallback to relative path to original
                        adjusted[field] = os.path.relpath(
                            original_linked_file_path, translated_md_dir
                        ).replace(os.path.sep, "/")
                        logger.debug(
                            f"Image not found, using relative path to original in '{field}': {adjusted[field]}"
                        )
                else:
                    # Point to original file (markdown-only mode behavior)
                    adjusted[field] = os.path.relpath(
                        original_linked_file_path, translated_md_dir
                    ).replace(os.path.sep, "/")
                    logger.debug(
                        f"Adjusted relative path to original in '{field}': {value} -> {adjusted[field]}"
                    )

        except Exception as e:
            logger.warning(
                f"Failed to adjust path in frontmatter field '{field}': {value}. Error: {e}. "
                f"Keeping original value."
            )
            # Keep original value on error

    return adjusted
