from co_op_translator.utils.llm.text_utils import (
    remove_code_backticks,
    gen_image_translation_prompt,
    TranslationResponse,
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


def test_gen_image_translation_prompt():
    """Test generating image translation prompts with numbered format."""
    text_data = ["Line 1", "Line 2", "Line 3"]
    language_code = "ko"
    language_name = "Korean"

    prompt = gen_image_translation_prompt(text_data, language_code, language_name)

    assert isinstance(prompt, str)
    assert language_code in prompt
    assert language_name in prompt
    assert "Keep exact same number of lines" in prompt
    assert "1. Line 1" in prompt
    assert "2. Line 2" in prompt
    assert "3. Line 3" in prompt


def test_gen_image_translation_prompt_empty():
    """Test generating image translation prompt with empty data."""
    prompt = gen_image_translation_prompt([], "ko", "Korean")
    assert isinstance(prompt, str)
    assert "ko" in prompt
    assert "Korean" in prompt


def test_gen_image_translation_prompt_special_chars():
    """Test generating image translation prompt with special characters."""
    text_data = [
        "Line with *special* chars",
        "Line with [markdown] syntax",
        "Line with <html> tags",
    ]
    prompt = gen_image_translation_prompt(text_data, "ko", "Korean")

    assert isinstance(prompt, str)
    assert all(line in prompt for line in text_data)


def test_translation_response():
    """Test TranslationResponse Pydantic model."""
    translations = ["Translated line 1", "Translated line 2", "Translated line 3"]
    response = TranslationResponse(translations=translations)
    
    assert response.translations == translations
    assert len(response.translations) == 3
    assert response.translations[0] == "Translated line 1"
