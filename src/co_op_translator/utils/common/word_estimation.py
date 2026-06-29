import re
from pathlib import Path
from typing import Any

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import read_input_file


def _get_estimation_source_text(
    file_path: Path,
    virtual_file_contents: dict[Path, str] | None = None,
) -> str:
    if virtual_file_contents:
        try:
            resolved_path = file_path.resolve()
        except Exception:
            resolved_path = file_path
        if resolved_path in virtual_file_contents:
            return virtual_file_contents[resolved_path].strip()
    return read_input_file(file_path)


def _estimate_words_for_sources(
    files: list[Path],
    virtual_file_contents: dict[Path, str] | None = None,
) -> int:
    total = 0
    for file_path in files:
        try:
            text = _get_estimation_source_text(
                file_path,
                virtual_file_contents=virtual_file_contents,
            )
            total += len(re.findall(r"\S+", text))
        except Exception:
            continue
    return total


def _collect_outdated_sources_for_update(translation_manager: Any) -> list[Path]:
    sources: list[Path] = []
    for lang_code in translation_manager.language_codes:
        translation_dir = translation_manager._get_language_root(lang_code)
        if not translation_dir.exists():
            continue

        trans_files: list[Path] = []
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            trans_files.extend(translation_dir.rglob(f"*{ext}"))
        for ext in translation_manager.supported_notebook_extensions:
            trans_files.extend(translation_dir.rglob(f"*{ext}"))

        for trans_file in trans_files:
            try:
                rel = trans_file.relative_to(translation_dir)
                original = translation_manager.root_dir / rel
                content_type = (
                    "notebook"
                    if trans_file.suffix.lower()
                    in translation_manager.supported_notebook_extensions
                    else "markdown"
                )
                if original.exists() and (
                    not hasattr(translation_manager, "_is_source_in_scope")
                    or translation_manager._is_source_in_scope(
                        original, content_type=content_type
                    )
                ):
                    sources.append(original)
            except Exception:
                continue
    return sources


def estimate_translation_words(
    translation_manager: Any,
    update: bool = False,
    virtual_file_contents: dict[Path, str] | None = None,
) -> dict[str, int]:
    """Estimate direct source word counts for pre-run display."""
    breakdown = {"outdated": 0, "markdown": 0, "notebook": 0, "images": 0}

    if ("markdown" in translation_manager.translation_types) or (
        "notebook" in translation_manager.translation_types
    ):
        if update:
            outdated_sources = _collect_outdated_sources_for_update(translation_manager)
        else:
            outdated_sources = [
                source_file
                for source_file, _ in translation_manager.get_outdated_translations()
            ]

        if outdated_sources:
            breakdown["outdated"] = _estimate_words_for_sources(
                outdated_sources,
                virtual_file_contents=virtual_file_contents,
            )

    if "markdown" in translation_manager.translation_types:
        md_pending = translation_manager._gather_pending_markdown(update=update)
        if md_pending:
            breakdown["markdown"] = _estimate_words_for_sources(
                md_pending,
                virtual_file_contents=virtual_file_contents,
            )

    if "notebook" in translation_manager.translation_types:
        nb_pending = translation_manager._gather_pending_notebooks(update=update)
        if nb_pending:
            breakdown["notebook"] = _estimate_words_for_sources(
                nb_pending,
                virtual_file_contents=virtual_file_contents,
            )

    total = sum(breakdown.values())
    return {**breakdown, "total": total}
