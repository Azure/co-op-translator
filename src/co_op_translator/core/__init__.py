from typing import Any

from co_op_translator.core.llm import *
from co_op_translator.core.project import *
from co_op_translator.optional_dependencies import raise_for_optional_dependency

__all__ = []


def __getattr__(name: str) -> Any:
    if name == "AzureImageTranslator":
        try:
            from co_op_translator.core.vision import AzureImageTranslator
        except ImportError as exc:
            raise_for_optional_dependency(
                feature="Vision translators",
                extra="image",
                exc=exc,
            )

        return AzureImageTranslator
    raise AttributeError(name)
