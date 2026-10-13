from __future__ import annotations

from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError

from co_op_translator.core.llm.model_clients.protocol import ModelResponse

StructuredResponseT = TypeVar("StructuredResponseT", bound=BaseModel)

LITELLM_INSTALL_HINT = 'pip install "co-op-translator[litellm]"'


def _import_litellm():
    try:
        import litellm
    except ImportError as exc:
        raise ImportError(
            "The LiteLLM provider requires the optional 'litellm' package. "
            f"Install it with: {LITELLM_INSTALL_HINT}"
        ) from exc
    return litellm


class LiteLLMModelClient:
    """Adapt the LiteLLM SDK to the translation boundary.

    LiteLLM routes one ``model`` string (``gpt-4.1-mini``,
    ``gemini/gemini-2.5-flash``, ``bedrock/...``, ``ollama/...``) to the
    matching provider API and returns OpenAI-format responses.
    """

    def __init__(
        self,
        model: str,
        *,
        api_key: str | None = None,
        api_base: str | None = None,
        max_output_tokens: int | None = None,
    ) -> None:
        self._model = model
        self._api_key = api_key
        self._api_base = api_base
        self._max_output_tokens = max_output_tokens

    def _request(
        self,
        system_prompt: str,
        user_content: str,
        temperature: float | None,
    ) -> dict[str, Any]:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_content})

        # drop_params lets LiteLLM drop OpenAI parameters the routed provider
        # does not accept instead of failing the translation.
        request: dict[str, Any] = {
            "model": self._model,
            "messages": messages,
            "drop_params": True,
        }
        if temperature is not None:
            request["temperature"] = temperature
        if self._max_output_tokens is not None:
            request["max_tokens"] = self._max_output_tokens
        # Forward credentials only when set so LiteLLM can fall back to the
        # routed provider's own environment variables.
        if self._api_key:
            request["api_key"] = self._api_key
        if self._api_base:
            request["api_base"] = self._api_base
        return request

    async def complete(
        self,
        system_prompt: str,
        user_content: str,
        *,
        temperature: float | None = None,
    ) -> ModelResponse:
        litellm = _import_litellm()
        response = await litellm.acompletion(
            **self._request(system_prompt, user_content, temperature)
        )
        if not response.choices:
            return ModelResponse(content="", finish_reason="length")

        choice = response.choices[0]
        return ModelResponse(
            content=choice.message.content or "",
            finish_reason=choice.finish_reason,
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
        """Complete a prompt using LiteLLM structured output."""
        litellm = _import_litellm()
        response = await litellm.acompletion(
            **self._request(system_prompt, user_content, temperature),
            response_format=response_format,
        )
        content = response.choices[0].message.content if response.choices else None
        if not content:
            raise TypeError(
                f"Expected {response_format.__name__} structured response, "
                "received an empty LiteLLM response."
            )
        try:
            return response_format.model_validate_json(content)
        except ValidationError as exc:
            # drop_params=True silently drops response_format for providers
            # without structured output support, which surfaces here as free
            # text instead of the requested JSON schema.
            raise TypeError(
                f"Expected {response_format.__name__} structured response, but the "
                f"LiteLLM response for model '{self._model}' could not be parsed "
                "as that schema. The model may not support structured output "
                "(response_format); choose a model that does."
            ) from exc
