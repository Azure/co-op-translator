"""Tests for frontmatter parsing and translation utilities."""

from pathlib import Path
from co_op_translator.utils.markdown.frontmatter import (
    FrontmatterConfig,
    FrontmatterParser,
    QuickLinksFrontmatterParser,
    ensure_quicklinks_frontmatter_parser,
    get_frontmatter_parser,
    adjust_frontmatter_links,
)


class TestFrontmatterConfig:
    """Test frontmatter configuration loading and field classification."""

    def test_load_default_config(self):
        """Test loading default bundled configuration."""
        config = FrontmatterConfig()

        # Should have preserve fields
        assert len(config.preserve_fields) > 0
        assert "slug" in config.preserve_fields
        assert "id" in config.preserve_fields
        assert "order" in config.preserve_fields
        assert "section" in config.preserve_fields

        # Should have translate fields
        assert len(config.translate_fields) > 0
        assert "title" in config.translate_fields
        assert "description" in config.translate_fields

    def test_should_preserve(self):
        """Test field preservation check."""
        config = FrontmatterConfig()

        assert config.should_preserve("slug") is True
        assert config.should_preserve("id") is True
        assert config.should_preserve("order") is True
        assert config.should_preserve("title") is False

    def test_should_translate(self):
        """Test field translation check."""
        config = FrontmatterConfig()

        assert config.should_translate("title") is True
        assert config.should_translate("description") is True
        assert config.should_translate("slug") is False
        assert config.should_translate("id") is False


class TestFrontmatterParser:
    """Test frontmatter parsing and reconstruction."""

    def test_extract_frontmatter_with_valid_yaml(self):
        """Test extracting valid YAML frontmatter."""
        content = """---
title: Getting Started
slug: getting-started
section: introduction
order: 1
---
# Welcome

This is the body content.
"""
        parser = FrontmatterParser()
        frontmatter, body = parser.extract_frontmatter(content)

        assert frontmatter is not None
        assert frontmatter["title"] == "Getting Started"
        assert frontmatter["slug"] == "getting-started"
        assert frontmatter["section"] == "introduction"
        assert frontmatter["order"] == 1
        assert body.strip().startswith("# Welcome")

    def test_extract_frontmatter_without_frontmatter(self):
        """Test extracting from content without frontmatter."""
        content = """# Welcome

This is just body content.
"""
        parser = FrontmatterParser()
        frontmatter, body = parser.extract_frontmatter(content)

        assert frontmatter is None
        assert body == content

    def test_extract_frontmatter_with_invalid_yaml(self):
        """Test extracting invalid YAML frontmatter."""
        content = """---
title: Getting Started
invalid yaml here: [unclosed bracket
---
# Welcome
"""
        parser = FrontmatterParser()
        frontmatter, body = parser.extract_frontmatter(content)

        # Should treat as no frontmatter on parse error
        assert frontmatter is None
        assert body == content

    def test_split_fields(self):
        """Test splitting frontmatter fields into preserve and translate."""
        frontmatter = {
            "title": "Getting Started",
            "description": "Welcome to our docs",
            "slug": "getting-started",
            "section": "introduction",
            "order": 1,
        }

        parser = FrontmatterParser()
        preserve, translate = parser.split_fields(frontmatter)

        # Preserve fields
        assert "slug" in preserve
        assert "section" in preserve
        assert "order" in preserve
        assert preserve["slug"] == "getting-started"
        assert preserve["order"] == 1

        # Translate fields
        assert "title" in translate
        assert "description" in translate
        assert translate["title"] == "Getting Started"
        assert translate["description"] == "Welcome to our docs"

    def test_split_fields_unknown_field_preserved(self):
        """Test that unknown fields are preserved by default."""
        frontmatter = {
            "title": "Getting Started",
            "unknown_field": "some value",
        }

        parser = FrontmatterParser()
        preserve, translate = parser.split_fields(frontmatter)

        # Unknown field should be preserved for safety
        assert "unknown_field" in preserve
        assert preserve["unknown_field"] == "some value"

    def test_merge_fields(self):
        """Test merging preserved and translated fields."""
        preserve = {
            "slug": "getting-started",
            "section": "introduction",
            "order": 1,
        }
        translate = {
            "title": "시작하기",
            "description": "문서에 오신 것을 환영합니다",
        }

        parser = FrontmatterParser()
        merged = parser.merge_fields(preserve, translate)

        assert merged["slug"] == "getting-started"
        assert merged["section"] == "introduction"
        assert merged["order"] == 1
        assert merged["title"] == "시작하기"
        assert merged["description"] == "문서에 오신 것을 환영합니다"

    def test_reconstruct_content_with_frontmatter(self):
        """Test reconstructing content with frontmatter."""
        frontmatter = {
            "title": "시작하기",
            "description": "문서에 오신 것을 환영합니다",
            "slug": "getting-started",
            "section": "introduction",
            "order": 1,
        }
        body = "# 환영합니다\n\n번역된 내용입니다."

        parser = FrontmatterParser()
        result = parser.reconstruct_content(frontmatter, body)

        assert result.startswith("---\n")
        assert "title: 시작하기" in result
        assert "slug: getting-started" in result
        assert "order: 1" in result
        assert "# 환영합니다" in result

    def test_reconstruct_content_without_frontmatter(self):
        """Test reconstructing content without frontmatter."""
        body = "# Welcome\n\nBody content."

        parser = FrontmatterParser()
        result = parser.reconstruct_content(None, body)

        assert result == body

    def test_extract_translatable_fields_as_markdown(self):
        """Test converting translatable fields to markdown format."""
        translate_fields = {
            "title": "Getting Started",
            "description": "Welcome to our documentation",
        }

        parser = FrontmatterParser()
        markdown = parser.extract_translatable_fields_as_markdown(translate_fields)

        assert "**title**: Getting Started" in markdown
        assert "**description**: Welcome to our documentation" in markdown

    def test_parse_translated_fields_from_markdown(self):
        """Test parsing translated fields from markdown."""
        original_fields = {
            "title": "Getting Started",
            "description": "Welcome to our documentation",
        }
        translated_markdown = """**title**: 시작하기
**description**: 문서에 오신 것을 환영합니다"""

        parser = FrontmatterParser()
        translated = parser.parse_translated_fields_from_markdown(
            translated_markdown, original_fields
        )

        assert "title" in translated
        assert "description" in translated
        assert translated["title"] == "시작하기"
        assert translated["description"] == "문서에 오신 것을 환영합니다"

    def test_end_to_end_frontmatter_workflow(self):
        """Test complete frontmatter translation workflow."""
        original_content = """---
title: Getting Started
description: Welcome to our docs
slug: getting-started
section: introduction
order: 1
---
# Welcome

This is the body content.
"""

        parser = FrontmatterParser()

        # Step 1: Extract frontmatter
        frontmatter, body = parser.extract_frontmatter(original_content)
        assert frontmatter is not None

        # Step 2: Split fields
        preserve, translate = parser.split_fields(frontmatter)
        assert "slug" in preserve
        assert "title" in translate

        # Step 3: Simulate translation (in real scenario, this goes to LLM)
        translated_fields = {
            "title": "시작하기",
            "description": "문서에 오신 것을 환영합니다",
        }

        # Step 4: Merge fields
        merged = parser.merge_fields(preserve, translated_fields)

        # Step 5: Reconstruct content
        translated_body = "# 환영합니다\n\n번역된 내용입니다."
        result = parser.reconstruct_content(merged, translated_body)

        # Verify result
        assert "---" in result
        assert "title: 시작하기" in result
        assert "slug: getting-started" in result  # Preserved
        assert "section: introduction" in result  # Preserved
        assert "order: 1" in result  # Preserved
        assert "# 환영합니다" in result


class TestGetFrontmatterParser:
    """Test singleton parser getter."""

    def test_get_default_parser(self):
        """Test getting default parser instance."""
        parser = get_frontmatter_parser()
        assert parser is not None
        assert isinstance(parser, FrontmatterParser)
        assert isinstance(parser, QuickLinksFrontmatterParser)

    def test_singleton_behavior(self):
        """Test that parser is reused (singleton pattern)."""
        parser1 = get_frontmatter_parser()
        parser2 = get_frontmatter_parser()
        assert parser1 is parser2

    def test_ensure_quicklinks_parser_overrides_default(self):
        parser = ensure_quicklinks_frontmatter_parser()
        assert isinstance(parser, QuickLinksFrontmatterParser)

        again = get_frontmatter_parser()
        assert again is parser


class TestQuickLinksFrontmatterParser:
    def test_split_fields_promotes_nested_strings(self):
        parser = QuickLinksFrontmatterParser()
        frontmatter = {
            "title": "Getting Started",
            "quickLinks": [
                {
                    "slug": "getting-started",
                    "title": "Getting Started",
                    "description": "Learn the basics",
                },
                {
                    "slug": "advanced",
                    "title": "Advanced",
                    "description": "Go deeper",
                },
            ],
        }

        preserve, translate = parser.split_fields(frontmatter)

        assert "quickLinks" in preserve
        assert preserve["quickLinks"][0]["slug"] == "getting-started"
        assert translate["quickLinks[0].title"] == "Getting Started"
        assert translate["quickLinks[0].description"] == "Learn the basics"
        assert translate["quickLinks[1].title"] == "Advanced"
        assert translate["quickLinks[1].description"] == "Go deeper"

    def test_merge_fields_reinserts_quicklinks_translations(self):
        parser = QuickLinksFrontmatterParser()
        preserve = {
            "quickLinks": [
                {
                    "slug": "getting-started",
                    "title": "Getting Started",
                    "description": "Learn the basics",
                },
                {
                    "slug": "advanced",
                    "title": "Advanced",
                    "description": "Go deeper",
                },
            ]
        }
        translated = {
            "quickLinks[0].title": "시작하기",
            "quickLinks[0].description": "기본을 배우세요",
            "quickLinks[1].title": "고급",
            "quickLinks[1].description": "더 깊이 탐구하세요",
        }

        merged = parser.merge_fields(preserve, translated)

        assert merged["quickLinks"][0]["title"] == "시작하기"
        assert merged["quickLinks"][0]["description"] == "기본을 배우세요"
        assert merged["quickLinks"][0]["slug"] == "getting-started"
        assert merged["quickLinks"][1]["title"] == "고급"
        assert merged["quickLinks"][1]["description"] == "더 깊이 탐구하세요"


class TestAdjustFrontmatterLinks:
    """Test frontmatter link adjustment functionality."""

    def test_adjust_relative_image_path_markdown_only(self, tmp_path):
        """Test adjusting relative image path in markdown-only mode."""
        # Setup directory structure
        root_dir = tmp_path / "project"
        root_dir.mkdir()

        docs_dir = root_dir / "docs"
        docs_dir.mkdir()

        images_dir = root_dir / "images"
        images_dir.mkdir()

        # Create a dummy image file
        image_file = images_dir / "hero.png"
        image_file.write_text("dummy")

        # Create markdown file
        md_file = docs_dir / "guide.md"
        md_file.write_text("# Guide")

        # Frontmatter with relative image path
        frontmatter = {
            "title": "Getting Started",
            "image": "../images/hero.png",
            "slug": "getting-started",
        }

        translations_dir = root_dir / "translations"
        translated_images_dir = root_dir / "translated_images"

        # Adjust links (markdown-only mode: images not in translation_types)
        adjusted = adjust_frontmatter_links(
            frontmatter,
            md_file,
            "ko",
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types=["markdown"],  # No images
        )

        # Should point to original image with adjusted relative path
        assert "image" in adjusted
        # From translations/ko/docs/guide.md to images/hero.png
        assert adjusted["image"] == "../../../images/hero.png"

        # Other fields should be unchanged
        assert adjusted["title"] == "Getting Started"
        assert adjusted["slug"] == "getting-started"

    def test_adjust_root_relative_path(self, tmp_path):
        """Test adjusting root-relative path."""
        root_dir = tmp_path / "project"
        root_dir.mkdir()

        docs_dir = root_dir / "docs"
        docs_dir.mkdir()

        md_file = docs_dir / "guide.md"
        md_file.write_text("# Guide")

        frontmatter = {
            "title": "Guide",
            "canonical_url": "/docs/guide",
        }

        translations_dir = root_dir / "translations"
        translated_images_dir = root_dir / "translated_images"

        adjusted = adjust_frontmatter_links(
            frontmatter,
            md_file,
            "ko",
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types=["markdown"],
        )

        # Root-relative paths should be kept as-is
        assert adjusted["canonical_url"] == "/docs/guide"

    def test_skip_web_urls(self, tmp_path):
        """Test that web URLs are not modified."""
        root_dir = tmp_path / "project"
        root_dir.mkdir()

        md_file = root_dir / "README.md"
        md_file.write_text("# README")

        frontmatter = {
            "title": "Project",
            "og_image": "https://example.com/image.png",
            "canonical_url": "https://example.com/docs",
        }

        translations_dir = root_dir / "translations"
        translated_images_dir = root_dir / "translated_images"

        adjusted = adjust_frontmatter_links(
            frontmatter,
            md_file,
            "ko",
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types=["markdown"],
        )

        # Web URLs should remain unchanged
        assert adjusted["og_image"] == "https://example.com/image.png"
        assert adjusted["canonical_url"] == "https://example.com/docs"

    def test_adjust_with_translated_images(self, tmp_path):
        """Test adjusting image paths when using translated images."""
        root_dir = tmp_path / "project"
        root_dir.mkdir()

        docs_dir = root_dir / "docs"
        docs_dir.mkdir()

        images_dir = root_dir / "images"
        images_dir.mkdir()

        image_file = images_dir / "hero.png"
        image_file.write_text("dummy")

        md_file = docs_dir / "guide.md"
        md_file.write_text("# Guide")

        frontmatter = {
            "title": "Getting Started",
            "image": "../images/hero.png",
        }

        translations_dir = root_dir / "translations"
        translated_images_dir = root_dir / "translated_images"

        # Adjust links with images in translation_types
        adjusted = adjust_frontmatter_links(
            frontmatter,
            md_file,
            "ko",
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types=["markdown", "images"],  # Images enabled
        )

        # Should point to translated image directory
        assert "image" in adjusted
        # Path should point to translated_images with language-specific filename
        assert "translated_images" in adjusted["image"]
        assert "/ko/" in adjusted["image"] or adjusted["image"].startswith("../ko/")

    def test_adjust_with_translated_images_and_lang_subdir(self, tmp_path):
        """Test translated image paths remain correct when lang_subdir is used."""
        root_dir = tmp_path / "project"
        root_dir.mkdir()

        docs_dir = root_dir / "docs"
        docs_dir.mkdir()

        images_dir = root_dir / "images"
        images_dir.mkdir()

        image_file = images_dir / "hero.png"
        image_file.write_text("dummy")

        md_file = docs_dir / "guide.md"
        md_file.write_text("# Guide")

        frontmatter = {
            "title": "Getting Started",
            "image": "../images/hero.png",
        }

        translations_dir = root_dir / "translations"
        translated_images_dir = root_dir / "translated_images"

        adjusted = adjust_frontmatter_links(
            frontmatter,
            md_file,
            "ko",
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types=["markdown", "images"],
            lang_subdir=Path("docs"),
        )

        assert adjusted["image"].startswith("../../../../translated_images/ko/")
        assert adjusted["image"].endswith(".webp")

    def test_no_modification_for_non_path_fields(self, tmp_path):
        """Test that non-path fields are not modified."""
        root_dir = tmp_path / "project"
        root_dir.mkdir()

        md_file = root_dir / "README.md"
        md_file.write_text("# README")

        frontmatter = {
            "title": "Project",
            "description": "A great project",
            "order": 1,
            "tags": ["python", "translation"],
        }

        translations_dir = root_dir / "translations"
        translated_images_dir = root_dir / "translated_images"

        adjusted = adjust_frontmatter_links(
            frontmatter,
            md_file,
            "ko",
            root_dir,
            translations_dir,
            translated_images_dir,
            translation_types=["markdown"],
        )

        # All fields should remain unchanged (no path fields)
        assert adjusted == frontmatter
