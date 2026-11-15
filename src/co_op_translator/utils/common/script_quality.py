"""Script-quality validation for translated text.

Some target languages are written in scripts that models do not generate
reliably. A weak model may leave the source English in place, romanize the
target language in Latin letters, or fall back to another script that was
historically used for the language. Each of those outcomes would otherwise be
written to disk as a successful translation.

A language opts into validation by declaring a ``script_quality`` block in
``font_language_mappings.yml``::

    mni:
      name: "Manipuri (Meitei Mayek)"
      font: "NotoSansMeeteiMayek-Medium.ttf"
      script_quality:
        required_blocks: ["ABC0-ABFF", "AAE0-AAFF"]
        forbidden_blocks: ["0980-09FF"]
        min_required_share: 0.6
        max_forbidden_share: 0.02

After stripping code, placeholders, URLs, link destinations and HTML tags,
the share of letters that fall inside ``required_blocks`` must reach
``min_required_share`` and the share inside ``forbidden_blocks`` must stay
below ``max_forbidden_share``. Latin letters are deliberately allowed up to
the remaining share because product names, identifiers and acronyms are
expected to stay in Latin script.
"""

from __future__ import annotations

import logging
import re
import unicodedata
from dataclasses import dataclass
from importlib import resources
from typing import Any, Iterable, Mapping

import yaml

from co_op_translator.utils.common.lang_utils import normalize_language_code

logger = logging.getLogger(__name__)

DEFAULT_MIN_REQUIRED_SHARE = 0.6
DEFAULT_MAX_FORBIDDEN_SHARE = 0.02
DEFAULT_MIN_LETTERS = 20

REASON_INSUFFICIENT_REQUIRED = "insufficient_required_script"
REASON_FORBIDDEN_SCRIPT = "forbidden_script"

_FENCED_CODE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
_PLACEHOLDER_RE = re.compile(r"@@[^@\s]+@@")
_URL_RE = re.compile(r"https?://\S+|www\.\S+")
_LINK_DESTINATION_RE = re.compile(r"\]\([^)\n]*\)")
_HTML_TAG_RE = re.compile(r"<[^>\n]+>")
_HTML_ENTITY_RE = re.compile(r"&[#A-Za-z0-9]+;")
_FRONTMATTER_RE = re.compile(r"\A\s*---\n.*?\n---\n", re.S)
_BLOCK_RANGE_RE = re.compile(
    r"^\s*(?:U\+)?([0-9A-Fa-f]{4,6})\s*-\s*(?:U\+)?([0-9A-Fa-f]{4,6})\s*$"
)


@dataclass(frozen=True)
class ScriptQualityPolicy:
    """Thresholds that translated text for one language must satisfy."""

    required_ranges: tuple[tuple[int, int], ...]
    forbidden_ranges: tuple[tuple[int, int], ...] = ()
    min_required_share: float = DEFAULT_MIN_REQUIRED_SHARE
    max_forbidden_share: float = DEFAULT_MAX_FORBIDDEN_SHARE
    min_letters: int = DEFAULT_MIN_LETTERS


@dataclass(frozen=True)
class ScriptQualityResult:
    """Outcome of checking one piece of translated text against a policy."""

    ok: bool
    letters: int
    required_share: float
    forbidden_share: float
    reason: str | None = None

    def metadata(self) -> dict[str, Any]:
        data: dict[str, Any] = {
            "letters": self.letters,
            "required_share": round(self.required_share, 3),
            "forbidden_share": round(self.forbidden_share, 3),
        }
        if self.reason:
            data["reason"] = self.reason
        return data

    def describe(self) -> str:
        if self.reason == REASON_FORBIDDEN_SCRIPT:
            return f"{self.forbidden_share:.0%} of letters are in a forbidden script"
        if self.reason == REASON_INSUFFICIENT_REQUIRED:
            return f"only {self.required_share:.0%} of letters are in the target script"
        return "script quality check passed"


def parse_block_range(value: str) -> tuple[int, int]:
    """Parse ``"ABC0-ABFF"`` or ``"U+ABC0-U+ABFF"`` into inclusive code points."""
    match = _BLOCK_RANGE_RE.match(str(value))
    if not match:
        raise ValueError(f"Invalid Unicode block range: {value!r}")
    start, end = int(match.group(1), 16), int(match.group(2), 16)
    if start > end:
        raise ValueError(f"Unicode block range is reversed: {value!r}")
    return start, end


def parse_script_quality_policy(
    config: Mapping[str, Any] | None,
) -> ScriptQualityPolicy | None:
    """Build a policy from the ``script_quality`` block of a language mapping."""
    if not config:
        return None
    if not isinstance(config, Mapping):
        raise ValueError("script_quality must be a mapping")

    required = tuple(parse_block_range(r) for r in config.get("required_blocks", []))
    if not required:
        raise ValueError("script_quality.required_blocks must list at least one range")
    forbidden = tuple(
        parse_block_range(r) for r in config.get("forbidden_blocks", []) or []
    )

    min_required = float(config.get("min_required_share", DEFAULT_MIN_REQUIRED_SHARE))
    max_forbidden = float(
        config.get("max_forbidden_share", DEFAULT_MAX_FORBIDDEN_SHARE)
    )
    min_letters = int(config.get("min_letters", DEFAULT_MIN_LETTERS))
    if not 0.0 < min_required <= 1.0:
        raise ValueError("script_quality.min_required_share must be in (0, 1]")
    if not 0.0 <= max_forbidden <= 1.0:
        raise ValueError("script_quality.max_forbidden_share must be in [0, 1]")
    if min_letters < 1:
        raise ValueError("script_quality.min_letters must be at least 1")

    return ScriptQualityPolicy(
        required_ranges=required,
        forbidden_ranges=forbidden,
        min_required_share=min_required,
        max_forbidden_share=max_forbidden,
        min_letters=min_letters,
    )


def strip_non_prose(text: str) -> str:
    """Remove the parts of Markdown that are expected to stay in Latin script."""
    text = _FRONTMATTER_RE.sub(" ", text)
    text = _FENCED_CODE_RE.sub(" ", text)
    text = _INLINE_CODE_RE.sub(" ", text)
    text = _PLACEHOLDER_RE.sub(" ", text)
    text = _URL_RE.sub(" ", text)
    text = _LINK_DESTINATION_RE.sub("]", text)
    text = _HTML_TAG_RE.sub(" ", text)
    text = _HTML_ENTITY_RE.sub(" ", text)
    return text


def _in_ranges(code_point: int, ranges: Iterable[tuple[int, int]]) -> bool:
    return any(start <= code_point <= end for start, end in ranges)


def evaluate_script_quality(
    text: str, policy: ScriptQualityPolicy
) -> ScriptQualityResult:
    """Score ``text`` against ``policy`` using letters and combining marks only."""
    letters = 0
    required = 0
    forbidden = 0
    for char in strip_non_prose(text):
        if unicodedata.category(char)[0] not in ("L", "M"):
            continue
        letters += 1
        code_point = ord(char)
        if _in_ranges(code_point, policy.required_ranges):
            required += 1
        elif _in_ranges(code_point, policy.forbidden_ranges):
            forbidden += 1

    if letters < policy.min_letters:
        # Too little prose to judge (for example a heading made of product names).
        return ScriptQualityResult(True, letters, 0.0, 0.0)

    required_share = required / letters
    forbidden_share = forbidden / letters
    if forbidden_share > policy.max_forbidden_share:
        reason: str | None = REASON_FORBIDDEN_SCRIPT
    elif required_share < policy.min_required_share:
        reason = REASON_INSUFFICIENT_REQUIRED
    else:
        reason = None
    return ScriptQualityResult(
        reason is None, letters, required_share, forbidden_share, reason
    )


def load_script_quality_policies() -> dict[str, ScriptQualityPolicy]:
    """Read every ``script_quality`` block from the packaged font mappings."""
    try:
        mappings_resource = resources.files("co_op_translator.fonts").joinpath(
            "font_language_mappings.yml"
        )
        with mappings_resource.open("r", encoding="utf-8") as file:
            font_mappings = yaml.safe_load(file) or {}
    except Exception as e:
        logger.warning(f"Failed to load font mappings: {e}")
        return {}

    policies: dict[str, ScriptQualityPolicy] = {}
    for lang_code, meta in font_mappings.items():
        if not isinstance(meta, dict) or "script_quality" not in meta:
            continue
        try:
            policy = parse_script_quality_policy(meta.get("script_quality"))
        except ValueError as e:
            logger.warning(
                "Ignoring invalid script_quality config for '%s': %s", lang_code, e
            )
            continue
        if policy:
            policies[normalize_language_code(str(lang_code))] = policy
    return policies


def get_script_quality_policy(language_code: str) -> ScriptQualityPolicy | None:
    """Return the policy for ``language_code``, or None when it has none."""
    return load_script_quality_policies().get(normalize_language_code(language_code))


def check_script_quality(text: str, language_code: str) -> ScriptQualityResult | None:
    """Validate ``text`` for ``language_code``; None means no policy applies."""
    policy = get_script_quality_policy(language_code)
    if policy is None:
        return None
    return evaluate_script_quality(text, policy)
