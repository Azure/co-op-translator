from pathlib import Path
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.llm_config.openai import OpenAIConfig
import logging
import time
import asyncio

logger = logging.getLogger(__name__)

class OpenAIMarkdownTranslator(MarkdownTranslator):
    """OpenAI implementation for markdown translation."""
    
    def __init__(self, root_dir: Path = None):
        """
        Initialize OpenAI Markdown Translator.
        
        Args:
            root_dir: Optional root directory for the project
        """
        super().__init__(root_dir)
        self.kernel = self._initialize_kernel()

    def _initialize_kernel(self):
        """
        Initialize the semantic kernel with OpenAI service.

        Returns:
            Kernel: Initialized semantic kernel.
        """
        kernel = Kernel()
        service_id = LLMProvider.OPENAI.value

        kernel.add_service(
            OpenAIChatCompletion(
                service_id=service_id,
                ai_model_id=OpenAIConfig.get_chat_model_id(),
                org_id=OpenAIConfig.get_org_id(),
                api_key=OpenAIConfig.get_api_key()
            )
        )
        return kernel

    async def _run_prompt(self, prompt: str, source_lang: str, target_lang: str, index: int, total: int) -> str:
        """
        Execute a single translation prompt using Azure OpenAI.
        
        Args:
            prompt: The translation prompt
            source_lang: Source language code
            target_lang: Target language code
            index: Current chunk index
            total: Total number of chunks
            
        Returns:
            str: Translated text
        """
        try:
            # For disclaimer and other system prompts, use semantic kernel
            if index == 'disclaimer' or isinstance(index, str):
                logger.info(f"Running system prompt: {index}")
                start_time = time.time()

                req_settings = self.kernel.get_prompt_execution_settings_from_service_id(LLMProvider.OPENAI.value)
                req_settings.max_tokens = 4096
                req_settings.temperature = 0.7
                req_settings.top_p = 0.8

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
                logger.info(f"System prompt completed in {end_time - start_time} seconds")

                await asyncio.sleep(1)
                return str(result)
            
            # For regular markdown content, use the text translator
            else:
                logger.info(f"Running translation prompt {index}/{total}")
                start_time = time.time()
                
                result = await self.text_translator.translate_text(prompt, target_lang)
                
                end_time = time.time()
                logger.info(f"Translation {index}/{total} completed in {end_time - start_time} seconds")
                
                await asyncio.sleep(1)
                return result
                
        except Exception as e:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
            raise  # Re-raise the exception to be handled by the base class
