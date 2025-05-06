"""
This module contains utility functions for handling file metadata and hashing operations.
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path


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
    metadata_json = json.dumps(metadata, indent=2)
    formatted_comment = f"<!--\nCO_OP_TRANSLATOR_METADATA:\n{metadata_json}\n-->\n"
    return formatted_comment
