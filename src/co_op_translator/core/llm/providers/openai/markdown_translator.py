from pathlib import Path
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)
from semantic_kernel.contents.chat_history import ChatHistory
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.utils.llm.markdown_utils import SPLIT_DELIMITER
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.llm_config.openai import OpenAIConfig
from co_op_translator.utils.common.env_set_utils import run_with_env_set_fallback_async
import logging
import time
import asyncio

logger = logging.getLogger(__name__)


class OpenAIMarkdownTranslator(MarkdownTranslator):
    """OpenAI implementation for markdown translation."""

    def __init__(
        self,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
    ):
        """Initialize translator with OpenAI configuration.

        Args:
            root_dir: Optional root directory for the project
        """
        super().__init__(
            root_dir, translations_dir=translations_dir, image_dir=image_dir
        )
        self.kernel = self._initialize_kernel()
        active = OpenAIConfig.get_active_env_set()
        self._env_set_index = active.index if active is not None else None

    def _initialize_kernel(self):
        """Create and configure Semantic Kernel with OpenAI service.

        Returns:
            Configured Semantic Kernel instance
        """
        kernel = Kernel()
        service_id = LLMProvider.OPENAI.value

        kernel.add_service(
            OpenAIChatCompletion(
                service_id=service_id,
                ai_model_id=OpenAIConfig.get_chat_model_id(),
                org_id=OpenAIConfig.get_org_id(),
                api_key=OpenAIConfig.get_api_key(),
            )
        )
        return kernel

    async def _run_prompt_once(self, prompt: str, index: int, total: int) -> str:
        # Configure model parameters for translation quality
        req_settings = self.kernel.get_prompt_execution_settings_from_service_id(
            LLMProvider.OPENAI.value
        )

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
                "Prompt did not contain expected system/user split (missing SPLIT_DELIMITER)."
            )
        system_text, user_text = parts[0].strip(), parts[1]

        chat = ChatHistory()
        chat.add_system_message(system_text)
        chat.add_user_message(user_text)

        # Retrieve the proper service and request completion
        service: ChatCompletionClientBase = self.kernel.get_service(
            LLMProvider.OPENAI.value
        )
        result_contents = await service.get_chat_message_contents(
            chat_history=chat, settings=req_settings
        )
        result = str(result_contents[0].content) if result_contents else ""
        end_time = time.time()
        logger.info(
            f"Prompt {index}/{total} completed in {end_time - start_time} seconds"
        )

        await asyncio.sleep(1)
        return str(result)

    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        """Execute translation prompt against OpenAI service.

        Args:
            prompt: Translation instruction prompt content
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            Translated text content or empty string on error
        """
        env_sets = OpenAIConfig.get_env_sets()
        if not env_sets:
            try:
                return await self._run_prompt_once(prompt, index, total)
            except Exception as e:
                logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
                return ""

        async def _call_once():
            return await self._run_prompt_once(prompt, index, total)

        def _on_env_set_change(env_set):
            if self._env_set_index != env_set.index:
                self.kernel = self._initialize_kernel()
                self._env_set_index = env_set.index

        try:
            return await run_with_env_set_fallback_async(
                env_sets=env_sets,
                group=OpenAIConfig._GROUP,
                op_name=f"OpenAI prompt {index}/{total}",
                fn=_call_once,
                on_env_set_change=_on_env_set_change,
                call_on_env_set_change_for_first_attempt=True,
            )
        except Exception as e:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
            return ""
