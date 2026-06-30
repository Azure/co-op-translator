from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable

from co_op_translator.config.base_config import Config
from co_op_translator.utils.common.lang_utils import normalize_language_codes

DEFAULT_TRANSLATION_TYPES = ("markdown", "notebook", "images")


class TranslationMode(str, Enum):
    PROJECT = "project"
    README = "readme"


@dataclass(frozen=True)
class TranslationRequest:
    """Normalized project translation options shared by CLI and API entrypoints."""

    mode: TranslationMode
    language_codes: str
    language_list: tuple[str, ...]
    translation_types: tuple[str, ...]
    root_dir: str
    root_path: Path
    all_languages_selected: bool

    def translation_types_list(self) -> list[str]:
        return list(self.translation_types)

    def language_list_values(self) -> list[str]:
        return list(self.language_list)


def resolve_translation_types(
    *,
    markdown: bool = False,
    images: bool = False,
    notebook: bool = False,
    readme_only: bool = False,
) -> tuple[str, ...]:
    """Return translation types using the existing CLI/API option semantics."""
    if readme_only:
        if images or notebook:
            raise ValueError("readme_only can only be used with markdown translation.")
        return ("markdown",)

    translation_types: list[str] = []
    if markdown:
        translation_types.append("markdown")
    if images:
        translation_types.append("images")
    if notebook:
        translation_types.append("notebook")
    if not translation_types:
        return DEFAULT_TRANSLATION_TYPES
    return tuple(translation_types)


def normalize_requested_language_codes(
    language_codes: str | Iterable[str],
) -> tuple[tuple[str, ...], bool]:
    """Normalize requested language codes and expand the existing exact ``all`` token."""
    all_languages_selected = isinstance(language_codes, str) and language_codes == "all"
    if all_languages_selected:
        raw_codes = Config.get_language_codes()
        if not raw_codes:
            raise ValueError("No valid language codes found in font mappings")
    elif isinstance(language_codes, str):
        raw_codes = [code.strip() for code in language_codes.split()]
    else:
        raw_codes = [str(code).strip() for code in language_codes]

    normalized = tuple(normalize_language_codes(raw_codes))
    if not normalized:
        raise ValueError("No valid language codes provided")

    return normalized, all_languages_selected


def build_translation_request(
    *,
    language_codes: str | Iterable[str],
    root_dir: str = ".",
    markdown: bool = False,
    images: bool = False,
    notebook: bool = False,
    readme_only: bool = False,
) -> TranslationRequest:
    """Build normalized request data without performing I/O or provider checks."""
    language_list, all_languages_selected = normalize_requested_language_codes(
        language_codes
    )
    translation_types = resolve_translation_types(
        markdown=markdown,
        images=images,
        notebook=notebook,
        readme_only=readme_only,
    )
    root_path = Path(root_dir).resolve()

    return TranslationRequest(
        mode=TranslationMode.README if readme_only else TranslationMode.PROJECT,
        language_codes=" ".join(language_list),
        language_list=language_list,
        translation_types=translation_types,
        root_dir=root_dir,
        root_path=root_path,
        all_languages_selected=all_languages_selected,
    )
