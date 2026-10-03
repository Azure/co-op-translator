import asyncio
import json

import pytest
from click.testing import CliRunner

from co_op_translator.api import translation as api
from co_op_translator.cli import translate as cli
from co_op_translator.core.llm import JupyterNotebookTranslator
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.core.project.readme_translator import ReadmeTranslator


class Provider:
    def __init__(self):
        self.active = self.peak = 0

    async def translate_markdown(self, document, language_code, **kwargs):
        self.active += 1
        self.peak = max(self.peak, self.active)
        try:
            await asyncio.sleep(0)
            return document
        finally:
            self.active -= 1

    translate_notebook = translate_markdown


@pytest.mark.parametrize("entrypoint", ["cli", "api"])
@pytest.mark.parametrize("mode", ["markdown", "notebook", "readme"])
@pytest.mark.parametrize("dry_run", [False, True])
def test_entrypoints_run_real_workflows_with_concurrency(
    monkeypatch, tmp_path, entrypoint, mode, dry_run
):
    provider = Provider()
    (tmp_path / "README.md").write_text("# Hello", encoding="utf-8")
    if mode == "notebook":
        (tmp_path / "guide.ipynb").write_text(
            json.dumps(
                {
                    "cells": [
                        {"cell_type": "markdown", "metadata": {}, "source": ["# Hello"]}
                    ],
                    "metadata": {},
                    "nbformat": 4,
                    "nbformat_minor": 5,
                }
            ),
            encoding="utf-8",
        )
    source_snapshot = {p.name: p.read_bytes() for p in tmp_path.iterdir()}

    def credentials(*args, **kwargs):
        if dry_run:
            pytest.fail("Dry run must not check credentials or initialize providers")
        return True

    def create_provider(*args, **kwargs):
        credentials()
        return provider

    monkeypatch.setattr(MarkdownTranslator, "create", create_provider)
    monkeypatch.setattr(JupyterNotebookTranslator, "create", create_provider)
    monkeypatch.setattr(api.Config, "check_configuration", credentials)
    monkeypatch.setattr(api.LLMConfig, "validate_connectivity", credentials)
    # Other API tests replace these module attributes; use real workflows here.
    for module in (api, cli):
        monkeypatch.setattr(module, "ProjectTranslator", ProjectTranslator)
        monkeypatch.setattr(module, "ReadmeTranslator", ReadmeTranslator)

    if entrypoint == "api":
        api.run_translation(
            "ko ja fr",
            root_dir=str(tmp_path),
            markdown=mode == "markdown",
            notebook=mode == "notebook",
            readme_only=mode == "readme",
            concurrency=2,
            dry_run=dry_run,
        )
    else:
        flag = {"markdown": "-md", "notebook": "-nb", "readme": "--readme-only"}[mode]
        args = [
            "-l",
            "ko ja fr",
            "-r",
            str(tmp_path),
            flag,
            "--concurrency",
            "2",
            "--no-disclaimer",
            "-y",
        ]
        if dry_run:
            args.append("--dry-run")
        result = CliRunner().invoke(cli.translate_command, args)
        assert result.exit_code == 0, result.output

    if dry_run:
        assert provider.peak == 0
        assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == source_snapshot
    else:
        assert provider.peak == 2
        name = "guide.ipynb" if mode == "notebook" else "README.md"
        assert all(
            (tmp_path / "translations" / lang / name).is_file()
            for lang in ("ko", "ja", "fr")
        )


@pytest.mark.parametrize("invalid", ["0", "-1", "1.5", "two"])
def test_cli_rejects_invalid_limit_before_work(tmp_path, invalid):
    result = CliRunner().invoke(
        cli.translate_command,
        [
            "-l",
            "ko",
            "-r",
            str(tmp_path),
            "-md",
            "--concurrency",
            invalid,
        ],
    )
    assert result.exit_code == 2
    assert "--concurrency" in result.output
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("invalid", [0, -1, True, 1.5, "2", None])
def test_api_rejects_invalid_limit_before_event_file_or_provider_work(
    tmp_path, invalid
):
    with pytest.raises(ValueError, match="concurrency must be a positive integer"):
        api.run_translation(
            "ko",
            root_dir=str(tmp_path),
            markdown=True,
            concurrency=invalid,
            json_events_path=tmp_path / "events.ndjson",
        )
    assert list(tmp_path.iterdir()) == []
