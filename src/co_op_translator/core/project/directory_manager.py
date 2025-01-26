from pathlib import Path
import logging
from typing import Set

from co_op_translator.utils.common.file_utils import filter_files

logger = logging.getLogger(__name__)

class DirectoryManager:
    """
    Manages directory structure and file cleanup for translation project.
    """
    
    def __init__(self, root_dir: Path, translations_dir: Path, language_codes: list[str], excluded_dirs: list[str]):
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

    def sync_directory_structure(self, markdown: bool = True, images: bool = True) -> tuple[int, int, int]:
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
        for path in self.root_dir.rglob('*'):
            if path.is_dir() and not any(excluded in str(path) for excluded in self.excluded_dirs):
                # For image-only mode, only include image directories
                if not markdown and not any(path.glob('*.png')) and not any(path.glob('*.jpg')):
                    continue
                # For markdown-only mode, only include markdown directories
                if not images and not any(path.glob('*.md')):
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
                for path in lang_dir.rglob('*'):
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
            for trans_dir in sorted(translation_dirs, reverse=True):  # Sort reverse to handle deep paths first
                if trans_dir not in original_dirs:
                    target_dir = lang_dir / trans_dir
                    try:
                        # Only remove if empty or contains no relevant files
                        has_relevant_files = False
                        if markdown and any(target_dir.rglob('*.md')):
                            has_relevant_files = True
                        if images and (any(target_dir.rglob('*.png')) or any(target_dir.rglob('*.jpg'))):
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

    def cleanup_orphaned_translations(self, markdown: bool = True, images: bool = True) -> int:
        """
        Remove translation files whose original files no longer exist.
        
        Args:
            markdown: Whether to clean up markdown files
            images: Whether to clean up image files
           
        Returns:
            int: Number of removed translation files
        """
        removed_count = 0
        
        # Iterate through each language directory
        for lang_code in self.language_codes:
            lang_dir = self.translations_dir / lang_code
            if not lang_dir.exists():
                continue
                
            # Find all files in the language directory
            for translated_file in filter_files(lang_dir, self.excluded_dirs):
                file_ext = translated_file.suffix.lower()
                
                # Skip files based on mode
                if not markdown and file_ext == '.md':
                    continue
                if not images and file_ext in ['.png', '.jpg']:
                    continue
                    
                try:
                    # Calculate original file path
                    relative_path = translated_file.relative_to(lang_dir)
                    original_file = self.root_dir / relative_path
                    
                    # If original doesn't exist, remove the translation
                    if not original_file.exists():
                        logger.info(f"Removing orphaned translation: {translated_file}")
                        try:
                            translated_file.unlink()  # Delete the file
                            removed_count += 1
                            
                            # Try to remove empty parent directories
                            parent = translated_file.parent
                            while parent != lang_dir:
                                if not any(parent.iterdir()):  # If directory is empty
                                    try:
                                        parent.rmdir()
                                        logger.info(f"Removed empty directory: {parent}")
                                    except OSError:
                                        break  # Stop if directory is not empty or can't be removed
                                else:
                                    break  # Stop if directory is not empty
                                parent = parent.parent
                                
                        except OSError as e:
                            logger.error(f"Failed to remove {translated_file}: {e}")
                            
                except Exception as e:
                    logger.error(f"Error processing {translated_file}: {e}")
                    continue
                    
        return removed_count
