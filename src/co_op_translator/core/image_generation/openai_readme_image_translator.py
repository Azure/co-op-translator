from __future__ import annotations

import hashlib
from pathlib import Path

from openai import AzureOpenAI, OpenAI
from PIL import Image

from co_op_translator.config.readme_image_config import (
    ReadmeImageConfig,
    ReadmeImageGenerationSettings,
)
from co_op_translator.core.image_generation.common import (
    build_localization_prompt,
    decode_and_restore_image,
    image_edit_size,
    png_upload_for_webp,
)


class OpenAIReadmeImageTranslator:
    """Regenerate README images with OpenAI or Azure OpenAI image edits."""

    PROMPT_VERSION = "2"

    def __init__(
        self,
        settings: ReadmeImageGenerationSettings,
        *,
        client=None,
    ):
        self.settings = settings
        self.client = client or self._create_client()
        fingerprint_input = "|".join(
            (
                self.PROMPT_VERSION,
                settings.provider,
                settings.model,
                settings.base_url or settings.endpoint or "",
                settings.api_version or "",
                settings.quality or "auto",
                settings.input_fidelity or "low",
                settings.prompt or "",
            )
        )
        fingerprint = hashlib.sha256(fingerprint_input.encode("utf-8")).hexdigest()[:16]
        self.metadata_fingerprint = (
            f"{settings.provider}-image:{settings.model}:{fingerprint}"
        )

    def _create_client(self):
        if self.settings.provider == ReadmeImageConfig.AZURE_OPENAI_PROVIDER:
            return AzureOpenAI(
                api_key=self.settings.api_key,
                azure_endpoint=self.settings.endpoint,
                api_version=self.settings.api_version,
            )
        return OpenAI(
            api_key=self.settings.api_key,
            organization=self.settings.organization,
            base_url=self.settings.base_url,
        )

    def translate_image(
        self,
        image_path: str | Path,
        language_code: str,
        fast_mode: bool = False,
    ) -> Image.Image:
        """Return a newly generated localized image based on the source image."""

        del fast_mode
        image_path = Path(image_path)
        request = {
            "model": self.settings.model,
            "prompt": build_localization_prompt(
                language_code,
                self.settings.prompt,
            ),
            "size": image_edit_size(image_path),
        }
        is_azure_openai = (
            self.settings.provider == ReadmeImageConfig.AZURE_OPENAI_PROVIDER
        )
        if not is_azure_openai:
            request["output_format"] = "png"
        if self.settings.quality:
            request["quality"] = self.settings.quality
        if self.settings.input_fidelity:
            request["input_fidelity"] = self.settings.input_fidelity

        if is_azure_openai and image_path.suffix.lower() == ".webp":
            _, image_file, _ = png_upload_for_webp(image_path)
            try:
                response = self.client.images.edit(image=image_file, **request)
            finally:
                image_file.close()
        else:
            with image_path.open("rb") as image_file:
                response = self.client.images.edit(image=image_file, **request)

        if not response.data or not response.data[0].b64_json:
            raise RuntimeError("The image model returned no image data.")
        return decode_and_restore_image(response.data[0].b64_json, image_path)
