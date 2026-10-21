from abc import ABC, abstractmethod
import asyncio
from dataclasses import dataclass
import logging
import re
from importlib import resources
from pathlib import Path

import yaml

from co_op_translator.utils.markdown import (
    process_markdown,
    generate_prompt_template,
    _read_language_prompt_template,
    replace_code_blocks,
    replace_markdown_link_destinations,
    restore_code_blocks,
    restore_markdown_link_destinations,
    normalize_cjk_emphasis_markers,
    SPLIT_DELIMITER,
)
from co_op_translator.utils.markdown.frontmatter import (
    get_frontmatter_parser,
)
from co_op_translator.config.font_config import FontConfig
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.utils.common.lang_utils import normalize_language_code
from co_op_translator.utils.common.events import emit_translation_event
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ChunkAnchors:
    """Control markers used to validate and rebuild one translated chunk."""

    text: str
    start_marker: str
    end_marker: str
    line_markers: list[str]
    line_endings: list[str]
    blank_lines: list[bool]


class TranslationIncompleteError(RuntimeError):
    """Raised when a provider response does not complete the requested chunk."""

    def __init__(
        self,
        message: str,
        *,
        expected_line_count: int | None = None,
        actual_line_count: int | None = None,
        first_missing_line: int | None = None,
        first_missing_source_line: int | None = None,
        terminal_suffix_omission: bool = False,
        protected_placeholder_mismatch: bool = False,
        expected_placeholder_count: int | None = None,
        actual_placeholder_count: int | None = None,
        first_mismatched_placeholder: str | None = None,
        translated_prefix: str | None = None,
    ) -> None:
        super().__init__(message)
        self.expected_line_count = expected_line_count
        self.actual_line_count = actual_line_count
        self.first_missing_line = first_missing_line
        self.first_missing_source_line = first_missing_source_line
        self.terminal_suffix_omission = terminal_suffix_omission
        self.protected_placeholder_mismatch = protected_placeholder_mismatch
        self.expected_placeholder_count = expected_placeholder_count
        self.actual_placeholder_count = actual_placeholder_count
        self.first_mismatched_placeholder = first_mismatched_placeholder
        self.translated_prefix = translated_prefix


class TranslationContentFilterError(RuntimeError):
    """Raised when a provider stops a translation because of content filtering."""


class MarkdownTranslator(ABC):
    """Define interface for markdown translation services.

    Provides common utilities and abstract methods to be implemented by providers.
    """

    TRANSLATION_TIMEOUT_SECONDS = 1000  # Translation timeout in seconds
    DEFAULT_CHUNK_MAX_TOKENS = 2600
    RECOVERY_CHUNK_MAX_TOKENS = (1300, 650, 325)
    CHUNK_RETRY_ATTEMPTS = 1
    LINE_MARKER_RE = re.compile(r"@@LINE_(\d{4})@@")
    PROTECTED_PLACEHOLDER_RE = re.compile(
        r"@@(?:CODE_BLOCK|INLINE_CODE|LINK_DESTINATION)_\d+@@"
    )
    _disclaimer_templates_cache: dict[str, str] | None = None

    def __init__(
        self,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
        context: str | None = None,
    ):
        """Initialize translator with project configuration.

        Args:
            root_dir: Root directory of the project for path calculations
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.image_dir = image_dir
        self.lang_subdir = Path(lang_subdir) if lang_subdir else None
        self.context = context
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

        The same chunking, literal protection, placeholder restoration,
        frontmatter translation, and CJK emphasis normalization used by project
        translation are preserved here. Only project path rewriting is skipped so
        callers can use this for standalone long documents or compose it with a
        separate path-rewrite pass.
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
        frontmatter_link_destination_map: dict[str, str] = {}

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
                (
                    frontmatter_section,
                    frontmatter_link_destination_map,
                ) = replace_markdown_link_destinations(frontmatter_section)
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

        document_with_placeholders, link_destination_map = (
            replace_markdown_link_destinations(document_with_placeholders)
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
        translated_content = "".join(results)

        # Step 4: Normalize emphasis markers for CJK scripts to improve renderer compatibility
        translated_content = normalize_cjk_emphasis_markers(
            translated_content, language_code=language_code
        )

        # Step 4.5: Restore protected link destinations and code blocks.
        translated_content = restore_markdown_link_destinations(
            translated_content, link_destination_map
        )
        translated_content = restore_code_blocks(translated_content, placeholder_map)

        # Step 5: Translate frontmatter fields if any
        translated_frontmatter_fields = {}
        if frontmatter_section:
            # Translate the frontmatter section
            frontmatter_prompt = generate_prompt_template(
                language_code,
                language_name,
                frontmatter_section,
                is_rtl,
                context=self.context,
            )
            try:
                translated_fm_markdown = await asyncio.wait_for(
                    self._run_prompt(frontmatter_prompt, "frontmatter", 1),
                    timeout=self.TRANSLATION_TIMEOUT_SECONDS,
                )
                translated_fm_markdown = restore_markdown_link_destinations(
                    translated_fm_markdown, frontmatter_link_destination_map
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
        source_line_start = 1
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
                    source_line_start=source_line_start,
                )
            )
            source_line_start += self._count_line_breaks(chunk)
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
        source_line_start: int,
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
                    source_line_start,
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
                if self._verified_prefix_line_count(
                    e
                ) > self._verified_prefix_line_count(last_error):
                    last_error = e
                elif last_error is None:
                    last_error = e
                if attempt < self.CHUNK_RETRY_ATTEMPTS:
                    emit_translation_event(
                        "block_retry",
                        file=str(md_file_path),
                        language=language_code,
                        block=chunk_label,
                        attempt=attempt + 2,
                        metadata=self._incomplete_error_metadata(e),
                    )
                    logger.warning(
                        "Incomplete translation for chunk %s of file '%s'; "
                        "retrying same chunk: %s",
                        chunk_label,
                        md_file_path.name,
                        e,
                    )
                    continue
                break

        if (
            last_error
            and last_error.terminal_suffix_omission
            and last_error.translated_prefix is not None
            and last_error.first_missing_line is not None
        ):
            source_lines = chunk.splitlines(keepends=True)
            suffix_start = last_error.first_missing_line - 1
            source_prefix = "".join(source_lines[:suffix_start])
            source_suffix = "".join(source_lines[suffix_start:])
            if source_prefix and source_suffix:
                logger.warning(
                    "Incomplete translation for chunk %s of file '%s'; "
                    "preserving %s translated lines and retrying only the missing suffix.",
                    chunk_label,
                    md_file_path.name,
                    suffix_start,
                )
                emit_translation_event(
                    "block_retry",
                    file=str(md_file_path),
                    language=language_code,
                    block=chunk_label,
                    attempt=self.CHUNK_RETRY_ATTEMPTS + 2,
                    metadata=self._incomplete_error_metadata(last_error),
                )
                translated_suffix = await self._translate_chunk_with_recovery(
                    source_suffix,
                    language_code,
                    language_name,
                    is_rtl,
                    md_file_path,
                    chunk_label=f"{chunk_label}.suffix",
                    index=index,
                    total=total,
                    split_depth=split_depth,
                    source_line_start=(
                        source_line_start + self._count_line_breaks(source_prefix)
                    ),
                )
                return last_error.translated_prefix + translated_suffix

        subchunks = self._split_failed_chunk(chunk, split_depth, last_error)
        if len(subchunks) <= 1:
            raise TranslationIncompleteError(
                f"Markdown translation remained incomplete for chunk {chunk_label} "
                f"of '{md_file_path.name}', and the chunk could not be split further.",
                expected_line_count=(
                    last_error.expected_line_count if last_error else None
                ),
                actual_line_count=(
                    last_error.actual_line_count if last_error else None
                ),
                first_missing_line=(
                    last_error.first_missing_line if last_error else None
                ),
                first_missing_source_line=(
                    last_error.first_missing_source_line if last_error else None
                ),
                terminal_suffix_omission=(
                    last_error.terminal_suffix_omission if last_error else False
                ),
                protected_placeholder_mismatch=(
                    last_error.protected_placeholder_mismatch if last_error else False
                ),
                expected_placeholder_count=(
                    last_error.expected_placeholder_count if last_error else None
                ),
                actual_placeholder_count=(
                    last_error.actual_placeholder_count if last_error else None
                ),
                first_mismatched_placeholder=(
                    last_error.first_mismatched_placeholder if last_error else None
                ),
                translated_prefix=(
                    last_error.translated_prefix if last_error else None
                ),
            ) from last_error

        logger.warning(
            "Incomplete translation for chunk %s of file '%s'; retrying as %s smaller chunks.",
            chunk_label,
            md_file_path.name,
            len(subchunks),
        )
        emit_translation_event(
            "block_retry",
            file=str(md_file_path),
            language=language_code,
            block=chunk_label,
            attempt=self.CHUNK_RETRY_ATTEMPTS + 2,
            metadata=self._incomplete_error_metadata(last_error),
        )

        sub_results = []
        subchunk_source_line_start = source_line_start
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
                    source_line_start=subchunk_source_line_start,
                )
            )
            subchunk_source_line_start += self._count_line_breaks(subchunk)

        return "".join(sub_results)

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
        source_line_start: int,
    ) -> str:
        anchored_chunk = self._add_chunk_anchors(chunk, chunk_label)
        prompt = generate_prompt_template(
            language_code,
            language_name,
            anchored_chunk.text,
            is_rtl,
            context=self.context,
        )
        try:
            translated = await asyncio.wait_for(
                self._run_prompt(prompt, index, total),
                timeout=self.TRANSLATION_TIMEOUT_SECONDS,
            )
            try:
                translated_chunk = self._strip_chunk_anchors(
                    translated,
                    anchored_chunk,
                    md_file_path,
                    chunk_label,
                    source_line_start,
                )
            except TranslationIncompleteError as exc:
                if (
                    exc.terminal_suffix_omission
                    and exc.translated_prefix is not None
                    and exc.actual_line_count
                ):
                    source_prefix = "".join(
                        chunk.splitlines(keepends=True)[: exc.actual_line_count]
                    )
                    self._validate_protected_placeholders(
                        source_prefix,
                        exc.translated_prefix,
                        md_file_path,
                        chunk_label,
                        source_line_start,
                    )
                raise
            self._validate_protected_placeholders(
                chunk,
                translated_chunk,
                md_file_path,
                chunk_label,
                source_line_start,
            )
            return translated_chunk
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

    def _add_chunk_anchors(self, chunk: str, chunk_label: str) -> ChunkAnchors:
        """Wrap a markdown chunk with completion and per-line anchor markers."""
        safe_label = self._safe_chunk_label(chunk_label)
        start_marker = f"@@COOP_CHUNK_START:{safe_label}@@"
        end_marker = f"@@COOP_CHUNK_END:{safe_label}@@"

        line_markers: list[str] = []
        line_endings: list[str] = []
        blank_lines: list[bool] = []
        anchored_parts = [start_marker, "\n"]

        for line_index, source_line in enumerate(chunk.splitlines(keepends=True), 1):
            line_content, line_ending = self._split_line_ending(source_line)
            line_marker = f"@@LINE_{line_index:04d}@@"
            line_markers.append(line_marker)
            line_endings.append(line_ending)
            blank_lines.append(line_content == "")

            separator = " " if line_content else ""
            anchored_parts.append(f"{line_marker}{separator}{line_content}")
            anchored_parts.append(line_ending or "\n")

        anchored_parts.append(end_marker)
        return ChunkAnchors(
            text="".join(anchored_parts),
            start_marker=start_marker,
            end_marker=end_marker,
            line_markers=line_markers,
            line_endings=line_endings,
            blank_lines=blank_lines,
        )

    def _strip_chunk_anchors(
        self,
        translated: str,
        anchors: ChunkAnchors,
        md_file_path: Path,
        chunk_label: str,
        source_line_start: int = 1,
    ) -> str:
        """Validate completion/line anchors and remove them from a translation."""
        start_pos = translated.find(anchors.start_marker)
        end_pos = translated.find(anchors.end_marker)
        if start_pos == -1 or end_pos == -1 or end_pos < start_pos:
            raise TranslationIncompleteError(
                f"Markdown translation for chunk {chunk_label} of '{md_file_path.name}' "
                "did not preserve required chunk envelope markers."
            )

        body = translated[start_pos + len(anchors.start_marker) : end_pos]
        marker_matches = list(self.LINE_MARKER_RE.finditer(body))
        actual_markers = [match.group(0) for match in marker_matches]
        if actual_markers != anchors.line_markers:
            is_prefix = actual_markers == anchors.line_markers[: len(actual_markers)]
            terminal_suffix_omission = is_prefix and len(actual_markers) < len(
                anchors.line_markers
            )
            first_missing_line = (
                len(actual_markers) + 1 if terminal_suffix_omission else None
            )
            first_missing_source_line = (
                source_line_start + first_missing_line - 1
                if first_missing_line is not None
                else None
            )
            detail = (
                f"preserved {len(actual_markers)} of "
                f"{len(anchors.line_markers)} line anchors"
            )
            if first_missing_line is not None:
                detail += (
                    f"; first missing chunk line is {first_missing_line} "
                    f"(source line {first_missing_source_line})"
                )
            translated_prefix = (
                self._rebuild_anchored_lines(body, marker_matches, anchors)
                if terminal_suffix_omission and marker_matches
                else None
            )
            raise TranslationIncompleteError(
                f"Markdown translation for chunk {chunk_label} of '{md_file_path.name}' "
                f"did not preserve required line anchor markers in order ({detail}).",
                expected_line_count=len(anchors.line_markers),
                actual_line_count=len(actual_markers),
                first_missing_line=first_missing_line,
                first_missing_source_line=first_missing_source_line,
                terminal_suffix_omission=terminal_suffix_omission,
                translated_prefix=translated_prefix,
            )

        return self._rebuild_anchored_lines(body, marker_matches, anchors)

    def _rebuild_anchored_lines(
        self,
        body: str,
        marker_matches: list[re.Match],
        anchors: ChunkAnchors,
    ) -> str:
        rebuilt_lines: list[str] = []
        for line_index, match in enumerate(marker_matches):
            segment_start = match.end()
            segment_end = (
                marker_matches[line_index + 1].start()
                if line_index + 1 < len(marker_matches)
                else len(body)
            )
            translated_line = body[segment_start:segment_end]
            if anchors.blank_lines[line_index]:
                rebuilt_lines.append(anchors.line_endings[line_index])
                continue

            cleaned_line = self._clean_anchored_line_segment(translated_line)
            rebuilt_lines.append(cleaned_line + anchors.line_endings[line_index])

        return "".join(rebuilt_lines)

    def _validate_protected_placeholders(
        self,
        source_chunk: str,
        translated_chunk: str,
        md_file_path: Path,
        chunk_label: str,
        source_line_start: int,
    ) -> None:
        """Reject silent loss, duplication, or reordering of protected content."""
        expected = self.PROTECTED_PLACEHOLDER_RE.findall(source_chunk)
        actual = self.PROTECTED_PLACEHOLDER_RE.findall(translated_chunk)
        if actual == expected:
            return

        mismatch_index = next(
            (
                index
                for index, (expected_marker, actual_marker) in enumerate(
                    zip(expected, actual)
                )
                if expected_marker != actual_marker
            ),
            min(len(expected), len(actual)),
        )
        first_mismatched_placeholder = (
            expected[mismatch_index] if mismatch_index < len(expected) else None
        )
        first_missing_line = None
        first_missing_source_line = None
        if first_mismatched_placeholder is not None:
            marker_offset = source_chunk.find(first_mismatched_placeholder)
            first_missing_line = (
                self._count_line_breaks(source_chunk[:marker_offset]) + 1
            )
            first_missing_source_line = source_line_start + first_missing_line - 1

        detail = f"preserved {len(actual)} of {len(expected)} protected placeholders"
        if first_mismatched_placeholder is not None:
            detail += f"; first mismatch is {first_mismatched_placeholder}"
        if first_missing_source_line is not None:
            detail += f" on source line {first_missing_source_line}"

        raise TranslationIncompleteError(
            f"Markdown translation for chunk {chunk_label} of '{md_file_path.name}' "
            f"did not preserve protected placeholders in order ({detail}).",
            first_missing_line=first_missing_line,
            first_missing_source_line=first_missing_source_line,
            protected_placeholder_mismatch=True,
            expected_placeholder_count=len(expected),
            actual_placeholder_count=len(actual),
            first_mismatched_placeholder=first_mismatched_placeholder,
        )

    @staticmethod
    def _safe_chunk_label(chunk_label: str) -> str:
        safe_label = re.sub(r"[^A-Za-z0-9_.-]", "_", chunk_label).strip("._-")
        return safe_label or "chunk"

    @staticmethod
    def _split_line_ending(line: str) -> tuple[str, str]:
        if line.endswith("\r\n"):
            return line[:-2], "\r\n"
        if line.endswith("\n"):
            return line[:-1], "\n"
        if line.endswith("\r"):
            return line[:-1], "\r"
        return line, ""

    @staticmethod
    def _clean_anchored_line_segment(segment: str) -> str:
        had_line_break = "\n" in segment or "\r" in segment
        cleaned = segment.strip("\r\n")
        cleaned = re.sub(r"[ \t]*(?:\r\n|\r|\n)[ \t]*", " ", cleaned)
        if cleaned.startswith(" "):
            cleaned = cleaned[1:]
        if not had_line_break and cleaned.endswith(" "):
            cleaned = cleaned[:-1]
        return cleaned

    def _split_failed_chunk(
        self,
        chunk: str,
        split_depth: int,
        error: TranslationIncompleteError | None = None,
    ) -> list[str]:
        if error and error.first_missing_line is not None:
            targeted_subchunks = self._split_chunk_at_line(
                chunk, error.first_missing_line
            )
            if len(targeted_subchunks) > 1:
                return targeted_subchunks

        for max_tokens in self.RECOVERY_CHUNK_MAX_TOKENS[split_depth:]:
            subchunks = [
                subchunk
                for subchunk in process_markdown(chunk, max_tokens=max_tokens)
                if subchunk
            ]
            if len(subchunks) > 1:
                return subchunks

        # Markdown-aware splitting can intentionally keep a large list, table, or
        # paragraph together even when it exceeds the requested token limit. If a
        # provider silently omits part of that block, retrying the same indivisible
        # chunk cannot recover. Fall back to a lossless line-boundary split so every
        # smaller request still carries the exact source lines and can be joined
        # without changing the document.
        return self._split_chunk_by_lines(chunk)

    @staticmethod
    def _split_chunk_at_line(chunk: str, line_number: int | None) -> list[str]:
        """Split immediately before a model-omitted source line."""
        if line_number is None or line_number <= 1:
            return []

        lines = chunk.splitlines(keepends=True)
        split_at = line_number - 1
        if split_at >= len(lines):
            return []

        subchunks = ["".join(lines[:split_at]), "".join(lines[split_at:])]
        if not all(subchunks) or "".join(subchunks) != chunk:
            return []
        return subchunks

    @staticmethod
    def _incomplete_error_metadata(
        error: TranslationIncompleteError | None,
    ) -> dict[str, int | str | bool]:
        if error is None:
            return {"reason": "incomplete_translation"}

        metadata: dict[str, int | str | bool] = {
            "reason": (
                "protected_placeholder_mismatch"
                if error.protected_placeholder_mismatch
                else (
                    "terminal_suffix_omission"
                    if error.terminal_suffix_omission
                    else "incomplete_translation"
                )
            )
        }
        if error.expected_line_count is not None:
            metadata["expected_line_count"] = error.expected_line_count
        if error.actual_line_count is not None:
            metadata["actual_line_count"] = error.actual_line_count
        if error.first_missing_line is not None:
            metadata["first_missing_chunk_line"] = error.first_missing_line
        if error.first_missing_source_line is not None:
            metadata["first_missing_source_line"] = error.first_missing_source_line
        if error.expected_placeholder_count is not None:
            metadata["expected_placeholder_count"] = error.expected_placeholder_count
        if error.actual_placeholder_count is not None:
            metadata["actual_placeholder_count"] = error.actual_placeholder_count
        if error.first_mismatched_placeholder is not None:
            metadata["first_mismatched_placeholder"] = (
                error.first_mismatched_placeholder
            )
        return metadata

    @staticmethod
    def _verified_prefix_line_count(
        error: TranslationIncompleteError | None,
    ) -> int:
        if (
            error is None
            or not error.terminal_suffix_omission
            or error.translated_prefix is None
        ):
            return -1
        return error.actual_line_count or 0

    @staticmethod
    def _count_line_breaks(chunk: str) -> int:
        """Count source line advances without double-counting CRLF."""
        return chunk.count("\n") + chunk.count("\r") - chunk.count("\r\n")

    @staticmethod
    def _split_chunk_by_lines(chunk: str) -> list[str]:
        """Bisect a failed chunk without changing or dropping source text."""
        lines = chunk.splitlines(keepends=True)
        if len(lines) <= 1:
            return []

        midpoint = len(lines) // 2
        paragraph_boundaries = [
            index for index in range(1, len(lines)) if not lines[index - 1].strip()
        ]
        split_at = (
            min(
                paragraph_boundaries,
                key=lambda index: (abs(index - midpoint), index),
            )
            if paragraph_boundaries
            else midpoint
        )

        subchunks = ["".join(lines[:split_at]), "".join(lines[split_at:])]
        if not all(subchunks) or "".join(subchunks) != chunk:
            return []
        return subchunks

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
        context: str | None = None,
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
                "No valid LLM provider configured. Please check your .env file and "
                "configure Azure OpenAI, OpenAI, or Anthropic credentials."
            )

        from co_op_translator.core.llm.model_client_translator import (
            ModelClientMarkdownTranslator,
        )

        return ModelClientMarkdownTranslator(
            provider=provider,
            root_dir=root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
            context=context,
        )
