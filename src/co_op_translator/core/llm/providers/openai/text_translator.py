from openai import OpenAI
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.config.llm_config.openai import OpenAIConfig


class OpenAITextTranslator(TextTranslator):
    """OpenAI implementation for text translation."""

    def __init__(self):
        """Initialize the OpenAI text translator with client."""
        super().__init__()

    def get_openai_client(self):
        """Create an OpenAI client instance.

        Configures client with API key, organization ID, and base URL
        from application settings.

        Returns:
            Configured OpenAI client
        """
        return OpenAI(
            api_key=OpenAIConfig.get_api_key(),
            organization=OpenAIConfig.get_org_id(),
            base_url=OpenAIConfig.get_base_url(),
        )

    def get_model_name(self) -> str:
        """Retrieve the configured OpenAI model name."""
        return OpenAIConfig.get_chat_model_id()
