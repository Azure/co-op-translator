import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from pathlib import Path

from co_op_translator.core.llm.markdown_translator import (
    MarkdownTranslator,
)
from co_op_translator.config.font_config import FontConfig

class MockMarkdownTranslator(MarkdownTranslator):
    """Mock class for testing MarkdownTranslator."""

    def __init__(self, root_dir: Path):
        """Initialize mock translator."""
        self.root_dir = root_dir
        self.font_config = FontConfig()

    def validate_input(self, document: str, language_code: str):
        """Validate input parameters."""
        if not isinstance(document, str):
            raise ValueError("document must be a string")
        if not document:
            raise ValueError("Empty document")
        if not language_code or language_code == "invalid":
            raise ValueError("Invalid language code")

    async def translate_markdown(self, document: str, language_code: str, md_file_path: str, markdown_only: bool = False) -> str:
        """Mock implementation of translate_markdown."""
        from co_op_translator.utils.llm.markdown_utils import (
            process_markdown,
            update_links,
            generate_prompt_template,
            count_links_in_markdown,
            process_markdown_with_many_links,
            replace_code_blocks_and_inline_code,
            restore_code_blocks_and_inline_code
        )

        self.validate_input(document, language_code)
        md_file_path = Path(md_file_path)

        # Step 1: Replace code blocks and inline code with placeholders
        document_with_placeholders, placeholder_map = replace_code_blocks_and_inline_code(document)

        # Step 2: Split the document into chunks and generate prompts
        link_count = count_links_in_markdown(document_with_placeholders)
        if link_count > 30:
            document_chunks = process_markdown_with_many_links(document_with_placeholders, 30)
        else:
            document_chunks = process_markdown(document_with_placeholders)

        # Step 3: Generate translation prompts and translate each chunk
        is_rtl = self.font_config.is_rtl(language_code)  # Call is_rtl() once and store result
        prompts = [generate_prompt_template(language_code, chunk, is_rtl) for chunk in document_chunks]
        results = await self._run_prompts_sequentially(prompts)
        translated_content = "\n".join(results)

        # Step 4: Restore the code blocks and inline code from placeholders
        translated_content = restore_code_blocks_and_inline_code(translated_content, placeholder_map)

        # Step 5: Update links and add disclaimer
        updated_content = update_links(md_file_path, translated_content, language_code, self.root_dir, markdown_only=markdown_only)
        disclaimer = await self.generate_disclaimer(language_code)
        updated_content += "\n\n" + disclaimer

        return updated_content

    async def _run_prompt(self, prompt: str, chunk_index: int = 1, total_chunks: int = 1) -> str:
        """Mock implementation of _run_prompt."""
        return f"Translated: {prompt}"

    async def _run_prompts_sequentially(self, prompts: list[str]) -> list[str]:
        """Mock implementation of _run_prompts_sequentially."""
        results = []
        for i, prompt in enumerate(prompts, 1):
            result = await self._run_prompt(prompt, i, len(prompts))
            results.append(result)
        return results

    async def generate_disclaimer(self, language_code: str) -> str:
        """Mock implementation of generate_disclaimer."""
        return "Translated Disclaimer"

TEST_MD_CONTENT = """
# Sample Markdown

This is a sample markdown document with links and code blocks.

```python
def hello_world():
    print("Hello, world!")
```
"""

TRANSLATED_CONTENT = "Translated Content"
TRANSLATED_DISCLAIMER = "Translated Disclaimer"

TEST_MD_WITH_MANY_LINKS = """
# Document with Many Links

[Link 1](link1.md)
[Link 2](link2.md)
[Link 3](link3.md)
[Link 4](link4.md)
[Link 5](link5.md)
[Link 6](link6.md)
[Link 7](link7.md)
[Link 8](link8.md)
[Link 9](link9.md)
[Link 10](link10.md)
[Link 11](link11.md)
"""

TEST_MD_WITH_VARIOUS_ELEMENTS = '''
# Complex Markdown Document

## Table Section
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

## Image Section
![Image 1](image1.png)
![Image 2](image2.jpg)

## Code Section
```python
def example():
    return "This is a code block"
```

`inline code`

## List Section
1. First item
2. Second item
   - Nested item
   - Another nested item
'''

@pytest.fixture
def markdown_translator(tmp_path):
    """
    Create a mock markdown translator for testing.
    """
    return MockMarkdownTranslator(root_dir=tmp_path)

@patch("co_op_translator.utils.llm.markdown_utils.replace_code_blocks_and_inline_code")
@patch("co_op_translator.utils.llm.markdown_utils.count_links_in_markdown")
@patch("co_op_translator.utils.llm.markdown_utils.process_markdown_with_many_links")
@patch("co_op_translator.utils.llm.markdown_utils.process_markdown")
@patch("co_op_translator.utils.llm.markdown_utils.generate_prompt_template")
@patch("co_op_translator.utils.llm.markdown_utils.restore_code_blocks_and_inline_code")
@patch("co_op_translator.utils.llm.markdown_utils.update_links")
@patch("co_op_translator.config.font_config.FontConfig.is_rtl")
@patch.object(MockMarkdownTranslator, "generate_disclaimer")
@patch.object(MockMarkdownTranslator, "_run_prompts_sequentially")
@pytest.mark.asyncio
async def test_translate_markdown(
    mock_run_prompts_sequentially,
    mock_generate_disclaimer,
    mock_is_rtl,
    mock_update_links,
    mock_restore_code_blocks,
    mock_generate_prompt_template,
    mock_process_markdown,
    mock_process_markdown_with_many_links,
    mock_count_links_in_markdown,
    mock_replace_code_blocks,
    markdown_translator,
):
    """
    Test the translate_markdown method to ensure it translates markdown content correctly.
    """
    mock_replace_code_blocks.return_value = (TEST_MD_CONTENT, {})
    mock_count_links_in_markdown.return_value = 5
    mock_process_markdown.return_value = ["Chunk 1"]
    mock_generate_prompt_template.return_value = "Generated Prompt"
    mock_run_prompts_sequentially.return_value = ["Translated Chunk"]
    mock_restore_code_blocks.return_value = TRANSLATED_CONTENT
    mock_update_links.return_value = TRANSLATED_CONTENT
    mock_generate_disclaimer.return_value = TRANSLATED_DISCLAIMER
    mock_is_rtl.return_value = False

    result = await markdown_translator.translate_markdown(
        document=TEST_MD_CONTENT,
        language_code="es",
        md_file_path="test.md",
        markdown_only=False
    )

    assert result == TRANSLATED_CONTENT + "\n\n" + TRANSLATED_DISCLAIMER
    mock_replace_code_blocks.assert_called_once_with(TEST_MD_CONTENT)
    mock_count_links_in_markdown.assert_called_once_with(TEST_MD_CONTENT)
    mock_process_markdown.assert_called_once_with(TEST_MD_CONTENT)
    mock_generate_prompt_template.assert_called_once_with("es", "Chunk 1", False)
    mock_restore_code_blocks.assert_called_once_with("Translated Chunk", {})
    mock_update_links.assert_called_once_with(Path("test.md"), TRANSLATED_CONTENT, "es", markdown_translator.root_dir, markdown_only=False)
    mock_generate_disclaimer.assert_called_once_with("es")

@patch("time.time", side_effect=[0, 1])
@patch("asyncio.sleep", new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_run_prompt(
    mock_sleep,
    mock_time,
    markdown_translator
):
    """
    Test the _run_prompt method.
    """
    result = await markdown_translator._run_prompt("Test prompt", 1, 2)
    assert result == "Translated: Test prompt"
    assert mock_sleep.await_count == 0

@patch.object(MockMarkdownTranslator, "_run_prompt")
@pytest.mark.asyncio
async def test_run_prompts_sequentially(mock_run_prompt, markdown_translator):
    """
    Test the _run_prompts_sequentially method to ensure it processes prompts sequentially.
    """
    async def mock_run(*args, **kwargs):
        return f"Translated: {args[0]}"

    mock_run_prompt.side_effect = mock_run
    prompts = ["Prompt 1", "Prompt 2"]
    results = await markdown_translator._run_prompts_sequentially(prompts)

    assert results == ["Translated: Prompt 1", "Translated: Prompt 2"]
    assert mock_run_prompt.call_count == 2

@patch.object(MockMarkdownTranslator, "_run_prompt")
@pytest.mark.asyncio
async def test_generate_disclaimer(mock_run_prompt, markdown_translator):
    """
    Test the generate_disclaimer method to ensure it generates the disclaimer correctly.
    """
    mock_run_prompt.return_value = "Translated Disclaimer"
    result = await markdown_translator.generate_disclaimer("es")
    assert result == "Translated Disclaimer"

@patch("co_op_translator.utils.llm.markdown_utils.update_links")
@patch("co_op_translator.utils.llm.markdown_utils.restore_code_blocks_and_inline_code")
@patch("co_op_translator.utils.llm.markdown_utils.generate_prompt_template")
@patch("co_op_translator.utils.llm.markdown_utils.process_markdown_with_many_links")
@patch("co_op_translator.utils.llm.markdown_utils.count_links_in_markdown")
@patch.object(MockMarkdownTranslator, "_run_prompts_sequentially")
@pytest.mark.asyncio
async def test_translate_markdown_with_many_links(
    mock_run_prompts_sequentially,
    mock_count_links,
    mock_process_many_links,
    mock_generate_prompt,
    mock_restore_code_blocks,
    mock_update_links,
    markdown_translator
):
    """
    Test translation of markdown documents with more than 10 links.
    """
    # Set up mocks
    mock_count_links.return_value = 31  # More than link_limit (30)
    mock_process_many_links.return_value = ["Chunk 1", "Chunk 2"]
    mock_generate_prompt.side_effect = ["Generated Prompt 1", "Generated Prompt 2"]
    mock_run_prompts_sequentially.return_value = ["Translated Chunk 1", "Translated Chunk 2"]
    mock_restore_code_blocks.return_value = "Restored Content"
    mock_update_links.return_value = "Updated Content"

    # Call the method
    result = await markdown_translator.translate_markdown(
        document=TEST_MD_WITH_MANY_LINKS,
        language_code="ko",
        md_file_path="test_many_links.md"
    )

    # Verify the expected behavior
    assert mock_count_links.call_count == 1
    assert mock_process_many_links.call_count == 1
    assert mock_generate_prompt.call_count == 2
    assert mock_run_prompts_sequentially.call_count == 1
    assert mock_restore_code_blocks.call_count == 1
    assert mock_update_links.call_count == 1
    assert result == "Updated Content\n\n" + TRANSLATED_DISCLAIMER

@pytest.mark.asyncio
async def test_translate_markdown_error_handling(markdown_translator):
    """
    Test error handling in markdown translation.
    """
    # Test with empty document
    with pytest.raises(ValueError, match="Empty document"):
        await markdown_translator.translate_markdown("", "ko", "test.md")
    
    # Test with None document
    with pytest.raises(ValueError, match="document must be a string"):
        await markdown_translator.translate_markdown(None, "ko", "test.md")
    
    # Test with invalid language code
    with pytest.raises(ValueError, match="Invalid language code"):
        await markdown_translator.translate_markdown(TEST_MD_CONTENT, "invalid", "test.md")
    
    # Test with None language code
    with pytest.raises(ValueError, match="Invalid language code"):
        await markdown_translator.translate_markdown(TEST_MD_CONTENT, None, "test.md")

@patch("co_op_translator.config.font_config.FontConfig.is_rtl")
@patch("co_op_translator.utils.llm.markdown_utils.update_links")
@patch("co_op_translator.utils.llm.markdown_utils.restore_code_blocks_and_inline_code")
@patch.object(MockMarkdownTranslator, "_run_prompts_sequentially")
@pytest.mark.asyncio
async def test_translate_markdown_rtl_language(
    mock_run_prompts_sequentially,
    mock_restore_code_blocks,
    mock_update_links,
    mock_is_rtl,
    markdown_translator
):
    """
    Test translation to RTL languages like Arabic.
    """
    mock_is_rtl.return_value = True
    mock_run_prompts_sequentially.return_value = ["Translated Content"]
    mock_restore_code_blocks.return_value = "Restored RTL Content"
    mock_update_links.return_value = "Final RTL Content"

    result = await markdown_translator.translate_markdown(
        document=TEST_MD_CONTENT,
        language_code="ar",
        md_file_path="test_rtl.md"
    )

    assert mock_is_rtl.call_count == 1
    assert mock_is_rtl.call_args[0][0] == "ar"
    assert result == "Final RTL Content\n\n" + TRANSLATED_DISCLAIMER

@patch("co_op_translator.utils.llm.markdown_utils.update_links")
@patch("co_op_translator.utils.llm.markdown_utils.restore_code_blocks_and_inline_code")
@patch("co_op_translator.utils.llm.markdown_utils.replace_code_blocks_and_inline_code")
@patch.object(MockMarkdownTranslator, "_run_prompts_sequentially")
@pytest.mark.asyncio
async def test_translate_markdown_with_various_elements(
    mock_run_prompts_sequentially,
    mock_replace_code_blocks,
    mock_restore_code_blocks,
    mock_update_links,
    markdown_translator
):
    """
    Test translation of markdown with various elements (tables, images, code blocks).
    """
    code_blocks = {
        "code_block_1": "def example():\n    return \"This is a code block\"",
        "inline_code_1": "inline code"
    }
    mock_replace_code_blocks.return_value = (TEST_MD_WITH_VARIOUS_ELEMENTS, code_blocks)
    mock_run_prompts_sequentially.return_value = ["Translated Content"]
    mock_restore_code_blocks.return_value = "Restored Content with Code"
    mock_update_links.return_value = "Final Content with Links"

    result = await markdown_translator.translate_markdown(
        document=TEST_MD_WITH_VARIOUS_ELEMENTS,
        language_code="ja",
        md_file_path="test_complex.md"
    )

    assert mock_replace_code_blocks.call_count == 1
    assert mock_restore_code_blocks.call_count == 1
    assert mock_update_links.call_count == 1
    assert result == "Final Content with Links\n\n" + TRANSLATED_DISCLAIMER
