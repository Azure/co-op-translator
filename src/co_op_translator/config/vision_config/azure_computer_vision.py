import os

from co_op_translator.utils.common.env_set_utils import get_active_env_set, get_env_sets


class AzureAIVisionConfig:
    """Azure AI Service specific configuration."""

    _GROUP = "azure_ai_service"
    _REQUIRED = (
        "AZURE_AI_SERVICE_API_KEY",
        "AZURE_AI_SERVICE_ENDPOINT",
    )

    @staticmethod
    def get_env_sets():
        return get_env_sets(group=AzureAIVisionConfig._GROUP, required=AzureAIVisionConfig._REQUIRED)

    @staticmethod
    def get_active_env_set():
        return get_active_env_set(
            group=AzureAIVisionConfig._GROUP,
            required=AzureAIVisionConfig._REQUIRED,
        )

    @staticmethod
    def get_api_key():
        """Retrieve the Azure AI Service API key from environment variables.

        First checks for AZURE_AI_SERVICE_API_KEY (recommended), then checks numbered
        variants like AZURE_AI_SERVICE_API_KEY_1.
        """
        env_set = AzureAIVisionConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_AI_SERVICE_API_KEY")

    @staticmethod
    def get_endpoint():
        """Retrieve the Azure AI service endpoint from environment variables."""
        env_set = AzureAIVisionConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_AI_SERVICE_ENDPOINT")
