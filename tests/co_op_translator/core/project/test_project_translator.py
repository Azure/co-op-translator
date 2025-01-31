import pytest
from pathlib import Path
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from co_op_translator.core.project.project_translator import ProjectTranslator
from unittest.mock import ANY


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

        # Mock async methods
        translator.translate_all_markdown_files = AsyncMock(return_value=(2, []))
        translator.translate_all_image_files = AsyncMock(return_value=(2, []))

        return translator


def test_translate_project(project_translator):
    """Test the synchronous translate_project method."""
    # Setup
    with patch.object(asyncio, "run", side_effect=lambda x: None) as mock_run:
        # Execute
        project_translator.translate_project(images=True, markdown=True)
        # Verify
        mock_run.assert_called_once()


@pytest.mark.asyncio
async def test_check_and_retry_translations(project_translator, temp_project_dir):
    """Test checking and retrying translations."""
    # Setup
    md_file = temp_project_dir / "docs" / "test.md"
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    translated_file.parent.mkdir(parents=True)
    translated_file.write_text(
        "# Test\nBroken translation"
    )  # Create a "broken" translation

    project_translator.markdown_translator.translate_markdown = AsyncMock(
        return_value="# 테스트 문서\n이것은 테스트입니다."
    )

    # Execute
    await project_translator.check_and_retry_translations()

    # Verify
    project_translator.markdown_translator.translate_markdown.assert_called()
    assert translated_file.exists()


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
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider"
        ) as mock_get_provider,
    ):
        # Setup mocks
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_get_provider.return_value = "azure"  # Mock LLM provider

        # Create translator in markdown-only mode
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_dir, markdown_only=True
        )

        # Verify
        assert translator.markdown_only is True
        assert translator.image_translator is None
