import base64
import json
from unittest.mock import MagicMock

import pytest
from PIL import Image

from co_op_translator.mcp import server as mcp_server
from co_op_translator.review.models import ReviewSummary


@pytest.mark.asyncio
async def test_mcp_translate_markdown_content_uses_public_api(monkeypatch):
    calls = []

    async def fake_translate(document, language_code, options=None):
        calls.append((document, language_code, options))
        return f"translated:{language_code}:{document}"

    monkeypatch.setattr(
        mcp_server.co_op_api,
        "translate_markdown_content",
        fake_translate,
    )

    result = await mcp_server.translate_markdown_content(
        "# Hello",
        "ko",
        source_path="docs/guide.md",
    )

    assert result == {
        "language_code": "ko",
        "content": "translated:ko:# Hello",
    }
    assert calls == [
        (
            "# Hello",
            "ko",
            {
                "source_path": "docs/guide.md",
            },
        )
    ]


@pytest.mark.asyncio
async def test_mcp_translate_notebook_content_uses_public_api(monkeypatch):
    calls = []

    async def fake_translate(notebook, language_code, options=None):
        calls.append((notebook, language_code, options))
        return json.dumps({"metadata": {"language": language_code}})

    monkeypatch.setattr(
        mcp_server.co_op_api,
        "translate_notebook_content",
        fake_translate,
    )

    result = await mcp_server.translate_notebook_content(
        {"cells": []},
        "ja",
        source_path="docs/tutorial.ipynb",
    )

    assert json.loads(result["notebook"]) == {"metadata": {"language": "ja"}}
    assert calls == [
        (
            {"cells": []},
            "ja",
            {
                "source_path": "docs/tutorial.ipynb",
            },
        )
    ]


def test_mcp_translate_image_content_returns_base64_payload(monkeypatch, tmp_path):
    fake_image = Image.new("RGB", (3, 2), "blue")
    translate = MagicMock(return_value=fake_image)
    monkeypatch.setattr(mcp_server.co_op_api, "translate_image_content", translate)

    output_path = tmp_path / "translated.png"
    result = mcp_server.translate_image_content(
        "docs/images/hero.png",
        "fr",
        root_dir="docs",
        fast_mode=True,
        output_path=str(output_path),
    )

    translate.assert_called_once_with(
        "docs/images/hero.png",
        "fr",
        {
            "root_dir": "docs",
            "fast_mode": True,
        },
    )
    assert result["mime_type"] == "image/png"
    assert result["width"] == 3
    assert result["height"] == 2
    assert output_path.exists()
    assert base64.b64decode(result["data_base64"])


def test_mcp_rewrite_markdown_paths_uses_public_api(monkeypatch):
    rewrite = MagicMock(return_value="rewritten")
    monkeypatch.setattr(mcp_server.co_op_api, "rewrite_markdown_paths", rewrite)

    result = mcp_server.rewrite_markdown_paths(
        "[link](../README.md)",
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={"language_code": "ko"},
    )

    assert result == {"content": "rewritten"}
    rewrite.assert_called_once_with(
        "[link](../README.md)",
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={"language_code": "ko"},
    )


def test_mcp_agent_translation_tools_use_public_api(monkeypatch):
    start = MagicMock(return_value={"job_type": "markdown_agent_translation"})
    finish = MagicMock(return_value={"content": "# 안녕하세요"})
    monkeypatch.setattr(mcp_server.co_op_api, "start_markdown_agent_translation", start)
    monkeypatch.setattr(
        mcp_server.co_op_api, "finish_markdown_agent_translation", finish
    )

    job = mcp_server.start_markdown_agent_translation(
        "# Hello",
        "ko",
        source_path="docs/guide.md",
    )
    result = mcp_server.finish_markdown_agent_translation(
        job,
        [{"chunk_id": "body:1", "translated_text": "# 안녕하세요"}],
    )

    assert job == {"job_type": "markdown_agent_translation"}
    assert result == {"content": "# 안녕하세요"}
    start.assert_called_once_with(
        "# Hello",
        "ko",
        source_path="docs/guide.md",
    )
    finish.assert_called_once_with(
        job,
        [{"chunk_id": "body:1", "translated_text": "# 안녕하세요"}],
    )


def test_mcp_run_translation_requires_confirmation_for_writes():
    with pytest.raises(ValueError, match="confirm_write=true"):
        mcp_server.run_translation(
            language_codes="ko",
            markdown=True,
            dry_run=False,
        )


def test_mcp_run_translation_captures_public_api_output(monkeypatch):
    def fake_run_translation(**kwargs):
        print("translation started")
        assert kwargs["groups"] == [("docs", "localized")]
        assert kwargs["dry_run"] is True
        assert kwargs["readme_only"] is True

    monkeypatch.setattr(
        mcp_server.co_op_api,
        "run_translation",
        fake_run_translation,
    )

    result = mcp_server.run_translation(
        language_codes="ko",
        readme_only=True,
        groups=[{"root_dir": "docs", "translations_dir": "localized"}],
    )

    assert result["ok"] is True
    assert result["dry_run"] is True
    assert "translation started" in result["stdout"]


def test_mcp_run_review_returns_structured_summary(monkeypatch, tmp_path):
    summary = ReviewSummary(
        root_dir=tmp_path,
        source_files=[tmp_path / "README.md"],
        languages=["ko"],
    )
    run_review = MagicMock(return_value=summary)
    monkeypatch.setattr(mcp_server.co_op_api, "run_review", run_review)

    result = mcp_server.run_review(
        language_codes=["ko"],
        root_dir=str(tmp_path),
        markdown=True,
    )

    assert result["ok"] is True
    assert result["summary"]["root_dir"] == str(tmp_path)
    assert result["summary"]["source_files"] == [str(tmp_path / "README.md")]
    assert result["summary"]["languages"] == ["ko"]


@pytest.mark.asyncio
async def test_create_server_registers_tools_and_resources(monkeypatch):
    async def fake_translate(document, language_code, options=None):
        return f"{language_code}:{document}"

    monkeypatch.setattr(
        mcp_server.co_op_api,
        "translate_markdown_content",
        fake_translate,
    )

    server = mcp_server.create_server()
    tools = await server.list_tools()
    tool_names = {tool.name for tool in tools}

    assert {
        "translate_markdown_content",
        "translate_notebook_content",
        "start_markdown_agent_translation",
        "finish_markdown_agent_translation",
        "start_notebook_agent_translation",
        "finish_notebook_agent_translation",
        "translate_image_content",
        "rewrite_markdown_paths",
        "rewrite_notebook_paths",
        "run_translation",
        "translate_project",
        "run_review",
        "get_configuration_status",
        "list_supported_languages",
        "get_api_overview",
    }.issubset(tool_names)

    content_blocks, structured = await server.call_tool(
        "translate_markdown_content",
        {"document": "# Hello", "language_code": "ko"},
    )

    assert structured["content"] == "ko:# Hello"
    assert "ko:# Hello" in content_blocks[0].text

    resources = await server.list_resources()
    resource_uris = {str(resource.uri) for resource in resources}
    assert {
        "co-op://api",
        "co-op://supported-languages",
        "co-op://configuration",
    }.issubset(resource_uris)

    api_resource = await server.read_resource("co-op://api")
    assert "Co-op Translator" in api_resource[0].content
