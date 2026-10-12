from __future__ import annotations

import sys
from types import ModuleType, SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from co_op_translator.core.llm.markdown_translator import TranslationIncompleteError
from co_op_translator.core.llm.model_client_translator import (
    ModelClientMarkdownTranslator,
)
from co_op_translator.core.llm.model_clients import (
    LiteLLMModelClient,
    StructuredTranslationModelClient,
    TranslationModelClient,
)
from co_op_translator.utils.llm.text_utils import TranslationResponse
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER


def _litellm_response(content, finish_reason="stop"):
    return SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(role="assistant", content=content),
                finish_reason=finish_reason,
            )
        ]
    )


@pytest.fixture
def fake_litellm(monkeypatch):
    """Install a stub ``litellm`` module so tests run without the extra."""
    module = ModuleType("litellm")
    module.acompletion = AsyncMock(return_value=_litellm_response("translated"))
    monkeypatch.setitem(sys.modules, "litellm", module)
    return module


def test_litellm_adapter_satisfies_translation_protocols():
    client = LiteLLMModelClient("gemini/gemini-2.5-flash")

    assert isinstance(client, TranslationModelClient)
    assert isinstance(client, StructuredTranslationModelClient)


@pytest.mark.asyncio
async def test_litellm_adapter_maps_messages_and_response(fake_litellm):
    client = LiteLLMModelClient("gemini/gemini-2.5-flash")

    response = await client.complete("system", "source", temperature=0.2)

    assert response.content == "translated"
    assert response.finish_reason == "stop"
    fake_litellm.acompletion.assert_awaited_once_with(
        model="gemini/gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "system"},
            {"role": "user", "content": "source"},
        ],
        drop_params=True,
        temperature=0.2,
    )


@pytest.mark.asyncio
async def test_litellm_adapter_forwards_credentials_and_token_limit(fake_litellm):
    client = LiteLLMModelClient(
        "ollama/llama3.1",
        api_key="test-key",
        api_base="http://localhost:11434",
        max_output_tokens=4096,
    )

    await client.complete("", "source")

    kwargs = fake_litellm.acompletion.await_args.kwargs
    assert kwargs["messages"] == [{"role": "user", "content": "source"}]
    assert kwargs["api_key"] == "test-key"
    assert kwargs["api_base"] == "http://localhost:11434"
    assert kwargs["max_tokens"] == 4096
    assert "temperature" not in kwargs


@pytest.mark.asyncio
async def test_litellm_adapter_omits_unset_credentials(fake_litellm):
    await LiteLLMModelClient("gpt-4.1-mini", api_key="", api_base="").complete(
        "system", "source"
    )

    kwargs = fake_litellm.acompletion.await_args.kwargs
    assert "api_key" not in kwargs
    assert "api_base" not in kwargs
    assert "max_tokens" not in kwargs


@pytest.mark.asyncio
async def test_litellm_adapter_returns_structured_response(fake_litellm):
    fake_litellm.acompletion.return_value = _litellm_response(
        '{"translations": ["안녕하세요", "세계"]}'
    )
    client = LiteLLMModelClient("gpt-4.1-mini")

    response = await client.complete_structured(
        "system",
        "source",
        TranslationResponse,
    )

    assert response == TranslationResponse(translations=["안녕하세요", "세계"])
    kwargs = fake_litellm.acompletion.await_args.kwargs
    assert kwargs["response_format"] is TranslationResponse
    assert kwargs["drop_params"] is True


@pytest.mark.asyncio
async def test_litellm_adapter_rejects_empty_structured_response(fake_litellm):
    fake_litellm.acompletion.return_value = _litellm_response(None)

    with pytest.raises(TypeError, match="TranslationResponse"):
        await LiteLLMModelClient("gpt-4.1-mini").complete_structured(
            "system",
            "source",
            TranslationResponse,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "content",
    ["Here are the translations: hello, world", '{"unexpected": ["hello"]}'],
)
async def test_litellm_adapter_explains_unparseable_structured_response(
    fake_litellm, content
):
    fake_litellm.acompletion.return_value = _litellm_response(content)

    with pytest.raises(TypeError, match="may not support structured output") as info:
        await LiteLLMModelClient("ollama/llama3.1").complete_structured(
            "system",
            "source",
            TranslationResponse,
        )

    assert "TranslationResponse" in str(info.value)
    assert "ollama/llama3.1" in str(info.value)


@pytest.mark.asyncio
async def test_litellm_adapter_reports_missing_choices_as_length(fake_litellm):
    fake_litellm.acompletion.return_value = SimpleNamespace(choices=[])

    response = await LiteLLMModelClient("gpt-4.1-mini").complete("system", "source")

    assert response.content == ""
    assert response.finish_reason == "length"


@pytest.mark.asyncio
async def test_litellm_truncated_translation_raises(tmp_path, fake_litellm):
    fake_litellm.acompletion.return_value = _litellm_response(
        "partial", finish_reason="length"
    )
    translator = ModelClientMarkdownTranslator(
        root_dir=tmp_path,
        model_client=LiteLLMModelClient("gpt-4.1-mini"),
    )

    with pytest.raises(TranslationIncompleteError, match="length"):
        await translator._run_prompt(f"system{SPLIT_DELIMITER}source", 1, 1)


@pytest.mark.asyncio
async def test_litellm_adapter_explains_missing_extra(monkeypatch):
    monkeypatch.setitem(sys.modules, "litellm", None)

    with pytest.raises(ImportError, match=r"co-op-translator\[litellm\]"):
        await LiteLLMModelClient("gpt-4.1-mini").complete("system", "source")
