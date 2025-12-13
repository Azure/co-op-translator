import os
from dotenv import load_dotenv

from co_op_translator.utils.common.env_set_utils import get_active_env_set, get_env_sets

# Load environment variables from .env file
load_dotenv()


class OpenAIConfig:
    """OpenAI specific configuration."""

    _GROUP = "openai"
    _REQUIRED = (
        "OPENAI_API_KEY",
        "OPENAI_CHAT_MODEL_ID",
    )
    _OPTIONAL = (
        "OPENAI_ORG_ID",
        "OPENAI_BASE_URL",
    )
    _DEFAULTS = {
        "OPENAI_BASE_URL": "https://api.openai.com/v1",
    }

    @staticmethod
    def get_env_sets():
        return get_env_sets(
            group=OpenAIConfig._GROUP,
            required=OpenAIConfig._REQUIRED,
            optional=OpenAIConfig._OPTIONAL,
            defaults=OpenAIConfig._DEFAULTS,
        )

    @staticmethod
    def get_active_env_set():
        return get_active_env_set(
            group=OpenAIConfig._GROUP,
            required=OpenAIConfig._REQUIRED,
            optional=OpenAIConfig._OPTIONAL,
            defaults=OpenAIConfig._DEFAULTS,
        )

    @staticmethod
    def get_api_key():
        """Retrieve the OpenAI API key from environment variables."""
        env_set = OpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("OPENAI_API_KEY")

    @staticmethod
    def get_org_id():
        """Retrieve the OpenAI organization ID from environment variables."""
        env_set = OpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("OPENAI_ORG_ID")

    @staticmethod
    def get_chat_model_id():
        """Retrieve the OpenAI chat model ID from environment variables."""
        env_set = OpenAIConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("OPENAI_CHAT_MODEL_ID")

    @staticmethod
    def get_api_version():
        """Retrieve the OpenAI API version from environment variables."""
        return os.getenv("OPENAI_API_VERSION")

    @staticmethod
    def get_base_url():
        """Retrieve the OpenAI base URL from environment variables or return default."""
        env_set = OpenAIConfig.get_active_env_set()
        if env_set is None:
            return OpenAIConfig._DEFAULTS["OPENAI_BASE_URL"]
        return env_set.values.get("OPENAI_BASE_URL", OpenAIConfig._DEFAULTS["OPENAI_BASE_URL"])
