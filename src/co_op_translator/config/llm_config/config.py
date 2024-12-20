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
        Prioritizes Azure OpenAI over OpenAI.
        
        Returns:
            LLMProvider: The available provider to use
            
        Raises:
            ValueError: If no provider is properly configured
        """
        # Try Azure OpenAI first
        config = cls.get_service_config(LLMProvider.AZURE_OPENAI)
        if all(config.env_vars.values()):
            return LLMProvider.AZURE_OPENAI
            
        # Then try OpenAI
        config = cls.get_service_config(LLMProvider.OPENAI)
        if all(config.env_vars.values()):
            return LLMProvider.OPENAI
            
        raise ValueError("No LLM provider is properly configured. Please check your environment variables.")

    @classmethod
    def get_service_config(cls, provider: LLMProvider) -> LLMServiceConfig:
        """
        Get configuration for a specific LLM service.
        
        Args:
            provider: LLM provider to get configuration for.
            
        Returns:
            LLMServiceConfig containing the service's configuration.
        """
        if provider == LLMProvider.AZURE_OPENAI:
            config = AzureOpenAIConfig()
            return LLMServiceConfig(
                required=True,
                env_vars={
                    "AZURE_OPENAI_API_KEY": config.get_api_key(),
                    "AZURE_OPENAI_ENDPOINT": config.get_endpoint(),
                    "AZURE_OPENAI_MODEL_NAME": config.get_model_name(),
                    "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": config.get_chat_deployment_name(),
                    "AZURE_OPENAI_API_VERSION": config.get_api_version(),
                }
            )
        elif provider == LLMProvider.OPENAI:
            config = OpenAIConfig()
            return LLMServiceConfig(
                required=False,
                env_vars={
                    "OPENAI_API_KEY": config.get_api_key(),
                    "OPENAI_ORG_ID": config.get_org_id(),
                    "OPENAI_CHAT_MODEL_ID": config.get_chat_model_id(),
                }
            )
        raise ValueError(f"Unknown LLM provider: {provider}")

    @classmethod
    def check_configuration(cls):
        """
        Check if all required LLM environment variables are set.
        Raises OSError if required variables are missing.
        """
        try:
            cls.get_available_provider()
        except ValueError as e:
            raise OSError(str(e))
