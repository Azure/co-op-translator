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

    async def translate_markdown(content, lang_code, original_file, markdown_only):
        from co_op_translator.utils.common.metadata_utils import (
            create_metadata,
            format_metadata_comment,
        )

        metadata = create_metadata(original_file, lang_code)
        metadata_comment = format_metadata_comment(metadata)
        return f"{metadata_comment}# Translated content"

    translator.translate_markdown = Mock(side_effect=translate_markdown)
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


def test_metadata_handling(setup_translation_dirs, mock_markdown_translator):
    """Test metadata handling in translations"""
    root_dir = setup_translation_dirs
    translations_dir = root_dir / "translations"
    image_dir = root_dir / "translated_images"

    # Create original file with content
    original_file = root_dir / "test.md"
    original_file.write_text("# Original content")

    # Create translation file with old metadata
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(parents=True)
    trans_file = ko_dir / "test.md"
    old_metadata = """<!--
TRANSLATOR_METADATA:
{
  "original_hash": "old_hash",
  "translation_date": "2024-01-01T00:00:00+00:00",
  "source_file": "test.md",
  "language_code": "ko"
}
-->
# Old translation"""
    trans_file.write_text(old_metadata)

    manager = TranslationManager(
        root_dir=root_dir,
        translations_dir=translations_dir,
        image_dir=image_dir,
        language_codes=["ko"],
        excluded_dirs=[],
        markdown_translator=mock_markdown_translator,
        markdown_only=True,
    )

    # Check if file is detected as outdated
    assert manager._is_translation_outdated(original_file, trans_file)

    # Test translation update
    asyncio.run(manager.translate_all_markdown_files(update=True))

    # Verify new metadata is written
    content = trans_file.read_text()
    assert "TRANSLATOR_METADATA" in content
    assert "old_hash" not in content  # Old hash should be replaced
    assert "translation_date" in content


def test_translation_without_metadata(setup_translation_dirs, mock_markdown_translator):
    """Test handling of translations without metadata"""
    root_dir = setup_translation_dirs
    translations_dir = root_dir / "translations"
    image_dir = root_dir / "translated_images"

    # Create original file
    original_file = root_dir / "test.md"
    original_file.write_text("# Original content")

    # Create translation without metadata
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(parents=True)
    trans_file = ko_dir / "test.md"
    trans_file.write_text("# Old translation without metadata")

    manager = TranslationManager(
        root_dir=root_dir,
        translations_dir=translations_dir,
        image_dir=image_dir,
        language_codes=["ko"],
        excluded_dirs=[],
        markdown_translator=mock_markdown_translator,
        markdown_only=True,
    )

    # File without metadata should be considered outdated
    assert manager._is_translation_outdated(original_file, trans_file)

    # Test translation update
    asyncio.run(manager.translate_all_markdown_files(update=True))

    # Verify metadata is added
    content = trans_file.read_text()
    assert "TRANSLATOR_METADATA" in content
    assert "original_hash" in content
    assert "translation_date" in content
