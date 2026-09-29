from __future__ import annotations

from enum import Enum
import os
import warnings

from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.anthropic import AnthropicConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_clients.protocol import TranslationModelClient

MODEL_CLIENT_ENV_VAR = "CO_OP_TRANSLATOR_MODEL_CLIENT"


class SemanticKernelDeprecationWarning(FutureWarning):
    """Warn that the Semantic Kernel model client is being phased out."""


class ModelClientBackend(str, Enum):
    SEMANTIC_KERNEL = "semantic-kernel"
    AGENT_FRAMEWORK = "agent-framework"


def get_model_client_backend() -> ModelClientBackend:
    value = os.getenv(
        MODEL_CLIENT_ENV_VAR, ModelClientBackend.AGENT_FRAMEWORK.value
    ).strip()
    normalized = value.lower().replace("_", "-")
    try:
        return ModelClientBackend(normalized)
    except ValueError as exc:
        supported = ", ".join(backend.value for backend in ModelClientBackend)
        raise ValueError(
            f"Unsupported {MODEL_CLIENT_ENV_VAR} value '{value}'. "
            f"Expected one of: {supported}."
        ) from exc


def create_translation_model_client(
    provider: LLMProvider,
    *,
    backend: ModelClientBackend | None = None,
) -> TranslationModelClient:
    selected_backend = backend or get_model_client_backend()
    if selected_backend == ModelClientBackend.SEMANTIC_KERNEL:
        warnings.warn(
            "The Semantic Kernel model client is deprecated in Co-op Translator "
            "0.22.0. It will become an optional dependency in 0.23.0 and is "
            "planned for removal in 0.24.0. Unset "
            f"{MODEL_CLIENT_ENV_VAR} or set it to "
            f"'{ModelClientBackend.AGENT_FRAMEWORK.value}'.",
            SemanticKernelDeprecationWarning,
            stacklevel=2,
        )
        return _create_semantic_kernel_client(provider)
    return _create_agent_framework_client(provider)


def _create_semantic_kernel_client(
    provider: LLMProvider,
) -> TranslationModelClient:
    from semantic_kernel import Kernel
    from semantic_kernel.connectors.ai.open_ai import (
        AzureChatCompletion,
        OpenAIChatCompletion,
    )

    from co_op_translator.core.llm.model_clients.semantic_kernel import (
        SemanticKernelModelClient,
    )

    service_id = provider.value
    kernel = Kernel()
    if provider == LLMProvider.AZURE_OPENAI:
        service = AzureChatCompletion(
            service_id=service_id,
            deployment_name=AzureOpenAIConfig.get_chat_deployment_name(),
            endpoint=AzureOpenAIConfig.get_endpoint(),
            api_key=AzureOpenAIConfig.get_api_key(),
            api_version=AzureOpenAIConfig.get_api_version(),
        )
    elif provider == LLMProvider.OPENAI:
        service = OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id=OpenAIConfig.get_chat_model_id(),
            org_id=OpenAIConfig.get_org_id(),
            api_key=OpenAIConfig.get_api_key(),
        )
    elif provider == LLMProvider.ANTHROPIC:
        raise ValueError(
            "Anthropic is available through the Agent Framework model client. "
            f"Unset {MODEL_CLIENT_ENV_VAR} or set it to "
            f"'{ModelClientBackend.AGENT_FRAMEWORK.value}'."
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

    kernel.add_service(service)
    settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
    return SemanticKernelModelClient(service=service, settings=settings)


def _create_agent_framework_client(
    provider: LLMProvider,
) -> TranslationModelClient:
    from co_op_translator.core.llm.model_clients.agent_framework import (
        AgentFrameworkModelClient,
    )

    if provider == LLMProvider.AZURE_OPENAI:
        from agent_framework.openai import OpenAIChatCompletionClient

        client = OpenAIChatCompletionClient(
            model=AzureOpenAIConfig.get_chat_deployment_name(),
            api_key=AzureOpenAIConfig.get_api_key(),
            azure_endpoint=AzureOpenAIConfig.get_endpoint(),
            api_version=AzureOpenAIConfig.get_api_version(),
        )
    elif provider == LLMProvider.OPENAI:
        from agent_framework.openai import OpenAIChatCompletionClient

        client = OpenAIChatCompletionClient(
            model=OpenAIConfig.get_chat_model_id(),
            api_key=OpenAIConfig.get_api_key(),
            org_id=OpenAIConfig.get_org_id(),
            base_url=OpenAIConfig.get_base_url(),
        )
    elif provider == LLMProvider.ANTHROPIC:
        from agent_framework_anthropic import AnthropicClient

        client = AnthropicClient(
            model=AnthropicConfig.get_model(),
            api_key=AnthropicConfig.get_api_key(),
            base_url=AnthropicConfig.get_base_url(),
        )
        return AgentFrameworkModelClient(
            client, max_output_tokens=AnthropicConfig.get_max_tokens()
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

    return AgentFrameworkModelClient(client)
