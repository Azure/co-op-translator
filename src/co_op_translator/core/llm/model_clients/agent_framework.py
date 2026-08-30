from __future__ import annotations

from typing import Any, Awaitable, cast

from agent_framework import BaseChatClient, ChatResponse, Message

from co_op_translator.core.llm.model_clients.protocol import ModelResponse


class AgentFrameworkModelClient:
    """Adapt a Microsoft Agent Framework chat client to the translation boundary."""

    def __init__(self, client: BaseChatClient[Any]) -> None:
        self._client = client

    async def complete(
        self,
        system_prompt: str,
        user_content: str,
        *,
        temperature: float | None = None,
    ) -> ModelResponse:
        messages = []
        if system_prompt:
            messages.append(Message("system", [system_prompt]))
        messages.append(Message("user", [user_content]))

        options: dict[str, Any] = {}
        if temperature is not None:
            options["temperature"] = temperature

        pending_response = self._client.get_response(
            messages,
            options=options or None,
        )
        response = await cast(Awaitable[ChatResponse[Any]], pending_response)
        return ModelResponse(
            content=response.text,
            finish_reason=(
                str(response.finish_reason)
                if response.finish_reason is not None
                else None
            ),
            raw_response=response,
        )
