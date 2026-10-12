from dataclasses import dataclass
from typing import Dict, Optional
import logging

from ai_healthcheck import check_openai
from az_ai_healthcheck import check_azure_openai

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.llm_config.anthropic import AnthropicConfig
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.litellm import LiteLLMConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig
from co_op_translator.utils.common.env_set_utils import (
    any_env_var_present,
    set_preferred_env_set,
)

logger = logging.getLogger(__name__)


@dataclass
class LLMServiceConfig:
    """Configuration for a specific LLM service."""

    required: bool
    env_vars: Dict[str, Optional[str]]


class LLMConfig:
    """Configuration for LLM-related services."""

    _PROVIDER_CONFIG_TYPES = {
        LLMProvider.AZURE_OPENAI: AzureOpenAIConfig,
        LLMProvider.OPENAI: OpenAIConfig,
        LLMProvider.ANTHROPIC: AnthropicConfig,
        LLMProvider.LITELLM: LiteLLMConfig,
    }

    @classmethod
    def get_provider_config_type(cls, provider: LLMProvider):
        """Return the environment configuration type for a provider."""
        try:
            return cls._PROVIDER_CONFIG_TYPES[provider]
        except KeyError as exc:
            raise ValueError(f"Unsupported LLM provider: {provider}") from exc

    @classmethod
    def validate_env_vars(
        cls, env_vars: Dict[str, Optional[str]], provider: LLMProvider
    ):
        """
        Validate environment variables for a given provider.
        - For OpenAI, the API key and model ID are required.
        - For Anthropic, the API key and Claude model are required.
        - For LiteLLM, only the model is required; provider keys may come from
          the routed provider's own environment variables.
        - For Azure, all listed env_vars must be non-empty.

        Additionally, distinguish between:
        - "NO_CONFIG" if no variables are set at all.
        - "Incomplete" if some are set but not all (or required ones are missing).
        """
        if provider == LLMProvider.OPENAI:
            bases = [
                "OPENAI_API_KEY",
                "OPENAI_CHAT_MODEL_ID",
                "OPENAI_ORG_ID",
                "OPENAI_BASE_URL",
            ]
            if not any_env_var_present(bases):
                raise ValueError("NO_CONFIG_OPENAI")

            if not env_vars.get("OPENAI_API_KEY"):
                raise ValueError(
                    "Incomplete OpenAI configuration. The 'OPENAI_API_KEY' must be set."
                )

            if not env_vars.get("OPENAI_CHAT_MODEL_ID"):
                raise ValueError(
                    "Incomplete OpenAI configuration. The 'OPENAI_CHAT_MODEL_ID' must be set."
                )

        elif provider == LLMProvider.ANTHROPIC:
            bases = [
                "ANTHROPIC_API_KEY",
                "ANTHROPIC_MODEL",
                "ANTHROPIC_BASE_URL",
            ]
            if not any_env_var_present(bases):
                raise ValueError("NO_CONFIG_ANTHROPIC")

            if not env_vars.get("ANTHROPIC_API_KEY") or not env_vars.get(
                "ANTHROPIC_MODEL"
            ):
                raise ValueError(
                    "Incomplete Anthropic configuration. Ensure 'ANTHROPIC_API_KEY' "
                    "and 'ANTHROPIC_MODEL' are set."
                )

        elif provider == LLMProvider.LITELLM:
            bases = [
                "LITELLM_MODEL",
                "LITELLM_API_KEY",
                "LITELLM_API_BASE",
            ]
            if not any_env_var_present(bases):
                raise ValueError("NO_CONFIG_LITELLM")

            if not env_vars.get("LITELLM_MODEL"):
                raise ValueError(
                    "Incomplete LiteLLM configuration. The 'LITELLM_MODEL' must be set."
                )

        elif provider == LLMProvider.AZURE_OPENAI:
            bases = list(env_vars.keys())
            if not any_env_var_present(bases):
                raise ValueError("NO_CONFIG_AZURE")

            if any(v is None or not str(v).strip() for v in env_vars.values()):
                raise ValueError(
                    f"Incomplete {provider.name} configuration. Ensure all required environment variables are set."
                )

    @classmethod
    def get_service_config(cls, provider: LLMProvider) -> LLMServiceConfig:
        """
        Build env_vars for each provider, validate them, and return LLMServiceConfig if valid.
        """
        if provider == LLMProvider.AZURE_OPENAI:
            azure_config = AzureOpenAIConfig()
            env_vars = {
                "AZURE_OPENAI_API_KEY": azure_config.get_api_key(),
                "AZURE_OPENAI_ENDPOINT": azure_config.get_endpoint(),
                "AZURE_OPENAI_MODEL_NAME": azure_config.get_model_name(),
                "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": azure_config.get_chat_deployment_name(),
                "AZURE_OPENAI_API_VERSION": azure_config.get_api_version(),
            }
            cls.validate_env_vars(env_vars, provider)
            return LLMServiceConfig(required=True, env_vars=env_vars)

        elif provider == LLMProvider.OPENAI:
            openai_config = OpenAIConfig()
            env_vars = {
                "OPENAI_API_KEY": openai_config.get_api_key(),
                "OPENAI_ORG_ID": openai_config.get_org_id(),
                "OPENAI_CHAT_MODEL_ID": openai_config.get_chat_model_id(),
            }
            cls.validate_env_vars(env_vars, provider)
            return LLMServiceConfig(required=False, env_vars=env_vars)

        elif provider == LLMProvider.ANTHROPIC:
            anthropic_config = AnthropicConfig()
            env_vars = {
                "ANTHROPIC_API_KEY": anthropic_config.get_api_key(),
                "ANTHROPIC_MODEL": anthropic_config.get_model(),
                "ANTHROPIC_BASE_URL": anthropic_config.get_base_url(),
            }
            cls.validate_env_vars(env_vars, provider)
            return LLMServiceConfig(required=False, env_vars=env_vars)

        elif provider == LLMProvider.LITELLM:
            env_vars = {
                "LITELLM_MODEL": LiteLLMConfig.get_model(),
                "LITELLM_API_KEY": LiteLLMConfig.get_api_key(),
                "LITELLM_API_BASE": LiteLLMConfig.get_api_base(),
            }
            cls.validate_env_vars(env_vars, provider)
            return LLMServiceConfig(required=False, env_vars=env_vars)

        else:
            raise ValueError(
                f"Unknown LLM provider: {provider}. Expected one of: {[e.name for e in LLMProvider]}"
            )

    @classmethod
    def get_available_provider(cls) -> LLMProvider:
        """
        1) Attempt Azure. If it fails:
           - If error string contains "NO_CONFIG_AZURE", ignore it (means Azure is not set at all).
           - Otherwise, raise that error (it must be an Incomplete config).
        2) Attempt OpenAI similarly.
        3) Attempt Anthropic similarly.
        4) Attempt LiteLLM similarly.
        5) If no provider is configured, raise "No LLM service is properly configured."
        """
        azure_error = None
        try:
            cls.get_service_config(LLMProvider.AZURE_OPENAI)
            return LLMProvider.AZURE_OPENAI
        except ValueError as e:
            if "NO_CONFIG_AZURE" in str(e):
                azure_error = None  # Means Azure is not configured at all
            else:
                azure_error = e  # Incomplete or other error

        openai_error = None
        try:
            cls.get_service_config(LLMProvider.OPENAI)
            return LLMProvider.OPENAI
        except ValueError as e:
            if "NO_CONFIG_OPENAI" in str(e):
                openai_error = None  # Means OpenAI is not configured at all
            else:
                openai_error = e

        anthropic_error = None
        try:
            cls.get_service_config(LLMProvider.ANTHROPIC)
            return LLMProvider.ANTHROPIC
        except ValueError as e:
            if "NO_CONFIG_ANTHROPIC" in str(e):
                anthropic_error = None
            else:
                anthropic_error = e

        litellm_error = None
        try:
            cls.get_service_config(LLMProvider.LITELLM)
            return LLMProvider.LITELLM
        except ValueError as e:
            if "NO_CONFIG_LITELLM" in str(e):
                litellm_error = None
            else:
                litellm_error = e

        # If every provider error is None, no provider is configured at all.
        if (
            not azure_error
            and not openai_error
            and not anthropic_error
            and not litellm_error
        ):
            raise ValueError("No LLM service is properly configured")

        # Otherwise, raise the first "incomplete" error if it exists
        if azure_error:
            raise azure_error
        if openai_error:
            raise openai_error
        if anthropic_error:
            raise anthropic_error
        if litellm_error:
            raise litellm_error

        # Fallback if something unexpected happened
        raise ValueError("No LLM service is properly configured")

    @classmethod
    def check_configuration(cls):
        """
        Checks if at least one LLM provider is properly configured.
        Raises ValueError if no LLM service is properly configured.
        """
        cls.get_available_provider()

    @classmethod
    def validate_connectivity(cls) -> bool:
        """
        Perform a lightweight connectivity and credential validation for the configured LLM provider.

        - Azure OpenAI: use az-ai-healthcheck. Return True when ok; otherwise raise ValueError.
        - OpenAI: use ai-healthcheck. Return True when ok; otherwise raise ValueError with details.

        Raises:
            ValueError: with actionable message if validation fails.
        """
        provider = cls.get_available_provider()

        if provider == LLMProvider.AZURE_OPENAI:
            env_sets = AzureOpenAIConfig.get_env_sets()
            if not env_sets:
                raise ValueError(
                    "Azure OpenAI configuration missing required values. Ensure AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_API_KEY, and AZURE_OPENAI_CHAT_DEPLOYMENT_NAME are set."
                )

            azure_last_message: Optional[str] = None
            for env_set in env_sets:
                endpoint = (env_set.values.get("AZURE_OPENAI_ENDPOINT") or "").rstrip(
                    "/"
                )
                api_version = env_set.values.get("AZURE_OPENAI_API_VERSION")
                api_key = env_set.values.get("AZURE_OPENAI_API_KEY")
                deployment = env_set.values.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

                if not endpoint or not api_version or not api_key or not deployment:
                    continue

                try:
                    res = check_azure_openai(
                        endpoint=endpoint,
                        api_key=api_key,
                        api_version=api_version,
                        deployment=deployment,
                        timeout=10.0,
                    )
                except Exception as e:
                    azure_last_message = str(e)
                    continue

                if res.ok:
                    set_preferred_env_set(AzureOpenAIConfig._GROUP, env_set.index)
                    return True
                azure_last_message = res.message

            raise ValueError(
                azure_last_message or "Azure OpenAI connectivity check failed"
            )

        elif provider == LLMProvider.OPENAI:
            env_sets = OpenAIConfig.get_env_sets()
            if not env_sets:
                raise ValueError(
                    "OpenAI configuration missing required values. Ensure OPENAI_API_KEY and OPENAI_CHAT_MODEL_ID are set."
                )

            openai_last_message: Optional[str] = None
            for env_set in env_sets:
                api_key = env_set.values.get("OPENAI_API_KEY")
                base_url = env_set.values.get("OPENAI_BASE_URL")
                org_id = env_set.values.get("OPENAI_ORG_ID")
                model_id = env_set.values.get("OPENAI_CHAT_MODEL_ID")

                if not api_key or not model_id:
                    continue

                try:
                    res = check_openai(
                        endpoint=base_url,
                        api_key=api_key,
                        model=model_id,
                        org_id=org_id,
                        timeout=10.0,
                    )
                except Exception as e:
                    openai_last_message = str(e)
                    continue

                if res.ok:
                    set_preferred_env_set(OpenAIConfig._GROUP, env_set.index)
                    return True
                openai_last_message = res.message

            raise ValueError(openai_last_message or "OpenAI connectivity check failed")
        elif provider == LLMProvider.ANTHROPIC:
            from anthropic import Anthropic

            env_sets = AnthropicConfig.get_env_sets()
            if not env_sets:
                raise ValueError(
                    "Anthropic configuration missing required values. Ensure "
                    "ANTHROPIC_API_KEY and ANTHROPIC_MODEL are set."
                )

            anthropic_last_message: Optional[str] = None
            for env_set in env_sets:
                api_key = env_set.values.get("ANTHROPIC_API_KEY")
                model = env_set.values.get("ANTHROPIC_MODEL")
                base_url = env_set.values.get("ANTHROPIC_BASE_URL")
                if not api_key or not model:
                    continue

                try:
                    client = Anthropic(api_key=api_key, base_url=base_url)
                    client.messages.create(
                        model=model,
                        max_tokens=1,
                        messages=[{"role": "user", "content": "Reply OK"}],
                    )
                except Exception as e:
                    anthropic_last_message = str(e)
                    continue

                set_preferred_env_set(AnthropicConfig._GROUP, env_set.index)
                return True

            raise ValueError(
                anthropic_last_message or "Anthropic connectivity check failed"
            )
        elif provider == LLMProvider.LITELLM:
            try:
                import litellm
            except ImportError as exc:
                raise ValueError(
                    "LiteLLM is configured but the 'litellm' package is not "
                    'installed. Install it with: pip install "co-op-translator[litellm]"'
                ) from exc

            env_sets = LiteLLMConfig.get_env_sets()
            if not env_sets:
                raise ValueError(
                    "LiteLLM configuration missing required values. Ensure "
                    "LITELLM_MODEL is set."
                )

            litellm_last_message: Optional[str] = None
            for env_set in env_sets:
                model = env_set.values.get("LITELLM_MODEL")
                if not model:
                    continue
                credentials = {
                    "api_key": env_set.values.get("LITELLM_API_KEY") or None,
                    "api_base": env_set.values.get("LITELLM_API_BASE") or None,
                }

                try:
                    litellm.completion(
                        model=model,
                        messages=[{"role": "user", "content": "Reply OK"}],
                        max_tokens=16,
                        drop_params=True,
                        timeout=10.0,
                        **{k: v for k, v in credentials.items() if v},
                    )
                except Exception as e:
                    litellm_last_message = str(e)
                    continue

                set_preferred_env_set(LiteLLMConfig._GROUP, env_set.index)
                return True

            raise ValueError(
                litellm_last_message or "LiteLLM connectivity check failed"
            )
        else:
            # Should not happen because get_available_provider() would have raised earlier otherwise
            raise ValueError("No LLM provider available for connectivity validation.")
