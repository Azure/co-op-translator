import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class OpenAIConfig:
    """OpenAI specific configuration."""

    @staticmethod
    def get_api_key():
        """Retrieve the OpenAI API key from environment variables."""
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_org_id():
        """Retrieve the OpenAI organization ID from environment variables."""
        return os.getenv("OPENAI_ORG_ID")

    @staticmethod
    def get_chat_model_id():
        """Retrieve the OpenAI chat model ID from environment variables."""
        return os.getenv("OPENAI_CHAT_MODEL_ID")

    @staticmethod
    def get_api_version():
        """Retrieve the OpenAI API version from environment variables."""
        return os.getenv("OPENAI_API_VERSION")

    @staticmethod
    def get_base_url():
        """Retrieve the OpenAI base URL from environment variables or return default."""
        return os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
