from typing import Any

from co_op_translator.optional_dependencies import raise_for_optional_dependency

__all__ = ["AzureImageTranslator"]


def __getattr__(name: str) -> Any:
    if name == "AzureImageTranslator":
        try:
            from co_op_translator.core.vision.providers.azure.image_translator import (
                AzureImageTranslator,
            )
        except ImportError as exc:
            raise_for_optional_dependency(
                feature="Vision translators",
                extra="image",
                exc=exc,
            )

        return AzureImageTranslator
    raise AttributeError(name)
