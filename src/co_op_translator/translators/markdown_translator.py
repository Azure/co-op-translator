import asyncio
import logging
from pathlib import Path
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig
from co_op_translator.utils.markdown_utils import (
    process_markdown,
    update_links,
    generate_prompt_template,
    count_links_in_markdown,
    process_markdown_with_many_links,
    replace_code_blocks_and_inline_code,
    restore_code_blocks_and_inline_code
)
from co_op_translator.config.base_config import Config
from co_op_translator.config.font_config import FontConfig
import time

logger = logging.getLogger(__name__)

class MarkdownTranslator:
    def __init__(self, root_dir):
        """
        Initialize the MarkdownTranslator with the root directory.

        Args:
            root_dir (Path): The root directory of the project.
        """
        self.root_dir = root_dir
        self.kernel = self._initialize_kernel()
        self.font_config = FontConfig()

    def _initialize_kernel(self):
        """
        Initialize the semantic kernel with Azure OpenAI service.

        Returns:
            Kernel: Initialized semantic kernel.
        """
        kernel = Kernel()
        service_id = "chat-gpt"

        kernel.add_service(
            AzureChatCompletion(
                service_id=service_id,
                deployment_name=Config.get_azure_openai_chat_deployment_name(),
                endpoint=Config.get_azure_openai_endpoint(),
                api_key=Config.get_azure_openai_api_key()
            )
        )
        return kernel

    async def translate_markdown(self, document: str, language_code: str, md_file_path: str | Path) -> str:
        """
        Translate the markdown document to the specified language, handling documents with more than 10 links by splitting them into chunks.

        Args:
            document (str): The content of the markdown file.
            language_code (str): The target language code.
            md_file_path (str | Path): The file path of the markdown file.

        Returns:
            str: The translated content with updated links and a disclaimer appended.
        """
        md_file_path = Path(md_file_path)

        # Step 1: Replace code blocks and inline code with placeholders
        document_with_placeholders, placeholder_map = replace_code_blocks_and_inline_code(document)

        # Step 2: Split the document into chunks and generate prompts
        link_limit = 30
        if count_links_in_markdown(document_with_placeholders) > link_limit:
            logger.info(f"Document contains more than {link_limit} links, splitting the document into chunks.")
            document_chunks = process_markdown_with_many_links(document_with_placeholders, link_limit)
        else:
            logger.info(f"Document contains {link_limit} or fewer links, processing normally.")
            document_chunks = process_markdown(document_with_placeholders)

        # Step 3: Generate translation prompts and translate each chunk
        prompts = [generate_prompt_template(language_code, chunk, self.font_config.is_rtl(language_code)) for chunk in document_chunks]
        results = await self._run_prompts_sequentially(prompts)
        translated_content = "\n".join(results)

        # Step 4: Restore the code blocks and inline code from placeholders
        translated_content = restore_code_blocks_and_inline_code(translated_content, placeholder_map)

        # Step 5: Update links and add disclaimer
        updated_content = update_links(md_file_path, translated_content, language_code, self.root_dir)
        disclaimer = await self.generate_disclaimer(language_code)
        updated_content += "\n\n" + disclaimer

        return updated_content

    async def _run_prompts_sequentially(self, prompts):
        """
        Run the translation prompts sequentially with a timeout for each chunk.

        Args:
            prompts (list): List of translation prompts.

        Returns:
            list: List of translated text chunks.
        """
        results = []
        for index, prompt in enumerate(prompts):
            try:
                result = await asyncio.wait_for(
                    self._run_prompt(prompt, index + 1, len(prompts)),
                    timeout=300
                )
                results.append(result)
            except asyncio.TimeoutError:
                logger.warning(f"Chunk {index + 1} translation timed out. Skipping...")
                results.append(f"Translation for chunk {index + 1} skipped due to timeout.")
            except Exception as e:
                logger.error(f"Error during prompt execution for chunk {index + 1}: {e}")
                results.append(f"Error during translation of chunk {index + 1}")
        return results

    async def _run_prompt(self, prompt, index, total):
        """
        Execute a single translation prompt.

        Args:
            prompt (str): The translation prompt to execute.
            index (int): The index of the prompt.
            total (int): The total number of prompts.

        Returns:
            str: The translated text.
        """
        try:
            logger.info(f"Running prompt {index}/{total}")
            start_time = time.time()
            req_settings = self.kernel.get_prompt_execution_settings_from_service_id("chat-gpt")
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
            logger.info(f"Prompt {index}/{total} completed in {end_time - start_time} seconds")

            await asyncio.sleep(1)
            return str(result)
        except Exception as e:
            logger.error(f"Error in prompt {index}/{total} - {prompt}: {e}")
            return ""

    async def generate_disclaimer(self, output_lang: str) -> str:
        """
        Generate a disclaimer translation prompt for the specified language.

        Args:
            output_lang (str): The target language for the disclaimer.

        Returns:
            str: The translated disclaimer text.
        """

        disclaimer_prompt = f""" Translate the following text to {output_lang}.

        **Disclaimer**: 
        This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation."""

        disclaimer = await self._run_prompt(disclaimer_prompt, 'disclaimer prompt', 1)
        
        return disclaimer
