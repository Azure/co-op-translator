from pathlib import Path
import logging
import json
from co_op_translator.utils.common.file_utils import get_unique_id
from pathlib import PurePosixPath
import os

logger = logging.getLogger(__name__)


class DirectoryManager:
    """
    Manages directory structure and file cleanup for translation project.
    """

    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path,
        language_codes: list[str],
        excluded_dirs: list[str],
    ):
        """
        Initialize DirectoryManager.

        Args:
            root_dir: Root directory containing original files
            translations_dir: Directory for translated files
            language_codes: List of target language codes
            excluded_dirs: List of directories to exclude
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs

    def sync_directory_structure(
        self, markdown: bool = True, images: bool = True
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
            tuple[int, int, int]: (created_dirs, removed_dirs, synced_langs)
        """
        created_count = 0
        removed_count = 0

        # Get original directory structure (excluding files)
        original_dirs = set()
        for path in self.root_dir.rglob("*"):
            if path.is_dir() and not any(
                excluded in str(path) for excluded in self.excluded_dirs
            ):
                # For image-only mode, only include image directories
                if (
                    not markdown
                    and not any(path.glob("*.png"))
                    and not any(path.glob("*.jpg"))
                ):
                    continue
                # For markdown-only mode, only include markdown directories
                if not images and not any(path.glob("*.md")):
                    continue
                # Store relative path for comparison
                original_dirs.add(path.relative_to(self.root_dir))

        # Sync each language directory
        for lang_code in self.language_codes:
            lang_dir = self.translations_dir / lang_code
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
                        if markdown and any(target_dir.rglob("*.md")):
                            has_relevant_files = True
                        if images and (
                            any(target_dir.rglob("*.png"))
                            or any(target_dir.rglob("*.jpg"))
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

    def cleanup_orphaned_translations(
        self, markdown: bool = True, images: bool = True
    ) -> int:
        """
        Remove translation files whose original files no longer exist.

        Args:
            markdown: Whether to clean up markdown files
            images: Whether to clean up image files

        Returns:
            int: Number of removed translation files
        """
        removed_count = 0
        logger.info(f"Starting cleanup with markdown={markdown}, images={images}")

        # Handle markdown files
        if markdown:
            for lang_code in self.language_codes:
                translation_dir = self.translations_dir / lang_code
                if not translation_dir.exists():
                    logger.info(
                        f"Translation directory does not exist: {translation_dir}"
                    )
                    continue

                logger.info(f"Checking translations in: {translation_dir}")

                md_files = []
                try:
                    md_files = list(translation_dir.rglob("*.md"))
                except Exception as e:
                    logger.warning(f"Error scanning for MD files: {e}")

                for trans_file in md_files:
                    try:
                        if not trans_file.exists():
                            continue

                        logger.info(f"Processing translation file: {trans_file}")
                        # Read translation file and find metadata comment
                        content = trans_file.read_text(encoding="utf-8")
                        metadata_start = content.find("<!--")
                        if metadata_start == -1:
                            logger.warning(f"No metadata found in: {trans_file}")
                            continue

                        metadata_end = content.find("-->", metadata_start)
                        if metadata_end == -1:
                            logger.warning(f"Incomplete metadata in: {trans_file}")
                            continue

                        metadata_str = content[
                            metadata_start + 4 : metadata_end
                        ].strip()
                        if "CO_OP_TRANSLATOR_METADATA:" in metadata_str:
                            _, json_str = metadata_str.split(
                                "CO_OP_TRANSLATOR_METADATA:", 1
                            )
                            metadata = json.loads(json_str.strip())
                        else:
                            metadata = json.loads(metadata_str)

                        source_file = metadata.get("source_file")
                        if not source_file:
                            logger.warning(f"No source_file in metadata: {trans_file}")
                            continue

                        normalized_path = str(PurePosixPath(source_file))
                        original_file = self.root_dir / normalized_path

                        logger.info(f"Checking original file: {original_file}")
                        if not original_file.exists():
                            logger.info(
                                f"Original file not found, deleting: {trans_file}"
                            )
                            trans_file.unlink()
                            removed_count += 1
                            logger.info(f"Successfully deleted: {trans_file}")

                            parent = trans_file.parent
                            while parent != translation_dir:
                                if parent.exists() and not any(parent.iterdir()):
                                    try:
                                        parent.rmdir()
                                        logger.info(
                                            f"Removed empty directory: {parent}"
                                        )
                                    except OSError as e:
                                        logger.warning(
                                            f"Could not remove directory {parent}: {e}"
                                        )
                                        break
                                else:
                                    break
                                parent = parent.parent
                        else:
                            logger.info(f"Original file exists, keeping: {trans_file}")

                    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
                        logger.warning(f"Error processing {trans_file}: {e}")
                        continue

        # Handle image files
        if images:
            # Collect all image files in the original directory
            original_images = {}  # path_hash -> original_file_path
            try:
                for original_img_file in self.root_dir.rglob("*"):
                    if not original_img_file.is_file():
                        continue

                    if original_img_file.suffix.lower() not in [
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".gif",
                    ]:
                        continue

                    try:
                        path_hash = get_unique_id(original_img_file, self.root_dir)
                        original_images[path_hash] = original_img_file
                    except ValueError:
                        continue
            except Exception as e:
                logger.warning(f"Error scanning for original images: {e}")

            for lang_code in self.language_codes:
                translation_dir = self.translations_dir / lang_code
                if not translation_dir.exists():
                    logger.info(
                        f"Image translation directory does not exist: {translation_dir}"
                    )
                    continue

                logger.info(f"Checking translated images in: {translation_dir}")

                image_files = []
                try:
                    image_files = list(translation_dir.rglob("*"))
                except Exception as e:
                    logger.warning(f"Error scanning for image files: {e}")

                for image_file in image_files:
                    if not image_file.is_file():
                        continue

                    if image_file.suffix.lower() not in [
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".gif",
                    ]:
                        continue

                    try:
                        parts = image_file.name.split(".")
                        if (
                            len(parts) < 4
                        ):  # Need at least name, hash, lang_code, and extension
                            continue

                        # Last part is extension, second to last is lang_code, third to last is path_hash
                        extension = parts[-1]
                        lang_code = parts[-2]
                        path_hash = parts[-3]

                        if lang_code not in self.language_codes:
                            continue

                        # Check if original file with matching path hash exists
                        if path_hash not in original_images:
                            image_file.unlink()
                            removed_count += 1
                            logger.debug(f"Removed orphaned image: {image_file}")

                            parent = image_file.parent
                            while parent != translation_dir:
                                if parent.exists() and not any(parent.iterdir()):
                                    try:
                                        parent.rmdir()
                                        logger.debug(
                                            f"Removed empty directory: {parent}"
                                        )
                                    except OSError as e:
                                        logger.warning(
                                            f"Could not remove directory {parent}: {e}"
                                        )
                                        break
                                else:
                                    break
                                parent = parent.parent

                    except Exception as e:
                        logger.warning(f"Error processing image {image_file}: {e}")
                        continue

        return removed_count
