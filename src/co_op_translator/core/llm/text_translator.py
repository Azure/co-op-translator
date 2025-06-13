from abc import ABC, abstractmethod
import logging
from co_op_translator.utils.llm.text_utils import (
    gen_image_translation_prompt,
    remove_code_backticks,
    extract_yaml_lines,
)
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.font_config import FontConfig

logger = logging.getLogger(__name__)


class TextTranslator(ABC):
    """Define interface for text translation services.

    Provides common functionality and abstract methods to be implemented by providers.
    """

    def __init__(self):
        self.client = self.get_openai_client()
        self.font_config = FontConfig()

    @abstractmethod
    def get_openai_client(self):
        """Create and configure a model client instance.

        Returns:
            Initialized AI model client for the specific provider
        """
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Retrieve the configured model name for the provider."""
        pass

    def translate_image_text(self, text_data: list, target_language: str) -> list:
        """Translate extracted text from images to target language.

        Processes text discovered through OCR and generates translations
        formatted for placement back onto images.

        Args:
            text_data: List of text lines to translate
            target_language: Target language code

        Returns:
            List of translated text lines
        """
        language_name = self.font_config.get_language_name(target_language)
        prompt = gen_image_translation_prompt(text_data, target_language, language_name)
        response = self.client.chat.completions.create(
            model=self.get_model_name(),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=2000,
        )
        translated_text = remove_code_backticks(response.choices[0].message.content)
        logger.debug(f"Raw translation response: {translated_text}")
        result = extract_yaml_lines(translated_text)
        logger.debug(f"Extracted translation lines: {result}")
        return result

    def translate_text(self, text: str, target_language: str) -> str:
        """Translate plain text to specified target language.

        Args:
            text: Source text content to translate
            target_language: Target language code

        Returns:
            Translated text content
        """
        prompt = f"Translate the following text into {target_language}:\n\n{text}"
        response = self.client.chat.completions.create(
            model=self.get_model_name(),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=2000,
        )
        translated_text = remove_code_backticks(response.choices[0].message.content)
        return translated_text

    @classmethod
    def create(cls) -> "TextTranslator":
        """Create appropriate text translator implementation based on configuration.

        Factory method that instantiates the correct translator class based on
        the LLM provider settings.

        Returns:
            Configured text translator instance

        Raises:
            ValueError: When no valid LLM provider is configured
        """
        provider = LLMConfig.get_available_provider()
        if provider == LLMProvider.AZURE_OPENAI:
            from co_op_translator.core.llm.providers.azure.text_translator import (
                AzureTextTranslator,
            )

            return AzureTextTranslator()
        elif provider == LLMProvider.OPENAI:
            from co_op_translator.core.llm.providers.openai.text_translator import (
                OpenAITextTranslator,
            )

            return OpenAITextTranslator()
        else:
            raise ValueError("No valid LLM provider configured")
