"""
This module contains utility functions for handling file metadata and hashing operations.
"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


def calculate_file_hash(file_path: Path) -> str:
    """
    Calculate MD5 hash of a file.

    Args:
        file_path (Path): Path to the file to calculate hash for.

    Returns:
        str: MD5 hash of the file content.
    """
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def calculate_string_hash(text: str) -> str:
    """
    Calculate MD5 hash of a Unicode string.

    This is used for per-cell source hashing in notebooks to detect changes.

    Args:
        text (str): Input text to hash.

    Returns:
        str: MD5 hash of the UTF-8 encoded text.
    """
    hasher = hashlib.md5()
    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()


def create_metadata(
    original_file: Path, language_code: str, root_dir: Path | None = None
) -> dict:
    """
    Create metadata for a translated file.

    Args:
        original_file (Path): Path to the original file
        language_code (str): Target language code
        root_dir (Path, optional): Root directory for relative path calculation

    Returns:
        dict: Metadata dictionary containing file information
    """
    utc_time = datetime.utcnow()
    formatted_time = utc_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    # Calculate relative path if root_dir is provided
    if root_dir:
        rel_path = original_file.relative_to(root_dir)
    else:
        rel_path = original_file

    normalized_path = str(rel_path).replace("\\", "/")

    return {
        "original_hash": calculate_file_hash(original_file),
        "translation_date": formatted_time,
        "source_file": normalized_path,
        "language_code": language_code,
    }


def extract_metadata_from_content(content: str) -> dict:
    """
    Extract metadata from the content of a markdown file.

    Supports both formats:
    1) Labeled block used by Co-op Translator:
       <!--\nCO_OP_TRANSLATOR_METADATA:\n{ ... }\n-->\n
    2) Unlabeled JSON inside an HTML comment (legacy/tests):
       <!--\n{ ... }\n-->\n
    Args:
        content (str): The content of the markdown file

    Returns:
        dict: Extracted metadata dictionary, or empty dict if no metadata found
    """
    # First try the labeled metadata block for precision
    metadata_start = content.find("<!--\nCO_OP_TRANSLATOR_METADATA:")
    if metadata_start != -1:
        json_start = content.find("{", metadata_start)
        if json_start != -1:
            comment_end = content.find("-->\n", json_start)
            if comment_end != -1:
                json_content = content[json_start:comment_end].strip()
                try:
                    return json.loads(json_content)
                except json.JSONDecodeError:
                    pass

    # Fallback: find the first HTML comment and attempt to parse JSON inside
    generic_start = content.find("<!--")
    if generic_start == -1:
        return {}
    generic_end = content.find("-->", generic_start)
    if generic_end == -1:
        return {}

    inner = content[generic_start + 4 : generic_end].strip()
    # If the inner starts with our label, strip it
    label = "CO_OP_TRANSLATOR_METADATA:"
    if inner.startswith(label):
        inner = inner[len(label) :].strip()

    # Try direct JSON
    try:
        return json.loads(inner)
    except json.JSONDecodeError:
        # Try to extract JSON between the first '{' and last '}'
        brace_start = inner.find("{")
        brace_end = inner.rfind("}")
        if brace_start != -1 and brace_end != -1 and brace_end > brace_start:
            try:
                return json.loads(inner[brace_start : brace_end + 1])
            except json.JSONDecodeError:
                return {}
        return {}


def extract_content_without_metadata(content: str) -> str:
    """
    Extract content from a markdown file, removing the metadata comment block.

    This function removes the CO_OP_TRANSLATOR_METADATA comment block.
    Note: This function only removes metadata, not disclaimers or other content.

    Args:
        content (str): The content of the markdown file

    Returns:
        str: The content with metadata comments removed
    """
    # Remove metadata comment block while preserving surrounding line structure.
    # We only remove the comment itself and at most a single following newline,
    # so the overall number of blank lines in the document stays stable.
    metadata_start = content.find("<!--\nCO_OP_TRANSLATOR_METADATA:")
    if metadata_start != -1:
        # Find the closing marker first (independent of trailing newline)
        comment_end = content.find("-->", metadata_start)
        if comment_end != -1:
            end_index = comment_end + len("-->")
            # If there is exactly one newline immediately after the closing
            # marker, skip it as part of the metadata block removal.
            if end_index < len(content) and content[end_index] == "\n":
                end_index += 1

            content = content[:metadata_start] + content[end_index:]

    # Do not strip the entire document; callers rely on preserving
    # original blank lines, especially at the end of README files.
    return content


def format_metadata_comment(metadata: dict) -> str:
    """
    Convert a metadata dictionary into a formatted HTML comment.

    This function serializes the metadata dictionary as a JSON string with indentation,
    wraps it in a custom HTML comment format, and returns the resulting string.

    Args:
        metadata (dict): A dictionary containing metadata to be formatted.

    Returns:
        str: A string containing the metadata formatted as an HTML comment.

    Example:
    <!--
    CO_OP_TRANSLATOR_METADATA:
    {
      "original_hash": "sample_hash",
      "translation_date": "2025-01-30T13:02:53+00:00",
      "source_file": "test.md",
      "language_code": "ko"
    }
    -->

    Total lines: 9
    """
    metadata_json = json.dumps(metadata, indent=2, ensure_ascii=False)
    formatted_comment = f"<!--\nCO_OP_TRANSLATOR_METADATA:\n{metadata_json}\n-->\n"
    return formatted_comment


# ============================================================================
# Notebook-specific metadata utilities
# ============================================================================


def _read_notebook_json(notebook_path: Path) -> Dict[str, Any]:
    """
    Safely read a notebook JSON file. Returns empty dict on error.

    Args:
        notebook_path: Path to the notebook file

    Returns:
        Dict containing the notebook JSON, or empty dict on error
    """
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def read_notebook_metadata(
    notebook_path: Path, metadata_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Read metadata from a notebook file.

    Example:
        metadata = read_notebook_metadata(notebook_path, "coopTranslator")

    Args:
        notebook_path: Path to the notebook file
        metadata_key: Optional key to extract specific metadata section.
                     If None, returns the entire metadata object.

    Returns:
        Dict containing the requested metadata. Returns empty dict if not present or on error.
    """
    nb = _read_notebook_json(notebook_path)
    meta = nb.get("metadata", {})
    if not isinstance(meta, dict):
        return {}

    if metadata_key is None:
        return meta

    specific_meta = meta.get(metadata_key, {})
    return specific_meta if isinstance(specific_meta, dict) else {}


def is_notebook_up_to_date(original_path: Path, translated_path: Path) -> bool:
    """
    Determine if a translated notebook is up to date with its original.

    Compares the current hash of the original notebook with the stored
    metadata.coopTranslator.original_hash in the translated notebook.

    Args:
        original_path: Path to the original notebook
        translated_path: Path to the translated notebook

    Returns:
        True if translated notebook is up to date, False otherwise
    """

    try:
        translated_path = Path(translated_path)
        if not translated_path.exists():
            return False

        lang_dir = _find_lang_dir_for_translated_file(translated_path)
        if lang_dir is not None:
            metadata = read_text_metadata_for_source(lang_dir, original_path)
            stored_hash = metadata.get("original_hash")
            if stored_hash:
                current_hash = calculate_file_hash(Path(original_path))
                return stored_hash == current_hash

        stored_hash = read_notebook_metadata(translated_path, "coopTranslator").get(
            "original_hash"
        )
        if not stored_hash:
            return False
        current_hash = calculate_file_hash(Path(original_path))
        return stored_hash == current_hash
    except Exception:
        return False


def add_notebook_metadata(
    notebook: Dict[str, Any],
    original_path: Path,
    language_code: str,
    root_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Add coopTranslator metadata to a notebook dictionary.

    Args:
        notebook: The notebook dictionary to modify
        original_path: Path to the original notebook file
        language_code: Target language code
        root_dir: Root directory for relative path calculation

    Returns:
        Modified notebook dictionary with coopTranslator metadata
    """
    # Create translation metadata
    translation_metadata = create_metadata(original_path, language_code, root_dir)

    # Ensure metadata section exists
    if "metadata" not in notebook:
        notebook["metadata"] = {}

    # Add coopTranslator metadata
    notebook["metadata"]["coopTranslator"] = translation_metadata

    return notebook


def _find_lang_dir_for_translated_file(translated_path: Path) -> Optional[Path]:
    translated_path = Path(translated_path)
    current = translated_path.parent

    while True:
        metadata_file = _get_metadata_file_path(current)
        if metadata_file.exists():
            return current

        parent = current.parent
        if parent == current:
            break
        current = parent

    return None


# ============================================================================
# Image-specific metadata utilities
# ============================================================================

# Metadata file name (placed in each language folder)
IMAGE_METADATA_FILENAME = ".co-op-translator.json"

# Lock for thread-safe metadata file access (per-language locks)
import threading

_metadata_locks: dict[str, threading.Lock] = {}
_locks_lock = threading.Lock()


def _get_lock_for_path(path: Path) -> threading.Lock:
    """Get or create a lock for a specific metadata file path."""
    path_str = str(path)
    with _locks_lock:
        if path_str not in _metadata_locks:
            _metadata_locks[path_str] = threading.Lock()
        return _metadata_locks[path_str]


def _get_metadata_file_path(lang_dir: Path) -> Path:
    """Get the path to the metadata file in a language directory."""
    return Path(lang_dir) / IMAGE_METADATA_FILENAME


def _get_image_key(image_path: Path) -> str:
    """Get the filename as the key (without language prefix)."""
    return Path(image_path).name


def _load_lang_metadata(lang_dir: Path) -> dict:
    """Load metadata from a language-specific metadata file."""
    metadata_file = _get_metadata_file_path(lang_dir)
    if metadata_file.exists():
        try:
            with open(metadata_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.debug(f"Failed to load image metadata from {metadata_file}: {e}")
    return {}


def _save_lang_metadata(lang_dir: Path, metadata: dict) -> None:
    """Save metadata to a language-specific metadata file."""
    metadata_file = _get_metadata_file_path(lang_dir)
    try:
        metadata_file.parent.mkdir(parents=True, exist_ok=True)
        ordered_metadata = {key: metadata[key] for key in sorted(metadata.keys())}
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(ordered_metadata, f, indent=2, ensure_ascii=False)
        logger.debug(f"Saved image metadata to: {metadata_file}")
    except Exception as e:
        logger.warning(f"Failed to save image metadata to {metadata_file}: {e}")


def create_image_metadata(
    original_file: Path, language_code: str, root_dir: Path | None = None
) -> dict:
    """
    Create metadata for a translated image file.

    This creates the same metadata structure as used for markdown and notebooks,
    ensuring consistency across all translated content types.

    Args:
        original_file (Path): Path to the original image file
        language_code (str): Target language code
        root_dir (Path, optional): Root directory for relative path calculation

    Returns:
        dict: Metadata dictionary containing file information
    """
    return create_metadata(original_file, language_code, root_dir)


def save_image_metadata(
    image_path: Path,
    original_file: Path,
    language_code: str,
    root_dir: Path | None = None,
    image_dir: Path | None = None,
) -> None:
    """
    Save translation metadata to the language-specific metadata file.

    Each language folder has its own .metadata.json file for efficient
    management and isolation.

    Args:
        image_path: Path to the translated image file
        original_file: Path to the original image file
        language_code: Target language code
        root_dir: Root directory for relative path calculation
        image_dir: Base directory for translated images (not used, kept for compatibility)
    """
    metadata = create_image_metadata(original_file, language_code, root_dir)

    # Get the language directory (parent of the image file)
    # Structure: translated_images/<lang>/<filename>
    lang_dir = Path(image_path).parent
    image_key = _get_image_key(image_path)

    lock = _get_lock_for_path(_get_metadata_file_path(lang_dir))
    with lock:
        all_metadata = _load_lang_metadata(lang_dir)
        all_metadata[image_key] = metadata
        _save_lang_metadata(lang_dir, all_metadata)

    logger.debug(f"Saved metadata for image: {image_key} in {lang_dir.name}")


def read_image_metadata(image_path: Path, image_dir: Path | None = None) -> dict:
    """
    Read metadata for a specific translated image from the language metadata file.

    Args:
        image_path: Path to the image file
        image_dir: Base directory for translated images (not used, kept for compatibility)

    Returns:
        dict: Metadata dictionary, or empty dict if not found or on error
    """
    image_path = Path(image_path)

    # Get the language directory (parent of the image file)
    lang_dir = image_path.parent
    image_key = _get_image_key(image_path)
    all_metadata = _load_lang_metadata(lang_dir)

    return all_metadata.get(image_key, {})


def remove_image_metadata(image_path: Path, image_dir: Path | None = None) -> None:
    """
    Remove metadata for a specific image from the language metadata file.

    Args:
        image_path: Path to the image file
        image_dir: Base directory for translated images (not used, kept for compatibility)
    """
    image_path = Path(image_path)

    # Get the language directory (parent of the image file)
    lang_dir = image_path.parent
    image_key = _get_image_key(image_path)

    lock = _get_lock_for_path(_get_metadata_file_path(lang_dir))
    with lock:
        all_metadata = _load_lang_metadata(lang_dir)
        if image_key in all_metadata:
            del all_metadata[image_key]
            _save_lang_metadata(lang_dir, all_metadata)
            logger.debug(
                f"Removed metadata for image: {image_key} from {lang_dir.name}"
            )


def cleanup_orphan_image_metadata(lang_dir: Path) -> int:
    """
    Remove metadata entries for images that no longer exist.

    This cleans up orphan metadata entries that remain after image files
    are manually deleted.

    Args:
        lang_dir: Language directory containing images and .co-op-translator.json

    Returns:
        Number of orphan entries removed
    """
    lang_dir = Path(lang_dir)
    metadata_file = _get_metadata_file_path(lang_dir)

    if not metadata_file.exists():
        return 0

    lock = _get_lock_for_path(metadata_file)
    with lock:
        all_metadata = _load_lang_metadata(lang_dir)
        original_count = len(all_metadata)

        # Keep only entries where the image file exists
        cleaned_metadata = {
            key: value
            for key, value in all_metadata.items()
            if (lang_dir / key).exists()
        }

        removed_count = original_count - len(cleaned_metadata)

        if removed_count > 0:
            _save_lang_metadata(lang_dir, cleaned_metadata)
            logger.info(
                f"Cleaned up {removed_count} orphan metadata entries from {lang_dir.name}"
            )

        return removed_count


def is_image_up_to_date(
    original_path: Path, translated_path: Path, image_dir: Path | None = None
) -> bool:
    """
    Determine if a translated image is up to date with its original.

    Compares the current hash of the original image with the stored
    metadata in the language-specific metadata file.

    Args:
        original_path: Path to the original image
        translated_path: Path to the translated image
        image_dir: Deprecated, not used (kept for backwards compatibility)

    Returns:
        True if translated image is up to date, False otherwise
    """
    try:
        if not translated_path.exists():
            return False

        stored_metadata = read_image_metadata(translated_path)
        stored_hash = stored_metadata.get("original_hash")

        if not stored_hash:
            return False

        current_hash = calculate_file_hash(original_path)
        return stored_hash == current_hash
    except Exception as e:
        logger.debug(f"Error checking image up-to-date status: {e}")
        return False


def _normalize_source_key(source: str | Path) -> str:
    return str(source).replace("\\", "/")


def load_language_metadata(lang_dir: Path) -> dict:
    return _load_lang_metadata(lang_dir)


def save_language_metadata(lang_dir: Path, metadata: dict) -> None:
    lock = _get_lock_for_path(_get_metadata_file_path(lang_dir))
    with lock:
        existing = _load_lang_metadata(lang_dir)
        existing.update(metadata)
        _save_lang_metadata(lang_dir, existing)


def save_text_metadata_for_source(
    lang_dir: Path,
    original_file: Path,
    language_code: str,
    root_dir: Path | None = None,
    extra_fields: Optional[dict] = None,
) -> dict:
    metadata = create_metadata(original_file, language_code, root_dir)
    if extra_fields:
        metadata.update(extra_fields)

    source_key = metadata.get("source_file")
    if not source_key:
        return metadata

    normalized_key = _normalize_source_key(source_key)  # relative, POSIX-style

    lock = _get_lock_for_path(_get_metadata_file_path(lang_dir))
    with lock:
        all_metadata = _load_lang_metadata(lang_dir)
        all_metadata[normalized_key] = metadata
        _save_lang_metadata(lang_dir, all_metadata)

    return metadata


def read_text_metadata_for_source(lang_dir: Path, source_file: str | Path) -> dict:
    """Read text metadata by source path.

    Keys are stored as repo-relative, POSIX-style paths. This lookup accepts any
    of the following and resolves to the best matching relative key:
    - relative POSIX-style path (exact match)
    - absolute path (Windows or POSIX): matched by the longest suffix against stored keys
    - paths with backslashes: normalized prior to matching
    """
    all_metadata = _load_lang_metadata(lang_dir)
    if not all_metadata:
        return {}

    normalized = _normalize_source_key(source_file)
    # Direct hit (already relative POSIX-style)
    if normalized in all_metadata:
        return all_metadata.get(normalized, {})

    # If absolute or otherwise not directly found, try suffix matching against stored relative keys
    # Build candidate suffixes from the provided path
    parts = normalized.split("/")
    best_key = None
    best_len = -1
    for i in range(len(parts)):
        suffix = "/".join(parts[i:])
        if suffix in all_metadata and len(suffix) > best_len:
            best_key = suffix
            best_len = len(suffix)

    if best_key is not None:
        return all_metadata.get(best_key, {})

    return {}


def remove_text_metadata_for_source(lang_dir: Path, source_file: str | Path) -> None:
    normalized_key = _normalize_source_key(source_file)
    lock = _get_lock_for_path(_get_metadata_file_path(lang_dir))
    with lock:
        all_metadata = _load_lang_metadata(lang_dir)
        changed = False
        if normalized_key in all_metadata:
            del all_metadata[normalized_key]
            changed = True
        # Also try absolute key variant if source_file was a Path
        try:
            absolute_key = _normalize_source_key(Path(source_file).resolve())
            if absolute_key in all_metadata:
                del all_metadata[absolute_key]
                changed = True
        except Exception:
            pass
        if changed:
            _save_lang_metadata(lang_dir, all_metadata)
