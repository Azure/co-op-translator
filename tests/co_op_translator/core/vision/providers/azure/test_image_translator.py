import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from co_op_translator.core.vision.providers.azure.image_translator import AzureVisionTranslator
from co_op_translator.core import VisionSettings

@pytest.fixture
def translator():
    settings = VisionSettings(
        api_key="test-key",
        additional_settings={"endpoint": "https://test.azure.com"}
    )
    return AzureVisionTranslator(settings)

@pytest.mark.asyncio
async def test_translate_image(translator, tmp_path):
    # Create a test image file
    image_path = tmp_path / "test.png"
    image_path.write_bytes(b"test image content")

    # Mock Azure response
    mock_read_response = MagicMock()
    mock_read_response.headers = {"Operation-Location": "operations/123"}

    mock_read_result = MagicMock()
    mock_read_result.status = "succeeded"
    mock_read_result.analyze_result.read_results = [
        MagicMock(
            lines=[
                MagicMock(
                    text="Hello World",
                    appearance=MagicMock(confidence=0.95)
                )
            ]
        )
    ]

    with patch.object(translator.client, 'read_in_stream', return_value=mock_read_response), \
         patch.object(translator.client, 'get_read_result', return_value=mock_read_result):
        
        result = await translator.translate_image(
            image_path,
            source_lang="en",
            target_lang="ko"
        )
        
        assert result["original_text"] == "Hello World"
        assert result["confidence"] == 0.95

@pytest.mark.asyncio
async def test_analyze_image(translator, tmp_path):
    # Create a test image file
    image_path = tmp_path / "test.png"
    image_path.write_bytes(b"test image content")

    # Mock Azure response
    mock_analysis = MagicMock()
    mock_analysis.description.captions = [
        MagicMock(text="A person walking", confidence=0.8)
    ]
    mock_analysis.tags = [
        MagicMock(name="person"),
        MagicMock(name="walking")
    ]
    mock_analysis.objects = [
        MagicMock(object_property="person")
    ]

    with patch.object(translator.client, 'analyze_image_in_stream', return_value=mock_analysis):
        result = await translator.analyze_image(image_path)
        
        assert result["description"] == "A person walking"
        assert result["confidence"] == 0.8
        assert "person" in result["tags"]
        assert "person" in result["objects"]
