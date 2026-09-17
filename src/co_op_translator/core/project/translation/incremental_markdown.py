from __future__ import annotations

import hashlib
import re
from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Awaitable, Callable

from markdown_it import MarkdownIt

from co_op_translator.core.project.translation.memory import (
    TranslationBaseline,
    TranslationUpdate,
)

DISCLAIMER_START = "<!-- CO-OP TRANSLATOR DISCLAIMER START -->"
DISCLAIMER_END = "<!-- CO-OP TRANSLATOR DISCLAIMER END -->"


@dataclass(frozen=True)
class MarkdownBlock:
    kind: str
    text: str

    @property
    def fingerprint(self) -> str:
        normalized = self.text.rstrip()
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _split_frontmatter(text: str) -> tuple[str | None, str]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text

    for index in range(1, len(lines)):
        if lines[index].strip() in {"---", "..."}:
            end = index + 1
            return "".join(lines[:end]), "".join(lines[end:])
    return None, text


def _token_kind(token) -> str:
    token_type = token.type
    if token_type == "heading_open":
        return f"heading:{token.tag}"
    if token_type in {"bullet_list_open", "ordered_list_open"}:
        return "list"
    if token_type == "blockquote_open":
        return "blockquote"
    if token_type == "table_open":
        return "table"
    if token_type in {"fence", "code_block"}:
        return "code"
    if token_type == "html_block":
        return "html"
    if token_type == "paragraph_open":
        return "paragraph"
    if token_type == "hr":
        return "thematic_break"
    return token_type.removesuffix("_open")


def split_markdown_blocks(text: str) -> list[MarkdownBlock]:
    """Split Markdown into stable top-level structural blocks.

    Token-sized chunks used for LLM limits are intentionally not reused here:
    their boundaries move when nearby text changes. Top-level Markdown blocks
    provide a conservative one-to-one structure for source/target alignment.
    """

    frontmatter, body = _split_frontmatter(text)
    blocks: list[MarkdownBlock] = []
    if frontmatter is not None:
        blocks.append(MarkdownBlock("frontmatter", frontmatter))

    if not body:
        return blocks

    lines = body.splitlines(keepends=True)
    parser = MarkdownIt("commonmark").enable("table")
    tokens = parser.parse(body)
    spans: list[tuple[int, int, str]] = []

    for token in tokens:
        if token.level != 0 or token.map is None or token.nesting == -1:
            continue
        start, end = token.map
        if end <= start:
            continue
        if spans and start < spans[-1][1]:
            continue
        spans.append((start, end, _token_kind(token)))

    if not spans:
        blocks.append(MarkdownBlock("text", body))
        return blocks

    if spans[0][0] > 0:
        blocks.append(MarkdownBlock("text", "".join(lines[: spans[0][0]])))

    for index, (start, end, kind) in enumerate(spans):
        next_start = spans[index + 1][0] if index + 1 < len(spans) else len(lines)
        block_end = max(end, next_start)
        blocks.append(MarkdownBlock(kind, "".join(lines[start:block_end])))

    return [block for block in blocks if block.text]


def strip_managed_disclaimer(text: str) -> str:
    start = text.find(DISCLAIMER_START)
    if start < 0:
        return text
    end = text.find(DISCLAIMER_END, start)
    if end < 0:
        return text

    end += len(DISCLAIMER_END)
    prefix = text[:start]
    suffix = text[end:]
    prefix = re.sub(r"\n*---\s*\n*$", "", prefix)
    return (prefix + suffix).rstrip() + ("\n" if text.endswith("\n") else "")


def _structure(blocks: list[MarkdownBlock]) -> list[str]:
    return [block.kind for block in blocks]


def _restore_trailing_whitespace(source: str, translated: str) -> str:
    match = re.search(r"\s*$", source)
    trailing = match.group(0) if match else ""
    return translated.rstrip() + trailing


async def build_incremental_markdown(
    *,
    baseline: TranslationBaseline,
    current_source: str,
    current_target: str,
    translate_block: Callable[[str], Awaitable[str]],
) -> TranslationUpdate:
    """Preserve unchanged target blocks and translate changed source blocks.

    The function is deliberately conservative. Any ambiguous source/target
    alignment returns ``mode="full"`` so the caller can use the established
    whole-file translation path.
    """

    previous_source_blocks = split_markdown_blocks(baseline.source_text)
    previous_target_blocks = split_markdown_blocks(
        strip_managed_disclaimer(baseline.target_text)
    )
    current_source_blocks = split_markdown_blocks(current_source)
    current_target_blocks = split_markdown_blocks(
        strip_managed_disclaimer(current_target)
    )

    if not previous_source_blocks or not previous_target_blocks:
        return TranslationUpdate(
            content="", mode="full", fallback_reason="empty_baseline"
        )

    if _structure(previous_source_blocks) != _structure(previous_target_blocks):
        return TranslationUpdate(
            content="", mode="full", fallback_reason="baseline_structure_mismatch"
        )

    if _structure(previous_target_blocks) != _structure(current_target_blocks):
        return TranslationUpdate(
            content="", mode="full", fallback_reason="current_target_structure_changed"
        )

    matcher = SequenceMatcher(
        a=[block.fingerprint for block in previous_source_blocks],
        b=[block.fingerprint for block in current_source_blocks],
        autojunk=False,
    )
    opcodes = matcher.get_opcodes()

    if any(tag != "equal" for tag, *_ in opcodes):
        previous_counts = Counter(block.fingerprint for block in previous_source_blocks)
        current_counts = Counter(block.fingerprint for block in current_source_blocks)
        if any(count > 1 for count in previous_counts.values()) or any(
            count > 1 for count in current_counts.values()
        ):
            return TranslationUpdate(
                content="",
                mode="full",
                fallback_reason="ambiguous_duplicate_blocks",
            )

    output: list[str] = []
    preserved = translated = added = deleted = 0

    for tag, old_start, old_end, new_start, new_end in opcodes:
        if tag == "equal":
            output.extend(
                block.text for block in current_target_blocks[old_start:old_end]
            )
            preserved += old_end - old_start
            continue

        if tag in {"replace", "delete"}:
            deleted += old_end - old_start

        if tag in {"replace", "insert"}:
            for block in current_source_blocks[new_start:new_end]:
                translated_text = await translate_block(block.text)
                if not translated_text:
                    return TranslationUpdate(
                        content="",
                        mode="full",
                        fallback_reason="empty_block_translation",
                    )
                translated_text = _restore_trailing_whitespace(
                    block.text, translated_text
                )
                translated_blocks = split_markdown_blocks(translated_text)
                if _structure(translated_blocks) != [block.kind]:
                    return TranslationUpdate(
                        content="",
                        mode="full",
                        fallback_reason="translated_block_structure_mismatch",
                    )
                output.append(translated_text)
                translated += 1
                if tag == "insert":
                    added += 1

    content = "".join(output)
    if _structure(split_markdown_blocks(content)) != _structure(current_source_blocks):
        return TranslationUpdate(
            content="", mode="full", fallback_reason="final_structure_mismatch"
        )

    return TranslationUpdate(
        content=content,
        mode="incremental",
        preserved_units=preserved,
        translated_units=translated,
        added_units=added,
        deleted_units=deleted,
    )
