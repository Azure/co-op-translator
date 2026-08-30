from pathlib import Path
import asyncio
import logging
import time
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator
from co_op_translator.core.llm.model_clients import (
    TranslationModelClient,
    create_translation_model_client,
)

logger = logging.getLogger(__name__)


class AzureMarkdownEvaluator(MarkdownEvaluator):
    """Azure OpenAI implementation for markdown evaluation."""

    def __init__(
        self,
        root_dir: Path | None = None,
        use_llm: bool = True,
        use_rule: bool = True,
        model_client: TranslationModelClient | None = None,
    ):
        """Initialize evaluator with Azure-specific configuration.

        Args:
            root_dir: Optional root directory for the project
            use_llm: Whether to use LLM for enhanced evaluation
            use_rule: Whether to use rule-based evaluation
        """
        super().__init__(root_dir, use_llm, use_rule)
        self.model_client = model_client or create_translation_model_client(
            LLMProvider.AZURE_OPENAI
        )

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
            # Log progress
            logger.info(f"Running evaluation prompt {index}/{total}")

            start_time = time.time()
            response = await self.model_client.complete("", prompt)
            end_time = time.time()
            logger.info(
                f"Prompt {index}/{total} completed in {end_time - start_time} seconds"
            )

            await asyncio.sleep(1)
            return response.content
        except Exception as e:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
            return ""
