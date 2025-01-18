from dataclasses import dataclass
from typing import Dict, Optional
import logging
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig

logger = logging.getLogger(__name__)

@dataclass
class LLMServiceConfig:
    """Configuration for a specific LLM service"""
    required: bool
    env_vars: Dict[str, Optional[str]]

class LLMConfig:
    """Configuration for LLM-related services."""

    @classmethod
    def get_available_provider(cls) -> LLMProvider:
        """
        Check environment variables and return the available LLM provider.
        Currently supports Azure OpenAI and OpenAI.
        
        Returns:
            LLMProvider: The available provider to use
            
        Raises:
            ValueError: If no provider is properly configured
        """
        # Check Azure OpenAI first
        config = cls.get_service_config(LLMProvider.AZURE_OPENAI)
        if config and all(value and value.strip() for value in config.env_vars.values()):
            return LLMProvider.AZURE_OPENAI
        
        # Check OpenAI next
        config = cls.get_service_config(LLMProvider.OPENAI)
        if config and all(value and value.strip() for value in config.env_vars.values()):
            return LLMProvider.OPENAI
        
        raise ValueError("No LLM service is properly configured")

    @classmethod
    def get_service_config(cls, provider: LLMProvider) -> LLMServiceConfig:
        """
        Get configuration for a specific LLM service.
        
        Args:
            provider: LLM provider to get configuration for.
            
        Returns:
            LLMServiceConfig: Service configuration
        """
        if provider == LLMProvider.AZURE_OPENAI:
            azure_config = AzureOpenAIConfig()
            return LLMServiceConfig(
                required=True,
                env_vars={
                    "AZURE_OPENAI_API_KEY": azure_config.get_api_key(),
                    "AZURE_OPENAI_ENDPOINT": azure_config.get_endpoint(),
                    "AZURE_OPENAI_MODEL_NAME": azure_config.get_model_name(),
                    "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": azure_config.get_chat_deployment_name(),
                    "AZURE_OPENAI_API_VERSION": azure_config.get_api_version(),
                }
            )
        elif provider == LLMProvider.OPENAI:
            openai_config = OpenAIConfig()
            api_key = openai_config.get_api_key()
            if api_key:
                return LLMServiceConfig(
                    required=True,
                    env_vars={"OPENAI_API_KEY": api_key}
                )
        return None

    @classmethod
    def check_configuration(cls):
        """
        Check if all required LLM environment variables are set.
        Raises ValueError if no LLM service is properly configured.
        """
        try:
            cls.get_available_provider()
        except ValueError as e:
            raise ValueError("No LLM service is properly configured") from e
