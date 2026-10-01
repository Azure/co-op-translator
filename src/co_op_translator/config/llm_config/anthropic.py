from dotenv import load_dotenv

from co_op_translator.utils.common.env_set_utils import get_active_env_set, get_env_sets

# Load environment variables from .env file
load_dotenv()


class AnthropicConfig:
    """Anthropic-specific configuration for Claude models."""

    _GROUP = "anthropic"
    _REQUIRED = (
        "ANTHROPIC_API_KEY",
        "ANTHROPIC_MODEL",
    )
    _OPTIONAL = ("ANTHROPIC_BASE_URL",)

    @staticmethod
    def get_env_sets():
        return get_env_sets(
            group=AnthropicConfig._GROUP,
            required=AnthropicConfig._REQUIRED,
            optional=AnthropicConfig._OPTIONAL,
        )

    @staticmethod
    def get_active_env_set():
        return get_active_env_set(
            group=AnthropicConfig._GROUP,
            required=AnthropicConfig._REQUIRED,
            optional=AnthropicConfig._OPTIONAL,
        )

    @staticmethod
    def get_api_key():
        """Retrieve the Anthropic API key from the active environment set."""
        env_set = AnthropicConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("ANTHROPIC_API_KEY")

    @staticmethod
    def get_model():
        """Retrieve the Claude model name from the active environment set."""
        env_set = AnthropicConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("ANTHROPIC_MODEL")

    @staticmethod
    def get_base_url():
        """Retrieve an optional Anthropic-compatible API base URL."""
        env_set = AnthropicConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("ANTHROPIC_BASE_URL")
