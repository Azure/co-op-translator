import pytest
from unittest.mock import patch, MagicMock
from co_op_translator.translators.text_translator import TextTranslator
from co_op_translator.utils.text_utils import gen_image_translation_prompt

@pytest.fixture
def translator():
    return TextTranslator()

@patch('co_op_translator.translators.text_translator.TextTranslator.translate_image_text')
@patch('co_op_translator.translators.text_translator.TextTranslator.get_openai_client')
def test_translate_image_text(mock_get_client, mock_translate_image_text, translator):

    mock_client = MagicMock()
    mock_translate_image_text.return_value = ["línea de ejemplo 1", "línea de ejemplo 2"]

    mock_get_client.return_value = mock_client
    
    text_data = ["example line 1", "example line 2"]
    target_language = "es"
    result = translator.translate_image_text(text_data, target_language)

    expected_result = ["línea de ejemplo 1", "línea de ejemplo 2"]
    assert isinstance(result, list)
    assert result == expected_result

@patch('co_op_translator.translators.text_translator.TextTranslator.translate_text')
@patch('co_op_translator.translators.text_translator.TextTranslator.get_openai_client')
def test_translate_text(mock_get_client, mock_translate_text, translator):

    mock_client = MagicMock()
    mock_translate_text.return_value = "Este es un texto de prueba."
    
    mock_get_client.return_value = mock_client
    
    text = "This is a test text."
    target_language = "es"
    result = translator.translate_text(text, target_language)

    expected_result = "Este es un texto de prueba."
    assert isinstance(result, str)
    assert result == expected_result
