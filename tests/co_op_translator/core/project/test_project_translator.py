import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from co_op_translator.core.project.project_translator import ProjectTranslator


def test_deferred_translators_initialize_atomically_and_attach_to_manager(tmp_path):
    translator = ProjectTranslator(
        "ko",
        root_dir=tmp_path,
        translation_types=["markdown", "images", "notebook"],
        initialize_translators=False,
    )
    text_instance = MagicMock()
    image_instance = MagicMock()
    markdown_instance = MagicMock()
    notebook_instance = MagicMock()

    with (
        patch(
            "co_op_translator.core.project.project_translator.text_translator.TextTranslator.create",
            return_value=text_instance,
        ) as create_text,
        patch(
            "co_op_translator.core.project.project_translator.image_translator.ImageTranslator.create",
            return_value=image_instance,
        ) as create_image,
        patch(
            "co_op_translator.core.project.project_translator.markdown_translator.MarkdownTranslator.create",
            return_value=markdown_instance,
        ) as create_markdown,
        patch(
            "co_op_translator.core.project.project_translator.JupyterNotebookTranslator.create",
            side_effect=[RuntimeError("temporary failure"), notebook_instance],
        ) as create_notebook,
    ):
        with pytest.raises(RuntimeError, match="temporary failure"):
            translator._initialize_translators()

        assert translator.text_translator is None
        assert translator.image_translator is None
        assert translator.markdown_translator is None
        assert translator.notebook_translator is None

        translator._initialize_translators()
        translator._initialize_translators()

    assert translator.text_translator is text_instance
    assert translator.image_translator is image_instance
    assert translator.markdown_translator is markdown_instance
    assert translator.notebook_translator is notebook_instance
    assert translator.translation_manager.markdown_translator is markdown_instance
    assert translator.translation_manager.image_translator is image_instance
    assert translator.translation_manager.notebook_translator is notebook_instance
    assert create_text.call_count == 2
    assert create_image.call_count == 2
    assert create_markdown.call_count == 2
    assert create_notebook.call_count == 2


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
            "co_op_translator.core.project.project_translator.JupyterNotebookTranslator"
        ) as mock_jupyter_translator,
    ):
        # Setup mock translators
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()
        mock_jupyter_translator.create.return_value = MagicMock()

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
    project_translator.translate_project()

    project_translator.translation_manager.translate_project_async.assert_awaited_once_with(
        update=False,
        fast_mode=False,
    )


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
            "co_op_translator.core.project.project_translator.JupyterNotebookTranslator"
        ) as mock_jupyter_translator,
    ):
        # Setup translator mocks
        mock_text_translator_instance = MagicMock()
        mock_text_translator.create.return_value = mock_text_translator_instance

        mock_markdown_translator_instance = MagicMock()
        mock_markdown_translator.create.return_value = mock_markdown_translator_instance

        mock_jupyter_translator_instance = MagicMock()
        mock_jupyter_translator.create.return_value = mock_jupyter_translator_instance

        # Create translator in markdown-only mode
        translator = ProjectTranslator(
            "ko ja", root_dir=temp_project_dir, translation_types=["markdown"]
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
        assert translator.translation_types == ["markdown"]
        assert translator.image_translator is None
        mock_jupyter_translator.create.assert_not_called()

        # Test async operation to ensure all coroutines are properly handled
        await translator.translation_manager.translate_project_async()
        # Verify that translate_project_async was called (no need to check args since translation_types is set in init)
        translator.translation_manager.translate_project_async.assert_called_once()


@pytest.mark.asyncio
async def test_project_translator_custom_output_directories(temp_project_dir):
    """ProjectTranslator should honor custom translations_dir and image_dir."""
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
            "co_op_translator.core.project.project_translator.JupyterNotebookTranslator"
        ) as mock_jupyter_translator,
    ):
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()
        mock_jupyter_translator.create.return_value = MagicMock()

        custom_translations = temp_project_dir / "content" / "i18n"
        custom_images = temp_project_dir / "public" / "translated_media"

        translator = ProjectTranslator(
            "ko ja",
            root_dir=temp_project_dir,
            translation_types=["markdown", "notebook", "images"],
            translations_dir=custom_translations,
            image_dir=custom_images,
        )

        assert translator.translations_dir == custom_translations.resolve()
        assert translator.image_dir == custom_images.resolve()
        assert (
            translator.translation_manager.translations_dir
            == translator.translations_dir
        )
        assert translator.translation_manager.image_dir == translator.image_dir
        assert (
            translator.directory_manager.translations_dir == translator.translations_dir
        )


@pytest.mark.asyncio
async def test_project_translator_relative_output_directories(temp_project_dir):
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
            "co_op_translator.core.project.project_translator.JupyterNotebookTranslator"
        ) as mock_jupyter_translator,
    ):
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()
        mock_jupyter_translator.create.return_value = MagicMock()

        translator = ProjectTranslator(
            "ko ja",
            root_dir=temp_project_dir,
            translation_types=["markdown", "notebook", "images"],
            translations_dir="content/i18n",
            image_dir="public/translated_media",
        )

        expected_translations = (temp_project_dir / "content" / "i18n").resolve()
        expected_images = (temp_project_dir / "public" / "translated_media").resolve()

        assert translator.translations_dir == expected_translations
        assert translator.image_dir == expected_images
