from abc import ABC, abstractmethod
import logging
from co_op_translator.utils.llm.text_utils import (
    gen_image_translation_prompt,
    remove_code_backticks,
    extract_yaml_lines,
)
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider

logger = logging.getLogger(__name__)


class TextTranslator(ABC):
    def __init__(self):
        self.client = self.get_openai_client()

    @abstractmethod
    def get_openai_client(self):
        """
        Initialize and return a client.

        Returns:
            The initialized AI model client.
        """
        pass

    @abstractmethod
    def get_model_name(self):
        """Get the model name for the provider."""
        pass

    def translate_image_text(self, text_data, target_language):
        """
        Translate text data in image using the LLM API.

        Args:
            text_data (list): List of text lines to be translated.
            target_language (str): Target language for translation.

        Returns:
            list: List of translated text lines.
        """
        prompt = gen_image_translation_prompt(text_data, target_language)
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

    def translate_text(self, text, target_language):
        """
        Translate a given text into the target language using the LLM API.

        Args:
            text (str): The text to be translated.
            target_language (str): The target language code.

        Returns:
            str: The translated text.
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
    def create(cls):
        """Factory method to create appropriate translator based on available provider."""
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
