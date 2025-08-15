"""
Utilities for working with Jupyter Notebook (.ipynb) metadata and update checks.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from .metadata_utils import calculate_file_hash


def _read_notebook_json(notebook_path: Path) -> Dict[str, Any]:
    """
    Safely read a notebook JSON file. Returns empty dict on error.
    """
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def read_notebook_metadata(notebook_path: Path, metadata_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Read metadata from a notebook file.
    Example of how to use this function:
    
    ```
    metadata = read_notebook_metadata(notebook_path, "coopTranslator")
    ```
    
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

    Returns False if metadata is missing or any error occurs.
    """
    try:
        stored_hash = read_notebook_metadata(translated_path, "coopTranslator").get("original_hash")
        if not stored_hash:
            return False
        current_hash = calculate_file_hash(Path(original_path))
        return stored_hash == current_hash
    except Exception:
        return False 