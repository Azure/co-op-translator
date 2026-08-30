from __future__ import annotations

from typing import Any

from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)
from semantic_kernel.contents.chat_history import ChatHistory

from co_op_translator.core.llm.model_clients.protocol import ModelResponse


class SemanticKernelModelClient:
    """Adapt a Semantic Kernel chat service to ``TranslationModelClient``."""

    def __init__(
        self,
        service: ChatCompletionClientBase,
        settings: Any,
    ) -> None:
        self._service = service
        self._settings = settings

    async def complete(
        self,
        system_prompt: str,
        user_content: str,
        *,
        temperature: float | None = None,
    ) -> ModelResponse:
        chat = ChatHistory()
        if system_prompt:
            chat.add_system_message(system_prompt)
        chat.add_user_message(user_content)

        settings = self._settings
        if temperature is not None and hasattr(settings, "model_copy"):
            settings = settings.model_copy(update={"temperature": temperature})

        result_contents = await self._service.get_chat_message_contents(
            chat_history=chat,
            settings=settings,
        )
        if not result_contents:
            return ModelResponse(content="", finish_reason="length")

        result = result_contents[0]
        content = str(result.content) if result.content else ""
        finish_reason = _normalize_finish_reason(getattr(result, "finish_reason", None))
        return ModelResponse(
            content=content,
            finish_reason=finish_reason,
            raw_response=result,
        )


def _normalize_finish_reason(value: Any) -> str | None:
    if value is None:
        return None
    normalized = getattr(value, "value", value)
    return str(normalized) if normalized is not None else None
