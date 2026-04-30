from __future__ import annotations

import hashlib
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

HASH_PREFIX_LENGTH = 16


def get_actual_image_path(
    image_relative_path: str | Path,
    markdown_file_path: str | Path,
    root_dir: Path = None,
) -> Path:
    """
    Given an image's relative path from the markdown file, return the actual file path
    by resolving the relative path against the markdown file's location or the project root.

    Args:
        image_relative_path (str | Path): The relative path of the image as found in the markdown file.
        markdown_file_path (str | Path): The path to the markdown file.
        root_dir (Path, optional): The root directory of the project, for resolving root-relative paths.

    Returns:
        Path: The resolved absolute path to the image file.
    """
    if isinstance(image_relative_path, str) and image_relative_path.startswith("/"):
        if root_dir is None:
            # If root_dir is not provided but we have a root-relative path,
            # try to derive root_dir from markdown_file_path
            # This is a fallback and may not be accurate
            logger.warning(
                "Root directory not provided for root-relative path: %s",
                image_relative_path,
            )
            markdown_file_path = Path(markdown_file_path).resolve()
            # Attempt to find the project root (this is a guess)
            actual_image_path = markdown_file_path.parent / image_relative_path[1:]
        else:
            # Use the root directory to resolve the path
            image_path_without_leading_slash = image_relative_path[1:]
            actual_image_path = (root_dir / image_path_without_leading_slash).resolve()
            logger.info(
                f"Resolved root-relative path: {image_relative_path} -> {actual_image_path}"
            )
    else:
        # Handle regular relative paths as before
        image_relative_path = Path(image_relative_path)
        markdown_file_path = Path(markdown_file_path).resolve()
        actual_image_path = (markdown_file_path.parent / image_relative_path).resolve()

    return actual_image_path


def map_original_to_translated(
    original_abs: Path,
    language_code: str,
    root_dir: Path,
    translations_dir: Path | None = None,
) -> Path | None:
    """
    Map an absolute path of an original file under root_dir to its translated counterpart.

    Rules:
    - If original_abs is not under root_dir, return None.
    - The translated candidate path is translations/<lang>/<original_rel_from_root>.
    - If the candidate exists on disk, return it; otherwise return None.

    Args:
        original_abs (Path): Absolute path to the original file.
        language_code (str): Language code (e.g., 'ko').
        root_dir (Path): Project root.
        translations_dir (Path | None): Override translations dir; default root_dir / 'translations'.

    Returns:
        Path | None: Absolute path to translated file if it exists, else None.
    """
    original_abs = Path(original_abs).resolve()
    root_dir = Path(root_dir).resolve()
    translations_dir = (
        Path(translations_dir).resolve()
        if translations_dir
        else (root_dir / "translations").resolve()
    )

    try:
        original_rel = original_abs.relative_to(root_dir)
    except ValueError:
        # Outside project root
        return None

    candidate = (translations_dir / language_code / original_rel).resolve()
    return candidate if candidate.exists() else None


def get_unique_id(file_path: str | Path, root_dir: Path) -> str:
    """
    Generate a unique identifier (hash) for the given file path, based on the relative path to the root directory.
    This function normalizes path separators to '/' before hashing to ensure consistency across operating systems.

    Args:
        file_path (str | Path): The file path to hash.
        root_dir (Path): The root directory to which the file path should be relative.

    Returns:
        str: A SHA-256 hash of the normalized relative file path.
    """
    file_path = Path(file_path).resolve()
    relative_path = file_path.relative_to(root_dir)

    # Normalize path separators to '/' for cross-platform consistency
    normalized_path = str(relative_path).replace(os.sep, "/")

    # Convert the normalized path to bytes and hash it
    relative_path_bytes = normalized_path.encode("utf-8")
    hash_object = hashlib.sha256(relative_path_bytes)
    unique_identifier = hash_object.hexdigest()

    logger.info(f"HASH for normalized path: {normalized_path} HASH={unique_identifier}")

    return unique_identifier


def generate_translated_filename(
    original_filepath: str | Path, language_code: str, root_dir: Path
) -> str:
    """
    Generate a filename for a translated file, including a unique hash and language code.

    All translated images are saved as WebP format for optimal compression.
    The original extension is preserved in the base filename for traceability.

    Note:
    If the file path and the file name are identical, the same hash will be generated.
    This is because the hash is based on the entire file path.

    Args:
        original_filepath (str): The original file path.
        language_code (str): The language code for the translation (e.g., 'en', 'fr').

    Returns:
        str: The translated file's new filename (always .webp extension).
    """
    from co_op_translator.config.constants import WEBP_EXTENSION

    original_filepath = Path(original_filepath)

    # Extract original file components
    original_filename, file_ext = get_filename_and_extension(original_filepath)

    # Compute the full path hash based on the normalized path
    full_hash = get_unique_id(str(original_filepath), root_dir)

    # Use a fixed-size prefix for deterministic filenames across runs/OS
    hash_prefix = full_hash[:HASH_PREFIX_LENGTH]

    # Generate the new filename with WebP extension for optimal compression
    # All translated images are saved as WebP regardless of original format
    new_filename = f"{original_filename}.{hash_prefix}{WEBP_EXTENSION}"

    return new_filename


def get_filename_and_extension(file_path: str | Path) -> tuple[str, str]:
    """
    Extract the filename without extension and the file extension from the given file path.

    Args:
        file_path (str | Path): The file path from which to extract the filename and extension.

    Returns:
        tuple[str, str]: A tuple containing the filename without extension and the file extension.
    """
    # Ensure the file_path is a string or Path object
    file_path = str(file_path)  # Convert to string if it's a Path object

    # Extract the base name (filename with extension) and split it into name and extension
    original_filename, file_ext = os.path.splitext(os.path.basename(file_path))

    # Return the filename without extension and the file extension in lowercase
    return original_filename, file_ext.lower()
