from abc import ABC, abstractmethod
import logging
from co_op_translator.utils.llm.text_utils import (
    gen_image_translation_prompt,
    remove_code_backticks,
    TranslationResponse,
)
from co_op_translator.utils.common.env_set_utils import set_preferred_env_set
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig
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

    def _get_env_sets_and_group(self):
        module = self.__class__.__module__
        if ".providers.azure." in module:
            return AzureOpenAIConfig.get_env_sets(), AzureOpenAIConfig._GROUP
        if ".providers.openai." in module:
            return OpenAIConfig.get_env_sets(), OpenAIConfig._GROUP

        provider = LLMConfig.get_available_provider()
        if provider == LLMProvider.AZURE_OPENAI:
            return AzureOpenAIConfig.get_env_sets(), AzureOpenAIConfig._GROUP
        if provider == LLMProvider.OPENAI:
            return OpenAIConfig.get_env_sets(), OpenAIConfig._GROUP
        return [], ""

    def _extract_status_code(self, exc: Exception):
        candidates = [
            exc,
            getattr(exc, "__cause__", None),
            getattr(exc, "__context__", None),
        ]
        if getattr(exc, "args", None):
            candidates.extend(list(exc.args))

        for obj in candidates:
            if obj is None:
                continue
            if not isinstance(obj, BaseException):
                continue

            status_code = getattr(obj, "status_code", None)
            if status_code is None and getattr(obj, "response", None) is not None:
                status_code = getattr(obj.response, "status_code", None)
            if status_code is not None:
                return status_code

        return None

    def _is_fallback_eligible_error(self, exc: Exception) -> bool:
        if isinstance(exc, (ValueError, TypeError)):
            return False

        status_code = self._extract_status_code(exc)
        if status_code in {401, 403, 408, 409, 429, 500, 502, 503, 504}:
            return True

        exc_name = type(exc).__name__
        if exc_name in {"APIConnectionError", "APITimeoutError"}:
            return True

        return False

    def _run_with_env_set_fallback(self, fn, op_name: str):
        env_sets, group = self._get_env_sets_and_group()
        if not env_sets or not group:
            return fn()

        logger.debug("%s env sets available: %s", op_name, [s.index for s in env_sets])

        last_exc: Exception | None = None
        for attempt_idx, env_set in enumerate(env_sets):
            if attempt_idx > 0:
                set_preferred_env_set(group, env_set.index)
                self.client = self.get_openai_client()
            try:
                return fn()
            except Exception as e:
                last_exc = e
                status_code = self._extract_status_code(e)
                if self._is_fallback_eligible_error(e):
                    logger.warning(
                        "%s failed (status=%s) on env set %s; trying next env set",
                        op_name,
                        status_code,
                        env_set.index,
                    )
                    continue
                raise

        if last_exc is not None:
            raise last_exc
        raise RuntimeError(f"{op_name} failed without exception")

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

        Uses structured outputs to ensure 1:1 line mapping and prevent
        Arabic ligature rendering issues.

        Args:
            text_data: List of text lines to translate
            target_language: Target language code

        Returns:
            List of translated text lines with exact count matching input
        """
        if not text_data:
            return []

        language_name = self.font_config.get_language_name(target_language)
        prompt = gen_image_translation_prompt(text_data, target_language, language_name)

        def _call_once():
            response = self.client.chat.completions.parse(
                model=self.get_model_name(),
                messages=[
                    {
                        "role": "system",
                        "content": "You are a translator. Return exactly the same number of translations as input lines.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format=TranslationResponse,
                temperature=0,
            )

            translations = response.choices[0].message.parsed.translations
            logger.debug(
                f"Structured output: {len(translations)} translations for {len(text_data)} input lines"
            )
            return translations

        return self._run_with_env_set_fallback(_call_once, op_name="translate_image_text")

    def translate_text(self, text: str, target_language: str) -> str:
        """Translate plain text to specified target language.

        Args:
            text: Source text content to translate
            target_language: Target language code

        Returns:
            Translated text content
        """
        prompt = f"Translate the following text into {target_language}:\n\n{text}"

        def _call_once():
            response = self.client.chat.completions.create(
                model=self.get_model_name(),
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0,
            )
            return remove_code_backticks(response.choices[0].message.content)

        return self._run_with_env_set_fallback(_call_once, op_name="translate_text")

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
