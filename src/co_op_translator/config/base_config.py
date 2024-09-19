import os
from dotenv import load_dotenv

load_dotenv()

# Base configuration class with common settings for all environments
class Config:
    AZURE_SUBSCRIPTION_KEY = os.getenv("AZURE_SUBSCRIPTION_KEY")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL_NAME")
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_AI_SERVICE_ENDPOINT = os.getenv("AZURE_AI_SERVICE_ENDPOINT")

    @staticmethod
    def check_configuration():
        missing_keys = []
        if not Config.AZURE_SUBSCRIPTION_KEY:
            missing_keys.append("AZURE_SUBSCRIPTION_KEY")
        if not Config.AZURE_OPENAI_API_KEY:
            missing_keys.append("AZURE_OPENAI_API_KEY")
        if not Config.AZURE_OPENAI_ENDPOINT:
            missing_keys.append("AZURE_OPENAI_ENDPOINT")
        if not Config.AZURE_OPENAI_MODEL_NAME:
            missing_keys.append("AZURE_OPENAI_MODEL_NAME")
        if not Config.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME:
            missing_keys.append("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
        if not Config.AZURE_OPENAI_API_VERSION:
            missing_keys.append("AZURE_OPENAI_API_VERSION")
        if not Config.AZURE_AI_SERVICE_ENDPOINT:
            missing_keys.append("AZURE_AI_SERVICE_ENDPOINT")

        if missing_keys:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_keys)}")

# Check the configuration
Config.check_configuration()