from pathlib import Path
import asyncio
import logging
import time
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.core.llm.model_clients import (
    TranslationModelClient,
    create_translation_model_client,
)
from co_op_translator.utils.common.env_set_utils import run_with_env_set_fallback_async
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator

logger = logging.getLogger(__name__)


class AzureMarkdownTranslator(MarkdownTranslator):
    """Azure OpenAI implementation for markdown translation."""

    def __init__(
        self,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
        model_client: TranslationModelClient | None = None,
    ):
        """Initialize translator with Azure-specific configuration.

        Args:
            root_dir: Optional root directory for the project
        """
        super().__init__(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
        )
        self._model_client_injected = model_client is not None
        self.model_client = model_client or self._initialize_model_client()
        active = (
            None
            if self._model_client_injected
            else AzureOpenAIConfig.get_active_env_set()
        )
        self._env_set_index = active.index if active is not None else None

    def _initialize_model_client(self) -> TranslationModelClient:
        """Create the configured framework adapter for Azure OpenAI."""
        return create_translation_model_client(LLMProvider.AZURE_OPENAI)

    async def _run_prompt_once(self, prompt: str, index: int, total: int) -> str:
        # Use different logging format for system vs. content prompts
        if index == "disclaimer" or isinstance(index, str):
            logger.info(f"Running system prompt: {index}")
        else:
            logger.info(f"Running translation prompt {index}/{total}")

        start_time = time.time()

        # Build chat messages: system for rules, user for content
        # Split using explicit delimiter inserted by generate_prompt_template
        parts = prompt.split(SPLIT_DELIMITER, 1)
        if len(parts) != 2:
            raise ValueError(
                "Prompt did not contain expected system/user split (missing blank line separator)."
            )
        system_text, user_text = parts[0].strip(), parts[1]

        response = await self.model_client.complete(system_text, user_text)
        self._raise_for_finish_reason(response.finish_reason, index, total)
        result = response.content
        end_time = time.time()
        logger.info(
            f"Prompt {index}/{total} completed in {end_time - start_time} seconds"
        )

        await asyncio.sleep(1)
        return str(result)

    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        """
        Execute a single translation prompt using Azure OpenAI.

        Args:
            prompt: Translation instruction prompt content
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            Translated text content or empty string on error
        """
        env_sets = (
            [] if self._model_client_injected else AzureOpenAIConfig.get_env_sets()
        )
        if not env_sets:
            try:
                return await self._run_prompt_once(prompt, index, total)
            except Exception as e:
                logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
                raise

        async def _call_once():
            return await self._run_prompt_once(prompt, index, total)

        def _on_env_set_change(env_set):
            if self._env_set_index != env_set.index:
                self.model_client = self._initialize_model_client()
                self._env_set_index = env_set.index

        try:
            return await run_with_env_set_fallback_async(
                env_sets=env_sets,
                group=AzureOpenAIConfig._GROUP,
                op_name=f"Azure OpenAI prompt {index}/{total}",
                fn=_call_once,
                on_env_set_change=_on_env_set_change,
                call_on_env_set_change_for_first_attempt=True,
            )
        except Exception as e:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
            raise
