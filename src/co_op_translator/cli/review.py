from __future__ import annotations

from pathlib import Path

import click

from co_op_translator.utils.common.exit_codes import (
    CliExitError,
    EXIT_CONFIGURATION,
    EXIT_VALIDATION,
)


def _split_language_options(values: tuple[str, ...]) -> list[str]:
    languages: list[str] = []
    for value in values:
        languages.extend(part for part in value.split() if part)
    return languages


@click.command(name="co-op-review")
@click.option(
    "--root-dir",
    "--source",
    "root_dir",
    "-r",
    default=".",
    help="Root directory of the project to review.",
)
@click.option(
    "--translations-dir",
    "--output",
    default=None,
    help="Translation output directory (default: translations under the source).",
)
@click.option(
    "--include",
    "include_patterns",
    multiple=True,
    help="Include source paths matching this glob. Repeat for multiple patterns.",
)
@click.option(
    "--exclude",
    "exclude_patterns",
    multiple=True,
    help="Exclude source paths matching this glob. Repeat for multiple patterns.",
)
@click.option(
    "--language-code",
    "-l",
    multiple=True,
    help='Language code to review. Can be passed multiple times or as "ko ja".',
)
@click.option(
    "--changed-from",
    help=(
        "Git ref to diff against. Reviews committed, staged, unstaged, and "
        "untracked source files."
    ),
)
@click.option(
    "--readme-only",
    is_flag=True,
    help="Review only the root README.md translation.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "github", "json"]),
    default="text",
    show_default=True,
    help="Output format.",
)
def review_command(
    root_dir: str,
    translations_dir: str | None,
    include_patterns: tuple[str, ...],
    exclude_patterns: tuple[str, ...],
    language_code: tuple[str, ...],
    changed_from: str | None,
    output_format: str,
    readme_only: bool,
) -> None:
    """Run deterministic translation review checks without API credentials."""
    from co_op_translator.api.review import run_review

    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        raise CliExitError(
            f"Root directory does not exist: {root_dir}", EXIT_CONFIGURATION
        )
    if not root_path.is_dir():
        raise CliExitError(
            f"Root path is not a directory: {root_dir}", EXIT_CONFIGURATION
        )

    try:
        run_review(
            language_codes=_split_language_options(language_code) or "all",
            root_dir=str(root_path),
            translations_dir=translations_dir,
            include=include_patterns,
            exclude=exclude_patterns,
            markdown=True,
            notebook=True,
            changed_from=changed_from,
            output_format=output_format,
            readme_only=readme_only,
        )
    except RuntimeError as exc:
        raise CliExitError(str(exc), EXIT_VALIDATION) from exc
    except ValueError as exc:
        raise CliExitError(str(exc), EXIT_CONFIGURATION) from exc
