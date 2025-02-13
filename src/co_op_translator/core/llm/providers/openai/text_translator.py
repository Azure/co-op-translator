from openai import OpenAI
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.config.llm_config.openai import OpenAIConfig


class OpenAITextTranslator(TextTranslator):
    """OpenAI implementation for text translation."""

    def __init__(self):
        """Initialize OpenAI Text Translator."""
        self.client = self.get_openai_client()

    def get_openai_client(self):
        """
        Initialize and return an OpenAI client.

        Returns:
            OpenAI: The initialized OpenAI client.
        """
        return OpenAI(
            api_key=OpenAIConfig.get_api_key(),
            organization=OpenAIConfig.get_org_id(),
            base_url=OpenAIConfig.get_base_url(),
        )

    def get_model_name(self):
        """Get the OpenAI model name."""
        return OpenAIConfig.get_chat_model_id()
