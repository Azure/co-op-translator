import os
import pytest
from unittest.mock import patch

from co_op_translator.config.base_config import Config
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.vision_config.config import VisionConfig


@pytest.fixture
def azure_openai_env_vars():
    return {
        "AZURE_OPENAI_API_KEY": "fake_openai_key",
        "AZURE_OPENAI_ENDPOINT": "https://fake-openai-endpoint.com",
        "AZURE_OPENAI_MODEL_NAME": "gpt",
        "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": "chat-deployment",
        "AZURE_OPENAI_API_VERSION": "v1",
    }


@pytest.fixture
def openai_env_vars():
    return {
        "OPENAI_API_KEY": "fake_openai_key",
        "OPENAI_CHAT_MODEL_ID": "gpt-4o",
    }


@pytest.fixture
def anthropic_env_vars():
    return {
        "ANTHROPIC_API_KEY": "fake_anthropic_key",
        "ANTHROPIC_MODEL": "claude-test",
    }


@pytest.fixture
def vision_env_vars():
    return {
        "AZURE_AI_SERVICE_API_KEY": "fake_ai_service_key",
        "AZURE_AI_SERVICE_ENDPOINT": "https://fake-ai-service-endpoint.com",
    }


def test_config_with_azure_openai_and_vision(azure_openai_env_vars, vision_env_vars):
    """Test configuration with Azure OpenAI and Vision services"""
    with patch.dict(
        os.environ, {**azure_openai_env_vars, **vision_env_vars}, clear=True
    ):
        Config.check_configuration()
        assert LLMConfig.get_available_provider() is not None
        assert VisionConfig.check_configuration() is True


def test_config_with_openai_and_vision(openai_env_vars, vision_env_vars):
    """Test configuration with OpenAI and Vision services"""
    with patch.dict(os.environ, {**openai_env_vars, **vision_env_vars}, clear=True):
        Config.check_configuration()
        assert LLMConfig.get_available_provider() is not None
        assert VisionConfig.check_configuration() is True


def test_config_with_azure_openai_only(azure_openai_env_vars):
    """Test configuration with only Azure OpenAI (markdown-only mode)"""
    with patch.dict(os.environ, azure_openai_env_vars, clear=True):
        Config.check_configuration()
        assert LLMConfig.get_available_provider() is not None
        assert VisionConfig.check_configuration() is False


def test_config_with_openai_only(openai_env_vars):
    """Test configuration with only OpenAI (markdown-only mode)"""
    with patch.dict(os.environ, openai_env_vars, clear=True):
        Config.check_configuration()
        assert LLMConfig.get_available_provider() is not None
        assert VisionConfig.check_configuration() is False


def test_config_with_anthropic_only(anthropic_env_vars):
    with patch.dict(os.environ, anthropic_env_vars, clear=True):
        Config.check_configuration()
        assert LLMConfig.get_available_provider() == LLMProvider.ANTHROPIC
        assert VisionConfig.check_configuration() is False


def test_config_with_no_llm_service():
    """Test configuration with no LLM service available"""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError) as excinfo:
            Config.check_configuration()
        assert "No LLM service is properly configured" in str(excinfo.value)


def test_config_with_partial_azure_openai():
    """Test configuration with incomplete Azure OpenAI setup"""
    partial_vars = {
        "AZURE_OPENAI_API_KEY": "fake_key",  # Other required fields are missing
        "AZURE_OPENAI_ENDPOINT": "",  # Missing required endpoint
    }
    with patch.dict(os.environ, partial_vars, clear=True):
        with pytest.raises(ValueError) as excinfo:
            Config.check_configuration()
        assert (
            "Incomplete AZURE_OPENAI configuration. Ensure all required environment variables are set."
            in str(excinfo.value)
        )


def test_config_with_partial_openai():
    """Test configuration with incomplete OpenAI setup"""
    partial_vars = {
        "OPENAI_API_KEY": "",  # Missing required API key
        "OPENAI_ORG_ID": "fake_org_id",
    }
    with patch.dict(os.environ, partial_vars, clear=True):
        with pytest.raises(ValueError) as excinfo:
            Config.check_configuration()
        assert (
            "Incomplete OpenAI configuration. The 'OPENAI_API_KEY' must be set."
            in str(excinfo.value)
        )


def test_config_with_partial_anthropic():
    with patch.dict(
        os.environ,
        {"ANTHROPIC_API_KEY": "fake_key"},
        clear=True,
    ):
        with pytest.raises(ValueError, match="ANTHROPIC_MODEL"):
            Config.check_configuration()


def test_anthropic_connectivity_uses_configured_model(anthropic_env_vars):
    with (
        patch.dict(os.environ, anthropic_env_vars, clear=True),
        patch("anthropic.Anthropic") as client_type,
    ):
        assert LLMConfig.validate_connectivity() is True

    client_type.assert_called_once_with(api_key="fake_anthropic_key", base_url=None)
    client_type.return_value.messages.create.assert_called_once_with(
        model="claude-test",
        max_tokens=1,
        messages=[{"role": "user", "content": "Reply OK"}],
    )


def test_get_language_codes_reads_packaged_font_mappings():
    language_codes = Config.get_language_codes()

    assert "en" in language_codes
    assert "zh-TW" in language_codes
    assert len(language_codes) == len(set(language_codes))


def test_anthropic_max_tokens_defaults_and_env_override(anthropic_env_vars):
    from co_op_translator.config.llm_config.anthropic import AnthropicConfig

    with patch.dict(os.environ, anthropic_env_vars, clear=True):
        assert AnthropicConfig.get_max_tokens() == AnthropicConfig.DEFAULT_MAX_TOKENS
        assert AnthropicConfig.DEFAULT_MAX_TOKENS == 8192

    with patch.dict(
        os.environ, {**anthropic_env_vars, "ANTHROPIC_MAX_TOKENS": "4096"}, clear=True
    ):
        assert AnthropicConfig.get_max_tokens() == 4096

    for invalid in ("lots", "0", "-1"):
        with patch.dict(
            os.environ,
            {**anthropic_env_vars, "ANTHROPIC_MAX_TOKENS": invalid},
            clear=True,
        ):
            with pytest.raises(ValueError, match="ANTHROPIC_MAX_TOKENS"):
                AnthropicConfig.get_max_tokens()


@pytest.fixture
def litellm_env_vars():
    return {"LITELLM_MODEL": "gemini/gemini-2.5-flash"}


def test_config_with_litellm_only(litellm_env_vars):
    with patch.dict(os.environ, litellm_env_vars, clear=True):
        assert Config.check_configuration() is None
        assert LLMConfig.get_available_provider() == LLMProvider.LITELLM


def test_litellm_is_detected_beside_routed_provider_keys(litellm_env_vars):
    # LiteLLM reads ANTHROPIC_API_KEY itself, so a Claude key without
    # ANTHROPIC_MODEL must not block a configured LiteLLM provider.
    with patch.dict(
        os.environ,
        {**litellm_env_vars, "ANTHROPIC_API_KEY": "fake_key"},
        clear=True,
    ):
        assert LLMConfig.get_available_provider() == LLMProvider.LITELLM


def test_complete_existing_providers_keep_precedence_over_litellm(
    openai_env_vars, litellm_env_vars
):
    with patch.dict(os.environ, {**openai_env_vars, **litellm_env_vars}, clear=True):
        assert LLMConfig.get_available_provider() == LLMProvider.OPENAI


def test_config_with_partial_litellm():
    with patch.dict(os.environ, {"LITELLM_API_KEY": "fake_key"}, clear=True):
        with pytest.raises(ValueError, match="LITELLM_MODEL"):
            Config.check_configuration()


def test_litellm_max_tokens_is_optional_and_validated(litellm_env_vars):
    from co_op_translator.config.llm_config.litellm import LiteLLMConfig

    with patch.dict(os.environ, litellm_env_vars, clear=True):
        assert LiteLLMConfig.get_max_tokens() is None

    with patch.dict(
        os.environ, {**litellm_env_vars, "LITELLM_MAX_TOKENS": "4096"}, clear=True
    ):
        assert LiteLLMConfig.get_max_tokens() == 4096

    for invalid in ("0", "-1", "many"):
        with patch.dict(
            os.environ,
            {**litellm_env_vars, "LITELLM_MAX_TOKENS": invalid},
            clear=True,
        ):
            with pytest.raises(ValueError, match="LITELLM_MAX_TOKENS"):
                LiteLLMConfig.get_max_tokens()


def _fake_litellm_module(monkeypatch, completion):
    import sys
    from types import ModuleType

    module = ModuleType("litellm")
    module.completion = completion
    monkeypatch.setitem(sys.modules, "litellm", module)
    return module


def test_litellm_connectivity_uses_configured_model(monkeypatch, litellm_env_vars):
    from unittest.mock import MagicMock

    completion = MagicMock()
    _fake_litellm_module(monkeypatch, completion)
    with patch.dict(
        os.environ,
        {**litellm_env_vars, "LITELLM_API_BASE": "http://localhost:11434"},
        clear=True,
    ):
        assert LLMConfig.validate_connectivity() is True

    completion.assert_called_once_with(
        model="gemini/gemini-2.5-flash",
        messages=[{"role": "user", "content": "Reply OK"}],
        max_tokens=16,
        drop_params=True,
        timeout=10.0,
        api_base="http://localhost:11434",
    )


def test_litellm_connectivity_is_time_bounded(monkeypatch, litellm_env_vars):
    from unittest.mock import MagicMock

    completion = MagicMock(side_effect=TimeoutError("Request timed out"))
    _fake_litellm_module(monkeypatch, completion)
    with patch.dict(os.environ, litellm_env_vars, clear=True):
        with pytest.raises(ValueError, match="timed out"):
            LLMConfig.validate_connectivity()

    assert completion.call_args.kwargs["timeout"] == 10.0


def test_litellm_connectivity_reports_provider_error(monkeypatch, litellm_env_vars):
    from unittest.mock import MagicMock

    _fake_litellm_module(
        monkeypatch, MagicMock(side_effect=RuntimeError("AuthenticationError: bad key"))
    )
    with patch.dict(os.environ, litellm_env_vars, clear=True):
        with pytest.raises(ValueError, match="AuthenticationError"):
            LLMConfig.validate_connectivity()


def test_litellm_connectivity_explains_missing_extra(monkeypatch, litellm_env_vars):
    import sys

    monkeypatch.setitem(sys.modules, "litellm", None)
    with patch.dict(os.environ, litellm_env_vars, clear=True):
        with pytest.raises(ValueError, match=r"co-op-translator\[litellm\]"):
            LLMConfig.validate_connectivity()
