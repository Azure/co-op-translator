import pytest
from unittest.mock import AsyncMock, patch
import re
from pathlib import Path

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator

# A sample markdown with a code block and a link for testing.
TEST_MD_CONTENT = """
# Sample Markdown

```python
print("Hello, world!")
```"""


class ConcreteMarkdownTranslator(MarkdownTranslator):
    """A concrete implementation of MarkdownTranslator for testing."""

    async def _run_prompt(self, prompt, index, total):
        # This implementation should be replaced by the mock in tests
        return f"[Default Translation] {prompt}"


@pytest.fixture
def real_markdown_translator(tmp_path):
    """Creates a concrete instance of MarkdownTranslator for testing."""
    return ConcreteMarkdownTranslator(root_dir=tmp_path)


@pytest.mark.asyncio
async def test_translate_markdown_partial_mock(real_markdown_translator, tmp_path):
    """Test the translation logic using the real code for:
    - replace_code_blocks_and_inline_code
    - restore_code_blocks_and_inline_code
    - update_links
    but mock _run_prompt to avoid calling a real external translator.

    This ensures we verify the actual internal workflow,
    while controlling the translation 'results' in _run_prompt.
    """
    # Create test file
    test_file = tmp_path / "example.md"
    test_file.write_text(TEST_MD_CONTENT)

    async def fake_prompt(prompt, index, total):
        # Return a translation that preserves markdown structure and placeholders
        # This simulates what a real translator would do with the prompt template
        if "Sample Markdown" in prompt:
            # Keep any code block placeholders in the translation
            placeholder_match = re.search(r"@@CODE_BLOCK_\d+@@", prompt)
            code_placeholder = placeholder_match.group(0) if placeholder_match else ""
            return f"# Ejemplo de Markdown\n\n{code_placeholder}"
        elif "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."
        return prompt  # Return the original prompt for any other content

    # Apply the mock directly to the instance
    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        # Execute the markdown translation
        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_CONTENT, language_code="es", md_file_path=test_file
        )

        # Verify that the code block content is still present in the final output
        assert (
            'print("Hello, world!")' in result
        ), "Expected the code block to remain after the placeholder/restore cycle."

        # Verify that our translation appears (in Spanish)
        assert (
            "Ejemplo de Markdown" in result
        ), "The mocked _run_prompt response should appear in the final output."

        # Verify that _run_prompt was called at least once
        assert (
            mock_run_prompt.call_count > 0
        ), "Expected at least one call to _run_prompt for the translation process."


@pytest.mark.asyncio
async def test_translate_markdown_full_integration(real_markdown_translator, tmp_path):
    """A full integration test that avoids mocking _run_prompt at all.
    This only works if the abstract _run_prompt has a default implementation
    or if real_markdown_translator is a fully realized subclass."""
    # Create test file
    test_file = tmp_path / "example_full.md"
    test_file.write_text(TEST_MD_CONTENT)

    try:
        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_CONTENT, language_code="es", md_file_path=test_file
        )
    except NotImplementedError:
        pytest.skip(
            "Skipping because _run_prompt is not implemented in the base class."
        )

    assert (
        'print("Hello, world!")' in result
    ), "Even in a full integration scenario, the code block should remain."
    assert (
        "[Default Translation]" in result
    ), "Expected the default translation text in the output."
