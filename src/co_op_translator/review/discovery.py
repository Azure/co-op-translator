from __future__ import annotations

import subprocess
from pathlib import Path

SOURCE_EXTENSIONS = {".md", ".mdx", ".ipynb"}
DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "dist",
    "htmlcov",
    "logs",
    "node_modules",
    "site",
    "translated_images",
    "translations",
    "venv",
}


def is_source_file(path: Path, source_extensions: set[str] | None = None) -> bool:
    return path.suffix.lower() in (source_extensions or SOURCE_EXTENSIONS)


def is_excluded(path: Path, excluded_dirs: set[str]) -> bool:
    return any(part in excluded_dirs for part in path.parts)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def discover_languages(translations_dir: Path) -> list[str]:
    if not translations_dir.is_dir():
        return []
    return sorted(
        path.name
        for path in translations_dir.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def discover_source_files(
    root_dir: Path, excluded_dirs: set[str], source_extensions: set[str] | None = None
) -> list[Path]:
    files: list[Path] = []
    for path in root_dir.rglob("*"):
        if not path.is_file() or not is_source_file(path, source_extensions):
            continue
        relative_path = path.relative_to(root_dir)
        if is_excluded(relative_path, excluded_dirs):
            continue
        files.append(path)
    return sorted(files)


def discover_changed_source_files(
    git_root: Path,
    source_root: Path,
    changed_from: str,
    excluded_dirs: set[str],
    source_extensions: set[str] | None = None,
) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{changed_from}...HEAD"],
        cwd=git_root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return discover_source_files(source_root, excluded_dirs, source_extensions)

    files: list[Path] = []
    for line in result.stdout.splitlines():
        relative_path = Path(line.strip())
        if not line.strip() or not is_source_file(relative_path, source_extensions):
            continue
        if is_excluded(relative_path, excluded_dirs):
            continue
        full_path = (git_root / relative_path).resolve()
        if full_path.is_file() and _is_relative_to(full_path, source_root):
            files.append(full_path)
    return sorted(files)
