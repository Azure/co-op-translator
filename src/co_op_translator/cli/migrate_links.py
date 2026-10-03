"""
Migrate-links command: reprocess translated markdowns that contain .ipynb links
to update them to translated notebooks when available (and keep originals otherwise).

This performs link-only processing using markdown link utilities,
so there are no LLM calls and it's fast and idempotent.
"""

import logging
from pathlib import Path
import click
import os
from urllib.parse import urlparse

from co_op_translator.config.base_config import Config
from co_op_translator.utils.common.progress import get_progress_reporter
from co_op_translator.utils.markdown.notebook_links import (
    migrate_notebook_links,
    update_notebook_links,
)
from co_op_translator.utils.common.file_utils import (
    map_original_to_translated,
    canonicalize_image_links_in_translations,
)
from co_op_translator.utils.common.logging_utils import setup_logging
from co_op_translator.config.constants import (
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.common.lang_utils import normalize_language_codes
from co_op_translator.utils.common.files.discovery import filter_files
from co_op_translator.utils.common.files.project_paths import ProjectPathConfig
from co_op_translator.utils.common.exit_codes import (
    CliExitError,
    EXIT_CONFIGURATION,
    EXIT_FATAL,
)
from co_op_translator.utils.markdown.link_placeholders import markdown_link_destinations

logger = logging.getLogger(__name__)


@click.command(name="migrate-links")
@click.option(
    "--language-codes",
    "-l",
    required=True,
    help='Space-separated language codes to process (e.g., "ko ja" or "all").',
)
@click.option(
    "--root-dir",
    "--source",
    "root_dir",
    "-r",
    default=".",
    help="Root directory of the project (default is current directory).",
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
    "--image-dir",
    default="translated_images",
    help="Base directory for translated images (relative to --root-dir).",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Perform a dry run without writing changes.",
)
@click.option(
    "--fallback-to-original/--no-fallback-to-original",
    default=True,
    help=(
        "If a translated notebook is missing, rewrite links to point to the original notebook. "
        "Enabled by default."
    ),
)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
@click.option(
    "--save-logs",
    "-s",
    is_flag=True,
    help="Save logs to the logs/ directory under --root-dir (always at DEBUG level).",
)
@click.option(
    "--yes",
    "--non-interactive",
    "yes",
    "-y",
    is_flag=True,
    help="Automatically confirm prompts (useful when using -l 'all').",
)
def migrate_links_command(
    language_codes,
    root_dir,
    translations_dir,
    include_patterns,
    exclude_patterns,
    image_dir,
    dry_run,
    fallback_to_original,
    debug,
    yes,
    save_logs,
):
    """
    Reprocess only translated markdown files that contain .ipynb links and
    update links to point to translated notebooks when available.
    """
    reporter = get_progress_reporter()
    try:
        # Link migration is entirely local and does not require provider credentials.
        try:
            path_config = ProjectPathConfig.resolve(
                source=root_dir,
                output=translations_dir,
                include=include_patterns,
                exclude=exclude_patterns,
            )
        except ValueError as exc:
            raise CliExitError(str(exc), EXIT_CONFIGURATION) from exc
        root_path = path_config.source_root

        log_file_path = setup_logging(
            root_path, debug=debug, save_logs=save_logs, command_name="migrate-links"
        )
        if debug:
            logging.debug("Debug mode enabled.")
        reporter.header(
            command="migrate-links",
            root_dir=root_path,
            languages=language_codes,
            modes=["links"],
        )
        if save_logs and log_file_path is not None:
            reporter.info(f"Logs will be saved to: {log_file_path}")

        translations_dir = path_config.output_root

        if not translations_dir.exists():
            reporter.info(f"No translations directory found at: {translations_dir}")
            return

        allowed_markdown: set[Path] = set()
        discovery_exclusions = path_config.discovery_exclusions()
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            allowed_markdown.update(
                path.relative_to(root_path)
                for path in filter_files(
                    root_path,
                    discovery_exclusions,
                    ext,
                    include_patterns=path_config.include_patterns,
                    exclude_patterns=path_config.exclude_patterns,
                )
            )

        # Canonicalize legacy alias-based language segments in links across translated content
        try:
            md_fix, nb_fix = canonicalize_image_links_in_translations(
                translations_dir=translations_dir,
                image_dir=(root_path / image_dir),
            )
            if md_fix or nb_fix:
                reporter.success(
                    "Canonicalized alias language segments in links: "
                    f"markdown={md_fix}, notebooks={nb_fix}"
                )
        except Exception as e:
            logger.debug(f"Canonicalization step skipped: {e}")

        # Warning and confirmation when processing all languages
        if isinstance(language_codes, str) and language_codes.lower() == "all":
            reporter.warning(
                "Processing 'all' languages can take significant time on large projects."
            )
            reporter.info(
                "For efficiency, contributors usually handle individual languages separately."
            )
            if not yes:
                confirmation_all = click.prompt(
                    "Do you still want to proceed with ALL languages? Type 'yes' to continue",
                    type=str,
                )
                if confirmation_all.lower() != "yes":
                    reporter.info("Operation for 'all' languages cancelled.")
                    return
                else:
                    reporter.info("Proceeding with operation for all languages...")
            else:
                reporter.info("Auto-confirming operation for all languages...")

        # Parse language codes list (support "all")
        if isinstance(language_codes, str) and language_codes.lower() == "all":
            lang_list = Config.get_language_codes()
        else:
            lang_list = [
                code.strip() for code in language_codes.split() if code.strip()
            ]
            lang_list = normalize_language_codes(lang_list)
        if not lang_list:
            raise click.ClickException("No valid language codes provided.")

        total_scanned = 0
        total_matched = 0  # files with at least one actionable in-root .ipynb link
        total_changed = 0
        total_candidates_updatable = 0  # files needing at least one update
        total_candidates_already = (
            0  # files where all actionable links already point to translation
        )
        total_candidates_missing = (
            0  # files where actionable links lack translated counterpart
        )

        for lang in lang_list:
            lang_dir = translations_dir / lang
            if not lang_dir.exists():
                logger.info(f"Language directory missing, skipping: {lang_dir}")
                continue

            # Find translated markdowns and show progress bar
            md_files: list[Path] = []
            for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                md_files.extend(lang_dir.rglob(f"*{ext}"))
            for md_translated in reporter.iter(
                md_files,
                description=f"Scanning {lang_dir.name} markdown links",
                unit="file",
            ):
                total_scanned += 1
                try:
                    content = md_translated.read_text(encoding="utf-8")
                except Exception:
                    logger.warning(f"Failed to read: {md_translated}")
                    continue

                # Quick filter: only process files containing supported notebook links
                if not any(ext in content for ext in SUPPORTED_NOTEBOOK_EXTENSIONS):
                    continue

                # Derive original md path from translated path (needed to resolve links)
                try:
                    relative = md_translated.relative_to(lang_dir)
                except ValueError:
                    logger.warning(
                        f"Cannot compute relative path for {md_translated}, skipping."
                    )
                    continue

                if relative not in allowed_markdown:
                    continue

                original_md_path = (root_path / relative).resolve()

                # Analyze .ipynb links within root for this file
                actionable_links = []

                for link_info in markdown_link_destinations(content):
                    if link_info.kind not in {"link", "reference"}:
                        continue
                    link = link_info.destination
                    # Normalize possible angle-bracketed URL and strip markdown title
                    raw = link.strip()
                    if raw.startswith("<") and ">" in raw:
                        raw = raw[1 : raw.index(">")]
                    # Drop optional title: (url "title") or (url 'title')
                    if '"' in raw or "'" in raw:
                        raw = raw.split()[0]
                    parsed = urlparse(raw)
                    if parsed.scheme in ("mailto", "http", "https") or "@" in link:
                        continue
                    path = parsed.path
                    if not any(
                        path.lower().endswith(ext)
                        for ext in SUPPORTED_NOTEBOOK_EXTENSIONS
                    ):
                        continue
                    # Resolve absolute path of the linked notebook
                    if path.startswith("/"):
                        linked_abs = (root_path / path.lstrip("/")).resolve()
                    else:
                        linked_abs = (original_md_path.parent / path).resolve()
                        try:
                            _ = linked_abs.relative_to(root_path)
                        except ValueError:
                            # Try resolving relative to translated markdown directory, then map back to root
                            translated_md_dir = (
                                translations_dir
                                / lang
                                / original_md_path.relative_to(root_path).parent
                            )
                            alt_abs = (translated_md_dir / path).resolve()
                            try:
                                rel_to_lang = alt_abs.relative_to(
                                    translations_dir / lang
                                )
                                linked_abs = (root_path / rel_to_lang).resolve()
                                _ = linked_abs.relative_to(root_path)
                            except Exception:
                                # If not under translations/<lang>, but under root, accept as-is
                                try:
                                    _ = alt_abs.relative_to(root_path)
                                    linked_abs = alt_abs
                                except Exception:
                                    continue  # still outside root

                    # Determine translated counterpart if exists
                    candidate_translated = map_original_to_translated(
                        original_abs=linked_abs,
                        language_code=lang_dir.name,
                        root_dir=root_path,
                        translations_dir=translations_dir,
                    )

                    actionable_links.append((link, linked_abs, candidate_translated))

                if not actionable_links:
                    logger.debug(f"No actionable .ipynb links in {md_translated}")
                    continue  # no in-root .ipynb links -> not a candidate

                # This file is a candidate
                total_matched += 1

                # Compute translated_md_dir for later comparisons
                translated_md_dir = (
                    translations_dir
                    / lang_dir.name
                    / original_md_path.relative_to(root_path).parent
                )

                needs_update = False
                all_missing = True

                for (
                    link,
                    linked_abs,
                    candidate_translated,
                ) in actionable_links:
                    if (
                        candidate_translated is None
                        or not candidate_translated.exists()
                    ):
                        continue

                    all_missing = False
                    # Build expected updated link relative to translated_md_dir
                    expected_link = os.path.relpath(
                        candidate_translated, translated_md_dir
                    ).replace(os.path.sep, "/")
                    parsed_link = urlparse(link)
                    if parsed_link.query:
                        expected_link += f"?{parsed_link.query}"
                    if parsed_link.fragment:
                        expected_link += f"#{parsed_link.fragment}"

                    if link != expected_link:
                        needs_update = True

                if needs_update:
                    total_candidates_updatable += 1
                    logger.debug(f"[Candidate-UPDATE] {md_translated}")
                elif all_missing:
                    total_candidates_missing += 1
                    logger.debug(f"[Candidate-MISSING] {md_translated}")
                else:
                    total_candidates_already += 1
                    logger.debug(f"[Candidate-ALREADY] {md_translated}")

                if fallback_to_original:
                    updated = update_notebook_links(
                        markdown_string=content,
                        md_file_path=original_md_path,
                        language_code=lang_dir.name,
                        translations_dir=translations_dir,
                        root_dir=root_path,
                        use_translated_notebook=True,
                    )
                else:
                    updated = migrate_notebook_links(
                        markdown_string=content,
                        md_file_path=original_md_path,
                        language_code=lang_dir.name,
                        root_dir=root_path,
                        translations_dir=translations_dir,
                    )

                if updated != content:
                    total_changed += 1
                    if dry_run:
                        reporter.info(f"[DRY-RUN] Would update: {md_translated}")
                    else:
                        try:
                            md_translated.write_text(updated, encoding="utf-8")
                            logger.info(f"Updated links in: {md_translated}")
                        except Exception as e:
                            logger.error(f"Failed to write {md_translated}: {e}")

        # Summary (concise by default; detailed when --debug)
        if debug:
            reporter.key_value_summary(
                title="Link Migration Summary",
                rows=[
                    ("Scanned", str(total_scanned)),
                    ("Candidates", str(total_matched)),
                    ("Updatable", str(total_candidates_updatable)),
                    ("Already current", str(total_candidates_already)),
                    ("Missing target", str(total_candidates_missing)),
                    ("Changed", str(total_changed)),
                ],
                fallback_lines=[
                    f"Scanned: {total_scanned}, Candidates: {total_matched} "
                    f"(updatable: {total_candidates_updatable}, already: {total_candidates_already}, missing: {total_candidates_missing}), "
                    f"Changed: {total_changed}"
                ],
            )
        else:
            reporter.key_value_summary(
                title="Link Migration Summary",
                rows=[
                    ("Scanned", str(total_scanned)),
                    ("Candidates", str(total_matched)),
                    ("Changed", str(total_changed)),
                ],
                fallback_lines=[
                    f"Scanned: {total_scanned}, Candidates: {total_matched}, Changed: {total_changed}"
                ],
            )

    except click.ClickException:
        raise
    except Exception as e:
        if debug:
            logger.exception("Error during migrate-links")
        raise CliExitError(str(e), EXIT_FATAL) from e


if __name__ == "__main__":
    migrate_links_command()
