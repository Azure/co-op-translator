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
    _OPTIONAL = ("ANTHROPIC_BASE_URL", "ANTHROPIC_MAX_TOKENS")

    # Agent Framework's Anthropic client defaults max_tokens to 1024, which
    # truncates translations into token-dense scripts (for example Meitei Mayek
    # uses roughly 6-8x the tokens of the English source). 8192 is accepted by
    # every currently supported Claude model.
    DEFAULT_MAX_TOKENS = 8192

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
    def get_max_tokens() -> int:
        """Return the completion token budget for Claude translation requests."""
        env_set = AnthropicConfig.get_active_env_set()
        raw_value = env_set.values.get("ANTHROPIC_MAX_TOKENS") if env_set else None
        if raw_value is None or not str(raw_value).strip():
            return AnthropicConfig.DEFAULT_MAX_TOKENS
        try:
            max_tokens = int(str(raw_value).strip())
        except ValueError as exc:
            raise ValueError(
                "ANTHROPIC_MAX_TOKENS must be a positive integer."
            ) from exc
        if max_tokens <= 0:
            raise ValueError("ANTHROPIC_MAX_TOKENS must be a positive integer.")
        return max_tokens

    @staticmethod
    def get_base_url():
        """Retrieve an optional Anthropic-compatible API base URL."""
        env_set = AnthropicConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("ANTHROPIC_BASE_URL")
