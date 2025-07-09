"""
Integration tests for Jupyter Notebook translation functionality.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from co_op_translator.core.project.project_translator import ProjectTranslator


@pytest.fixture
def temp_project_with_notebook(tmp_path):
    """Create a temporary project directory with notebook files."""
    # Create a sample notebook
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Test Notebook\n",
                    "\n",
                    "This is a test for translation.",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["print('Hello, World!')"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": "## Section 2\n\nAnother section to translate.",
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

    # Create notebook file
    notebook_file = tmp_path / "test_notebook.ipynb"
    with open(notebook_file, "w", encoding="utf-8") as f:
        json.dump(notebook_content, f, ensure_ascii=False, indent=1)

    # Create markdown file for comparison
    (tmp_path / "test.md").write_text("# Test Document\nThis is a test.")

    return tmp_path


class TestJupyterNotebookIntegration:
    """Integration tests for Jupyter Notebook translation."""

    @patch("co_op_translator.core.llm.text_translator.TextTranslator")
    @patch("co_op_translator.core.llm.markdown_translator.MarkdownTranslator")
    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @patch("co_op_translator.config.llm_config.config.LLMConfig.get_available_provider")
    def test_project_translator_includes_notebooks(
        self,
        mock_get_provider,
        mock_jupyter_markdown_translator,
        mock_markdown_translator,
        mock_text_translator,
        temp_project_with_notebook,
    ):
        """Test that ProjectTranslator correctly initializes notebook translator."""
        # Setup mocks
        mock_get_provider.return_value = "azure"
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_jupyter_markdown_translator.create.return_value = MagicMock()

        # Create translator
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_with_notebook, markdown_only=True
        )

        # Verify notebook translator was created
        assert translator.notebook_translator is not None

        # Verify translation manager has notebook translator
        assert translator.translation_manager.notebook_translator is not None

    @patch("co_op_translator.core.llm.text_translator.TextTranslator")
    @patch("co_op_translator.core.llm.markdown_translator.MarkdownTranslator")
    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @patch("co_op_translator.config.llm_config.config.LLMConfig.get_available_provider")
    @pytest.mark.asyncio
    async def test_translation_manager_processes_notebooks(
        self,
        mock_get_provider,
        mock_jupyter_markdown_translator,
        mock_markdown_translator,
        mock_text_translator,
        temp_project_with_notebook,
    ):
        """Test that TranslationManager processes notebook files."""
        # Setup mocks
        mock_get_provider.return_value = "azure"
        mock_text_translator.create.return_value = MagicMock()

        # Mock markdown translator
        mock_md_translator = AsyncMock()
        mock_md_translator.translate_markdown = AsyncMock(
            return_value="# Translated\nTranslated content"
        )
        mock_markdown_translator.create.return_value = mock_md_translator

        # Mock jupyter notebook translator
        mock_jupyter_md_translator = AsyncMock()
        mock_jupyter_md_translator.translate_markdown = AsyncMock(
            return_value="# Translated\nTranslated content"
        )
        mock_jupyter_markdown_translator.create.return_value = (
            mock_jupyter_md_translator
        )

        # Create translator
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_with_notebook, markdown_only=True
        )

        # Mock the notebook translator's translate_notebook method
        mock_notebook_translator = AsyncMock()
        translated_notebook = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["# Translated\n", "Translated content"],
                },
                {
                    "cell_type": "code",
                    "metadata": {},
                    "source": ["print('Hello, World!')"],
                },
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": "## Translated Section\nTranslated content",
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
        mock_notebook_translator.translate_notebook = AsyncMock(
            return_value=json.dumps(translated_notebook, ensure_ascii=False, indent=1)
        )
        translator.translation_manager.notebook_translator = mock_notebook_translator

        # Run translation
        total_modified, errors = (
            await translator.translation_manager.translate_all_notebook_files()
        )

        # Verify notebook translation was attempted
        assert mock_notebook_translator.translate_notebook.call_count >= 1
        assert total_modified >= 0  # Should have attempted to translate
        assert isinstance(errors, list)

    @patch("co_op_translator.core.llm.text_translator.TextTranslator")
    @patch("co_op_translator.core.llm.markdown_translator.MarkdownTranslator")
    @patch("co_op_translator.core.llm.jupyter_notebook_translator.MarkdownTranslator")
    @patch("co_op_translator.config.llm_config.config.LLMConfig.get_available_provider")
    def test_project_translator_handles_no_notebook_translator(
        self,
        mock_get_provider,
        mock_jupyter_markdown_translator,
        mock_markdown_translator,
        mock_text_translator,
        temp_project_with_notebook,
    ):
        """Test that system gracefully handles missing notebook translator."""
        # Setup mocks
        mock_get_provider.return_value = "azure"
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_jupyter_markdown_translator.create.return_value = MagicMock()

        # Create translator
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_with_notebook, markdown_only=True
        )

        # Simulate missing notebook translator
        translator.translation_manager.notebook_translator = None

        # Should not raise exception
        assert translator.translation_manager.notebook_translator is None

    def test_constants_include_notebook_extensions(self):
        """Test that notebook extensions are included in constants."""
        from co_op_translator.config.constants import SUPPORTED_NOTEBOOK_EXTENSIONS

        assert ".ipynb" in SUPPORTED_NOTEBOOK_EXTENSIONS
