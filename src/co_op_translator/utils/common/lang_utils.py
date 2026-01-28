from __future__ import annotations

import importlib.resources
import logging
import re
from pathlib import Path
from typing import Iterable, List, Tuple

import yaml

logger = logging.getLogger(__name__)

# Explicit alias map only (no heuristics). All keys are lower-case.
ALIAS_TO_BCP47: dict[str, str] = {
    # Chinese regions
    "cn": "zh-CN",
    "tw": "zh-TW",
    "hk": "zh-HK",
    "mo": "zh-MO",
    # Portuguese regions
    "br": "pt-BR",
    "pt": "pt-PT",  # treat bare 'pt' as Portugal when normalizing
    # Common country-code aliases
    "jp": "ja",
    "kr": "ko",
    # Generic zh alias maps to Mainland China for our purposes
    "zh": "zh-CN",
}

# BCP 47 basic pattern: language[-script][-region][-variants...]
# We only standardize language + region casing here, not validating scripts/variants.
_BCP47_SPLIT = re.compile(r"[-_]")


def canonical_case(code: str) -> str:
    """Apply canonical casing: language lower-case, region upper-case.

    Examples:
    - "pt-br" -> "pt-BR"
    - "ZH-tw" -> "zh-TW"
    - "ja" -> "ja"
    """
    parts = _BCP47_SPLIT.split(code.strip())
    if not parts:
        return code
    lang = parts[0].lower()
    rest: List[str] = []
    for i, p in enumerate(parts[1:], start=1):
        if len(p) == 2:  # region
            rest.append(p.upper())
        else:
            # leave script/variants as-is but prefer title for script (4 letters)
            if len(p) == 4:
                rest.append(p.title())
            else:
                rest.append(p)
    return "-".join([lang, *rest]) if rest else lang


def normalize_language_code(code: str) -> str:
    """Normalize an input code to our canonical BCP 47 form using explicit aliases.

    - Applies explicit alias mapping first (exact match on lower-cased input)
    - Then applies canonical casing rules.
    """
    raw = code.strip()
    if not raw:
        return raw
    key = raw.lower()
    if key in ALIAS_TO_BCP47:
        return ALIAS_TO_BCP47[key]
    return canonical_case(raw)


def normalize_language_codes(codes: Iterable[str]) -> List[str]:
    seen: set[str] = set()
    normalized: List[str] = []
    for c in codes:
        canon = normalize_language_code(c)
        if canon not in seen and canon:
            seen.add(canon)
            normalized.append(canon)
    return normalized


def get_supported_language_codes() -> List[str]:
    """Return canonical supported codes (keys) from font_language_mappings.yml.

    Note: This list reflects our packaging and is used when "all" is selected.
    """
    try:
        with importlib.resources.path(
            "co_op_translator.fonts", "font_language_mappings.yml"
        ) as mappings_path:
            with open(mappings_path, "r", encoding="utf-8") as file:
                font_mappings = yaml.safe_load(file) or {}
                return [
                    lang_code
                    for lang_code, meta in font_mappings.items()
                    if isinstance(meta, dict)
                ]
    except Exception as e:
        logger.warning(f"Failed to load font mappings: {e}")
        return []


def is_supported_language(code: str) -> bool:
    canon = normalize_language_code(code)
    return canon in set(get_supported_language_codes())
