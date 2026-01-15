import json
from freezegun import freeze_time
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    create_metadata,
    format_metadata_comment,
    read_notebook_metadata,
    is_notebook_up_to_date,
    add_notebook_metadata,
    _read_notebook_json,
    create_image_metadata,
    save_image_metadata,
    read_image_metadata,
    is_image_up_to_date,
    remove_image_metadata,
    IMAGE_METADATA_FILENAME,
    _get_metadata_file_path,
)


def test_calculate_file_hash(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    # Calculate hash
    result = calculate_file_hash(test_file)

    # MD5 hash of "Hello, World!" is 65a8e27d8879283831b664bd8b7f0ad4
    expected_hash = "65a8e27d8879283831b664bd8b7f0ad4"
    assert result == expected_hash


@freeze_time("2025-01-26T14:30:00Z")  # Using UTC time
def test_create_metadata(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_content = "Test content"
    test_file.write_text(test_content)

    # Test with root_dir
    root_dir = tmp_path
    result = create_metadata(test_file, "ko", root_dir)

    expected = {
        "original_hash": calculate_file_hash(test_file),
        "translation_date": "2025-01-26T14:30:00+00:00",  # UTC time
        "source_file": "test.txt",
        "language_code": "ko",
    }
    assert result == expected

    # Test without root_dir
    result_no_root = create_metadata(test_file, "en")

    normalized_path = str(test_file).replace("\\", "/")

    expected_no_root = {
        "original_hash": calculate_file_hash(test_file),
        "translation_date": "2025-01-26T14:30:00+00:00",  # UTC time
        "source_file": normalized_path,
        "language_code": "en",
    }
    assert result_no_root == expected_no_root


@freeze_time("2025-01-26T14:30:00Z")
def test_path_normalization_in_metadata():
    """Test that paths are properly normalized regardless of platform."""
    # Create test paths with different path separators
    windows_style_path = "path\\to\\test\\file.txt"
    posix_style_path = "path/to/test/file.txt"
    mixed_style_path = "path\\to/test\\file.txt"

    # Test path normalization directly (manual replacement)
    assert windows_style_path.replace("\\", "/") == "path/to/test/file.txt"
    assert posix_style_path == "path/to/test/file.txt"
    assert mixed_style_path.replace("\\", "/") == "path/to/test/file.txt"

    # Mock the file hash calculation to avoid file access
    mock_hash = "mock_file_hash_for_testing"
    with patch(
        "co_op_translator.utils.common.metadata_utils.calculate_file_hash",
        return_value=mock_hash,
    ):
        # Create mock function to replace Path.relative_to that returns our test paths
        def mock_str(self):
            return windows_style_path

        def mock_relative_to(self, *args, **kwargs):
            return self

        # Test with create_metadata function using patching
        with patch("pathlib.Path.__str__", mock_str):
            with patch("pathlib.Path.relative_to", mock_relative_to):
                # No root_dir case
                metadata = create_metadata(Path("dummy"), "en")
                assert (
                    metadata["source_file"].replace("\\", "/")
                    == "path/to/test/file.txt"
                )
                # This is the real check - our implementation should ensure no backslashes exist
                assert "\\" not in metadata["source_file"]
                assert "/" in metadata["source_file"]
                # Verify the hash was mocked properly
                assert metadata["original_hash"] == mock_hash

        # Test with POSIX style path
        def mock_str_posix(self):
            return posix_style_path

        with patch("pathlib.Path.__str__", mock_str_posix):
            with patch("pathlib.Path.relative_to", mock_relative_to):
                metadata = create_metadata(Path("dummy"), "en")
                assert metadata["source_file"] == "path/to/test/file.txt"
                assert metadata["original_hash"] == mock_hash

        # Test with mixed style path
        def mock_str_mixed(self):
            return mixed_style_path

        with patch("pathlib.Path.__str__", mock_str_mixed):
            with patch("pathlib.Path.relative_to", mock_relative_to):
                metadata = create_metadata(Path("dummy"), "en")
                assert (
                    metadata["source_file"].replace("\\", "/")
                    == "path/to/test/file.txt"
                )
                assert "\\" not in metadata["source_file"]
                assert metadata["original_hash"] == mock_hash


def test_format_metadata_comment():
    test_metadata = {
        "original_hash": "test_hash",
        "translation_date": "2025-01-26T14:30:00+09:00",
        "source_file": "test.txt",
        "language_code": "ko",
    }

    result = format_metadata_comment(test_metadata)

    # Verify the format
    assert result.startswith("<!--\nCO_OP_TRANSLATOR_METADATA:\n")
    assert result.endswith("\n-->\n")

    # Extract and parse the JSON content
    json_content = result.replace("<!--\nCO_OP_TRANSLATOR_METADATA:\n", "").replace(
        "\n-->\n", ""
    )
    parsed_metadata = json.loads(json_content)

    # Verify the metadata content
    assert parsed_metadata == test_metadata

    # Verify the indentation
    assert "  " in result  # Should have 2-space indentation


# ============================================================================
# Notebook-specific tests
# ============================================================================


def test_read_notebook_json(tmp_path):
    """Test reading notebook JSON file."""
    # Create a test notebook file
    notebook_file = tmp_path / "test.ipynb"
    test_notebook = {
        "cells": [{"cell_type": "markdown", "source": ["# Test Notebook"]}],
        "metadata": {
            "kernelspec": {"name": "python3"},
            "coopTranslator": {"test": "value"},
        },
    }

    notebook_file.write_text(json.dumps(test_notebook), encoding="utf-8")

    # Test successful read
    result = _read_notebook_json(notebook_file)
    assert result == test_notebook

    # Test with non-existent file
    non_existent = tmp_path / "non_existent.ipynb"
    result = _read_notebook_json(non_existent)
    assert result == {}

    # Test with invalid JSON
    invalid_json_file = tmp_path / "invalid.ipynb"
    invalid_json_file.write_text("invalid json content")
    result = _read_notebook_json(invalid_json_file)
    assert result == {}


def test_read_notebook_metadata(tmp_path):
    """Test reading notebook metadata."""
    # Create a test notebook with metadata
    notebook_file = tmp_path / "test.ipynb"
    test_notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {"name": "python3"},
            "coopTranslator": {
                "original_hash": "test_hash",
                "translation_date": "2025-01-26T14:30:00+00:00",
                "source_file": "test.ipynb",
                "language_code": "ko",
            },
        },
    }

    notebook_file.write_text(json.dumps(test_notebook), encoding="utf-8")

    # Test reading all metadata
    result = read_notebook_metadata(notebook_file)
    assert result == test_notebook["metadata"]

    # Test reading specific metadata key
    result = read_notebook_metadata(notebook_file, "coopTranslator")
    assert result == test_notebook["metadata"]["coopTranslator"]

    # Test reading non-existent metadata key
    result = read_notebook_metadata(notebook_file, "nonExistent")
    assert result == {}

    # Test with notebook without metadata
    notebook_no_metadata = {"cells": []}
    notebook_file_no_meta = tmp_path / "no_meta.ipynb"
    notebook_file_no_meta.write_text(json.dumps(notebook_no_metadata), encoding="utf-8")

    result = read_notebook_metadata(notebook_file_no_meta)
    assert result == {}

    result = read_notebook_metadata(notebook_file_no_meta, "coopTranslator")
    assert result == {}


@freeze_time("2025-01-26T14:30:00Z")
def test_add_notebook_metadata(tmp_path):
    """Test adding metadata to notebook."""
    # Create original notebook file for hash calculation
    original_file = tmp_path / "original.ipynb"
    original_content = {"cells": [{"cell_type": "markdown", "source": ["# Original"]}]}
    original_file.write_text(json.dumps(original_content), encoding="utf-8")

    # Test notebook without metadata
    notebook = {"cells": []}
    result = add_notebook_metadata(notebook, original_file, "ko", tmp_path)

    assert "metadata" in result
    assert "coopTranslator" in result["metadata"]

    coop_meta = result["metadata"]["coopTranslator"]
    assert coop_meta["original_hash"] == calculate_file_hash(original_file)
    assert coop_meta["translation_date"] == "2025-01-26T14:30:00+00:00"
    assert coop_meta["source_file"] == "original.ipynb"
    assert coop_meta["language_code"] == "ko"

    # Test notebook with existing metadata
    notebook_with_meta = {"cells": [], "metadata": {"kernelspec": {"name": "python3"}}}
    result = add_notebook_metadata(notebook_with_meta, original_file, "en")

    assert "kernelspec" in result["metadata"]  # Should preserve existing metadata
    assert "coopTranslator" in result["metadata"]  # Should add new metadata


def test_is_notebook_up_to_date(tmp_path):
    """Test checking if notebook translation is up to date."""
    # Create original notebook
    original_file = tmp_path / "original.ipynb"
    original_content = {"cells": [{"cell_type": "markdown", "source": ["# Original"]}]}
    original_file.write_text(json.dumps(original_content), encoding="utf-8")

    original_hash = calculate_file_hash(original_file)

    # Create translated notebook with correct hash
    translated_file = tmp_path / "translated.ipynb"
    translated_content = {
        "cells": [{"cell_type": "markdown", "source": ["# Translated"]}],
        "metadata": {
            "coopTranslator": {
                "original_hash": original_hash,
                "translation_date": "2025-01-26T14:30:00+00:00",
                "source_file": "original.ipynb",
                "language_code": "ko",
            }
        },
    }
    translated_file.write_text(json.dumps(translated_content), encoding="utf-8")

    # Should be up to date
    assert is_notebook_up_to_date(original_file, translated_file) == True

    # Create translated notebook with incorrect hash
    outdated_translated_file = tmp_path / "outdated.ipynb"
    outdated_content = {
        "cells": [{"cell_type": "markdown", "source": ["# Outdated translation"]}],
        "metadata": {
            "coopTranslator": {
                "original_hash": "wrong_hash",
                "translation_date": "2025-01-26T14:30:00+00:00",
                "source_file": "original.ipynb",
                "language_code": "ko",
            }
        },
    }
    outdated_translated_file.write_text(json.dumps(outdated_content), encoding="utf-8")

    # Should be outdated
    assert is_notebook_up_to_date(original_file, outdated_translated_file) == False

    # Test with translated notebook without metadata
    no_metadata_file = tmp_path / "no_metadata.ipynb"
    no_metadata_content = {"cells": []}
    no_metadata_file.write_text(json.dumps(no_metadata_content), encoding="utf-8")

    # Should be outdated (no metadata means outdated)
    assert is_notebook_up_to_date(original_file, no_metadata_file) == False

    # Test with non-existent files
    non_existent = tmp_path / "non_existent.ipynb"
    assert is_notebook_up_to_date(original_file, non_existent) == False
    assert is_notebook_up_to_date(non_existent, translated_file) == False


# ============================================================================
# Image-specific metadata tests (per-language metadata file approach)
# ============================================================================


@freeze_time("2025-01-26T14:30:00Z")
def test_create_image_metadata(tmp_path):
    """Test creating image metadata."""
    # Create a test image file
    test_image = tmp_path / "test.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(test_image)

    # Test with root_dir
    result = create_image_metadata(test_image, "ko", tmp_path)

    assert result["original_hash"] == calculate_file_hash(test_image)
    assert result["translation_date"] == "2025-01-26T14:30:00+00:00"
    assert result["source_file"] == "test.png"
    assert result["language_code"] == "ko"


@freeze_time("2025-01-26T14:30:00Z")
def test_save_image_metadata(tmp_path):
    """Test saving metadata to language-specific metadata file."""
    # Setup: translated_images/<lang>/<filename> structure
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    # Create original image
    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="blue")
    img.save(original_path)

    # Save translated image
    translated_path = lang_dir / "translated.png"
    img.save(translated_path)

    # Save metadata
    save_image_metadata(translated_path, original_path, "ko", tmp_path)

    # Check metadata file exists in language folder
    metadata_file = _get_metadata_file_path(lang_dir)
    assert metadata_file.exists()

    # Read and verify metadata
    with open(metadata_file, "r", encoding="utf-8") as f:
        all_metadata = json.load(f)

    assert "translated.png" in all_metadata
    metadata = all_metadata["translated.png"]
    assert metadata["original_hash"] == calculate_file_hash(original_path)
    assert metadata["translation_date"] == "2025-01-26T14:30:00+00:00"
    assert metadata["source_file"] == "original.png"
    assert metadata["language_code"] == "ko"


@freeze_time("2025-01-26T14:30:00Z")
def test_save_multiple_images_different_languages(tmp_path):
    """Test saving metadata for images in different languages creates separate files."""
    # Setup directory structure
    image_dir = tmp_path / "translated_images"
    ko_dir = image_dir / "ko"
    ja_dir = image_dir / "ja"
    ko_dir.mkdir(parents=True)
    ja_dir.mkdir(parents=True)

    # Create original images
    original1 = tmp_path / "image1.png"
    original2 = tmp_path / "image2.jpg"
    img1 = Image.new("RGB", (100, 100), color="red")
    img2 = Image.new("RGB", (100, 100), color="blue")
    img1.save(original1)
    img2.save(original2)

    # Save translated images
    translated1 = ko_dir / "image1.hash1.png"
    translated2 = ja_dir / "image2.hash2.jpg"
    img1.save(translated1)
    img2.save(translated2)

    # Save metadata
    save_image_metadata(translated1, original1, "ko", tmp_path)
    save_image_metadata(translated2, original2, "ja", tmp_path)

    # Verify separate metadata files for each language
    ko_metadata_file = _get_metadata_file_path(ko_dir)
    ja_metadata_file = _get_metadata_file_path(ja_dir)

    assert ko_metadata_file.exists()
    assert ja_metadata_file.exists()

    with open(ko_metadata_file, "r", encoding="utf-8") as f:
        ko_metadata = json.load(f)
    with open(ja_metadata_file, "r", encoding="utf-8") as f:
        ja_metadata = json.load(f)

    assert "image1.hash1.png" in ko_metadata
    assert "image2.hash2.jpg" in ja_metadata
    assert len(ko_metadata) == 1
    assert len(ja_metadata) == 1


@freeze_time("2025-01-26T14:30:00Z")
def test_image_metadata_keys_are_sorted_by_filename(tmp_path):
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    first_translated = lang_dir / "z_last.png"
    second_translated = lang_dir / "a_first.png"
    img.save(first_translated)
    img.save(second_translated)

    save_image_metadata(first_translated, original_path, "ko", tmp_path)
    save_image_metadata(second_translated, original_path, "ko", tmp_path)

    metadata_file = _get_metadata_file_path(lang_dir)
    contents = metadata_file.read_text(encoding="utf-8")

    first_index = contents.find("a_first.png")
    second_index = contents.find("z_last.png")

    assert first_index != -1
    assert second_index != -1
    assert first_index < second_index


def test_read_image_metadata(tmp_path):
    """Test reading metadata from language-specific file."""
    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="green")
    img.save(original_path)

    translated_path = lang_dir / "translated.png"
    img.save(translated_path)
    save_image_metadata(translated_path, original_path, "ko", tmp_path)

    # Read metadata
    metadata = read_image_metadata(translated_path)

    assert metadata["original_hash"] == calculate_file_hash(original_path)
    assert metadata["source_file"] == "original.png"
    assert metadata["language_code"] == "ko"


def test_read_image_metadata_not_found(tmp_path):
    """Test reading metadata for image not in metadata file."""
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    test_image = lang_dir / "no_metadata.png"
    img = Image.new("RGB", (100, 100), color="yellow")
    img.save(test_image)

    # Read metadata - should return empty dict
    metadata = read_image_metadata(test_image)
    assert metadata == {}


def test_remove_image_metadata(tmp_path):
    """Test removing metadata for a specific image."""
    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    translated_path = lang_dir / "translated.png"
    img.save(translated_path)
    save_image_metadata(translated_path, original_path, "ko", tmp_path)

    # Verify metadata exists
    metadata = read_image_metadata(translated_path)
    assert metadata != {}

    # Remove metadata
    remove_image_metadata(translated_path)

    # Verify metadata is gone
    metadata = read_image_metadata(translated_path)
    assert metadata == {}


def test_is_image_up_to_date(tmp_path):
    """Test checking if image translation is up to date."""
    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    translated_path = lang_dir / "translated.png"
    img.save(translated_path)
    save_image_metadata(translated_path, original_path, "ko", tmp_path)

    # Should be up to date
    assert is_image_up_to_date(original_path, translated_path) == True


def test_is_image_up_to_date_outdated(tmp_path):
    """Test detecting outdated image translation."""
    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    translated_path = lang_dir / "translated.png"
    img.save(translated_path)
    save_image_metadata(translated_path, original_path, "ko", tmp_path)

    # Modify the original image
    img_modified = Image.new("RGB", (100, 100), color="blue")
    img_modified.save(original_path)

    # Should be outdated now
    assert is_image_up_to_date(original_path, translated_path) == False


def test_is_image_up_to_date_no_metadata(tmp_path):
    """Test that image without metadata is considered outdated."""
    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    translated_path = lang_dir / "translated.png"
    img.save(translated_path)  # No metadata saved

    # Should be outdated (no metadata)
    assert is_image_up_to_date(original_path, translated_path) == False


def test_is_image_up_to_date_nonexistent_translated(tmp_path):
    """Test that non-existent translated image is considered outdated."""
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    translated_path = lang_dir / "non_existent.png"

    # Should be outdated (file doesn't exist)
    assert is_image_up_to_date(original_path, translated_path) == False


def test_cleanup_orphan_image_metadata(tmp_path):
    """Test cleaning up metadata for deleted images."""
    from co_op_translator.utils.common.metadata_utils import (
        cleanup_orphan_image_metadata,
    )

    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    # Create two translated images
    translated1 = lang_dir / "image1.abc123.png"
    translated2 = lang_dir / "image2.def456.png"
    img.save(translated1)
    img.save(translated2)

    # Save metadata for both
    save_image_metadata(translated1, original_path, "ko", tmp_path)
    save_image_metadata(translated2, original_path, "ko", tmp_path)

    # Verify both have metadata
    assert read_image_metadata(translated1) != {}
    assert read_image_metadata(translated2) != {}

    # Delete one image file (but not its metadata)
    translated2.unlink()

    # Run cleanup
    removed_count = cleanup_orphan_image_metadata(lang_dir)

    # Should have removed 1 orphan entry
    assert removed_count == 1

    # Metadata for existing image should remain
    assert read_image_metadata(translated1) != {}

    # Metadata for deleted image should be gone
    assert read_image_metadata(translated2) == {}


def test_cleanup_orphan_image_metadata_no_orphans(tmp_path):
    """Test cleanup when there are no orphan entries."""
    from co_op_translator.utils.common.metadata_utils import (
        cleanup_orphan_image_metadata,
    )

    # Setup
    image_dir = tmp_path / "translated_images"
    lang_dir = image_dir / "ko"
    lang_dir.mkdir(parents=True)

    original_path = tmp_path / "original.png"
    img = Image.new("RGB", (100, 100), color="red")
    img.save(original_path)

    # Create translated image with metadata
    translated = lang_dir / "image.abc123.png"
    img.save(translated)
    save_image_metadata(translated, original_path, "ko", tmp_path)

    # Run cleanup (no orphans)
    removed_count = cleanup_orphan_image_metadata(lang_dir)

    # Should have removed nothing
    assert removed_count == 0

    # Metadata should still exist
    assert read_image_metadata(translated) != {}
