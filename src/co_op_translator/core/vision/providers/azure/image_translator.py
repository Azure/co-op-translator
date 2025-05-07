import logging
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.config.vision_config.azure_computer_vision import (
    AzureComputerVisionConfig,
)

logger = logging.getLogger(__name__)


class AzureImageTranslator(ImageTranslator):
    """Azure implementation for image translation using Computer Vision API.

    This class provides image translation capabilities using Azure's Computer Vision
    service for text extraction, combined
    with translation services to convert text within images to different languages.
    """

    def get_image_analysis_client(self):
        """
        Initialize and return an Image Analysis Client.

        Returns:
            ImageAnalysisClient: The initialized client.
        """
        endpoint = AzureComputerVisionConfig.get_endpoint()
        subscription_key = AzureComputerVisionConfig.get_api_key()
        return ImageAnalysisClient(endpoint, AzureKeyCredential(subscription_key))
