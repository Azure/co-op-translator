from dataclasses import dataclass
from typing import Dict, Optional
import logging
from co_op_translator.config.vision_config.provider import VisionProvider
from co_op_translator.config.vision_config.azure_computer_vision import (
    AzureComputerVisionConfig,
)

logger = logging.getLogger(__name__)


@dataclass
class VisionServiceConfig:
    """Configuration for a specific Vision service"""

    required: bool
    env_vars: Dict[str, Optional[str]]


class VisionConfig:
    """Configuration for Vision-related services."""

    @classmethod
    def get_available_provider(cls) -> Optional[VisionProvider]:
        """
        Check environment variables and return the available Vision provider.
        Currently only supports Azure Computer Vision.

        Returns:
            Optional[VisionProvider]: The available provider to use, or None if no provider is configured
        """
        for provider in VisionProvider:
            config = cls.get_service_config(provider)
            if config and all(
                value and value.strip() for value in config.env_vars.values()
            ):
                return provider
        return None

    @classmethod
    def get_service_config(
        cls, provider: VisionProvider
    ) -> Optional[VisionServiceConfig]:
        """
        Get configuration for a specific Vision service.

        Args:
            provider: Vision provider to get configuration for.

        Returns:
            Optional[VisionServiceConfig]: Service configuration if available, None if not configured
        """
        if provider == VisionProvider.AZURE_COMPUTER_VISION:
            azure_config = AzureComputerVisionConfig()
            # If any required environment variable is missing, return None
            if not azure_config.get_api_key() or not azure_config.get_endpoint():
                return None

            return VisionServiceConfig(
                required=True,
                env_vars={
                    "AZURE_AI_SERVICE_API_KEY": azure_config.get_api_key(),
                    "AZURE_AI_SERVICE_ENDPOINT": azure_config.get_endpoint(),
                },
            )
        return None

    @staticmethod
    def check_configuration() -> bool:
        """
        Check if Computer Vision service is available and properly configured.

        Returns:
            bool: True if Computer Vision is available and configured, False otherwise
        """
        return VisionConfig.get_available_provider() is not None
