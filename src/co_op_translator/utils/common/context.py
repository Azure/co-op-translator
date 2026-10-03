from __future__ import annotations

from pathlib import Path


def resolve_translation_context(
    context: str | None = None,
    context_file: str | Path | None = None,
) -> str | None:
    """Return combined inline and file-based translation guidance."""
    parts: list[str] = []
    if context and context.strip():
        parts.append(context.strip())
    if context_file is not None:
        path = Path(context_file).resolve()
        if not path.is_file():
            raise ValueError(f"Translation context file does not exist: {context_file}")
        file_context = path.read_text(encoding="utf-8").strip()
        if file_context:
            parts.append(file_context)
    return "\n\n".join(parts) or None
