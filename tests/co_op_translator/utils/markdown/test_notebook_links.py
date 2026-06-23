from co_op_translator.utils.markdown.notebook_links import update_notebook_links


def test_update_notebook_links_prefers_translated(tmp_path):
    """When translated notebook exists, link should point to translated notebook relative to translated md dir."""
    root_dir = tmp_path
    translations_dir = root_dir / "translations"
    (translations_dir / "ko").mkdir(parents=True)

    # Original MD and notebook
    md_file_path = root_dir / "docs" / "guide.md"
    nb_orig = root_dir / "notebook" / "01" / "foo.ipynb"
    nb_orig.parent.mkdir(parents=True, exist_ok=True)
    md_file_path.parent.mkdir(parents=True, exist_ok=True)
    nb_orig.touch()

    # Translated counterpart exists
    nb_trans = translations_dir / "ko" / "notebook" / "01" / "foo.ipynb"
    nb_trans.parent.mkdir(parents=True, exist_ok=True)
    nb_trans.touch()

    # Content has a relative link to the notebook from original md location
    content = "See [nb](../notebook/01/foo.ipynb)"

    # Compute translated md directory
    translated_md_dir = (
        translations_dir / "ko" / md_file_path.relative_to(root_dir).parent
    )
    translated_md_dir.mkdir(parents=True, exist_ok=True)

    updated = update_notebook_links(
        markdown_string=content,
        md_file_path=md_file_path,
        language_code="ko",
        translations_dir=translations_dir,
        root_dir=root_dir,
        use_translated_notebook=True,
    )

    import os

    expected_rel = os.path.relpath(nb_trans, translated_md_dir).replace(
        os.path.sep, "/"
    )
    assert f"[nb]({expected_rel})" in updated


def test_update_notebook_links_fallback_to_original(tmp_path):
    """When translated notebook is missing, link should point to original notebook relative to translated md dir."""
    root_dir = tmp_path
    translations_dir = root_dir / "translations"
    (translations_dir / "ko").mkdir(parents=True)

    # Original MD and notebook
    md_file_path = root_dir / "docs" / "guide.md"
    nb_orig = root_dir / "notebook" / "02" / "bar.ipynb"
    nb_orig.parent.mkdir(parents=True, exist_ok=True)
    md_file_path.parent.mkdir(parents=True, exist_ok=True)
    nb_orig.touch()

    # Translated counterpart missing
    # content points to the notebook
    content = "See [nb](../notebook/02/bar.ipynb)"

    # Compute translated md directory
    translated_md_dir = (
        translations_dir / "ko" / md_file_path.relative_to(root_dir).parent
    )
    translated_md_dir.mkdir(parents=True, exist_ok=True)

    updated = update_notebook_links(
        markdown_string=content,
        md_file_path=md_file_path,
        language_code="ko",
        translations_dir=translations_dir,
        root_dir=root_dir,
        use_translated_notebook=True,
    )

    import os

    expected_rel = os.path.relpath(nb_orig, translated_md_dir).replace(os.path.sep, "/")
    assert f"[nb]({expected_rel})" in updated
