# Workflow commands

Run commands with the project's Python environment and from the source root,
unless an explicit root is supplied. Replace the example languages with the
user's selection.

## Repository translation and synchronization

For Markdown and notebooks in the default `translations/<lang>/` layout:

```bash
translate -r . -l "ko ja" -md -nb --dry-run
translate -r . -l "ko ja" -md -nb -y --json-events translation-events.ndjson
translate -r . -l "ko ja" -md -nb --dry-run
co-op-review -r . -l "ko ja"
```

Use only `-md` when notebooks are outside scope. Without a content-type flag,
translation includes images and requires Vision configuration.
The review CLI checks Markdown and notebooks together; use `run_review` with
explicit types when a narrower review is needed. Review reports a nonzero exit
status, or raises `RuntimeError` through Python, when it finds errors. Inspect
the reported issues before treating this as an execution failure.

The second command makes provider calls and writes files. Normal orchestration
can also update README language tables, migrate legacy language folders, and
clean orphaned translations. Inspect the final diff. `-y` removes interactive
prompts; it does not expand the user's authorization.

Structured progress uses `co-op.translation.event.v1`. Read `type`, `stage_key`,
`language`, `current_path`, `completed`, and `total` when present. Counts are
stage-specific. Inspect errors and the final review, not only the last event.
`--dry-run` does not write an event file.

For custom layouts, use the public API. This works without depending on newer
CLI output-directory flags:

```python
from co_op_translator.api import run_review, run_translation

settings = dict(
    language_codes="ko ja",
    root_dir="./docs",
    translations_dir="i18n",
    markdown=True,
)
run_translation(**settings, dry_run=True)
# After checking the preview, run these in the same environment:
run_translation(**settings, json_events_path="translation-events.ndjson")
run_translation(**settings, dry_run=True)
run_review(**settings)
```

Review custom layouts carefully: if a diagnostic treats generated translations
as source files, inspect discovery and exclusions before interpreting the count.
Do not delete translations or suppress a whole warning class to make review pass.

For existing MCP, call `run_translation` with the same settings and
`dry_run=true`. To execute already authorized work, set `dry_run=false` and
`confirm_write=true`. Inspect `ok`, `error`, and `events`. Use `run_review`
afterwards. Tool names may have a host-specific namespace.

## Agent-assisted Markdown

The public Python API and MCP use the same prepare/finish contract. With Python,
save the job and translated chunks as UTF-8 JSON outside the source scan if
separate commands need to share state. Do not keep job state only in memory
across shell processes.

```python
from co_op_translator.api import (
    start_markdown_agent_translation,
    finish_markdown_agent_translation,
)

job = start_markdown_agent_translation(
    document=source_text,
    language_code="ko",
    source_path="docs/guide.md",
)
# Read job["chunks"]. Translate each chunk["source"] using chunk["prompt"].
# Keep every placeholder exactly as returned. Use chunk["id"] as chunk_id.
translated_chunks = [
    {"chunk_id": chunk_id, "translated_text": translated_text}
    for chunk_id, translated_text in completed_translations
]
result = finish_markdown_agent_translation(job, translated_chunks)
# Inspect result["warnings"], then use result["content"].
```

`source_text` and `completed_translations` above are the source and actual
translations supplied by the host agent. They are not an automatic provider
loop. If the destination changes relative paths, call `rewrite_markdown_paths`
before saving and inspect the rewritten code examples:

```python
from co_op_translator.api import rewrite_markdown_paths

content = rewrite_markdown_paths(
    result["content"],
    source_path="docs/guide.md",
    target_path="translations/ko/docs/guide.md",
    policy={
        "language_code": "ko",
        "root_dir": ".",
        "translations_dir": "translations",
        "translation_types": ["markdown"],
    },
)
```

With MCP, send the complete original `job` and translated chunks to
`finish_markdown_agent_translation`, then write the returned `content`.

## Agent-assisted notebooks

Use `start_notebook_agent_translation(notebook, language_code, source_path)` and
`finish_notebook_agent_translation(job, translated_chunks)` instead. Translate
the returned Markdown-cell chunks. Preserve cell IDs, code, outputs, execution
counts, and notebook metadata. Use `rewrite_notebook_paths` for changed paths.
The finish result stores the JSON string in `result["notebook"]`; Markdown
uses `result["content"]`. Inspect `result["warnings"]`, parse the notebook
JSON, and compare non-Markdown cells with the source.

## Configuration and current reference

Use existing configuration. Repository batches need Azure OpenAI, OpenAI, or
Anthropic credentials; image text additionally needs Azure AI Vision. The host
agent mode above does not use those provider credentials.

- [Provider configuration](https://azure.github.io/co-op-translator/configuration/)
- [Python API](https://azure.github.io/co-op-translator/api/)
- [MCP setup and tools](https://azure.github.io/co-op-translator/mcp/)
- [CLI reference](https://azure.github.io/co-op-translator/cli/)

Consult the installed version's help and these references when behavior differs.
