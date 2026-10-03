from click.testing import CliRunner
import pytest

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


def test_migrate_links_ignores_notebook_links_inside_code(tmp_path):
    source_dir = tmp_path / "docs"
    translated_dir = tmp_path / "translations" / "ko" / "docs"
    source_dir.mkdir()
    translated_dir.mkdir(parents=True)
    (source_dir / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (source_dir / "notebook.ipynb").write_text("{}\n", encoding="utf-8")
    (translated_dir / "notebook.ipynb").write_text("{}\n", encoding="utf-8")
    translated_markdown = translated_dir / "guide.md"
    content = (
        "`[Inline](notebook.ipynb)`\n\n"
        "```shell\necho '[Fenced](notebook.ipynb)'\n```\n"
        "[Real](/docs/notebook.ipynb)\n"
    )
    translated_markdown.write_text(content, encoding="utf-8")

    result = CliRunner().invoke(
        migrate_links_command,
        ["-r", str(tmp_path), "-l", "ko"],
    )

    assert result.exit_code == 0, result.output
    updated = translated_markdown.read_text(encoding="utf-8")
    assert "`[Inline](notebook.ipynb)`" in updated
    assert "[Fenced](notebook.ipynb)" in updated
    assert "[Real](notebook.ipynb)" in updated


def test_migrate_links_non_interactive_never_prompts(monkeypatch, tmp_path):
    (tmp_path / "translations").mkdir()
    monkeypatch.setattr(
        "co_op_translator.cli.migrate_links.click.prompt",
        lambda *args, **kwargs: pytest.fail("non-interactive mode prompted"),
    )
    monkeypatch.setattr(
        "co_op_translator.cli.migrate_links.Config.get_language_codes",
        lambda: ["ko"],
    )

    result = CliRunner().invoke(
        migrate_links_command,
        ["-r", str(tmp_path), "-l", "all", "--non-interactive"],
    )

    assert result.exit_code == 0, result.output


def test_migrate_links_uses_custom_paths_and_filters(tmp_path):
    source = tmp_path / "docs"
    output = source / "i18n"
    source.mkdir()
    (source / "notebook.ipynb").write_text("{}\n", encoding="utf-8")
    for name in ("keep.md", "skip.md"):
        (source / name).write_text("# Source\n", encoding="utf-8")
        translated = output / "ko" / name
        translated.parent.mkdir(parents=True, exist_ok=True)
        translated.write_text("[Notebook](/notebook.ipynb)\n", encoding="utf-8")
    (output / "ko" / "notebook.ipynb").write_text("{}\n", encoding="utf-8")

    result = CliRunner().invoke(
        migrate_links_command,
        [
            "--source",
            str(source),
            "--output",
            str(output),
            "--include",
            "*.md",
            "--exclude",
            "skip.md",
            "-l",
            "ko",
        ],
    )

    assert result.exit_code == 0, result.output
    assert (output / "ko" / "keep.md").read_text(encoding="utf-8") == (
        "[Notebook](notebook.ipynb)\n"
    )
    assert (output / "ko" / "skip.md").read_text(encoding="utf-8") == (
        "[Notebook](/notebook.ipynb)\n"
    )
