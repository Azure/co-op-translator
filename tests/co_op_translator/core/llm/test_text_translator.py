import pytest
from unittest.mock import MagicMock
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.utils.llm.text_utils import TranslationResponse


class MockTextTranslator(TextTranslator):
    """Mock implementation of TextTranslator for testing."""

    def __init__(self):
        self.client = self.get_openai_client()
        # Mock font_config
        self.font_config = MagicMock()
        self.font_config.get_language_name.return_value = "Korean"

    def get_openai_client(self):
        mock_client = MagicMock()

        # Mock for structured outputs (translate_image_text)
        mock_parsed_response = MagicMock()
        mock_parsed_response.choices = [
            MagicMock(
                message=MagicMock(
                    parsed=TranslationResponse(
                        translations=["Translated line 1", "Translated line 2"]
                    )
                )
            )
        ]
        mock_client.chat.completions.parse.return_value = mock_parsed_response

        # Mock for regular text translation
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="```\nTranslated Text\n```"))
        ]
        mock_client.chat.completions.create.return_value = mock_response

        return mock_client

    def get_model_name(self):
        return "gpt-4o"

    def translate_batch(self, texts, target_language):
        """Mock implementation of translate_batch."""
        return [f"Translated: {text}" for text in texts]

    def translate_text(self, text, target_language):
        """Mock implementation of translate_text."""
        return f"Translated: {text}"


@pytest.fixture
def text_translator():
    """
    Fixture to provide an instance of MockTextTranslator for each test.
    """
    return MockTextTranslator()


def test_translate_text(text_translator):
    """
    Test the translate_text method to ensure it translates text correctly.
    """
    text = "Text to translate"
    target_language = "es"
    result = text_translator.translate_text(text, target_language)

    assert result == "Translated: Text to translate"


def test_translate_batch(text_translator):
    """
    Test the translate_batch method to ensure it translates multiple texts correctly.
    """
    texts = ["Line 1", "Line 2"]
    target_language = "es"
    result = text_translator.translate_batch(texts, target_language)

    assert result == ["Translated: Line 1", "Translated: Line 2"]


def test_translate_image_text(text_translator):
    """
    Test the translate_image_text method using structured outputs.
    """
    text_data = ["Line 1", "Line 2"]
    target_language = "ko"
    result = text_translator.translate_image_text(text_data, target_language)

    assert result == ["Translated line 1", "Translated line 2"]
    assert len(result) == len(text_data)
    # Verify structured output was used
    text_translator.client.chat.completions.parse.assert_called_once()


def test_translate_image_text_empty(text_translator):
    """
    Test the translate_image_text method with empty input.
    """
    result = text_translator.translate_image_text([], "ko")
    assert result == []
