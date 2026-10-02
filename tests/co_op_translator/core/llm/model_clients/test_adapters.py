from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest
from agent_framework import ChatResponse, Message

from co_op_translator.core.llm.model_clients import (
    AgentFrameworkModelClient,
    ModelResponse,
    SemanticKernelModelClient,
    StructuredTranslationModelClient,
    TranslationModelClient,
)
from co_op_translator.utils.llm.text_utils import TranslationResponse


class FakeAgentFrameworkClient:
    def __init__(self) -> None:
        self.messages = []
        self.options = None

    async def get_response(self, messages, *, options=None):
        self.messages = messages
        self.options = options
        return ChatResponse(
            messages=Message("assistant", ["translated"]),
            finish_reason="stop",
        )


class FakeSettings:
    def __init__(self, temperature=None) -> None:
        self.temperature = temperature

    def model_copy(self, *, update):
        return FakeSettings(temperature=update.get("temperature"))


@pytest.mark.asyncio
async def test_agent_framework_adapter_maps_messages_and_response():
    client = FakeAgentFrameworkClient()
    adapter = AgentFrameworkModelClient(client)  # type: ignore[arg-type]

    response = await adapter.complete(
        "system rules",
        "source content",
        temperature=0.2,
    )

    assert response == ModelResponse(content="translated", finish_reason="stop")
    assert [(message.role, message.text) for message in client.messages] == [
        ("system", "system rules"),
        ("user", "source content"),
    ]
    assert client.options == {"temperature": 0.2}
    assert isinstance(adapter, TranslationModelClient)


@pytest.mark.asyncio
async def test_agent_framework_adapter_returns_structured_response():
    client = FakeAgentFrameworkClient()
    client.get_response = AsyncMock(
        return_value=ChatResponse(
            messages=Message(
                "assistant",
                ['{"translations":["번역"]}'],
            ),
            response_format=TranslationResponse,
        )
    )
    adapter = AgentFrameworkModelClient(client)  # type: ignore[arg-type]

    response = await adapter.complete_structured(
        "system rules",
        "source content",
        TranslationResponse,
    )

    assert response == TranslationResponse(translations=["번역"])
    assert client.get_response.await_args.kwargs["options"] == {
        "response_format": TranslationResponse
    }
    assert isinstance(adapter, StructuredTranslationModelClient)


@pytest.mark.asyncio
async def test_semantic_kernel_adapter_maps_messages_and_response():
    service = AsyncMock()
    service.get_chat_message_contents.return_value = [
        SimpleNamespace(content="translated", finish_reason="stop")
    ]
    adapter = SemanticKernelModelClient(service, FakeSettings())

    response = await adapter.complete(
        "system rules",
        "source content",
        temperature=0.2,
    )

    assert response == ModelResponse(content="translated", finish_reason="stop")
    call = service.get_chat_message_contents.await_args.kwargs
    assert [
        (message.role.value, str(message.content)) for message in call["chat_history"]
    ] == [
        ("system", "system rules"),
        ("user", "source content"),
    ]
    assert call["settings"].temperature == 0.2
    assert isinstance(adapter, TranslationModelClient)


@pytest.mark.asyncio
async def test_semantic_kernel_adapter_reports_empty_response_as_length():
    service = AsyncMock()
    service.get_chat_message_contents.return_value = []
    adapter = SemanticKernelModelClient(service, FakeSettings())

    response = await adapter.complete("", "source content")

    assert response.content == ""
    assert response.finish_reason == "length"


@pytest.mark.asyncio
async def test_agent_framework_adapter_applies_output_token_limit():
    client = FakeAgentFrameworkClient()
    adapter = AgentFrameworkModelClient(client, max_output_tokens=8192)  # type: ignore[arg-type]

    await adapter.complete("system rules", "source content", temperature=0.2)

    assert client.options == {"temperature": 0.2, "max_tokens": 8192}
