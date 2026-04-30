from __future__ import annotations

from pathlib import Path

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.project.directory_manager import DirectoryManager

from .content_translation import ContentTranslationMixin
from .translation_discovery import TranslationDiscoveryMixin
from .translation_maintenance import TranslationMaintenanceMixin
from .translation_status import TranslationStatusMixin
from .translation_task_executor import TranslationTaskExecutorMixin
from .translation_workflow import TranslationWorkflowMixin


class TranslationManager(
    ContentTranslationMixin,
    TranslationWorkflowMixin,
    TranslationDiscoveryMixin,
    TranslationStatusMixin,
    TranslationMaintenanceMixin,
    TranslationTaskExecutorMixin,
):
    """Coordinate project translation through focused responsibility mixins."""

    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path,
        image_dir: Path,
        language_codes: list[str],
        excluded_dirs: list[str],
        supported_image_extensions: list[str],
        supported_notebook_extensions: list[str],
        markdown_translator: MarkdownTranslator,
        image_translator=None,
        notebook_translator=None,
        translation_types: list[str] = None,
        add_disclaimer: bool = True,
        lang_subdir: Path | None = None,
    ):
        """Initialize translation manager with required components and settings.

        Sets up paths, translators, and configurations needed for managing translations.

        Args:
            root_dir: Root directory containing original files
            translations_dir: Directory for translated files
            image_dir: Directory for translated images
            language_codes: List of target language codes
            excluded_dirs: List of directories to exclude
            supported_image_extensions: List of supported image extensions
            supported_notebook_extensions: List of supported notebook extensions
            markdown_translator: Translator instance for markdown files
            image_translator: Translator instance for image files
            notebook_translator: Translator instance for notebook files
            translation_types: List of file types to translate (e.g., ["markdown", "images", "notebook"])
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs
        self.supported_image_extensions = supported_image_extensions
        self.supported_notebook_extensions = supported_notebook_extensions
        self.markdown_translator = markdown_translator
        self.image_translator = image_translator
        self.notebook_translator = notebook_translator

        # Default translation types if not specified
        if translation_types is None:
            translation_types = ["markdown", "notebook", "images"]
        self.translation_types = translation_types
        self.add_disclaimer = add_disclaimer
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None
        self.directory_manager = DirectoryManager(
            root_dir,
            translations_dir,
            language_codes,
            excluded_dirs,
            image_dir=image_dir,
        )

    def _get_language_root(self, language_code: str) -> Path:
        """Return the root directory for a specific language.

        Default layout is translations_dir / language_code. When lang_subdir is
        set, we append it, yielding translations_dir / language_code / lang_subdir.
        """
        lang_dir = self.translations_dir / language_code
        if self.lang_subdir:
            lang_dir = lang_dir / self.lang_subdir
        return lang_dir
