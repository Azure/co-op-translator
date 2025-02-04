import pytest
from unittest.mock import AsyncMock, MagicMock
from co_op_translator.core.project.translation_manager import TranslationManager


@pytest.fixture
def temp_project_dir(tmp_path):
    """Creates a temporary project directory structure."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "test.md").write_text(
        "# Test Document\nThis is a test.", encoding="utf-8"
    )

    images_dir = tmp_path / "images"
    images_dir.mkdir()
    (images_dir / "test.png").touch()

    translations_dir = tmp_path / "translations"
    translations_dir.mkdir()

    return tmp_path


@pytest.fixture
def mock_translation_manager(temp_project_dir):
    """Creates a fully mocked instance of TranslationManager."""
    manager = MagicMock(spec=TranslationManager)

    # Mock all async methods
    manager.translate_markdown = AsyncMock()
    manager.translate_image = AsyncMock()
    manager.translate_all_markdown_files = AsyncMock()
    manager.translate_all_image_files = AsyncMock()
    manager.process_api_requests_parallel = AsyncMock()
    manager.process_api_requests_sequential = AsyncMock()

    # Set up common attributes
    manager.root_dir = temp_project_dir
    manager.translations_dir = temp_project_dir / "translations"
    manager.image_dir = temp_project_dir / "translated_images"
    manager.language_codes = ["ko", "ja"]

    return manager


@pytest.mark.asyncio
async def test_translate_markdown(mock_translation_manager, temp_project_dir):
    """Tests the translation of a single markdown file."""
    md_file = temp_project_dir / "docs" / "test.md"
    translated_content = "# Test Document\nThis is a translated test."

    # Setup mock
    mock_translation_manager.markdown_translator = MagicMock()
    mock_translation_manager.markdown_translator.translate_markdown = AsyncMock(
        return_value=translated_content
    )
    mock_translation_manager.translate_markdown = AsyncMock(
        return_value=translated_content
    )

    # Call and verify
    mock_translation_manager.translate_markdown.assert_not_called()
    result = await mock_translation_manager.translate_markdown(md_file, "ko")
    assert result == translated_content
    mock_translation_manager.translate_markdown.assert_awaited_once_with(md_file, "ko")


@pytest.mark.asyncio
async def test_translate_image(mock_translation_manager, temp_project_dir):
    """Tests the translation of a single image file."""
    image_file = temp_project_dir / "images" / "test.png"
    expected_translated_path = str(
        temp_project_dir / "translated_images" / "ko" / "images" / "test.png"
    )

    # Setup mock
    mock_translation_manager.image_translator = MagicMock()
    mock_translation_manager.image_translator.translate_image = MagicMock(
        return_value=expected_translated_path
    )
    mock_translation_manager.translate_image = AsyncMock(
        return_value=expected_translated_path
    )

    # Call and verify
    mock_translation_manager.translate_image.assert_not_called()
    result = await mock_translation_manager.translate_image(image_file, "ko")
    assert result == expected_translated_path
    mock_translation_manager.translate_image.assert_awaited_once_with(image_file, "ko")


@pytest.mark.asyncio
async def test_translate_all_markdown_files(mock_translation_manager, temp_project_dir):
    """Tests the translation of all markdown files."""
    expected_count = 2  # One for each language
    mock_translation_manager.translate_all_markdown_files = AsyncMock(
        return_value=(expected_count, [])
    )

    # Call and verify
    mock_translation_manager.translate_all_markdown_files.assert_not_called()
    count, errors = await mock_translation_manager.translate_all_markdown_files()
    assert count == expected_count
    assert not errors
    mock_translation_manager.translate_all_markdown_files.assert_awaited_once()


@pytest.mark.asyncio
async def test_translate_all_image_files(mock_translation_manager, temp_project_dir):
    """Tests the translation of all image files."""
    expected_count = 2  # One for each language
    mock_translation_manager.translate_all_image_files = AsyncMock(
        return_value=(expected_count, [])
    )

    # Call and verify
    mock_translation_manager.translate_all_image_files.assert_not_called()
    count, errors = await mock_translation_manager.translate_all_image_files()
    assert count == expected_count
    assert not errors
    mock_translation_manager.translate_all_image_files.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_api_requests_parallel(mock_translation_manager):
    """Tests parallel API request processing."""
    mock_tasks = [AsyncMock() for _ in range(3)]
    mock_translation_manager.process_api_requests_parallel = AsyncMock()

    await mock_translation_manager.process_api_requests_parallel(
        mock_tasks, "Test tasks"
    )

    mock_translation_manager.process_api_requests_parallel.assert_called_once_with(
        mock_tasks, "Test tasks"
    )


@pytest.mark.asyncio
async def test_process_api_requests_sequential(mock_translation_manager):
    """Tests sequential API request processing."""
    mock_tasks = [AsyncMock() for _ in range(3)]
    mock_translation_manager.process_api_requests_sequential = AsyncMock()

    await mock_translation_manager.process_api_requests_sequential(
        mock_tasks, "Test tasks"
    )

    mock_translation_manager.process_api_requests_sequential.assert_called_once_with(
        mock_tasks, "Test tasks"
    )


@pytest.mark.asyncio
async def test_get_outdated_translations(mock_translation_manager, temp_project_dir):
    """Tests the detection of outdated translation files."""
    # Setup test files
    ko_dir = temp_project_dir / "translations" / "ko"
    ko_dir.mkdir(parents=True, exist_ok=True)
    test_md = temp_project_dir / "test.md"
    test_md.write_text("# Test Document\nThis is a test.", encoding="utf-8")
    ko_test_md = ko_dir / "test.md"
    ko_test_md.parent.mkdir(parents=True, exist_ok=True)
    ko_test_md.write_text("# 테스트 문서\n이것은 테스트입니다.", encoding="utf-8")

    # Mock _is_translation_outdated to return True for our test file
    mock_translation_manager._is_translation_outdated = MagicMock(return_value=True)
    mock_translation_manager.get_outdated_translations = (
        TranslationManager.get_outdated_translations.__get__(mock_translation_manager)
    )
    mock_translation_manager.root_dir = temp_project_dir
    mock_translation_manager.translations_dir = temp_project_dir / "translations"
    mock_translation_manager.language_codes = ["ko"]

    # Get outdated translations
    outdated_files = mock_translation_manager.get_outdated_translations()

    # Verify results
    assert len(outdated_files) == 1
    original_file, translation_file = outdated_files[0]
    assert original_file.name == "test.md"
    assert translation_file.parent.name == "ko"


@pytest.mark.asyncio
async def test_retranslate_outdated_files(mock_translation_manager, temp_project_dir):
    """Tests retranslation of outdated files."""
    # Setup test files
    test_md = temp_project_dir / "test.md"
    test_md.write_text("# Test Document\nThis is a test.", encoding="utf-8")

    ko_dir = temp_project_dir / "translations" / "ko"
    ko_dir.mkdir(parents=True, exist_ok=True)
    ko_test_md = ko_dir / "test.md"
    ko_test_md.write_text("# 테스트 문서\n이것은 테스트입니다.", encoding="utf-8")

    # Create a list of outdated files
    outdated_files = [(test_md, ko_test_md)]

    # Mock translate_markdown
    mock_translation_manager.markdown_translator = MagicMock()
    mock_translation_manager.markdown_translator.translate_markdown = AsyncMock(
        return_value="# 테스트 문서\n이것은 테스트입니다."
    )
    mock_translation_manager.markdown_translator.create_metadata = MagicMock(
        return_value={"file_hash": "test_hash"}
    )
    mock_translation_manager.translate_markdown = AsyncMock(
        return_value=str(ko_test_md)
    )
    mock_translation_manager.retranslate_outdated_files = (
        TranslationManager.retranslate_outdated_files.__get__(mock_translation_manager)
    )
    mock_translation_manager.translations_dir = ko_dir.parent

    # Call retranslate_outdated_files
    await mock_translation_manager.retranslate_outdated_files(outdated_files)

    # Verify results
    mock_translation_manager.translate_markdown.assert_awaited_once_with(test_md, "ko")


@pytest.mark.asyncio
async def test_translate_project_async_with_outdated(
    mock_translation_manager, temp_project_dir
):
    """Tests the full project translation process with outdated files."""
    # Setup test files
    test_md = temp_project_dir / "test.md"
    test_md.write_text("# Test Document\nThis is a test.", encoding="utf-8")

    # Mock necessary methods
    mock_translation_manager.get_outdated_translations = MagicMock(
        return_value=[(test_md, temp_project_dir / "translations" / "ko" / "test.md")]
    )
    mock_translation_manager.retranslate_outdated_files = AsyncMock()
    mock_translation_manager.translate_all_markdown_files = AsyncMock()
    mock_translation_manager.translate_all_image_files = AsyncMock()
    mock_translation_manager.directory_manager = MagicMock()
    mock_translation_manager.directory_manager.sync_directory_structure = MagicMock(
        return_value=(0, 0, [])
    )
    mock_translation_manager.directory_manager.cleanup_orphaned_translations = (
        MagicMock(return_value=0)
    )
    mock_translation_manager.translate_project_async = (
        TranslationManager.translate_project_async.__get__(mock_translation_manager)
    )

    # Call translate_project_async
    await mock_translation_manager.translate_project_async(markdown=True)

    # Verify the sequence of operations
    mock_translation_manager.directory_manager.sync_directory_structure.assert_called_once()
    mock_translation_manager.directory_manager.cleanup_orphaned_translations.assert_called_once()
    mock_translation_manager.get_outdated_translations.assert_called_once()
    mock_translation_manager.retranslate_outdated_files.assert_called_once()
    mock_translation_manager.translate_all_markdown_files.assert_called_once()
