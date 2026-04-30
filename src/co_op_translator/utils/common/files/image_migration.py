from __future__ import annotations

import logging
import re
from pathlib import Path

from .paths import HASH_PREFIX_LENGTH

logger = logging.getLogger(__name__)


def migrate_translated_image_filenames(
    image_dir: Path, language_codes: list[str]
) -> dict[str, str]:
    """Migrate translated images to language subdirectories with 16-hex hash prefixes.

    This performs two migrations:
    1) Flattened files named like base.hash.lang.ext → move to image_dir/lang/base.hash.ext
       and remove the language segment from the filename.
    2) Normalize hash segment to 16-hex prefix when legacy lengths are found (64/24/20).

    Returns a mapping from old basenames to new relative paths including the language
    directory (e.g., {"diagram.abcdef0123456789.ko.png": "ko/diagram.abcdef0123456789.png"})
    for updating markdown/notebook links.
    """

    image_dir = Path(image_dir)
    if not image_dir.exists():
        return {}

    rename_map: dict[str, str] = {}

    try:
        image_files = sorted(image_dir.rglob("*"))
    except Exception:
        return {}

    from co_op_translator.utils.common.lang_utils import normalize_language_code

    for image_file in image_files:
        if not image_file.is_file():
            continue
        if image_file.suffix.lower() not in [
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
        ]:
            continue

        rel_parts = ()
        try:
            rel_parts = image_file.relative_to(image_dir).parts
        except Exception:
            rel_parts = ()

        parts = image_file.name.split(".")
        if len(parts) < 3:
            continue

        extension = parts[-1]

        # Detect language either from directory or from legacy filename
        under_lang_dir = False
        lang_code: str | None = None
        if len(rel_parts) >= 2:
            parent_lang = rel_parts[0]
            normalized_parent = normalize_language_code(parent_lang)
            if normalized_parent in language_codes:
                under_lang_dir = True
                lang_code = normalized_parent

        # Legacy filename pattern includes trailing language segment
        has_legacy_lang_in_name = (
            len(parts) >= 4 and normalize_language_code(parts[-2]) in language_codes
        )

        if not under_lang_dir and not has_legacy_lang_in_name:
            # Cannot determine language; skip conservatively
            continue

        if has_legacy_lang_in_name and lang_code is None:
            lang_code = normalize_language_code(parts[-2])

        if lang_code not in language_codes:
            # Skip unsupported languages
            continue

        # Determine raw hash and base name depending on pattern
        if has_legacy_lang_in_name:
            raw_hash = parts[-3]
            base_name = ".".join(parts[:-3])
        else:
            raw_hash = parts[-2]
            base_name = ".".join(parts[:-2])

        # Validate and normalize hash
        if not re.fullmatch(r"[0-9a-f]+", raw_hash or ""):
            continue
        seg_len = len(raw_hash)
        if seg_len not in (HASH_PREFIX_LENGTH, 64, 24, 20):
            continue
        new_prefix = (
            raw_hash if seg_len == HASH_PREFIX_LENGTH else raw_hash[:HASH_PREFIX_LENGTH]
        )

        new_basename = f"{base_name}.{new_prefix}.{extension}"
        target_dir = image_dir / lang_code
        target_dir.mkdir(parents=True, exist_ok=True)
        new_path = target_dir / new_basename

        # Compute textual mapping entries for link migration
        old_basename = image_file.name
        new_rel_for_links = f"{lang_code}/{new_basename}"
        # Prefer most specific replacements first (full paths), then less specific
        full_rel = None
        try:
            full_rel = str(image_file.relative_to(image_dir)).replace("\\", "/")
        except Exception:
            full_rel = old_basename

        # If path is unchanged (already in place), consider only renaming to drop legacy lang
        if image_file.resolve() == new_path.resolve():
            # If only the hash length needs normalization or the name still contains lang segment under lang dir
            if has_legacy_lang_in_name:
                # Under lang dir with legacy language in name → rename to drop it
                try:
                    image_file.rename(new_path)
                    rename_map[old_basename] = new_rel_for_links
                except Exception:
                    pass
            else:
                # Already correct location and naming; nothing to do
                continue
        else:
            # Move/rename to the new path
            if new_path.exists():
                # If target exists, remove the source to dedupe
                try:
                    image_file.unlink()
                except Exception:
                    pass
            else:
                try:
                    image_file.rename(new_path)
                except Exception:
                    continue
            # Insert mappings in order: with base image dir/fast prefixes, then lang-prefixed basename, then plain basename
            base_dir_name = image_dir.name
            # Current configured base image directory
            rename_map[f"{base_dir_name}/{full_rel}"] = (
                f"{base_dir_name}/{new_rel_for_links}"
            )
            # Backward compatibility: previous defaults that may appear in existing content
            if base_dir_name != "translated_images":
                rename_map[f"translated_images/{full_rel}"] = (
                    f"{base_dir_name}/{new_rel_for_links}"
                )
            # Fast directory historical default
            rename_map[f"translated_images_fast/{full_rel}"] = (
                f"{base_dir_name}/{new_rel_for_links}"
            )
            # If the old path already had a language directory, provide that form too
            if lang_code and not full_rel.startswith(lang_code + "/"):
                rename_map[f"{lang_code}/{old_basename}"] = (
                    f"{lang_code}/{new_basename}"
                )
            rename_map[old_basename] = new_rel_for_links

    return rename_map


def migrate_images_to_webp(
    image_dir: Path, language_codes: list[str] | None = None
) -> dict[str, str]:
    """Migrate existing translated images (PNG, JPG, JPEG) to WebP format.

    This function:
    1. Finds all non-WebP images in the translated_images directory
    2. Converts them to WebP format with optimal compression (quality=90)
    3. Updates the metadata file to reflect the new filenames
    4. Deletes the original PNG/JPG files after successful conversion

    Returns a mapping from old filenames to new WebP filenames for updating
    markdown/notebook links (e.g., {"image.abc123.png": "image.abc123.webp"}).

    Args:
        image_dir: Path to the translated_images directory

    Returns:
        dict mapping old relative paths to new WebP paths
    """
    from PIL import Image
    import json

    image_dir = Path(image_dir)
    if not image_dir.exists():
        logger.info(f"Image directory does not exist: {image_dir}")
        return {}

    rename_map: dict[str, str] = {}
    converted_count = 0
    failed_count = 0
    skipped_count = 0

    # Process each language subdirectory (optionally scoped to specific languages)
    for lang_dir in image_dir.iterdir():
        if not lang_dir.is_dir():
            continue
        if language_codes is not None and lang_dir.name not in language_codes:
            continue

        metadata_file = lang_dir / ".co-op-translator.json"
        metadata = {}
        if metadata_file.exists():
            try:
                metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
            except Exception as e:
                logger.warning(f"Failed to load metadata from {metadata_file}: {e}")

        updated_metadata = {}

        for image_file in sorted(lang_dir.iterdir()):
            if not image_file.is_file():
                continue

            suffix = image_file.suffix.lower()

            # Skip non-image files and already converted WebP files
            if suffix == ".webp":
                # Keep existing WebP metadata
                key = image_file.name
                if key in metadata:
                    updated_metadata[key] = metadata[key]
                skipped_count += 1
                continue

            if suffix not in {".png", ".jpg", ".jpeg"}:
                continue

            # Generate new WebP filename
            new_name = image_file.stem + ".webp"
            new_path = lang_dir / new_name

            try:
                # Open and convert to WebP
                with Image.open(image_file) as img:
                    # Preserve RGBA mode for transparency
                    if img.mode in ("RGBA", "LA") or (
                        img.mode == "P" and "transparency" in img.info
                    ):
                        img = img.convert("RGBA")
                    else:
                        img = img.convert("RGB")

                    # Save as WebP with high quality
                    img.save(new_path, format="WEBP", quality=90, method=6)

                # Update metadata: copy old entry to new key
                old_key = image_file.name
                if old_key in metadata:
                    updated_metadata[new_name] = metadata[old_key]
                else:
                    # If no metadata exists, we can't preserve it
                    logger.debug(f"No metadata found for {old_key}")

                # Add to rename map for link migration
                old_rel = f"{lang_dir.name}/{image_file.name}"
                new_rel = f"{lang_dir.name}/{new_name}"
                rename_map[old_rel] = new_rel
                rename_map[image_file.name] = new_name

                # Delete the original file after successful conversion
                image_file.unlink()
                converted_count += 1
                logger.debug(f"Converted {image_file.name} -> {new_name}")

            except Exception as e:
                logger.error(f"Failed to convert {image_file}: {e}")
                failed_count += 1
                # Keep original metadata if conversion failed
                old_key = image_file.name
                if old_key in metadata:
                    updated_metadata[old_key] = metadata[old_key]

        # Write updated metadata
        if updated_metadata:
            try:
                metadata_file.write_text(
                    json.dumps(updated_metadata, indent=2, ensure_ascii=False),
                    encoding="utf-8",
                )
            except Exception as e:
                logger.error(f"Failed to update metadata file {metadata_file}: {e}")

    logger.info(
        f"WebP migration complete: {converted_count} converted, "
        f"{skipped_count} already WebP, {failed_count} failed"
    )

    return rename_map
