import os


class AzureComputerVisionConfig:
    """Azure Computer Vision specific configuration."""

    @staticmethod
    def get_subscription_key():
        """Retrieve the Azure subscription key from environment variables."""
        return os.getenv("AZURE_SUBSCRIPTION_KEY")

    @staticmethod
    def get_endpoint():
        """Retrieve the Azure AI service endpoint from environment variables."""
        return os.getenv("AZURE_AI_SERVICE_ENDPOINT")
