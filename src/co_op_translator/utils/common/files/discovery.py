from __future__ import annotations

from pathlib import Path


def filter_files(directory: str | Path, excluded_dirs, extension: str = None) -> list:
    """
    Filter and return only the files in the given directory, excluding specified directories.
    Optionally filter by file extension.

    Args:
        directory (str | Path): The directory path to search for files.
        excluded_dirs (set): A set of directory names to exclude from the search.
        extension (str, optional): File extension to filter by (e.g., '.ipynb').
                                If None, all file types are included.

    Returns:
        list: A list of Path objects representing only the files (excluding specified directories).
    """
    directory = Path(directory)
    files = []

    # Normalize excluded directories into two buckets: absolute paths and names
    abs_excluded: list[Path] = []
    name_excluded: set[str] = set()
    for item in excluded_dirs:
        try:
            p = Path(item)
            if p.is_absolute():
                abs_excluded.append(p.resolve())
            else:
                name_excluded.add(str(item))
        except Exception:
            name_excluded.add(str(item))

    # Recursively traverse the directory
    for path in directory.rglob("*"):
        if not path.is_file():
            continue
        if extension is not None and path.suffix.lower() != extension.lower():
            continue

        # Exclude by absolute path ancestry
        excluded_by_abs = False
        try:
            resolved = path.resolve()
            for abs_dir in abs_excluded:
                try:
                    resolved.relative_to(abs_dir)
                    excluded_by_abs = True
                    break
                except Exception:
                    continue
        except Exception:
            # If resolve() fails, fall back to name-based exclusion only
            excluded_by_abs = False

        if excluded_by_abs:
            continue

        # Name-based exclusion (segment match)
        if any(ex in path.parts for ex in name_excluded):
            continue

        files.append(path)

    return files
