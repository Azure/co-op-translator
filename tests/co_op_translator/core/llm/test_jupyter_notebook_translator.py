"""
Tests for JupyterNotebookTranslator functionality.
"""

import json
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from co_op_translator.core.llm.jupyter_notebook_translator import (
    JupyterNotebookTranslator,
)
from co_op_translator.utils.markdown.notebook_path_rewriter import (
    rewrite_notebook_paths,
)
from co_op_translator.utils.markdown.path_rewriter import MarkdownPathRewritePolicy


@pytest.fixture
def sample_notebook():
    """Sample notebook content for testing."""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# Hello World\n", "\n", "This is a test notebook."],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "print('Hello, World!')\n",
                    "# This should not be translated",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Section 2\n", "\n", "Another markdown cell."],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }


@pytest.fixture
def temp_notebook_file(tmp_path, sample_notebook):
    """Create a temporary notebook file for testing."""
    notebook_file = tmp_path / "test.ipynb"
    with open(notebook_file, "w", encoding="utf-8") as f:
        json.dump(sample_notebook, f, ensure_ascii=False, indent=1)
    return notebook_file


class TestJupyterNotebookTranslator:
    """Test cases for JupyterNotebookTranslator."""

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    def test_create_translator(self, mock_markdown_translator_class):
        """Test that translator can be created."""
        mock_markdown_translator_class.create.return_value = MagicMock()
        translator = JupyterNotebookTranslator.create()
        assert translator is not None
        assert translator.root_dir is None

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    def test_create_translator_with_root_dir(
        self, mock_markdown_translator_class, tmp_path
    ):
        """Test that translator can be created with root directory."""
        mock_markdown_translator_class.create.return_value = MagicMock()
        translator = JupyterNotebookTranslator.create(tmp_path)
        assert translator.root_dir == tmp_path

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_basic(
        self, mock_markdown_translator_class, temp_notebook_file
    ):
        """Test basic notebook translation functionality."""
        # Setup mock
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated Content\n\nTranslated text."
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        notebook_content = temp_notebook_file.read_text(encoding="utf-8")
        result = await translator.translate_notebook(
            notebook_content, "es", source_path=temp_notebook_file
        )

        # Verify result is valid JSON
        translated_notebook = json.loads(result)
        assert "cells" in translated_notebook
        assert len(translated_notebook["cells"]) == 3

        # Verify markdown cells were processed
        assert mock_translator.translate_markdown.call_count == 2  # Two markdown cells

        # Verify code cell remains unchanged
        code_cell = translated_notebook["cells"][1]
        assert code_cell["cell_type"] == "code"
        assert "print('Hello, World!')" in "".join(code_cell["source"])

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_empty_cells(
        self, mock_markdown_translator_class, tmp_path
    ):
        """Test translation with empty markdown cells."""
        # Create notebook with empty cells
        notebook_content = {
            "cells": [
                {"cell_type": "markdown", "metadata": {}, "source": []},
                {"cell_type": "markdown", "metadata": {}, "source": ""},
                {"cell_type": "code", "metadata": {}, "source": ["print('test')"]},
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 4,
        }

        notebook_file = tmp_path / "empty_test.ipynb"
        with open(notebook_file, "w", encoding="utf-8") as f:
            json.dump(notebook_content, f)

        # Setup mock
        mock_translator = AsyncMock()
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            notebook_file.read_text(encoding="utf-8"),
            "es",
            source_path=notebook_file,
        )

        # Verify no translation calls were made for empty cells
        mock_translator.translate_markdown.assert_not_called()

        # Verify result is valid
        translated_notebook = json.loads(result)
        assert len(translated_notebook["cells"]) == 3

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_with_list_source(
        self, mock_markdown_translator_class, tmp_path
    ):
        """Test translation with source as list of strings."""
        # Create notebook with list-based source
        notebook_content = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["# Title\n", "\n", "Some content"],
                }
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 4,
        }

        notebook_file = tmp_path / "list_test.ipynb"
        with open(notebook_file, "w", encoding="utf-8") as f:
            json.dump(notebook_content, f)

        # Setup mock
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated Title\n\nTranslated content"
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            notebook_file.read_text(encoding="utf-8"),
            "es",
            source_path=notebook_file,
        )

        # Verify translation was called
        mock_translator.translate_markdown.assert_called_once()

        # Verify result maintains list format
        translated_notebook = json.loads(result)
        cell_source = translated_notebook["cells"][0]["source"]
        assert isinstance(cell_source, list)
        assert all(isinstance(line, str) for line in cell_source)

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_rewrites_markdown_cell_paths(
        self, mock_markdown_translator_class, tmp_path
    ):
        root_dir = tmp_path
        notebook_file = root_dir / "docs" / "tutorial.ipynb"
        image_file = root_dir / "docs" / "images" / "hero.png"
        translations_dir = root_dir / "translations"
        image_dir = root_dir / "translated_images"
        target_path = translations_dir / "ko" / "docs" / "tutorial.ipynb"

        notebook_file.parent.mkdir(parents=True)
        image_file.parent.mkdir(parents=True)
        translations_dir.mkdir()
        image_dir.mkdir()
        image_file.write_text("image", encoding="utf-8")
        notebook_file.write_text(
            json.dumps(
                {
                    "cells": [
                        {
                            "cell_type": "markdown",
                            "metadata": {},
                            "source": ["# Title\n", "![Hero](images/hero.png)\n"],
                        }
                    ],
                    "metadata": {},
                    "nbformat": 4,
                    "nbformat_minor": 4,
                }
            ),
            encoding="utf-8",
        )

        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated\n\n![Hero](images/hero.png)"
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        translator = JupyterNotebookTranslator.create(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
        )
        result = await translator.translate_notebook(
            notebook_file.read_text(encoding="utf-8"),
            "ko",
            source_path=notebook_file,
        )
        result = rewrite_notebook_paths(
            result,
            source_path=notebook_file,
            target_path=target_path,
            policy=MarkdownPathRewritePolicy(
                language_code="ko",
                root_dir=root_dir,
                translations_dir=translations_dir,
                translated_images_dir=image_dir,
                translation_types=["markdown", "notebook", "images"],
            ),
        )

        translated_notebook = json.loads(result)
        cell_source = "".join(translated_notebook["cells"][0]["source"])

        assert "images/hero.png" not in cell_source
        assert "../../../translated_images/ko/hero." in cell_source
        assert cell_source.endswith(".webp)\n")

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_does_not_embed_metadata(
        self,
        mock_markdown_translator_class,
        temp_notebook_file,
        tmp_path,
    ):
        """Notebook translation should NOT embed coopTranslator metadata (centralized JSON is used)."""
        # Setup mock translator
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated Content"
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator with root directory and translate without disclaimer for simplicity
        translator = JupyterNotebookTranslator.create(tmp_path)
        result = await translator.translate_notebook(
            temp_notebook_file.read_text(encoding="utf-8"),
            "ko",
            source_path=temp_notebook_file,
        )

        # Verify result includes notebook metadata but not coopTranslator section
        translated_notebook = json.loads(result)
        assert "metadata" in translated_notebook
        assert "coopTranslator" not in translated_notebook["metadata"]

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_handles_translation_errors(
        self, mock_markdown_translator_class, temp_notebook_file, caplog
    ):
        """Test that notebook translation handles individual cell translation errors gracefully."""
        # Setup mock translator that raises exception
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            side_effect=Exception("Translation API error")
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file.read_text(encoding="utf-8"),
            "ko",
            source_path=temp_notebook_file,
        )

        # Verify translation still completes (graceful error handling)
        translated_notebook = json.loads(result)
        assert "cells" in translated_notebook

        # Verify warning was logged
        assert "Failed to translate cell" in caplog.text

        # Verify original content is preserved when translation fails
        markdown_cells = [
            cell
            for cell in translated_notebook["cells"]
            if cell["cell_type"] == "markdown"
        ]
        assert len(markdown_cells) > 0
        # Original content should be preserved
        assert "Hello World" in "".join(markdown_cells[0]["source"])

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_preserves_notebook_structure(
        self, mock_markdown_translator_class, temp_notebook_file
    ):
        """Test that notebook translation preserves the overall notebook structure."""
        # Setup mock
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated Title\n\nTranslated content"
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file.read_text(encoding="utf-8"),
            "ko",
            source_path=temp_notebook_file,
        )

        # Parse result
        translated_notebook = json.loads(result)

        # Verify notebook structure is preserved
        assert translated_notebook["nbformat"] == 4
        assert translated_notebook["nbformat_minor"] == 4
        assert "kernelspec" in translated_notebook["metadata"]

        # Verify cell count and types are preserved
        assert len(translated_notebook["cells"]) == 3
        cell_types = [cell["cell_type"] for cell in translated_notebook["cells"]]
        assert cell_types == ["markdown", "code", "markdown"]

        # Verify code cells are completely unchanged
        code_cell = translated_notebook["cells"][1]
        expected_code_source = [
            "print('Hello, World!')\n",
            "# This should not be translated",
        ]
        assert code_cell["source"] == expected_code_source
        assert code_cell["execution_count"] is None

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_does_not_add_disclaimer_in_core(
        self, mock_markdown_translator_class, temp_notebook_file
    ):
        """Notebook core translation leaves disclaimer insertion to the project layer."""
        # Setup mock translator
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated Title\n\nTranslated content"
        )
        mock_translator.generate_disclaimer = AsyncMock(
            return_value="**Disclaimer**: This document has been translated using an AI translation service."
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file.read_text(encoding="utf-8"),
            "ko",
            source_path=temp_notebook_file,
        )

        # Parse result
        translated_notebook = json.loads(result)

        # Verify no disclaimer cell was added
        cells = translated_notebook["cells"]
        assert len(cells) == 3

        # Verify generate_disclaimer was not called
        mock_translator.generate_disclaimer.assert_not_called()
