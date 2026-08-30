from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(frozen=True)
class ModelResponse:
    """Framework-neutral response returned by a translation model client."""

    content: str
    finish_reason: str | None = None
    raw_response: Any = field(default=None, repr=False, compare=False)


@runtime_checkable
class TranslationModelClient(Protocol):
    """Minimal completion boundary used by translation and evaluation flows."""

    async def complete(
        self,
        system_prompt: str,
        user_content: str,
        *,
        temperature: float | None = None,
    ) -> ModelResponse:
        """Complete one system/user prompt pair."""
