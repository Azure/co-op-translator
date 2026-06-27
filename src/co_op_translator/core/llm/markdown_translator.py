from abc import ABC, abstractmethod
import asyncio
import logging
import re
from importlib import resources
from pathlib import Path

import yaml

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.utils.markdown import (
    process_markdown,
    generate_prompt_template,
    _read_language_prompt_template,
    replace_code_blocks,
    restore_code_blocks,
    normalize_cjk_emphasis_markers,
    normalize_internal_anchor_links,
    SPLIT_DELIMITER,
)
from co_op_translator.utils.markdown.frontmatter import (
    get_frontmatter_parser,
)
from co_op_translator.utils.llm.code_comment_translator import (
    translate_comments_in_code_blocks,
)
from co_op_translator.config.font_config import FontConfig
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.utils.common.lang_utils import normalize_language_code
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
)

logger = logging.getLogger(__name__)


class TranslationIncompleteError(RuntimeError):
    """Raised when a provider response does not complete the requested chunk."""


class TranslationContentFilterError(RuntimeError):
    """Raised when a provider stops a translation because of content filtering."""


class MarkdownTranslator(ABC):
    """Define interface for markdown translation services.

    Provides common utilities and abstract methods to be implemented by providers.
    """

    TRANSLATION_TIMEOUT_SECONDS = 1000  # Translation timeout in seconds
    DEFAULT_CHUNK_MAX_TOKENS = 2600
    RECOVERY_CHUNK_MAX_TOKENS = (1300, 650)
    CHUNK_RETRY_ATTEMPTS = 1
    _disclaimer_templates_cache: dict[str, str] | None = None

    def __init__(
        self,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
    ):
        """Initialize translator with project configuration.

        Args:
            root_dir: Root directory of the project for path calculations
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None
        self.font_config = FontConfig()

    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of a file for change detection.

        Args:
            file_path: Path to the file to hash

        Returns:
            MD5 hash of the file content
        """
        return calculate_file_hash(file_path)

    async def translate_markdown(
        self,
        document: str,
        language_code: str,
        source_path: str | Path | None = None,
    ) -> str:
        """Translate markdown content without rewriting project-relative paths.

        The same chunking, placeholder restoration, code-comment translation,
        frontmatter translation, CJK emphasis normalization, and anchor
        normalization used by project translation are preserved here. Only
        project path rewriting is skipped so callers can use this for standalone
        long documents or compose it with a separate path-rewrite pass.
        """

        md_file_path = Path(source_path) if source_path else Path("content.md")

        # Determine language display information once
        language_name = self.font_config.get_language_name(language_code)
        is_rtl = self.font_config.is_rtl(language_code)

        # Step 0: Extract and process frontmatter
        parser = get_frontmatter_parser()
        frontmatter, body = parser.extract_frontmatter(document)

        preserve_fields = {}
        translate_fields = {}
        frontmatter_section = ""

        if frontmatter:
            # Split frontmatter into preserve and translate fields
            preserve_fields, translate_fields = parser.split_fields(frontmatter)
            logger.debug(
                f"Frontmatter split for '{md_file_path.name}': "
                f"{len(preserve_fields)} preserve, {len(translate_fields)} translate"
            )

            # Convert translatable fields to markdown for LLM
            if translate_fields:
                frontmatter_section = parser.extract_translatable_fields_as_markdown(
                    translate_fields
                )
                logger.debug(
                    f"Translatable frontmatter fields for '{md_file_path.name}': "
                    f"{list(translate_fields.keys())}"
                )

        # Use body for translation (frontmatter already extracted)
        document_to_translate = body

        # Step 1: Replace code blocks and inline code with placeholders
        (
            document_with_placeholders,
            placeholder_map,
        ) = replace_code_blocks(document_to_translate)

        # Step 1.5: Translate only the comments inside fenced code blocks
        placeholder_map = await translate_comments_in_code_blocks(
            placeholder_map,
            language_code,
            language_name,
            is_rtl,
            self._run_prompt,
        )

        # Step 2: Split the document into chunks
        document_chunks = process_markdown(
            document_with_placeholders, max_tokens=self.DEFAULT_CHUNK_MAX_TOKENS
        )

        # Step 3: Translate each chunk and recover incomplete chunks without
        # rerunning the whole file.
        results = await self._translate_chunks_with_recovery(
            document_chunks,
            language_code,
            language_name,
            is_rtl,
            md_file_path,
        )
        translated_content = "\n".join(results)

        # Step 4: Normalize emphasis markers for CJK scripts to improve renderer compatibility
        translated_content = normalize_cjk_emphasis_markers(
            translated_content, language_code=language_code
        )

        # Step 4.5: Normalize internal anchor links against translated headings.
        # Run this before restoring code placeholders so code examples are never rewritten.
        translated_content = normalize_internal_anchor_links(
            document, translated_content
        )

        # Step 4.75: Restore the code blocks and inline code from placeholders
        translated_content = restore_code_blocks(translated_content, placeholder_map)

        # Step 5: Translate frontmatter fields if any
        translated_frontmatter_fields = {}
        if frontmatter_section:
            # Translate the frontmatter section
            frontmatter_prompt = generate_prompt_template(
                language_code, language_name, frontmatter_section, is_rtl
            )
            try:
                translated_fm_markdown = await asyncio.wait_for(
                    self._run_prompt(frontmatter_prompt, "frontmatter", 1),
                    timeout=self.TRANSLATION_TIMEOUT_SECONDS,
                )
                # Parse translated fields back from markdown
                translated_frontmatter_fields = (
                    parser.parse_translated_fields_from_markdown(
                        translated_fm_markdown, translate_fields
                    )
                )
                logger.debug(
                    f"Translated frontmatter fields for '{md_file_path.name}': "
                    f"{list(translated_frontmatter_fields.keys())}"
                )
            except asyncio.TimeoutError:
                logger.warning(
                    f"Frontmatter translation timeout for '{md_file_path.name}': "
                    f"Using original values for translatable fields."
                )
                translated_frontmatter_fields = translate_fields
            except Exception as e:
                logger.error(
                    f"Frontmatter translation failed for '{md_file_path.name}': {e}. "
                    f"Using original values for translatable fields."
                )
                translated_frontmatter_fields = translate_fields

        # Step 6: Merge frontmatter and reconstruct
        if frontmatter:
            merged_frontmatter = parser.merge_fields(
                preserve_fields, translated_frontmatter_fields
            )
            translated_content = parser.reconstruct_content(
                merged_frontmatter, translated_content
            )

        return translated_content

    async def _translate_chunks_with_recovery(
        self,
        chunks: list[str],
        language_code: str,
        language_name: str,
        is_rtl: bool,
        md_file_path: Path,
    ) -> list[str]:
        results = []
        total = len(chunks)
        for index, chunk in enumerate(chunks, start=1):
            results.append(
                await self._translate_chunk_with_recovery(
                    chunk,
                    language_code,
                    language_name,
                    is_rtl,
                    md_file_path,
                    chunk_label=str(index),
                    index=index,
                    total=total,
                    split_depth=0,
                )
            )
        return results

    async def _translate_chunk_with_recovery(
        self,
        chunk: str,
        language_code: str,
        language_name: str,
        is_rtl: bool,
        md_file_path: Path,
        chunk_label: str,
        index: int,
        total: int,
        split_depth: int,
    ) -> str:
        last_error: TranslationIncompleteError | None = None

        for attempt in range(self.CHUNK_RETRY_ATTEMPTS + 1):
            try:
                return await self._translate_chunk_once(
                    chunk,
                    language_code,
                    language_name,
                    is_rtl,
                    md_file_path,
                    chunk_label,
                    index,
                    total,
                )
            except TranslationContentFilterError:
                logger.error(
                    "Translation blocked by content filter for chunk %s of file '%s'.",
                    chunk_label,
                    md_file_path.name,
                    exc_info=True,
                )
                raise
            except TranslationIncompleteError as e:
                last_error = e
                if attempt < self.CHUNK_RETRY_ATTEMPTS:
                    logger.warning(
                        "Incomplete translation for chunk %s of file '%s'; retrying same chunk.",
                        chunk_label,
                        md_file_path.name,
                    )
                    continue
                break

        subchunks = self._split_failed_chunk(chunk, split_depth)
        if len(subchunks) <= 1:
            raise TranslationIncompleteError(
                f"Markdown translation remained incomplete for chunk {chunk_label} "
                f"of '{md_file_path.name}', and the chunk could not be split further."
            ) from last_error

        logger.warning(
            "Incomplete translation for chunk %s of file '%s'; retrying as %s smaller chunks.",
            chunk_label,
            md_file_path.name,
            len(subchunks),
        )

        sub_results = []
        for sub_index, subchunk in enumerate(subchunks, start=1):
            sub_results.append(
                await self._translate_chunk_with_recovery(
                    subchunk,
                    language_code,
                    language_name,
                    is_rtl,
                    md_file_path,
                    chunk_label=f"{chunk_label}.{sub_index}",
                    index=sub_index,
                    total=len(subchunks),
                    split_depth=split_depth + 1,
                )
            )

        return "\n".join(sub_results)

    async def _translate_chunk_once(
        self,
        chunk: str,
        language_code: str,
        language_name: str,
        is_rtl: bool,
        md_file_path: Path,
        chunk_label: str,
        index: int,
        total: int,
    ) -> str:
        prompt = generate_prompt_template(language_code, language_name, chunk, is_rtl)
        try:
            return await asyncio.wait_for(
                self._run_prompt(prompt, index, total),
                timeout=self.TRANSLATION_TIMEOUT_SECONDS,
            )
        except asyncio.TimeoutError as exc:
            logger.warning(
                f"Translation timeout for chunk {chunk_label} of file '{md_file_path.name}': "
                f"Request exceeded {self.TRANSLATION_TIMEOUT_SECONDS} seconds. "
                f"Check your network connection and API response time."
            )
            raise TranslationIncompleteError(
                f"Markdown translation timed out for chunk {chunk_label} of '{md_file_path.name}'"
            ) from exc
        except (TranslationIncompleteError, TranslationContentFilterError):
            raise
        except Exception as e:
            logger.error(
                f"Translation failed for chunk {chunk_label} of file '{md_file_path.name}': {str(e)}. "
                f"Check your API configuration and network connection.",
                exc_info=True,
            )
            raise RuntimeError(
                f"Markdown translation failed for chunk {chunk_label} of '{md_file_path.name}': {e}"
            ) from e

    def _split_failed_chunk(self, chunk: str, split_depth: int) -> list[str]:
        if split_depth >= len(self.RECOVERY_CHUNK_MAX_TOKENS):
            return []

        max_tokens = self.RECOVERY_CHUNK_MAX_TOKENS[split_depth]
        subchunks = process_markdown(chunk, max_tokens=max_tokens)
        return [subchunk for subchunk in subchunks if subchunk]

    def _raise_for_finish_reason(
        self,
        finish_reason,
        index: int | str,
        total: int,
    ) -> None:
        reason = self._normalize_finish_reason(finish_reason)
        if reason is None or reason == "stop":
            return

        prompt_ref = f"{index}/{total}"
        if reason in {"length", "max_tokens"}:
            raise TranslationIncompleteError(
                f"Provider stopped markdown translation at prompt {prompt_ref} "
                f"because finish_reason was '{reason}'."
            )

        if reason in {"content_filter", "contentfilter"}:
            raise TranslationContentFilterError(
                f"Provider blocked markdown translation at prompt {prompt_ref} "
                f"because finish_reason was '{reason}'."
            )

        raise TranslationIncompleteError(
            f"Provider stopped markdown translation at prompt {prompt_ref} "
            f"with unsupported finish_reason '{reason}'."
        )

    @staticmethod
    def _normalize_finish_reason(finish_reason) -> str | None:
        if finish_reason is None:
            return None

        value = getattr(finish_reason, "value", finish_reason)
        if value is None:
            return None

        reason = str(value).strip().lower()
        if not reason:
            return None

        return reason.rsplit(".", 1)[-1]

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
                raise RuntimeError(
                    f"Markdown translation timed out for chunk {index + 1} of '{md_file_path.name}'"
                )
            except Exception as e:
                logger.error(
                    f"Translation failed for chunk {index + 1} of file '{md_file_path.name}': {str(e)}. "
                    f"Check your API configuration and network connection.",
                    exc_info=True,
                )
                raise RuntimeError(
                    f"Markdown translation failed for chunk {index + 1} of '{md_file_path.name}': {e}"
                ) from e
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
        """Return a translated disclaimer notice.

        Uses packaged language-specific templates first so contributor-reviewed
        disclaimers remain stable. Falls back to LLM generation only when no
        template exists for the target language.

        Args:
            output_lang: Target language code

        Returns:
            Translated disclaimer text
        """
        disclaimer_template = self._read_disclaimer_template_for_language(output_lang)
        if disclaimer_template:
            return disclaimer_template

        template_text = self._read_disclaimer_template_inner()
        if not template_text:
            return ""

        language_name = self.font_config.get_language_name(output_lang)
        system_text = (
            f"Translate the following text to {language_name} ({output_lang}). "
            "Preserve Markdown syntax and tokens exactly as written; "
            "if links are present, keep Markdown link structure [text](URL) and do not rewrite links as plain text."
        )
        language_template = _read_language_prompt_template(output_lang)
        if language_template:
            system_text += f"\n\n{language_template}"
        user_text = template_text
        disclaimer_prompt = system_text + SPLIT_DELIMITER + user_text

        try:
            disclaimer = await self._run_prompt(
                disclaimer_prompt, "disclaimer prompt", 1
            )
        except Exception as e:
            logger.warning(
                f"Failed to generate disclaimer for language '{output_lang}': {e}"
            )
            return ""

        return disclaimer

    @classmethod
    def _load_disclaimer_templates(cls) -> dict[str, str]:
        """Load packaged language-specific disclaimer templates."""
        if cls._disclaimer_templates_cache is not None:
            return cls._disclaimer_templates_cache

        try:
            with (
                resources.files("co_op_translator.templates")
                .joinpath("disclaimer_templates.yml")
                .open("r", encoding="utf-8") as f
            ):
                raw_templates = yaml.safe_load(f) or {}
        except Exception as e:
            logger.warning(f"Failed to load disclaimer templates: {e}")
            cls._disclaimer_templates_cache = {}
            return cls._disclaimer_templates_cache

        templates: dict[str, str] = {}
        for language_code, disclaimer in raw_templates.items():
            if not isinstance(disclaimer, str):
                continue
            normalized_code = normalize_language_code(str(language_code))
            disclaimer = disclaimer.strip()
            if normalized_code and disclaimer:
                templates[normalized_code] = disclaimer

        cls._disclaimer_templates_cache = templates
        return templates

    def _read_disclaimer_template_for_language(self, output_lang: str) -> str:
        """Read a packaged disclaimer template for the requested language."""
        normalized_lang = normalize_language_code(output_lang)
        return self._load_disclaimer_templates().get(normalized_lang, "")

    def _read_disclaimer_template_inner(self) -> str:
        """Read the packaged disclaimer template and return inner content between markers.

        Returns empty string if the template is missing or markers not found.
        """
        try:
            with (
                resources.files("co_op_translator.templates")
                .joinpath("disclaimer.md")
                .open("r", encoding="utf-8") as f
            ):
                text = f.read()
        except Exception:
            return ""

        start_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER START -->"
        end_marker = "<!-- CO-OP TRANSLATOR DISCLAIMER END -->"
        pattern = re.compile(
            re.escape(start_marker) + r"\s*(.*?)\s*" + re.escape(end_marker), re.DOTALL
        )
        m = pattern.search(text)
        if not m:
            return ""
        return m.group(1).strip()

    @classmethod
    def create(
        cls,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
    ) -> "MarkdownTranslator":
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

            return AzureMarkdownTranslator(
                root_dir=root_dir,
                translations_dir=translations_dir,
                image_dir=image_dir,
                lang_subdir=lang_subdir,
            )
        elif provider == LLMProvider.OPENAI:
            from co_op_translator.core.llm.providers.openai.markdown_translator import (
                OpenAIMarkdownTranslator,
            )

            return OpenAIMarkdownTranslator(
                root_dir=root_dir,
                translations_dir=translations_dir,
                image_dir=image_dir,
                lang_subdir=lang_subdir,
            )
        else:
            raise ValueError(
                f"Unsupported LLM provider '{provider}'. Supported providers: AZURE_OPENAI, OPENAI. Please check your configuration."
            )
