from __future__ import annotations

import logging
from pathlib import Path
from typing import List

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    filter_files,
    generate_translated_filename,
    get_filename_and_extension,
)
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    extract_metadata_from_content,
    is_image_up_to_date,
    is_notebook_up_to_date,
    read_text_metadata_for_source,
)

logger = logging.getLogger(__name__)


def _resolve_language_root_for(manager, language_code: str) -> Path:
    """Resolve a language root for real or partially mocked managers."""
    try:
        lang_dir = manager._get_language_root(language_code)
        if isinstance(lang_dir, Path):
            return lang_dir
    except Exception:
        pass

    lang_dir = Path(manager.translations_dir) / language_code
    lang_subdir = getattr(manager, "lang_subdir", None)
    if isinstance(lang_subdir, (str, Path)) and str(lang_subdir):
        lang_dir = lang_dir / Path(lang_subdir)
    return lang_dir


class TranslationStatusMixin:
    async def check_outdated_files(self, update: bool = False) -> tuple[int, List[str]]:
        """Identify and update outdated translations (markdown + notebooks).

        Delegates detection to get_outdated_translations() which supports both
        markdown and notebook files, and then retranslates them via
        retranslate_outdated_files().

        Args:
            update: When True, treat all existing translation files as outdated and
                    retranslate them regardless of hash values.

        Returns:
            Tuple containing (number_of_files_scheduled_for_retranslation, error_messages_list)
        """
        errors: List[str] = []

        try:
            # Build list of files to retranslate
            if update:
                files: list[tuple[Path, Path]] = []
                for lang_code in self.language_codes:
                    translation_dir = self.translations_dir / lang_code
                    if not translation_dir.exists():
                        continue
                    trans_files: list[Path] = []
                    for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                        trans_files.extend(translation_dir.rglob(f"*{ext}"))
                    for ext in self.supported_notebook_extensions:
                        trans_files.extend(translation_dir.rglob(f"*{ext}"))

                    for trans_file in trans_files:
                        try:
                            rel = trans_file.relative_to(translation_dir)
                            original = self.root_dir / rel
                            if original.exists():
                                files.append((original, trans_file))
                        except Exception:
                            continue
                outdated_files = files
            else:
                # Ensure legacy inline metadata is migrated before outdated detection.
                try:
                    self._migrate_legacy_inline_text_metadata()
                except Exception as e:
                    logger.warning(f"Legacy text metadata migration skipped: {e}")
                outdated_files = self.get_outdated_translations()

            modified_count = len(outdated_files)

            if outdated_files:
                await self.retranslate_outdated_files(outdated_files)

            return modified_count, errors
        except Exception as e:
            logger.error(f"Failed to check outdated files: {e}")
            errors.append(str(e))
            return 0, errors

    def get_outdated_translations(self) -> List[tuple[Path, Path]]:
        """Identify translations that need updates based on file hash comparison.

        Scans all translation files and compares their metadata with source files.

        Returns:
            List of (original_file, translation_file) tuples that need updates
        """
        outdated_files = []
        all_translation_files = []

        for lang_code in self.language_codes:
            translation_dir = _resolve_language_root_for(self, lang_code)
            if not translation_dir.exists():
                continue
            for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                for md_file in translation_dir.rglob(f"*{ext}"):
                    all_translation_files.append((lang_code, md_file))
            for ext in self.supported_notebook_extensions:
                for nb_file in translation_dir.rglob(f"*{ext}"):
                    all_translation_files.append((lang_code, nb_file))

        if not all_translation_files:
            return []

        for lang_code, trans_file in all_translation_files:
            try:
                lang_dir = _resolve_language_root_for(self, lang_code)
                relative_path = trans_file.relative_to(lang_dir)
                original_file = self.root_dir / relative_path

                if not original_file.exists():
                    continue

                # Compare metadata
                if self._is_translation_outdated(original_file, trans_file):
                    outdated_files.append((original_file, trans_file))
            except ValueError:
                logger.warning(f"Error calculating relative path for {trans_file}")
                continue

        return outdated_files

    def _resolve_language_root(self, language_code: str) -> Path:
        """Return a concrete language root even for partially mocked managers in tests."""
        return _resolve_language_root_for(self, language_code)

    def get_outdated_images(self) -> List[tuple[Path, Path, str]]:
        """Identify translated images that need updates based on metadata hash comparison.

        Scans all translated image files and compares their metadata with source images.

        Returns:
            List of (original_file, translated_file, language_code) tuples that need updates
        """
        outdated_images = []

        # Discover original image files
        image_files = filter_files(self.root_dir, self.excluded_dirs)
        original_images = [
            f.resolve()
            for f in image_files
            if get_filename_and_extension(f)[1] in self.supported_image_extensions
        ]

        if not original_images:
            return []

        for image_file_path in original_images:
            for language_code in self.language_codes:
                translated_filename = generate_translated_filename(
                    image_file_path, language_code, self.root_dir
                )
                translated_image_path = (
                    Path(self.image_dir) / language_code / translated_filename
                )

                if not translated_image_path.exists():
                    # File doesn't exist - not outdated, just new (will be handled by translate_all)
                    continue

                # Check if the translation is outdated using metadata
                if not is_image_up_to_date(
                    image_file_path, translated_image_path, self.image_dir
                ):
                    outdated_images.append(
                        (image_file_path, translated_image_path, language_code)
                    )

        return outdated_images

    def _is_translation_outdated(
        self, original_file: Path, translation_file: Path
    ) -> bool:
        """Determine if a translation file needs updating based on content hash.

        Compares the hash of the original file with the hash stored in the translation
        file's metadata. Handles both markdown and notebook files.

        Args:
            original_file: Path to the original file
            translation_file: Path to the translation file

        Returns:
            True if translation needs updating, False if it's current
        """
        if not translation_file.exists():
            return True

        try:
            # Handle notebook files using dedicated helper (centralized JSON preferred inside helper)
            if translation_file.suffix.lower() in self.supported_notebook_extensions:
                return not is_notebook_up_to_date(original_file, translation_file)

            # Determine language directory and language code from translation path
            lang_dir = None
            lang_code = None
            try:
                # Find which language this file belongs to by checking roots
                for lc in self.language_codes:
                    root = self._get_language_root(lc)
                    try:
                        # Use resolve() to handle potential symlinks or relative path complexities
                        rel = translation_file.resolve().relative_to(root.resolve())
                        lang_code = lc
                        lang_dir = root
                        break
                    except (ValueError, IndexError):
                        continue

                if not lang_dir:
                    # Fallback to translations_dir / lang_code if not found in subdirs
                    rel = translation_file.resolve().relative_to(
                        self.translations_dir.resolve()
                    )
                    lang_code = rel.parts[0]
                    lang_dir = self.translations_dir / lang_code
            except Exception:
                # Fallback: use the parent directory (may be incorrect for deeply nested paths)
                lang_dir = translation_file.parent

            # Prefer centralized JSON metadata
            source_key: str | Path
            try:
                source_key = str(original_file.relative_to(self.root_dir)).replace(
                    "\\", "/"
                )
            except Exception:
                source_key = original_file
            metadata = read_text_metadata_for_source(lang_dir, source_key)
            if metadata and isinstance(metadata, dict):
                stored_hash = metadata.get("original_hash")
                if stored_hash:
                    current_hash = calculate_file_hash(original_file)
                    return stored_hash != current_hash

            # Legacy fallback: read inline HTML comment metadata and migrate
            try:
                content = translation_file.read_text(encoding="utf-8")
            except Exception:
                return True

            legacy_meta = extract_metadata_from_content(content)
            stored_hash = (
                legacy_meta.get("original_hash")
                if isinstance(legacy_meta, dict)
                else None
            )
            if stored_hash:
                # Read-only fallback: compare against inline stored hash.
                current_hash = calculate_file_hash(original_file)
                return stored_hash != current_hash

            # No metadata available; consider it outdated
            return True

        except Exception:
            return True
