from __future__ import annotations

import os
from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class ReadmeImageGenerationSettings:
    """Configuration for opt-in README image generation."""

    provider: str
    api_key: str
    model: str
    organization: str | None = None
    base_url: str | None = None
    endpoint: str | None = None
    api_version: str | None = None
    quality: str | None = None
    input_fidelity: str | None = None
    prompt: str | None = None


class ReadmeImageConfig:
    """Read opt-in README image generation settings from the environment."""

    ENABLED_ENV = "README_IMAGE_TRANSLATION_ENABLED"
    PROVIDER_ENV = "README_IMAGE_TRANSLATION_PROVIDER"
    OPENAI_PROVIDER = "openai"
    AZURE_OPENAI_PROVIDER = "azure_openai"
    FOUNDRY_PROVIDER = "foundry"
    _SUPPORTED_PROVIDERS: ClassVar[set[str]] = {
        OPENAI_PROVIDER,
        AZURE_OPENAI_PROVIDER,
        FOUNDRY_PROVIDER,
    }
    _TRUE_VALUES: ClassVar[set[str]] = {"1", "true", "yes", "on"}

    @classmethod
    def get_provider(cls) -> str | None:
        value = os.getenv(cls.PROVIDER_ENV, "").strip().lower()
        if value:
            return value

        enabled = os.getenv(cls.ENABLED_ENV, "").strip().lower()
        if enabled in cls._TRUE_VALUES:
            return cls.AZURE_OPENAI_PROVIDER
        return None

    @classmethod
    def is_enabled(cls) -> bool:
        return cls.get_provider() is not None

    @classmethod
    def get_settings(cls) -> ReadmeImageGenerationSettings | None:
        provider = cls.get_provider()
        if provider is None:
            return None
        if provider not in cls._SUPPORTED_PROVIDERS:
            supported = ", ".join(sorted(cls._SUPPORTED_PROVIDERS))
            raise ValueError(
                f"Unsupported {cls.PROVIDER_ENV} value '{provider}'. "
                f"Supported values: {supported}."
            )

        if provider == cls.OPENAI_PROVIDER:
            return cls._get_openai_settings(provider)
        if provider == cls.AZURE_OPENAI_PROVIDER:
            return cls._get_azure_openai_settings(provider)
        return cls._get_foundry_settings(provider)

    @staticmethod
    def _require(values: dict[str, str], provider: str) -> None:
        missing = [description for description, value in values.items() if not value]
        if missing:
            raise ValueError(
                f"README image generation provider '{provider}' is enabled but "
                f"required configuration is missing: {', '.join(missing)}."
            )

    @staticmethod
    def _prompt() -> str | None:
        return os.getenv("README_IMAGE_TRANSLATION_PROMPT", "").strip() or None

    @classmethod
    def _get_openai_settings(cls, provider: str) -> ReadmeImageGenerationSettings:
        api_key = (
            os.getenv("OPENAI_IMAGE_API_KEY", "").strip()
            or os.getenv("OPENAI_API_KEY", "").strip()
        )
        model = os.getenv("OPENAI_IMAGE_MODEL_ID", "").strip()
        cls._require(
            {
                "OPENAI_IMAGE_API_KEY (or OPENAI_API_KEY)": api_key,
                "OPENAI_IMAGE_MODEL_ID": model,
            },
            provider,
        )
        return ReadmeImageGenerationSettings(
            provider=provider,
            api_key=api_key,
            model=model,
            organization=(
                os.getenv("OPENAI_IMAGE_ORG_ID", "").strip()
                or os.getenv("OPENAI_ORG_ID", "").strip()
                or None
            ),
            base_url=(
                os.getenv("OPENAI_IMAGE_BASE_URL", "").strip()
                or os.getenv("OPENAI_BASE_URL", "").strip()
                or None
            ),
            quality=os.getenv("OPENAI_IMAGE_QUALITY", "").strip() or None,
            input_fidelity=(
                os.getenv("OPENAI_IMAGE_INPUT_FIDELITY", "").strip() or "high"
            ),
            prompt=cls._prompt(),
        )

    @classmethod
    def _get_azure_openai_settings(cls, provider: str) -> ReadmeImageGenerationSettings:
        api_key = (
            os.getenv("AZURE_OPENAI_IMAGE_API_KEY", "").strip()
            or os.getenv("AZURE_OPENAI_API_KEY", "").strip()
        )
        endpoint = (
            os.getenv("AZURE_OPENAI_IMAGE_ENDPOINT", "").strip()
            or os.getenv("AZURE_OPENAI_ENDPOINT", "").strip()
        )
        deployment = os.getenv("AZURE_OPENAI_IMAGE_DEPLOYMENT_NAME", "").strip()
        api_version = (
            os.getenv("AZURE_OPENAI_IMAGE_API_VERSION", "").strip()
            or os.getenv("AZURE_OPENAI_API_VERSION", "").strip()
        )
        cls._require(
            {
                "AZURE_OPENAI_IMAGE_API_KEY (or AZURE_OPENAI_API_KEY)": api_key,
                "AZURE_OPENAI_IMAGE_ENDPOINT (or AZURE_OPENAI_ENDPOINT)": endpoint,
                "AZURE_OPENAI_IMAGE_DEPLOYMENT_NAME": deployment,
                "AZURE_OPENAI_IMAGE_API_VERSION (or AZURE_OPENAI_API_VERSION)": api_version,
            },
            provider,
        )
        return ReadmeImageGenerationSettings(
            provider=provider,
            api_key=api_key,
            model=deployment,
            endpoint=endpoint,
            api_version=api_version,
            quality=os.getenv("AZURE_OPENAI_IMAGE_QUALITY", "").strip() or None,
            input_fidelity=(
                os.getenv("AZURE_OPENAI_IMAGE_INPUT_FIDELITY", "").strip() or "high"
            ),
            prompt=cls._prompt(),
        )

    @classmethod
    def _get_foundry_settings(cls, provider: str) -> ReadmeImageGenerationSettings:
        api_key = os.getenv("FOUNDRY_IMAGE_API_KEY", "").strip()
        endpoint = os.getenv("FOUNDRY_IMAGE_ENDPOINT", "").strip()
        deployment = os.getenv("FOUNDRY_IMAGE_DEPLOYMENT_NAME", "").strip()
        cls._require(
            {
                "FOUNDRY_IMAGE_API_KEY": api_key,
                "FOUNDRY_IMAGE_ENDPOINT": endpoint,
                "FOUNDRY_IMAGE_DEPLOYMENT_NAME": deployment,
            },
            provider,
        )
        return ReadmeImageGenerationSettings(
            provider=provider,
            api_key=api_key,
            model=deployment,
            endpoint=endpoint,
            prompt=cls._prompt(),
        )

    @classmethod
    def validate_if_enabled(cls) -> bool:
        if not cls.is_enabled():
            return False
        cls.get_settings()
        return True
