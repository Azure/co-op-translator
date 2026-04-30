from __future__ import annotations

from pathlib import Path
import re

LANG_TABLE_START = "<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->"
LANG_TABLE_END = "<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->"
OTHER_COURSES_START = "<!-- CO-OP TRANSLATOR OTHER COURSES START -->"
OTHER_COURSES_END = "<!-- CO-OP TRANSLATOR OTHER COURSES END -->"


def _replace_between_markers_generic(
    readme_text: str, new_block: str, start_marker: str, end_marker: str
) -> str:
    """
    Replace content between the provided start/end markers with the new block.
    Markers are included in the replacement. If markers are missing, returns original text.
    """
    # Case-insensitive detection of markers so users can vary casing
    lower_text = readme_text.lower()
    start_idx = lower_text.find(start_marker.lower())
    end_idx = lower_text.find(end_marker.lower())
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        return readme_text

    # Expand end to include the end marker line completely
    end_idx_inclusive = end_idx + len(end_marker)

    before = readme_text[:start_idx].rstrip()
    after = readme_text[end_idx_inclusive:].lstrip()

    # Ensure surrounding newlines for readability
    pieces = []
    if before:
        pieces.append(before)
    pieces.append(new_block.strip())
    if after:
        pieces.append(after)
    result = "\n\n".join(pieces)
    if readme_text.endswith("\n"):
        result = result.rstrip("\n") + "\n"
    else:
        result = result.rstrip("\n")
    return result


def replace_between_markers(readme_text: str, new_block: str) -> str:
    """
    Backward-compatible helper that replaces between the LANGUAGES TABLE markers.
    """
    return _replace_between_markers_generic(
        readme_text, new_block, LANG_TABLE_START, LANG_TABLE_END
    )


def load_languages_table_template() -> str:
    """Load the bundled languages table template markdown."""
    try:
        from importlib import resources

        with resources.open_text(
            "co_op_translator.templates", "languages_table.md", encoding="utf-8"
        ) as f:
            return f.read()
    except Exception:
        return ""


def load_other_courses_template() -> str:
    """Load the bundled other courses template markdown."""
    try:
        from importlib import resources

        with resources.open_text(
            "co_op_translator.templates", "other_courses.md", encoding="utf-8"
        ) as f:
            return f.read()
    except Exception:
        return ""


def render_updated_readme_languages_table(
    readme_text: str, repo_url: str | None = None
) -> str:
    """Return README content with the bundled languages table rendered."""
    template = load_languages_table_template()
    if not template:
        return readme_text
    # Strip markdownlint directives from template to avoid injecting them into user README
    template = re.sub(
        r"^\s*<!--\s*markdownlint-disable[^>]*-->\s*\n?",
        "",
        template,
        flags=re.IGNORECASE,
    )

    # Personalize advisory block in template (if repo_url provided)
    repo_url_value = (
        repo_url.strip() if isinstance(repo_url, str) and repo_url.strip() else None
    )
    if repo_url_value:
        repo_url_value = repo_url_value.rstrip()
        repo_url_without_git = (
            repo_url_value[:-4] if repo_url_value.endswith(".git") else repo_url_value
        )
        repo_url_with_git = (
            repo_url_value
            if repo_url_value.endswith(".git")
            else f"{repo_url_value}.git"
        )

        # Handle `<repo_url>` placeholders before appending repo name snippets
        template = template.replace("<repo_url>.git", repo_url_with_git)
        template = template.replace("<repo_url>", repo_url_value)

        # Replace generic GitHub snippet placeholders when present in template
        template = template.replace("https://github.com/*****.git", repo_url_with_git)

        try:
            tail = repo_url_without_git.rstrip("/").split("/")[-1]
            repo_name_value = tail[:-4] if tail.endswith(".git") else tail
        except Exception:
            repo_name_value = None

        if repo_name_value:
            for placeholder in ("cd <repo_name>", "cd *****"):
                template = template.replace(placeholder, f"cd {repo_name_value}")

    lower_t = template.lower()
    start_idx = lower_t.find(LANG_TABLE_START.lower())
    end_idx = lower_t.find(LANG_TABLE_END.lower())
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        return False

    inner_content = template[start_idx + len(LANG_TABLE_START) : end_idx].strip()
    new_block = f"{LANG_TABLE_START}\n{inner_content}\n{LANG_TABLE_END}"

    return _replace_between_markers_generic(
        readme_text, new_block, LANG_TABLE_START, LANG_TABLE_END
    )


def render_updated_readme_other_courses(readme_text: str) -> str:
    """Return README content with the bundled Other courses block rendered."""
    template = load_other_courses_template()
    if not template:
        return readme_text
    return _replace_between_markers_generic(
        readme_text, template, OTHER_COURSES_START, OTHER_COURSES_END
    )


def update_readme_languages_table(
    readme_path: Path, repo_url: str | None = None
) -> bool:
    """
    Update README languages table between markers using bundled template.
    Optionally appends a 'Prefer to Clone Locally?' advisory block INSIDE the markers.

    If repo_url is provided, it will be used to personalize the snippet; otherwise
    the advisory will be shown with placeholder stars as given by the user.

    Returns True if updated, False otherwise.
    """
    if not readme_path.exists():
        return False
    original = readme_path.read_text(encoding="utf-8")
    updated = render_updated_readme_languages_table(original, repo_url=repo_url)
    if updated != original:
        readme_path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def update_readme_other_courses(readme_path: Path) -> bool:
    """
    Update README 'Other courses' section between markers using bundled template.
    Returns True if updated, False otherwise.
    """
    if not readme_path.exists():
        return False
    original = readme_path.read_text(encoding="utf-8")
    updated = render_updated_readme_other_courses(original)
    if updated != original:
        readme_path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False
