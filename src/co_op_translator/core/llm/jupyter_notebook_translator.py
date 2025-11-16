"""
Jupyter Notebook translator for translating .ipynb files.

This module provides functionality to translate Jupyter Notebook files by
extracting markdown cells, translating them, and preserving code cells unchanged.
"""

import json
import logging
from pathlib import Path

from .markdown_translator import MarkdownTranslator
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    add_notebook_metadata,
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
    ):
        """Initialize the notebook translator.

        Args:
            root_dir: Root directory of the project for path calculations
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.markdown_translator = MarkdownTranslator.create(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
        )

    async def translate_notebook(
        self,
        notebook_path: str | Path,
        language_code: str,
        use_translated_images: bool = True,
        add_disclaimer: bool = True,
    ) -> str:
        """Translate a Jupyter Notebook file to the target language.

        Extracts markdown cells from the notebook, translates them using
        the existing markdown translator, and reconstructs the notebook
        with translated content.

        Args:
            notebook_path: Path to the .ipynb file
            language_code: Target language code
            use_translated_images: Whether to use translated images (False = skip image translation)
            add_disclaimer: Add disclaimer cell at the end of notebook if True

        Returns:
            str: The translated notebook content as JSON string
        """
        notebook_path = Path(notebook_path)

        # Read the notebook file
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        # Compute notebook-level hash of the original file content
        original_hash = calculate_file_hash(notebook_path)

        # Track which cells were translated for logging
        translated_cells = 0
        total_markdown_cells = 0

        # Process each cell
        for cell in notebook.get("cells", []):
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

                try:
                    # Translate the markdown content
                    # Don't add metadata and disclaimer to individual cells
                    # For notebook translation, always enable notebook link processing
                    notebook_translation_types = ["markdown", "notebook"]
                    if use_translated_images:
                        notebook_translation_types.append("images")

                    translated_content = (
                        await self.markdown_translator.translate_markdown(
                            markdown_content,
                            language_code,
                            notebook_path,
                            translation_types=notebook_translation_types,
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

                    translated_cells += 1

                except Exception as e:
                    logger.warning(
                        f"Failed to translate cell in {notebook_path}: {e}. "
                        f"Keeping original content."
                    )

        logger.info(
            f"Translated {translated_cells}/{total_markdown_cells} markdown cells "
            f"in {notebook_path.name}"
        )

        # Add disclaimer cell at the end if requested
        if add_disclaimer:
            disclaimer_text = await self.markdown_translator.generate_disclaimer(
                language_code
            )
            if disclaimer_text:
                start_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER START -->"
                end_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER END -->"
                disclaimer_block = (
                    f"---\n\n{start_marker}\n{disclaimer_text}\n{end_marker}"
                )
                disclaimer_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [disclaimer_block + "\n"],
                }
                notebook["cells"].append(disclaimer_cell)
                logger.debug(f"Added disclaimer cell to {notebook_path.name}")

        # Add coopTranslator metadata to the notebook
        notebook_path = Path(notebook_path)
        notebook = add_notebook_metadata(
            notebook, notebook_path, language_code, self.root_dir
        )

        logger.debug(f"Added coopTranslator metadata to {notebook_path.name}")

        # Return the modified notebook as JSON string
        return json.dumps(notebook, ensure_ascii=False, indent=1)

    @classmethod
    def create(
        cls,
        root_dir: Path = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
    ) -> "JupyterNotebookTranslator":
        """Create a Jupyter Notebook translator instance.

        Factory method for creating the translator.

        Args:
            root_dir: Root directory of the project for path calculations

        Returns:
            JupyterNotebookTranslator instance
        """
        return cls(root_dir, translations_dir=translations_dir, image_dir=image_dir)
