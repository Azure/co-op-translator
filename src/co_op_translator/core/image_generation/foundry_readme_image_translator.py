from __future__ import annotations

import hashlib
from io import BytesIO
from pathlib import Path
from typing import ClassVar

import httpx
from PIL import Image

from co_op_translator.config.readme_image_config import ReadmeImageGenerationSettings
from co_op_translator.core.image_generation.common import (
    build_localization_prompt,
    decode_and_restore_image,
    png_upload_for_webp,
)


class FoundryReadmeImageTranslator:
    """Regenerate README images with the Microsoft Foundry MAI Images API."""

    PROMPT_VERSION = "2"
    REQUEST_TIMEOUT_SECONDS = 300
    _MIME_TYPES: ClassVar[dict[str, str]] = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
    }

    def __init__(
        self,
        settings: ReadmeImageGenerationSettings,
        *,
        http_client=None,
    ):
        self.settings = settings
        self.http_client = http_client or httpx
        fingerprint_input = "|".join(
            (
                self.PROMPT_VERSION,
                settings.model,
                settings.endpoint or "",
                settings.prompt or "",
            )
        )
        fingerprint = hashlib.sha256(fingerprint_input.encode("utf-8")).hexdigest()[:16]
        self.metadata_fingerprint = f"foundry-image:{settings.model}:{fingerprint}"

    def translate_image(
        self,
        image_path: str | Path,
        language_code: str,
        fast_mode: bool = False,
    ) -> Image.Image:
        """Return a localized image produced by a Foundry MAI image deployment."""

        del fast_mode
        image_path = Path(image_path)
        suffix = image_path.suffix.lower()
        mime_type = self._MIME_TYPES.get(suffix)
        if mime_type is None and suffix != ".webp":
            raise ValueError(
                "Microsoft Foundry README image translation supports PNG, JPEG, "
                "and WebP inputs."
            )

        if suffix == ".webp":
            upload_name, upload_data, mime_type = png_upload_for_webp(image_path)
        else:
            upload_name = image_path.name
            upload_data = BytesIO(image_path.read_bytes())

        endpoint = (self.settings.endpoint or "").rstrip("/")
        try:
            response = self.http_client.post(
                f"{endpoint}/mai/v1/images/edits",
                headers={"api-key": self.settings.api_key},
                data={
                    "model": self.settings.model,
                    "prompt": build_localization_prompt(
                        language_code,
                        self.settings.prompt,
                    ),
                },
                files={"image": (upload_name, upload_data, mime_type)},
                timeout=self.REQUEST_TIMEOUT_SECONDS,
            )
        finally:
            upload_data.close()
        response.raise_for_status()
        payload = response.json()
        encoded = next(
            (
                item.get("b64_json")
                for item in payload.get("data", [])
                if item.get("b64_json")
            ),
            None,
        )
        if not encoded:
            raise RuntimeError(
                "The Microsoft Foundry image model returned no image data."
            )
        return decode_and_restore_image(encoded, image_path)
