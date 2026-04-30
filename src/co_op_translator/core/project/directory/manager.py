from __future__ import annotations

from pathlib import Path

from .cleanup import DirectoryCleanupMixin
from .link_migration import DirectoryLinkMigrationMixin
from .sync import DirectorySyncMixin


class DirectoryManager(
    DirectorySyncMixin,
    DirectoryCleanupMixin,
    DirectoryLinkMigrationMixin,
):
    """Manage directory structure, cleanup, and link migration for translations."""

    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path,
        language_codes: list[str],
        excluded_dirs: list[str],
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
    ):
        """Initialize directory manager with project configuration.

        Args:
            root_dir: Root directory containing original files
            translations_dir: Directory for translated text files (markdown/notebooks)
            language_codes: List of target language codes
            excluded_dirs: List of directories to exclude
            image_dir: Directory for translated images (flat tree, language code embedded in filename)
            lang_subdir: Optional nested subdirectory within each language folder
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs
        # Default to root_dir / "translated_images" if not provided
        self.image_dir = (
            image_dir
            if image_dir is not None
            else (self.root_dir / "translated_images")
        )
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None

    def _get_language_root(self, language_code: str) -> Path:
        """Get the root directory for a specific language's translations.

        Args:
            language_code: The target language code (e.g., 'ko', 'fr')

        Returns:
            Path to the language-specific translation directory
        """
        lang_dir = self.translations_dir / language_code
        if self.lang_subdir:
            lang_dir = lang_dir / self.lang_subdir
        return lang_dir
