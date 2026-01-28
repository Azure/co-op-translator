import importlib.resources
import yaml
from co_op_translator.utils.common.lang_utils import (
    normalize_language_code,
)


class FontConfig:
    def __init__(self):
        """
        Initialize the FontConfig class by loading the font mappings from a YAML file.
        """
        with importlib.resources.path(
            "co_op_translator.fonts", "font_language_mappings.yml"
        ) as mappings_path:
            with open(mappings_path, "r", encoding="utf-8") as file:
                self.font_mappings = yaml.safe_load(file)

    def _resolve_mapping_key(self, language_code: str) -> str:
        """
        Resolve provided language code to a canonical BCP 47 key present in font_language_mappings.yml.
        The YAML now uses canonical keys only. Alias inputs are normalized before lookup.
        """
        if not language_code:
            raise ValueError("Empty language code is not supported.")

        # Normalize input (accept alias like "tw", "cn")
        canonical = normalize_language_code(language_code)
        if canonical in self.font_mappings:
            return canonical

        raise ValueError(
            f"Font for language code '{language_code}' is not supported or not found."
        )

    def get_font_path(self, language_code):
        """
        Retrieve the font path for a given language code.

        Args:
            language_code (str): The language code.

        Returns:
            str: The full path to the corresponding font file.

        Raises:
            ValueError: If the language code or font is not found in the mappings.
        """
        key = self._resolve_mapping_key(language_code)
        font_name = self.font_mappings.get(key, {}).get("font")

        if not font_name:
            raise ValueError(
                f"Font for language code '{language_code}' is not supported or not found."
            )

        with importlib.resources.path("co_op_translator.fonts", font_name) as font_path:
            return str(font_path)

    def get_language_name(self, language_code):
        """
        Retrieve the language name for a given language code.

        Args:
            language_code (str): The language code.

        Returns:
            str: The name of the language corresponding to the language code.

        Raises:
            ValueError: If the language code is not found in the mappings.
        """
        try:
            key = self._resolve_mapping_key(language_code)
        except ValueError:
            # Preserve historical error message for tests/backward-compat
            raise ValueError(f"Language code '{language_code}' is not supported.")
        return self.font_mappings.get(key, {}).get("name", key)

    def is_rtl(self, language_code):
        """
        Check if the language is written from right to left (RTL).

        Args:
            language_code (str): The language code.

        Returns:
            bool: True if the language is RTL, False otherwise.

        Raises:
            ValueError: If the language code is not found in the mappings.
        """
        try:
            key = self._resolve_mapping_key(language_code)
        except ValueError:
            # Preserve historical error message for tests/backward-compat
            raise ValueError(f"Language code '{language_code}' is not supported.")
        # Return RTL info if available, default to False
        return self.font_mappings.get(key, {}).get("rtl", False)
