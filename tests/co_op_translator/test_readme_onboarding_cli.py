from unittest.mock import AsyncMock, MagicMock

import pytest
from click.testing import CliRunner

from co_op_translator.cli import translate as translate_cli
from co_op_translator.cli.translate import translate_command
from co_op_translator.api.review import run_review
from co_op_translator.core.project.readme_translator import ReadmeTranslator


@pytest.mark.parametrize("preview", [True, False])
def test_readme_cli_preserves_source_and_scopes_output(monkeypatch, tmp_path, preview):
    source = "# Hello\n\n[Guide](docs/guide.md)\n"
    (tmp_path / "README.md").write_text(source, encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/guide.md").write_text("# Guide\n", encoding="utf-8")
    provider = MagicMock()
    provider.translate_markdown = AsyncMock(
        return_value="# 안녕하세요\n\n[안내](docs/guide.md)\n"
    )

    def make_translator(*args, **kwargs):
        kwargs["markdown_translator"] = provider
        return ReadmeTranslator(*args, **kwargs)

    monkeypatch.setattr(translate_cli, "ReadmeTranslator", make_translator)
    for owner, name in (
        (translate_cli.Config, "check_configuration"),
        (translate_cli.LLMConfig, "validate_connectivity"),
        (translate_cli.VisionConfig, "validate_connectivity"),
    ):
        mock = MagicMock(return_value=True)
        if preview:
            mock.side_effect = AssertionError("Preview must not check credentials")
        monkeypatch.setattr(owner, name, mock)

    shared_updates = []
    for name in ("update_readme_languages_table", "update_readme_other_courses"):
        mock = MagicMock()
        shared_updates.append(mock)
        monkeypatch.setattr(translate_cli, name, mock)

    args = ["-r", str(tmp_path), "-l", "ko", "--readme-only", "--no-disclaimer", "-y"]
    if preview:
        args.append("--dry-run")
    result = CliRunner().invoke(translate_command, args)

    assert result.exit_code == 0, result.output
    assert (tmp_path / "README.md").read_text(encoding="utf-8") == source
    for mock in shared_updates:
        mock.assert_not_called()
    if preview:
        provider.translate_markdown.assert_not_awaited()
        assert not (tmp_path / "translations").exists()
    else:
        provider.translate_markdown.assert_awaited_once()
        assert not (tmp_path / "translations/ko/docs").exists()
        summary = run_review(
            root_dir=str(tmp_path), language_codes="ko", readme_only=True
        )
        assert summary.error_count == summary.warning_count == 0


@pytest.mark.parametrize("preview", [True, False])
def test_readme_cli_rejects_missing_source_before_provider_checks(
    monkeypatch, tmp_path, preview
):
    config_check = MagicMock(side_effect=AssertionError("Must validate source first"))
    monkeypatch.setattr(translate_cli.Config, "check_configuration", config_check)
    args = ["-r", str(tmp_path), "-l", "ko", "--readme-only", "-y"]
    if preview:
        args.append("--dry-run")

    result = CliRunner().invoke(translate_command, args)

    assert result.exit_code == 1
    assert "README.md not found" in result.output
    config_check.assert_not_called()
    assert not (tmp_path / "translations").exists()
