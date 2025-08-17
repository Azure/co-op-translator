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
    prompt = f"Translate each line to {language_name} ({language_code}). Keep exact same number of lines and preserve original formatting:\n\n"
    for line in text_data:
        prompt += f"{line}\n"
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
