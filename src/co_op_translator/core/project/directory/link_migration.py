from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from co_op_translator.config.constants import (
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.common.file_utils import HASH_PREFIX_LENGTH

logger = logging.getLogger(__name__)


class DirectoryLinkMigrationMixin:
    def migrate_markdown_image_links(self, rename_map: dict[str, str]) -> int:
        """Update translated markdown files to use new image basenames.

        The rename_map keys and values are basenames (no directory component).
        This helper scans all translated markdown files and replaces any
        occurrences of old basenames with the corresponding new basenames.
        """

        # Proceed even if rename_map is empty to apply regex-based rewrites

        updated_files = 0

        try:
            md_files: list[Path] = []
            for lang_code in self.language_codes:
                lang_dir = self.translations_dir / lang_code
                if not lang_dir.exists():
                    continue
                for path in lang_dir.rglob("*"):
                    if (
                        path.is_file()
                        and path.suffix.lower() in SUPPORTED_MARKDOWN_EXTENSIONS
                    ):
                        md_files.append(path)
        except Exception as e:
            logger.warning(
                f"Error scanning markdown files for migration in {self.translations_dir}: {e}"
            )
            return 0

        for md_file in md_files:
            try:
                original_content = md_file.read_text(encoding="utf-8")
            except Exception as e:
                logger.warning(f"Error reading markdown file {md_file}: {e}")
                continue

            migrated_content = original_content
            for old_name, new_name in rename_map.items():
                if old_name in migrated_content:
                    migrated_content = migrated_content.replace(old_name, new_name)

            # Additionally, rewrite legacy flattened image links to folder-based structure via regex
            # Pattern matches: [../]*/<base_dir>/<basename>.<hash>.<lang>.<ext>
            base_dir_name = self.image_dir.name
            pattern = re.compile(
                rf"(?P<prefix>(?:\.\./)*/?)?"
                rf"(?P<bdir>{re.escape(base_dir_name)}|translated_images|translated_images_fast)"
                rf"/"
                rf"(?P<basename>[^/]+?)\.(?P<hash>[0-9a-fA-F]{{16,64}})\.(?P<lang>[a-z]{{2}})(?P<ext>\.(?:png|jpg|jpeg|gif))"
            )

            def _rewrite_legacy(m: re.Match) -> str:
                prefix = m.group("prefix") or ""
                lang = m.group("lang")
                basename = m.group("basename")
                hashseg = m.group("hash")
                ext = m.group("ext")
                # Normalize to configured base dir name and folder-based path
                return f"{prefix}{base_dir_name}/{lang}/{basename}.{hashseg}{ext}"

            migrated_content = pattern.sub(_rewrite_legacy, migrated_content)

            migrated_content = self._rewrite_existing_webp_links(migrated_content)

            if migrated_content != original_content:
                try:
                    md_file.write_text(migrated_content, encoding="utf-8")
                    updated_files += 1
                except Exception as e:
                    logger.warning(
                        f"Error writing migrated markdown file {md_file}: {e}"
                    )

        return updated_files

    def _rewrite_existing_webp_links(self, text: str) -> str:
        """Replace .png/.jpg/.jpeg translated_images links with .webp when available."""

        if not self.image_dir.exists():
            return text

        base_dir_name = self.image_dir.name
        pattern = re.compile(
            rf"(?P<prefix>(?:\.\./)*/?)?"
            rf"(?P<bdir>{re.escape(base_dir_name)}|translated_images|translated_images_fast)"
            rf"/(?P<lang>[A-Za-z0-9-]+)/"
            rf"(?P<basename>[^/]+?)\.(?P<hash>[0-9a-fA-F]{{16,64}})(?P<ext>\.(?:png|jpg|jpeg))"
        )

        def _rewrite_existing(m: re.Match) -> str:
            ext = m.group("ext").lower()
            if ext == ".webp":
                return m.group(0)

            lang = m.group("lang")
            basename = m.group("basename")
            hashseg = m.group("hash")
            prefix = m.group("prefix") or ""

            candidate_hash = (
                hashseg[:HASH_PREFIX_LENGTH]
                if len(hashseg) > HASH_PREFIX_LENGTH
                else hashseg
            )
            candidate_rel = Path(lang) / f"{basename}.{candidate_hash}.webp"
            candidate_path = self.image_dir / candidate_rel

            if candidate_path.exists():
                return (
                    f"{prefix}{base_dir_name}/{lang}/{basename}.{candidate_hash}.webp"
                )

            return m.group(0)

        return pattern.sub(_rewrite_existing, text)

    def migrate_notebook_image_links(self, rename_map: dict[str, str]) -> int:
        # Proceed even if rename_map is empty to apply regex-based rewrites

        updated_files = 0

        try:
            nb_files: list[Path] = []
            for lang_code in self.language_codes:
                lang_dir = self.translations_dir / lang_code
                if not lang_dir.exists():
                    continue
                for path in lang_dir.rglob("*"):
                    if (
                        path.is_file()
                        and path.suffix.lower() in SUPPORTED_NOTEBOOK_EXTENSIONS
                    ):
                        nb_files.append(path)
        except Exception as e:
            logger.warning(
                f"Error scanning notebook files for migration in {self.translations_dir}: {e}"
            )
            return 0

        for nb_file in nb_files:
            try:
                with nb_file.open("r", encoding="utf-8") as f:
                    notebook = json.load(f)
            except Exception as e:
                logger.warning(f"Error reading notebook file {nb_file}: {e}")
                continue

            changed = False

            for cell in notebook.get("cells", []):
                if cell.get("cell_type") != "markdown":
                    continue

                source = cell.get("source", [])
                if isinstance(source, list):
                    original_text = "".join(source)
                else:
                    original_text = str(source)

                migrated_text = original_text
                for old_name, new_name in rename_map.items():
                    if old_name in migrated_text:
                        migrated_text = migrated_text.replace(old_name, new_name)

                # Regex-based rewrite for legacy flattened image links in notebook markdown cells
                base_dir_name = self.image_dir.name
                pattern = re.compile(
                    rf"(?P<prefix>(?:\.\./)*/?)?"
                    rf"(?P<bdir>{re.escape(base_dir_name)}|translated_images|translated_images_fast)"
                    rf"/"
                    rf"(?P<basename>[^/]+?)\.(?P<hash>[0-9a-fA-F]{{16,64}})\.(?P<lang>[a-z]{{2}})(?P<ext>\.(?:png|jpg|jpeg|gif))"
                )

                def _rewrite_legacy_nb(m: re.Match) -> str:
                    prefix = m.group("prefix") or ""
                    lang = m.group("lang")
                    basename = m.group("basename")
                    hashseg = m.group("hash")
                    ext = m.group("ext")
                    return f"{prefix}{base_dir_name}/{lang}/{basename}.{hashseg}{ext}"

                migrated_text = pattern.sub(_rewrite_legacy_nb, migrated_text)

                migrated_text = self._rewrite_existing_webp_links(migrated_text)

                if migrated_text != original_text:
                    changed = True
                    if isinstance(source, list):
                        lines = migrated_text.splitlines(keepends=True)
                        lines = [
                            line if line.endswith("\n") else line + "\n"
                            for line in lines
                        ]
                        cell["source"] = lines
                    else:
                        cell["source"] = migrated_text

            if changed:
                try:
                    with nb_file.open("w", encoding="utf-8") as f:
                        json.dump(notebook, f, ensure_ascii=False, indent=1)
                    updated_files += 1
                except Exception as e:
                    logger.warning(
                        f"Error writing migrated notebook file {nb_file}: {e}"
                    )

        return updated_files
