import pytest
from unittest.mock import AsyncMock, patch
import re

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.utils.llm.markdown_utils import SPLIT_DELIMITER

# A sample markdown with a code block and a link for testing.
TEST_MD_CONTENT = """
# Sample Markdown

```python
print("Hello, world!")
```"""


TEST_MD_WITH_COMMENTS = """
# Sample Markdown

```python
# First comment
print("Hello, world!")
# Second comment
```"""


TEST_MD_WITH_MERMAID = """
# Sample Markdown

```mermaid
graph TD;
    A[Start] --> B{Decision};
    B -->|Yes| C[Do it];
    B -->|No| D[Stop];
```
"""


TEST_MD_WITH_DETAILS = """
# Sample Details

<details>
  <summary>TypeScript</summary>

  ```sh
  npm install @modelcontextprotocol/sdk zod
  npm install -D @types/node typescript
  ```
</details>
"""


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
async def test_generate_disclaimer_includes_markdown_safety_rules(real_markdown_translator):
    """Disclaimer prompt should include minimal markdown-structure preservation rules."""

    captured_prompts = []

    async def fake_prompt(prompt, index, total):
        captured_prompts.append(prompt)
        return "Translated disclaimer"

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.generate_disclaimer("ja")

    assert result == "Translated disclaimer"
    assert len(captured_prompts) == 1
    assert "Preserve Markdown syntax and tokens exactly as written" in captured_prompts[0]
    assert "keep Markdown link structure [text](URL)" in captured_prompts[0]


@pytest.mark.asyncio
async def test_translate_markdown_partial_mock(real_markdown_translator, tmp_path):
    """Test the translation logic using the real code for:
    - replace_code_blocks
    - restore_code_blocks
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
        if "Each line is in the form 'COMMENT_n: <text>'." in prompt:
            # Comment-only translation request for code blocks
            _, user_part = prompt.split(SPLIT_DELIMITER, 1)
            lines = [ln.strip() for ln in user_part.splitlines() if ln.strip()]
            out_lines = []
            for line in lines:
                m = re.match(r"^(COMMENT_\d+):\s*(.*)$", line)
                if not m:
                    continue
                prefix, text = m.groups()
                out_lines.append(f"{prefix}: [es]{text}[/es]")
            return "\n".join(out_lines)
        if "Sample Markdown" in prompt:
            # Keep any code block placeholders in the translation
            placeholder_match = re.search(r"@@CODE_BLOCK_\d+@@", prompt)
            code_placeholder = placeholder_match.group(0) if placeholder_match else ""
            return f"# Ejemplo de Markdown\n\n{code_placeholder}"
        if "Disclaimer" in prompt.lower():
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
async def test_translate_markdown_translates_code_comments(
    real_markdown_translator, tmp_path
):
    """Ensure that comments inside fenced code blocks are translated
    while preserving the original code lines.
    """
    # Create test file
    test_file = tmp_path / "example_comments.md"
    test_file.write_text(TEST_MD_WITH_COMMENTS)

    async def fake_prompt(prompt, index, total):
        if "Each line is in the form 'COMMENT_n: <text>'." in prompt:
            # Comment-only translation request for code blocks
            _, user_part = prompt.split(SPLIT_DELIMITER, 1)
            lines = [ln.strip() for ln in user_part.splitlines() if ln.strip()]
            out_lines = []
            for line in lines:
                m = re.match(r"^(COMMENT_\d+):\s*(.*)$", line)
                if not m:
                    continue
                prefix, text = m.groups()
                out_lines.append(f"{prefix}: [es]{text}[/es]")
            return "\n".join(out_lines)
        if "Sample Markdown" in prompt:
            placeholder_match = re.search(r"@@CODE_BLOCK_\d+@@", prompt)
            code_placeholder = placeholder_match.group(0) if placeholder_match else ""
            return f"# Ejemplo de Markdown\n\n{code_placeholder}"
        if "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_WITH_COMMENTS,
            language_code="es",
            md_file_path=test_file,
        )

    # Code line must remain intact
    assert 'print("Hello, world!")' in result

    # Comments should be translated according to our fake_prompt
    assert "# [es]First comment[/es]" in result
    assert "# [es]Second comment[/es]" in result


@pytest.mark.asyncio
async def test_translate_markdown_translates_mermaid_block(
    real_markdown_translator, tmp_path
):
    """Ensure that Mermaid fenced code blocks are translated as diagrams,
    preserving syntax while translating human-readable labels.
    """
    test_file = tmp_path / "example_mermaid.md"
    test_file.write_text(TEST_MD_WITH_MERMAID)

    async def fake_prompt(prompt, index, total):
        # Mermaid-specific translation
        if "Mermaid diagram code" in prompt:
            _, code_block = prompt.split(SPLIT_DELIMITER, 1)
            # Simulate translation by wrapping labels in [es]...[/es]
            # We keep the overall Mermaid syntax intact.
            translated = (
                code_block.replace("Start", "[es]Start[/es]")
                .replace("Decision", "[es]Decision[/es]")
                .replace("Do it", "[es]Do it[/es]")
                .replace("Stop", "[es]Stop[/es]")
            )
            return translated
        if "Sample Markdown" in prompt:
            placeholder_match = re.search(r"@@CODE_BLOCK_\d+@@", prompt)
            code_placeholder = placeholder_match.group(0) if placeholder_match else ""
            return f"# Ejemplo de Markdown\n\n{code_placeholder}"
        if "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_WITH_MERMAID,
            language_code="es",
            md_file_path=test_file,
        )

    # Mermaid syntax must still be present
    assert "graph TD;" in result

    # Labels should be translated according to our fake_prompt
    assert "[es]Start[/es]" in result
    assert "[es]Decision[/es]" in result
    assert "[es]Do it[/es]" in result
    assert "[es]Stop[/es]" in result


@pytest.mark.asyncio
async def test_translate_markdown_preserves_details_blocks(
    real_markdown_translator, tmp_path
):
    """Ensure that HTML <details>/<summary> blocks are preserved and
    their visible text can be translated while code blocks inside are
    still handled via placeholders.
    """
    test_file = tmp_path / "example_details.md"
    test_file.write_text(TEST_MD_WITH_DETAILS)

    async def fake_prompt(prompt, index, total):
        # Preserve disclaimers logic from other tests
        if "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."

        # Main markdown translation: echo back content, but simulate
        # translation of the heading and summary text while preserving
        # HTML structure and any code block placeholders.
        if "Sample Details" in prompt or "<details>" in prompt:
            _, body = prompt.split(SPLIT_DELIMITER, 1)
            body = body.replace("# Sample Details", "# Ejemplo de Detalles")
            body = body.replace(
                "<summary>TypeScript</summary>",
                "<summary>TypeScript (ES)</summary>",
            )
            return body

        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_WITH_DETAILS,
            language_code="es",
            md_file_path=test_file,
        )

    # <details>/<summary> HTML structure should be preserved
    assert "<details>" in result
    assert "</details>" in result
    assert "<summary>TypeScript (ES)</summary>" in result

    # The shell code block content should still be present after
    # placeholder replacement and restoration.
    assert "npm install @modelcontextprotocol/sdk zod" in result


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
