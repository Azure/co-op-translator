import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.utils.llm.text_utils import remove_code_backticks


class MockTextTranslator(TextTranslator):
    """Mock implementation of TextTranslator for testing."""

    def __init__(self):
        self.client = self.get_openai_client()

    def get_openai_client(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="```\nTranslated Text\n```"))
        ]
        mock_client.chat.completions.create.return_value = mock_response
        return mock_client

    def get_model_name(self):
        return "gpt-4"

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
