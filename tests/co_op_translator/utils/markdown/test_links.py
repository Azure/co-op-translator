from co_op_translator.utils.markdown.links import update_links


def test_update_links(temp_dir, sample_markdown):
    """Test updating all links in markdown content."""
    md_file_path = temp_dir / "test.md"

    result = update_links(
        md_file_path,
        sample_markdown,
        "ko",
        temp_dir,
        translation_types=["markdown", "images", "notebook"],
    )

    assert "ko" in result
    assert "translations/ko" in result or "translated_images" in result
