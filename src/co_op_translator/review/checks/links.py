from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.review.targets import ReviewTarget

MARKDOWN_LINK_PATTERN = re.compile(r"(!?)\[[^\]]*]\(([^)]+)\)")


def _is_external_link(target: str) -> bool:
    lowered = target.lower()
    return (
        "://" in lowered
        or lowered.startswith("#")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
    )


def _clean_link_target(target: str) -> str:
    target = target.strip().strip("<>")
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target)


def _target_exists(translated_path: Path, target: str) -> bool:
    cleaned = _clean_link_target(target)
    if not cleaned:
        return True
    candidate = Path(cleaned)
    if candidate.is_absolute():
        return candidate.exists()
    return (translated_path.parent / candidate).exists()


def check_local_links(
    target: ReviewTarget, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        if source_file.suffix.lower() == ".ipynb":
            continue
        for language in languages:
            translated_path = target.translated_path(source_file, language)
            if not translated_path.exists():
                continue
            content = translated_path.read_text(encoding="utf-8")
            for is_image, link_target in MARKDOWN_LINK_PATTERN.findall(content):
                if _is_external_link(link_target) or _target_exists(
                    translated_path, link_target
                ):
                    continue
                check_name = "image-link" if is_image else "local-link"
                issues.append(
                    ReviewIssue(
                        check=check_name,
                        severity=ReviewSeverity.WARNING,
                        path=target.display_translated_path(translated_path),
                        language=language,
                        message=f"Local target does not exist: {link_target}",
                    )
                )
    return issues
