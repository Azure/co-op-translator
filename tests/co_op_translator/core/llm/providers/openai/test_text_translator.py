import pytest
from unittest.mock import patch, MagicMock
from co_op_translator.core.llm.providers.openai.text_translator import OpenAITextTranslator
from co_op_translator.core import LLMSettings

@pytest.fixture
def translator():
    settings = LLMSettings(
        api_key="test-key",
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    return OpenAITextTranslator(settings)

@pytest.mark.asyncio
async def test_translate_text(translator):
    # Mock OpenAI response
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="번역된 텍스트"))
    ]

    with patch('openai.ChatCompletion.acreate', return_value=mock_response):
        result = await translator.translate_text(
            "Hello, world!",
            source_lang="en",
            target_lang="ko"
        )
        
        assert result == "번역된 텍스트"
