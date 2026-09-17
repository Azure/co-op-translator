from __future__ import annotations

from pathlib import Path
import subprocess

from co_op_translator.review.discovery import (
    DEFAULT_EXCLUDED_DIRS,
    discover_changed_source_files,
)


def _git(repo: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", *arguments],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _write(repo: Path, relative_path: str, content: str = "# Document\n") -> Path:
    path = repo / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _initialize_repository(repo: Path) -> str:
    _git(repo, "init")
    _git(repo, "config", "user.email", "review-tests@example.com")
    _git(repo, "config", "user.name", "Review Tests")
    _write(repo, ".gitignore", "ignored.md\n")
    _write(repo, "README.md")
    _write(repo, "docs/existing.md")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "Initial content")
    return _git(repo, "rev-parse", "HEAD")


def test_changed_source_discovery_includes_committed_and_local_files(tmp_path):
    base_revision = _initialize_repository(tmp_path)

    committed = _write(tmp_path, "docs/committed.md")
    _git(tmp_path, "add", committed.relative_to(tmp_path).as_posix())
    _git(tmp_path, "commit", "-m", "Add committed document")

    unstaged = _write(tmp_path, "README.md", "# Updated locally\n")
    staged = _write(tmp_path, "docs/staged.md")
    _git(tmp_path, "add", staged.relative_to(tmp_path).as_posix())
    untracked = _write(tmp_path, "docs/한글 guide.md")

    _write(tmp_path, "ignored.md")
    _write(tmp_path, "notes.txt", "not a translation source\n")
    _write(tmp_path, "translations/ko/local.md")

    discovered = discover_changed_source_files(
        tmp_path,
        tmp_path,
        base_revision,
        set(DEFAULT_EXCLUDED_DIRS),
    )

    assert {path.relative_to(tmp_path) for path in discovered} == {
        committed.relative_to(tmp_path),
        staged.relative_to(tmp_path),
        unstaged.relative_to(tmp_path),
        untracked.relative_to(tmp_path),
    }


def test_changed_source_discovery_falls_back_when_git_diff_fails(tmp_path):
    _initialize_repository(tmp_path)
    source = _write(tmp_path, "docs/local.md")

    discovered = discover_changed_source_files(
        tmp_path,
        tmp_path,
        "missing-ref",
        set(DEFAULT_EXCLUDED_DIRS),
    )

    assert source in discovered
