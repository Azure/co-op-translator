from __future__ import annotations

import logging
import re

import tiktoken
from markdown_it import MarkdownIt

from co_op_translator.config.constants import LINE_BREAK_MARGIN

logger = logging.getLogger(__name__)


def get_tokenizer(encoding_name: str):
    """
    Get the tokenizer based on the encoding name.

    Args:
        encoding_name (str): The name of the encoding.

    Returns:
        tiktoken.Encoding: The tokenizer for the given encoding.
    """
    return tiktoken.get_encoding(encoding_name)


def count_tokens(text: str, tokenizer) -> int:
    """
    Count the number of tokens in a given text using the tokenizer.

    Args:
        text (str): The text to tokenize.
        tokenizer (tiktoken.Encoding): The tokenizer to use.

    Returns:
        int: The number of tokens in the text.
    """
    return len(tokenizer.encode(text))


def split_markdown_content(content: str, max_tokens: int, tokenizer) -> list:
    """
    Split the markdown content into smaller chunks based on code blocks, blockquotes, or HTML,
    preserving markdown structure by splitting at line breaks when possible.

    Args:
        content (str): The markdown content to split.
        max_tokens (int): The maximum number of tokens allowed per chunk.
        tokenizer: The tokenizer to use for counting tokens.

    Returns:
        list: A list of markdown chunks.
    """
    chunks = []

    # Use markdown-it-py to parse content into alternating text/code parts
    parts = _parse_markdown_text_and_code_parts(content)

    current_chunk = []
    current_length = 0

    # Safety margin: allow up to 10% over the max_tokens when trying to find a line break
    # This prevents excessive fragmentation while still respecting token limits
    line_break_margin = min(500, max_tokens * 0.1)  # 10% margin, capped at 500 tokens
    extended_max = max_tokens + line_break_margin

    for part_text, part_type in parts:
        part_tokens = count_tokens(part_text, tokenizer)

        if part_type == "code":
            # Treat code blocks as atomic units
            if current_length + part_tokens <= max_tokens:
                current_chunk.append(part_text)
                current_length += part_tokens
            else:
                if current_chunk:
                    chunks.append("".join(current_chunk))
                    current_chunk = []
                    current_length = 0
                chunks.append(part_text)
        else:
            # Regular text - try to preserve line breaks
            if current_length + part_tokens <= max_tokens:
                current_chunk.append(part_text)
                current_length += part_tokens
            else:
                lines = _group_lines_preserving_list_items(part_text)
                current_line_buffer = []
                current_line_tokens = 0

                for line in lines:
                    line_tokens = count_tokens(line, tokenizer)

                    if (
                        current_length + current_line_tokens + line_tokens
                        <= extended_max
                    ):
                        current_line_buffer.append(line)
                        current_line_tokens += line_tokens
                    else:
                        if current_chunk or current_line_buffer:
                            current_chunk.extend(current_line_buffer)
                            chunks.append("".join(current_chunk))

                        current_chunk = []
                        current_length = 0

                        if line_tokens > max_tokens:
                            if "@@CODE_BLOCK" in line or "@@INLINE_CODE" in line:
                                chunks.append(line)
                            else:
                                chunks.extend(
                                    _split_text_preserving_whitespace(
                                        line, max_tokens, tokenizer
                                    )
                                )
                        else:
                            current_chunk = [line]
                            current_length = line_tokens
                            current_line_buffer = []
                            current_line_tokens = 0

                if current_line_buffer:
                    current_chunk.extend(current_line_buffer)
                    current_length += current_line_tokens

    # Add the final chunk if there's anything left
    if current_chunk:
        chunks.append("".join(current_chunk))

    return chunks


def _split_text_preserving_whitespace(
    text: str, max_tokens: int, tokenizer
) -> list[str]:
    """Split oversized text without normalizing whitespace or line breaks."""
    chunks: list[str] = []
    current_parts: list[str] = []
    current_tokens = 0

    for part in re.findall(r"\s+|\S+", text):
        part_tokens = count_tokens(part, tokenizer)

        if part_tokens > max_tokens:
            if current_parts:
                chunks.append("".join(current_parts))
                current_parts = []
                current_tokens = 0

            chunks.extend(
                _split_unbroken_text_preserving_characters(part, max_tokens, tokenizer)
            )
            continue

        if current_tokens + part_tokens <= max_tokens:
            current_parts.append(part)
            current_tokens += part_tokens
        else:
            chunks.append("".join(current_parts))
            current_parts = [part]
            current_tokens = part_tokens

    if current_parts:
        chunks.append("".join(current_parts))

    return chunks


def _split_unbroken_text_preserving_characters(
    text: str, max_tokens: int, tokenizer
) -> list[str]:
    """Split a single oversized non-whitespace span while preserving all chars."""
    chunks: list[str] = []
    current_chars: list[str] = []
    current_tokens = 0

    for char in text:
        char_tokens = count_tokens(char, tokenizer)

        if current_chars and current_tokens + char_tokens > max_tokens:
            chunks.append("".join(current_chars))
            current_chars = [char]
            current_tokens = char_tokens
        else:
            current_chars.append(char)
            current_tokens += char_tokens

    if current_chars:
        chunks.append("".join(current_chars))

    return chunks


def _group_lines_preserving_list_items(text: str) -> list[str]:
    """Group markdown text while keeping each list item's continuation together."""
    lines = text.splitlines(keepends=True)
    if not lines:
        return []

    grouped_lines: list[str] = []
    idx = 0
    list_item_pattern = re.compile(r"^(\s*)(?:[*+-]|\d+[.)])\s+")

    while idx < len(lines):
        line = lines[idx]
        list_item_match = list_item_pattern.match(line)

        if list_item_match:
            block = [line]
            idx += 1

            while idx < len(lines):
                next_line = lines[idx]
                if next_line.strip() == "":
                    block.append(next_line)
                    idx += 1
                    continue

                next_item_match = list_item_pattern.match(next_line)
                if next_item_match:
                    break

                if next_line.startswith((" ", "\t")):
                    block.append(next_line)
                    idx += 1
                    continue

                break

            grouped_lines.append("".join(block))
            continue

        grouped_lines.append(line)
        idx += 1

    return grouped_lines


def process_markdown(
    content: str, max_tokens=2600, encoding="o200k_base"
) -> list:  # o200k_base is for GPT-4o, cl100k_base is for GPT-4 and GPT-3.5
    """
    Process the markdown content to split it into smaller chunks.

    Args:
        content (str): The markdown content to process.
        max_tokens (int): The maximum number of tokens allowed per chunk.
        encoding (str): The encoding to use for the tokenizer.

    Returns:
        list: A list of processed markdown chunks.
    """
    tokenizer = get_tokenizer(encoding)
    chunks = split_markdown_content(content, max_tokens, tokenizer)

    for i, chunk in enumerate(chunks):
        chunk_tokens = count_tokens(chunk, tokenizer)
        logger.info(f"Chunk {i+1}: Length = {chunk_tokens} tokens")
        if chunk_tokens == max_tokens:
            logger.warning("Warning: This chunk has reached the maximum token limit.")

    return chunks


def _parse_markdown_text_and_code_parts(content: str) -> list[tuple[str, str]]:
    """
    Parse markdown into ordered segments of (text, type) where type is "text" or "code".
    Uses markdown-it-py to detect well-formed fenced code blocks (``` or ~~~).

    Unmatched/partial fences are treated as normal text and will not become code segments.

    Args:
        content: Markdown source text.

    Returns:
        List of tuples: [(segment_text, "text"|"code"), ...]
    """
    md = MarkdownIt("commonmark")
    tokens = md.parse(content)

    # Build mapping from line index to absolute character offset
    lines = content.splitlines(keepends=True)
    offsets = [0]
    for ln in lines:
        offsets.append(offsets[-1] + len(ln))

    code_spans = []  # (start_char, end_char)
    for tok in tokens:
        if tok.type == "fence" and tok.map:
            start_line, end_line = tok.map  # end is exclusive
            start_char = offsets[start_line]
            end_char = offsets[end_line]
            code_spans.append((start_char, end_char))

    code_spans.sort(key=lambda x: x[0])

    parts: list[tuple[str, str]] = []
    pos = 0
    for start_char, end_char in code_spans:
        if pos < start_char:
            parts.append((content[pos:start_char], "text"))
        parts.append((content[start_char:end_char], "code"))
        pos = end_char

    if pos < len(content):
        parts.append((content[pos:], "text"))

    if not parts:
        return [(content, "text")]

    return parts


def process_markdown_with_many_links(content: str, max_links) -> list:
    """
    Process markdown document by splitting it into chunks where each chunk contains max_links or fewer links.

    Args:
        content (str): The markdown content.
        max_links (int): Maximum number of links allowed per chunk.

    Returns:
        list: List of markdown chunks to process.
    """
    lines = content.split("\n")
    chunks = []
    current_chunk = ""
    current_links = 0

    for line in lines:
        line_links = count_links_in_markdown(line)

        if current_links + line_links > max_links:
            chunks.append(current_chunk.strip())
            current_chunk = line + "\n"
            current_links = line_links
        else:
            current_chunk += line + "\n"
            current_links += line_links

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def compare_line_breaks(original_text, translated_text):
    """
    Compare the number of line breaks in the original and translated text
    to determine if the format is broken.
    """
    original_line_breaks = original_text.count("\n")
    translated_line_breaks = translated_text.count("\n")

    if abs(original_line_breaks - translated_line_breaks) > LINE_BREAK_MARGIN:
        return True
    return False


def count_links_in_markdown(content: str) -> int:
    """
    Count the number of links in a markdown document.
    Args:
        content (str): The markdown content.
    Returns:
        int: The number of links in the content.
    """

    link_pattern = re.compile(r"\[.*?\]\(.*?\)")
    return len(link_pattern.findall(content))


def replace_code_blocks(document: str):
    """
    Replace code blocks in the document with placeholders.
    Inline code is left as-is for the LLM to handle naturally.

    Args:
        document (str): The markdown document to process.

    Returns:
        tuple: A tuple containing:
            - The document with placeholders.
            - A dictionary mapping placeholders to their original code.
    """
    placeholder_map = {}

    parts = _parse_markdown_text_and_code_parts(document)

    output_segments = []
    code_index = 0
    for segment, seg_type in parts:
        if seg_type == "code":
            placeholder = f"@@CODE_BLOCK_{code_index}@@"
            output_segments.append(placeholder)
            placeholder_map[placeholder] = segment
            code_index += 1
        else:
            output_segments.append(segment)

    return "".join(output_segments), placeholder_map


def restore_code_blocks(translated_document: str, placeholder_map: dict) -> str:
    """
    Restore code blocks into the translated document from the placeholders.

    Args:
        translated_document (str): The translated document containing placeholders.
        placeholder_map (dict): A dictionary mapping placeholders to their original code.

    Returns:
        str: The translated document with the original code blocks restored.
    """
    for placeholder, code in placeholder_map.items():
        translated_document = translated_document.replace(placeholder, code)

    return translated_document
