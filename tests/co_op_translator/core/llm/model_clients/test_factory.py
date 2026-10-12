from unittest.mock import patch

import pytest

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_clients import (
    MODEL_CLIENT_ENV_VAR,
    AgentFrameworkModelClient,
    LiteLLMModelClient,
    ModelClientBackend,
    SemanticKernelDeprecationWarning,
    SemanticKernelModelClient,
    create_translation_model_client,
    get_model_client_backend,
)


def test_model_client_backend_defaults_to_agent_framework(monkeypatch):
    monkeypatch.delenv(MODEL_CLIENT_ENV_VAR, raising=False)

    assert get_model_client_backend() == ModelClientBackend.AGENT_FRAMEWORK


def test_model_client_backend_accepts_agent_framework_alias(monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "agent_framework")

    assert get_model_client_backend() == ModelClientBackend.AGENT_FRAMEWORK


def test_model_client_backend_rejects_unknown_value(monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "unknown")

    with pytest.raises(ValueError, match=MODEL_CLIENT_ENV_VAR):
        get_model_client_backend()


@pytest.mark.parametrize("provider", [LLMProvider.AZURE_OPENAI, LLMProvider.OPENAI])
def test_factory_creates_semantic_kernel_adapters(provider, monkeypatch):
    monkeypatch.setenv(MODEL_CLIENT_ENV_VAR, "semantic-kernel")
    config_values = _patch_provider_config(provider)
    with (
        config_values,
        pytest.warns(
            SemanticKernelDeprecationWarning,
            match="deprecated.*0.22.0.*optional dependency.*0.23.0.*removal.*0.24.0",
        ),
    ):
        client = create_translation_model_client(provider)

    assert isinstance(client, SemanticKernelModelClient)


# LiteLLM uses its own SDK client; every other provider, including ones added
# later, must default to the Agent Framework backend.
AGENT_FRAMEWORK_PROVIDERS = [
    provider for provider in LLMProvider if provider is not LLMProvider.LITELLM
]


@pytest.mark.parametrize("provider", AGENT_FRAMEWORK_PROVIDERS)
def test_factory_defaults_to_agent_framework_adapters(provider, monkeypatch):
    monkeypatch.delenv(MODEL_CLIENT_ENV_VAR, raising=False)
    config_values = _patch_provider_config(provider)
    with config_values:
        client = create_translation_model_client(provider)

    assert isinstance(client, AgentFrameworkModelClient)


def test_anthropic_rejects_semantic_kernel_backend():
    with (
        pytest.warns(SemanticKernelDeprecationWarning),
        pytest.raises(ValueError, match="Agent Framework"),
    ):
        create_translation_model_client(
            LLMProvider.ANTHROPIC,
            backend=ModelClientBackend.SEMANTIC_KERNEL,
        )


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
        org_id="org-test",
        base_url="https://gateway.example/v1",
    )


def test_agent_framework_anthropic_client_uses_claude_configuration():
    with (
        _patch_provider_config(LLMProvider.ANTHROPIC),
        patch("agent_framework_anthropic.AnthropicClient") as client_constructor,
    ):
        create_translation_model_client(
            LLMProvider.ANTHROPIC,
            backend=ModelClientBackend.AGENT_FRAMEWORK,
        )

    client_constructor.assert_called_once_with(
        model="claude-test",
        api_key="test-key",
        base_url="https://api.anthropic.test",
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
    if provider == LLMProvider.OPENAI:
        return patch.multiple(
            "co_op_translator.core.llm.model_clients.factory.OpenAIConfig",
            get_chat_model_id=lambda: "gpt-4o-mini",
            get_org_id=lambda: "org-test",
            get_api_key=lambda: "test-key",
            get_base_url=lambda: "https://gateway.example/v1",
        )
    return patch.multiple(
        "co_op_translator.core.llm.model_clients.factory.AnthropicConfig",
        get_model=lambda: "claude-test",
        get_api_key=lambda: "test-key",
        get_base_url=lambda: "https://api.anthropic.test",
        get_max_tokens=lambda: 4321,
    )


def test_agent_framework_anthropic_client_sets_output_token_limit():
    with (
        _patch_provider_config(LLMProvider.ANTHROPIC),
        patch("agent_framework_anthropic.AnthropicClient"),
    ):
        client = create_translation_model_client(
            LLMProvider.ANTHROPIC,
            backend=ModelClientBackend.AGENT_FRAMEWORK,
        )

    assert isinstance(client, AgentFrameworkModelClient)
    assert client._max_output_tokens == 4321


def _patch_litellm_config(**overrides):
    values = {
        "get_model": lambda: "gemini/gemini-2.5-flash",
        "get_api_key": lambda: None,
        "get_api_base": lambda: None,
        "get_max_tokens": lambda: None,
        **overrides,
    }
    return patch.multiple(
        "co_op_translator.core.llm.model_clients.factory.LiteLLMConfig",
        **values,
    )


def test_factory_creates_litellm_client_from_configuration(monkeypatch):
    monkeypatch.delenv(MODEL_CLIENT_ENV_VAR, raising=False)
    with _patch_litellm_config(
        get_api_key=lambda: "test-key",
        get_api_base=lambda: "http://localhost:11434",
        get_max_tokens=lambda: 4096,
    ):
        client = create_translation_model_client(LLMProvider.LITELLM)

    assert isinstance(client, LiteLLMModelClient)
    assert client._model == "gemini/gemini-2.5-flash"
    assert client._api_key == "test-key"
    assert client._api_base == "http://localhost:11434"
    assert client._max_output_tokens == 4096


@pytest.mark.parametrize("backend", list(ModelClientBackend))
def test_litellm_ignores_model_client_backend_setting(backend, recwarn):
    with _patch_litellm_config():
        client = create_translation_model_client(LLMProvider.LITELLM, backend=backend)

    assert isinstance(client, LiteLLMModelClient)
    assert not [
        warning
        for warning in recwarn
        if issubclass(warning.category, SemanticKernelDeprecationWarning)
    ]
