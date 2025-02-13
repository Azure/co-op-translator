from pathlib import Path
import asyncio
import logging
import time
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator

logger = logging.getLogger(__name__)


class AzureMarkdownTranslator(MarkdownTranslator):
    """Azure OpenAI implementation for markdown translation."""

    def __init__(self, root_dir: Path = None):
        """
        Initialize Azure Markdown Translator.

        Args:
            root_dir: Optional root directory for the project
        """
        super().__init__(root_dir)
        self.kernel = self._initialize_kernel()

    def _initialize_kernel(self):
        """
        Initialize the semantic kernel with Azure OpenAI service.

        Returns:
            Kernel: Initialized semantic kernel.
        """
        kernel = Kernel()
        service_id = LLMProvider.AZURE_OPENAI.value

        kernel.add_service(
            AzureChatCompletion(
                service_id=service_id,
                deployment_name=AzureOpenAIConfig.get_chat_deployment_name(),
                endpoint=AzureOpenAIConfig.get_endpoint(),
                api_key=AzureOpenAIConfig.get_api_key(),
            )
        )
        return kernel

    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        """
        Execute a single translation prompt using Azure OpenAI.

        Args:
            prompt: The translation prompt
            index: Current chunk index
            total: Total number of chunks

        Returns:
            str: Translated text
        """
        try:
            # Initialize settings for all prompts
            req_settings = self.kernel.get_prompt_execution_settings_from_service_id(
                LLMProvider.AZURE_OPENAI.value
            )
            req_settings.max_tokens = 4096
            req_settings.temperature = 0.7
            req_settings.top_p = 0.8

            # Log appropriate message based on prompt type
            if index == "disclaimer" or isinstance(index, str):
                logger.info(f"Running system prompt: {index}")
            else:
                logger.info(f"Running translation prompt {index}/{total}")

            start_time = time.time()

            prompt_template_config = PromptTemplateConfig(
                template=prompt,
                name="translate",
                description="Translate a text to another language",
                template_format="semantic-kernel",
                execution_settings=req_settings,
            )

            function = self.kernel.add_function(
                function_name="translate_function",
                plugin_name="translate_plugin",
                prompt_template_config=prompt_template_config,
            )

            result = await self.kernel.invoke(function)
            end_time = time.time()
            logger.info(
                f"Prompt {index}/{total} completed in {end_time - start_time} seconds"
            )

            await asyncio.sleep(1)
            return str(result)
        except Exception as e:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
            return ""
