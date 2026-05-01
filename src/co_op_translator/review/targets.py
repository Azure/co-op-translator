from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ReviewTarget:
    source_root: Path
    translations_dir: Path
    lang_subdir: Path | None = None

    def language_root(self, language: str) -> Path:
        lang_root = self.translations_dir / language
        if self.lang_subdir:
            lang_root = lang_root / self.lang_subdir
        return lang_root

    def translated_path(self, source_file: Path, language: str) -> Path:
        return self.language_root(language) / source_file.relative_to(self.source_root)

    def display_source_path(self, source_file: Path) -> Path:
        try:
            return source_file.relative_to(self.source_root)
        except ValueError:
            return source_file

    def display_translated_path(self, translated_file: Path) -> Path:
        try:
            return translated_file.relative_to(self.translations_dir)
        except ValueError:
            return translated_file


def split_lang_placeholder(path: str) -> tuple[str, str | None]:
    placeholder = "<lang>"
    if placeholder not in path:
        return path, None

    prefix, suffix = path.split(placeholder, 1)
    prefix = prefix.rstrip("/\\")
    suffix = suffix.lstrip("/\\")
    return prefix, (suffix or None)


def resolve_output_root(source_root: Path, output_root: str | None) -> Path:
    if output_root is None:
        return source_root / "translations"

    output_path = Path(output_root)
    if output_path.is_absolute():
        return output_path.resolve()
    return (source_root / output_path).resolve()


def build_review_targets(
    *,
    root_dir: str | Path,
    translations_dir: str | None = None,
    root_dirs: Iterable[str] | None = None,
    groups: Iterable[tuple[str, str | None]] | None = None,
) -> list[ReviewTarget]:
    if groups is not None:
        targets: list[ReviewTarget] = []
        for source_root_value, output_template in list(groups):
            source_root = Path(source_root_value).resolve()
            output_root = output_template
            lang_subdir: str | None = None
            if output_template is not None:
                output_root, lang_subdir = split_lang_placeholder(output_template)
            targets.append(
                ReviewTarget(
                    source_root=source_root,
                    translations_dir=resolve_output_root(source_root, output_root),
                    lang_subdir=Path(lang_subdir) if lang_subdir else None,
                )
            )
        return targets

    if root_dirs is not None:
        targets = []
        for source_root_value in list(root_dirs):
            source_root = Path(source_root_value).resolve()
            targets.append(
                ReviewTarget(
                    source_root=source_root,
                    translations_dir=resolve_output_root(source_root, translations_dir),
                )
            )
        return targets

    source_root = Path(root_dir).resolve()
    return [
        ReviewTarget(
            source_root=source_root,
            translations_dir=resolve_output_root(source_root, translations_dir),
        )
    ]
