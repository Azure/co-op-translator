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
