from __future__ import annotations

from pathlib import Path

from co_op_translator.api import run_review
from co_op_translator.utils.common.metadata_utils import save_text_metadata_for_source


def _write_source(root: Path, relative_path: str, content: str = "# Hello\n") -> Path:
    source_file = root / relative_path
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text(content, encoding="utf-8")
    return source_file


def _write_translation(
    source_root: Path,
    output_root: Path,
    source_file: Path,
    language: str,
    lang_subdir: str | None = None,
) -> Path:
    lang_root = output_root / language
    if lang_subdir:
        lang_root = lang_root / lang_subdir
    translated_file = lang_root / source_file.relative_to(source_root)
    translated_file.parent.mkdir(parents=True, exist_ok=True)
    translated_file.write_text("# 안녕하세요\n", encoding="utf-8")
    save_text_metadata_for_source(
        lang_root, source_file, language, root_dir=source_root
    )
    return translated_file


def test_run_review_returns_summary_for_default_translation_layout(tmp_path):
    source_file = _write_source(tmp_path, "README.md")
    _write_translation(tmp_path, tmp_path / "translations", source_file, "ko")

    summary = run_review(
        language_codes="ko",
        root_dir=str(tmp_path),
        markdown=True,
    )

    assert summary.error_count == 0
    assert summary.languages == ["ko"]
    assert summary.source_files == [Path("README.md")]


def test_run_review_supports_translation_style_groups(tmp_path):
    docs_root = tmp_path / "docs"
    source_file = _write_source(docs_root, "guide.md")
    output_root = tmp_path / "i18n"
    lang_subdir = "docusaurus-plugin-content-docs/current"
    _write_translation(docs_root, output_root, source_file, "ko", lang_subdir)

    summary = run_review(
        language_codes="ko",
        root_dir=str(tmp_path),
        markdown=True,
        groups=[
            (
                str(docs_root),
                str(output_root / "<lang>" / lang_subdir),
            )
        ],
        output_format="github",
    )

    assert summary.error_count == 0
    assert summary.source_files == [Path("docs") / "guide.md"]


def test_run_review_supports_multiple_root_dirs(tmp_path):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    source1 = _write_source(root1, "one.md")
    source2 = _write_source(root2, "two.md")
    _write_translation(root1, root1 / "translations", source1, "ko")
    _write_translation(root2, root2 / "translations", source2, "ko")

    summary = run_review(
        language_codes="ko",
        root_dir=str(tmp_path),
        markdown=True,
        root_dirs=[str(root1), str(root2)],
    )

    assert summary.error_count == 0
    assert summary.source_files == [
        Path("content1") / "one.md",
        Path("content2") / "two.md",
    ]
