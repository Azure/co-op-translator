from pathlib import Path
import pytest
from co_op_translator.utils.common.file_utils import (
    read_input_file,
    write_output_file,
    handle_empty_document,
    get_unique_id,
    get_filename_and_extension,
    filter_files,
    generate_translated_filename,
    get_actual_image_path,
    reset_translation_directories,
    delete_translated_markdown_files_by_language_code,
    delete_translated_images_by_language_code,
    map_original_to_translated,
)


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for testing."""
    return tmp_path


@pytest.fixture
def test_file(temp_dir):
    """Create a test file with content."""
    file_path = temp_dir / "test.txt"
    with file_path.open("w", encoding="utf-8") as f:
        f.write("Test content\nLine 2")
    return file_path


@pytest.fixture
def empty_file(temp_dir):
    """Create an empty test file."""
    file_path = temp_dir / "empty.txt"
    file_path.touch()
    return file_path


def test_read_input_file(test_file):
    """Test reading content from a file."""
    content = read_input_file(test_file)
    assert content == "Test content\nLine 2"


def test_write_output_file(temp_dir):
    """Test writing content to a file."""
    output_file = temp_dir / "output.txt"
    results = ["Line 1", "Line 2", "Line 3"]
    write_output_file(output_file, results)

    content = output_file.read_text(encoding="utf-8")
    assert content.strip() == "\n".join(results)


def test_handle_empty_document(empty_file, temp_dir):
    """Test handling empty document by copying it."""
    output_file = temp_dir / "output.txt"
    handle_empty_document(empty_file, output_file)
    assert output_file.exists()
    assert output_file.stat().st_size == 0


def test_get_unique_id(temp_dir):
    """Test generating unique ID for a file path."""
    file_path = temp_dir / "dir" / "file.txt"
    file_path.parent.mkdir(parents=True)
    file_path.touch()

    unique_id = get_unique_id(file_path, temp_dir)
    assert isinstance(unique_id, str)
    assert len(unique_id) > 0


def test_cross_platform_path_hash_consistency(temp_dir, monkeypatch):
    """Test that path hashing is consistent across different OS path separators."""
    import os

    # Setup test directory structure
    test_dir = temp_dir / "test_dir"
    test_dir.mkdir()
    file_path = test_dir / "subdir" / "test_file.txt"
    file_path.parent.mkdir(parents=True)
    file_path.touch()

    # Case 1: Get hash with default OS path separator
    original_hash = get_unique_id(file_path, temp_dir)

    # Case 2: Simulate Windows-style paths with backslashes
    windows_style_path = str(file_path).replace("/", "\\")
    windows_hash = get_unique_id(windows_style_path, temp_dir)

    # Case 3: Simulate Unix-style paths with forward slashes
    unix_style_path = str(file_path).replace("\\", "/")
    unix_hash = get_unique_id(unix_style_path, temp_dir)

    # All hashes should be identical regardless of path separator style
    assert (
        original_hash == windows_hash
    ), "Hash should be the same regardless of Windows or default style paths"
    assert (
        original_hash == unix_hash
    ), "Hash should be the same regardless of Unix or default style paths"
    assert (
        windows_hash == unix_hash
    ), "Hash should be the same regardless of Windows or Unix style paths"


def test_get_filename_and_extension():
    """Test extracting filename and extension."""
    test_cases = [
        ("file.txt", ("file", ".txt")),
        ("path/to/file.md", ("file", ".md")),
        ("file", ("file", "")),
        (".gitignore", (".gitignore", "")),
    ]

    for input_path, expected in test_cases:
        filename, ext = get_filename_and_extension(input_path)
        assert (filename, ext) == expected


def test_filter_files(temp_dir):
    """Test filtering files in a directory."""
    # Create test directory structure
    (temp_dir / "dir1").mkdir()
    (temp_dir / "dir2").mkdir()
    (temp_dir / "file1.txt").touch()
    (temp_dir / "file2.txt").touch()
    (temp_dir / "dir1/file3.txt").touch()

    excluded_dirs = {"dir1"}
    files = filter_files(temp_dir, excluded_dirs)

    assert len(files) == 2
    assert all(f.name.endswith(".txt") for f in files)
    assert not any("dir1" in str(f) for f in files)


def test_generate_translated_filename(temp_dir):
    """Test generating translated filename."""
    file_path = temp_dir / "dir" / "file.txt"
    file_path.parent.mkdir(parents=True)
    file_path.touch()

    language_code = "ko"
    filename = generate_translated_filename(file_path, language_code, temp_dir)
    assert language_code in filename
    assert filename.endswith(".txt")


def test_get_actual_image_path(temp_dir):
    """Test resolving actual image path."""
    md_file = temp_dir / "doc/readme.md"
    md_file.parent.mkdir(parents=True)
    md_file.touch()

    image_path = "../images/test.png"
    actual_path = get_actual_image_path(image_path, md_file)

    assert isinstance(actual_path, Path)
    assert str(actual_path).endswith("test.png")


def test_reset_translation_directories(temp_dir):
    """Test resetting translation directories."""
    translations_dir = temp_dir / "translations"
    image_dir = temp_dir / "images"
    language_codes = ["ko", "en"]

    # Create existing directories with content
    translations_dir.mkdir()
    image_dir.mkdir()
    (translations_dir / "old.txt").touch()

    reset_translation_directories(translations_dir, image_dir, language_codes)

    assert translations_dir.exists()
    assert image_dir.exists()
    assert not (translations_dir / "old.txt").exists()
    assert all((translations_dir / code).exists() for code in language_codes)


def test_delete_translated_markdown_files(temp_dir):
    """Test deleting translated markdown files."""
    translations_dir = temp_dir / "translations"
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(parents=True)
    (ko_dir / "test.md").touch()

    delete_translated_markdown_files_by_language_code("ko", translations_dir)
    assert not ko_dir.exists()


def test_delete_translated_images(temp_dir):
    """Test deleting translated images."""
    image_dir = temp_dir / "images"
    image_dir.mkdir()
    (image_dir / "test.ko.png").touch()
    (image_dir / "test.en.png").touch()

    delete_translated_images_by_language_code("ko", image_dir)
    assert not (image_dir / "test.ko.png").exists()
    assert (image_dir / "test.en.png").exists()


def test_map_original_to_translated_exists_and_missing(temp_dir):
    """map_original_to_translated should return the translated path when it exists, else None."""
    root_dir = temp_dir
    translations_dir = root_dir / "translations"
    lang = "ko"

    # Create original structure
    orig_nb = root_dir / "notebook" / "01" / "foo.ipynb"
    orig_nb.parent.mkdir(parents=True)
    orig_nb.touch()

    # Case 1: missing translated counterpart -> None
    mapped_missing = map_original_to_translated(
        original_abs=orig_nb,
        language_code=lang,
        root_dir=root_dir,
        translations_dir=translations_dir,
    )
    assert mapped_missing is None

    # Case 2: exists translated counterpart -> Path
    translated_nb = translations_dir / lang / "notebook" / "01" / "foo.ipynb"
    translated_nb.parent.mkdir(parents=True)
    translated_nb.touch()

    mapped_exists = map_original_to_translated(
        original_abs=orig_nb,
        language_code=lang,
        root_dir=root_dir,
        translations_dir=translations_dir,
    )
    assert mapped_exists is not None
    assert mapped_exists.exists()
    assert mapped_exists == translated_nb.resolve()
