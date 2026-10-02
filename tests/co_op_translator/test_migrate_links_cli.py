from click.testing import CliRunner

from co_op_translator.cli.migrate_links import migrate_links_command


def test_migrate_links_dry_run_works_with_incomplete_provider_config(
    monkeypatch, tmp_path
):
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "placeholder")
    for name in (
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_MODEL_NAME",
        "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME",
        "AZURE_OPENAI_API_VERSION",
        "OPENAI_API_KEY",
        "OPENAI_CHAT_MODEL_ID",
    ):
        monkeypatch.delenv(name, raising=False)

    source_dir = tmp_path / "docs"
    translated_dir = tmp_path / "translations" / "ko" / "docs"
    source_dir.mkdir()
    translated_dir.mkdir(parents=True)
    (source_dir / "guide.md").write_text(
        "[Notebook](notebook.ipynb)\n", encoding="utf-8"
    )
    (source_dir / "notebook.ipynb").write_text("{}\n", encoding="utf-8")
    translated_markdown = translated_dir / "guide.md"
    original_translation = "[Notebook](/docs/notebook.ipynb)\n"
    translated_markdown.write_text(original_translation, encoding="utf-8")
    (translated_dir / "notebook.ipynb").write_text("{}\n", encoding="utf-8")

    result = CliRunner().invoke(
        migrate_links_command,
        ["-r", str(tmp_path), "-l", "ko", "--dry-run"],
    )

    assert result.exit_code == 0, result.output
    assert "[DRY-RUN] Would update:" in result.output
    assert translated_markdown.read_text(encoding="utf-8") == original_translation
