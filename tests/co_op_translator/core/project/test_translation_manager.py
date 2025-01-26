"""
Tests for TranslationManager class
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch
import asyncio

from co_op_translator.core.project.translation_manager import TranslationManager
from co_op_translator.utils.common.file_utils import filter_files


@pytest.fixture
def setup_translation_dirs(tmp_path):
    """Set up test directory structure for translations"""
    root_dir = tmp_path / "test_project"
    translations_dir = root_dir / "translations"
    image_dir = root_dir / "translated_images"

    root_dir.mkdir()
    translations_dir.mkdir()
    image_dir.mkdir()

    # Create test files
    (root_dir / "test.md").write_text("# Test content\n\n![test](img/test.png)")
    (root_dir / "img").mkdir()
    (root_dir / "img/test.png").write_bytes(b"fake png content")

    return root_dir


@pytest.fixture
def mock_markdown_translator():
    """Create a mock markdown translator"""
    translator = Mock()
    translator.translate_markdown = Mock()
    translator.translate_markdown.return_value = "# Translated content"
    return translator


def test_init_translation_manager(setup_translation_dirs, mock_markdown_translator):
    """Test TranslationManager initialization"""
    root_dir = setup_translation_dirs
    translations_dir = root_dir / "translations"
    image_dir = root_dir / "translated_images"
    language_codes = ["ko", "ja"]
    excluded_dirs = ["node_modules", ".git"]

    manager = TranslationManager(
        root_dir=root_dir,
        translations_dir=translations_dir,
        image_dir=image_dir,
        language_codes=language_codes,
        excluded_dirs=excluded_dirs,
        markdown_translator=mock_markdown_translator,
        markdown_only=False,
    )

    assert manager.root_dir == root_dir
    assert manager.translations_dir == translations_dir
    assert manager.image_dir == image_dir
    assert manager.language_codes == language_codes
    assert manager.excluded_dirs == excluded_dirs


@pytest.mark.asyncio
@patch("co_op_translator.utils.common.file_utils.filter_files")
async def test_translate_all_markdown_files(
    mock_filter_files, setup_translation_dirs, mock_markdown_translator
):
    """Test markdown file translation"""
    root_dir = setup_translation_dirs
    translations_dir = root_dir / "translations"
    image_dir = root_dir / "translated_images"

    # Setup mock for filter_files
    test_md = root_dir / "test.md"
    mock_filter_files.return_value = [test_md]

    manager = TranslationManager(
        root_dir=root_dir,
        translations_dir=translations_dir,
        image_dir=image_dir,
        language_codes=["ko"],
        excluded_dirs=[],
        markdown_translator=mock_markdown_translator,
        markdown_only=True,
    )

    # Test translation
    await manager.translate_all_markdown_files()

    # Verify translation was called
    mock_markdown_translator.translate_markdown.assert_called_once()


@pytest.mark.asyncio
@patch("co_op_translator.utils.common.file_utils.filter_files")
async def test_translate_all_image_files(
    mock_filter_files, setup_translation_dirs, mock_markdown_translator
):
    """Test image file translation"""
    root_dir = setup_translation_dirs
    translations_dir = root_dir / "translations"
    image_dir = root_dir / "translated_images"

    # Setup mock for filter_files
    test_img = root_dir / "img/test.png"
    mock_filter_files.return_value = [test_img]

    manager = TranslationManager(
        root_dir=root_dir,
        translations_dir=translations_dir,
        image_dir=image_dir,
        language_codes=["ko"],
        excluded_dirs=[],
        markdown_translator=mock_markdown_translator,
        markdown_only=False,
    )

    # Test translation
    await manager.translate_all_image_files()

    # Verify file was copied
    target_path = translations_dir / "ko/img/test.png"
    assert target_path.parent.exists()  # Directory should be created
