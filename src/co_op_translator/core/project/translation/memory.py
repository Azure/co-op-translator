from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Protocol, runtime_checkable


@dataclass(frozen=True)
class TranslationBaseline:
    """Previously accepted source and target content for one translated file."""

    source_text: str
    target_text: str
    revision: str | None = None
    source_hash: str | None = None
    target_hash: str | None = None


@dataclass(frozen=True)
class TranslationUpdate:
    """Outcome of an incremental translation attempt."""

    content: str
    mode: Literal["incremental", "full"]
    preserved_units: int = 0
    translated_units: int = 0
    added_units: int = 0
    deleted_units: int = 0
    fallback_reason: str | None = None


@runtime_checkable
class TranslationStateProvider(Protocol):
    """Optional persistence boundary for translation baselines.

    Co-op Translator deliberately does not prescribe a database or storage format.
    Hosted products can implement this protocol, while existing CLI users continue
    to use the normal file-level retranslation behavior when no provider is passed.
    """

    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        """Return the last accepted source/target pair, if one is available."""

        ...

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        """Record a generated candidate without marking it as accepted."""

        ...
