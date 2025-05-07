"""
This module contains utility functions for handling Markdown content.
Functions include loading language mappings, generating translation prompts,
and processing specific Markdown structures such as comments and URLs.
"""

import os
import re
import tiktoken
from pathlib import Path
from urllib.parse import urlparse
import logging
from co_op_translator.config.constants import (
    SUPPORTED_IMAGE_EXTENSIONS,
    LINE_BREAK_MARGIN,
)
from co_op_translator.utils.common.file_utils import (
    generate_translated_filename,
    get_actual_image_path,
    get_filename_and_extension,
)

logger = logging.getLogger(__name__)


def generate_prompt_template(
    output_lang: str, document_chunk: str, is_rtl: bool
) -> str:
    """
    Generate a translation prompt for a document chunk, considering language direction.

    Args:
        output_lang (str): The target language for translation.
        document_chunk (str): The chunk of the document to be translated.
        is_rtl (bool): Whether the target language is right-to-left.

    Returns:
        str: The generated translation prompt.
    """

    if len(document_chunk.split("\n")) == 1:
        prompt = f"Translate the following text to {output_lang}. NEVER ADD ANY EXTRA CONTENT OR TAGS OUTSIDE THE TRANSLATION. DO NOT ADD '''markdown OR ANY OTHER TAGS. TRANSLATE ONLY WHAT IS GIVEN TO YOU. MAINTAIN MARKDOWN FORMAT.\n\n{document_chunk}"
    else:
        prompt = f"""
        Translate the following markdown file to {output_lang}.
        IMPORTANT RULES:
        1. DO NOT add '''markdown or any other tags around the translation
        2. Make sure the translation does not sound too literal
        3. Translate comments as well
        4. This file is written in Markdown format - do not treat it as XML or HTML
        5. Do not translate:
           - [!NOTE], [!WARNING], [!TIP], [!IMPORTANT], [!CAUTION]
           - Variable names, function names, class names
           - Placeholders like @@INLINE_CODE_x@@ or @@CODE_BLOCK_x@@
           - URLs or paths
        6. Keep all original markdown formatting intact
        7. Return ONLY the translated content without any additional tags or markup
        """

    if is_rtl:
        prompt += "Please write the output from right to left, respecting that this is a right-to-left language.\n"
    else:
        prompt += "Please write the output from left to right.\n"

    prompt += "\n" + document_chunk

    return prompt


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
    Split the markdown content into smaller chunks based on code blocks, blockquotes, or HTML.

    Args:
        content (str): The markdown content to split.
        max_tokens (int): The maximum number of tokens allowed per chunk.
        tokenizer: The tokenizer to use for counting tokens.

    Returns:
        list: A list of markdown chunks.
    """
    chunks = []
    block_pattern = re.compile(
        r"(```[\s\S]*?```|<.*?>|(?:>\s+.*(?:\n>.*|\n(?!\n))*\n?)+)"
    )
    parts = block_pattern.split(content)

    current_chunk = []
    current_length = 0

    for part in parts:
        part_tokens = count_tokens(part, tokenizer)

        if current_length + part_tokens <= max_tokens:
            current_chunk.append(part)
            current_length += part_tokens
        else:
            if block_pattern.match(part):
                if current_chunk:
                    chunks.append("".join(current_chunk))
                chunks.append(part)
                current_chunk = []
                current_length = 0
            else:
                words = part.split()
                for word in words:
                    word_tokens = count_tokens(word + " ", tokenizer)
                    if current_length + word_tokens > max_tokens:
                        chunks.append("".join(current_chunk))
                        current_chunk = [word + " "]
                        current_length = word_tokens
                    else:
                        current_chunk.append(word + " ")
                        current_length += word_tokens

    if current_chunk:
        chunks.append("".join(current_chunk))

    return chunks


def process_markdown(
    content: str, max_tokens=4096, encoding="o200k_base"
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


def update_links(
    md_file_path: Path,
    markdown_string: str,
    language_code: str,
    root_dir: Path,
    markdown_only: bool = False,
) -> str:
    logger.info("Updating links in the markdown file")

    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Update image links
    markdown_string = update_image_links(
        markdown_string,
        md_file_path,
        language_code,
        translations_dir,
        translated_images_dir,
        root_dir,
        markdown_only=markdown_only,
    )

    # Update non-image file links
    markdown_string = update_file_links(
        markdown_string, md_file_path, language_code, translations_dir, root_dir
    )

    # Update translation links
    markdown_string = update_translation_links(
        markdown_string, md_file_path, language_code, translations_dir, root_dir
    )

    return markdown_string


def update_image_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    translated_images_dir: Path,
    root_dir: Path,
    markdown_only: bool = False,
) -> str:
    """
    Update image links in markdown content based on mode and Azure Computer Vision availability.

    Args:
        markdown_string (str): The markdown content to process
        md_file_path (Path): Path to the markdown file being processed
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations
        translated_images_dir (Path): Directory containing translated images
        root_dir (Path): Root directory of the project
        markdown_only (bool): Whether we're in markdown-only mode

    Returns:
        str: Updated markdown content with modified image links
    """
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    image_matches = re.findall(image_pattern, markdown_string)

    # Use original image links if in markdown-only mode
    use_original_images = markdown_only

    if use_original_images:
        logger.info("Using original image links (markdown-only mode)")
    else:
        logger.info("Using translated image links")

    for alt_text, link in image_matches:
        parsed_url = urlparse(link)
        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.info(f"Skipped {link} as it is an email or web URL")
            continue

        path = parsed_url.path
        original_filename, file_ext = get_filename_and_extension(path)

        if file_ext in SUPPORTED_IMAGE_EXTENSIONS:
            logger.info(f"Processing image file {link}")

            try:
                # We'll resolve actual_image_path later based on the path type
                translated_md_dir = (
                    translations_dir
                    / language_code
                    / md_file_path.relative_to(root_dir).parent
                )

                if use_original_images:
                    # Link to original image when in markdown-only mode
                    # For root-relative paths (starting with '/'), keep them unchanged
                    if path.startswith("/"):
                        logger.info(
                            f"Root-relative path detected in markdown-only mode: {path}"
                        )
                        # Keep the original root-relative path as is
                        updated_link = path
                        logger.info(
                            f"Keeping original root-relative path: {updated_link}"
                        )
                    else:
                        # Handle regular relative paths
                        original_linked_file_path = (
                            md_file_path.parent / path
                        ).resolve()
                        updated_link = os.path.relpath(
                            original_linked_file_path, translated_md_dir
                        ).replace(os.path.sep, "/")
                        logger.info(f"Using original image link: {updated_link}")
                else:
                    # Link to translated image when not in markdown-only mode
                    # We need to handle both root-relative and regular paths
                    try:
                        # Pass root_dir to get_actual_image_path to properly handle root-relative paths
                        if path.startswith("/"):
                            # For root-relative paths, we need to use the root_dir
                            logger.info(
                                f"Root-relative path detected in non-markdown-only mode: {path}"
                            )
                            # Use the modified get_actual_image_path that accepts root_dir
                            actual_image_path = get_actual_image_path(
                                path, md_file_path, root_dir
                            )
                        else:
                            # No change for regular paths
                            actual_image_path = get_actual_image_path(
                                path, md_file_path
                            )

                        rel_path = os.path.relpath(
                            translated_images_dir, translated_md_dir
                        )
                        new_filename = generate_translated_filename(
                            actual_image_path, language_code, root_dir
                        )
                        updated_link = os.path.join(rel_path, new_filename).replace(
                            os.path.sep, "/"
                        )
                        logger.info(f"Using translated image link: {updated_link}")
                    except Exception as e:
                        logger.error(f"Error processing image path {path}: {e}")
                        # Fallback to original path if there's an error
                        updated_link = path
                        logger.warning(f"Falling back to original path: {updated_link}")

                old_image_markup = f"![{alt_text}]({link})"
                new_image_markup = f"![{alt_text}]({updated_link})"
                markdown_string = markdown_string.replace(
                    old_image_markup, new_image_markup
                )

            except Exception as e:
                logger.error(f"Error processing image {link}: {e}")
                logger.info(f"Skipping image {link}")
                continue

    return markdown_string


def update_file_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
) -> str:
    file_pattern = r"\[(.*?)\]\((.*?)\)"
    file_matches = re.findall(file_pattern, markdown_string)

    for alt_text, link in file_matches:
        parsed_url = urlparse(link)
        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.info(f"Skipped {link} as it is an email or web URL")
            continue

        path = parsed_url.path
        original_filename, file_ext = get_filename_and_extension(path)

        if file_ext in SUPPORTED_IMAGE_EXTENSIONS:
            logger.info(f"Skipping image file {link}")
            continue

        if file_ext == ".md":
            logger.info(f"Skipping markdown file {link}")
            continue

        logger.info(f"Processing non-image, non-markdown file {link}")
        try:
            translated_md_dir = (
                translations_dir
                / language_code
                / md_file_path.relative_to(root_dir).parent
            )
            original_linked_file_path = (md_file_path.parent / path).resolve()

            updated_link = os.path.relpath(
                original_linked_file_path, translated_md_dir
            ).replace(os.path.sep, "/")

            old_file_markup = f"[{alt_text}]({link})"
            new_file_markup = f"[{alt_text}]({updated_link})"
            markdown_string = markdown_string.replace(old_file_markup, new_file_markup)

            logger.info(f"Updated non-image file markdown: {new_file_markup}")

        except Exception as e:
            logger.error(f"Error processing non-image file {link}: {e}")
            continue

    return markdown_string


def update_translation_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
) -> str:
    logger.info("Updating translation links in the markdown file")

    translation_link_pattern = (
        r"(\[.*?\])\((?:\.?/)?translations/([a-zA-Z\-]+)/README\.md\)"
    )

    def replace_link(match):
        alt_text_with_brackets = match.group(1)
        other_language_code = match.group(2)
        logger.info(
            f"Found language code in link: {other_language_code} with alt text '{alt_text_with_brackets}'"
        )

        other_translated_md_path = (
            translations_dir / other_language_code / "README.md"
        ).resolve()
        logger.debug(
            f"Other translated markdown path (absolute): {other_translated_md_path}"
        )

        current_translated_md_path = (
            translations_dir / language_code / "README.md"
        ).resolve()
        current_md_dir = current_translated_md_path.parent
        logger.debug(f"Current markdown directory (current_md_dir): {current_md_dir}")

        try:
            relative_dir = os.path.relpath(
                other_translated_md_path.parent, current_md_dir
            ).replace(os.path.sep, "/")
            relative_path_to_translation = f"{relative_dir}/README.md"
            logger.info(
                f"Relative path to {other_language_code} translation: {relative_path_to_translation}"
            )

            new_translation_link_markup = (
                f"{alt_text_with_brackets}({relative_path_to_translation})"
            )
            logger.info(
                f"Updated translation link markdown: {new_translation_link_markup}"
            )
            return new_translation_link_markup
        except Exception as e:
            logger.error(
                f"Error updating translation links for {other_language_code}: {e}"
            )
            return match.group(0)

    markdown_string = re.sub(translation_link_pattern, replace_link, markdown_string)

    return markdown_string


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


def replace_code_blocks_and_inline_code(document: str):
    """
    Replace code blocks and inline code in the document with placeholders.

    Args:
        document (str): The markdown document to process.

    Returns:
        tuple: A tuple containing:
            - The document with placeholders.
            - A dictionary mapping placeholders to their original code.
    """
    code_block_pattern = r"```[\s\S]*?```"
    inline_code_pattern = r"`[^`]+`"

    # Replace code blocks
    code_blocks = re.findall(code_block_pattern, document)
    inline_codes = re.findall(inline_code_pattern, document)

    placeholder_map = {}

    # Replace code blocks with placeholders
    for i, code_block in enumerate(code_blocks):
        placeholder = f"@@CODE_BLOCK_{i}@@"
        document = document.replace(code_block, placeholder)
        placeholder_map[placeholder] = code_block

    # Replace inline codes with placeholders
    for i, inline_code in enumerate(inline_codes):
        placeholder = f"@@INLINE_CODE_{i}@@"
        document = document.replace(inline_code, placeholder)
        placeholder_map[placeholder] = inline_code

    return document, placeholder_map


def restore_code_blocks_and_inline_code(
    translated_document: str, placeholder_map: dict
):
    """
    Restore code blocks and inline code into the translated document from the placeholders.

    Args:
        translated_document (str): The translated document containing placeholders.
        placeholder_map (dict): A dictionary mapping placeholders to their original code.

    Returns:
        str: The translated document with the original code blocks and inline code restored.
    """
    for placeholder, code in placeholder_map.items():
        translated_document = translated_document.replace(placeholder, code)
    return translated_document
