import logging
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.config.vision_config.azure_computer_vision import (
    AzureAIVisionConfig,
)

logger = logging.getLogger(__name__)


class AzureImageTranslator(ImageTranslator):
    """Implements image translation using Azure AI Vision services.

    This class provides image translation capabilities using Azure's AI Vision
    service for text extraction, combined
    with translation services to convert text within images to different languages.
    """

    def get_image_analysis_client(self):
        """Create an Azure Image Analysis Client using configured credentials.

        Retrieves endpoint and API key from AzureAIVisionConfig to establish
        a connection to the Azure AI Vision service.

        Returns:
            Configured Azure ImageAnalysisClient instance
        """
        endpoint = AzureAIVisionConfig.get_endpoint()
        subscription_key = AzureAIVisionConfig.get_api_key()
        return ImageAnalysisClient(endpoint, AzureKeyCredential(subscription_key))
