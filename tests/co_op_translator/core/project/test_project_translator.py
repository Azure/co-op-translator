import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.config.llm_config.provider import LLMProvider


@pytest.fixture
async def temp_project_dir(tmp_path):
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
async def project_translator(temp_project_dir):
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
            "co_op_translator.core.llm.jupyter_notebook_translator.JupyterNotebookTranslator"
        ) as mock_jupyter_translator,
        patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider"
        ) as mock_get_provider,
    ):
        # Setup mock translators and config
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()
        mock_jupyter_translator.create.return_value = MagicMock()
        mock_get_provider.return_value = LLMProvider.AZURE_OPENAI  # Mock LLM provider

        translator = ProjectTranslator("ko ja", root_dir=temp_project_dir)
        translator.translation_manager.translate_all_markdown_files = AsyncMock(
            return_value=(2, [])
        )
        translator.translation_manager.translate_all_image_files = AsyncMock(
            return_value=(0, [])
        )
        # Mock translate_project_async to avoid unawaited coroutine warning
        translator.translation_manager.translate_project_async = AsyncMock(
            return_value=None
        )

        yield translator


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

    # Mock translation methods with proper async behavior
    project_translator.translation_manager.check_outdated_files = AsyncMock(
        return_value=(1, [])
    )
    project_translator.translation_manager.translate_all_markdown_files = AsyncMock(
        return_value=(2, [])
    )
    project_translator.translation_manager.translate_all_image_files = AsyncMock(
        return_value=(0, [])
    )

    # Execute and verify
    total_count, errors = await project_translator.check_and_retry_translations()

    # Verify results
    assert total_count == 3  # 1 (outdated) + 2 (markdown) + 0 (images)
    assert errors == []  # No errors expected
    assert project_translator.translation_manager.check_outdated_files.called
    assert project_translator.translation_manager.translate_all_markdown_files.called
    assert project_translator.translation_manager.translate_all_image_files.called


def test_translate_project(project_translator):
    """Test the synchronous translate_project method."""
    # Setup
    with patch.object(asyncio, "run", side_effect=lambda x: None) as mock_run:
        # Execute
        project_translator.translate_project(images=True, markdown=True)
        # Verify
        mock_run.assert_called_once()


@pytest.mark.asyncio
async def test_markdown_only_mode(temp_project_dir):
    """Test ProjectTranslator in markdown-only mode."""
    with (
        patch(
            "co_op_translator.core.llm.text_translator.TextTranslator"
        ) as mock_text_translator,
        patch(
            "co_op_translator.core.llm.markdown_translator.MarkdownTranslator"
        ) as mock_markdown_translator,
        patch(
            "co_op_translator.core.llm.jupyter_notebook_translator.JupyterNotebookTranslator"
        ) as mock_jupyter_translator,
        patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider"
        ) as mock_get_provider,
    ):
        # Setup translator mocks
        mock_text_translator_instance = AsyncMock()
        mock_text_translator.create.return_value = mock_text_translator_instance

        mock_markdown_translator_instance = AsyncMock()
        mock_markdown_translator.create.return_value = mock_markdown_translator_instance

        mock_jupyter_translator_instance = AsyncMock()
        mock_jupyter_translator.create.return_value = mock_jupyter_translator_instance

        mock_get_provider.return_value = LLMProvider.AZURE_OPENAI

        # Create translator in markdown-only mode
        translator = ProjectTranslator(
            "ko ja", root_dir=temp_project_dir, markdown_only=True
        )

        # Mock the async methods after initialization
        translator.translation_manager.translate_project_async = AsyncMock()
        translator.translation_manager.check_outdated_files = AsyncMock(
            return_value=(0, [])
        )
        translator.translation_manager.translate_all_markdown_files = AsyncMock(
            return_value=(0, [])
        )
        translator.translation_manager.translate_all_image_files = AsyncMock(
            return_value=(0, [])
        )

        # Verify markdown-only mode configuration
        assert translator.markdown_only is True
        assert translator.image_translator is None

        # Test async operation to ensure all coroutines are properly handled
        await translator.translation_manager.translate_project_async(markdown=True)
        assert (
            translator.translation_manager.translate_project_async.call_args.kwargs[
                "markdown"
            ]
            is True
        )
