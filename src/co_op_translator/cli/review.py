from __future__ import annotations

from pathlib import Path

import click

from co_op_translator.api.review import run_review


def _split_language_options(values: tuple[str, ...]) -> list[str]:
    languages: list[str] = []
    for value in values:
        languages.extend(part for part in value.split() if part)
    return languages


@click.command(name="co-op-review")
@click.option(
    "--root-dir",
    "-r",
    default=".",
    help="Root directory of the project to review.",
)
@click.option(
    "--language-code",
    "-l",
    multiple=True,
    help='Language code to review. Can be passed multiple times or as "ko ja".',
)
@click.option(
    "--changed-from",
    help="Git ref to diff against. When provided, only changed source files are reviewed.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "github"]),
    default="text",
    show_default=True,
    help="Output format.",
)
def review_command(
    root_dir: str,
    language_code: tuple[str, ...],
    changed_from: str | None,
    output_format: str,
) -> None:
    """Run deterministic translation review checks without API credentials."""
    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        raise click.ClickException(f"Root directory does not exist: {root_dir}")
    if not root_path.is_dir():
        raise click.ClickException(f"Root path is not a directory: {root_dir}")

    try:
        run_review(
            language_codes=_split_language_options(language_code) or "all",
            root_dir=str(root_path),
            markdown=True,
            notebook=True,
            changed_from=changed_from,
            output_format=output_format,
        )
    except RuntimeError as exc:
        raise click.ClickException(str(exc)) from exc
