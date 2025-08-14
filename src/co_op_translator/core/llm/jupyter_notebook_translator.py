"""
Jupyter Notebook translator for translating .ipynb files.

This module provides functionality to translate Jupyter Notebook files by
extracting markdown cells, translating them, and preserving code cells unchanged.
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, List

from .markdown_translator import MarkdownTranslator
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    calculate_string_hash,
)

logger = logging.getLogger(__name__)


class JupyterNotebookTranslator:
    """Handles translation of Jupyter Notebook (.ipynb) files.

    Translates markdown cells while preserving code cells, metadata,
    and the overall notebook structure.
    """

    def __init__(self, root_dir: Path = None):
        """Initialize the notebook translator.

        Args:
            root_dir: Root directory of the project for path calculations
        """
        self.root_dir = root_dir
        self.markdown_translator = MarkdownTranslator.create(root_dir)

    async def translate_notebook(
        self,
        notebook_path: str | Path,
        language_code: str,
        markdown_only: bool = False,
    ) -> str:
        """Translate a Jupyter Notebook file to the target language.

        Extracts markdown cells from the notebook, translates them using
        the existing markdown translator, and reconstructs the notebook
        with translated content.

        Args:
            notebook_path: Path to the .ipynb file
            language_code: Target language code
            markdown_only: Skip embedded image translation if True

        Returns:
            str: The translated notebook content as JSON string
        """
        notebook_path = Path(notebook_path)

        # Read the notebook file
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        # Compute notebook-level hash of the original file content
        original_hash = calculate_file_hash(notebook_path)

        # Attempt to load existing translated notebook (if any) to enable per-cell reuse
        existing_translated: dict | None = None
        # The caller determines output path; we only reuse by matching cells if the caller provided content.
        # Here, we support reuse by looking inside this notebook itself if already translated previously.
        # If this is an original (non-translated) notebook, metadata won't exist and reuse won't happen.
        existing_translated = notebook

        translated_cells_by_id: dict[str, dict] = {}
        translated_cells_by_index: dict[int, dict] = {}
        if isinstance(existing_translated, dict):
            cells = existing_translated.get("cells", [])
            for idx, cell in enumerate(cells):
                if cell.get("cell_type") != "markdown":
                    continue
                meta = cell.get("metadata", {}).get("coopTranslator", {})
                src_hash = meta.get("source_hash")
                if not src_hash:
                    continue
                # Prefer cell id mapping if present
                cell_id = cell.get("id")
                entry = {"index": idx, "cell": cell, "source_hash": src_hash}
                if isinstance(cell_id, str):
                    translated_cells_by_id[cell_id] = entry
                translated_cells_by_index[idx] = entry

        # Track which cells were translated for logging
        translated_cells = 0
        total_markdown_cells = 0

        # Process each cell
        for idx, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") == "markdown":
                total_markdown_cells += 1

                # Extract the source content
                source = cell.get("source", [])
                if not source:
                    continue

                # Convert source to string (it might be a list of lines)
                if isinstance(source, list):
                    markdown_content = "".join(source)
                else:
                    markdown_content = str(source)

                # Skip empty cells
                if not markdown_content.strip():
                    continue

                # Compute per-cell source hash and check if unchanged
                current_src_hash = calculate_string_hash(markdown_content)

                # Try to reuse existing translated content if source hash matches
                reused = False
                cell_id = cell.get("id")
                candidate = None
                if isinstance(cell_id, str) and cell_id in translated_cells_by_id:
                    candidate = translated_cells_by_id[cell_id]
                elif idx in translated_cells_by_index:
                    candidate = translated_cells_by_index[idx]

                if candidate and candidate.get("source_hash") == current_src_hash:
                    prev_cell = candidate["cell"]
                    prev_source = prev_cell.get("source", [])
                    # Reuse previous translated source as-is
                    cell["source"] = prev_source
                    # Ensure metadata is set
                    cell.setdefault("metadata", {}).setdefault("coopTranslator", {})[
                        "source_hash"
                    ] = current_src_hash
                    reused = True

                if reused:
                    continue

                try:
                    # Translate the markdown content
                    # Don't add metadata and disclaimer to individual cells
                    translated_content = (
                        await self.markdown_translator.translate_markdown(
                            markdown_content,
                            language_code,
                            notebook_path,
                            markdown_only=markdown_only,
                            add_metadata=False,
                            add_disclaimer=False,
                        )
                    )

                    # Convert back to the original format (list or string)
                    if isinstance(source, list):
                        # Split by lines but preserve the original line ending behavior
                        translated_lines = translated_content.splitlines(keepends=True)
                        # Ensure lines end with \n if they don't already
                        translated_lines = [
                            line if line.endswith("\n") else line + "\n"
                            for line in translated_lines
                        ]
                        cell["source"] = translated_lines
                    else:
                        cell["source"] = translated_content

                    # Record per-cell metadata for future reuse
                    cell.setdefault("metadata", {}).setdefault("coopTranslator", {})[
                        "source_hash"
                    ] = current_src_hash

                    translated_cells += 1

                except Exception as e:
                    logger.warning(
                        f"Failed to translate cell in {notebook_path}: {e}. "
                        f"Keeping original content."
                    )

        # Save notebook-level metadata
        notebook.setdefault("metadata", {}).setdefault("coopTranslator", {})[
            "original_hash"
        ] = original_hash
        notebook["metadata"]["coopTranslator"]["language_code"] = language_code

        logger.info(
            f"Translated {translated_cells}/{total_markdown_cells} markdown cells "
            f"in {notebook_path.name}"
        )

        # Return the modified notebook as JSON string
        return json.dumps(notebook, ensure_ascii=False, indent=1)

    @classmethod
    def create(cls, root_dir: Path = None) -> "JupyterNotebookTranslator":
        """Create a Jupyter Notebook translator instance.

        Factory method for creating the translator.

        Args:
            root_dir: Root directory of the project for path calculations

        Returns:
            JupyterNotebookTranslator instance
        """
        return cls(root_dir)
