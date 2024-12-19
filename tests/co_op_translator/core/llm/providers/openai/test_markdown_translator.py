import pytest
from unittest.mock import patch, MagicMock
from co_op_translator.core.llm.providers.openai.markdown_translator import OpenAIMarkdownTranslator
from co_op_translator.core import LLMSettings

@pytest.fixture
def translator():
    settings = LLMSettings(
        api_key="test-key",
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    return OpenAIMarkdownTranslator(settings)

@pytest.mark.asyncio
async def test_translate_markdown(translator):
    markdown_text = """
    # Hello
    This is a test
    - Item 1
    - Item 2
    """
    
    # Mock OpenAI response
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="# 안녕하세요\n이것은 테스트입니다\n- 항목 1\n- 항목 2"))
    ]

    with patch('openai.ChatCompletion.acreate', return_value=mock_response):
        result = await translator.translate_markdown(
            markdown_text,
            source_lang="en",
            target_lang="ko"
        )
        
        assert "안녕하세요" in result
        assert "항목" in result
