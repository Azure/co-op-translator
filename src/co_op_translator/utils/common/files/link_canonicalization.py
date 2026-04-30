from __future__ import annotations

from pathlib import Path


def canonicalize_image_links_in_translations(
    translations_dir: Path, image_dir: Path
) -> tuple[int, int]:
    """
    Canonicalize image links in translated markdown and notebooks by rewriting
    alias-based language directory segments to canonical BCP 47.

    Examples:
      translated_images/tw/...  -> translated_images/zh-TW/...
      translated_images/cn/...  -> translated_images/zh-CN/...
      <base_dir>/br/...         -> <base_dir>/pt-BR/...

    The function scans under translations_dir and updates files in-place.

    Returns:
      (md_files_updated, nb_files_updated)
    """
    from co_op_translator.utils.common.lang_utils import ALIAS_TO_BCP47
    from co_op_translator.config.constants import (
        SUPPORTED_MARKDOWN_EXTENSIONS,
        SUPPORTED_NOTEBOOK_EXTENSIONS,
    )

    translations_dir = Path(translations_dir)
    image_dir = Path(image_dir)
    base_dir_name = image_dir.name
    base_dirs = [base_dir_name, "translated_images", "translated_images_fast"]

    def _canonicalize_text(text: str) -> str:
        updated = text
        for bdir in base_dirs:
            for alias, canonical in ALIAS_TO_BCP47.items():
                updated = updated.replace(f"{bdir}/{alias}/", f"{bdir}/{canonical}/")
                # Also replace Windows-style separators just in case
                updated = updated.replace(
                    f"{bdir}\\{alias}\\", f"{bdir}\\{canonical}\\"
                )
        return updated

    md_updated = 0
    nb_updated = 0

    # Markdown files
    try:
        md_files: list[Path] = []
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            md_files.extend(translations_dir.rglob(f"*{ext}"))
        for md in md_files:
            try:
                original = md.read_text(encoding="utf-8")
            except Exception:
                continue
            updated = _canonicalize_text(original)
            if updated != original:
                try:
                    md.write_text(updated, encoding="utf-8")
                    md_updated += 1
                except Exception:
                    pass
    except Exception:
        pass

    # Notebooks (JSON)
    try:
        nb_files: list[Path] = []
        for ext in SUPPORTED_NOTEBOOK_EXTENSIONS:
            nb_files.extend(translations_dir.rglob(f"*{ext}"))
        for nb in nb_files:
            try:
                content = nb.read_text(encoding="utf-8")
            except Exception:
                continue
            updated = _canonicalize_text(content)
            if updated != content:
                try:
                    nb.write_text(updated, encoding="utf-8")
                    nb_updated += 1
                except Exception:
                    pass
    except Exception:
        pass

    return md_updated, nb_updated
