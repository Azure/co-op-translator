import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class for managing environment variables.
    Provides static methods to retrieve required Azure configuration values.
    """
    
    @staticmethod
    def get_azure_subscription_key():
        """
        Retrieve the Azure subscription key from environment variables.
        """
        return os.getenv("AZURE_SUBSCRIPTION_KEY")

    @staticmethod
    def get_azure_openai_api_key():
        """
        Retrieve the Azure OpenAI API key from environment variables.
        """
        return os.getenv("AZURE_OPENAI_API_KEY")

    @staticmethod
    def get_azure_openai_endpoint():
        """
        Retrieve the Azure OpenAI endpoint from environment variables.
        """
        return os.getenv("AZURE_OPENAI_ENDPOINT")

    @staticmethod
    def get_azure_openai_model_name():
        """
        Retrieve the Azure OpenAI model name from environment variables.
        """
        return os.getenv("AZURE_OPENAI_MODEL_NAME")

    @staticmethod
    def get_azure_openai_chat_deployment_name():
        """
        Retrieve the Azure OpenAI chat deployment name from environment variables.
        """
        return os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

    @staticmethod
    def get_azure_openai_api_version():
        """
        Retrieve the Azure OpenAI API version from environment variables.
        """
        return os.getenv("AZURE_OPENAI_API_VERSION")

    @staticmethod
    def get_azure_ai_service_endpoint():
        """
        Retrieve the Azure AI service endpoint from environment variables.
        """
        return os.getenv("AZURE_AI_SERVICE_ENDPOINT")

    @staticmethod
    def check_configuration():
        """
        Checks if all required environment variables are set.
        Raises an OSError if any required environment variables are missing.
        """
        required_vars = {
            "AZURE_SUBSCRIPTION_KEY": Config.get_azure_subscription_key(),
            "AZURE_OPENAI_API_KEY": Config.get_azure_openai_api_key(),
            "AZURE_OPENAI_ENDPOINT": Config.get_azure_openai_endpoint(),
            "AZURE_OPENAI_MODEL_NAME": Config.get_azure_openai_model_name(),
            "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": Config.get_azure_openai_chat_deployment_name(),
            "AZURE_OPENAI_API_VERSION": Config.get_azure_openai_api_version(),
            "AZURE_AI_SERVICE_ENDPOINT": Config.get_azure_ai_service_endpoint(),
        }

        missing_keys = [key for key, value in required_vars.items() if not value]

        if missing_keys:
            raise OSError(f"Missing required environment variables: {', '.join(missing_keys)}")
