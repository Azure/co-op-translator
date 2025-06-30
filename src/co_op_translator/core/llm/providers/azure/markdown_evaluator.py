from pathlib import Path
import asyncio
import logging
import time
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator

logger = logging.getLogger(__name__)


class AzureMarkdownEvaluator(MarkdownEvaluator):
    """Azure OpenAI implementation for markdown evaluation."""

    def __init__(
        self, root_dir: Path = None, use_llm: bool = True, use_rule: bool = True
    ):
        """Initialize evaluator with Azure-specific configuration.

        Args:
            root_dir: Optional root directory for the project
            use_llm: Whether to use LLM for enhanced evaluation
            use_rule: Whether to use rule-based evaluation
        """
        super().__init__(root_dir, use_llm, use_rule)
        self.kernel = self._initialize_kernel()

    def _initialize_kernel(self):
        """Create and configure Semantic Kernel with Azure OpenAI service.

        Returns:
            Configured Semantic Kernel instance
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
        Execute a single evaluation prompt using Azure OpenAI.

        Args:
            prompt: Evaluation instruction prompt content
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            Evaluation result as text or empty string on error
        """
        try:
            # Configure model parameters for evaluation quality
            req_settings = self.kernel.get_prompt_execution_settings_from_service_id(
                LLMProvider.AZURE_OPENAI.value
            )
            req_settings.max_tokens = 2048
            req_settings.temperature = 0
            req_settings.top_p = 0.95

            # Log progress
            logger.info(f"Running evaluation prompt {index}/{total}")

            start_time = time.time()
            prompt_template_config = PromptTemplateConfig(
                template=prompt,
                name="evaluate",
                description="Evaluate a text translation quality",
                template_format="semantic-kernel",
                execution_settings=req_settings,
            )

            function = self.kernel.add_function(
                function_name="evaluate_function",
                plugin_name="evaluate_plugin",
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
