import logging
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.config.vision_config.azure_computer_vision import (
    AzureAIVisionConfig,
)
from co_op_translator.utils.common.env_set_utils import run_with_env_set_fallback

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

    def extract_line_bounding_boxes(self, image_path):
        env_sets = AzureAIVisionConfig.get_env_sets()
        if not env_sets:
            return super().extract_line_bounding_boxes(image_path)

        def _call_once():
            return super(AzureImageTranslator, self).extract_line_bounding_boxes(
                image_path
            )

        return run_with_env_set_fallback(
            env_sets=env_sets,
            group=AzureAIVisionConfig._GROUP,
            op_name="Azure AI Vision READ",
            fn=_call_once,
        )
