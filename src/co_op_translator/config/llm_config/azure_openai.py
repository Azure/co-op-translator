import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AzureOpenAIConfig:
    """Azure OpenAI specific configuration."""

    @staticmethod
    def get_api_key():
        """Retrieve the Azure OpenAI API key from environment variables."""
        return os.getenv("AZURE_OPENAI_API_KEY")

    @staticmethod
    def get_endpoint():
        """Retrieve the Azure OpenAI endpoint from environment variables."""
        return os.getenv("AZURE_OPENAI_ENDPOINT")

    @staticmethod
    def get_model_name():
        """Retrieve the Azure OpenAI model name from environment variables."""
        return os.getenv("AZURE_OPENAI_MODEL_NAME")

    @staticmethod
    def get_chat_deployment_name():
        """Retrieve the Azure OpenAI chat deployment name from environment variables."""
        return os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

    @staticmethod
    def get_api_version():
        """Retrieve the Azure OpenAI API version from environment variables."""
        return os.getenv("AZURE_OPENAI_API_VERSION")
