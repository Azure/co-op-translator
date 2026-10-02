from __future__ import annotations

from typing import Any, Awaitable, TypeVar, cast

from agent_framework import BaseChatClient, ChatResponse, Message
from pydantic import BaseModel

from co_op_translator.core.llm.model_clients.protocol import ModelResponse

StructuredResponseT = TypeVar("StructuredResponseT", bound=BaseModel)


class AgentFrameworkModelClient:
    """Adapt a Microsoft Agent Framework chat client to the translation boundary."""

    def __init__(
        self,
        client: BaseChatClient[Any],
        *,
        max_output_tokens: int | None = None,
    ) -> None:
        self._client = client
        self._max_output_tokens = max_output_tokens

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
        if self._max_output_tokens is not None:
            options["max_tokens"] = self._max_output_tokens

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

    async def complete_structured(
        self,
        system_prompt: str,
        user_content: str,
        response_format: type[StructuredResponseT],
        *,
        temperature: float | None = None,
    ) -> StructuredResponseT:
        """Complete a prompt using Agent Framework structured output."""
        messages = []
        if system_prompt:
            messages.append(Message("system", [system_prompt]))
        messages.append(Message("user", [user_content]))

        options: dict[str, Any] = {"response_format": response_format}
        if temperature is not None:
            options["temperature"] = temperature
        if self._max_output_tokens is not None:
            options["max_tokens"] = self._max_output_tokens

        pending_response = self._client.get_response(messages, options=options)
        response = await cast(
            Awaitable[ChatResponse[StructuredResponseT]], pending_response
        )
        value = response.value
        if not isinstance(value, response_format):
            raise TypeError(
                f"Expected {response_format.__name__} structured response, "
                f"received {type(value).__name__}."
            )
        return value
