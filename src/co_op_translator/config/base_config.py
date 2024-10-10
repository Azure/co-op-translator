import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get_azure_subscription_key():
        return os.getenv("AZURE_SUBSCRIPTION_KEY")

    @staticmethod
    def get_azure_openai_api_key():
        return os.getenv("AZURE_OPENAI_API_KEY")

    @staticmethod
    def get_azure_openai_endpoint():
        return os.getenv("AZURE_OPENAI_ENDPOINT")

    @staticmethod
    def get_azure_openai_model_name():
        return os.getenv("AZURE_OPENAI_MODEL_NAME")

    @staticmethod
    def get_azure_openai_chat_deployment_name():
        return os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

    @staticmethod
    def get_azure_openai_api_version():
        return os.getenv("AZURE_OPENAI_API_VERSION")

    @staticmethod
    def get_azure_ai_service_endpoint():
        return os.getenv("AZURE_AI_SERVICE_ENDPOINT")

    @staticmethod
    def check_configuration():
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
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_keys)}")
