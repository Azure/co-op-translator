import pytest
from unittest.mock import AsyncMock, patch
import re

from co_op_translator.core.llm.markdown_translator import (
    MarkdownTranslator,
    TranslationContentFilterError,
    TranslationIncompleteError,
)
from co_op_translator.utils.common.lang_utils import get_supported_language_codes
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER

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


TEST_MD_WITH_MERMAID_AND_PARAGRAPH = """
# Sample Markdown

```mermaid
graph TD
    ServerA --> KnowledgeA
    subgraph Server A
        KnowledgeA[Knowledge]
    end
```
Universal connector text.
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


TEST_MD_WITH_INTERNAL_LINK_IN_CODE = """
# Sample

- [Section One](#section-one)

## Section One

```md
[Example](#section-one)
```
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


def _translate_marked_prompt_body(prompt: str, replacements: dict[str, str]) -> str:
    """Return the marked user body with requested text replacements applied."""
    _, body = prompt.split(SPLIT_DELIMITER, 1)
    for source, target in replacements.items():
        body = body.replace(source, target)
    return body


def _translate_numbered_prompt_slots(
    prompt: str,
    prefix: str,
    transform,
) -> str:
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
async def test_generate_disclaimer_uses_packaged_language_template(
    real_markdown_translator,
):
    """Supported languages should use packaged templates without an LLM call."""

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        result = await real_markdown_translator.generate_disclaimer("ja")

    assert "**免責事項**" in result
    assert "[Co-op Translator](https://github.com/Azure/co-op-translator)" in result
    mock_run_prompt.assert_not_called()


def test_disclaimer_templates_cover_supported_languages(real_markdown_translator):
    """Every supported language should have a canonical disclaimer template."""

    templates = real_markdown_translator._load_disclaimer_templates()
    co_op_link = "[Co-op Translator](https://github.com/Azure/co-op-translator)"

    assert set(get_supported_language_codes()).issubset(set(templates))
    assert all(co_op_link in templates[code] for code in get_supported_language_codes())


def test_finish_reason_stop_or_missing_is_allowed(real_markdown_translator):
    real_markdown_translator._raise_for_finish_reason("stop", 1, 1)
    real_markdown_translator._raise_for_finish_reason(None, 1, 1)


def test_finish_reason_length_is_incomplete(real_markdown_translator):
    with pytest.raises(TranslationIncompleteError):
        real_markdown_translator._raise_for_finish_reason("length", 1, 1)


def test_finish_reason_content_filter_is_separate_error(real_markdown_translator):
    with pytest.raises(TranslationContentFilterError):
        real_markdown_translator._raise_for_finish_reason("content_filter", 1, 1)


def test_finish_reason_enum_values_are_normalized(real_markdown_translator):
    class FinishReason:
        value = "stop"

    real_markdown_translator._raise_for_finish_reason(FinishReason(), 1, 1)


@pytest.mark.asyncio
async def test_generate_disclaimer_fallback_includes_markdown_safety_rules(
    real_markdown_translator,
):
    """Fallback disclaimer prompt should preserve markdown-structure rules."""

    captured_prompts = []

    async def fake_prompt(prompt, index, total):
        captured_prompts.append(prompt)
        return "Translated disclaimer"

    with (
        patch.object(
            real_markdown_translator,
            "_read_disclaimer_template_for_language",
            return_value="",
        ),
        patch.object(
            real_markdown_translator, "_run_prompt", new_callable=AsyncMock
        ) as mock_run_prompt,
    ):
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.generate_disclaimer("ja")

    assert result == "Translated disclaimer"
    assert len(captured_prompts) == 1
    assert (
        "Preserve Markdown syntax and tokens exactly as written" in captured_prompts[0]
    )
    assert "keep Markdown link structure [text](URL)" in captured_prompts[0]
    assert "Japanese mode: preserve Markdown tokens strictly." in captured_prompts[0]
    assert "NEVER rewrite links as plain text" in captured_prompts[0]


@pytest.mark.asyncio
async def test_translate_markdown_partial_mock(real_markdown_translator, tmp_path):
    """Test the translation logic using the real code for:
    - replace_code_blocks
    - restore_code_blocks
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
            return _translate_marked_prompt_body(
                prompt, {"# Sample Markdown": "# Ejemplo de Markdown"}
            )
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
            document=TEST_MD_CONTENT, language_code="es", source_path=test_file
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
async def test_translate_markdown_skips_project_path_rewrite(
    real_markdown_translator,
):
    """Content-only translation should keep links as translated by the model."""

    document = "# Sample\n\n![Hero](images/hero.png)\n"

    async def fake_prompt(prompt, index, total):
        if "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."
        if "# Sample" in prompt:
            _, body = prompt.split(SPLIT_DELIMITER, 1)
            return body.replace("# Sample", "# Ejemplo")
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document,
            "es",
        )

    assert "# Ejemplo" in result
    assert "![Hero](images/hero.png)" in result
    assert "translated_images" not in result


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
            return _translate_marked_prompt_body(
                prompt, {"# Sample Markdown": "# Ejemplo de Markdown"}
            )
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
            source_path=test_file,
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
        if "MERMAID_SLOT_n" in prompt:
            return _translate_numbered_prompt_slots(
                prompt, "MERMAID_SLOT", lambda text: f"[es]{text}[/es]"
            )
        if "Sample Markdown" in prompt:
            return _translate_marked_prompt_body(
                prompt, {"# Sample Markdown": "# Ejemplo de Markdown"}
            )
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
            source_path=test_file,
        )

    # Mermaid syntax must still be present
    assert "graph TD;" in result

    # Labels should be translated according to our fake_prompt
    assert "[es]Start[/es]" in result
    assert "[es]Decision[/es]" in result
    assert "[es]Do it[/es]" in result
    assert "[es]Stop[/es]" in result


@pytest.mark.asyncio
async def test_translate_markdown_keeps_mermaid_closing_fence_separate_from_text(
    real_markdown_translator, tmp_path
):
    """Mermaid fence boundaries must survive translation before paragraph text."""
    test_file = tmp_path / "example_mermaid_paragraph.md"
    test_file.write_text(TEST_MD_WITH_MERMAID_AND_PARAGRAPH)

    async def fake_prompt(prompt, index, total):
        if "MERMAID_SLOT_n" in prompt:
            return _translate_numbered_prompt_slots(
                prompt, "MERMAID_SLOT", lambda text: text.replace("Knowledge", "知識")
            )
        if "Sample Markdown" in prompt:
            return _translate_marked_prompt_body(
                prompt,
                {
                    "# Sample Markdown": "# サンプル Markdown",
                    "Universal connector text.": "ユニバーサルコネクターにより",
                },
            )
        if "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_WITH_MERMAID_AND_PARAGRAPH,
            language_code="ja",
            source_path=test_file,
        )

    assert "end\n```\nユニバーサルコネクターにより" in result
    assert "end```" not in result
    assert "```ユニバーサル" not in result


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
            source_path=test_file,
        )

    # <details>/<summary> HTML structure should be preserved
    assert "<details>" in result
    assert "</details>" in result
    assert "<summary>TypeScript (ES)</summary>" in result

    # The shell code block content should still be present after
    # placeholder replacement and restoration.
    assert "npm install @modelcontextprotocol/sdk zod" in result


@pytest.mark.asyncio
async def test_translate_markdown_keeps_internal_links_inside_code_blocks_unchanged(
    real_markdown_translator, tmp_path
):
    """Internal-link normalization must not mutate markdown shown inside code blocks."""
    test_file = tmp_path / "example_internal_links_in_code.md"
    test_file.write_text(TEST_MD_WITH_INTERNAL_LINK_IN_CODE)

    async def fake_prompt(prompt, index, total):
        if "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."

        if "# Sample" in prompt:
            return _translate_marked_prompt_body(
                prompt,
                {
                    "# Sample": "# 샘플",
                    "- [Section One](#section-one)": "- [섹션 1](#section-one)",
                    "## Section One": "## 섹션 1",
                },
            )

        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_WITH_INTERNAL_LINK_IN_CODE,
            language_code="ko",
            source_path=test_file,
        )

    assert "- [섹션 1](#섹션-1)" in result
    assert "```md\n[Example](#section-one)\n```" in result


@pytest.mark.asyncio
async def test_translate_markdown_rebuilds_lines_from_collapsed_anchor_output(
    real_markdown_translator,
):
    """Line anchors allow recovery when a provider merges markdown lines."""

    document = "# Title\n\nFirst paragraph.  \nSecond paragraph.\n"

    async def fake_prompt(prompt, index, total):
        if "# Title" in prompt:
            body = _translate_marked_prompt_body(
                prompt,
                {
                    "# Title": "# Titulo",
                    "First paragraph.": "Primer parrafo.",
                    "Second paragraph.": "Segundo parrafo.",
                },
            )
            return " ".join(body.splitlines())
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(document, "es")

    assert result == "# Titulo\n\nPrimer parrafo.  \nSegundo parrafo.\n"
    assert "@@COOP_CHUNK_START" not in result
    assert "@@LINE_" not in result


@pytest.mark.asyncio
async def test_translate_markdown_missing_chunk_end_marker_is_incomplete(
    real_markdown_translator,
):
    """Missing envelope markers should be treated as incomplete responses."""

    calls = 0

    async def fake_prompt(prompt, index, total):
        nonlocal calls
        calls += 1
        _, body = prompt.split(SPLIT_DELIMITER, 1)
        return re.sub(r"@@COOP_CHUNK_END:[^@]+@@", "", body)

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        with pytest.raises(TranslationIncompleteError):
            await real_markdown_translator.translate_markdown("# Title\n", "es")

    assert calls == 2


@pytest.mark.asyncio
async def test_translate_markdown_retries_incomplete_chunk_once(
    real_markdown_translator,
    tmp_path,
):
    test_file = tmp_path / "retry_once.md"
    test_file.write_text("# Retry me\n\nStable text.\n")
    calls = 0

    async def fake_prompt(prompt, index, total):
        nonlocal calls
        if "# Retry me" in prompt:
            calls += 1
            if calls == 1:
                raise TranslationIncompleteError("length")
            return _translate_marked_prompt_body(
                prompt,
                {"# Retry me": "# Reintentar", "Stable text.": "Texto estable."},
            )
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            "# Retry me\n\nStable text.\n",
            "es",
            source_path=test_file,
        )

    assert "# Reintentar" in result
    assert "Texto estable." in result
    assert calls == 2


@pytest.mark.asyncio
async def test_translate_markdown_splits_incomplete_chunk_after_retry(
    real_markdown_translator,
    monkeypatch,
    tmp_path,
):
    test_file = tmp_path / "split_retry.md"
    document = "# Needs split\n\nFirst part.\n\nSecond part.\n"
    test_file.write_text(document)
    split_max_tokens = []
    original_failures = 0

    def fake_process_markdown(content, max_tokens=2600, encoding="o200k_base"):
        split_max_tokens.append(max_tokens)
        if max_tokens == 2600:
            return [content]
        return ["# Needs split\n\nFirst part.\n", "Second part.\n"]

    monkeypatch.setattr(
        "co_op_translator.core.llm.markdown_translator.process_markdown",
        fake_process_markdown,
    )

    async def fake_prompt(prompt, index, total):
        nonlocal original_failures
        if "First part." in prompt and "Second part." in prompt:
            original_failures += 1
            raise TranslationIncompleteError("length")
        if "First part." in prompt:
            return _translate_marked_prompt_body(
                prompt,
                {"# Needs split": "# Dividido", "First part.": "Primera parte."},
            )
        if "Second part." in prompt:
            return _translate_marked_prompt_body(
                prompt, {"Second part.": "Segunda parte."}
            )
        return prompt

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        result = await real_markdown_translator.translate_markdown(
            document,
            "es",
            source_path=test_file,
        )

    assert "# Dividido" in result
    assert "Primera parte." in result
    assert "Segunda parte." in result
    assert original_failures == 2
    assert split_max_tokens == [2600, 1300]


@pytest.mark.asyncio
async def test_translate_markdown_does_not_split_content_filter_errors(
    real_markdown_translator,
    monkeypatch,
    tmp_path,
):
    test_file = tmp_path / "content_filter.md"
    document = "# Blocked\n"
    test_file.write_text(document)
    split_max_tokens = []

    def fake_process_markdown(content, max_tokens=2600, encoding="o200k_base"):
        split_max_tokens.append(max_tokens)
        return [content]

    monkeypatch.setattr(
        "co_op_translator.core.llm.markdown_translator.process_markdown",
        fake_process_markdown,
    )

    async def fake_prompt(prompt, index, total):
        raise TranslationContentFilterError("content_filter")

    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        with pytest.raises(TranslationContentFilterError):
            await real_markdown_translator.translate_markdown(
                document,
                "es",
                source_path=test_file,
            )

    assert split_max_tokens == [2600]


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
            document=TEST_MD_CONTENT, language_code="es", source_path=test_file
        )
    except NotImplementedError:
        pytest.skip(
            "Skipping because _run_prompt is not implemented in the base class."
        )

    assert (
        'print("Hello, world!")' in result
    ), "Even in a full integration scenario, the code block should remain."
    assert (
        "@@LINE_" not in result
    ), "Expected chunk line anchors to be stripped from the output."
