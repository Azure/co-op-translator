import pytest
from pathlib import Path
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from co_op_translator.core.project.project_translator import ProjectTranslator
from unittest.mock import ANY


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary project directory structure."""
    # Create project structure
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "test.md").write_text("# Test Document\nThis is a test.")

    images_dir = tmp_path / "images"
    images_dir.mkdir()
    (images_dir / "test.png").touch()

    translations_dir = tmp_path / "translations"
    translations_dir.mkdir()

    return tmp_path


@pytest.fixture
def project_translator(temp_project_dir):
    """Create a ProjectTranslator instance with mocked dependencies."""
    with (
        patch(
            "co_op_translator.core.llm.text_translator.TextTranslator"
        ) as mock_text_translator,
        patch(
            "co_op_translator.core.llm.markdown_translator.MarkdownTranslator"
        ) as mock_markdown_translator,
        patch(
            "co_op_translator.core.vision.image_translator.ImageTranslator"
        ) as mock_image_translator,
        patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider"
        ) as mock_get_provider,
    ):

        # Setup mock translators and config
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_image_translator.create.return_value = MagicMock()
        mock_get_provider.return_value = "azure"  # Mock LLM provider

        translator = ProjectTranslator("ko ja", root_dir=temp_project_dir)
        return translator


@pytest.mark.asyncio
async def test_translate_markdown(project_translator, temp_project_dir):
    """Test translating a single markdown file."""
    # Setup
    md_file = temp_project_dir / "docs" / "test.md"
    project_translator.markdown_translator.translate_markdown = AsyncMock(
        return_value="# Test Document\nThis is a test in Korean."
    )

    # Execute
    await project_translator.translate_markdown(md_file, "ko")

    # Verify
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    assert translated_file.exists()
    content = translated_file.read_text(encoding="utf-8")
    assert "Test Document" in content


@pytest.mark.asyncio
async def test_translate_image(project_translator, temp_project_dir):
    """Test translating a single image file."""
    # Setup
    image_file = temp_project_dir / "images" / "test.png"
    project_translator.image_translator.translate_image = MagicMock(
        return_value=str(temp_project_dir / "translated_images" / "ko_test.png")
    )

    # Execute
    await project_translator.translate_image(image_file, "ko")

    # Verify
    project_translator.image_translator.translate_image.assert_called_once()


@pytest.mark.asyncio
async def test_translate_all_markdown_files(project_translator, temp_project_dir):
    """Test translating all markdown files."""
    # Setup
    project_translator.markdown_translator.translate_markdown = AsyncMock(
        return_value="# 테스트 문서\n이것은 테스트입니다."
    )

    # Execute
    await project_translator.translate_all_markdown_files()

    # Verify
    for lang in ["ko", "ja"]:
        translated_file = temp_project_dir / "translations" / lang / "docs" / "test.md"
        assert translated_file.exists()


@pytest.mark.asyncio
async def test_translate_all_image_files(project_translator, temp_project_dir):
    """Test translating all image files."""
    # Setup
    (temp_project_dir / "images").mkdir(parents=True, exist_ok=True)
    image_file = temp_project_dir / "images" / "test.png"
    image_file.touch()  # Create a dummy file for testing

    async def mock_translate_image(path, lang, _):
        return str(temp_project_dir / "translated_images" / f"{lang}_test.png")

    project_translator.image_translator.translate_image = AsyncMock(
        side_effect=mock_translate_image
    )

    # Execute
    await asyncio.wait_for(project_translator.translate_all_image_files(), timeout=10)

    # Verify
    assert (
        project_translator.image_translator.translate_image.call_count == 2
    )  # Called for "ko" and "ja"
    project_translator.image_translator.translate_image.assert_any_call(
        image_file, "ko", ANY
    )
    project_translator.image_translator.translate_image.assert_any_call(
        image_file, "ja", ANY
    )


@pytest.mark.asyncio
async def test_translate_project_async(project_translator):
    """Test translating entire project asynchronously."""
    # Setup
    project_translator.translate_all_markdown_files = AsyncMock()
    project_translator.translate_all_image_files = AsyncMock()

    # Execute
    await project_translator.translate_project_async(images=True, markdown=True)

    # Verify
    project_translator.translate_all_markdown_files.assert_called_once()
    project_translator.translate_all_image_files.assert_called_once()


def test_translate_project(project_translator):
    """Test the synchronous translate_project method."""
    # Setup
    with patch.object(asyncio, "run") as mock_run:
        # Execute
        project_translator.translate_project(images=True, markdown=True)

        # Verify
        mock_run.assert_called_once()


@pytest.mark.asyncio
async def test_check_and_retry_translations(project_translator, temp_project_dir):
    """Test checking and retrying translations."""
    # Setup
    md_file = temp_project_dir / "docs" / "test.md"
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    translated_file.parent.mkdir(parents=True)
    translated_file.write_text(
        "# Test\nBroken translation"
    )  # Create a "broken" translation

    project_translator.markdown_translator.translate_markdown = AsyncMock(
        return_value="# 테스트 문서\n이것은 테스트입니다."
    )

    # Execute
    await project_translator.check_and_retry_translations()

    # Verify
    project_translator.markdown_translator.translate_markdown.assert_called()
    assert translated_file.exists()


@pytest.mark.asyncio
async def test_process_api_requests_parallel(project_translator):
    """Test processing API requests in parallel."""
    # Setup
    mock_task1 = AsyncMock()
    mock_task2 = AsyncMock()
    tasks = [mock_task1, mock_task2]

    # Execute
    await project_translator.process_api_requests_parallel(tasks, "Test tasks")

    # No direct verification possible due to queue-based implementation
    # Success is indicated by no exceptions being raised


@pytest.mark.asyncio
async def test_process_api_requests_sequential(project_translator):
    """Test processing API requests sequentially."""
    # Setup
    mock_task1 = AsyncMock()
    mock_task2 = AsyncMock()
    tasks = [lambda: mock_task1(), lambda: mock_task2()]

    # Execute
    await project_translator.process_api_requests_sequential(tasks, "Test tasks")

    # Verify
    mock_task1.assert_called_once()
    mock_task2.assert_called_once()


def test_markdown_only_mode(temp_project_dir):
    """Test ProjectTranslator in markdown-only mode."""
    with (
        patch(
            "co_op_translator.core.llm.text_translator.TextTranslator"
        ) as mock_text_translator,
        patch(
            "co_op_translator.core.llm.markdown_translator.MarkdownTranslator"
        ) as mock_markdown_translator,
        patch(
            "co_op_translator.config.llm_config.config.LLMConfig.get_available_provider"
        ) as mock_get_provider,
    ):

        # Setup mocks
        mock_text_translator.create.return_value = MagicMock()
        mock_markdown_translator.create.return_value = MagicMock()
        mock_get_provider.return_value = "azure"  # Mock LLM provider

        # Create translator in markdown-only mode
        translator = ProjectTranslator(
            "ko", root_dir=temp_project_dir, markdown_only=True
        )

        # Verify
        assert translator.markdown_only is True
        assert translator.image_translator is None
