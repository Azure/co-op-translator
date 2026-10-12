from dotenv import load_dotenv

from co_op_translator.utils.common.env_set_utils import get_active_env_set, get_env_sets

# Load environment variables from .env file
load_dotenv()


class LiteLLMConfig:
    """LiteLLM SDK configuration for routing translations to any supported model."""

    _GROUP = "litellm"
    _REQUIRED = ("LITELLM_MODEL",)
    # The API key is optional: LiteLLM reads the routed provider's own variables
    # (OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, AWS_* for Bedrock, ...)
    # when LITELLM_API_KEY is unset.
    _OPTIONAL = ("LITELLM_API_KEY", "LITELLM_API_BASE", "LITELLM_MAX_TOKENS")

    @staticmethod
    def get_env_sets():
        return get_env_sets(
            group=LiteLLMConfig._GROUP,
            required=LiteLLMConfig._REQUIRED,
            optional=LiteLLMConfig._OPTIONAL,
        )

    @staticmethod
    def get_active_env_set():
        return get_active_env_set(
            group=LiteLLMConfig._GROUP,
            required=LiteLLMConfig._REQUIRED,
            optional=LiteLLMConfig._OPTIONAL,
        )

    @staticmethod
    def get_model():
        """Retrieve the LiteLLM model string, e.g. ``gemini/gemini-2.5-flash``."""
        env_set = LiteLLMConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("LITELLM_MODEL")

    @staticmethod
    def get_api_key():
        """Retrieve an optional API key passed to LiteLLM for the routed provider."""
        env_set = LiteLLMConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("LITELLM_API_KEY")

    @staticmethod
    def get_api_base():
        """Retrieve an optional API base, e.g. for Ollama or a self-hosted server."""
        env_set = LiteLLMConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("LITELLM_API_BASE")

    @staticmethod
    def get_max_tokens() -> int | None:
        """Retrieve an optional output token limit for translation requests."""
        env_set = LiteLLMConfig.get_active_env_set()
        raw_value = env_set.values.get("LITELLM_MAX_TOKENS") if env_set else None
        if raw_value is None or not str(raw_value).strip():
            return None
        try:
            max_tokens = int(str(raw_value).strip())
        except ValueError as exc:
            raise ValueError("LITELLM_MAX_TOKENS must be a positive integer.") from exc
        if max_tokens <= 0:
            raise ValueError("LITELLM_MAX_TOKENS must be a positive integer.")
        return max_tokens
