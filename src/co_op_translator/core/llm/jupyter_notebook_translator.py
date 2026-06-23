"""
Jupyter Notebook translator for translating .ipynb files.

This module provides functionality to translate Jupyter Notebook files by
extracting markdown cells, translating them, and preserving code cells unchanged.
"""

import json
import logging
from copy import deepcopy
from pathlib import Path
from typing import Any

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.utils.markdown.notebook_cells import (
    get_cell_source_text,
    iter_markdown_cells,
    set_cell_source_text,
)

logger = logging.getLogger(__name__)


class JupyterNotebookTranslator:
    """Handles translation of Jupyter Notebook (.ipynb) files.

    Translates markdown cells while preserving code cells, metadata,
    and the overall notebook structure.
    """

    def __init__(
        self,
        root_dir: Path = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
    ):
        """Initialize the notebook translator.

        Args:
            root_dir: Optional project root retained for compatibility
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None
        self.markdown_translator = MarkdownTranslator.create()

    def _load_notebook(self, notebook: str | dict[str, Any]) -> dict[str, Any]:
        if isinstance(notebook, dict):
            return deepcopy(notebook)
        return json.loads(notebook)

    async def translate_notebook(
        self,
        notebook: str | dict[str, Any],
        language_code: str,
        source_path: str | Path | None = None,
    ) -> str:
        """Translate markdown cells in a Jupyter Notebook payload.

        This method performs no file I/O, no project path rewriting, no
        disclaimer insertion, and no metadata writes. Project-level callers
        compose those steps around this content-only translation.

        Args:
            notebook: Notebook JSON string or parsed notebook dictionary
            language_code: Target language code
            source_path: Optional source path used only for translation context/logging

        Returns:
            str: The translated notebook content as JSON string
        """
        notebook_name = Path(source_path).name if source_path else "notebook"
        translated_notebook = self._load_notebook(notebook)

        # Track which cells were translated for logging
        translated_cells = 0
        total_markdown_cells = 0

        # Process each cell
        for cell in iter_markdown_cells(translated_notebook):
            total_markdown_cells += 1

            markdown_content = get_cell_source_text(cell)
            if not markdown_content.strip():
                continue

            try:
                translated_content = await self.markdown_translator.translate_markdown(
                    markdown_content,
                    language_code,
                    source_path=source_path,
                )
                set_cell_source_text(cell, translated_content)
                translated_cells += 1

            except Exception as e:
                logger.warning(
                    f"Failed to translate cell in {notebook_name}: {e}. "
                    f"Keeping original content."
                )

        logger.info(
            f"Translated {translated_cells}/{total_markdown_cells} markdown cells "
            f"in {notebook_name}"
        )

        # Return the modified notebook as JSON string
        return json.dumps(translated_notebook, ensure_ascii=False, indent=1)

    @classmethod
    def create(
        cls,
        root_dir: Path = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
    ) -> "JupyterNotebookTranslator":
        """Create a Jupyter Notebook translator instance.

        Factory method for creating the translator.

        Args:
            root_dir: Root directory of the project for path calculations

        Returns:
            JupyterNotebookTranslator instance
        """
        return cls(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
        )
