from co_op_translator.utils.markdown.processing import (
    _group_lines_preserving_list_items,
    count_links_in_markdown,
    process_markdown,
    process_markdown_with_many_links,
    split_markdown_content,
)


def test_process_markdown():
    """Test processing markdown content into chunks."""
    content = "# Test\n" * 100  # Create large content
    chunks = process_markdown(content, max_tokens=100)

    assert isinstance(chunks, list)
    assert len(chunks) > 1
    assert all(isinstance(chunk, str) for chunk in chunks)


def test_process_markdown_with_many_links():
    """Test processing markdown with many links."""
    content = "[link](test.md)\n" * 10
    max_links = 5
    chunks = process_markdown_with_many_links(content, max_links)

    assert isinstance(chunks, list)
    assert len(chunks) > 1
    assert all(count_links_in_markdown(chunk) <= max_links for chunk in chunks)


def test_group_lines_preserving_list_items_splits_sibling_items():
    """Sibling list items should be separate split units for large TOCs."""
    content = """- [One](one.md)
- [Two](two.md)
- [Three](three.md)

Paragraph
"""

    groups = _group_lines_preserving_list_items(content)

    assert groups == [
        "- [One](one.md)\n",
        "- [Two](two.md)\n",
        "- [Three](three.md)\n\n",
        "Paragraph\n",
    ]


def test_group_lines_preserving_list_items_keeps_nested_code_with_item():
    """Indented code blocks inside a list item should stay with that item."""
    content = """- Step 1

    ```bash
    echo one
    ```
- Step 2
"""

    groups = _group_lines_preserving_list_items(content)

    assert groups == [
        "- Step 1\n\n    ```bash\n    echo one\n    ```\n",
        "- Step 2\n",
    ]


def test_group_lines_preserving_list_items_splits_nested_items():
    """Nested list items should still be separate split units."""
    content = """- Parent
  - Child 1
    - Grandchild
- Next
"""

    groups = _group_lines_preserving_list_items(content)

    assert groups == [
        "- Parent\n",
        "  - Child 1\n",
        "    - Grandchild\n",
        "- Next\n",
    ]


def test_split_markdown_content_keeps_list_newlines_when_splitting_large_toc():
    """Oversized link-heavy lists should split at item boundaries, not words."""
    content = """- [One](one.md)
- [Two](two.md)
- [Three](three.md)
- [Four](four.md)
"""

    class MockTokenizer:
        def encode(self, text):
            return list(text)

    chunks = split_markdown_content(content, 35, MockTokenizer())

    assert len(chunks) > 1
    assert all(" - " not in chunk for chunk in chunks)
    assert "".join(chunks) == content


def test_split_markdown_content_keeps_nested_toc_newlines_when_splitting():
    """Large nested TOCs should not be flattened into one-line chunks."""
    content = """- Phi application development samples
  - Text & Chat Applications
    - Phi-4 Samples
      - [Chat With Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat with Phi-4 local ONNX Model .NET](./md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime/)
  - Azure AI Inference SDK Code Based Samples
    - Phi-4 Samples
      - [Generate project code using Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
"""

    class MockTokenizer:
        def encode(self, text):
            return list(text)

    chunks = split_markdown_content(content, 120, MockTokenizer())

    assert len(chunks) > 1
    assert (
        "- Phi application development samples - Text & Chat Applications"
        not in "".join(chunks)
    )
    assert "- Phi-4 Samples - [Chat With Phi-4-mini ONNX Model]" not in "".join(chunks)
    assert "".join(chunks) == content


def test_split_markdown_content_preserves_whitespace_in_oversized_fallback():
    """Fallback splitting should preserve exact whitespace and newlines."""
    content = """- Step with a very long continuation
  This continuation keeps  double spaces.
  This continuation keeps the second line.
"""

    class MockTokenizer:
        def encode(self, text):
            return list(text)

    chunks = split_markdown_content(content, 32, MockTokenizer())

    assert len(chunks) > 1
    assert "".join(chunks) == content
    assert "  double spaces" in "".join(chunks)
    assert "\n  This continuation keeps the second line." in "".join(chunks)


def test_split_markdown_content_splits_unbroken_text_without_losing_characters():
    """Fallback splitting should preserve oversized spans without whitespace."""
    content = "https://example.com/" + ("verylongpath" * 8) + "\n"

    class MockTokenizer:
        def encode(self, text):
            return list(text)

    chunks = split_markdown_content(content, 25, MockTokenizer())

    assert len(chunks) > 1
    assert "".join(chunks) == content
    assert all(len(chunk) <= 25 for chunk in chunks if chunk.strip())


def test_count_links_in_markdown():
    """Test counting links in markdown content."""
    content = """
    # Test
    [link1](test1.md)
    [link2](test2.md)
    ![image](test.png)
    """
    count = count_links_in_markdown(content)
    assert count == 3  # Two links and one image


def test_split_markdown_content():
    """Test splitting markdown content into chunks."""
    content = """
    # Section 1
    Normal text.
    ```python
    code block
    ```
    > blockquote
    Normal text again.
    """

    # Create a mock tokenizer
    class MockTokenizer:
        def encode(self, text):
            return [0] * len(text)  # Simulate token count

    chunks = split_markdown_content(content, 100, MockTokenizer())

    assert isinstance(chunks, list)
    assert len(chunks) > 0
    assert all(isinstance(chunk, str) for chunk in chunks)


def test_split_markdown_content_keeps_list_item_with_code_placeholder():
    """List item text and indented code placeholder should stay in the same chunk."""
    content = """- Step 1: run this command\n    @@CODE_BLOCK_0@@\n\nParagraph after list item.\n"""

    class MockTokenizer:
        def encode(self, text):
            return [0] * len(text)

    chunks = split_markdown_content(content, 30, MockTokenizer())

    assert len(chunks) >= 1
    assert any("- Step 1" in chunk and "@@CODE_BLOCK_0@@" in chunk for chunk in chunks)
