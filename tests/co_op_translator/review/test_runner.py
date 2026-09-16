from __future__ import annotations

from pathlib import Path

import pytest
from click.testing import CliRunner

from co_op_translator.cli.review import review_command
from co_op_translator.review.models import ReviewSeverity
from co_op_translator.review.runner import ReviewConfig, ReviewRunner
from co_op_translator.utils.common.metadata_utils import save_text_metadata_for_source


def _write_source(root: Path, relative_path: str, content: str = "# Hello\n") -> Path:
    source_file = root / relative_path
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text(content, encoding="utf-8")
    return source_file


def _write_translation(
    root: Path, source_file: Path, language: str, content: str = "# 안녕하세요\n"
) -> Path:
    translated_file = root / "translations" / language / source_file.relative_to(root)
    translated_file.parent.mkdir(parents=True, exist_ok=True)
    translated_file.write_text(content, encoding="utf-8")
    save_text_metadata_for_source(
        root / "translations" / language,
        source_file,
        language,
        root_dir=root,
    )
    return translated_file


def test_review_runner_passes_for_fresh_translation(tmp_path):
    source_file = _write_source(tmp_path, "README.md")
    _write_translation(tmp_path, source_file, "ko")

    summary = ReviewRunner(ReviewConfig(tmp_path, languages=["ko"])).run()

    assert summary.error_count == 0
    assert summary.warning_count == 0
    assert summary.source_files == [Path("README.md")]


def test_review_runner_reports_missing_translation(tmp_path):
    _write_source(tmp_path, "README.md")

    summary = ReviewRunner(ReviewConfig(tmp_path, languages=["ko"])).run()

    assert summary.error_count == 1
    issue = summary.issues[0]
    assert issue.check == "structure"
    assert issue.severity == ReviewSeverity.ERROR


def test_review_runner_reports_stale_translation_metadata(tmp_path):
    source_file = _write_source(tmp_path, "README.md", "# Hello\n")
    _write_translation(tmp_path, source_file, "ko")
    source_file.write_text("# Hello again\n", encoding="utf-8")

    summary = ReviewRunner(ReviewConfig(tmp_path, languages=["ko"])).run()

    assert summary.error_count == 1
    assert summary.issues[0].check == "freshness"


def test_review_runner_reports_markdown_integrity_errors(tmp_path):
    source_file = _write_source(
        tmp_path, "README.md", "# Hello\n\n```python\nprint(1)\n```\n"
    )
    _write_translation(
        tmp_path, source_file, "ko", "# 안녕하세요\n\n```python\nprint(1)\n"
    )

    summary = ReviewRunner(ReviewConfig(tmp_path, languages=["ko"])).run()

    assert summary.error_count == 1
    assert summary.issues[0].check == "markdown-integrity"


def test_review_runner_reports_local_link_warnings(tmp_path):
    source_file = _write_source(tmp_path, "README.md")
    _write_translation(tmp_path, source_file, "ko", "[missing](missing.md)\n")

    summary = ReviewRunner(ReviewConfig(tmp_path, languages=["ko"])).run()

    assert summary.error_count == 0
    assert summary.warning_count == 1
    assert summary.issues[0].check == "local-link"


def test_review_cli_outputs_github_summary(tmp_path):
    source_file = _write_source(tmp_path, "README.md")
    _write_translation(tmp_path, source_file, "ko")

    result = CliRunner().invoke(
        review_command,
        ["--root-dir", str(tmp_path), "--language-code", "ko", "--format", "github"],
    )

    assert result.exit_code == 0
    assert "## Co-op Review" in result.output
    assert "Status: **passed**" in result.output


def test_readme_review_ignores_untranslated_docs_and_nested_readmes(tmp_path):
    source_file = _write_source(tmp_path, "README.md")
    _write_translation(tmp_path, source_file, "ko")
    _write_source(tmp_path, "docs/guide.md")
    _write_source(tmp_path, "docs/README.md")
    _write_source(tmp_path, "examples/demo.ipynb", "{}")

    result = CliRunner().invoke(
        review_command,
        ["-r", str(tmp_path), "-l", "ko", "--readme-only", "--format", "github"],
    )

    assert result.exit_code == 0, result.output
    assert "| Source files reviewed | 1 |" in result.output
    assert "Status: **passed**" in result.output
    # Full review still reports the other missing translations.
    assert ReviewRunner(ReviewConfig(tmp_path, languages=["ko"])).run().error_count == 3


@pytest.mark.parametrize("problem", ["missing-source", "missing-translation", "stale"])
def test_readme_review_fails_for_incomplete_output(tmp_path, problem):
    if problem != "missing-source":
        source = _write_source(tmp_path, "README.md")
        if problem == "stale":
            _write_translation(tmp_path, source, "ko")
            source.write_text("# Updated source\n", encoding="utf-8")

    result = CliRunner().invoke(
        review_command, ["-r", str(tmp_path), "-l", "ko", "--readme-only"]
    )

    assert result.exit_code == 1
    assert "README.md" in result.output


def test_readme_review_intersects_changed_sources(tmp_path, monkeypatch):
    from co_op_translator.review import runner

    source = _write_source(tmp_path, "README.md")
    guide = _write_source(tmp_path, "docs/guide.md")
    _write_translation(tmp_path, source, "ko")
    monkeypatch.setattr(
        runner, "discover_changed_source_files", lambda *args: [source, guide]
    )
    config = ReviewConfig(
        tmp_path, languages=["ko"], changed_from="origin/main", readme_only=True
    )
    summary = ReviewRunner(config).run()
    assert summary.source_files == [Path("README.md")]
    assert summary.error_count == 0

    monkeypatch.setattr(runner, "discover_changed_source_files", lambda *args: [guide])
    assert ReviewRunner(config).run().source_files == []
