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


def test_update_links_can_keep_markdown_links_pointing_to_source(tmp_path):
    (tmp_path / "docs").mkdir()
    source_readme = tmp_path / "README.md"
    source_readme.write_text("# Home", encoding="utf-8")
    (tmp_path / "docs" / "guide.md").write_text("# Guide", encoding="utf-8")

    result = update_links(
        source_readme,
        "[Guide](docs/guide.md#install)",
        "ko",
        tmp_path,
        translation_types=["markdown"],
        target_path=tmp_path / "translations" / "ko" / "README.md",
        use_translated_markdown_links=False,
    )

    assert result == "[Guide](../../docs/guide.md#install)"
