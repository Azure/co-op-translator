from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from co_op_translator.review.checks.freshness import check_translation_freshness
from co_op_translator.review.checks.links import check_local_links
from co_op_translator.review.checks.markdown_integrity import check_markdown_integrity
from co_op_translator.review.checks.structure import check_translation_structure
from co_op_translator.review.discovery import (
    DEFAULT_EXCLUDED_DIRS,
    discover_changed_source_files,
    discover_languages,
    discover_source_files,
)
from co_op_translator.review.models import ReviewSummary
from co_op_translator.review.targets import ReviewTarget, build_review_targets


@dataclass(frozen=True)
class ReviewConfig:
    root_dir: Path
    languages: list[str] = field(default_factory=list)
    changed_from: str | None = None
    excluded_dirs: set[str] = field(default_factory=lambda: set(DEFAULT_EXCLUDED_DIRS))
    targets: list[ReviewTarget] | None = None
    source_extensions: set[str] | None = None


class ReviewRunner:
    def __init__(self, config: ReviewConfig):
        self.config = config

    def run(self) -> ReviewSummary:
        root_dir = self.config.root_dir.resolve()
        targets = self.config.targets or build_review_targets(root_dir=root_dir)
        languages = self.config.languages or sorted(
            {
                language
                for target in targets
                for language in discover_languages(target.translations_dir)
            }
        )

        issues = []
        source_files: list[Path] = []
        for target in targets:
            if self.config.changed_from:
                target_source_files = discover_changed_source_files(
                    root_dir,
                    target.source_root,
                    self.config.changed_from,
                    self.config.excluded_dirs,
                    self.config.source_extensions,
                )
            else:
                target_source_files = discover_source_files(
                    target.source_root,
                    self.config.excluded_dirs,
                    self.config.source_extensions,
                )
            source_files.extend(target_source_files)

            if not languages:
                continue

            issues.extend(
                check_translation_structure(target, target_source_files, languages)
            )
            issues.extend(
                check_translation_freshness(target, target_source_files, languages)
            )
            issues.extend(
                check_markdown_integrity(target, target_source_files, languages)
            )
            issues.extend(check_local_links(target, target_source_files, languages))

        return ReviewSummary(
            root_dir=root_dir,
            source_files=[
                _display_path(root_dir, path) for path in sorted(source_files)
            ],
            languages=languages,
            issues=issues,
        )


def _display_path(root_dir: Path, path: Path) -> Path:
    try:
        return path.relative_to(root_dir)
    except ValueError:
        return path
