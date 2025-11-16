"""
Migrate-links command: reprocess translated markdowns that contain .ipynb links
to update them to translated notebooks when available (and keep originals otherwise).

This performs link-only processing using utils.llm.markdown_utils.update_links(),
so there are no LLM calls and it's fast and idempotent.
"""

import logging
from pathlib import Path
import click
import os
import re
from urllib.parse import urlparse
from tqdm import tqdm
import importlib.resources
import yaml

from co_op_translator.config.base_config import Config
from co_op_translator.utils.llm.markdown_utils import (
    migrate_notebook_links,
    update_notebook_links,
)
from co_op_translator.utils.common.file_utils import map_original_to_translated
from co_op_translator.utils.common.logging_utils import setup_logging

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
    "-r",
    default=".",
    help="Root directory of the project (default is current directory).",
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
    "-y",
    is_flag=True,
    help="Automatically confirm prompts (useful when using -l 'all').",
)
def migrate_links_command(
    language_codes,
    root_dir,
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
    try:
        # Validate root directory and config
        Config.check_configuration()

        root_path = Path(root_dir).resolve()
        if not root_path.exists() or not root_path.is_dir():
            raise click.ClickException(f"Invalid root directory: {root_dir}")

        log_file_path = setup_logging(
            root_path, debug=debug, save_logs=save_logs, command_name="migrate-links"
        )
        if debug:
            logging.debug("Debug mode enabled.")
        if save_logs and log_file_path is not None:
            click.echo(f"📄 Logs will be saved to: {log_file_path}")

        translations_dir = root_path / "translations"

        if not translations_dir.exists():
            click.echo(f"No translations directory found at: {translations_dir}")
            return

        # Warning and confirmation when processing all languages
        if isinstance(language_codes, str) and language_codes.lower() == "all":
            click.echo(
                "Warning: Processing 'all' languages can take significant time on large projects."
            )
            click.echo(
                "For efficiency, contributors usually handle individual languages separately."
            )
            if not yes:
                confirmation_all = click.prompt(
                    "Do you still want to proceed with ALL languages? Type 'yes' to continue",
                    type=str,
                )
                if confirmation_all.lower() != "yes":
                    click.echo("Operation for 'all' languages cancelled.")
                    return
                else:
                    click.echo("Proceeding with operation for all languages...")
            else:
                click.echo("Auto-confirming operation for all languages...")

        # Parse language codes list (support "all")
        if isinstance(language_codes, str) and language_codes.lower() == "all":
            try:
                with importlib.resources.path(
                    "co_op_translator.fonts", "font_language_mappings.yml"
                ) as mappings_path:
                    with open(mappings_path, "r", encoding="utf-8") as file:
                        font_mappings = yaml.safe_load(file)
                        if not font_mappings:
                            raise click.ClickException("Empty font mappings file")
                        lang_list = [
                            lang_code
                            for lang_code in font_mappings
                            if isinstance(font_mappings[lang_code], dict)
                        ]
                        if not lang_list:
                            raise click.ClickException(
                                "No valid language codes found in font mappings"
                            )
                        logging.debug(
                            f"Expanded 'all' to language codes from font mapping: {lang_list}"
                        )
            except (FileNotFoundError, yaml.YAMLError) as e:
                raise click.ClickException(
                    f"Failed to load language codes for 'all': {str(e)}"
                )
        else:
            lang_list = [
                code.strip() for code in language_codes.split() if code.strip()
            ]
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
            md_files = list(lang_dir.rglob("*.md"))
            for md_translated in tqdm(md_files, desc=f"{lang} md", unit="file"):
                total_scanned += 1
                try:
                    content = md_translated.read_text(encoding="utf-8")
                except Exception:
                    logger.warning(f"Failed to read: {md_translated}")
                    continue

                # Quick filter: only process files containing .ipynb links
                if ".ipynb" not in content:
                    continue

                # Derive original md path from translated path (needed to resolve links)
                try:
                    relative = md_translated.relative_to(lang_dir)
                except ValueError:
                    logger.warning(
                        f"Cannot compute relative path for {md_translated}, skipping."
                    )
                    continue

                original_md_path = (root_path / relative).resolve()

                # Analyze .ipynb links within root for this file
                actionable_links = []
                already_translated = (
                    True  # assume already translated until proven otherwise
                )
                missing_translation = True  # assume missing until we find at least one translated counterpart

                for alt_text, link in re.findall(r"\[(.*?)\]\((.*?)\)", content):
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
                    if not path.lower().endswith(".ipynb"):
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
                        language_code=lang,
                        root_dir=root_path,
                    )

                    actionable_links.append(
                        (alt_text, link, linked_abs, candidate_translated)
                    )

                if not actionable_links:
                    logger.debug(f"No actionable .ipynb links in {md_translated}")
                    continue  # no in-root .ipynb links -> not a candidate

                # This file is a candidate
                total_matched += 1

                # Compute translated_md_dir for later comparisons
                translated_md_dir = (
                    translations_dir
                    / lang
                    / original_md_path.relative_to(root_path).parent
                )

                needs_update = False
                all_missing = True

                for (
                    alt_text,
                    link,
                    linked_abs,
                    candidate_translated,
                ) in actionable_links:
                    if (
                        candidate_translated is None
                        or not candidate_translated.exists()
                    ):
                        # There is at least one link without translated counterpart
                        already_translated = False
                        continue

                    all_missing = False
                    # Build expected updated link relative to translated_md_dir
                    expected_link = os.path.relpath(
                        candidate_translated, translated_md_dir
                    ).replace(os.path.sep, "/")
                    if parsed := urlparse(link):
                        # preserve existing query/fragment when comparing
                        if parsed.query:
                            expected_link += f"?{parsed.query}"
                        if parsed.fragment:
                            expected_link += f"#{parsed.fragment}"

                    if link != expected_link:
                        needs_update = True
                        already_translated = False

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
                        language_code=lang,
                        translations_dir=translations_dir,
                        root_dir=root_path,
                        use_translated_notebook=True,
                    )
                else:
                    updated = migrate_notebook_links(
                        markdown_string=content,
                        md_file_path=original_md_path,
                        language_code=lang,
                        root_dir=root_path,
                    )

                if updated != content:
                    total_changed += 1
                    if dry_run:
                        click.echo(f"[DRY-RUN] Would update: {md_translated}")
                    else:
                        try:
                            md_translated.write_text(updated, encoding="utf-8")
                            logger.info(f"Updated links in: {md_translated}")
                        except Exception as e:
                            logger.error(f"Failed to write {md_translated}: {e}")

        # Summary (concise by default; detailed when --debug)
        if debug:
            click.echo(
                (
                    f"Scanned: {total_scanned}, Candidates: {total_matched} "
                    f"(updatable: {total_candidates_updatable}, already: {total_candidates_already}, missing: {total_candidates_missing}), "
                    f"Changed: {total_changed}"
                )
            )
        else:
            click.echo(
                f"Scanned: {total_scanned}, Candidates: {total_matched}, Changed: {total_changed}"
            )

    except Exception as e:
        if debug:
            logger.exception("Error during migrate-links")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    migrate_links_command()
