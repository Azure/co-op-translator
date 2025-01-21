import os
import pytest
from unittest.mock import patch

from co_op_translator.config.base_config import Config
from co_op_translator.config.llm_config.config import LLMConfig
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
    return {"OPENAI_API_KEY": "fake_openai_key"}


@pytest.fixture
def vision_env_vars():
    return {
        "AZURE_SUBSCRIPTION_KEY": "fake_subscription_key",
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
