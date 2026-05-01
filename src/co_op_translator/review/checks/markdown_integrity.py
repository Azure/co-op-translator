from __future__ import annotations

import json
import re
from pathlib import Path

from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.review.targets import ReviewTarget

FENCE_PATTERN = re.compile(r"^\s*(```|~~~)", re.MULTILINE)


def _has_frontmatter(content: str) -> bool:
    return content.startswith("---\n")


def _frontmatter_is_closed(content: str) -> bool:
    if not _has_frontmatter(content):
        return True
    return content.find("\n---", 4) != -1


def _fence_count(content: str) -> int:
    return len(FENCE_PATTERN.findall(content))


def _check_markdown_file(
    target: ReviewTarget, source_file: Path, translated_path: Path, language: str
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    source_content = source_file.read_text(encoding="utf-8")
    translated_content = translated_path.read_text(encoding="utf-8")
    relative_path = target.display_source_path(source_file)

    if _has_frontmatter(source_content):
        if not _has_frontmatter(translated_content):
            issues.append(
                ReviewIssue(
                    check="markdown-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message="Translated file is missing source frontmatter.",
                )
            )
        elif not _frontmatter_is_closed(translated_content):
            issues.append(
                ReviewIssue(
                    check="markdown-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message="Translated frontmatter is not closed.",
                )
            )

    if _fence_count(source_content) != _fence_count(translated_content):
        issues.append(
            ReviewIssue(
                check="markdown-integrity",
                severity=ReviewSeverity.ERROR,
                path=relative_path,
                language=language,
                message="Code fence count differs from the source file.",
            )
        )

    return issues


def _check_notebook_file(
    target: ReviewTarget, source_file: Path, translated_path: Path, language: str
) -> list[ReviewIssue]:
    try:
        json.loads(translated_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return [
            ReviewIssue(
                check="notebook-integrity",
                severity=ReviewSeverity.ERROR,
                path=target.display_source_path(source_file),
                language=language,
                message="Translated notebook is not valid JSON.",
            )
        ]
    return []


def check_markdown_integrity(
    target: ReviewTarget, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        for language in languages:
            translated_path = target.translated_path(source_file, language)
            if not translated_path.exists():
                continue
            if source_file.suffix.lower() == ".ipynb":
                issues.extend(
                    _check_notebook_file(target, source_file, translated_path, language)
                )
            else:
                issues.extend(
                    _check_markdown_file(target, source_file, translated_path, language)
                )
    return issues
