import json

import pytest

from co_op_translator.core.agent_translation import (
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
)


def _translate_chunk_source(source: str) -> str:
    return (
        source.replace("Hello", "안녕하세요")
        .replace("Welcome", "환영합니다")
        .replace("Use", "사용하세요")
        .replace("here", "여기")
    )


def test_markdown_agent_translation_round_trips_placeholders():
    document = """# Hello

Use `pip install` here.

```python
print("Hello")
```
"""

    job = start_markdown_agent_translation(
        document,
        "ko",
        source_path="docs/guide.md",
    )

    assert job["job_type"] == "markdown_agent_translation"
    assert job["language_code"] == "ko"
    assert job["source_path"] == "docs/guide.md"
    assert job["chunks"]
    assert "@@CODE_BLOCK_" in job["chunks"][0]["source"]

    translated_chunks = [
        {
            "chunk_id": chunk["id"],
            "translated_text": _translate_chunk_source(chunk["source"]),
        }
        for chunk in job["chunks"]
    ]
    result = finish_markdown_agent_translation(job, translated_chunks)

    assert "# 안녕하세요" in result["content"]
    assert "`pip install`" in result["content"]
    assert 'print("Hello")' in result["content"]
    assert result["warnings"] == []


def test_markdown_agent_translation_restores_original_link_destinations():
    document = (
        "# Hello\n\n[Course](https://example.com/course?WT.mc_id=tracking-value)\n"
    )

    job = start_markdown_agent_translation(document, "ko")
    body_chunks = [chunk for chunk in job["chunks"] if chunk["kind"] == "body"]

    assert body_chunks
    assert "@@LINK_DESTINATION_" in body_chunks[0]["source"]
    assert "WT.mc_id" not in body_chunks[0]["source"]

    translated_chunks = {
        chunk["id"]: _translate_chunk_source(chunk["source"]).replace(
            "WT.mc_id", "WT_mc_id"
        )
        for chunk in job["chunks"]
    }
    result = finish_markdown_agent_translation(job, translated_chunks)

    assert "# 안녕하세요" in result["content"]
    assert "https://example.com/course?WT.mc_id=tracking-value" in result["content"]
    assert "WT_mc_id" not in result["content"]
    assert "@@LINK_DESTINATION_" not in result["content"]


def test_markdown_agent_translation_protects_frontmatter_link_destinations():
    document = (
        "---\n"
        "title: Guide\n"
        'description: "Read [Docs](https://example.com/?WT.mc_id=frontmatter)"\n'
        "---\n"
        "# Hello\n"
    )

    job = start_markdown_agent_translation(document, "ko")
    frontmatter_chunk = next(
        chunk for chunk in job["chunks"] if chunk["kind"] == "frontmatter"
    )
    assert "@@LINK_DESTINATION_" in frontmatter_chunk["source"]
    assert "https://example.com" not in frontmatter_chunk["source"]

    translated_chunks = {
        chunk["id"]: _translate_chunk_source(chunk["source"]).replace(
            "WT.mc_id", "WT_mc_id"
        )
        for chunk in job["chunks"]
    }
    result = finish_markdown_agent_translation(job, translated_chunks)

    assert "https://example.com/?WT.mc_id=frontmatter" in result["content"]
    assert "WT_mc_id" not in result["content"]
    assert "@@LINK_DESTINATION_" not in result["content"]


def test_markdown_agent_translation_rejects_missing_link_placeholder():
    job = start_markdown_agent_translation("[Docs](https://example.com)", "ko")
    translated_chunks = {
        chunk["id"]: chunk["source"].replace("@@LINK_DESTINATION_0@@", "")
        for chunk in job["chunks"]
    }

    with pytest.raises(ValueError, match="exactly once"):
        finish_markdown_agent_translation(job, translated_chunks)


def test_markdown_agent_translation_requires_all_chunks():
    job = start_markdown_agent_translation("# Hello\n\nWelcome.", "ko")

    with pytest.raises(ValueError, match="Missing translated chunks"):
        finish_markdown_agent_translation(job, {})


def test_notebook_agent_translation_translates_only_markdown_cells():
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# Hello\n", "\n", "Welcome.\n"],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "source": ["print('Hello')\n"],
                "outputs": [],
            },
        ],
        "metadata": {"kernelspec": {"name": "python3"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    job = start_notebook_agent_translation(
        notebook,
        "ko",
        source_path="docs/tutorial.ipynb",
    )

    assert job["job_type"] == "notebook_agent_translation"
    assert job["chunk_count"] == len(job["chunks"])
    assert all(chunk["id"].startswith("cell:0:") for chunk in job["chunks"])

    translated_chunks = {
        chunk["id"]: _translate_chunk_source(chunk["source"]) for chunk in job["chunks"]
    }
    result = finish_notebook_agent_translation(job, translated_chunks)
    translated = json.loads(result["notebook"])

    assert translated["cells"][0]["source"][0].startswith("# 안녕하세요")
    assert translated["cells"][1]["source"] == ["print('Hello')\n"]
    assert translated["metadata"] == notebook["metadata"]
    assert result["translated_cell_count"] == 1


MNI_MEITEI_TEXT = (
    "Co-op Translator ꯅꯥ Markdown ꯐꯥꯏꯜ ꯑꯃꯁꯨꯡ ꯐꯣꯇꯣꯁꯤꯡ ꯑꯁꯤ ꯂꯣꯜꯇꯥꯡ ꯀꯌꯥ ꯗ "
    "ꯑꯣꯇꯣꯃꯦꯇꯤꯛ ꯑꯣꯏꯅ ꯄꯥꯟꯗꯝ ꯄꯤꯔꯤ꯫ ꯃꯁꯤꯅ ꯐꯣꯔꯃꯦꯇꯤꯡ ꯑꯃꯁꯨꯡ ꯂꯤꯡꯛꯁ ꯐꯛꯅꯔꯛꯅ ꯊꯝꯃꯤ꯫"
)
MNI_ENGLISH_TEXT = (
    "Co-op Translator automates the translation of Markdown files and images "
    "into many languages while preserving formatting and links."
)


def _mni_job():
    document = (
        "# Overview\n\n"
        "Co-op Translator automates the translation of Markdown files and images "
        "into many languages while preserving formatting and links.\n"
    )
    return start_markdown_agent_translation(document, "mni", source_path="README.md")


def test_markdown_agent_finish_rejects_wrong_script_for_mni():
    job = _mni_job()
    body_ids = [c["id"] for c in job["chunks"] if c["kind"] == "body"]
    translations = {
        chunk_id: f"# ꯑꯣꯚꯔꯚꯤꯎ\n\n{MNI_ENGLISH_TEXT}\n" for chunk_id in body_ids
    }

    with pytest.raises(ValueError) as exc_info:
        finish_markdown_agent_translation(job, translations)

    message = str(exc_info.value)
    assert "not written in the expected script" in message
    assert body_ids[0] in message


def test_markdown_agent_finish_accepts_meitei_mayek_for_mni():
    job = _mni_job()
    body_ids = [c["id"] for c in job["chunks"] if c["kind"] == "body"]
    translations = {
        chunk_id: f"# ꯑꯣꯚꯔꯚꯤꯎ\n\n{MNI_MEITEI_TEXT}\n" for chunk_id in body_ids
    }

    result = finish_markdown_agent_translation(job, translations)

    assert result["language_code"] == "mni"
    assert MNI_MEITEI_TEXT in result["content"]
    assert result["warnings"] == []
