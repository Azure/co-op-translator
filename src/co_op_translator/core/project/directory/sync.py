from __future__ import annotations

import logging

from co_op_translator.config.constants import (
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)

logger = logging.getLogger(__name__)


class DirectorySyncMixin:
    def sync_directory_structure(
        self, markdown: bool = True, images: bool = True, notebooks: bool = True
    ) -> tuple[int, int, int]:
        """
        Synchronize the directory structure of translations with the original structure.

        Process:
        1. Scan original directory structure
        2. For each language:
           - Create missing directories that exist in original
           - Remove directories that don't exist in original

        Args:
            markdown: Whether to sync markdown directories
            images: Whether to sync image directories

        Returns:
            Tuple containing counts of created directories, removed directories,
            and number of languages synchronized
        """
        created_count = 0
        removed_count = 0

        # Get original directory structure (excluding files)
        original_dirs = set()
        for path in self.root_dir.rglob("*"):
            if path.is_dir() and not any(
                excluded in str(path) for excluded in self.excluded_dirs
            ):
                # Determine if this dir contains relevant file types per flags
                has_md = any(
                    any(path.glob(f"*{ext}")) for ext in SUPPORTED_MARKDOWN_EXTENSIONS
                )
                has_img = any(path.glob("*.png")) or any(path.glob("*.jpg"))
                has_nb = any(
                    any(path.glob(f"*{ext}")) for ext in SUPPORTED_NOTEBOOK_EXTENSIONS
                )

                if not (
                    (markdown and has_md)
                    or (images and has_img)
                    or (notebooks and has_nb)
                ):
                    continue

                # Store relative path for comparison
                original_dirs.add(path.relative_to(self.root_dir))

        # Sync each language directory
        for lang_code in self.language_codes:
            lang_dir = self._get_language_root(lang_code)
            if not lang_dir.exists():
                lang_dir.mkdir(parents=True)
                logger.info(f"Created language directory: {lang_dir}")

            # Get existing translation directories
            translation_dirs = set()
            if lang_dir.exists():
                for path in lang_dir.rglob("*"):
                    if path.is_dir():
                        try:
                            translation_dirs.add(path.relative_to(lang_dir))
                        except ValueError:
                            continue

            # Create missing directories
            for orig_dir in original_dirs:
                target_dir = lang_dir / orig_dir
                if not target_dir.exists():
                    target_dir.mkdir(parents=True, exist_ok=True)
                    created_count += 1
                    logger.info(f"Created directory: {target_dir}")

            # Remove extra directories that don't exist in original
            for trans_dir in sorted(
                translation_dirs, reverse=True
            ):  # Sort reverse to handle deep paths first
                if trans_dir not in original_dirs:
                    target_dir = lang_dir / trans_dir
                    try:
                        # Only remove if empty or contains no relevant files
                        has_relevant_files = False
                        if markdown and any(
                            any(target_dir.rglob(f"*{ext}"))
                            for ext in SUPPORTED_MARKDOWN_EXTENSIONS
                        ):
                            has_relevant_files = True
                        if images and (
                            any(target_dir.rglob("*.png"))
                            or any(target_dir.rglob("*.jpg"))
                        ):
                            has_relevant_files = True
                        if notebooks and any(
                            any(target_dir.rglob(f"*{ext}"))
                            for ext in SUPPORTED_NOTEBOOK_EXTENSIONS
                        ):
                            has_relevant_files = True

                        if not has_relevant_files:
                            target_dir.rmdir()  # This will only remove empty directories
                            removed_count += 1
                            logger.info(f"Removed empty directory: {target_dir}")
                        else:
                            logger.info(f"Skipping non-empty directory: {target_dir}")
                    except OSError as e:
                        logger.warning(f"Could not remove directory {target_dir}: {e}")

        return created_count, removed_count, len(self.language_codes)
