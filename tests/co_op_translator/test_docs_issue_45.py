from __future__ import annotations

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

ISSUE_45_DOCS = [
    ROOT_DIR / "README.md",
    ROOT_DIR / "CONTRIBUTING.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "command-line-guide.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "install-package.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "create-env-file.md",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_issue_45_known_typos_and_stale_phrases_do_not_reappear() -> None:
    combined = "\n".join(_read(path) for path in ISSUE_45_DOCS)

    stale_phrases = [
        "intial",
        "handeled",
        "delete this lin",
        "Co-Op Translator",
        "Co-op translator package",
        "poetry init",
        "co-op-translator translate",
        "Markdown-only mode",
        "markdown-only-mode.md",
        "supported models and services list",
        "Azure Computer Vision",
        "Python 3.10 or higher",
    ]

    for phrase in stale_phrases:
        assert phrase not in combined


def test_contributing_links_new_contributors_to_setup_and_pr_resources() -> None:
    contributing = _read(ROOT_DIR / "CONTRIBUTING.md")

    expected_links = [
        "[Installation guide](./getting_started/command-line-guide/install-package.md)",
        "[Configuration reference](./docs/configuration.md)",
        "[CLI reference](./docs/cli.md)",
        "[Fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)",
        "[Create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)",
    ]

    for link in expected_links:
        assert link in contributing


def test_install_guide_keeps_beginner_setup_paths() -> None:
    install_guide = _read(
        ROOT_DIR / "getting_started" / "command-line-guide" / "install-package.md"
    )

    expected_sections = [
        "## Install from PyPI",
        "## Install from a repository clone",
        "Python 3.10 through 3.12",
        "pip install co-op-translator",
        "poetry install",
        "pip install -e .",
        'translate -l "ko" -md',
    ]

    for section in expected_sections:
        assert section in install_guide
