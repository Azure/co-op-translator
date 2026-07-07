"""Structured translation progress events."""

from __future__ import annotations

import json
import logging
import re
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping
from uuid import uuid4

logger = logging.getLogger(__name__)

EVENT_SCHEMA = "co-op.translation.event.v1"

TranslationEventCallback = Callable[["TranslationEvent"], None]

_STAGE_KEYS_BY_LABEL = {
    "Cleaning orphaned files": "cleanup_orphaned_files",
    "Synchronizing directories": "synchronizing_directories",
    "Checking translations": "checking_translations",
    "Checking images": "checking_images",
    "Checking translated files": "checking_translated_files",
    "Retranslating files": "retranslating_files",
    "Retranslating outdated notebooks": "retranslating_outdated_notebooks",
    "Retranslating outdated markdown files": "retranslating_outdated_markdowns",
    "Retranslating outdated images": "retranslating_outdated_images",
    "Translating markdown files": "translating_markdown_files",
    "Translating notebook files": "translating_notebook_files",
    "Translating images": "translating_images",
    "Translating images (fast mode)": "translating_images",
    "Final image cleanup": "final_image_cleanup",
}


def utc_timestamp() -> str:
    """Return an ISO-8601 UTC timestamp suitable for event payloads."""
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def stage_key_for_label(label: str) -> str:
    """Return a stable stage key for a human-facing stage label."""
    if label in _STAGE_KEYS_BY_LABEL:
        return _STAGE_KEYS_BY_LABEL[label]
    key = re.sub(r"[^a-z0-9]+", "_", label.strip().lower())
    return key.strip("_") or "unknown_stage"


def _json_safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


@dataclass(frozen=True)
class TranslationEvent:
    """Versioned event emitted by translation flows for integrations."""

    type: str
    run_id: str
    timestamp: str = field(default_factory=utc_timestamp)
    schema: str = EVENT_SCHEMA
    command: str | None = None
    root_dir: str | None = None
    languages: list[str] | None = None
    modes: list[str] | None = None
    stage_key: str | None = None
    stage_label: str | None = None
    language: str | None = None
    current_path: str | None = None
    completed: int | None = None
    total: int | None = None
    progress: int | None = None
    total_tokens: int | None = None
    total_words: int | None = None
    message: str | None = None
    level: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "schema": self.schema,
            "type": self.type,
            "run_id": self.run_id,
            "timestamp": self.timestamp,
        }
        optional_fields = {
            "command": self.command,
            "root_dir": self.root_dir,
            "languages": self.languages,
            "modes": self.modes,
            "stage_key": self.stage_key,
            "stage_label": self.stage_label,
            "language": self.language,
            "current_path": self.current_path,
            "completed": self.completed,
            "total": self.total,
            "progress": self.progress,
            "total_tokens": self.total_tokens,
            "total_words": self.total_words,
            "message": self.message,
            "level": self.level,
        }
        for key, value in optional_fields.items():
            if value is not None:
                payload[key] = _json_safe(value)
        if self.metadata:
            payload["metadata"] = _json_safe(self.metadata)
        return payload


class TranslationEventEmitter:
    """Dispatch translation events to callbacks and optional NDJSON files."""

    def __init__(
        self,
        *,
        callback: TranslationEventCallback | None = None,
        json_events_path: str | Path | None = None,
        run_id: str | None = None,
    ) -> None:
        self.run_id = run_id or uuid4().hex
        self._callbacks = [callback] if callback is not None else []
        self._event_file = None
        if json_events_path is not None:
            path = Path(json_events_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            self._event_file = path.open("w", encoding="utf-8")

    @property
    def active(self) -> bool:
        return bool(self._callbacks or self._event_file is not None)

    def close(self) -> None:
        if self._event_file is not None:
            self._event_file.close()
            self._event_file = None

    def emit(self, event_type: str, **fields: Any) -> TranslationEvent | None:
        if not self.active:
            return None

        completed = fields.get("completed")
        total = fields.get("total")
        if fields.get("progress") is None and completed is not None and total:
            fields["progress"] = int((int(completed) / int(total)) * 100)

        event = TranslationEvent(
            type=event_type,
            run_id=self.run_id,
            **fields,
        )
        for callback in self._callbacks:
            try:
                callback(event)
            except Exception as exc:  # pragma: no cover - defensive integration guard
                logger.warning("Translation event callback failed: %s", exc)
        if self._event_file is not None:
            self._event_file.write(
                json.dumps(event.to_dict(), ensure_ascii=False) + "\n"
            )
            self._event_file.flush()
        return event


_CURRENT_EMITTER: ContextVar[TranslationEventEmitter | None] = ContextVar(
    "co_op_translation_event_emitter",
    default=None,
)


@contextmanager
def translation_event_context(
    *,
    callback: TranslationEventCallback | None = None,
    json_events_path: str | Path | None = None,
    run_id: str | None = None,
) -> Iterator[TranslationEventEmitter | None]:
    """Install an event emitter for the current translation run."""
    emitter = TranslationEventEmitter(
        callback=callback,
        json_events_path=json_events_path,
        run_id=run_id,
    )
    if not emitter.active:
        yield None
        return

    token = _CURRENT_EMITTER.set(emitter)
    try:
        yield emitter
    finally:
        _CURRENT_EMITTER.reset(token)
        emitter.close()


def get_translation_event_emitter() -> TranslationEventEmitter | None:
    return _CURRENT_EMITTER.get()


def emit_translation_event(event_type: str, **fields: Any) -> TranslationEvent | None:
    emitter = get_translation_event_emitter()
    if emitter is None:
        return None
    return emitter.emit(event_type, **fields)
