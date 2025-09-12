"""
This module contains utility functions for handling file metadata and hashing operations.
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


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
    # Remove metadata comment block
    metadata_start = content.find("<!--\nCO_OP_TRANSLATOR_METADATA:")
    if metadata_start != -1:
        comment_end = content.find("-->\n", metadata_start)
        if comment_end != -1:
            # Remove the metadata block and the newline after it
            content = content[:metadata_start] + content[comment_end + 4 :]

    return content.strip()


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
