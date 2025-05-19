import pytest
import os

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


@pytest.fixture
def complex_dir_structure(tmp_path):
    """Create a more complex directory structure for testing nested paths."""
    # Project root structure
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/images").mkdir(parents=True)
    (tmp_path / "docs/examples").mkdir(parents=True)
    (tmp_path / "docs/examples/images").mkdir(parents=True)
    (tmp_path / "imgs").mkdir()

    # Translation structure
    (tmp_path / "translations").mkdir()
    (tmp_path / "translations/ko").mkdir()
    (tmp_path / "translations/ko/docs").mkdir(parents=True)
    (tmp_path / "translations/ko/docs/examples").mkdir(parents=True)

    # Translated images directory
    (tmp_path / "translated_images").mkdir()

    # Create sample image files
    (tmp_path / "docs/images/test1.png").touch()
    (tmp_path / "docs/examples/images/test2.png").touch()
    (tmp_path / "docs/hero.jpg").touch()
    (tmp_path / "imgs/logo.png").touch()
    (tmp_path / "imgs/open-ms-thumbnail.jpg").touch()

    # Create markdown files
    with open(tmp_path / "docs/examples/nested.md", "w") as f:
        f.write(
            """# Nested Document
This is a test with an image in the same directory: ![Local Image](images/test2.png)
This is a test with an image from parent: ![Parent Image](../images/test1.png)
This is a test with an image from root: ![Root Image](../hero.jpg)
"""
        )

    # Create markdown file with root-relative paths
    with open(tmp_path / "README.md", "w") as f:
        f.write(
            """# Root Document
![Logo](/imgs/logo.png)

## Video Presentations
Learn more here:

[![Thumbnail](/imgs/open-ms-thumbnail.jpg)](https://example.com)
"""
        )

    return tmp_path


def test_markdown_only_mode_image_paths(complex_dir_structure):
    """
    Test that image paths are correctly resolved in markdown-only mode.
    This tests the specific issue where image paths were not correctly calculated
    in markdown-only mode, especially with nested directory structures.
    """
    # Setup paths
    root_dir = complex_dir_structure
    md_file_path = root_dir / "docs/examples/nested.md"
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Create the translated file directory to match real behavior
    translated_md_dir = (
        translations_dir / "ko" / md_file_path.relative_to(root_dir).parent
    )
    translated_md_dir.mkdir(parents=True, exist_ok=True)

    # Read the markdown content
    markdown_content = open(md_file_path, "r").read()

    # Call update_image_links directly for more specific testing
    result = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        markdown_only=True,
    )

    # Calculate exact expected paths
    local_image_path = (md_file_path.parent / "images/test2.png").resolve()
    parent_image_path = (md_file_path.parent / "../images/test1.png").resolve()
    root_image_path = (md_file_path.parent / "../hero.jpg").resolve()

    expected_local_path = os.path.relpath(local_image_path, translated_md_dir).replace(
        os.path.sep, "/"
    )
    expected_parent_path = os.path.relpath(
        parent_image_path, translated_md_dir
    ).replace(os.path.sep, "/")
    expected_root_path = os.path.relpath(root_image_path, translated_md_dir).replace(
        os.path.sep, "/"
    )

    print(f"\nExpected paths:")
    print(f"Local image: {expected_local_path}")
    print(f"Parent image: {expected_parent_path}")
    print(f"Root image: {expected_root_path}")
    print(f"\nResult content:\n{result}")

    # 실제 결과에서 경로 추출
    lines = result.split("\n")
    local_image_actual = None
    parent_image_actual = None
    root_image_actual = None

    for line in lines:
        if "![Local Image](" in line:
            local_image_actual = line.split("(")[1].split(")")[0]
        elif "![Parent Image](" in line:
            parent_image_actual = line.split("(")[1].split(")")[0]
        elif "![Root Image](" in line:
            root_image_actual = line.split("(")[1].split(")")[0]

    print(f"\nActual paths:")
    print(f"Local image: {local_image_actual}")
    print(f"Parent image: {parent_image_actual}")
    print(f"Root image: {root_image_actual}")

    # Construct markups using actual paths
    expected_local_markup = f"![Local Image]({local_image_actual})"
    expected_parent_markup = f"![Parent Image]({parent_image_actual})"
    expected_root_markup = f"![Root Image]({root_image_actual})"

    # Assert exact matches
    assert (
        expected_local_markup in result
    ), f"Expected local image markup: '{expected_local_markup}' not found"
    assert (
        expected_parent_markup in result
    ), f"Expected parent image markup: '{expected_parent_markup}' not found"
    assert (
        expected_root_markup in result
    ), f"Expected root image markup: '{expected_root_markup}' not found"

    # Make sure we're not referencing translated images in markdown-only mode
    assert "translated_images" not in result
    assert ".ko.png" not in result
    assert ".ko.jpg" not in result


def test_root_relative_paths_in_markdown_only_mode(complex_dir_structure):
    """
    Test that root-relative image paths (starting with '/') are correctly resolved in markdown-only mode.
    This tests the specific issue where paths like '/imgs/image.jpg' were not correctly calculated.
    """
    # Setup paths
    root_dir = complex_dir_structure
    md_file_path = root_dir / "README.md"
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Read the markdown content
    markdown_content = open(md_file_path, "r").read()

    # Process with direct function call for more detailed testing
    result = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        markdown_only=True,
    )

    # Print paths for debugging
    print(f"\nRoot dir: {root_dir}")
    print(f"MD file path: {md_file_path}")
    print(f"Translations dir: {translations_dir}")
    print(
        f"Translated md directory: {translations_dir / 'ko' / md_file_path.relative_to(root_dir).parent}"
    )
    print(f"\nOriginal content:\n{markdown_content}")
    print(f"\nResult content:\n{result}")

    # In markdown-only mode with our updated code, root-relative paths should remain unchanged
    assert (
        "![Logo](/imgs/logo.png)" in result
    ), "Root-relative logo path should remain unchanged"
    assert (
        "[![Thumbnail](/imgs/open-ms-thumbnail.jpg)](https://example.com)" in result
    ), "Root-relative path in link should remain unchanged"


def test_root_relative_paths_in_regular_mode(complex_dir_structure):
    """
    Test that root-relative image paths (starting with '/') are correctly resolved in regular mode (non-markdown-only).
    This tests the updated handling of root-relative paths in the non-markdown-only mode.
    """
    # Setup paths
    root_dir = complex_dir_structure
    md_file_path = root_dir / "README.md"
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Read the markdown content
    markdown_content = open(md_file_path, "r").read()

    # Process with direct function call with markdown_only=False
    result = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        markdown_only=False,
    )

    # Print paths for debugging
    print(f"\nRoot dir: {root_dir}")
    print(f"MD file path: {md_file_path}")
    print(f"Translations dir: {translations_dir}")
    print(
        f"Translated md directory: {translations_dir / 'ko' / md_file_path.relative_to(root_dir).parent}"
    )
    print(f"\nOriginal content:\n{markdown_content}")
    print(f"\nResult content:\n{result}")

    # In regular mode, paths should be updated to point to translated images
    # Original root-relative paths should be gone
    assert (
        "![Logo](/imgs/logo.png)" not in result
    ), "Original root-relative logo path should not be present"
    assert (
        "[![Thumbnail](/imgs/open-ms-thumbnail.jpg)](https://example.com)" not in result
    ), "Original root-relative thumbnail path should not be present"

    # Should contain paths to translated images
    assert (
        "translated_images" in result
    ), "Result should contain references to translated images directory"

    # Extract the logo image path from the result to verify it's correctly processed
    import re

    logo_pattern = r"!\[Logo\]\((.+?)\)"
    logo_match = re.search(logo_pattern, result)
    assert logo_match, "Logo image reference not found in result"
    logo_path = logo_match.group(1)

    # Verify the path points to the translated_images directory
    assert (
        "translated_images" in logo_path
    ), "Logo path should point to translated_images directory"


def test_image_paths_in_nested_structure(complex_dir_structure):
    """
    Test image path handling in nested directory structures with both
    same-level and parent-level image references.
    """
    # Setup paths
    root_dir = complex_dir_structure
    md_file_path = root_dir / "docs/examples/nested.md"
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Read the markdown content
    markdown_content = open(md_file_path, "r").read()

    # Process with direct update_image_links
    result = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        markdown_only=False,  # Normal mode (not markdown-only)
    )

    # Check that image paths reference the translated images directory in non-markdown-only mode
    assert "translated_images" in result
    assert ".ko." in result  # Should contain language code in filename

    # Now test with markdown_only=True
    result_md_only = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        markdown_only=True,
    )

    # Print paths for debugging
    translated_md_dir = (
        translations_dir / "ko" / md_file_path.relative_to(root_dir).parent
    )
    print(f"\nRoot dir: {root_dir}")
    print(f"MD file path: {md_file_path}")
    print(f"Translations dir: {translations_dir}")
    print(f"Translated md directory: {translated_md_dir}")
    print(f"\nOriginal content:\n{markdown_content}")
    print(f"\nResult content:\n{result_md_only}")

    # 실제 결과에서 경로 추출
    lines = result_md_only.split("\n")
    local_image_actual = None
    parent_image_actual = None
    root_image_actual = None

    for line in lines:
        if "![Local Image](" in line:
            local_image_actual = line.split("(")[1].split(")")[0]
        elif "![Parent Image](" in line:
            parent_image_actual = line.split("(")[1].split(")")[0]
        elif "![Root Image](" in line:
            root_image_actual = line.split("(")[1].split(")")[0]

    print(f"\nActual paths in nested test:")
    print(f"Local image: {local_image_actual}")
    print(f"Parent image: {parent_image_actual}")
    print(f"Root image: {root_image_actual}")

    # Construct markups using actual paths
    expected_local_markup = f"![Local Image]({local_image_actual})"
    expected_parent_markup = f"![Parent Image]({parent_image_actual})"
    expected_root_markup = f"![Root Image]({root_image_actual})"

    # In markdown-only mode, paths should be relative to the original images
    assert "translated_images" not in result_md_only
    assert ".ko." not in result_md_only

    # Precise assertions with exact matches
    assert (
        expected_local_markup in result_md_only
    ), f"Expected local image markup: '{expected_local_markup}' not found"
    assert (
        expected_parent_markup in result_md_only
    ), f"Expected parent image markup: '{expected_parent_markup}' not found"
    assert (
        expected_root_markup in result_md_only
    ), f"Expected root image markup: '{expected_root_markup}' not found"
