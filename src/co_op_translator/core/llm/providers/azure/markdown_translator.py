from pathlib import Path
import asyncio
import logging
import time
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig
from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)
from semantic_kernel.contents.chat_history import ChatHistory
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.utils.common.env_set_utils import set_preferred_env_set
from co_op_translator.utils.llm.markdown_utils import SPLIT_DELIMITER
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
    ):
        """Initialize translator with Azure-specific configuration.

        Args:
            root_dir: Optional root directory for the project
        """
        super().__init__(
            root_dir, translations_dir=translations_dir, image_dir=image_dir
        )
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

    def _is_transient_error(self, exc: Exception) -> bool:
        if isinstance(exc, (ValueError, TypeError)):
            return False
        status_code = self._extract_status_code(exc)
        if status_code in {401, 403, 408, 409, 429, 500, 502, 503, 504}:
            return True
        exc_name = type(exc).__name__
        if exc_name in {"APIConnectionError", "APITimeoutError"}:
            return True
        return False

    async def _run_prompt_once(self, prompt: str, index: int, total: int) -> str:
        # Configure model parameters for translation quality
        req_settings = self.kernel.get_prompt_execution_settings_from_service_id(
            LLMProvider.AZURE_OPENAI.value
        )
        req_settings.temperature = 0
        req_settings.top_p = 0.8

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

        chat = ChatHistory()
        chat.add_system_message(system_text)
        chat.add_user_message(user_text)

        service: ChatCompletionClientBase = self.kernel.get_service(
            LLMProvider.AZURE_OPENAI.value
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
        """
        Execute a single translation prompt using Azure OpenAI.

        Args:
            prompt: Translation instruction prompt content
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            Translated text content or empty string on error
        """
        env_sets = AzureOpenAIConfig.get_env_sets()
        if not env_sets:
            try:
                return await self._run_prompt_once(prompt, index, total)
            except Exception as e:
                logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
                return ""

        logger.debug("Azure OpenAI env sets available: %s", [s.index for s in env_sets])

        last_exc: Exception | None = None
        for attempt_idx, env_set in enumerate(env_sets):
            if attempt_idx > 0:
                set_preferred_env_set(AzureOpenAIConfig._GROUP, env_set.index)
                self.kernel = self._initialize_kernel()
            try:
                return await self._run_prompt_once(prompt, index, total)
            except Exception as e:
                last_exc = e
                status_code = self._extract_status_code(e)
                if self._is_transient_error(e):
                    logger.warning(
                        "Azure OpenAI request failed (status=%s) on env set %s; trying next env set",
                        status_code,
                        env_set.index,
                    )
                    continue
                logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
                return ""

        if last_exc is not None:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {last_exc}")
        return ""
