import json
from freezegun import freeze_time
from pathlib import Path
from unittest.mock import patch

from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    create_metadata,
    format_metadata_comment,
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
