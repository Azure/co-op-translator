from __future__ import annotations

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

ENTRYPOINT_DOCS = [
    ROOT_DIR / "README.md",
    ROOT_DIR / "getting_started" / "command-reference.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "command-line-guide.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "install-package.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "create-env-file.md",
    ROOT_DIR / "getting_started" / "command-line-guide" / "translator-your-project.md",
    ROOT_DIR
    / "getting_started"
    / "github-actions-guide"
    / "github-actions-guide-public.md",
    ROOT_DIR
    / "getting_started"
    / "github-actions-guide"
    / "github-actions-guide-org.md",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_getting_started_delegates_full_references_to_mkdocs_pages() -> None:
    command_reference = _read(ROOT_DIR / "getting_started" / "command-reference.md")
    command_line_guide = _read(
        ROOT_DIR / "getting_started" / "command-line-guide" / "command-line-guide.md"
    )
    readme = _read(ROOT_DIR / "README.md")
    github_action_public = _read(
        ROOT_DIR
        / "getting_started"
        / "github-actions-guide"
        / "github-actions-guide-public.md"
    )
    github_action_org = _read(
        ROOT_DIR
        / "getting_started"
        / "github-actions-guide"
        / "github-actions-guide-org.md"
    )

    assert "[CLI reference](../docs/cli.md)" in command_reference
    assert "[Configuration](../../docs/configuration.md)" in command_line_guide
    assert "[Configuration](../../docs/configuration.md)" in github_action_public
    assert "[Configuration](../../docs/configuration.md)" in github_action_org
    assert "[CLI reference](./docs/cli.md)" in readme
    assert "[Python API](./docs/api.md)" in readme


def test_getting_started_does_not_repeat_removed_or_stale_cli_flags() -> None:
    combined = "\n".join(_read(path) for path in ENTRYPOINT_DOCS)

    stale_patterns = [
        r"\btranslate\s+[^\n]*\s-a\b",
        r"\btranslate\s+[^\n]*\s-chk\b",
        r"markdown-only-mode\.md",
        r"set-up-resources/",
        r"supported-models-and-services",
    ]
    for pattern in stale_patterns:
        assert re.search(pattern, combined) is None


def test_entrypoint_relative_links_resolve() -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

    for doc_path in ENTRYPOINT_DOCS:
        for raw_target in link_pattern.findall(_read(doc_path)):
            target = raw_target.split("#", 1)[0]
            if not target or re.match(r"^[a-z]+:", target):
                continue

            resolved = (doc_path.parent / target).resolve()
            assert resolved.exists(), f"{doc_path} links to missing file {raw_target}"
