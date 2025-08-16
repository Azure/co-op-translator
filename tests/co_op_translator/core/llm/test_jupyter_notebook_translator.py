"""
Tests for JupyterNotebookTranslator functionality.
"""

import json
import pytest
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
            temp_notebook_file, "es", use_translated_images=False, add_disclaimer=False
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
            notebook_file, "es", add_disclaimer=False
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
            notebook_file, "es", add_disclaimer=False
        )

        # Verify translation was called
        mock_translator.translate_markdown.assert_called_once()

        # Verify result maintains list format
        translated_notebook = json.loads(result)
        cell_source = translated_notebook["cells"][0]["source"]
        assert isinstance(cell_source, list)
        assert all(isinstance(line, str) for line in cell_source)

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @patch(
        "co_op_translator.core.llm.jupyter_notebook_translator.add_notebook_metadata"
    )
    @pytest.mark.asyncio
    async def test_translate_notebook_adds_metadata(
        self,
        mock_add_metadata,
        mock_markdown_translator_class,
        temp_notebook_file,
        tmp_path,
    ):
        """Test that notebook translation adds coopTranslator metadata."""
        # Setup mock translator
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# Translated Content"
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Setup mock metadata function
        expected_metadata = {
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3",
                },
                "coopTranslator": {
                    "original_hash": "test_hash",
                    "translation_date": "2025-01-26T14:30:00+00:00",
                    "source_file": "test.ipynb",
                    "language_code": "ko",
                },
            }
        }
        mock_add_metadata.return_value = {"cells": [], **expected_metadata}

        # Create translator with root directory
        translator = JupyterNotebookTranslator.create(tmp_path)
        result = await translator.translate_notebook(temp_notebook_file, "ko")

        # Verify add_notebook_metadata was called with correct parameters
        mock_add_metadata.assert_called_once()
        call_args = mock_add_metadata.call_args
        assert call_args[0][1] == temp_notebook_file  # original_path
        assert call_args[0][2] == "ko"  # language_code
        assert call_args[0][3] == tmp_path  # root_dir

        # Verify result includes metadata
        translated_notebook = json.loads(result)
        assert "metadata" in translated_notebook

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
        result = await translator.translate_notebook(temp_notebook_file, "ko")

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
            return_value="# 번역된 제목\n\n번역된 내용"
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file, "ko", add_disclaimer=False
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
    async def test_translate_notebook_with_disclaimer(
        self, mock_markdown_translator_class, temp_notebook_file
    ):
        """Test that notebook translation adds disclaimer cell when enabled."""
        # Setup mock translator
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# 번역된 제목\n\n번역된 내용"
        )
        mock_translator.generate_disclaimer = AsyncMock(
            return_value="**면책조항**: 이 문서는 AI 번역 서비스를 사용하여 번역되었습니다."
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate with disclaimer
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file, "ko", add_disclaimer=True
        )

        # Parse result
        translated_notebook = json.loads(result)

        # Verify disclaimer cell was added at the end
        cells = translated_notebook["cells"]
        assert len(cells) == 4  # Original 3 + 1 disclaimer

        disclaimer_cell = cells[-1]  # Last cell should be disclaimer
        assert disclaimer_cell["cell_type"] == "markdown"
        disclaimer_content = "".join(disclaimer_cell["source"])
        assert "면책조항" in disclaimer_content
        assert "---" in disclaimer_content  # Separator line

        # Verify generate_disclaimer was called
        mock_translator.generate_disclaimer.assert_called_once_with("ko")

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_without_disclaimer(
        self, mock_markdown_translator_class, temp_notebook_file
    ):
        """Test that notebook translation skips disclaimer when disabled."""
        # Setup mock translator
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# 번역된 제목\n\n번역된 내용"
        )
        mock_translator.generate_disclaimer = AsyncMock(
            return_value="**면책조항**: 이 문서는 AI 번역 서비스를 사용하여 번역되었습니다."
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate without disclaimer
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file, "ko", add_disclaimer=False
        )

        # Parse result
        translated_notebook = json.loads(result)

        # Verify no disclaimer cell was added
        cells = translated_notebook["cells"]
        assert len(cells) == 3  # Original 3, no disclaimer

        # Verify generate_disclaimer was not called
        mock_translator.generate_disclaimer.assert_not_called()

    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @pytest.mark.asyncio
    async def test_translate_notebook_disclaimer_generation_fails(
        self, mock_markdown_translator_class, temp_notebook_file
    ):
        """Test that notebook translation handles disclaimer generation failure gracefully."""
        # Setup mock translator with failing disclaimer generation
        mock_translator = AsyncMock()
        mock_translator.translate_markdown = AsyncMock(
            return_value="# 번역된 제목\n\n번역된 내용"
        )
        mock_translator.generate_disclaimer = AsyncMock(
            return_value=""  # Empty disclaimer (failure case)
        )
        mock_markdown_translator_class.create.return_value = mock_translator

        # Create translator and translate
        translator = JupyterNotebookTranslator.create()
        result = await translator.translate_notebook(
            temp_notebook_file, "ko", add_disclaimer=True
        )

        # Parse result
        translated_notebook = json.loads(result)

        # Verify no disclaimer cell was added when generation fails
        cells = translated_notebook["cells"]
        assert len(cells) == 3  # Original 3, no disclaimer due to failure

        # Verify generate_disclaimer was called but failed
        mock_translator.generate_disclaimer.assert_called_once_with("ko")
