from abc import ABC, abstractmethod
import asyncio
import logging
from pathlib import Path
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.utils.llm.markdown_utils import (
    process_markdown,
    update_links,
    generate_prompt_template,
    replace_code_blocks,
    restore_code_blocks,
)
from co_op_translator.config.font_config import FontConfig
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    create_metadata,
    format_metadata_comment,
)

logger = logging.getLogger(__name__)


class MarkdownTranslator(ABC):
    """Define interface for markdown translation services.

    Provides common utilities and abstract methods to be implemented by providers.
    """

    TRANSLATION_TIMEOUT_SECONDS = 300  # Translation timeout in seconds

    def __init__(self, root_dir: Path = None):
        """Initialize translator with project configuration.

        Args:
            root_dir: Root directory of the project for path calculations
        """
        self.root_dir = root_dir
        self.font_config = FontConfig()

    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of a file for change detection.

        Args:
            file_path: Path to the file to hash

        Returns:
            MD5 hash of the file content
        """
        return calculate_file_hash(file_path)

    def create_metadata(self, original_file: Path, language_code: str) -> dict:
        """Create metadata for a translated file.

        Args:
            original_file: Path to the source file being translated
            language_code: Target language code

        Returns:
            Metadata dictionary with source file information
        """
        return create_metadata(original_file, language_code, self.root_dir)

    def format_metadata_comment(self, metadata: dict) -> str:
        """Format metadata dictionary as HTML comment.

        Serializes the metadata as JSON and wraps it in an HTML comment format
        for embedding in markdown files.

        Args:
            metadata: Dictionary containing translation metadata

        Returns:
            Formatted HTML comment string
        """
        return format_metadata_comment(metadata)

    async def translate_markdown(
        self,
        document: str,
        language_code: str,
        md_file_path: str | Path,
        markdown_only: bool = False,
        add_metadata: bool = True,
        add_disclaimer: bool = True,
    ) -> str:
        """Translate markdown document to target language.

        Handles complex documents by splitting into manageable chunks while
        preserving formatting, links, and code blocks.

        Args:
            document: Content of the markdown file
            language_code: Target language code
            md_file_path: Path to the markdown file
            markdown_only: Skip embedded image translation if True
            add_metadata: Whether to add metadata comment at the beginning
            add_disclaimer: Whether to add disclaimer at the end

        Returns:
            str: The translated content with optional metadata and disclaimer.
        """
        md_file_path = Path(md_file_path)

        # Create and format metadata (only if requested)
        metadata_comment = ""
        if add_metadata:
            metadata = self.create_metadata(md_file_path, language_code)
            metadata_comment = self.format_metadata_comment(metadata)

        # Step 1: Replace code blocks and inline code with placeholders
        (
            document_with_placeholders,
            placeholder_map,
        ) = replace_code_blocks(document)

        # Step 2: Split the document into chunks
        document_chunks = process_markdown(document_with_placeholders)

        # Step 3: Generate translation prompts and translate each chunk
        language_name = self.font_config.get_language_name(language_code)
        is_rtl = self.font_config.is_rtl(language_code)
        prompts = [
            generate_prompt_template(language_code, language_name, chunk, is_rtl)
            for chunk in document_chunks
        ]
        results = await self._run_prompts_sequentially(prompts, md_file_path)
        translated_content = "\n".join(results)

        # Step 4: Restore the code blocks and inline code from placeholders
        translated_content = restore_code_blocks(translated_content, placeholder_map)

        # Step 5: Update links
        updated_content = update_links(
            md_file_path,
            translated_content,
            language_code,
            self.root_dir,
            markdown_only=markdown_only,
        )

        # Step 6: Add metadata and disclaimer (only if requested)
        result = updated_content
        if add_metadata:
            result = metadata_comment + result
        if add_disclaimer:
            disclaimer = await self.generate_disclaimer(language_code)
            result = result + "\n\n" + disclaimer

        return result

    async def _run_prompts_sequentially(self, prompts, md_file_path):
        """Execute translation prompts in sequence with timeout protection.

        Args:
            prompts: List of translation prompts to process
            md_file_path: Path to the markdown file being translated

        Returns:
            List of translated text chunks or error messages
        """
        results = []
        for index, prompt in enumerate(prompts):
            try:
                result = await asyncio.wait_for(
                    self._run_prompt(prompt, index + 1, len(prompts)),
                    timeout=self.TRANSLATION_TIMEOUT_SECONDS,
                )
                results.append(result)
            except asyncio.TimeoutError:
                logger.warning(
                    f"Translation timeout for chunk {index + 1} of file '{md_file_path.name}': "
                    f"Request exceeded {self.TRANSLATION_TIMEOUT_SECONDS} seconds. "
                    f"Check your network connection and API response time."
                )
                results.append(
                    f"Translation for chunk {index + 1} of '{md_file_path.name}' skipped due to timeout."
                )
            except Exception as e:
                logger.error(
                    f"Translation failed for chunk {index + 1} of file '{md_file_path.name}': {str(e)}. "
                    f"Check your API configuration and network connection."
                )
                results.append(
                    f"Error translating chunk {index + 1} of '{md_file_path.name}': {str(e)}"
                )
        return results

    @abstractmethod
    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        """Execute a single translation prompt against LLM provider.

        Args:
            prompt: Translation instruction prompt content
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            Translated text content
        """
        pass

    async def generate_disclaimer(self, output_lang: str) -> str:
        """Generate a translated disclaimer notice.

        Creates standardized disclaimer about machine translation quality
        in the target language.

        Args:
            output_lang: Target language code

        Returns:
            Translated disclaimer text
        """
        language_name = self.font_config.get_language_name(output_lang)
        disclaimer_prompt = f""" Translate the following text to {language_name} ({output_lang}).

        **Disclaimer**: 
        This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation."""

        disclaimer = await self._run_prompt(disclaimer_prompt, "disclaimer prompt", 1)

        return disclaimer

    @classmethod
    def create(cls, root_dir: Path = None) -> "MarkdownTranslator":
        """Create appropriate markdown translator based on configured provider.

        Factory method that instantiates the correct implementation based on
        the LLM provider configuration.

        Args:
            root_dir: Root directory of the project for path calculations

        Returns:
            Appropriate translator implementation instance

        Raises:
            ValueError: If no valid LLM provider is configured
        """
        provider = LLMConfig.get_available_provider()
        if provider is None:
            raise ValueError(
                "No valid LLM provider configured. Please check your .env file and ensure AZURE_OPENAI_API_KEY or OPENAI_API_KEY is set."
            )

        if provider == LLMProvider.AZURE_OPENAI:
            from co_op_translator.core.llm.providers.azure.markdown_translator import (
                AzureMarkdownTranslator,
            )

            return AzureMarkdownTranslator(root_dir)
        elif provider == LLMProvider.OPENAI:
            from co_op_translator.core.llm.providers.openai.markdown_translator import (
                OpenAIMarkdownTranslator,
            )

            return OpenAIMarkdownTranslator(root_dir)
        else:
            raise ValueError(
                f"Unsupported LLM provider '{provider}'. Supported providers: AZURE_OPENAI, OPENAI. Please check your configuration."
            )
