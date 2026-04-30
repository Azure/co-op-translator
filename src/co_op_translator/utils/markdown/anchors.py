from __future__ import annotations

import re
from urllib.parse import unquote

from markdown_it import MarkdownIt


def _slugify_heading_text(text: str) -> str:
    """Create a GitHub-style anchor slug from heading text."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^\w\-\u00C0-\uFFFF]", "", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def _extract_headings_with_slugs(markdown: str) -> list[tuple[str, str]]:
    """Extract headings and generated unique slugs from markdown content."""
    headings: list[tuple[str, str]] = []
    slug_counts: dict[str, int] = {}
    tokens = MarkdownIt("commonmark").parse(markdown)

    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue

        if index + 1 >= len(tokens):
            continue
        inline_token = tokens[index + 1]
        if inline_token.type != "inline":
            continue

        heading_text = inline_token.content.strip()
        base_slug = _slugify_heading_text(heading_text)
        if not base_slug:
            continue

        count = slug_counts.get(base_slug, 0)
        slug = f"{base_slug}-{count}" if count else base_slug
        slug_counts[base_slug] = count + 1
        headings.append((heading_text, slug))

    return headings


def _extract_internal_link_fragments(markdown: str) -> set[str]:
    """Extract internal markdown-link fragments (without '#') using markdown-it AST."""
    fragments: set[str] = set()
    tokens = MarkdownIt("commonmark").parse(markdown)

    for token in tokens:
        if token.type != "inline" or not token.children:
            continue

        for child in token.children:
            if child.type != "link_open":
                continue

            href = child.attrGet("href")
            if not href or not href.startswith("#"):
                continue

            fragments.add(unquote(href[1:]).strip().lower())

    return fragments


def normalize_internal_anchor_links(
    source_markdown: str, translated_markdown: str
) -> str:
    """Align translated internal fragment links with translated heading slugs.

    This function only rewrites fragment identifiers (the `#...` part of links).
    Heading text in the translated document is never modified.
    """
    source_headings = _extract_headings_with_slugs(source_markdown)
    translated_headings = _extract_headings_with_slugs(translated_markdown)

    if not source_headings or not translated_headings:
        return translated_markdown

    source_slug_to_index = {slug: idx for idx, (_, slug) in enumerate(source_headings)}
    translated_slugs = [slug for _, slug in translated_headings]
    translated_internal_fragments = _extract_internal_link_fragments(
        translated_markdown
    )

    translated_link_pattern = re.compile(r"(\[[^\]]+\]\(#)([^\)]+)(\))")

    def _replace_fragment(match: re.Match[str]) -> str:
        current_fragment = unquote(match.group(2)).strip().lower()
        if current_fragment not in translated_internal_fragments:
            return match.group(0)

        source_target_index = source_slug_to_index.get(current_fragment)

        # If the translated link is no longer using the source fragment,
        # keep it untouched instead of doing positional remapping.
        if source_target_index is None or source_target_index >= len(translated_slugs):
            return match.group(0)

        return (
            f"{match.group(1)}{translated_slugs[source_target_index]}{match.group(3)}"
        )

    return translated_link_pattern.sub(_replace_fragment, translated_markdown)
