from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from co_op_translator.utils.common.lang_utils import ALIAS_TO_BCP47

logger = logging.getLogger(__name__)


@dataclass
class MigrationEntry:
    base_dir: Path
    source_dir: Path
    dest_dir: Path
    alias: str
    canonical: str
    conflict: bool = False


class LanguageFolderMigrator:
    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
    ):
        self.root_dir = Path(root_dir)
        self.translations_dir = (
            (self.root_dir / "translations")
            if translations_dir is None
            else Path(translations_dir)
        )
        self.image_dir = (
            (self.root_dir / "translated_images")
            if image_dir is None
            else Path(image_dir)
        )
        self.image_fast_dir = self.root_dir / "translated_images_fast"
        self._aliases = set(ALIAS_TO_BCP47.keys())

    def detect_alias_folders(self) -> List[MigrationEntry]:
        entries: List[MigrationEntry] = []
        for base in [self.translations_dir, self.image_dir, self.image_fast_dir]:
            if not base.exists() or not base.is_dir():
                continue
            try:
                for child in base.iterdir():
                    if not child.is_dir():
                        continue
                    alias = child.name
                    if alias in self._aliases:
                        canonical = ALIAS_TO_BCP47[alias]
                        dest = base / canonical
                        conflict = dest.exists() and any(dest.iterdir())
                        entries.append(
                            MigrationEntry(
                                base_dir=base,
                                source_dir=child,
                                dest_dir=dest,
                                alias=alias,
                                canonical=canonical,
                                conflict=conflict,
                            )
                        )
            except Exception as e:
                logger.debug(f"Failed scanning {base}: {e}")
        return entries

    @staticmethod
    def format_plan(entries: List[MigrationEntry]) -> str:
        if not entries:
            return "No non-standard language folders detected."
        lines: List[str] = ["Detected non-standard language folders:"]
        for e in entries:
            status = "(conflict)" if e.conflict else ""
            lines.append(
                f"- {e.source_dir.relative_to(e.base_dir)} -> {e.dest_dir.relative_to(e.base_dir)} {status}"
            )
        return "\n".join(lines)

    def _fs_rename(self, src: Path, dst: Path) -> Tuple[bool, str]:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
            return True, ""
        except Exception as e:
            return False, str(e)

    def _rewrite_lang_metadata(self, lang_dir: Path, canonical_code: str) -> None:
        """Ensure per-language metadata under lang_dir stores canonical language_code.

        Delegates to normalize_language_codes_in_lang_metadata to avoid duplication.
        """
        try:
            from co_op_translator.utils.common.metadata_utils import (
                normalize_language_codes_in_lang_metadata,
            )

            normalize_language_codes_in_lang_metadata(lang_dir, canonical_code)
        except Exception:
            # Non-fatal if metadata normalization fails
            pass

    def execute(
        self,
        entries: List[MigrationEntry],
        use_git: bool | None = None,
        dry_run: bool = False,
    ) -> Tuple[int, List[str]]:
        """Execute migration entries. Skips conflicting destinations.

        Returns number of successful renames and a list of messages for errors or conflicts.

        Note: `use_git` is currently ignored and preserved only for backward compatibility.
        """
        if not entries:
            return 0, []

        msgs: List[str] = []
        successes = 0
        for e in entries:
            if e.conflict:
                msgs.append(
                    f"Conflict: '{e.dest_dir}' already exists. Skipping auto-merge for '{e.source_dir}'."
                )
                continue
            if dry_run:
                # No changes, preview only
                continue
            ok, err = self._fs_rename(e.source_dir, e.dest_dir)
            if ok:
                successes += 1
                # After successful rename, rewrite metadata to canonical code
                try:
                    self._rewrite_lang_metadata(e.dest_dir, e.canonical)
                except Exception:
                    # Non-fatal if metadata rewrite fails
                    pass
            else:
                msgs.append(
                    f"Failed to rename '{e.source_dir}' -> '{e.dest_dir}': {err}"
                )
        return successes, msgs
