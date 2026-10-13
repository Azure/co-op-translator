from __future__ import annotations

import base64
from io import BytesIO
from pathlib import Path

from PIL import Image


def build_localization_prompt(
    language_code: str,
    project_instruction: str | None = None,
) -> str:
    prompt = (
        "Create a localized version of this README image for the target locale "
        f"'{language_code}'. Translate every piece of visible natural-language "
        "text into that locale. Preserve the original meaning, branding, visual "
        "hierarchy, composition, colors, logos, and aspect ratio. Do not add new "
        "claims, labels, watermarks, or decorative text. Keep every label fully "
        "inside the canvas, translate each label exactly once, and do not duplicate "
        "or omit any text. Render all translated text clearly and legibly."
    )
    if project_instruction:
        prompt += f" Additional project instruction: {project_instruction}"
    return prompt


def image_edit_size(source_path: Path) -> str:
    """Choose the closest supported GPT Image edit size for the source."""

    with Image.open(source_path) as source:
        width, height = source.size
    if width > height:
        return "1536x1024"
    if height > width:
        return "1024x1536"
    return "1024x1024"


def decode_and_restore_image(encoded: str, source_path: Path) -> Image.Image:
    """Decode a generated PNG and restore the source dimensions and alpha mode."""

    generated_bytes = base64.b64decode(encoded)
    with Image.open(BytesIO(generated_bytes)) as generated:
        result = generated.copy()

    original_alpha = None
    with Image.open(source_path) as original:
        original_size = original.size
        original_has_alpha = original.mode in {"RGBA", "LA"} or (
            original.mode == "P" and "transparency" in original.info
        )
        if original_has_alpha:
            original_alpha = original.convert("RGBA").getchannel("A")

    if result.size != original_size:
        result = result.resize(original_size, Image.Resampling.LANCZOS)
    if original_has_alpha and result.mode != "RGBA":
        result = result.convert("RGBA")
    if original_alpha is not None:
        result.putalpha(original_alpha)
    elif not original_has_alpha and result.mode not in {"RGB", "RGBA"}:
        result = result.convert("RGB")
    return result


def png_upload_for_webp(source_path: Path) -> tuple[str, BytesIO, str]:
    """Convert a WebP source to an in-memory PNG multipart upload."""

    upload_data = BytesIO()
    with Image.open(source_path) as source:
        source.save(upload_data, format="PNG")
    upload_data.seek(0)
    upload_data.name = f"{source_path.stem}.png"
    return upload_data.name, upload_data, "image/png"
