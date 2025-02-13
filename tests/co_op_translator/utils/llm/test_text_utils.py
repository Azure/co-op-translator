"""
Test cases for text utility functions.
"""

import pytest
from co_op_translator.utils.llm.text_utils import (
    remove_code_backticks,
    extract_yaml_lines,
    gen_image_translation_prompt,
)


def test_remove_code_backticks():
    """Test removing code backticks from messages."""
    test_cases = [
        ("```python\nprint('hello')\n```", "print('hello')"),
        ("```\nplain text\n```", "plain text"),
        ("no backticks here", "no backticks here"),
        ("```javascript\nconst x = 1;\n```", "const x = 1;"),
    ]

    for input_text, expected in test_cases:
        result = remove_code_backticks(input_text)
        assert result == expected


def test_extract_yaml_lines():
    """Test extracting YAML lines from messages."""
    test_cases = [
        (
            "- text: Hello\n- key: value\n---\nother content",
            ["text: Hello", "key: value"],
        ),
        ("no yaml content", []),
        ("- key1: value1\n- key2: value2", ["key1: value1", "key2: value2"]),
    ]

    for input_text, expected in test_cases:
        result = extract_yaml_lines(input_text)
        result = [line.strip() for line in result]  # Remove whitespace and newlines
        assert result == expected


def test_gen_image_translation_prompt():
    """Test generating image translation prompts."""
    text_data = ["Line 1", "Line 2", "Line 3"]
    language = "ko"

    prompt = gen_image_translation_prompt(text_data, language)

    assert isinstance(prompt, str)
    assert language in prompt
    assert all(line in prompt for line in text_data)


def test_gen_image_translation_prompt_empty():
    """Test generating image translation prompt with empty data."""
    prompt = gen_image_translation_prompt([], "ko")
    assert isinstance(prompt, str)
    assert "ko" in prompt


def test_gen_image_translation_prompt_special_chars():
    """Test generating image translation prompt with special characters."""
    text_data = [
        "Line with *special* chars",
        "Line with [markdown] syntax",
        "Line with <html> tags",
    ]
    prompt = gen_image_translation_prompt(text_data, "ko")

    assert isinstance(prompt, str)
    assert all(line in prompt for line in text_data)
