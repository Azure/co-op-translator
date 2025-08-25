from dataclasses import dataclass
from typing import Dict, Optional
import logging
import base64
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from co_op_translator.config.vision_config.provider import VisionProvider
from co_op_translator.config.vision_config.azure_computer_vision import (
    AzureAIVisionConfig,
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
        Currently only supports Azure AI Service.

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
            azure_config = AzureAIVisionConfig()
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
        Check if Azure AI Service is available and properly configured.

        Returns:
            bool: True if Azure AI Service is available and configured, False otherwise
        """
        return VisionConfig.get_available_provider() is not None

    @staticmethod
    def validate_connectivity() -> None:
        """
        Perform a lightweight connectivity and credential validation for Azure AI Vision
        using a tiny in-memory PNG and a minimal analysis feature.

        Hard-fails on 401/403 (auth/permission). Other statuses will only warn and proceed.
        """
        provider = VisionConfig.get_available_provider()
        if provider != VisionProvider.AZURE_COMPUTER_VISION:
            return

        endpoint = AzureAIVisionConfig.get_endpoint()
        api_key = AzureAIVisionConfig.get_api_key()
        if not endpoint or not api_key:
            raise ValueError(
                "Azure AI Service configuration missing required values. Ensure AZURE_AI_SERVICE_ENDPOINT and AZURE_AI_SERVICE_API_KEY are set."
            )

        # 1x1 transparent PNG (base64)
        tiny_png_b64 = b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHJgL9oS2s2wAAAABJRU5ErkJggg=="
        image_bytes = base64.b64decode(tiny_png_b64)

        client = ImageAnalysisClient(endpoint, AzureKeyCredential(api_key))

        try:
            # Use a minimal feature such as CAPTION; if the service rejects tiny images with 4xx (not 401/403), warn and continue
            result = client.analyze(
                image_data=image_bytes, visual_features=[VisualFeatures.CAPTION]
            )
            # If SDK raises on non-2xx, this line may not be reached; otherwise treat as success
            return
        except Exception as e:
            status = getattr(e, "status_code", None)
            if status in (401, 403):
                raise ValueError(
                    "Authentication failed for Azure AI Service (Vision) (401/403). Verify AZURE_AI_SERVICE_API_KEY and endpoint permissions."
                )
            # Non-auth errors: warn and proceed
            logger.warning(
                f"Azure AI Vision health check returned non-2xx status. Proceeding (non-strict). Details: {e}"
            )
            return
