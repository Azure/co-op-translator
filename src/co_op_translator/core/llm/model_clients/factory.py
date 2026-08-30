from __future__ import annotations

from enum import Enum
import os

from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_clients.protocol import TranslationModelClient

MODEL_CLIENT_ENV_VAR = "CO_OP_TRANSLATOR_MODEL_CLIENT"


class ModelClientBackend(str, Enum):
    SEMANTIC_KERNEL = "semantic-kernel"
    AGENT_FRAMEWORK = "agent-framework"


def get_model_client_backend() -> ModelClientBackend:
    value = os.getenv(
        MODEL_CLIENT_ENV_VAR, ModelClientBackend.SEMANTIC_KERNEL.value
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
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

    kernel.add_service(service)
    settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
    return SemanticKernelModelClient(service=service, settings=settings)


def _create_agent_framework_client(
    provider: LLMProvider,
) -> TranslationModelClient:
    from agent_framework.openai import OpenAIChatCompletionClient

    from co_op_translator.core.llm.model_clients.agent_framework import (
        AgentFrameworkModelClient,
    )

    if provider == LLMProvider.AZURE_OPENAI:
        client = OpenAIChatCompletionClient(
            model=AzureOpenAIConfig.get_chat_deployment_name(),
            api_key=AzureOpenAIConfig.get_api_key(),
            azure_endpoint=AzureOpenAIConfig.get_endpoint(),
            api_version=AzureOpenAIConfig.get_api_version(),
        )
    elif provider == LLMProvider.OPENAI:
        client = OpenAIChatCompletionClient(
            model=OpenAIConfig.get_chat_model_id(),
            api_key=OpenAIConfig.get_api_key(),
            org_id=OpenAIConfig.get_org_id(),
            base_url=OpenAIConfig.get_base_url(),
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

    return AgentFrameworkModelClient(client)
