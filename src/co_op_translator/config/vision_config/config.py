from dataclasses import dataclass
from typing import Dict, Optional
import logging
from co_op_translator.config.vision_config.provider import VisionProvider
from co_op_translator.config.vision_config.azure_computer_vision import AzureComputerVisionConfig

logger = logging.getLogger(__name__)

@dataclass
class VisionServiceConfig:
    """Configuration for a specific Vision service"""
    required: bool
    env_vars: Dict[str, Optional[str]]

class VisionConfig:
    """Configuration for Vision-related services."""
    
    @classmethod
    def get_available_provider(cls) -> VisionProvider:
        """
        Check environment variables and return the available Vision provider.
        Currently only supports Azure Computer Vision.
        
        Returns:
            VisionProvider: The available provider to use
            
        Raises:
            ValueError: If no provider is properly configured
        """
        config = cls.get_service_config(VisionProvider.AZURE_COMPUTER_VISION)
        if all(config.env_vars.values()):
            return VisionProvider.AZURE_COMPUTER_VISION
            
        raise ValueError("No Vision provider is properly configured. Please check your environment variables.")

    @classmethod
    def get_service_config(cls, provider: VisionProvider) -> VisionServiceConfig:
        """
        Get configuration for a specific Vision service.
        
        Args:
            provider: Vision provider to get configuration for.
            
        Returns:
            VisionServiceConfig containing the service's configuration.
        """
        if provider == VisionProvider.AZURE_COMPUTER_VISION:
            azure_config = AzureComputerVisionConfig()
            return VisionServiceConfig(
                required=True,
                env_vars={
                    "AZURE_SUBSCRIPTION_KEY": azure_config.get_subscription_key(),
                    "AZURE_AI_SERVICE_ENDPOINT": azure_config.get_endpoint(),
                }
            )
        raise ValueError(f"Unknown Vision provider: {provider}")

    @classmethod
    def check_configuration(cls):
        """
        Check if all required Vision environment variables are set.
        Raises OSError if required variables are missing.
        """
        try:
            cls.get_available_provider()
        except ValueError as e:
            raise OSError(str(e))
