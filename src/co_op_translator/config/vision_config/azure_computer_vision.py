import os


class AzureComputerVisionConfig:
    """Azure Computer Vision specific configuration."""

    @staticmethod
    def get_api_key():
        """Retrieve the Azure AI Vision API key from environment variables.

        First checks for AZURE_AI_SERVICE_API_KEY (recommended), then falls back to
        AZURE_SUBSCRIPTION_KEY for backward compatibility.
        """
        # First check new naming convention (Azure AI Vision)
        key = os.getenv("AZURE_AI_SERVICE_API_KEY")
        if key:
            return key

        # Fall back to legacy naming convention for backward compatibility
        return os.getenv("AZURE_SUBSCRIPTION_KEY")

    @staticmethod
    def get_endpoint():
        """Retrieve the Azure AI service endpoint from environment variables."""
        return os.getenv("AZURE_AI_SERVICE_ENDPOINT")
