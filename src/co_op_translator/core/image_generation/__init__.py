import logging

from co_op_translator.config.readme_image_config import ReadmeImageConfig
from co_op_translator.core.image_generation.foundry_readme_image_translator import (
    FoundryReadmeImageTranslator,
)
from co_op_translator.core.image_generation.openai_readme_image_translator import (
    OpenAIReadmeImageTranslator,
)

logger = logging.getLogger(__name__)


def create_readme_image_translator():
    """Create the configured opt-in README image translator."""

    settings = ReadmeImageConfig.get_settings()
    if settings is None:
        raise ValueError(
            "README image generation is not enabled. Set "
            "README_IMAGE_TRANSLATION_ENABLED=true first."
        )
    logger.warning(
        "Experimental README image generation is enabled with provider '%s' "
        "and model '%s'. Generated text, especially small or dense text, may "
        "be misspelled, duplicated, omitted, or distorted. Visually review every "
        "generated image before publishing; Azure AI Vision remains the default "
        "image translation pipeline.",
        settings.provider,
        settings.model,
    )
    if settings.provider == ReadmeImageConfig.FOUNDRY_PROVIDER:
        return FoundryReadmeImageTranslator(settings)
    return OpenAIReadmeImageTranslator(settings)


__all__ = [
    "FoundryReadmeImageTranslator",
    "OpenAIReadmeImageTranslator",
    "create_readme_image_translator",
]
