from textwrap import dedent
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from co_op_translator.translators.markdown_translator import MarkdownTranslator
from pathlib import Path

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

@pytest.fixture
def markdown_translator(tmp_path):
    """
    Fixture to provide an instance of MarkdownTranslator for each test.
    """
    return MarkdownTranslator(root_dir=tmp_path)

@patch("co_op_translator.translators.markdown_translator.update_links")
@patch("co_op_translator.translators.markdown_translator.restore_code_blocks_and_inline_code")
@patch("co_op_translator.translators.markdown_translator.generate_prompt_template")
@patch("co_op_translator.translators.markdown_translator.replace_code_blocks_and_inline_code")
@patch("co_op_translator.translators.markdown_translator.count_links_in_markdown")
@patch("co_op_translator.translators.markdown_translator.process_markdown_with_many_links")
@patch("co_op_translator.translators.markdown_translator.process_markdown")
@patch("co_op_translator.translators.markdown_translator.FontConfig.is_rtl")
@patch("co_op_translator.translators.markdown_translator.MarkdownTranslator.generate_disclaimer")
@patch("co_op_translator.translators.markdown_translator.MarkdownTranslator._run_prompts_sequentially")
@pytest.mark.asyncio
async def test_translate_markdown(
    mock_run_prompts_sequentially,
    mock_generate_disclaimer,
    mock_is_rtl,
    mock_process_markdown,
    mock_process_markdown_with_many_links,
    mock_count_links_in_markdown,
    mock_replace_code_blocks,
    mock_generate_prompt_template,
    mock_restore_code_blocks,
    mock_update_links,
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
        md_file_path="test.md"
    )

    # Assertions
    assert result == TRANSLATED_CONTENT + "\n\n" + TRANSLATED_DISCLAIMER

    mock_replace_code_blocks.assert_called_once_with(TEST_MD_CONTENT)
    mock_count_links_in_markdown.assert_called_once_with(TEST_MD_CONTENT)
    mock_process_markdown.assert_called_once_with(TEST_MD_CONTENT)
    mock_generate_prompt_template.assert_called_once_with("es", "Chunk 1", False)
    mock_run_prompts_sequentially.assert_called_once_with(["Generated Prompt"])
    mock_restore_code_blocks.assert_called_once_with("Translated Chunk", {})
    mock_update_links.assert_called_once_with(Path("test.md"), TRANSLATED_CONTENT, "es", markdown_translator.root_dir)
    mock_generate_disclaimer.assert_called_once_with("es")

@patch("co_op_translator.translators.markdown_translator.time.time", side_effect=[0, 1])
@patch("co_op_translator.translators.markdown_translator.asyncio.sleep", new_callable=AsyncMock)
@patch("co_op_translator.translators.markdown_translator.Kernel.invoke", new_callable=AsyncMock)
@patch("co_op_translator.translators.markdown_translator.Kernel.add_function")
@patch("co_op_translator.translators.markdown_translator.PromptTemplateConfig")
@patch("co_op_translator.translators.markdown_translator.Kernel.get_prompt_execution_settings_from_service_id")
@pytest.mark.asyncio
async def test_run_prompt(
    mock_get_settings,
    mock_prompt_config,
    mock_add_function,
    mock_invoke,
    mock_sleep,
    mock_time,
    markdown_translator,
):
    """
    Test the _run_prompt method to ensure it executes prompts correctly.
    """

    mock_get_settings.return_value = MagicMock()
    mock_add_function.return_value = "function"
    mock_invoke.return_value = "Prompt Result"

    result = await markdown_translator._run_prompt("Test Prompt", 1, 1)

    assert result == "Prompt Result"
    mock_get_settings.assert_called_once_with("chat-gpt")
    mock_prompt_config.assert_called_once()
    mock_add_function.assert_called_once()
    mock_invoke.assert_called_once_with("function")
    mock_sleep.assert_awaited_once_with(1)

@patch("co_op_translator.translators.markdown_translator.MarkdownTranslator._run_prompt")
@pytest.mark.asyncio
async def test_generate_disclaimer(mock_run_prompt, markdown_translator):
    """
    Test the generate_disclaimer method to ensure it generates the disclaimer correctly.
    """

    mock_run_prompt.return_value = TRANSLATED_DISCLAIMER

    result = await markdown_translator.generate_disclaimer("es")

    assert result == TRANSLATED_DISCLAIMER

    expected_prompt = dedent("""
        Translate the following text to es.

        **Disclaimer**: 
        This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
    """)

    expected_prompt_normalized = ''.join(expected_prompt.split())
    actual_prompt_normalized = ''.join(mock_run_prompt.call_args[0][0].split())

    assert actual_prompt_normalized == expected_prompt_normalized, f"Expected:\n{expected_prompt}\n\nActual:\n{mock_run_prompt.call_args[0][0]}"

@patch("co_op_translator.translators.markdown_translator.MarkdownTranslator._run_prompt")
@pytest.mark.asyncio
async def test_run_prompts_sequentially(mock_run_prompt, markdown_translator):

    """
    Test the _run_prompts_sequentially method to ensure it processes prompts sequentially.
    """
    mock_run_prompt.side_effect = ["Result 1", "Result 2"]

    prompts = ["Prompt 1", "Prompt 2"]
    results = await markdown_translator._run_prompts_sequentially(prompts)

    assert results == ["Result 1", "Result 2"]
    assert mock_run_prompt.await_count == 2
    mock_run_prompt.assert_any_call("Prompt 1", 1, 2)
    mock_run_prompt.assert_any_call("Prompt 2", 2, 2)
