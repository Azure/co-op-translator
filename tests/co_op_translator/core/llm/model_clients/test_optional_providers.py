import json
from unittest.mock import AsyncMock

import pytest
from agent_framework import ChatResponse, Message
from agent_framework.openai import OpenAIChatCompletionClient
from anthropic import AsyncAnthropic
from agent_framework_anthropic import AnthropicClient
from agent_framework_ollama import OllamaChatClient
from httpx import AsyncClient, MockTransport, Request, Response
from openai import AsyncOpenAI

from co_op_translator.core.llm.model_clients import AgentFrameworkModelClient
from co_op_translator.utils.llm.text_utils import TranslationResponse


def _openai_response(content, *, finish_reason="stop"):
    return Response(
        200,
        json={
            "id": "chatcmpl_test",
            "object": "chat.completion",
            "created": 0,
            "model": "gpt-test",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": content,
                        "refusal": None,
                        "annotations": [],
                    },
                    "finish_reason": finish_reason,
                    "logprobs": None,
                }
            ],
            "usage": {
                "prompt_tokens": 1,
                "completion_tokens": 1,
                "total_tokens": 2,
            },
        },
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("finish_reason", ["stop", "length"])
async def test_agent_framework_adapter_completes_through_openai_connector(
    finish_reason,
):
    def respond(request: Request) -> Response:
        assert request.url.path == "/v1/chat/completions"
        payload = json.loads(request.content)
        assert payload["model"] == "gpt-test"
        assert payload["messages"] == [
            {"role": "system", "content": "system"},
            {"role": "user", "content": "source"},
        ]
        return _openai_response("translated", finish_reason=finish_reason)

    http_client = AsyncClient(transport=MockTransport(respond))
    openai_client = AsyncOpenAI(api_key="test-key", http_client=http_client)
    client = OpenAIChatCompletionClient(
        async_client=openai_client,
        model="gpt-test",
    )

    try:
        response = await AgentFrameworkModelClient(client).complete(
            "system",
            "source",
        )
    finally:
        await openai_client.close()

    assert response.content == "translated"
    assert response.finish_reason == finish_reason


@pytest.mark.asyncio
async def test_openai_connector_supports_structured_translation_output():
    def respond(request: Request) -> Response:
        payload = json.loads(request.content)
        assert payload["response_format"]["type"] == "json_schema"
        assert (
            "translations"
            in payload["response_format"]["json_schema"]["schema"]["properties"]
        )
        return _openai_response('{"translations":["번역"]}')

    http_client = AsyncClient(transport=MockTransport(respond))
    openai_client = AsyncOpenAI(api_key="test-key", http_client=http_client)
    client = OpenAIChatCompletionClient(
        async_client=openai_client,
        model="gpt-test",
    )

    try:
        response = await AgentFrameworkModelClient(client).complete_structured(
            "system",
            "source",
            TranslationResponse,
        )
    finally:
        await openai_client.close()

    assert response == TranslationResponse(translations=["번역"])


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client",
    [
        OllamaChatClient(host="http://localhost:11434", model="test-model"),
    ],
    ids=["ollama"],
)
async def test_agent_framework_adapter_accepts_optional_provider_clients(client):
    client.get_response = AsyncMock(
        return_value=ChatResponse(
            messages=Message("assistant", ["translated"]),
            finish_reason="stop",
        )
    )
    adapter = AgentFrameworkModelClient(client)

    response = await adapter.complete("system", "source")

    assert response.content == "translated"
    client.get_response.assert_awaited_once()


@pytest.mark.asyncio
async def test_agent_framework_adapter_completes_through_anthropic_connector():
    def respond(request: Request) -> Response:
        assert request.url.path == "/v1/messages"
        return Response(
            200,
            json={
                "id": "msg_test",
                "type": "message",
                "role": "assistant",
                "model": "claude-test",
                "content": [{"type": "text", "text": "translated"}],
                "stop_reason": "end_turn",
                "stop_sequence": None,
                "usage": {"input_tokens": 1, "output_tokens": 1},
            },
        )

    http_client = AsyncClient(transport=MockTransport(respond))
    anthropic_client = AsyncAnthropic(api_key="test-key", http_client=http_client)
    client = AnthropicClient(
        anthropic_client=anthropic_client,
        model="claude-test",
    )

    try:
        response = await AgentFrameworkModelClient(client).complete(
            "system",
            "source",
        )
    finally:
        await anthropic_client.close()

    assert response.content == "translated"
    assert response.finish_reason == "stop"


@pytest.mark.asyncio
async def test_anthropic_connector_supports_structured_translation_output():
    def respond(request: Request) -> Response:
        payload = json.loads(request.content)
        assert payload["output_config"]["format"]["type"] == "json_schema"
        assert (
            "translations" in payload["output_config"]["format"]["schema"]["properties"]
        )
        return Response(
            200,
            json={
                "id": "msg_structured",
                "type": "message",
                "role": "assistant",
                "model": "claude-test",
                "content": [{"type": "text", "text": '{"translations":["번역"]}'}],
                "stop_reason": "end_turn",
                "stop_sequence": None,
                "usage": {"input_tokens": 1, "output_tokens": 1},
            },
        )

    http_client = AsyncClient(transport=MockTransport(respond))
    anthropic_client = AsyncAnthropic(api_key="test-key", http_client=http_client)
    client = AnthropicClient(
        anthropic_client=anthropic_client,
        model="claude-test",
    )

    try:
        response = await AgentFrameworkModelClient(client).complete_structured(
            "system",
            "source",
            TranslationResponse,
        )
    finally:
        await anthropic_client.close()

    assert response == TranslationResponse(translations=["번역"])
