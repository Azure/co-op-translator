import json
from freezegun import freeze_time
from pathlib import Path
from unittest.mock import patch

from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    create_metadata,
    format_metadata_comment,
    read_notebook_metadata,
    is_notebook_up_to_date,
    add_notebook_metadata,
    _read_notebook_json,
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
        "cells": [{"cell_type": "markdown", "source": ["# 번역됨"]}],
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
        "cells": [{"cell_type": "markdown", "source": ["# 오래된 번역"]}],
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
