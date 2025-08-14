"""
Utilities for working with Jupyter Notebook (.ipynb) metadata and update checks.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

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


def read_notebook_metadata(notebook_path: Path) -> Dict[str, Any]:
    """
    Read the root-level metadata object from a notebook file.
    Returns empty dict if not available or on error.
    """
    nb = _read_notebook_json(notebook_path)
    meta = nb.get("metadata", {})
    return meta if isinstance(meta, dict) else {}


def read_coop_metadata(notebook_path: Path) -> Dict[str, Any]:
    """
    Read the co-op translator metadata section from a notebook file.
    Returns empty dict if not present or on error.
    """
    meta = read_notebook_metadata(notebook_path)
    coop_meta = meta.get("coopTranslator", {})
    return coop_meta if isinstance(coop_meta, dict) else {}


def is_notebook_up_to_date(original_path: Path, translated_path: Path) -> bool:
    """
    Determine if a translated notebook is up to date with its original.

    Compares the current hash of the original notebook with the stored
    metadata.coopTranslator.original_hash in the translated notebook.

    Returns False if metadata is missing or any error occurs.
    """
    try:
        stored_hash = read_coop_metadata(translated_path).get("original_hash")
        if not stored_hash:
            return False
        current_hash = calculate_file_hash(Path(original_path))
        return stored_hash == current_hash
    except Exception:
        return False 