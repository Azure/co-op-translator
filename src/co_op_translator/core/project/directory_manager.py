from pathlib import Path
import logging
import json
from co_op_translator.utils.common.file_utils import get_unique_id

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

        # Handle markdown files
        if markdown:
            for lang_code in self.language_codes:
                translation_dir = self.translations_dir / lang_code
                if not translation_dir.exists():
                    continue

                for trans_file in translation_dir.rglob("*.md"):
                    try:
                        # Read translation file and find metadata comment
                        content = trans_file.read_text(encoding="utf-8")
                        metadata_start = content.find("<!--")
                        if metadata_start == -1:
                            continue

                        metadata_end = content.find("-->", metadata_start)
                        if metadata_end == -1:
                            continue

                        metadata_str = content[
                            metadata_start + 4 : metadata_end
                        ].strip()
                        metadata = json.loads(metadata_str)

                        # Check if original file exists
                        source_file = metadata.get("source_file")
                        if not source_file:
                            continue

                        original_file = self.root_dir / source_file
                        if not original_file.exists():
                            trans_file.unlink()
                            removed_count += 1
                            logger.debug(f"Removed orphaned translation: {trans_file}")

                            # Try to remove empty parent directories
                            parent = trans_file.parent
                            while parent != translation_dir:
                                if not any(parent.iterdir()):  # If directory is empty
                                    try:
                                        parent.rmdir()
                                        logger.debug(
                                            f"Removed empty directory: {parent}"
                                        )
                                    except OSError:
                                        break  # Stop if directory is not empty or can't be removed
                                else:
                                    break  # Stop if directory is not empty
                                parent = parent.parent

                    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
                        logger.warning(f"Error processing {trans_file}: {e}")
                        continue

        # Handle image files
        if images:
            # Collect all image files in the original directory
            original_images = {}  # path_hash -> original_file_path
            for image_file in self.root_dir.rglob("*"):
                if not image_file.is_file():
                    continue

                if image_file.suffix.lower() not in [".png", ".jpg", ".jpeg", ".gif"]:
                    continue

                try:
                    path_hash = get_unique_id(image_file, self.root_dir)
                    original_images[path_hash] = image_file
                except ValueError:
                    continue

            # Check translated images in each language directory
            for lang_code in self.language_codes:
                translation_dir = self.translations_dir / lang_code
                if not translation_dir.exists():
                    continue

                for image_file in translation_dir.rglob("*"):
                    if not image_file.is_file():
                        continue

                    if image_file.suffix.lower() not in [
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".gif",
                    ]:
                        continue

                    # Image files follow the pattern: [original_name].[path_hash].[lang_code].[ext]
                    try:
                        # Split filename into parts
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

                            # Try to remove empty parent directories
                            parent = image_file.parent
                            while parent != translation_dir:
                                if not any(parent.iterdir()):  # If directory is empty
                                    try:
                                        parent.rmdir()
                                        logger.debug(
                                            f"Removed empty directory: {parent}"
                                        )
                                    except OSError:
                                        break  # Stop if directory is not empty or can't be removed
                                else:
                                    break  # Stop if directory is not empty
                                parent = parent.parent

                    except Exception as e:
                        logger.warning(f"Error processing image {image_file}: {e}")
                        continue

        return removed_count
