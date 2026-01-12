"""
This module contains utility functions for handling text and generating prompts.
Functions include generating translation prompts and processing responses from OpenAI.
"""

import re
import logging
from typing import List
from pydantic import BaseModel


class TranslationResponse(BaseModel):
    """Schema for structured translation output."""

    translations: List[str]


logger = logging.getLogger(__name__)

# Pattern to match line number prefixes like "1.", "2.", "[1]", "[2]", etc.
LINE_NUMBER_PREFIX_PATTERN = re.compile(r"^(?:\[\d+\]|\d+\.)\s*")


def strip_line_number_prefix(text: str) -> str:
    """Remove line number prefix (e.g., "1.", "[1]") from text if present.

    Args:
        text: Text that may contain a line number prefix

    Returns:
        Text with line number prefix removed
    """
    return LINE_NUMBER_PREFIX_PATTERN.sub("", text)


def gen_image_translation_prompt(text_data, language_code, language_name):
    """
    Generate a translation prompt for structured output.

    Args:
        text_data (list): List of text lines to be translated.
        language_code (str): Target language code for translation.
        language_name (str): Target language name for translation.

    Returns:
        str: Generated translation prompt for structured output.
    """
    line_count = len(text_data)
    numbered_lines = "\n".join(f"{i}. {line}" for i, line in enumerate(text_data, 1))

    prompt = f"""Translate to {language_name} ({language_code}). Return EXACTLY {line_count} items.

RULES:
- Output translated text only, without line numbers
- Keep symbols/numbers unchanged: +, -, →, 123
- Empty input → empty string ""

{numbered_lines}"""
    return prompt


def remove_code_backticks(message):
    """
    Remove code block backticks from a message.

    Args:
        message (str): The message containing code block backticks.

    Returns:
        str: The message without code block backticks.
    """
    match = re.match(r"```(?:\w+)?\n(.*?)\n```", message, re.DOTALL)
    return match.group(1) if match else message
