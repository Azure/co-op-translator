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
from co_op_translator.config.constants import SUPPORTED_IMAGE_EXTENSIONS
from co_op_translator.utils.file_utils import generate_translated_filename, get_actual_image_path, get_filename_and_extension

logger = logging.getLogger(__name__)

def generate_prompt_template(output_lang: str, document_chunk: str, is_rtl: bool) -> str:
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
        prompt = f"Translate the following text to {output_lang}. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n{document_chunk}"
    else:
        prompt = f"""
        Translate the following markdown file to {output_lang}.
        Make sure the translation does not sound too literal. Make sure you translate comments as well.
        This file is written in Markdown format. Do not treat this as XML or HTML.
        Do not translate any [!NOTE], [!WARNING], [!TIP], [!IMPORTANT], or [!CAUTION].
        Do not translate any entities, such as variable names, function names, or class names, but keep them in the file.
        Do not translate any urls or paths, but keep them in the file.
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
    block_pattern = re.compile(r'(```[\s\S]*?```|<.*?>|(?:>\s+.*(?:\n>.*|\n(?!\n))*\n?)+)')
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
                    chunks.append(''.join(current_chunk))
                chunks.append(part)
                current_chunk = []
                current_length = 0
            else:
                words = part.split()
                for word in words:
                    word_tokens = count_tokens(word + ' ', tokenizer)
                    if current_length + word_tokens > max_tokens:
                        chunks.append(''.join(current_chunk))
                        current_chunk = [word + ' ']
                        current_length = word_tokens
                    else:
                        current_chunk.append(word + ' ')
                        current_length += word_tokens

    if current_chunk:
        chunks.append(''.join(current_chunk))

    return chunks

def process_markdown(content: str, max_tokens=4096, encoding='o200k_base') -> list: # o200k_base is for GPT-4o, cl100k_base is for GPT-4 and GPT-3.5
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

def update_links(md_file_path: Path, markdown_string: str, language_code: str, root_dir: Path) -> str:
    logger.info("Updating links in the markdown file")

    translations_dir = root_dir / 'translations'
    translated_images_dir = root_dir / 'translated_images'

    # Update image links
    markdown_string = update_image_links(markdown_string, md_file_path, language_code, translations_dir, translated_images_dir, root_dir)

    # Update non-image file links
    markdown_string = update_file_links(markdown_string, md_file_path, language_code, translations_dir, root_dir)

    # Update translation links
    markdown_string = update_translation_links(markdown_string, md_file_path, language_code, translations_dir, root_dir)

    return markdown_string

def update_image_links(markdown_string: str, md_file_path: Path, language_code: str, translations_dir: Path, translated_images_dir: Path, root_dir: Path) -> str:
    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    image_matches = re.findall(image_pattern, markdown_string)

    for alt_text, link in image_matches:
        parsed_url = urlparse(link)
        if parsed_url.scheme in ('mailto', 'http', 'https') or '@' in link or link.endswith(('.com', '.org', '.net')):
            logger.info(f"Skipped {link} as it is an email or web URL")
            continue

        path = parsed_url.path
        original_filename, file_ext = get_filename_and_extension(path)

        if file_ext in SUPPORTED_IMAGE_EXTENSIONS:
            logger.info(f"Processing image file {link}")

            try:
                actual_image_path = get_actual_image_path(link, md_file_path)
                translated_md_dir = translations_dir / language_code / md_file_path.relative_to(root_dir).parent
                rel_path = os.path.relpath(translated_images_dir, translated_md_dir)

                new_filename = generate_translated_filename(actual_image_path, language_code, root_dir)
                updated_link = os.path.join(rel_path, new_filename).replace(os.path.sep, '/')

                old_image_markup = f'![{alt_text}]({link})'
                new_image_markup = f'![{alt_text}]({updated_link})'
                markdown_string = markdown_string.replace(old_image_markup, new_image_markup)

                logger.info(f"Updated image markdown: {new_image_markup}")

            except Exception as e:
                logger.error(f"Error processing image {link}: {e}")
                logger.info(f"Skipping image {link}")
                continue

    return markdown_string

def update_file_links(markdown_string: str, md_file_path: Path, language_code: str, translations_dir: Path, root_dir: Path) -> str:
    file_pattern = r'\[(.*?)\]\((.*?)\)'
    file_matches = re.findall(file_pattern, markdown_string)

    for alt_text, link in file_matches:
        parsed_url = urlparse(link)
        if parsed_url.scheme in ('mailto', 'http', 'https') or '@' in link or link.endswith(('.com', '.org', '.net')):
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
            translated_md_dir = translations_dir / language_code / md_file_path.relative_to(root_dir).parent
            original_linked_file_path = (md_file_path.parent / path).resolve()

            updated_link = os.path.relpath(original_linked_file_path, translated_md_dir).replace(os.path.sep, '/')

            old_file_markup = f'[{alt_text}]({link})'
            new_file_markup = f'[{alt_text}]({updated_link})'
            markdown_string = markdown_string.replace(old_file_markup, new_file_markup)

            logger.info(f"Updated non-image file markdown: {new_file_markup}")

        except Exception as e:
            logger.error(f"Error processing non-image file {link}: {e}")
            continue

    return markdown_string

def update_translation_links(markdown_string: str, md_file_path: Path, language_code: str, translations_dir: Path, root_dir: Path) -> str:
    logger.info("Updating translation links in the markdown file")

    translation_link_pattern = r'(\[.*?\])\((?:\.?/)?translations/([a-zA-Z\-]+)/README\.md\)'

    def replace_link(match):
        alt_text_with_brackets = match.group(1)
        other_language_code = match.group(2)
        logger.info(f"Found language code in link: {other_language_code} with alt text '{alt_text_with_brackets}'")

        other_translated_md_path = (translations_dir / other_language_code / 'README.md').resolve()
        logger.debug(f"Other translated markdown path (absolute): {other_translated_md_path}")

        current_translated_md_path = (translations_dir / language_code / 'README.md').resolve()
        current_md_dir = current_translated_md_path.parent
        logger.debug(f"Current markdown directory (current_md_dir): {current_md_dir}")

        try:
            relative_dir = os.path.relpath(other_translated_md_path.parent, current_md_dir).replace(os.path.sep, '/')
            relative_path_to_translation = f"{relative_dir}/README.md"
            logger.info(f"Relative path to {other_language_code} translation: {relative_path_to_translation}")

            new_translation_link_markup = f'{alt_text_with_brackets}({relative_path_to_translation})'
            logger.info(f"Updated translation link markdown: {new_translation_link_markup}")
            return new_translation_link_markup
        except Exception as e:
            logger.error(f"Error updating translation links for {other_language_code}: {e}")
            return match.group(0)

    markdown_string = re.sub(translation_link_pattern, replace_link, markdown_string)

    return markdown_string

def compare_line_breaks(original_text, translated_text):
    """
    Compare the number of line breaks in the original and translated text
    to determine if the format is broken.
    """
    original_line_breaks = original_text.count('\n')
    translated_line_breaks = translated_text.count('\n')

    if abs(original_line_breaks - translated_line_breaks) > 5:  # Allow a margin for disclaimer
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
