from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

import click

from co_op_translator.review.models import ReviewSummary
from co_op_translator.review.runner import ReviewConfig, ReviewRunner
from co_op_translator.review.targets import build_review_targets
from co_op_translator.utils.common.lang_utils import normalize_language_codes
from co_op_translator.utils.common.logging_utils import setup_logging

logger = logging.getLogger(__name__)


def _build_review_types(markdown: bool, images: bool, notebook: bool) -> list[str]:
    review_types: list[str] = []
    if markdown:
        review_types.append("markdown")
    if images:
        review_types.append("images")
    if notebook:
        review_types.append("notebook")
    if not review_types:
        review_types = ["markdown", "notebook", "images"]
    return review_types


def _source_extensions_for_review_types(review_types: list[str]) -> set[str]:
    source_extensions: set[str] = set()
    if "markdown" in review_types:
        source_extensions.update({".md", ".mdx"})
    if "notebook" in review_types:
        source_extensions.add(".ipynb")
    return source_extensions


def _normalize_review_languages(language_codes: str | Iterable[str]) -> list[str]:
    if isinstance(language_codes, str):
        if language_codes == "all":
            return []
        raw_codes = [code for code in language_codes.split() if code]
    else:
        raw_codes = [code for code in language_codes if code]
    return normalize_language_codes(raw_codes) if raw_codes else []


def run_review(
    language_codes: str | Iterable[str] = "all",
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = True,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: Iterable[str] | None = None,
    groups: Iterable[tuple[str, str | None]] | None = None,
    repo_url: str | None = None,
    glossaries: Iterable[str] | None = None,
    dry_run: bool = False,
    changed_from: str | None = None,
    output_format: str = "text",
    fail_on_warnings: bool = False,
) -> ReviewSummary:
    """Programmatic deterministic review entrypoint.

    The signature intentionally mirrors ``run_translation`` where possible so
    automation can switch between translate and review workflows with minimal
    branching. Review ignores mutating translation-only options such as
    ``update``, ``yes``, ``add_disclaimer``, ``repo_url``, ``glossaries``, and
    ``dry_run``.
    """
    del update, yes, add_disclaimer, image_dir, repo_url, glossaries, dry_run

    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        raise ValueError(f"Root directory does not exist: {root_dir}")
    if not root_path.is_dir():
        raise ValueError(f"Root path is not a directory: {root_dir}")

    log_file_path = setup_logging(
        root_path, debug=debug, save_logs=save_logs, command_name="co-op-review"
    )
    if debug:
        logging.debug("Debug mode enabled.")
    if save_logs and log_file_path is not None:
        click.echo(f"Logs will be saved to: {log_file_path}")

    review_types = _build_review_types(markdown, images, notebook)
    logger.info("Review mode: %s", ", ".join(review_types))

    targets = build_review_targets(
        root_dir=root_path,
        translations_dir=translations_dir,
        root_dirs=root_dirs,
        groups=groups,
    )
    languages = _normalize_review_languages(language_codes)

    summary = ReviewRunner(
        ReviewConfig(
            root_dir=root_path,
            languages=languages,
            changed_from=changed_from,
            targets=targets,
            source_extensions=_source_extensions_for_review_types(review_types),
        )
    ).run()

    if output_format == "github":
        click.echo(summary.to_github_markdown())
    elif output_format == "text":
        click.echo(summary.to_text())
    else:
        raise ValueError(f"Unsupported review output format: {output_format}")

    if summary.error_count or (fail_on_warnings and summary.warning_count):
        raise RuntimeError(
            "co-op-review found "
            f"{summary.error_count} error(s) and {summary.warning_count} warning(s)."
        )

    return summary
