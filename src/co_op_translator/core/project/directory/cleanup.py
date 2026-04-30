from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from co_op_translator.config.constants import (
    SUPPORTED_IMAGE_EXTENSIONS,
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.common.file_utils import (
    get_filename_and_extension,
    get_unique_id,
)
from co_op_translator.utils.common.lang_utils import normalize_language_code
from co_op_translator.utils.common.metadata_utils import (
    extract_metadata_from_content,
    remove_image_metadata,
    remove_text_metadata_for_source,
)

logger = logging.getLogger(__name__)


class DirectoryCleanupMixin:
    def cleanup_orphaned_translations(
        self, markdown: bool = True, images: bool = True, notebooks: bool = True
    ) -> int:
        """Remove orphaned translation files that no longer have source files.

        Identifies and removes translation files where the original source file
        has been deleted or moved. Processes files by matching metadata to determine
        the correct language code and source file relationship.

        Args:
            markdown: Whether to clean up markdown files
            images: Whether to clean up image files
            notebooks: Whether to clean up notebook files

        Returns:
            Number of removed translation files
        """
        removed_count = 0
        logger.info(
            f"Starting cleanup with markdown={markdown}, images={images}, notebooks={notebooks}"
        )

        # Handle markdown files
        if markdown:
            for lang_code in self.language_codes:
                translation_dir = self._get_language_root(lang_code)
                if not translation_dir.exists():
                    logger.info(
                        f"Translation directory does not exist: {translation_dir}"
                    )
                    continue

                logger.info(f"Checking translations in: {translation_dir}")

                try:
                    md_files: list[Path] = []
                    for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                        md_files.extend(translation_dir.rglob(f"*{ext}"))
                except Exception as e:
                    logger.warning(f"Error scanning for MD files: {e}")
                    md_files = []

                for trans_file in md_files:
                    try:
                        if not trans_file.exists():
                            continue

                        logger.info(f"Processing translation file: {trans_file}")

                        original_file = None
                        # Prefer legacy inline metadata if present to resolve original path robustly
                        try:
                            content = trans_file.read_text(encoding="utf-8")
                            metadata = extract_metadata_from_content(content)
                            source_file = (
                                metadata.get("source_file") if metadata else None
                            )
                            if source_file:
                                # Normalize backslashes and construct a proper relative Path
                                rel_parts = (
                                    str(source_file).replace("\\", "/").split("/")
                                )
                                rel_path = Path(*rel_parts)
                                original_file = self.root_dir / rel_path
                        except Exception:
                            # Ignore content read/parse issues; will fallback to relative mapping
                            pass

                        if original_file is None:
                            # Fallback: compute original path by relative path from language dir
                            try:
                                rel = trans_file.relative_to(translation_dir)
                                original_file = self.root_dir / rel
                            except ValueError:
                                logger.warning(
                                    f"Unable to determine source for: {trans_file}"
                                )
                                continue

                        logger.info(f"Checking original file: {original_file}")
                        if not original_file.exists():
                            logger.info(
                                f"Original file not found, deleting: {trans_file}"
                            )
                            try:
                                trans_file.unlink()
                                removed_count += 1
                                logger.info(f"Successfully deleted: {trans_file}")
                            finally:
                                # Remove centralized metadata entry for this source
                                try:
                                    remove_text_metadata_for_source(
                                        translation_dir, original_file
                                    )
                                except Exception:
                                    pass

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

        # Handle notebook files
        if notebooks:
            for lang_code in self.language_codes:
                translation_dir = self._get_language_root(lang_code)
                if not translation_dir.exists():
                    logger.info(
                        f"Notebook translation directory does not exist: {translation_dir}"
                    )
                    continue

                logger.info(f"Checking translated notebooks in: {translation_dir}")

                try:
                    notebook_files: list[Path] = []
                    for ext in SUPPORTED_NOTEBOOK_EXTENSIONS:
                        notebook_files.extend(translation_dir.rglob(f"*{ext}"))
                except Exception as e:
                    logger.warning(f"Error scanning for notebook files: {e}")
                    notebook_files = []

                for nb_file in notebook_files:
                    try:
                        if not nb_file.exists():
                            continue

                        original_file = None
                        # Prefer legacy notebook inline metadata if present
                        try:
                            with open(nb_file, "r", encoding="utf-8") as f:
                                nb_json = json.load(f)
                            coop_meta = nb_json.get("metadata", {}).get(
                                "coopTranslator", {}
                            )
                            source_file = coop_meta.get("source_file")
                            if source_file:
                                rel_parts = (
                                    str(source_file).replace("\\", "/").split("/")
                                )
                                rel_path = Path(*rel_parts)
                                original_file = self.root_dir / rel_path
                        except Exception:
                            # Ignore JSON read/parse issues; will fallback to relative mapping
                            pass

                        if original_file is None:
                            # Fallback: compute original notebook path by relative path from language dir
                            try:
                                rel = nb_file.relative_to(translation_dir)
                                original_file = self.root_dir / rel
                            except ValueError:
                                logger.warning(
                                    f"Unable to determine source for notebook: {nb_file}"
                                )
                                continue

                        if not original_file.exists():
                            logger.info(
                                f"Original notebook not found, deleting: {nb_file}"
                            )
                            try:
                                nb_file.unlink()
                                removed_count += 1
                            finally:
                                # Remove centralized metadata entry for this source
                                try:
                                    remove_text_metadata_for_source(
                                        translation_dir, original_file
                                    )
                                except Exception:
                                    pass

                            parent = nb_file.parent
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
                            logger.info(f"Original notebook exists, keeping: {nb_file}")
                    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
                        logger.warning(f"Error processing notebook {nb_file}: {e}")
                        continue

        # Handle image files
        if images:
            # Collect all candidate original images (compute path hash map)
            original_images: dict[str, Path] = {}
            try:
                for original_img_file in self.root_dir.rglob("*"):
                    if not original_img_file.is_file():
                        continue
                    # Skip any files under excluded directories (e.g., translations, translated_images, translated_images_fast)
                    try:
                        rel_path = original_img_file.relative_to(self.root_dir)
                        if any(part in self.excluded_dirs for part in rel_path.parts):
                            continue
                    except ValueError:
                        # Outside root_dir
                        continue

                    if (
                        original_img_file.suffix.lower()
                        not in SUPPORTED_IMAGE_EXTENSIONS
                    ):
                        continue
                    try:
                        path_hash = get_unique_id(original_img_file, self.root_dir)
                        original_images[path_hash] = original_img_file
                    except ValueError:
                        continue
            except Exception as e:
                logger.warning(f"Error scanning for original images: {e}")

            image_dir = self.image_dir
            if not image_dir.exists():
                logger.info(f"Image directory does not exist: {image_dir}")
            else:
                logger.info(f"Checking translated images in: {image_dir}")

                try:
                    image_files = list(image_dir.rglob("*"))
                except Exception as e:
                    logger.warning(f"Error scanning for image files: {e}")
                    image_files = []

                for image_file in image_files:
                    if not image_file.is_file():
                        continue
                    if image_file.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
                        continue

                    try:
                        parts = image_file.name.split(".")
                        if len(parts) < 3:
                            continue

                        # Determine language code primarily from subdirectory (new format)
                        try:
                            rel_parts = image_file.relative_to(image_dir).parts
                        except Exception:
                            rel_parts = ()
                        lang_code = None
                        # Accept alias language folder names by normalizing to canonical
                        if len(rel_parts) >= 2:
                            parent_lang = rel_parts[0]
                            normalized_parent = normalize_language_code(parent_lang)
                            if normalized_parent in self.language_codes:
                                lang_code = normalized_parent
                                path_hash_segment = parts[-2]
                                base_name = ".".join(parts[:-2])
                        else:
                            # Legacy format: base.hash.lang.ext
                            if len(parts) < 4:
                                continue
                            lang_code = normalize_language_code(parts[-2])
                            path_hash_segment = parts[-3]
                            base_name = ".".join(parts[:-3])

                        # If language code is not supported (not in language_codes), delete it
                        if lang_code not in self.language_codes:
                            try:
                                image_file.unlink()
                                removed_count += 1
                                logger.debug(
                                    f"Removed image with unsupported language code: {image_file}"
                                )
                                # Remove from central metadata file
                                remove_image_metadata(image_file, image_dir)
                            except Exception as e:
                                logger.warning(
                                    f"Failed to delete image with unsupported language {image_file}: {e}"
                                )
                            continue

                        segment = (path_hash_segment or "").lower()
                        hex_allowed = re.fullmatch(
                            r"[0-9a-f]{16}|[0-9a-f]{64}", segment
                        )

                        if not hex_allowed:
                            has_match = False
                        else:
                            if len(segment) == 16:
                                candidates = [
                                    h
                                    for h in original_images.keys()
                                    if h.startswith(segment)
                                ]
                                has_match = False
                                for h in candidates:
                                    orig_path = original_images[h]
                                    orig_base, _ = get_filename_and_extension(orig_path)
                                    if orig_base == base_name:
                                        has_match = True
                                        break
                            elif len(segment) == 64:
                                if segment in original_images:
                                    orig_path = original_images[segment]
                                    orig_base, _ = get_filename_and_extension(orig_path)
                                    has_match = orig_base == base_name
                                else:
                                    has_match = False
                            else:
                                has_match = False

                        if not has_match:
                            try:
                                image_file.unlink()
                                removed_count += 1
                                logger.debug(f"Removed orphaned image: {image_file}")
                                # Remove from central metadata file
                                remove_image_metadata(image_file, image_dir)
                            except Exception as e:
                                logger.warning(
                                    f"Failed to delete orphaned image {image_file}: {e}"
                                )
                                continue

                            parent = image_file.parent
                            while parent != image_dir:
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
