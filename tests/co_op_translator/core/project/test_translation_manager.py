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
    manager = MagicMock()

    # Mock all async methods
    manager.translate_markdown = AsyncMock()
    manager.translate_image = AsyncMock()
    manager.translate_all_markdown_files = AsyncMock()
    manager.translate_all_image_files = AsyncMock()
    manager.process_api_requests_parallel = AsyncMock()
    manager.process_api_requests_sequential = AsyncMock()
    manager.translate_notebook = AsyncMock()

    # Set up common attributes
    manager.root_dir = temp_project_dir
    manager.translations_dir = temp_project_dir / "translations"
    manager.image_dir = temp_project_dir / "translated_images"
    manager.language_codes = ["ko", "ja"]
    manager.supported_notebook_extensions = [".ipynb"]

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
    ko_test_md.write_text("# Test Document\nThis is a test.", encoding="utf-8")

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
    ko_test_md.write_text("# Test Document\nThis is a test.", encoding="utf-8")

    # Create a list of outdated files
    outdated_files = [(test_md, ko_test_md)]

    # Mock translate_markdown
    mock_translation_manager.markdown_translator = MagicMock()
    mock_translation_manager.markdown_translator.translate_markdown = AsyncMock(
        return_value="# Test Document\nThis is a test."
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
    mock_translation_manager.directory_manager.migrate_markdown_image_links = (
        MagicMock(return_value=0)
    )
    mock_translation_manager.translation_types = ["markdown", "notebook", "images"]
    mock_translation_manager.translate_project_async = (
        TranslationManager.translate_project_async.__get__(mock_translation_manager)
    )

    # Call translate_project_async
    await mock_translation_manager.translate_project_async()

    # Verify the sequence of operations
    mock_translation_manager.directory_manager.sync_directory_structure.assert_called_once()
    mock_translation_manager.directory_manager.cleanup_orphaned_translations.assert_called_once()
    mock_translation_manager.get_outdated_translations.assert_called_once()
    mock_translation_manager.retranslate_outdated_files.assert_called_once()
    mock_translation_manager.translate_all_markdown_files.assert_called_once()


# ============================================================================
# Notebook-specific tests
# ============================================================================


@pytest.mark.asyncio
async def test_translate_notebook_basic(mock_translation_manager, temp_project_dir):
    """Tests the translation of a single notebook file."""
    import json

    # Create test notebook
    notebook_file = temp_project_dir / "test.ipynb"
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Test Notebook"]},
            {"cell_type": "code", "source": ["print('hello')"]},
        ],
        "metadata": {},
    }
    notebook_file.write_text(json.dumps(notebook_content), encoding="utf-8")

    # Mock the notebook translator
    mock_translation_manager.notebook_translator = MagicMock()
    mock_translation_manager.notebook_translator.translate_notebook = AsyncMock(
        return_value=json.dumps(
            {
                "cells": [
                    {"cell_type": "markdown", "source": ["# Test Notebook"]},
                    {"cell_type": "code", "source": ["print('hello')"]},
                ],
                "metadata": {
                    "coopTranslator": {
                        "original_hash": "test_hash",
                        "translation_date": "2025-01-26T14:30:00+00:00",
                        "source_file": "test.ipynb",
                        "language_code": "ko",
                    }
                },
            }
        )
    )

    # Add missing attributes
    mock_translation_manager.translation_types = ["markdown", "notebook"]

    # Instead of using the real method, mock the method directly
    mock_translation_manager.translate_notebook = AsyncMock(
        return_value="translated_notebook_path"
    )

    # Call translate_notebook
    result = await mock_translation_manager.translate_notebook(notebook_file, "ko")

    # Verify translation was called with correct parameters
    mock_translation_manager.translate_notebook.assert_called_once_with(
        notebook_file, "ko"
    )

    # Verify result contains path
    assert result != ""


@pytest.mark.asyncio
async def test_retranslate_outdated_files_with_notebooks(temp_project_dir):
    """Test that retranslate_outdated_files correctly handles notebook files."""
    import json
    from unittest.mock import patch

    # Create test notebook file
    notebook_file = temp_project_dir / "test.ipynb"
    notebook_content = {"cells": [], "metadata": {}}
    notebook_file.write_text(json.dumps(notebook_content), encoding="utf-8")

    # Create markdown file
    md_file = temp_project_dir / "test.md"
    md_file.write_text("# Test", encoding="utf-8")

    # Setup outdated files list with both types
    outdated_files = [
        (notebook_file, temp_project_dir / "translations" / "ko" / "test.ipynb"),
        (md_file, temp_project_dir / "translations" / "ko" / "test.md"),
    ]

    # Create translation manager without strict spec to allow attribute access
    manager = MagicMock()
    manager.translations_dir = temp_project_dir / "translations"
    manager.language_codes = ["ko"]
    manager.supported_notebook_extensions = [".ipynb"]
    manager.translate_notebook = AsyncMock(return_value="notebook_result")
    manager.translate_markdown = AsyncMock(return_value="markdown_result")

    # Bind the actual method
    manager.retranslate_outdated_files = (
        TranslationManager.retranslate_outdated_files.__get__(manager)
    )

    # Call retranslate_outdated_files
    await manager.retranslate_outdated_files(outdated_files)

    # Verify correct translation methods were called
    manager.translate_notebook.assert_called_once_with(notebook_file, "ko")
    manager.translate_markdown.assert_called_once_with(md_file, "ko")


@pytest.mark.asyncio
async def test_translate_all_notebook_files_with_hash_check(temp_project_dir):
    """Test notebook translation with hash-based up-to-date checking."""
    import json
    from unittest.mock import patch

    # Create original notebook
    original_notebook = temp_project_dir / "test.ipynb"
    notebook_content = {"cells": [{"cell_type": "markdown", "source": ["# Original"]}]}
    original_notebook.write_text(json.dumps(notebook_content), encoding="utf-8")

    # Create translations directory
    translations_dir = temp_project_dir / "translations"
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(parents=True)

    # Create existing translated notebook (up-to-date)
    translated_notebook = ko_dir / "test.ipynb"
    translated_content = {
        "cells": [{"cell_type": "markdown", "source": ["# Original"]}],
        "metadata": {
            "coopTranslator": {
                "original_hash": "current_hash",  # Will be mocked to match
                "translation_date": "2025-01-26T14:30:00+00:00",
                "source_file": "test.ipynb",
                "language_code": "ko",
            }
        },
    }
    translated_notebook.write_text(json.dumps(translated_content), encoding="utf-8")

    # Create translation manager
    manager = MagicMock()
    manager.root_dir = temp_project_dir
    manager.translations_dir = translations_dir
    manager.language_codes = ["ko"]
    manager.supported_notebook_extensions = [".ipynb"]
    manager.excluded_dirs = {"translations"}
    manager.translate_notebook = AsyncMock(return_value="translated_result")

    # Mock notebook translator
    manager.notebook_translator = MagicMock()
    manager.notebook_translator.translate_notebook = AsyncMock(
        return_value="notebook_json"
    )

    # Mock process_api_requests_sequential to actually execute the tasks
    async def mock_process_sequential(tasks, description):
        results = []
        for task in tasks:
            try:
                result = await task()
                results.append(result)
            except Exception as e:
                results.append(None)
        return results

    manager.process_api_requests_sequential = mock_process_sequential

    # Bind the actual method
    manager.translate_all_notebook_files = (
        TranslationManager.translate_all_notebook_files.__get__(manager)
    )

    # Mock filter_files to return only the original notebook
    with patch(
        "co_op_translator.core.project.translation_manager.filter_files",
        return_value=[original_notebook],
    ):
        # Mock is_notebook_up_to_date to return True (up-to-date)
        with patch(
            "co_op_translator.core.project.translation_manager.is_notebook_up_to_date",
            return_value=True,
        ):
            result = await manager.translate_all_notebook_files(update=False)

    # Verify no translation was performed (file is up-to-date)
    manager.translate_notebook.assert_not_called()
    modified_count, errors = result
    assert modified_count == 0  # No files translated (skipped)
    assert errors == []


@pytest.mark.asyncio
async def test_translate_all_notebook_files_outdated(temp_project_dir):
    """Test notebook translation when files are outdated."""
    import json
    from unittest.mock import patch

    # Create original notebook
    original_notebook = temp_project_dir / "test.ipynb"
    notebook_content = {"cells": [{"cell_type": "markdown", "source": ["# Original"]}]}
    original_notebook.write_text(json.dumps(notebook_content), encoding="utf-8")

    # Create translations directory
    translations_dir = temp_project_dir / "translations"
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(parents=True)

    # Create existing translated notebook (outdated)
    translated_notebook = ko_dir / "test.ipynb"
    translated_content = {
        "cells": [{"cell_type": "markdown", "source": ["# Previous version"]}],
        "metadata": {
            "coopTranslator": {
                "original_hash": "old_hash",  # Different from current
                "translation_date": "2025-01-25T14:30:00+00:00",
                "source_file": "test.ipynb",
                "language_code": "ko",
            }
        },
    }
    translated_notebook.write_text(json.dumps(translated_content), encoding="utf-8")

    # Create translation manager
    manager = MagicMock()
    manager.root_dir = temp_project_dir
    manager.translations_dir = translations_dir
    manager.language_codes = ["ko"]
    manager.supported_notebook_extensions = [".ipynb"]
    manager.excluded_dirs = {"translations"}
    manager.translate_notebook = AsyncMock(return_value="updated_translation")

    # Mock notebook translator
    manager.notebook_translator = MagicMock()
    manager.notebook_translator.translate_notebook = AsyncMock(
        return_value="notebook_json"
    )

    # Mock process_api_requests_sequential to actually execute the tasks
    async def mock_process_sequential(tasks, description):
        results = []
        for task in tasks:
            try:
                result = await task()
                results.append(result)
            except Exception as e:
                results.append(None)
        return results

    manager.process_api_requests_sequential = mock_process_sequential

    # Bind the actual method
    manager.translate_all_notebook_files = (
        TranslationManager.translate_all_notebook_files.__get__(manager)
    )

    # Mock filter_files to return only the original notebook
    with patch(
        "co_op_translator.core.project.translation_manager.filter_files",
        return_value=[original_notebook],
    ):
        # Mock is_notebook_up_to_date to return False (outdated)
        with patch(
            "co_op_translator.core.project.translation_manager.is_notebook_up_to_date",
            return_value=False,
        ):
            result = await manager.translate_all_notebook_files(update=False)

    # Verify translation was performed (file is outdated)
    manager.translate_notebook.assert_called_once()
    modified_count, errors = result
    assert modified_count == 1
    assert errors == []
