"""
Test cases for markdown utility functions.
"""

import pytest
from pathlib import Path
from co_op_translator.utils.llm.markdown_utils import (
    update_links,
    update_image_links,
    update_file_links,
    process_markdown,
    process_markdown_with_many_links,
    generate_prompt_template,
    count_links_in_markdown,
    split_markdown_content,
)


@pytest.fixture
def sample_markdown():
    """Sample markdown content for testing."""
    return """# Test Document
This is a test document with [a link](test.md) and ![an image](test.png).
Here's another [link](docs/example.md) and ![image](images/test.jpg).
"""


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory structure for testing."""
    # Create directories
    (tmp_path / "translations").mkdir()
    (tmp_path / "translations/ko").mkdir()
    (tmp_path / "images").mkdir()
    (tmp_path / "translated_images").mkdir()

    # Create test files
    (tmp_path / "test.md").touch()
    (tmp_path / "test.png").touch()
    (tmp_path / "images/test.jpg").touch()

    return tmp_path


def test_update_links(temp_dir, sample_markdown):
    """Test updating all links in markdown content."""
    md_file_path = temp_dir / "test.md"
    translations_dir = temp_dir / "translations"
    translated_images_dir = temp_dir / "translated_images"

    result = update_links(
        md_file_path, sample_markdown, "ko", temp_dir, markdown_only=False
    )

    assert "ko" in result
    assert "translations/ko" in result or "translated_images" in result


def test_update_image_links(temp_dir, sample_markdown):
    """Test updating image links in markdown content."""
    md_file_path = temp_dir / "test.md"
    translations_dir = temp_dir / "translations"
    translated_images_dir = temp_dir / "images"

    result = update_image_links(
        sample_markdown,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        temp_dir,
    )

    assert "ko" in result
    assert ".png" in result
    assert "test.png" not in result  # Original image links should be updated


def test_update_file_links(temp_dir, sample_markdown):
    """Test updating file links in markdown content."""
    # Create necessary directories and files
    md_file_path = temp_dir / "test.md"
    md_file_path.touch()

    translations_dir = temp_dir / "translations"
    translations_dir.mkdir(exist_ok=True)
    ko_dir = translations_dir / "ko"
    ko_dir.mkdir(exist_ok=True)

    # Create test files
    docs_dir = temp_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    (docs_dir / "example.txt").touch()  # Non-markdown, non-image file

    # Create test markdown with a text file link
    test_markdown = "# Test Document\nHere's a [link to text file](docs/example.txt)"

    result = update_file_links(
        test_markdown, md_file_path, "ko", translations_dir, temp_dir
    )

    # Verify that non-markdown, non-image links are updated with correct relative paths
    assert "../../docs/example.txt" in result  # Updated relative path
    assert "[link to text file]" in result  # Link text should remain unchanged


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


def test_generate_prompt_template():
    """Test generating translation prompt template."""
    document_chunk = "Test content"
    prompt = generate_prompt_template("ko", document_chunk, False)

    assert isinstance(prompt, str)
    assert "ko" in prompt
    assert document_chunk in prompt


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
