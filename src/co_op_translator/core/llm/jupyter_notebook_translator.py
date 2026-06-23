"""
Jupyter Notebook translator for translating .ipynb files.

This module provides functionality to translate Jupyter Notebook files by
extracting markdown cells, translating them, and preserving code cells unchanged.
"""

import json
import logging
from pathlib import Path

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.utils.markdown.path_rewriter import (
    MarkdownPathRewritePolicy,
    rewrite_markdown_paths,
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
            root_dir: Root directory of the project for path calculations
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None
        self.markdown_translator = MarkdownTranslator.create(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=self.lang_subdir,
        )

    def _get_notebook_target_path(
        self,
        notebook_path: Path,
        language_code: str,
        target_path: str | Path | None = None,
    ) -> Path | None:
        if target_path is not None:
            return Path(target_path).resolve()
        if self.root_dir is None:
            return None

        root_dir = Path(self.root_dir).resolve()
        try:
            relative_path = notebook_path.resolve().relative_to(root_dir)
        except ValueError:
            return None

        translations_dir = (
            Path(self.translations_dir)
            if self.translations_dir is not None
            else root_dir / "translations"
        )
        language_root = translations_dir / language_code
        if self.lang_subdir:
            language_root = language_root / self.lang_subdir
        return (language_root / relative_path).resolve()

    def _rewrite_markdown_cell_paths(
        self,
        content: str,
        notebook_path: Path,
        target_notebook_path: Path | None,
        language_code: str,
        translation_types: list[str],
    ) -> str:
        if target_notebook_path is None or self.root_dir is None:
            return content

        return rewrite_markdown_paths(
            content,
            source_path=notebook_path,
            target_path=target_notebook_path,
            policy=MarkdownPathRewritePolicy(
                language_code=language_code,
                root_dir=self.root_dir,
                translations_dir=self.translations_dir,
                translated_images_dir=self.image_dir,
                translation_types=translation_types,
                lang_subdir=self.lang_subdir,
            ),
        )

    async def translate_notebook(
        self,
        notebook_path: str | Path,
        language_code: str,
        use_translated_images: bool = True,
        add_disclaimer: bool = True,
        target_path: str | Path | None = None,
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
            target_path: Optional translated notebook path used as the relative-link base

        Returns:
            str: The translated notebook content as JSON string
        """
        notebook_path = Path(notebook_path)
        target_notebook_path = self._get_notebook_target_path(
            notebook_path, language_code, target_path=target_path
        )

        # Read the notebook file
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

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
                            source_path=notebook_path,
                        )
                    )
                    translated_content = self._rewrite_markdown_cell_paths(
                        translated_content,
                        notebook_path,
                        target_notebook_path,
                        language_code,
                        notebook_translation_types,
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

        # Return the modified notebook as JSON string
        return json.dumps(notebook, ensure_ascii=False, indent=1)

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
