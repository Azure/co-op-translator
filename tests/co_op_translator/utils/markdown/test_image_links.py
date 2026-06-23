import os
import re
from pathlib import Path

import pytest

from co_op_translator.utils.markdown.image_links import update_image_links


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
    assert ".webp" in result  # All translated images are now WebP format
    assert "test.png" not in result  # Original image links should be updated


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


def test_untranslated_images_mode_image_paths(complex_dir_structure):
    """
    Test that image paths are correctly resolved in untranslated images mode.
    This tests the specific issue where image paths were not correctly calculated
    in untranslated images mode, especially with nested directory structures.
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
        use_translated_images=False,
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

    print("\nExpected paths:")
    print(f"Local image: {expected_local_path}")
    print(f"Parent image: {expected_parent_path}")
    print(f"Root image: {expected_root_path}")
    print(f"\nResult content:\n{result}")

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

    print("\nActual paths:")
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

    # Make sure we're not referencing translated images in untranslated images mode
    assert "translated_images" not in result
    assert ".ko.png" not in result
    assert ".ko.jpg" not in result


def test_root_relative_paths_in_untranslated_images_mode(complex_dir_structure):
    """
    Test that root-relative image paths (starting with '/') are correctly resolved in untranslated images mode.
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
        use_translated_images=False,
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

    # In untranslated images mode with our updated code, root-relative paths should remain unchanged
    assert (
        "![Logo](/imgs/logo.png)" in result
    ), "Root-relative logo path should remain unchanged"
    assert (
        "[![Thumbnail](/imgs/open-ms-thumbnail.jpg)](https://example.com)" in result
    ), "Root-relative path in link should remain unchanged"


def test_root_relative_paths_in_regular_mode(complex_dir_structure):
    """
    Test that root-relative image paths (starting with '/') are correctly resolved in regular mode (non-markdown-only).
    This tests the updated handling of root-relative paths in the non-untranslated images mode.
    """
    # Setup paths
    root_dir = complex_dir_structure
    md_file_path = root_dir / "README.md"
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Read the markdown content
    markdown_content = open(md_file_path, "r").read()

    # Process with direct function call with use_translated_images=True
    result = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        use_translated_images=True,
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
        use_translated_images=True,  # Translated images mode
    )

    # Check that image paths reference the translated images directory in translated images mode
    assert "translated_images" in result
    assert (
        "translated_images/ko/" in result
    )  # Should contain language code in directory path

    # Now test with use_translated_images=False (original images mode)
    result_md_only = update_image_links(
        markdown_content,
        md_file_path,
        "ko",
        translations_dir,
        translated_images_dir,
        root_dir,
        use_translated_images=False,
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

    print("\nActual paths in nested test:")
    print(f"Local image: {local_image_actual}")
    print(f"Parent image: {parent_image_actual}")
    print(f"Root image: {root_image_actual}")

    # Construct markups using actual paths
    expected_local_markup = f"![Local Image]({local_image_actual})"
    expected_parent_markup = f"![Parent Image]({parent_image_actual})"
    expected_root_markup = f"![Root Image]({root_image_actual})"

    # In untranslated images mode, paths should be relative to the original images
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


def test_image_path_depth_in_nested_translations(complex_dir_structure):
    """
    Regression test for incorrect relative path depth (e.g., ../../../../../ vs ../../../).
    Tests a file at '15-rag-and-vector-databases/README.md' translated to 'et'.
    The translated file is at 'translations/et/15-rag-and-vector-databases/README.md'.
    The images are at 'translated_images/et/'.
    The relative path from 'translations/et/15-rag-and-vector-databases/' to 'translated_images/et/'
    should be '../../../translated_images/et/'.
    """
    root_dir = complex_dir_structure
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"

    # Create the nested directory structure
    md_rel_path = Path("15-rag-and-vector-databases/README.md")
    md_file_path = root_dir / md_rel_path
    md_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create a dummy image file to ensure generate_translated_filename works
    img_rel_path = Path("imgs/banner.png")
    img_file_path = root_dir / img_rel_path
    img_file_path.parent.mkdir(parents=True, exist_ok=True)
    img_file_path.write_text("dummy image content")

    language_code = "et"
    markdown_content = f"![Banner]({img_rel_path.as_posix()})"

    # Process
    result = update_image_links(
        markdown_content,
        md_file_path,
        language_code,
        translations_dir,
        translated_images_dir,
        root_dir,
        use_translated_images=True,
    )

    # The translated MD will be at: translations/et/15-rag-and-vector-databases/README.md
    # The translated images at: translated_images/et/
    # Distance:
    # 1. 15-rag-and-vector-databases/ -> ..
    # 2. et/ -> ..
    # 3. translations/ -> ..
    # Total: ../../../

    assert "../../../translated_images/et/" in result
    assert "../../../../../" not in result


def test_webp_translated_images_prefix_depth_is_normalized(complex_dir_structure):
    root_dir = complex_dir_structure
    translations_dir = root_dir / "translations"
    translated_images_dir = root_dir / "translated_images"
    translations_dir.mkdir(parents=True, exist_ok=True)
    translated_images_dir.mkdir(parents=True, exist_ok=True)

    md_rel_path = Path("15-rag-and-vector-databases/README.md")
    md_file_path = root_dir / md_rel_path
    md_file_path.parent.mkdir(parents=True, exist_ok=True)

    language_code = "et"
    # Intentionally wrong depth (one extra ../) pointing to an already-translated WebP
    markdown_content = (
        "![Banner](../../../../translated_images/et/foo.1234567890abcdef.webp)"
    )

    result = update_image_links(
        markdown_content,
        md_file_path,
        language_code,
        translations_dir,
        translated_images_dir,
        root_dir,
        use_translated_images=True,
    )

    assert "../../../translated_images/et/foo.1234567890abcdef.webp" in result
    assert "../../../../translated_images/et/foo.1234567890abcdef.webp" not in result
