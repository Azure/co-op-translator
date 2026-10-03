import importlib
import json
from unittest.mock import AsyncMock, Mock

import pytest
from click.testing import CliRunner

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.llm import JupyterNotebookTranslator
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    read_text_metadata_for_source,
    save_text_metadata_for_source,
)


@pytest.fixture
def cli(monkeypatch):
    module = importlib.import_module("co_op_translator.cli.translate")
    monkeypatch.setenv("CO_OP_TRANSLATOR_OUTPUT_STYLE", "plain")
    monkeypatch.setattr(module.Config, "check_configuration", Mock())
    monkeypatch.setattr(module.LLMConfig, "validate_connectivity", Mock())
    return module


@pytest.fixture
def provider(monkeypatch):
    async def translate(document, *args, **kwargs):
        return document.replace("Hello", "Translated")

    fake = Mock()
    fake.translate_markdown = AsyncMock(side_effect=translate)
    fake.translate_notebook = AsyncMock(side_effect=translate)
    monkeypatch.setattr(MarkdownTranslator, "create", Mock(return_value=fake))
    monkeypatch.setattr(JupyterNotebookTranslator, "create", Mock(return_value=fake))
    return fake


@pytest.mark.parametrize("mode", ["-md", "-nb", "--readme-only"])
@pytest.mark.parametrize("layout", ["default", "relative", "absolute"])
def test_translation_uses_output_directory_and_tracks_freshness(
    cli, provider, tmp_path, mode, layout
):
    root = tmp_path / "docs"
    root.mkdir()
    (root / "README.md").write_text("# Hello\n", encoding="utf-8")
    (root / "lesson.ipynb").write_text(
        json.dumps(
            {
                "cells": [
                    {"cell_type": "markdown", "metadata": {}, "source": ["# Hello\n"]}
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
        ),
        encoding="utf-8",
    )
    output = {
        "default": root / "translations",
        "relative": root / "i18n",
        "absolute": tmp_path / "localized",
    }[layout]
    args = ["-r", str(root), "-l", "ko", mode, "--no-disclaimer", "-y"]
    if layout != "default":
        args += ["--translations-dir", "i18n" if layout == "relative" else str(output)]
    runner = CliRunner()
    result = runner.invoke(cli.translate_command, args)
    assert result.exit_code == 0, result.output

    filename = "lesson.ipynb" if mode == "-nb" else "README.md"
    translated = output / "ko" / filename
    assert "Translated" in translated.read_text(encoding="utf-8")
    metadata = read_text_metadata_for_source(output / "ko", filename)
    assert metadata["original_hash"] == calculate_file_hash(root / filename)
    if layout != "default":
        assert not (root / "translations").exists()
    method = (
        provider.translate_notebook if mode == "-nb" else provider.translate_markdown
    )
    method.assert_awaited_once()

    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    result = runner.invoke(cli.translate_command, args + ["--dry-run"])
    assert result.exit_code == 0, result.output
    assert "Estimated tokens before translation: 0" in result.output
    assert {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()} == before

    result = runner.invoke(cli.translate_command, args)
    assert result.exit_code == 0, result.output
    method.assert_awaited_once()
    assert not (output / "ko" / output.name).exists()

    source = root / filename
    source.write_text(
        source.read_text(encoding="utf-8").replace("Hello", "Hello again")
    )
    result = runner.invoke(cli.translate_command, args)
    assert result.exit_code == 0, result.output
    assert "Translated again" in translated.read_text(encoding="utf-8")
    assert method.await_count == 2


@pytest.mark.parametrize("mode", ["-md", "--readme-only"])
def test_custom_output_dry_run_does_not_create_directories(cli, tmp_path, mode):
    (tmp_path / "README.md").write_text("# Hello\n", encoding="utf-8")
    result = CliRunner().invoke(
        cli.translate_command,
        [
            "-r",
            str(tmp_path),
            "-l",
            "ko",
            mode,
            "--translations-dir",
            "i18n",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert sorted(p.name for p in tmp_path.iterdir()) == ["README.md"]
    cli.Config.check_configuration.assert_not_called()
    cli.LLMConfig.validate_connectivity.assert_not_called()


@pytest.mark.parametrize("preview", [True, False])
def test_alias_migration_and_metadata_use_custom_output(
    cli, provider, tmp_path, preview
):
    source = tmp_path / "README.md"
    source.write_text("# Hello\n", encoding="utf-8")
    custom_alias = tmp_path / "i18n" / "cn"
    custom_alias.mkdir(parents=True)
    (custom_alias / "README.md").write_text("# Translated\n", encoding="utf-8")
    save_text_metadata_for_source(custom_alias, source, "cn", root_dir=tmp_path)
    default_alias = tmp_path / "translations" / "cn"
    default_alias.mkdir(parents=True)
    sentinel = default_alias / "README.md"
    sentinel.write_text("Unrelated translation", encoding="utf-8")
    args = [
        "-r",
        str(tmp_path),
        "-l",
        "cn",
        "--readme-only",
        "--no-disclaimer",
        "--translations-dir",
        "i18n",
        "--migrate-language-folders",
        "-y",
    ]
    if preview:
        args.append("--dry-run")
    result = CliRunner().invoke(cli.translate_command, args)
    assert result.exit_code == 0, result.output
    assert "cn -> zh-CN" in result.output
    assert sentinel.read_text(encoding="utf-8") == "Unrelated translation"
    if preview:
        assert custom_alias.is_dir()
        assert not (tmp_path / "i18n" / "zh-CN").exists()
    else:
        assert not custom_alias.exists()
        metadata = read_text_metadata_for_source(
            tmp_path / "i18n" / "zh-CN", "README.md"
        )
        assert metadata["language_code"] == "zh-CN"
    provider.translate_markdown.assert_not_awaited()


def test_output_file_is_rejected_before_provider_checks(cli, tmp_path):
    (tmp_path / "i18n").write_text("Existing file", encoding="utf-8")
    result = CliRunner().invoke(
        cli.translate_command,
        ["-r", str(tmp_path), "-l", "ko", "-md", "--translations-dir", "i18n"],
    )
    assert result.exit_code != 0
    assert "--translations-dir" in result.output
    assert "Not a directory" in result.output
    cli.Config.check_configuration.assert_not_called()
