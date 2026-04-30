from __future__ import annotations

import logging
from pathlib import Path
from typing import List

from tqdm import tqdm

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.metadata_utils import (
    extract_content_without_metadata,
    extract_metadata_from_content,
    read_text_metadata_for_source,
    remove_image_metadata,
    save_text_metadata_for_source,
)
from co_op_translator.utils.llm.markdown_utils import update_image_links

logger = logging.getLogger(__name__)


class TranslationMaintenanceMixin:
    async def retranslate_outdated_files(
        self, outdated_files: List[tuple[Path, Path]]
    ) -> None:
        """Translate files identified as outdated or requiring updates.

        Extracts language codes from translation file paths and re-processes files.

        Args:
            outdated_files: List of (original_file, translation_file) tuples to retranslate
        """
        if not outdated_files:
            return

        files_to_translate = []
        for original_file, translation_file in outdated_files:
            try:
                relative_path = translation_file.relative_to(self.translations_dir)
                lang_code = relative_path.parts[0]

                if lang_code not in self.language_codes:
                    logger.warning(
                        f"Unknown language code in path: {lang_code}, skipping {translation_file}"
                    )
                    continue

                files_to_translate.append((original_file, lang_code))
            except (ValueError, IndexError) as e:
                logger.error(
                    f"Failed to extract language code from {translation_file}: {e}"
                )
                continue

        # Split into notebook and markdown tasks for clearer progress reporting
        notebook_items = [
            (original_file, language_code)
            for original_file, language_code in files_to_translate
            if original_file.suffix.lower() in self.supported_notebook_extensions
        ]
        markdown_items = [
            (original_file, language_code)
            for original_file, language_code in files_to_translate
            if original_file.suffix.lower() in SUPPORTED_MARKDOWN_EXTENSIONS
        ]

        # Notebooks
        if notebook_items:
            with tqdm(
                total=len(notebook_items), desc="📓 Retranslating outdated notebooks"
            ) as progress_bar:
                for original_file, language_code in notebook_items:
                    await self.translate_notebook(original_file, language_code)
                    progress_bar.update(1)
                    progress_bar.set_postfix_str(f"Current: {original_file.name}")

        # Markdown files
        if markdown_items:
            with tqdm(
                total=len(markdown_items), desc="📝 Retranslating outdated markdowns"
            ) as progress_bar:
                for original_file, language_code in markdown_items:
                    await self.translate_markdown(original_file, language_code)
                    progress_bar.update(1)
                    progress_bar.set_postfix_str(f"Current: {original_file.name}")

    async def retranslate_outdated_images(
        self, outdated_images: List[tuple[Path, Path, str]], fast_mode: bool = False
    ) -> None:
        """Retranslate images identified as outdated.

        Args:
            outdated_images: List of (original_file, translated_file, language_code) tuples
            fast_mode: Whether to use faster translation method
        """
        if not outdated_images:
            return

        with tqdm(
            total=len(outdated_images), desc="🖼️  Retranslating outdated images"
        ) as progress_bar:
            for original_file, translated_file, language_code in outdated_images:
                # Delete the outdated translated file and remove from central metadata
                try:
                    translated_file.unlink()
                    remove_image_metadata(translated_file, self.image_dir)
                except Exception as e:
                    logger.warning(
                        f"Failed to delete outdated image {translated_file}: {e}"
                    )

                # Retranslate
                await self.translate_image(
                    original_file, language_code, fast_mode=fast_mode
                )
                progress_bar.update(1)
                progress_bar.set_postfix_str(f"Current: {original_file.name}")

    async def fix_incorrect_image_paths(self):
        """Scan all translated markdown files and fix incorrect relative image paths.

        This identifies and corrects paths with excessive '../' segments that were
        previously generated incorrectly.
        """
        logger.info("Checking for incorrect image paths in existing translations...")
        fixed_count = 0
        translations_dir = self.translations_dir

        for lang_code in self.language_codes:
            lang_dir = translations_dir / lang_code
            if not lang_dir.exists():
                continue

            md_files = []
            for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                md_files.extend(list(lang_dir.rglob(f"*{ext}")))

            if not md_files:
                continue

            for md_translated in md_files:
                try:
                    content = md_translated.read_text(encoding="utf-8")
                    # Derive original md path to correctly resolve relative links
                    rel_to_lang = md_translated.relative_to(lang_dir)
                    original_md_path = (self.root_dir / rel_to_lang).resolve()

                    # Use module-level update_image_links with resolved paths to get correct links
                    updated = update_image_links(
                        content,
                        original_md_path,
                        lang_code,
                        translations_dir=self.translations_dir,
                        translated_images_dir=self.image_dir,
                        root_dir=self.root_dir,
                        use_translated_images=True,
                    )

                    if updated != content:
                        md_translated.write_text(updated, encoding="utf-8")
                        fixed_count += 1
                        logger.debug(f"Fixed image paths in: {md_translated}")
                except Exception as e:
                    logger.error(f"Failed to fix paths in {md_translated}: {e}")

        if fixed_count > 0:
            logger.info(f"Successfully fixed image paths in {fixed_count} files.")
        else:
            logger.info("No incorrect image paths found.")

        return fixed_count

    def _migrate_legacy_inline_text_metadata(self) -> int:
        migrated = 0

        for lang_code in self.language_codes:
            lang_dir = self.translations_dir / lang_code
            if not lang_dir.exists():
                continue

            md_files: list[Path] = []
            for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                md_files.extend(list(lang_dir.rglob(f"*{ext}")))

            for trans_file in md_files:
                try:
                    rel_to_lang = trans_file.relative_to(lang_dir)
                    original_file = (self.root_dir / rel_to_lang).resolve()
                    if not original_file.exists():
                        continue

                    source_key: str | Path
                    try:
                        source_key = str(
                            original_file.relative_to(self.root_dir)
                        ).replace("\\", "/")
                    except Exception:
                        source_key = original_file
                    existing = read_text_metadata_for_source(lang_dir, source_key)
                    if isinstance(existing, dict) and existing.get("original_hash"):
                        continue

                    content = trans_file.read_text(encoding="utf-8")
                    legacy_meta = extract_metadata_from_content(content)
                    legacy_hash = (
                        legacy_meta.get("original_hash")
                        if isinstance(legacy_meta, dict)
                        else None
                    )
                    if not legacy_hash:
                        # If there is no legacy inline metadata, do not synthesize
                        # a fresh metadata record from the current source hash.
                        # Doing so would incorrectly mark unknown/manual translations
                        # as up-to-date and skip retranslation.
                        continue

                    extra_fields = {"original_hash": legacy_hash}
                    if isinstance(legacy_meta, dict) and legacy_meta.get(
                        "translation_date"
                    ):
                        extra_fields["translation_date"] = legacy_meta.get(
                            "translation_date"
                        )

                    save_text_metadata_for_source(
                        lang_dir,
                        original_file,
                        lang_code,
                        root_dir=self.root_dir,
                        extra_fields=extra_fields,
                    )

                    cleaned = extract_content_without_metadata(content)
                    if cleaned != content:
                        try:
                            trans_file.write_text(cleaned, encoding="utf-8")
                        except Exception:
                            pass

                    migrated += 1
                except Exception:
                    continue

        return migrated
