import logging
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.exceptions import HttpResponseError, ServiceRequestError
from azure.core.credentials import AzureKeyCredential
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.config.vision_config.azure_computer_vision import (
    AzureAIVisionConfig,
)
from co_op_translator.utils.common.env_set_utils import set_preferred_env_set

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

        last_exc = None
        for env_set in env_sets:
            set_preferred_env_set(AzureAIVisionConfig._GROUP, env_set.index)
            try:
                result = super().extract_line_bounding_boxes(image_path)
                return result
            except HttpResponseError as e:
                status_code = getattr(e, "status_code", None)
                if status_code is None and getattr(e, "response", None) is not None:
                    status_code = getattr(e.response, "status_code", None)

                last_exc = e
                if status_code in {401, 403, 408, 429, 500, 502, 503, 504}:
                    logger.warning(
                        "Azure AI Vision request failed (status=%s); trying next env set",
                        status_code,
                    )
                    continue
                raise
            except ServiceRequestError as e:
                last_exc = e
                logger.warning(
                    "Azure AI Vision request error; trying next env set: %s", str(e)
                )
                continue

        if last_exc is not None:
            raise last_exc

        return super().extract_line_bounding_boxes(image_path)
