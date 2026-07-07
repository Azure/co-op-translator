import pytest
import re

from co_op_translator.utils.llm.code_comment_translator import (
    translate_comments_in_code_blocks,
)
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER


def _translate_numbered_prompt_slots(prompt: str, prefix: str, transform) -> str:
    _, user_part = prompt.split(SPLIT_DELIMITER, 1)
    marker_pattern = re.compile(rf"\b{re.escape(prefix)}_(\d+):\s*")
    matches = list(marker_pattern.finditer(user_part))
    out_lines = []
    for match_index, match in enumerate(matches):
        slot_number = match.group(1)
        text_start = match.end()
        text_end = (
            matches[match_index + 1].start()
            if match_index + 1 < len(matches)
            else len(user_part)
        )
        text = user_part[text_start:text_end].strip()
        out_lines.append(f"{prefix}_{slot_number}: {transform(text)}")
    return "\n".join(out_lines)


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
        if "MERMAID_SLOT_n" in prompt:
            return _translate_numbered_prompt_slots(
                prompt, "MERMAID_SLOT", lambda text: f"[es]{text}[/es]"
            )
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
async def test_translate_comments_in_code_blocks_mermaid_restores_fence_newlines():
    """Mermaid translation must keep closing fences on their own lines."""

    placeholder_map = {
        "@@CODE_BLOCK_0@@": (
            "```mermaid\n"
            "graph TD\n"
            "    subgraph Server A\n"
            "        KnowledgeA[Knowledge]\n"
            "    end\n"
            "```\n"
        )
    }

    async def fake_run_prompt(prompt, index, total):
        if "MERMAID_SLOT_n" in prompt:
            return _translate_numbered_prompt_slots(
                prompt, "MERMAID_SLOT", lambda text: text.replace("Knowledge", "知識")
            )
        return prompt

    result_map = await translate_comments_in_code_blocks(
        placeholder_map,
        language_code="ja",
        language_name="Japanese",
        is_rtl=False,
        run_prompt=fake_run_prompt,
    )

    translated_block = result_map["@@CODE_BLOCK_0@@"]

    assert "end\n```\n" in translated_block
    assert "end```" not in translated_block


@pytest.mark.asyncio
async def test_translate_comments_in_code_blocks_mermaid_collapsed_slot_response():
    """Collapsed Mermaid slot responses must not collapse the diagram block."""

    original_block = (
        "```mermaid\n"
        "sequenceDiagram\n"
        "    participant WebApp as Web App<br/>(ContentSafetyController)\n"
        "    WebApp->>MCP: Send text for moderation\n"
        "    MCP-->>WebApp: Return decision\n"
        "```\n"
    )
    placeholder_map = {"@@CODE_BLOCK_0@@": original_block}

    async def fake_run_prompt(prompt, index, total):
        if "MERMAID_SLOT_n" in prompt:
            translated = _translate_numbered_prompt_slots(
                prompt, "MERMAID_SLOT", lambda text: f"[ko]{text}[/ko]"
            )
            return " ".join(translated.splitlines())
        return prompt

    result_map = await translate_comments_in_code_blocks(
        placeholder_map,
        language_code="ko",
        language_name="Korean",
        is_rtl=False,
        run_prompt=fake_run_prompt,
    )

    translated_block = result_map["@@CODE_BLOCK_0@@"]

    assert translated_block.count("\n") == original_block.count("\n")
    assert "sequenceDiagram\n" in translated_block
    assert "```mermaid\n" in translated_block
    assert "```\n" in translated_block
    assert "[ko]Send text for moderation[/ko]" in translated_block
    assert "[ko]Return decision[/ko]" in translated_block


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
