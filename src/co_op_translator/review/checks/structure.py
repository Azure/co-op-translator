from __future__ import annotations

from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.review.targets import ReviewTarget


def check_translation_structure(
    target: ReviewTarget, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        for language in languages:
            translated_path = target.translated_path(source_file, language)
            if not translated_path.exists():
                issues.append(
                    ReviewIssue(
                        check="structure",
                        severity=ReviewSeverity.ERROR,
                        path=target.display_source_path(source_file),
                        language=language,
                        message="Missing translated file.",
                    )
                )
    return issues
