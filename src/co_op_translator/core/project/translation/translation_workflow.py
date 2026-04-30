from __future__ import annotations

import logging
from pathlib import Path

from tqdm import tqdm

from co_op_translator.config.base_config import Config
from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.core.project.directory_manager import DirectoryManager
from co_op_translator.utils.common.file_utils import (
    canonicalize_image_links_in_translations,
    filter_files,
    migrate_images_to_webp,
    migrate_translated_image_filenames,
    read_input_file,
)
from co_op_translator.utils.common.metadata_utils import cleanup_orphan_image_metadata
from co_op_translator.utils.common.token_estimation import (
    estimate_tokens_for_outdated,
    estimate_tokens_for_sources,
)
from co_op_translator.utils.llm.markdown_utils import compare_line_breaks

logger = logging.getLogger(__name__)


class TranslationWorkflowMixin:
    async def translate_project_async(
        self,
        update: bool = False,
        fast_mode: bool = False,
    ) -> tuple[int, list[str]]:
        """Translate project files asynchronously following a structured workflow.

        The translation process follows these steps:
        1. Remove orphaned files
        2. Synchronize directory structure with source
        3. Identify outdated translations
        4. Perform translation on required files

        Translation types are determined by the translation_types list set during initialization.

        Args:
            update: Whether to update existing translations
            fast_mode: Whether to use faster translation method

        Returns:
            Tuple containing (total_modified_files, error_messages_list)
        """
        logger.info("Starting project translation...")
        total_modified = 0
        all_errors = []

        try:
            rename_map: dict[str, str] = {}
            migrated_image_count = 0
            should_migrate_links = (
                "markdown" in self.translation_types
                or "notebook" in self.translation_types
            )

            if "images" in self.translation_types:
                # Migrate legacy translated image filenames and update markdown/notebook links

                try:
                    rename_map = migrate_translated_image_filenames(
                        self.image_dir, self.language_codes
                    )
                    migrated_image_count += len(rename_map)
                except Exception as e:
                    logger.warning(f"Image filename migration skipped: {e}")
                    rename_map = {}

                try:
                    webp_rename_map = migrate_images_to_webp(
                        self.image_dir, self.language_codes
                    )
                except Exception as e:
                    logger.warning(f"WebP migration skipped: {e}")
                else:
                    rename_map.update(webp_rename_map)
                    migrated_image_count += len(webp_rename_map)
            else:
                logger.info(
                    "Skipping translated image migration because image translation is disabled"
                )

            if should_migrate_links:
                try:
                    # Always run link migration to rewrite legacy flattened links in content,
                    # even when no files were moved or image translation is disabled.
                    migrated_md = self.directory_manager.migrate_markdown_image_links(
                        rename_map
                    )
                    migrated_nb = self.directory_manager.migrate_notebook_image_links(
                        rename_map
                    )
                    logger.info(
                        "Updated image links in %d markdown and %d notebook files (migrated image files: %d)",
                        migrated_md,
                        migrated_nb,
                        migrated_image_count,
                    )
                except Exception as e:
                    logger.warning(f"Image link migration skipped: {e}")

                # As a safety net, canonicalize any remaining alias-based language dir segments in links.
                try:
                    md_fix, nb_fix = canonicalize_image_links_in_translations(
                        self.translations_dir, self.image_dir
                    )
                    if md_fix or nb_fix:
                        logger.info(
                            "Canonicalized image links in %d markdown and %d notebooks",
                            md_fix,
                            nb_fix,
                        )
                except Exception as e:
                    logger.warning(f"Image link canonicalization skipped: {e}")

            # Clean up files no longer needed in target directories
            logger.info("Removing orphaned files...")
            with tqdm(total=1, desc="🧹 Cleaning orphaned files") as cleanup_progress:
                # Markdown/Notebook cleanup scoped to selected languages
                removed_md_nb = self.directory_manager.cleanup_orphaned_translations(
                    markdown="markdown" in self.translation_types,
                    images=False,
                    notebooks="notebook" in self.translation_types,
                )

                # Image cleanup should consider ALL supported languages to avoid removing other languages
                removed_imgs = 0
                if "images" in self.translation_types:
                    cleanup_langs = Config.get_language_codes()
                    img_dm = DirectoryManager(
                        self.root_dir,
                        self.translations_dir,
                        cleanup_langs,
                        self.excluded_dirs,
                        image_dir=self.image_dir,
                    )
                    removed_imgs = img_dm.cleanup_orphaned_translations(
                        markdown=False,
                        images=True,
                        notebooks=False,
                    )

                removed_total = (removed_md_nb or 0) + (removed_imgs or 0)
                cleanup_progress.set_postfix_str(
                    "None" if removed_total == 0 else f"Removed: {removed_total}"
                )
                cleanup_progress.update(1)

            # Create and update directory structure to match source
            logger.info("Synchronizing directory structure...")
            with tqdm(total=1, desc="📁 Synchronizing directories") as sync_progress:
                created, removed, _ = self.directory_manager.sync_directory_structure(
                    markdown="markdown" in self.translation_types,
                    images="images" in self.translation_types,
                    notebooks="notebook" in self.translation_types,
                )
                sync_progress.set_postfix_str(
                    "None"
                    if (created == 0 and removed == 0)
                    else f"Created: {created}, Removed: {removed}"
                )
                sync_progress.update(1)

            # Find files needing translation due to source changes (markdown + notebooks)
            if (
                "markdown" in self.translation_types
                or "notebook" in self.translation_types
            ):
                # Pre-migrate legacy inline markdown metadata into centralized JSON before
                # outdated detection to avoid first-run false positives.
                try:
                    self._migrate_legacy_inline_text_metadata()
                except Exception as e:
                    logger.warning(f"Legacy text metadata migration skipped: {e}")

                with tqdm(total=1, desc="🔍 Checking translations") as check_progress:
                    outdated_files = self.get_outdated_translations()
                    check_progress.set_postfix_str(
                        "None"
                        if not outdated_files
                        else f"Found: {len(outdated_files)}"
                    )
                    check_progress.update(1)

                if outdated_files:
                    try:
                        est_tokens = estimate_tokens_for_outdated(
                            self,
                            outdated_files,
                            content_type="markdown",
                        ) + estimate_tokens_for_outdated(
                            self,
                            outdated_files,
                            content_type="notebook",
                        )
                        logger.info(
                            f"Estimated tokens for selected retranslation targets: {est_tokens:,}"
                        )
                    except Exception as e:
                        logger.debug(
                            f"Failed to estimate tokens for outdated files: {e}"
                        )
                    await self.retranslate_outdated_files(outdated_files)

            # Find outdated images needing retranslation
            if "images" in self.translation_types:
                # Clean up orphan metadata entries (images deleted but metadata remains)
                for lang_code in self.language_codes:
                    lang_dir = self.image_dir / lang_code
                    if lang_dir.exists():
                        cleanup_orphan_image_metadata(lang_dir)

                with tqdm(total=1, desc="🔍 Checking images") as check_progress:
                    outdated_images = self.get_outdated_images()
                    check_progress.set_postfix_str(
                        "None"
                        if not outdated_images
                        else f"Found: {len(outdated_images)}"
                    )
                    check_progress.update(1)

                if outdated_images:
                    await self.retranslate_outdated_images(
                        outdated_images, fast_mode=fast_mode
                    )

            # Execute translation for markdown, notebook and image files
            if "markdown" in self.translation_types:
                try:
                    md_pending = self._gather_pending_markdown(update=update)
                    md_tokens = estimate_tokens_for_sources(md_pending)
                    logger.info(
                        f"Estimated tokens for markdown translations: {md_tokens:,} (files: {len(md_pending)})"
                    )
                except Exception as e:
                    logger.debug(f"Failed to estimate markdown tokens: {e}")
                md_modified, md_errors = await self.translate_all_markdown_files(
                    update=update
                )
                total_modified += md_modified
                all_errors.extend(md_errors)

            if "notebook" in self.translation_types:
                try:
                    nb_pending = self._gather_pending_notebooks(update=update)
                    nb_tokens = estimate_tokens_for_sources(nb_pending)
                    logger.info(
                        f"Estimated tokens for notebook translations: {nb_tokens:,} (files: {len(nb_pending)})"
                    )
                except Exception as e:
                    logger.debug(f"Failed to estimate notebook tokens: {e}")
                nb_modified, nb_errors = await self.translate_all_notebook_files(
                    update=update
                )
                total_modified += nb_modified
                all_errors.extend(nb_errors)

            if "images" in self.translation_types:
                img_modified, img_errors = await self.translate_all_image_files(
                    update=update, fast_mode=fast_mode
                )
                total_modified += img_modified
                all_errors.extend(img_errors)

                # Final image cleanup: ALWAYS across ALL supported languages (like -l "all").
                cleanup_langs = Config.get_language_codes()
                logger.info(
                    "Performing final cleanup of translated images across ALL supported languages..."
                )

                dm_all = DirectoryManager(
                    self.root_dir,
                    self.translations_dir,
                    cleanup_langs,
                    self.excluded_dirs,
                    image_dir=self.image_dir,
                )
                with tqdm(total=1, desc="🧹 Final image cleanup") as cleanup_progress:
                    removed_after = dm_all.cleanup_orphaned_translations(
                        markdown=False,
                        images=True,
                        notebooks=False,
                    )
                    cleanup_progress.set_postfix_str(
                        "None" if removed_after == 0 else f"Removed: {removed_after}"
                    )
                    cleanup_progress.update(1)

                # Also cleanup fast-mode images if that directory exists
                fast_image_dir = self.root_dir / "translated_images_fast"
                if fast_image_dir.exists():
                    temp_dm = DirectoryManager(
                        self.root_dir,
                        self.translations_dir,
                        cleanup_langs,
                        self.excluded_dirs,
                        image_dir=fast_image_dir,
                    )
                    removed_fast = temp_dm.cleanup_orphaned_translations(
                        markdown=False, images=True, notebooks=False
                    )
                    logger.info(
                        f"Final cleanup (fast) removed {removed_fast} files from {fast_image_dir}"
                    )

            # Final step: Fix incorrect translated-image links only when image translations ran
            if (
                "markdown" in self.translation_types
                and "images" in self.translation_types
            ):
                await self.fix_incorrect_image_paths()

        except Exception as e:
            logger.error(f"Error during translation: {e}")
            # Fail fast: propagate to CLI so the process exits
            raise

        logger.info(f"Translation completed. Modified {total_modified} files.")
        if all_errors:
            logger.warning(f"Encountered {len(all_errors)} errors during translation")

        return total_modified, all_errors

    async def check_and_retry_translations(self):
        """Check translated files for formatting errors and retry failed translations.

        Identifies missing translations or files with line break inconsistencies
        and schedules them for retranslation.

        Returns:
            Tuple containing (total_files_checked, total_files_translated)
        """
        total_files_checked = 0
        files_to_translate = []

        # Collect all markdown files
        markdown_files = [
            file
            for file in filter_files(self.root_dir, self.excluded_dirs)
            if file.suffix.lower() in SUPPORTED_MARKDOWN_EXTENSIONS
        ]
        all_markdown_files = [
            (file, language_code)
            for file in markdown_files
            for language_code in self.language_codes
        ]

        total_files = len(all_markdown_files)

        if total_files == 0:
            logger.warning("No markdown files found for checking.")
            return

        logger.info("Checking translated files for errors...")

        # Identify files needing translation due to missing or format issues
        with tqdm(
            total=total_files, desc="Checking files", unit="file"
        ) as progress_bar:
            for md_file_path, language_code in all_markdown_files:
                md_file_path = Path(md_file_path).resolve()
                total_files_checked += 1

                # Find the path of the translated file
                relative_path = md_file_path.relative_to(self.root_dir)
                translated_md_file_path = (
                    self._get_language_root(language_code) / relative_path
                )

                if not translated_md_file_path.exists():
                    logger.warning(
                        f"Translated file does not exist: {translated_md_file_path}"
                    )
                    files_to_translate.append((md_file_path, language_code))
                    progress_bar.update(1)
                    continue

                # Read the content of both original and translated files
                original_content = read_input_file(md_file_path)
                translated_content = read_input_file(translated_md_file_path)

                # Check if line breaks are mismatched
                if compare_line_breaks(original_content, translated_content):
                    files_to_translate.append((md_file_path, language_code))
                    logger.warning(
                        f"Detected formatting issue in {translated_md_file_path}"
                    )

                # Update the progress bar after each file is checked
                progress_bar.update(1)

        # Translate files with missing translations or format problems
        if files_to_translate:
            logger.info(f"Starting translation for {len(files_to_translate)} files...")

            # Create a progress bar for translations
            with tqdm(
                total=len(files_to_translate), desc="Translating files", unit="file"
            ) as translation_progress_bar:
                for md_file_path, language_code in files_to_translate:
                    logger.info(f"Translating {md_file_path} to {language_code}...")

                    # Translate the file
                    await self.translate_markdown(
                        file_path=md_file_path,
                        language_code=language_code,
                    )

                    # Update the progress bar for translation process
                    translation_progress_bar.update(1)

            logger.info(f"Total files translated: {len(files_to_translate)}")
        else:
            logger.info("No formatting issues found in the translated files.")

        logger.info(f"Total files checked: {total_files_checked}")
