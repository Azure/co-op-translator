import pytest
import re

from co_op_translator.utils.llm.code_comment_translator import (
    translate_comments_in_code_blocks,
)
from co_op_translator.utils.llm.markdown_utils import SPLIT_DELIMITER


@pytest.mark.asyncio
async def test_translate_comments_in_code_blocks_python_comments():
    """Translate only # comments inside a fenced python code block."""

    placeholder_map = {
        "@@CODE_BLOCK_0@@": (
            "```python\n"
            "# First comment\n"
            'print("Hello, world!")\n'
            "# Second comment\n"
            "```"
        )
    }

    async def fake_run_prompt(prompt, index, total):
        # COMMENT_n aggregation prompt
        if "Each line is in the form 'COMMENT_n: <text>'." in prompt:
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
        return prompt

    result_map = await translate_comments_in_code_blocks(
        placeholder_map,
        language_code="es",
        language_name="Spanish",
        is_rtl=False,
        run_prompt=fake_run_prompt,
    )

    translated_block = result_map["@@CODE_BLOCK_0@@"]

    # Code must remain intact
    assert 'print("Hello, world!")' in translated_block

    # Comments should be translated according to our fake_run_prompt
    assert "# [es]First comment[/es]" in translated_block
    assert "# [es]Second comment[/es]" in translated_block


@pytest.mark.asyncio
async def test_translate_comments_in_code_blocks_mermaid_block():
    """Translate labels inside a Mermaid fenced code block while preserving syntax."""

    placeholder_map = {
        "@@CODE_BLOCK_0@@": (
            "```mermaid\n"
            "graph TD;\n"
            "    A[Start] --> B{Decision};\n"
            "    B -->|Yes| C[Do it];\n"
            "    B -->|No| D[Stop];\n"
            "```\n"
        )
    }

    async def fake_run_prompt(prompt, index, total):
        # Mermaid-specific translation
        if "Mermaid diagram code" in prompt:
            _, code_block = prompt.split(SPLIT_DELIMITER, 1)
            translated = (
                code_block.replace("Start", "[es]Start[/es]")
                .replace("Decision", "[es]Decision[/es]")
                .replace("Do it", "[es]Do it[/es]")
                .replace("Stop", "[es]Stop[/es]")
            )
            return translated
        return prompt

    result_map = await translate_comments_in_code_blocks(
        placeholder_map,
        language_code="es",
        language_name="Spanish",
        is_rtl=False,
        run_prompt=fake_run_prompt,
    )

    translated_block = result_map["@@CODE_BLOCK_0@@"]

    # Mermaid syntax must still be present
    assert "graph TD;" in translated_block

    # Labels should be translated according to our fake_run_prompt
    assert "[es]Start[/es]" in translated_block
    assert "[es]Decision[/es]" in translated_block
    assert "[es]Do it[/es]" in translated_block
    assert "[es]Stop[/es]" in translated_block


@pytest.mark.asyncio
async def test_translate_comments_in_code_blocks_non_code_block_unchanged():
    """Non-fenced or unsupported language blocks should be returned unchanged."""

    original_block = "Some text without fences or comments.\n"
    placeholder_map = {"@@CODE_BLOCK_0@@": original_block}

    async def fake_run_prompt(
        prompt, index, total
    ):  # pragma: no cover - should not run
        raise AssertionError("run_prompt should not be called for non-fenced blocks")

    result_map = await translate_comments_in_code_blocks(
        placeholder_map,
        language_code="es",
        language_name="Spanish",
        is_rtl=False,
        run_prompt=fake_run_prompt,
    )

    assert result_map["@@CODE_BLOCK_0@@"] == original_block
