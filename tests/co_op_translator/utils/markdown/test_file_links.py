import pytest

from co_op_translator.utils.markdown.file_links import update_untranslated_file_links


def test_update_untranslated_file_links(temp_dir, sample_markdown):
    """Test updating untranslated file links in markdown content."""
    # Create necessary directories and files
    md_file_path = temp_dir / "test.md"
    md_file_path.touch()

    translations_dir = temp_dir / "translations"
    translations_dir.mkdir(exist_ok=True)
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(exist_ok=True)

    # Create test files
    docs_dir = temp_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    (docs_dir / "example.txt").touch()  # Non-markdown, non-image file

    # Create test markdown with a text file link
    test_markdown = "# Test Document\nHere's a [link to text file](docs/example.txt)"

    result = update_untranslated_file_links(
        test_markdown, md_file_path, "ko", translations_dir, temp_dir
    )

    # Verify that non-markdown, non-image links are updated with correct relative paths
    assert "../../docs/example.txt" in result  # Updated relative path
    assert "[link to text file]" in result  # Link text should remain unchanged


def test_update_untranslated_file_links_skips_internal_anchor_links(temp_dir):
    """Same-document anchor links should remain unchanged."""
    md_file_path = temp_dir / "test.md"
    md_file_path.touch()

    translations_dir = temp_dir / "translations"
    translations_dir.mkdir(exist_ok=True)
    (translations_dir / "ko").mkdir(exist_ok=True)

    test_markdown = "# Doc\n\n- [Section](#section-one)"

    result = update_untranslated_file_links(
        test_markdown, md_file_path, "ko", translations_dir, temp_dir
    )

    assert "[Section](#section-one)" in result
    assert "../.." not in result


@pytest.mark.parametrize(
    "link",
    ["", ".", "./", "?tab=readme", ".#section-one", "./#section-one", "/#section-one"],
)
def test_update_untranslated_file_links_skips_current_document_links(temp_dir, link):
    """Current-document links should not be rewritten to the source directory."""
    md_file_path = temp_dir / "docs" / "README.md"
    md_file_path.parent.mkdir(exist_ok=True)
    md_file_path.touch()

    translations_dir = temp_dir / "translations"
    translations_dir.mkdir(exist_ok=True)
    (translations_dir / "ja").mkdir(exist_ok=True)

    test_markdown = f"- [Section]({link})"

    result = update_untranslated_file_links(
        test_markdown, md_file_path, "ja", translations_dir, temp_dir
    )

    assert result == test_markdown
    assert "../" not in result
