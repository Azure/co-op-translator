"""
This module contains utility functions for handling text and generating prompts.
Functions include generating translation prompts and processing responses from OpenAI.
"""

import re
import logging

logger = logging.getLogger(__name__)


def gen_image_translation_prompt(text_data, language):
    """
    Generate a translation prompt for the given text data.

    Args:
        text_data (list): List of text lines to be translated.
        language (str): Target language for translation.

    Returns:
        str: Generated translation prompt.
    """
    prompt = f"""
    You are a translator that receives a batch of lines in an image. Given the following yaml file, please translate each line into {language}.
    For each line, fill it in with the translation, respecting the context of the text.
    Return only the yaml file, fully filled in.
    """
    for line in text_data:
        prompt += f"- {line}\n"
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


def extract_yaml_lines(message):
    """
    Extract YAML lines from a message.

    Args:
        message (str): The message containing YAML lines.

    Returns:
        list: List of extracted YAML lines.
    """
    lines = message.split("\n")
    yaml_lines = [line[2:] for line in lines if line.startswith("- ")]
    return yaml_lines
