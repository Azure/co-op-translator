"""
Tests for metadata_utils.py
"""

import json
from freezegun import freeze_time

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
    expected_no_root = {
        "original_hash": calculate_file_hash(test_file),
        "translation_date": "2025-01-26T14:30:00+00:00",  # UTC time
        "source_file": str(test_file),
        "language_code": "en",
    }
    assert result_no_root == expected_no_root


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
