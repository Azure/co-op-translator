import importlib.resources
import yaml


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
        font_name = self.font_mappings.get(language_code, {}).get("font")

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
        if language_code not in self.font_mappings:
            raise ValueError(f"Language code '{language_code}' is not supported.")

        return self.font_mappings.get(language_code, {}).get("name", language_code)

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
        if language_code not in self.font_mappings:
            raise ValueError(f"Language code '{language_code}' is not supported.")

        # Return RTL info if available, default to False
        return self.font_mappings.get(language_code, {}).get("rtl", False)
