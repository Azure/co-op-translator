import pytest

from co_op_translator.config.readme_image_config import ReadmeImageConfig

README_IMAGE_ENV_VARS = (
    "README_IMAGE_TRANSLATION_ENABLED",
    "README_IMAGE_TRANSLATION_PROVIDER",
    "OPENAI_IMAGE_API_KEY",
    "OPENAI_IMAGE_MODEL_ID",
    "OPENAI_IMAGE_INPUT_FIDELITY",
    "OPENAI_API_KEY",
    "AZURE_OPENAI_IMAGE_API_KEY",
    "AZURE_OPENAI_IMAGE_ENDPOINT",
    "AZURE_OPENAI_IMAGE_DEPLOYMENT_NAME",
    "AZURE_OPENAI_IMAGE_API_VERSION",
    "AZURE_OPENAI_IMAGE_INPUT_FIDELITY",
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_API_VERSION",
    "FOUNDRY_IMAGE_API_KEY",
    "FOUNDRY_IMAGE_ENDPOINT",
    "FOUNDRY_IMAGE_DEPLOYMENT_NAME",
)


@pytest.fixture(autouse=True)
def clear_readme_image_environment(monkeypatch):
    for name in README_IMAGE_ENV_VARS:
        monkeypatch.delenv(name, raising=False)


def test_readme_image_generation_is_disabled_by_default():
    assert ReadmeImageConfig.is_enabled() is False
    assert ReadmeImageConfig.get_settings() is None


def test_enabled_flag_defaults_to_azure_openai(monkeypatch):
    monkeypatch.setenv("README_IMAGE_TRANSLATION_ENABLED", "true")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "key")
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://example.openai.azure.com")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")
    monkeypatch.setenv("AZURE_OPENAI_IMAGE_DEPLOYMENT_NAME", "gpt-image")

    settings = ReadmeImageConfig.get_settings()

    assert settings is not None
    assert settings.provider == "azure_openai"
    assert settings.model == "gpt-image"
    assert settings.api_key == "key"


def test_explicit_openai_provider_enables_feature(monkeypatch):
    monkeypatch.setenv("README_IMAGE_TRANSLATION_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "key")
    monkeypatch.setenv("OPENAI_IMAGE_MODEL_ID", "gpt-image-1.5")

    settings = ReadmeImageConfig.get_settings()

    assert settings is not None
    assert settings.provider == "openai"
    assert settings.model == "gpt-image-1.5"


def test_foundry_provider_requires_its_image_credentials(monkeypatch):
    monkeypatch.setenv("README_IMAGE_TRANSLATION_PROVIDER", "foundry")

    with pytest.raises(ValueError, match="FOUNDRY_IMAGE_API_KEY"):
        ReadmeImageConfig.get_settings()


def test_unknown_provider_fails_clearly(monkeypatch):
    monkeypatch.setenv("README_IMAGE_TRANSLATION_PROVIDER", "other")

    with pytest.raises(ValueError, match="Unsupported"):
        ReadmeImageConfig.get_settings()
