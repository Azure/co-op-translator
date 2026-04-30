"""File utility modules split by responsibility."""

from .cleanup import (
    delete_translated_images_by_language_code,
    delete_translated_markdown_files_by_language_code,
    reset_translation_directories,
)
from .discovery import filter_files
from .image_migration import migrate_images_to_webp, migrate_translated_image_filenames
from .io import handle_empty_document, read_input_file, write_output_file
from .link_canonicalization import canonicalize_image_links_in_translations
from .paths import (
    HASH_PREFIX_LENGTH,
    generate_translated_filename,
    get_actual_image_path,
    get_filename_and_extension,
    get_unique_id,
    map_original_to_translated,
)
from .readme_templates import (
    OTHER_COURSES_END,
    OTHER_COURSES_START,
    LANG_TABLE_END,
    LANG_TABLE_START,
    load_languages_table_template,
    load_other_courses_template,
    render_updated_readme_languages_table,
    render_updated_readme_other_courses,
    replace_between_markers,
    update_readme_languages_table,
    update_readme_other_courses,
)

__all__ = [
    "HASH_PREFIX_LENGTH",
    "LANG_TABLE_END",
    "LANG_TABLE_START",
    "OTHER_COURSES_END",
    "OTHER_COURSES_START",
    "canonicalize_image_links_in_translations",
    "delete_translated_images_by_language_code",
    "delete_translated_markdown_files_by_language_code",
    "filter_files",
    "generate_translated_filename",
    "get_actual_image_path",
    "get_filename_and_extension",
    "get_unique_id",
    "handle_empty_document",
    "load_languages_table_template",
    "load_other_courses_template",
    "map_original_to_translated",
    "migrate_images_to_webp",
    "migrate_translated_image_filenames",
    "read_input_file",
    "render_updated_readme_languages_table",
    "render_updated_readme_other_courses",
    "replace_between_markers",
    "reset_translation_directories",
    "update_readme_languages_table",
    "update_readme_other_courses",
    "write_output_file",
]
