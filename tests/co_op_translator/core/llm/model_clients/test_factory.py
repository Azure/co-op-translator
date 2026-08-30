from unittest.mock import patch

import pytest

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_clients import (
    MODEL_CLIENT_ENV_VAR,
    AgentFrameworkModelClient,
    ModelClientBackend,
    SemanticKernelModelClient,
    create_translation_model_client,
    get_model_client_backend,
)


def test_model_client_backend_defaults_to_semantic_kernel(monkeypatch):
    monkeypatch.delenv(MODEL_CLIENT_ENV_VAR, raising=False)

    assert get_model_client_backend() == ModelClientBackend.SEMANTIC_KERNEL


def test_model_client_backend_accepts_agent_framework_alias(monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "agent_framework")

    assert get_model_client_backend() == ModelClientBackend.AGENT_FRAMEWORK


def test_model_client_backend_rejects_unknown_value(monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "unknown")

    with pytest.raises(ValueError, match=MODEL_CLIENT_ENV_VAR):
        get_model_client_backend()


@pytest.mark.parametrize("provider", list(LLMProvider))
def test_factory_creates_semantic_kernel_adapters(provider, monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "semantic-kernel")
    config_values = _patch_provider_config(provider)
    with config_values:
        client = create_translation_model_client(provider)

    assert isinstance(client, SemanticKernelModelClient)


@pytest.mark.parametrize("provider", list(LLMProvider))
def test_factory_creates_agent_framework_adapters(provider, monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "agent-framework")
    config_values = _patch_provider_config(provider)
    with config_values:
        client = create_translation_model_client(provider)

    assert isinstance(client, AgentFrameworkModelClient)


def test_agent_framework_azure_client_uses_explicit_azure_routing():
    with (
        _patch_provider_config(LLMProvider.AZURE_OPENAI),
        patch(
            "agent_framework.openai.OpenAIChatCompletionClient"
        ) as client_constructor,
    ):
        create_translation_model_client(
            LLMProvider.AZURE_OPENAI,
            backend=ModelClientBackend.AGENT_FRAMEWORK,
        )

    client_constructor.assert_called_once_with(
        model="deployment",
        api_key="test-key",
        azure_endpoint="https://example.openai.azure.com/",
        api_version="2024-12-01-preview",
    )


def test_agent_framework_openai_client_preserves_custom_base_url():
    with (
        _patch_provider_config(LLMProvider.OPENAI),
        patch(
            "agent_framework.openai.OpenAIChatCompletionClient"
        ) as client_constructor,
    ):
        create_translation_model_client(
            LLMProvider.OPENAI,
            backend=ModelClientBackend.AGENT_FRAMEWORK,
        )

    client_constructor.assert_called_once_with(
        model="gpt-4o-mini",
        api_key="test-key",
        org_id=None,
        base_url="https://api.openai.com/v1",
    )


def _patch_provider_config(provider):
    if provider == LLMProvider.AZURE_OPENAI:
        return patch.multiple(
            "co_op_translator.core.llm.model_clients.factory.AzureOpenAIConfig",
            get_chat_deployment_name=lambda: "deployment",
            get_endpoint=lambda: "https://example.openai.azure.com/",
            get_api_key=lambda: "test-key",
            get_api_version=lambda: "2024-12-01-preview",
        )
    return patch.multiple(
        "co_op_translator.core.llm.model_clients.factory.OpenAIConfig",
        get_chat_model_id=lambda: "gpt-4o-mini",
        get_org_id=lambda: None,
        get_api_key=lambda: "test-key",
        get_base_url=lambda: "https://api.openai.com/v1",
    )
