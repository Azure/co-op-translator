import asyncio
import logging
import time
from pathlib import Path

from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.llm.model_clients import (
    TranslationModelClient,
    create_translation_model_client,
)
from co_op_translator.utils.common.env_set_utils import run_with_env_set_fallback_async
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER

logger = logging.getLogger(__name__)


class ModelClientMarkdownTranslator(MarkdownTranslator):
    """Translate Markdown through the framework-neutral model client boundary."""

    def __init__(
        self,
        provider: LLMProvider | None = None,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
        model_client: TranslationModelClient | None = None,
        context: str | None = None,
    ):
        super().__init__(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
            context=context,
        )
        if provider is None and model_client is None:
            raise ValueError("A provider or injected model client is required.")

        self.provider = provider
        self._provider_config = (
            LLMConfig.get_provider_config_type(provider)
            if provider is not None
            else None
        )
        self._model_client_injected = model_client is not None
        self.model_client = model_client or self._initialize_model_client()
        active = (
            None
            if self._model_client_injected or self._provider_config is None
            else self._provider_config.get_active_env_set()
        )
        self._env_set_index = active.index if active is not None else None

    def _initialize_model_client(self) -> TranslationModelClient:
        if self.provider is None:
            raise ValueError("An injected model client is required without a provider.")
        return create_translation_model_client(self.provider)

    async def _run_prompt_once(
        self,
        prompt: str,
        index: int | str,
        total: int,
    ) -> str:
        if isinstance(index, str):
            logger.info("Running system prompt: %s", index)
        else:
            logger.info("Running translation prompt %s/%s", index, total)

        parts = prompt.split(SPLIT_DELIMITER, 1)
        if len(parts) != 2:
            raise ValueError(
                "Prompt did not contain expected system/user split "
                "(missing SPLIT_DELIMITER)."
            )
        system_text, user_text = parts[0].strip(), parts[1]

        start_time = time.time()
        response = await self.model_client.complete(system_text, user_text)
        self._raise_for_finish_reason(response.finish_reason, index, total)
        logger.info(
            "Prompt %s/%s completed in %s seconds",
            index,
            total,
            time.time() - start_time,
        )
        await asyncio.sleep(1)
        return response.content

    async def _run_prompt(
        self,
        prompt: str,
        index: int | str,
        total: int,
    ) -> str:
        config = self._provider_config
        if self._model_client_injected or config is None:
            return await self._run_prompt_once(prompt, index, total)

        env_sets = config.get_env_sets()
        if not env_sets:
            return await self._run_prompt_once(prompt, index, total)

        async def _call_once():
            return await self._run_prompt_once(prompt, index, total)

        def _on_env_set_change(env_set):
            if self._env_set_index != env_set.index:
                self.model_client = self._initialize_model_client()
                self._env_set_index = env_set.index

        provider_name = self.provider.display_name if self.provider else "model client"
        return await run_with_env_set_fallback_async(
            env_sets=env_sets,
            group=config._GROUP,
            op_name=f"{provider_name} prompt {index}/{total}",
            fn=_call_once,
            on_env_set_change=_on_env_set_change,
            call_on_env_set_change_for_first_attempt=True,
        )
