import json
from pathlib import Path

from co_op_translator.review.checks.completeness import (
    check_translation_completeness,
)
from co_op_translator.review.runner import ReviewConfig, ReviewRunner
from co_op_translator.review.targets import ReviewTarget


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _checks(root: Path, relative: str, source: str, translated: str) -> set[str]:
    source_path = _write(root / relative, source)
    _write(root / "i18n" / "ko" / relative, translated)
    target = ReviewTarget(root, root / "i18n")
    return {
        issue.check
        for issue in check_translation_completeness(target, [source_path], ["ko"])
    }


def test_completeness_reports_missing_duplicate_untranslated_and_literal_damage(
    tmp_path,
):
    long_source = (
        "This explanatory paragraph has enough English words to detect unchanged prose."
    )
    checks = _checks(
        tmp_path,
        "guide.md",
        f"# Guide\n\n{long_source}\n\nSecond source paragraph.\n\n`docs/setup.md`\n",
        f"# 안내\n\n{long_source}\n\n{long_source}\n\n`docs/changed.md`\n",
    )

    assert "duplicated-blocks" in checks
    assert "suspicious-untranslated-prose" in checks
    assert "protected-literals" in checks

    missing = _checks(
        tmp_path / "missing",
        "guide.md",
        "# Guide\n\nFirst paragraph.\n\nSecond paragraph.\n",
        "# 안내\n\n첫 번째 문단.\n",
    )
    assert "missing-blocks" in missing


def test_completeness_checks_markdown_cells_in_notebooks(tmp_path):
    source = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["Use `python app.py` to start the documented service."],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "source": ["print('ignored')"],
                "outputs": [],
                "execution_count": None,
            },
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    translated = json.loads(json.dumps(source))
    translated["cells"][0]["source"] = [
        "문서화된 서비스를 시작하려면 `python changed.py`를 사용하세요."
    ]

    checks = _checks(
        tmp_path,
        "guide.ipynb",
        json.dumps(source),
        json.dumps(translated),
    )

    assert "protected-literals" in checks


def test_review_uses_custom_paths_filters_and_excludes_nested_output(tmp_path):
    source = tmp_path / "docs"
    _write(source / "keep.md", "# Keep\n")
    _write(source / "skip.md", "# Skip\n")
    _write(source / "i18n" / "ko" / "keep.md", "# 유지\n")
    _write(source / "i18n" / "ko" / "generated.md", "# Generated\n")

    summary = ReviewRunner(
        ReviewConfig(
            source,
            languages=["ko"],
            targets=[ReviewTarget(source, source / "i18n")],
            include_patterns=("**/*.md",),
            exclude_patterns=("skip.md",),
        )
    ).run()

    assert summary.source_files == [Path("keep.md")]
    assert all("generated.md" not in issue.location() for issue in summary.issues)
    payload = summary.to_dict()
    assert payload["schema"] == "co-op.translation.verification.v1"
    assert set(payload["verification"]) == {
        "source_hash_current",
        "markdown_structure_valid",
        "translation_appears_complete",
        "protected_literals_preserved",
        "links_valid",
    }
