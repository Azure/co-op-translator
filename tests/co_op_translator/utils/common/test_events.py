import json

from co_op_translator.utils.common.events import (
    EVENT_SCHEMA,
    TranslationEvent,
    emit_translation_event,
    stage_key_for_label,
    translation_event_context,
)


def test_translation_event_serializes_stable_contract_fields():
    event = TranslationEvent(
        type="stage_progress",
        run_id="run-1",
        stage_key="translating_markdown_files",
        stage_label="Translating markdown files",
        language="ko",
        current_path="docs/intro.md",
        completed=12,
        total=40,
        progress=30,
    )

    payload = event.to_dict()

    assert payload["schema"] == EVENT_SCHEMA
    assert payload["type"] == "stage_progress"
    assert payload["stage_key"] == "translating_markdown_files"
    assert payload["stage_label"] == "Translating markdown files"
    assert payload["language"] == "ko"
    assert payload["current_path"] == "docs/intro.md"
    assert payload["progress"] == 30


def test_stage_key_prefers_stable_mapping_over_label_slug():
    assert (
        stage_key_for_label("Retranslating outdated markdown files")
        == "retranslating_outdated_markdowns"
    )
    assert stage_key_for_label("Custom Stage") == "custom_stage"


def test_translation_event_context_writes_ndjson(tmp_path):
    event_path = tmp_path / "progress.ndjson"

    with translation_event_context(json_events_path=event_path):
        emit_translation_event(
            "run_started",
            command="translate",
            languages=["ko"],
        )
        emit_translation_event(
            "run_completed",
            metadata={"dry_run": True},
        )

    rows = [
        json.loads(line) for line in event_path.read_text(encoding="utf-8").splitlines()
    ]

    assert [row["type"] for row in rows] == ["run_started", "run_completed"]
    assert all(row["schema"] == EVENT_SCHEMA for row in rows)
    assert rows[0]["languages"] == ["ko"]
    assert rows[1]["metadata"] == {"dry_run": True}
