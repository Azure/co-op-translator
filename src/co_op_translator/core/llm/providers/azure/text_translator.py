from openai import AzureOpenAI
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig


class AzureTextTranslator(TextTranslator):
    """Azure OpenAI implementation for text translation."""

    def __init__(self):
        """Initialize Azure Text Translator."""
        super().__init__()

    def get_openai_client(self):
        """Create an Azure OpenAI client instance.

        Configures client with API key, version and deployment endpoint
        from application settings.

        Returns:
            Configured Azure OpenAI client
        """
        return AzureOpenAI(
            api_key=AzureOpenAIConfig.get_api_key(),
            api_version=AzureOpenAIConfig.get_api_version(),
            base_url=f"{AzureOpenAIConfig.get_endpoint()}/openai/deployments/{AzureOpenAIConfig.get_chat_deployment_name()}",
        )

    def get_model_name(self):
        """Retrieve the configured Azure OpenAI model name."""
        return AzureOpenAIConfig.get_model_name()
