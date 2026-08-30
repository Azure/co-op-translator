from unittest.mock import AsyncMock

import pytest
from agent_framework import ChatResponse, Message
from agent_framework_anthropic import AnthropicClient
from agent_framework_ollama import OllamaChatClient

from co_op_translator.core.llm.model_clients import AgentFrameworkModelClient


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client",
    [
        AnthropicClient(api_key="test-key", model="claude-test"),
        OllamaChatClient(host="http://localhost:11434", model="test-model"),
    ],
    ids=["claude", "ollama"],
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
