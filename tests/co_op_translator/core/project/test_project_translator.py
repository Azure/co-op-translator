import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.core import LLMSettings, VisionSettings
from co_op_translator.core.llm.providers.openai.text_translator import OpenAITextTranslator
from co_op_translator.core.vision.providers.azure.image_translator import AzureVisionTranslator

@pytest.fixture
def project_translator():
    # Setup mock translators
    llm_settings = LLMSettings(api_key="test-key")
    vision_settings = VisionSettings(
        api_key="test-key",
        additional_settings={"endpoint": "https://test.azure.com"}
    )
    
    llm_translator = OpenAITextTranslator(llm_settings)
    vision_translator = AzureVisionTranslator(vision_settings)
    
    return ProjectTranslator(
        llm_translator=llm_translator,
        vision_translator=vision_translator
    )

@pytest.mark.asyncio
async def test_translate_project(project_translator, tmp_path):
    # Create test project structure
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    
    # Create test files
    text_file = project_dir / "test.txt"
    text_file.write_text("Hello World")
    
    md_file = project_dir / "test.md"
    md_file.write_text("# Hello\nWorld")
    
    image_file = project_dir / "test.png"
    image_file.write_bytes(b"test image content")
    
    # Mock translator responses
    async def mock_translate_text(*args, **kwargs):
        return "안녕하세요"
    
    async def mock_translate_markdown(*args, **kwargs):
        return "# 안녕하세요\n세상"
    
    async def mock_translate_image(*args, **kwargs):
        return {
            "original_text": "Hello World",
            "translated_text": "안녕하세요 세상",
            "confidence": 0.9
        }
    
    with patch.object(project_translator.llm_translator, 'translate_text', mock_translate_text), \
         patch.object(project_translator.llm_translator, 'translate_markdown', mock_translate_markdown), \
         patch.object(project_translator.vision_translator, 'translate_image', mock_translate_image):
        
        result = await project_translator.translate_project(
            project_dir,
            source_lang="en",
            target_lang="ko"
        )
        
        assert 'text_files' in result
        assert 'image_files' in result
        assert str(text_file) in result['text_files']
        assert str(image_file) in result['image_files']

@pytest.mark.asyncio
async def test_get_project_structure(project_translator, tmp_path):
    # Create test project structure
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    
    # Create test files
    (project_dir / "test.txt").write_text("Hello")
    (project_dir / "test.md").write_text("# Hello")
    (project_dir / "test.png").write_bytes(b"test")
    
    result = await project_translator.get_project_structure(project_dir)
    
    assert 'files' in result
    assert 'stats' in result
    assert result['stats']['total_files'] == 3
    assert len(result['files']) == 3
    assert all(file.get('path') for file in result['files'])
