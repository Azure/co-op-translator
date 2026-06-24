"""Provider-free translation job helpers for agent-assisted MCP workflows."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping, Sequence

from co_op_translator.config.font_config import FontConfig
from co_op_translator.utils.common.lang_utils import normalize_language_code
from co_op_translator.utils.markdown import (
    generate_prompt_template,
    normalize_cjk_emphasis_markers,
    normalize_internal_anchor_links,
    process_markdown,
    replace_code_blocks,
    restore_code_blocks,
)
from co_op_translator.utils.markdown.frontmatter import get_frontmatter_parser
from co_op_translator.utils.markdown.notebook_cells import (
    get_cell_source_text,
    set_cell_source_text,
)

AGENT_TRANSLATION_JOB_VERSION = 1
MARKDOWN_JOB_TYPE = "markdown_agent_translation"
NOTEBOOK_JOB_TYPE = "notebook_agent_translation"


def _language_details(language_code: str) -> tuple[str, str, bool]:
    normalized = normalize_language_code(language_code)
    font_config = FontConfig()
    return (
        normalized,
        font_config.get_language_name(normalized),
        font_config.is_rtl(normalized),
    )


def _path_label(source_path: str | Path | None, fallback: str) -> str | None:
    if source_path is None:
        return None
    return str(source_path) or fallback


def _chunk(
    *,
    chunk_id: str,
    kind: str,
    source: str,
    prompt: str,
    index: int,
    total: int,
) -> dict[str, Any]:
    return {
        "id": chunk_id,
        "kind": kind,
        "index": index,
        "total": total,
        "source": source,
        "prompt": prompt,
        "instructions": (
            "Translate this chunk by following the prompt. Return only the "
            "translated content for this chunk, preserving placeholders and "
            "Markdown structure exactly."
        ),
    }


def start_markdown_agent_translation(
    document: str,
    language_code: str,
    source_path: str | Path | None = None,
) -> dict[str, Any]:
    """Prepare a Markdown translation job without calling an LLM provider.

    The returned job is self-contained. An MCP host agent can translate each
    returned chunk with its own model, then pass the job and translated chunks to
    ``finish_markdown_agent_translation`` for deterministic reconstruction.
    """

    normalized_code, language_name, is_rtl = _language_details(language_code)
    source_label = _path_label(source_path, "content.md")

    parser = get_frontmatter_parser()
    frontmatter, body = parser.extract_frontmatter(document)
    preserve_fields: dict[str, Any] = {}
    translate_fields: dict[str, Any] = {}
    frontmatter_section = ""

    if frontmatter:
        preserve_fields, translate_fields = parser.split_fields(frontmatter)
        if translate_fields:
            frontmatter_section = parser.extract_translatable_fields_as_markdown(
                translate_fields
            )

    document_with_placeholders, placeholder_map = replace_code_blocks(body)
    body_chunks = process_markdown(document_with_placeholders)

    chunks: list[dict[str, Any]] = []
    if frontmatter_section:
        prompt = generate_prompt_template(
            normalized_code, language_name, frontmatter_section, is_rtl
        )
        chunks.append(
            _chunk(
                chunk_id="frontmatter:1",
                kind="frontmatter",
                source=frontmatter_section,
                prompt=prompt,
                index=1,
                total=1,
            )
        )

    for index, body_chunk in enumerate(body_chunks, start=1):
        prompt = generate_prompt_template(
            normalized_code, language_name, body_chunk, is_rtl
        )
        chunks.append(
            _chunk(
                chunk_id=f"body:{index}",
                kind="body",
                source=body_chunk,
                prompt=prompt,
                index=index,
                total=len(body_chunks),
            )
        )

    return {
        "job_type": MARKDOWN_JOB_TYPE,
        "version": AGENT_TRANSLATION_JOB_VERSION,
        "language_code": normalized_code,
        "language_name": language_name,
        "is_rtl": is_rtl,
        "source_path": source_label,
        "chunk_count": len(chunks),
        "chunks": chunks,
        "state": {
            "original_document": document,
            "placeholder_map": placeholder_map,
            "has_frontmatter": frontmatter is not None,
            "preserve_fields": preserve_fields,
            "translate_fields": translate_fields,
        },
        "agent_instructions": (
            "Translate each item in chunks with the host agent model. Do not "
            "call Co-op Translator provider-backed translate tools for these "
            "chunks. Pass translated chunks to finish_markdown_agent_translation "
            "using chunk_id and translated_text."
        ),
    }


def _translated_chunk_text(item: Mapping[str, Any]) -> str:
    for key in ("translated_text", "translation", "content", "text"):
        if key in item:
            return str(item[key])
    raise ValueError(
        "Each translated chunk must include translated_text, translation, content, or text."
    )


def _coerce_translated_chunks(
    translated_chunks: Mapping[str, Any] | Sequence[Mapping[str, Any]],
) -> dict[str, str]:
    if isinstance(translated_chunks, Mapping):
        return {
            str(chunk_id): str(text) for chunk_id, text in translated_chunks.items()
        }

    translations: dict[str, str] = {}
    for item in translated_chunks:
        chunk_id = item.get("chunk_id", item.get("id"))
        if not chunk_id:
            raise ValueError("Each translated chunk must include chunk_id or id.")
        chunk_id = str(chunk_id)
        if chunk_id in translations:
            raise ValueError(f"Duplicate translated chunk id: {chunk_id}")
        translations[chunk_id] = _translated_chunk_text(item)
    return translations


def _validate_markdown_job(job: Mapping[str, Any]) -> None:
    if job.get("job_type") != MARKDOWN_JOB_TYPE:
        raise ValueError("Expected a markdown agent translation job.")
    if job.get("version") != AGENT_TRANSLATION_JOB_VERSION:
        raise ValueError(
            f"Unsupported markdown agent translation job version: {job.get('version')}"
        )


def finish_markdown_agent_translation(
    job: Mapping[str, Any],
    translated_chunks: Mapping[str, Any] | Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Reconstruct a translated Markdown document from agent-translated chunks."""

    _validate_markdown_job(job)
    translations = _coerce_translated_chunks(translated_chunks)

    chunks = list(job.get("chunks", []))
    expected_ids = [str(chunk["id"]) for chunk in chunks]
    missing = [chunk_id for chunk_id in expected_ids if chunk_id not in translations]
    if missing:
        raise ValueError(f"Missing translated chunks: {', '.join(missing)}")

    extra = sorted(set(translations) - set(expected_ids))
    body_results: list[str] = []
    frontmatter_result = ""

    for chunk in chunks:
        chunk_id = str(chunk["id"])
        kind = str(chunk.get("kind"))
        translated = translations[chunk_id]
        if kind == "frontmatter":
            frontmatter_result = translated
        elif kind == "body":
            body_results.append(translated)

    translated_content = "\n".join(body_results)
    language_code = str(job["language_code"])
    state = dict(job.get("state", {}))

    translated_content = normalize_cjk_emphasis_markers(
        translated_content, language_code=language_code
    )
    translated_content = normalize_internal_anchor_links(
        str(state.get("original_document", "")), translated_content
    )
    translated_content = restore_code_blocks(
        translated_content,
        dict(state.get("placeholder_map", {})),
    )

    if state.get("has_frontmatter"):
        parser = get_frontmatter_parser()
        preserve_fields = dict(state.get("preserve_fields", {}))
        translate_fields = dict(state.get("translate_fields", {}))
        translated_frontmatter_fields = dict(translate_fields)
        if frontmatter_result and translate_fields:
            translated_frontmatter_fields.update(
                parser.parse_translated_fields_from_markdown(
                    frontmatter_result,
                    translate_fields,
                )
            )
        merged_frontmatter = parser.merge_fields(
            preserve_fields,
            translated_frontmatter_fields,
        )
        translated_content = parser.reconstruct_content(
            merged_frontmatter,
            translated_content,
        )

    return {
        "language_code": language_code,
        "source_path": job.get("source_path"),
        "content": translated_content,
        "warnings": (
            [f"Ignored extra translated chunks: {', '.join(extra)}"] if extra else []
        ),
    }


def _load_notebook(notebook: str | Mapping[str, Any]) -> dict[str, Any]:
    if isinstance(notebook, str):
        return json.loads(notebook)
    return deepcopy(dict(notebook))


def start_notebook_agent_translation(
    notebook: str | Mapping[str, Any],
    language_code: str,
    source_path: str | Path | None = None,
) -> dict[str, Any]:
    """Prepare a notebook Markdown-cell translation job without provider calls."""

    normalized_code, language_name, is_rtl = _language_details(language_code)
    notebook_payload = _load_notebook(notebook)
    source_label = _path_label(source_path, "notebook.ipynb")

    cell_jobs: list[dict[str, Any]] = []
    chunks: list[dict[str, Any]] = []
    for cell_index, cell in enumerate(notebook_payload.get("cells", [])):
        if cell.get("cell_type") != "markdown":
            continue

        markdown = get_cell_source_text(cell)
        if not markdown.strip():
            continue

        cell_source_path = (
            f"{source_label}#cell-{cell_index}"
            if source_label
            else f"cell-{cell_index}"
        )
        markdown_job = start_markdown_agent_translation(
            markdown,
            normalized_code,
            source_path=cell_source_path,
        )
        cell_jobs.append(
            {
                "cell_index": cell_index,
                "job": markdown_job,
            }
        )
        for chunk in markdown_job["chunks"]:
            prefixed_chunk = dict(chunk)
            prefixed_chunk["id"] = f"cell:{cell_index}:{chunk['id']}"
            prefixed_chunk["cell_index"] = cell_index
            chunks.append(prefixed_chunk)

    return {
        "job_type": NOTEBOOK_JOB_TYPE,
        "version": AGENT_TRANSLATION_JOB_VERSION,
        "language_code": normalized_code,
        "language_name": language_name,
        "is_rtl": is_rtl,
        "source_path": source_label,
        "chunk_count": len(chunks),
        "chunks": chunks,
        "state": {
            "notebook": notebook_payload,
            "cell_jobs": cell_jobs,
        },
        "agent_instructions": (
            "Translate each returned chunk with the host agent model. Pass the "
            "translated chunks to finish_notebook_agent_translation using chunk_id "
            "and translated_text. Code cells, outputs, and notebook metadata will "
            "be preserved."
        ),
    }


def _validate_notebook_job(job: Mapping[str, Any]) -> None:
    if job.get("job_type") != NOTEBOOK_JOB_TYPE:
        raise ValueError("Expected a notebook agent translation job.")
    if job.get("version") != AGENT_TRANSLATION_JOB_VERSION:
        raise ValueError(
            f"Unsupported notebook agent translation job version: {job.get('version')}"
        )


def finish_notebook_agent_translation(
    job: Mapping[str, Any],
    translated_chunks: Mapping[str, Any] | Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Reconstruct a translated notebook from agent-translated Markdown chunks."""

    _validate_notebook_job(job)
    translations = _coerce_translated_chunks(translated_chunks)

    chunks = list(job.get("chunks", []))
    expected_ids = [str(chunk["id"]) for chunk in chunks]
    missing = [chunk_id for chunk_id in expected_ids if chunk_id not in translations]
    if missing:
        raise ValueError(f"Missing translated chunks: {', '.join(missing)}")

    extra = sorted(set(translations) - set(expected_ids))
    state = dict(job.get("state", {}))
    notebook_payload = deepcopy(state.get("notebook", {}))
    translated_cell_count = 0

    for cell_job in state.get("cell_jobs", []):
        cell_index = int(cell_job["cell_index"])
        prefix = f"cell:{cell_index}:"
        markdown_translations = {
            chunk_id.removeprefix(prefix): text
            for chunk_id, text in translations.items()
            if chunk_id.startswith(prefix)
        }
        result = finish_markdown_agent_translation(
            cell_job["job"],
            markdown_translations,
        )
        set_cell_source_text(
            notebook_payload["cells"][cell_index],
            result["content"],
        )
        translated_cell_count += 1

    return {
        "language_code": job["language_code"],
        "source_path": job.get("source_path"),
        "notebook": json.dumps(notebook_payload, ensure_ascii=False, indent=1),
        "translated_cell_count": translated_cell_count,
        "warnings": (
            [f"Ignored extra translated chunks: {', '.join(extra)}"] if extra else []
        ),
    }
