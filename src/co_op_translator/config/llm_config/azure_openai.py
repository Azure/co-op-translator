import os
from dotenv import load_dotenv

from co_op_translator.utils.common.env_set_utils import get_active_env_set, get_env_sets

# Load environment variables from .env file
load_dotenv()


class AzureOpenAIConfig:
    """Azure OpenAI specific configuration."""

    _GROUP = "azure_openai"
    _REQUIRED = (
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_MODEL_NAME",
        "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME",
        "AZURE_OPENAI_API_VERSION",
    )

    @staticmethod
    def get_env_sets():
        return get_env_sets(group=AzureOpenAIConfig._GROUP, required=AzureOpenAIConfig._REQUIRED)

    @staticmethod
    def get_active_env_set():
        return get_active_env_set(group=AzureOpenAIConfig._GROUP, required=AzureOpenAIConfig._REQUIRED)

    @staticmethod
    def get_api_key():
        """Retrieve the Azure OpenAI API key from environment variables."""
        env_set = AzureOpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_OPENAI_API_KEY")

    @staticmethod
    def get_endpoint():
        """Retrieve the Azure OpenAI endpoint from environment variables."""
        env_set = AzureOpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_OPENAI_ENDPOINT")

    @staticmethod
    def get_model_name():
        """Retrieve the Azure OpenAI model name from environment variables."""
        env_set = AzureOpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_OPENAI_MODEL_NAME")

    @staticmethod
    def get_chat_deployment_name():
        """Retrieve the Azure OpenAI chat deployment name from environment variables."""
        env_set = AzureOpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

    @staticmethod
    def get_api_version():
        """Retrieve the Azure OpenAI API version from environment variables."""
        env_set = AzureOpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_OPENAI_API_VERSION")
