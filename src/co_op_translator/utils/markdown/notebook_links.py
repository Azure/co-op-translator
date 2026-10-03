from __future__ import annotations

import logging
import os
from pathlib import Path
from urllib.parse import urlparse

from co_op_translator.config.constants import SUPPORTED_NOTEBOOK_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    get_filename_and_extension,
    map_original_to_translated,
)
from co_op_translator.utils.markdown.link_placeholders import (
    MarkdownLinkDestination,
    rewrite_markdown_link_destinations,
)

logger = logging.getLogger(__name__)


def migrate_notebook_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    root_dir: Path,
    translations_dir: Path | None = None,
) -> str:
    """
    Migration-only notebook link updater.

    - Targets only links to .ipynb files in markdown content.
    - If a translated notebook exists under translations/<lang>/, rewrite link
      to the translated notebook relative to the translated markdown location.
    - If not, leave the original link as-is (no normalization or fallback rewrite).
    - Preserves query strings and fragments.
    - Skips web/email links.
    """
    translations_dir = (translations_dir or root_dir / "translations").resolve()

    def _rewrite(link_info: MarkdownLinkDestination) -> str | None:
        if link_info.kind not in {"link", "reference"}:
            return None
        link = link_info.destination
        parsed = urlparse(link)
        # Skip web/email links
        if (
            parsed.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.debug(f"Skipping web/email link: {link}")
            return None

        path = parsed.path
        _, ext = get_filename_and_extension(path)
        if ext.lower() not in SUPPORTED_NOTEBOOK_EXTENSIONS:
            logger.debug(f"Skipping non-notebook link: {link}")
            return None

        try:
            # Resolve absolute original linked notebook path
            if path.startswith("/"):
                original_linked_abs = (root_dir / path.lstrip("/")).resolve()
            else:
                original_linked_abs = (md_file_path.parent / path).resolve()
                # If outside root, try resolving relative to translated MD dir and map back to root
                try:
                    _ = original_linked_abs.relative_to(root_dir)
                except ValueError:
                    translated_md_dir = (
                        translations_dir
                        / language_code
                        / md_file_path.relative_to(root_dir).parent
                    )
                    alt_abs = (translated_md_dir / path).resolve()
                    try:
                        rel_to_lang = alt_abs.relative_to(
                            translations_dir / language_code
                        )
                        original_linked_abs = (root_dir / rel_to_lang).resolve()
                        _ = original_linked_abs.relative_to(root_dir)
                    except Exception:
                        # If not under translations/<lang>, but under root, accept as-is
                        try:
                            _ = alt_abs.relative_to(root_dir)
                            original_linked_abs = alt_abs
                        except Exception:
                            # Still not within root, skip this link
                            logger.debug(
                                f"Link outside root after alt resolution: {link}"
                            )
                            return None

            # Map to translated counterpart if it exists
            candidate_translated = map_original_to_translated(
                original_abs=original_linked_abs,
                language_code=language_code,
                root_dir=root_dir,
                translations_dir=translations_dir,
            )
            if not candidate_translated:
                logger.debug(
                    f"No translated notebook found for: {original_linked_abs} (lang={language_code})"
                )
                # No translated notebook -> leave link unchanged
                return None

            if not candidate_translated.exists():
                # No translated notebook -> leave link unchanged
                return None

            # Translated markdown directory (for relative link computation)
            translated_md_dir = (
                translations_dir
                / language_code
                / md_file_path.relative_to(root_dir).parent
            )

            # Build relative link from translated markdown dir to translated notebook
            updated_link = os.path.relpath(
                candidate_translated, translated_md_dir
            ).replace(os.path.sep, "/")

            # Preserve query/fragment
            if parsed.query:
                updated_link += f"?{parsed.query}"
            if parsed.fragment:
                updated_link += f"#{parsed.fragment}"

            if link == updated_link:
                logger.debug(f"Already correct, no change: {link}")
                return None
            logger.debug(f"Updated notebook link: {link} -> {updated_link}")
            return updated_link

        except Exception as e:
            logger.error(f"Error processing migration notebook link {link}: {e}")
            return None

    return rewrite_markdown_link_destinations(markdown_string, _rewrite)


def update_notebook_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
    use_translated_notebook: bool = True,
    target_path: Path | None = None,
) -> str:
    """
    Update links to .ipynb files in markdown content.

    If a translated notebook exists under translations/<lang>/, update the link to point to it.
    Otherwise (or if disabled), ensure the link correctly points to the original notebook
    from the translated markdown location. Preserves query strings and fragments.

    Args:
        markdown_string (str): The markdown content to process
        md_file_path (Path): Path to the markdown file being processed (original file path)
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations
        root_dir (Path): Root directory of the project
        use_translated_notebook (bool): Whether to use translated notebooks when available

    Returns:
        str: Updated markdown content with modified notebook links
    """

    def _rewrite(link_info: MarkdownLinkDestination) -> str | None:
        if link_info.kind not in {"link", "reference"}:
            return None
        link = link_info.destination
        parsed = urlparse(link)
        # Skip web/email links
        if (
            parsed.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.debug(f"Skipped {link} as it is an email or web URL")
            return None

        path = parsed.path
        _, ext = get_filename_and_extension(path)
        if ext.lower() not in SUPPORTED_NOTEBOOK_EXTENSIONS:
            # Only handle notebook links here
            return None

        try:
            # Determine directory of the translated markdown (target doc location)
            translated_md_dir = (
                Path(target_path).parent.resolve()
                if target_path is not None
                else (
                    translations_dir
                    / language_code
                    / md_file_path.relative_to(root_dir).parent
                )
            )

            # Resolve the original linked notebook absolute path
            if path.startswith("/"):
                original_linked_abs = (root_dir / path.lstrip("/")).resolve()
            else:
                original_linked_abs = (md_file_path.parent / path).resolve()
                # If outside root, try resolving relative to translated MD dir and map back to root
                try:
                    _ = original_linked_abs.relative_to(root_dir)
                except ValueError:
                    alt_abs = (translated_md_dir / path).resolve()
                    try:
                        rel_to_lang = alt_abs.relative_to(
                            translations_dir / language_code
                        )
                        original_linked_abs = (root_dir / rel_to_lang).resolve()
                        _ = original_linked_abs.relative_to(root_dir)
                    except Exception:
                        # If not under translations/<lang>, but under root, accept as-is
                        try:
                            _ = alt_abs.relative_to(root_dir)
                            original_linked_abs = alt_abs
                        except Exception:
                            logger.debug(
                                f"Link outside root after alt resolution: {link}"
                            )
                            return None

            # Compute the candidate translated notebook path
            original_rel_from_root = original_linked_abs.relative_to(root_dir)
            candidate_translated = (
                translations_dir / language_code / original_rel_from_root
            ).resolve()

            # Choose target (translated if available and enabled, else original)
            if use_translated_notebook and candidate_translated.exists():
                target_abs = candidate_translated
                logger.debug(
                    f"Using translated notebook link for {path} -> {candidate_translated}"
                )
            else:
                target_abs = original_linked_abs
                logger.debug(f"Using original notebook link for {path}")

            # Build relative link from translated markdown dir to target
            updated_link = os.path.relpath(target_abs, translated_md_dir).replace(
                os.path.sep, "/"
            )

            # Preserve query and fragment
            if parsed.query:
                updated_link += f"?{parsed.query}"
            if parsed.fragment:
                updated_link += f"#{parsed.fragment}"

            logger.debug(f"Updated notebook link: {link} -> {updated_link}")
            return updated_link

        except Exception as e:
            logger.error(f"Error processing notebook link {link}: {e}")
            return None

    return rewrite_markdown_link_destinations(markdown_string, _rewrite)
