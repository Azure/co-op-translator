"""
Tests for JupyterNotebookTranslator functionality.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from co_op_translator.core.llm.jupyter_notebook_translator import (
    JupyterNotebookTranslator,
)


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
        result = await translator.translate_notebook(
            temp_notebook_file, "es", markdown_only=True
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
        result = await translator.translate_notebook(notebook_file, "es")

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
        result = await translator.translate_notebook(notebook_file, "es")

        # Verify translation was called
        mock_translator.translate_markdown.assert_called_once()

        # Verify result maintains list format
        translated_notebook = json.loads(result)
        cell_source = translated_notebook["cells"][0]["source"]
        assert isinstance(cell_source, list)
        assert all(isinstance(line, str) for line in cell_source)
