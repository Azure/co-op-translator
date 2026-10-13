import base64
import logging
from io import BytesIO
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image

from co_op_translator.config.readme_image_config import (
    ReadmeImageGenerationSettings,
)
from co_op_translator.core.image_generation.foundry_readme_image_translator import (
    FoundryReadmeImageTranslator,
)
from co_op_translator.core.image_generation import create_readme_image_translator
from co_op_translator.core.image_generation.openai_readme_image_translator import (
    OpenAIReadmeImageTranslator,
)


def _encoded_png(size=(4, 4), color="red") -> str:
    output = BytesIO()
    Image.new("RGB", size, color).save(output, format="PNG")
    return base64.b64encode(output.getvalue()).decode("ascii")


class FakeImages:
    def __init__(self, encoded):
        self.encoded = encoded
        self.request = None

    def edit(self, **kwargs):
        self.request = kwargs
        return SimpleNamespace(data=[SimpleNamespace(b64_json=self.encoded)])


class FakeOpenAIClient:
    def __init__(self, encoded):
        self.images = FakeImages(encoded)


class FakeResponse:
    def __init__(self, encoded):
        self.encoded = encoded

    def raise_for_status(self):
        return None

    def json(self):
        return {"data": [{"b64_json": self.encoded}]}


class FakeHttpClient:
    def __init__(self, encoded):
        self.encoded = encoded
        self.request = None

    def post(self, url, **kwargs):
        self.request = (url, kwargs)
        return FakeResponse(self.encoded)


def test_openai_image_edit_restores_source_dimensions(tmp_path):
    source = tmp_path / "hero.png"
    Image.new("RGB", (20, 10), "white").save(source)
    client = FakeOpenAIClient(_encoded_png())
    translator = OpenAIReadmeImageTranslator(
        ReadmeImageGenerationSettings(
            provider="openai",
            api_key="key",
            model="gpt-image-1.5",
            input_fidelity="high",
        ),
        client=client,
    )

    result = translator.translate_image(source, "ko")

    assert result.size == (20, 10)
    assert client.images.request["model"] == "gpt-image-1.5"
    assert client.images.request["output_format"] == "png"
    assert client.images.request["input_fidelity"] == "high"
    assert client.images.request["size"] == "1536x1024"
    assert "'ko'" in client.images.request["prompt"]


def test_azure_openai_image_edit_uses_deployment_without_openai_output_format(
    tmp_path,
):
    source = tmp_path / "hero.png"
    Image.new("RGB", (10, 10), "white").save(source)
    client = FakeOpenAIClient(_encoded_png())
    translator = OpenAIReadmeImageTranslator(
        ReadmeImageGenerationSettings(
            provider="azure_openai",
            api_key="key",
            model="image-deployment",
            endpoint="https://example.openai.azure.com",
            api_version="2025-04-01-preview",
            input_fidelity="high",
        ),
        client=client,
    )

    translator.translate_image(source, "fr")

    assert client.images.request["model"] == "image-deployment"
    assert client.images.request["input_fidelity"] == "high"
    assert "response_format" not in client.images.request
    assert "output_format" not in client.images.request


def test_foundry_mai_image_edit_uses_deployment_and_api_key(tmp_path):
    source = tmp_path / "hero.jpg"
    Image.new("RGB", (18, 9), "white").save(source)
    client = FakeHttpClient(_encoded_png())
    translator = FoundryReadmeImageTranslator(
        ReadmeImageGenerationSettings(
            provider="foundry",
            api_key="key",
            model="mai-image",
            endpoint="https://example.services.ai.azure.com/",
        ),
        http_client=client,
    )

    result = translator.translate_image(source, "ja")

    url, request = client.request
    assert url == "https://example.services.ai.azure.com/mai/v1/images/edits"
    assert request["headers"] == {"api-key": "key"}
    assert request["data"]["model"] == "mai-image"
    assert request["files"]["image"][2] == "image/jpeg"
    assert result.size == (18, 9)


def test_factory_warns_that_readme_image_generation_is_experimental(
    monkeypatch, caplog
):
    monkeypatch.setenv("README_IMAGE_TRANSLATION_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "key")
    monkeypatch.setenv("OPENAI_IMAGE_MODEL_ID", "gpt-image-1.5")

    with (
        patch(
            "co_op_translator.core.image_generation.OpenAIReadmeImageTranslator",
            return_value=object(),
        ),
        caplog.at_level(logging.WARNING),
    ):
        create_readme_image_translator()

    assert "Experimental README image generation is enabled" in caplog.text
    assert "Visually review every generated image" in caplog.text
