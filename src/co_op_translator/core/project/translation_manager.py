"""Backward-compatible import path for the project translation manager."""

from co_op_translator.core.project.translation.manager import TranslationManager
from co_op_translator.utils.common.file_utils import (  # re-exported for legacy monkeypatch paths
    canonicalize_image_links_in_translations,
    filter_files,
    migrate_images_to_webp,
    migrate_translated_image_filenames,
)
from co_op_translator.utils.common.metadata_utils import is_notebook_up_to_date

__all__ = [
    "TranslationManager",
    "canonicalize_image_links_in_translations",
    "filter_files",
    "is_notebook_up_to_date",
    "migrate_images_to_webp",
    "migrate_translated_image_filenames",
]
