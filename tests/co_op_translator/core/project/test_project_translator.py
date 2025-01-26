"""
Tests for ProjectTranslator class
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from co_op_translator.core.project.project_translator import ProjectTranslator


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary project directory structure."""
    # Create project structure
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "test.md").write_text("# Test Document\nThis is a test.")

    images_dir = tmp_path / "images"
    images_dir.mkdir()
    (images_dir / "test.png").touch()

    translations_dir = tmp_path / "translations"
    translations_dir.mkdir()

    return tmp_path


@pytest.fixture
def project_translator(temp_project_dir):
    """Create a ProjectTranslator instance with mocked dependencies."""
    with (
        patch(
            "co_op_translator.core.llm.text_translator.TextTranslator"
        ) as mock_text_translator,
        patch(
            "co_op_translator.core.llm.markdown_translator.MarkdownTranslator"
        ) as mock_markdown_translator,
        patch(
            "co_op_translator.core.vision.image_translator.ImageTranslator"
        ) as mock_image_translator,
        patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider"
        ) as mock_get_provider,
    ):
        # Setup mock translators and config
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()
        mock_get_provider.return_value = "azure"  # Mock LLM provider

        translator = ProjectTranslator("ko ja", root_dir=temp_project_dir)
        return translator


def test_project_translator_init(project_translator, temp_project_dir):
    """Test ProjectTranslator initialization"""
    # Test normal initialization
    translator = project_translator
    assert translator.language_codes == ["ko", "ja"]
    assert translator.root_dir == temp_project_dir.resolve()
    assert translator.translations_dir == temp_project_dir / "translations"
    assert translator.image_dir == temp_project_dir / "translated_images"
    assert not translator.markdown_only

    # Test markdown-only mode
    with (
        patch(
            "co_op_translator.core.llm.text_translator.TextTranslator"
        ) as mock_text_translator,
        patch(
            "co_op_translator.core.llm.markdown_translator.MarkdownTranslator"
        ) as mock_markdown_translator,
        patch(
            "co_op_translator.core.vision.image_translator.ImageTranslator"
        ) as mock_image_translator,
    ):
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_dir, markdown_only=True
        )
        assert translator.markdown_only
        assert translator.image_translator is None


def test_translate_project(project_translator):
    """Test the synchronous translate_project method."""
    # Setup
    project_translator.translation_manager.translate_project_async = AsyncMock()

    # Execute
    project_translator.translate_project(markdown=True, images=True)

    # Verify
    project_translator.translation_manager.translate_project_async.assert_awaited_once_with(
        markdown=True, images=True, update=False
    )


def test_markdown_only_mode(temp_project_dir):
    """Test ProjectTranslator in markdown-only mode."""
    with (
        patch(
            "co_op_translator.core.llm.text_translator.TextTranslator"
        ) as mock_text_translator,
        patch(
            "co_op_translator.core.llm.markdown_translator.MarkdownTranslator"
        ) as mock_markdown_translator,
        patch(
            "co_op_translator.core.vision.image_translator.ImageTranslator"
        ) as mock_image_translator,
    ):
        # Setup mocks
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()

        # Create translator in markdown-only mode
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_dir, markdown_only=True
        )

        # Verify
        assert translator.markdown_only
        assert translator.image_translator is None
        assert not mock_image_translator.create.called
