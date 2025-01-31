import pytest
from unittest.mock import AsyncMock, MagicMock
from co_op_translator.core.project.translation_manager import TranslationManager

@pytest.fixture
def temp_project_dir(tmp_path):
    """Creates a temporary project directory structure."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "test.md").write_text("# Test Document\nThis is a test.", encoding="utf-8")

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

def test_translate_markdown(mock_translation_manager, temp_project_dir):
    """Tests the translation of a single markdown file."""
    md_file = temp_project_dir / "docs" / "test.md"
    translated_content = "# Test Document\nThis is a translated test."
    
    # Setup mock
    mock_translation_manager.translate_markdown.return_value = translated_content
    
    # Call and verify
    mock_translation_manager.translate_markdown.assert_not_called()
    mock_translation_manager.translate_markdown(md_file, "ko")
    mock_translation_manager.translate_markdown.assert_called_once_with(md_file, "ko")

def test_translate_image(mock_translation_manager, temp_project_dir):
    """Tests the translation of a single image file."""
    image_file = temp_project_dir / "images" / "test.png"
    expected_translated_path = str(temp_project_dir / "translated_images" / "ko_test.png")
    
    # Setup mock
    mock_translation_manager.translate_image.return_value = expected_translated_path
    
    # Call and verify
    mock_translation_manager.translate_image.assert_not_called()
    mock_translation_manager.translate_image(image_file, "ko")
    mock_translation_manager.translate_image.assert_called_once_with(image_file, "ko")

def test_translate_all_markdown_files(mock_translation_manager, temp_project_dir):
    """Tests the translation of all markdown files."""
    expected_count = 2  # One for each language
    mock_translation_manager.translate_all_markdown_files.return_value = (expected_count, [])
    
    # Call and verify
    mock_translation_manager.translate_all_markdown_files.assert_not_called()
    mock_translation_manager.translate_all_markdown_files()
    mock_translation_manager.translate_all_markdown_files.assert_called_once()

def test_translate_all_image_files(mock_translation_manager, temp_project_dir):
    """Tests the translation of all image files."""
    expected_count = 2  # One for each language
    mock_translation_manager.translate_all_image_files.return_value = (expected_count, [])
    
    # Call and verify
    mock_translation_manager.translate_all_image_files.assert_not_called()
    mock_translation_manager.translate_all_image_files()
    mock_translation_manager.translate_all_image_files.assert_called_once()

def test_process_api_requests_parallel(mock_translation_manager):
    """Tests parallel API request processing."""
    mock_tasks = [AsyncMock(), AsyncMock()]
    
    # Call and verify
    mock_translation_manager.process_api_requests_parallel.assert_not_called()
    mock_translation_manager.process_api_requests_parallel(mock_tasks, "Test tasks")
    mock_translation_manager.process_api_requests_parallel.assert_called_once_with(mock_tasks, "Test tasks")

def test_process_api_requests_sequential(mock_translation_manager):
    """Tests sequential API request processing."""
    mock_tasks = [AsyncMock(), AsyncMock()]
    
    # Call and verify
    mock_translation_manager.process_api_requests_sequential.assert_not_called()
    mock_translation_manager.process_api_requests_sequential(mock_tasks, "Test tasks")
    mock_translation_manager.process_api_requests_sequential.assert_called_once_with(mock_tasks, "Test tasks")
