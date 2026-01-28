"""
This module contains utility functions for handling file operations.
Functions include reading from files, writing to files, and handling empty document scenarios.
"""

import hashlib
from pathlib import Path
import re

LANG_TABLE_START = "<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->"
LANG_TABLE_END = "<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->"
OTHER_COURSES_START = "<!-- CO-OP TRANSLATOR OTHER COURSES START -->"
OTHER_COURSES_END = "<!-- CO-OP TRANSLATOR OTHER COURSES END -->"


def _replace_between_markers_generic(
    readme_text: str, new_block: str, start_marker: str, end_marker: str
) -> str:
    """
    Replace content between the provided start/end markers with the new block.
    Markers are included in the replacement. If markers are missing, returns original text.
    """
    # Case-insensitive detection of markers so users can vary casing
    lower_text = readme_text.lower()
    start_idx = lower_text.find(start_marker.lower())
    end_idx = lower_text.find(end_marker.lower())
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        return readme_text

    # Expand end to include the end marker line completely
    end_idx_inclusive = end_idx + len(end_marker)

    before = readme_text[:start_idx].rstrip()
    after = readme_text[end_idx_inclusive:].lstrip()

    # Ensure surrounding newlines for readability
    pieces = []
    if before:
        pieces.append(before)
    pieces.append(new_block.strip())
    if after:
        pieces.append(after)
    result = "\n\n".join(pieces)
    if readme_text.endswith("\n"):
        result = result.rstrip("\n") + "\n"
    else:
        result = result.rstrip("\n")
    return result


def replace_between_markers(readme_text: str, new_block: str) -> str:
    """
    Backward-compatible helper that replaces between the LANGUAGES TABLE markers.
    """
    return _replace_between_markers_generic(
        readme_text, new_block, LANG_TABLE_START, LANG_TABLE_END
    )


def load_languages_table_template() -> str:
    """Load the bundled languages table template markdown."""
    try:
        from importlib import resources

        with resources.open_text(
            "co_op_translator.templates", "languages_table.md", encoding="utf-8"
        ) as f:
            return f.read()
    except Exception:
        return ""


def load_other_courses_template() -> str:
    """Load the bundled other courses template markdown."""
    try:
        from importlib import resources

        with resources.open_text(
            "co_op_translator.templates", "other_courses.md", encoding="utf-8"
        ) as f:
            return f.read()
    except Exception:
        return ""


def update_readme_languages_table(
    readme_path: Path, repo_url: str | None = None
) -> bool:
    """
    Update README languages table between markers using bundled template.
    Optionally appends a 'Prefer to Clone Locally?' advisory block INSIDE the markers.

    If repo_url is provided, it will be used to personalize the snippet; otherwise
    the advisory will be shown with placeholder stars as given by the user.

    Returns True if updated, False otherwise.
    """
    if not readme_path.exists():
        return False
    original = readme_path.read_text(encoding="utf-8")
    template = load_languages_table_template()
    if not template:
        return False
    # Strip markdownlint directives from template to avoid injecting them into user README
    template = re.sub(
        r"^\s*<!--\s*markdownlint-disable[^>]*-->\s*\n?",
        "",
        template,
        flags=re.IGNORECASE,
    )

    # Build advisory block (with optional repo URL substitution)
    repo_url_value = (
        repo_url.strip() if isinstance(repo_url, str) and repo_url.strip() else None
    )
    repo_name_value: str | None = None
    if repo_url_value:
        try:
            tail = repo_url_value.rstrip("/").split("/")[-1]
            repo_name_value = tail[:-4] if tail.endswith(".git") else tail
        except Exception:
            repo_name_value = None

    advisory_repo_url = repo_url_value or "https://github.com/*****.git"
    advisory_repo_name = repo_name_value or "*****"

    advisory_block = (
        "> **Prefer to Clone Locally?**\n\n"
        "> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:\n"
        "> ```bash\n"
        f"> git clone --filter=blob:none --sparse {advisory_repo_url}\n"
        f"> cd {advisory_repo_name}\n"
        "> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'\n"
        "> ```\n"
        "> This gives you everything you need to complete the course with a much faster download."
    )

    # Insert advisory INSIDE the template's markers
    lower_t = template.lower()
    start_idx = lower_t.find(LANG_TABLE_START.lower())
    end_idx = lower_t.find(LANG_TABLE_END.lower())
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        return False

    inner_content = template[start_idx + len(LANG_TABLE_START) : end_idx].strip()
    combined_inner = (inner_content + "\n\n" + advisory_block).strip()
    new_block = f"{LANG_TABLE_START}\n{combined_inner}\n{LANG_TABLE_END}"

    updated = _replace_between_markers_generic(
        original, new_block, LANG_TABLE_START, LANG_TABLE_END
    )
    if updated != original:
        readme_path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def update_readme_other_courses(readme_path: Path) -> bool:
    """
    Update README 'Other courses' section between markers using bundled template.
    Returns True if updated, False otherwise.
    """
    if not readme_path.exists():
        return False
    original = readme_path.read_text(encoding="utf-8")
    template = load_other_courses_template()
    if not template:
        return False
    updated = _replace_between_markers_generic(
        original, template, OTHER_COURSES_START, OTHER_COURSES_END
    )
    if updated != original:
        readme_path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


import shutil
import os
import logging

logger = logging.getLogger(__name__)


# Fixed hash prefix length (in hex characters) for translated image filenames.
HASH_PREFIX_LENGTH = 16


# Using a fixed-length hash prefix; collision-aware selection logic removed.


def read_input_file(input_file: str | Path) -> str:
    """
    Read the content of an input file and return it as a stripped string.

    Args:
        input_file (str | Path): The path to the input file.

    Returns:
        str: The stripped content of the file.
    """
    input_file = Path(input_file)
    with input_file.open("r", encoding="utf-8") as file:
        return file.read().strip()


def handle_empty_document(input_file: str | Path, output_file: str | Path) -> None:
    """
    Copy the input file to the output location if the document is empty.

    Args:
        input_file (str | Path): The path to the input file.
        output_file (str | Path): The path to the output file.
    """
    input_file = Path(input_file)
    output_file = Path(output_file)
    shutil.copyfile(input_file, output_file)


def write_output_file(output_file: str | Path, results: list) -> None:
    """
    Write a list of results to the output file, each on a new line.

    Args:
        output_file (str | Path): The path to the output file.
        results (list): A list of strings to write to the file.
    """
    output_file = Path(output_file)
    with output_file.open("w", encoding="utf-8") as text_file:
        for result in results:
            text_file.write(result)
            text_file.write("\n")


def get_actual_image_path(
    image_relative_path: str | Path,
    markdown_file_path: str | Path,
    root_dir: Path = None,
) -> Path:
    """
    Given an image's relative path from the markdown file, return the actual file path
    by resolving the relative path against the markdown file's location or the project root.

    Args:
        image_relative_path (str | Path): The relative path of the image as found in the markdown file.
        markdown_file_path (str | Path): The path to the markdown file.
        root_dir (Path, optional): The root directory of the project, for resolving root-relative paths.

    Returns:
        Path: The resolved absolute path to the image file.
    """
    if isinstance(image_relative_path, str) and image_relative_path.startswith("/"):
        if root_dir is None:
            # If root_dir is not provided but we have a root-relative path,
            # try to derive root_dir from markdown_file_path
            # This is a fallback and may not be accurate
            logger.warning(
                "Root directory not provided for root-relative path: %s",
                image_relative_path,
            )
            markdown_file_path = Path(markdown_file_path).resolve()
            # Attempt to find the project root (this is a guess)
            actual_image_path = markdown_file_path.parent / image_relative_path[1:]
        else:
            # Use the root directory to resolve the path
            image_path_without_leading_slash = image_relative_path[1:]
            actual_image_path = (root_dir / image_path_without_leading_slash).resolve()
            logger.info(
                f"Resolved root-relative path: {image_relative_path} -> {actual_image_path}"
            )
    else:
        # Handle regular relative paths as before
        image_relative_path = Path(image_relative_path)
        markdown_file_path = Path(markdown_file_path).resolve()
        actual_image_path = (markdown_file_path.parent / image_relative_path).resolve()

    return actual_image_path


def map_original_to_translated(
    original_abs: Path,
    language_code: str,
    root_dir: Path,
    translations_dir: Path | None = None,
) -> Path | None:
    """
    Map an absolute path of an original file under root_dir to its translated counterpart.

    Rules:
    - If original_abs is not under root_dir, return None.
    - The translated candidate path is translations/<lang>/<original_rel_from_root>.
    - If the candidate exists on disk, return it; otherwise return None.

    Args:
        original_abs (Path): Absolute path to the original file.
        language_code (str): Language code (e.g., 'ko').
        root_dir (Path): Project root.
        translations_dir (Path | None): Override translations dir; default root_dir / 'translations'.

    Returns:
        Path | None: Absolute path to translated file if it exists, else None.
    """
    original_abs = Path(original_abs).resolve()
    root_dir = Path(root_dir).resolve()
    translations_dir = (
        Path(translations_dir).resolve()
        if translations_dir
        else (root_dir / "translations").resolve()
    )

    try:
        original_rel = original_abs.relative_to(root_dir)
    except ValueError:
        # Outside project root
        return None

    candidate = (translations_dir / language_code / original_rel).resolve()
    return candidate if candidate.exists() else None


def get_unique_id(file_path: str | Path, root_dir: Path) -> str:
    """
    Generate a unique identifier (hash) for the given file path, based on the relative path to the root directory.
    This function normalizes path separators to '/' before hashing to ensure consistency across operating systems.

    Args:
        file_path (str | Path): The file path to hash.
        root_dir (Path): The root directory to which the file path should be relative.

    Returns:
        str: A SHA-256 hash of the normalized relative file path.
    """
    file_path = Path(file_path).resolve()
    relative_path = file_path.relative_to(root_dir)

    # Normalize path separators to '/' for cross-platform consistency
    normalized_path = str(relative_path).replace(os.sep, "/")

    # Convert the normalized path to bytes and hash it
    relative_path_bytes = normalized_path.encode("utf-8")
    hash_object = hashlib.sha256(relative_path_bytes)
    unique_identifier = hash_object.hexdigest()

    logger.info(f"HASH for normalized path: {normalized_path} HASH={unique_identifier}")

    return unique_identifier


def generate_translated_filename(
    original_filepath: str | Path, language_code: str, root_dir: Path
) -> str:
    """
    Generate a filename for a translated file, including a unique hash and language code.

    All translated images are saved as WebP format for optimal compression.
    The original extension is preserved in the base filename for traceability.

    Note:
    If the file path and the file name are identical, the same hash will be generated.
    This is because the hash is based on the entire file path.

    Args:
        original_filepath (str): The original file path.
        language_code (str): The language code for the translation (e.g., 'en', 'fr').

    Returns:
        str: The translated file's new filename (always .webp extension).
    """
    from co_op_translator.config.constants import WEBP_EXTENSION

    original_filepath = Path(original_filepath)

    # Extract original file components
    original_filename, file_ext = get_filename_and_extension(original_filepath)

    # Compute the full path hash based on the normalized path
    full_hash = get_unique_id(str(original_filepath), root_dir)

    # Use a fixed-size prefix for deterministic filenames across runs/OS
    hash_prefix = full_hash[:HASH_PREFIX_LENGTH]

    # Generate the new filename with WebP extension for optimal compression
    # All translated images are saved as WebP regardless of original format
    new_filename = f"{original_filename}.{hash_prefix}{WEBP_EXTENSION}"

    return new_filename


def get_filename_and_extension(file_path: str | Path) -> tuple[str, str]:
    """
    Extract the filename without extension and the file extension from the given file path.

    Args:
        file_path (str | Path): The file path from which to extract the filename and extension.

    Returns:
        tuple[str, str]: A tuple containing the filename without extension and the file extension.
    """
    # Ensure the file_path is a string or Path object
    file_path = str(file_path)  # Convert to string if it's a Path object

    # Extract the base name (filename with extension) and split it into name and extension
    original_filename, file_ext = os.path.splitext(os.path.basename(file_path))

    # Return the filename without extension and the file extension in lowercase
    return original_filename, file_ext.lower()


def filter_files(directory: str | Path, excluded_dirs, extension: str = None) -> list:
    """
    Filter and return only the files in the given directory, excluding specified directories.
    Optionally filter by file extension.

    Args:
        directory (str | Path): The directory path to search for files.
        excluded_dirs (set): A set of directory names to exclude from the search.
        extension (str, optional): File extension to filter by (e.g., '.ipynb').
                                If None, all file types are included.

    Returns:
        list: A list of Path objects representing only the files (excluding specified directories).
    """
    directory = Path(directory)
    files = []

    # Normalize excluded directories into two buckets: absolute paths and names
    abs_excluded: list[Path] = []
    name_excluded: set[str] = set()
    for item in excluded_dirs:
        try:
            p = Path(item)
            if p.is_absolute():
                abs_excluded.append(p.resolve())
            else:
                name_excluded.add(str(item))
        except Exception:
            name_excluded.add(str(item))

    # Recursively traverse the directory
    for path in directory.rglob("*"):
        if not path.is_file():
            continue
        if extension is not None and path.suffix.lower() != extension.lower():
            continue

        # Exclude by absolute path ancestry
        excluded_by_abs = False
        try:
            resolved = path.resolve()
            for abs_dir in abs_excluded:
                try:
                    resolved.relative_to(abs_dir)
                    excluded_by_abs = True
                    break
                except Exception:
                    continue
        except Exception:
            # If resolve() fails, fall back to name-based exclusion only
            excluded_by_abs = False

        if excluded_by_abs:
            continue

        # Name-based exclusion (segment match)
        if any(ex in path.parts for ex in name_excluded):
            continue

        files.append(path)

    return files


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
    language_code: str, translations_dir: Path
):
    """
    Delete the entire directory for the specified language code, including all its contents.

    Args:
        language_code (str): The language code whose folder should be deleted (e.g., 'ko').
        translations_dir (Path): The directory where translated markdown files are stored.
    """
    # Construct the path to the directory for the specific language
    language_dir = translations_dir / language_code

    if not language_dir.exists():
        logger.warning(
            f"Directory {language_dir} does not exist. No markdown files to delete."
        )
        return

    # Remove the entire directory and its contents
    shutil.rmtree(language_dir)
    logger.info(f"Deleted the directory and all files for language: {language_code}")


def canonicalize_image_links_in_translations(
    translations_dir: Path, image_dir: Path
) -> tuple[int, int]:
    """
    Canonicalize image links in translated markdown and notebooks by rewriting
    alias-based language directory segments to canonical BCP 47.

    Examples:
      translated_images/tw/...  -> translated_images/zh-TW/...
      translated_images/cn/...  -> translated_images/zh-CN/...
      <base_dir>/br/...         -> <base_dir>/pt-BR/...

    The function scans under translations_dir and updates files in-place.

    Returns:
      (md_files_updated, nb_files_updated)
    """
    from co_op_translator.utils.common.lang_utils import ALIAS_TO_BCP47
    from co_op_translator.config.constants import (
        SUPPORTED_MARKDOWN_EXTENSIONS,
        SUPPORTED_NOTEBOOK_EXTENSIONS,
    )

    translations_dir = Path(translations_dir)
    image_dir = Path(image_dir)
    base_dir_name = image_dir.name
    base_dirs = [base_dir_name, "translated_images", "translated_images_fast"]

    def _canonicalize_text(text: str) -> str:
        updated = text
        for bdir in base_dirs:
            for alias, canonical in ALIAS_TO_BCP47.items():
                updated = updated.replace(f"{bdir}/{alias}/", f"{bdir}/{canonical}/")
                # Also replace Windows-style separators just in case
                updated = updated.replace(
                    f"{bdir}\\{alias}\\", f"{bdir}\\{canonical}\\"
                )
        return updated

    md_updated = 0
    nb_updated = 0

    # Markdown files
    try:
        md_files: list[Path] = []
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            md_files.extend(translations_dir.rglob(f"*{ext}"))
        for md in md_files:
            try:
                original = md.read_text(encoding="utf-8")
            except Exception:
                continue
            updated = _canonicalize_text(original)
            if updated != original:
                try:
                    md.write_text(updated, encoding="utf-8")
                    md_updated += 1
                except Exception:
                    pass
    except Exception:
        pass

    # Notebooks (JSON)
    try:
        nb_files: list[Path] = []
        for ext in SUPPORTED_NOTEBOOK_EXTENSIONS:
            nb_files.extend(translations_dir.rglob(f"*{ext}"))
        for nb in nb_files:
            try:
                content = nb.read_text(encoding="utf-8")
            except Exception:
                continue
            updated = _canonicalize_text(content)
            if updated != content:
                try:
                    nb.write_text(updated, encoding="utf-8")
                    nb_updated += 1
                except Exception:
                    pass
    except Exception:
        pass

    return md_updated, nb_updated
