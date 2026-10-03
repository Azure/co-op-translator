from __future__ import annotations

from dataclasses import dataclass

from markdown_it import MarkdownIt


@dataclass(frozen=True, order=True)
class MarkdownSpan:
    """An exact half-open character span in Markdown source."""

    start: int
    end: int
    kind: str


def _line_offsets(document: str) -> list[int]:
    offsets = [0]
    for line in document.splitlines(keepends=True):
        offsets.append(offsets[-1] + len(line))
    return offsets


def _inline_code_spans(segment: str, absolute_start: int) -> list[MarkdownSpan]:
    spans: list[MarkdownSpan] = []
    position = 0
    while position < len(segment):
        if segment[position] != "`" or not _is_unescaped(segment, position):
            position += 1
            continue

        marker_length = 1
        while (
            position + marker_length < len(segment)
            and segment[position + marker_length] == "`"
        ):
            marker_length += 1

        closing = position + marker_length
        while closing < len(segment):
            if segment[closing] != "`" or not _is_unescaped(segment, closing):
                closing += 1
                continue

            closing_length = 1
            while (
                closing + closing_length < len(segment)
                and segment[closing + closing_length] == "`"
            ):
                closing_length += 1

            if closing_length == marker_length:
                spans.append(
                    MarkdownSpan(
                        absolute_start + position,
                        absolute_start + closing + closing_length,
                        "inline_code",
                    )
                )
                position = closing + closing_length
                break
            closing += closing_length
        else:
            position += marker_length

    return spans


def _is_unescaped(text: str, position: int) -> bool:
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return backslashes % 2 == 0


def markdown_code_spans(document: str) -> list[MarkdownSpan]:
    """Return exact fenced, indented, and inline code spans."""

    parser = MarkdownIt("commonmark")
    tokens = parser.parse(document)
    offsets = _line_offsets(document)
    block_spans: list[MarkdownSpan] = []
    inline_spans: list[MarkdownSpan] = []

    for token in tokens:
        if token.type in {"fence", "code_block"} and token.map:
            start_line, end_line = token.map
            block_spans.append(
                MarkdownSpan(offsets[start_line], offsets[end_line], token.type)
            )
            continue

        if token.type != "inline" or not token.map or not token.children:
            continue
        if not any(child.type == "code_inline" for child in token.children):
            continue

        start_line, end_line = token.map
        region_start = offsets[start_line]
        region_end = offsets[end_line]
        inline_spans.extend(
            _inline_code_spans(document[region_start:region_end], region_start)
        )

    spans = sorted(block_spans + inline_spans)
    merged: list[MarkdownSpan] = []
    for span in spans:
        if merged and span.start >= merged[-1].start and span.end <= merged[-1].end:
            continue
        merged.append(span)
    return merged


def mask_markdown_code(document: str) -> str:
    """Mask code while retaining source length and line boundaries."""

    characters = list(document)
    for span in markdown_code_spans(document):
        for index in range(span.start, span.end):
            if characters[index] not in {"\n", "\r"}:
                characters[index] = " "
    return "".join(characters)


def replace_markdown_code(document: str) -> tuple[str, dict[str, str]]:
    """Replace all Markdown code forms with exact, restorable placeholders."""

    placeholder_map: dict[str, str] = {}
    replacements: list[tuple[int, int, str]] = []
    marker_indexes = {"block": 0, "inline": 0}
    for span in markdown_code_spans(document):
        marker_kind = "block" if span.kind in {"fence", "code_block"} else "inline"
        marker_prefix = "CODE_BLOCK" if marker_kind == "block" else "INLINE_CODE"
        marker_index = marker_indexes[marker_kind]
        marker = f"@@{marker_prefix}_{marker_index}@@"
        while marker in document or marker in placeholder_map:
            marker_index += 1
            marker = f"@@{marker_prefix}_{marker_index}@@"
        placeholder_map[marker] = document[span.start : span.end]
        replacements.append((span.start, span.end, marker))
        marker_indexes[marker_kind] = marker_index + 1

    protected = document
    for start, end, marker in reversed(replacements):
        protected = protected[:start] + marker + protected[end:]
    return protected, placeholder_map


def restore_markdown_code(document: str, placeholder_map: dict[str, str]) -> str:
    """Restore protected code and reject missing or duplicated placeholders."""

    for marker, literal in placeholder_map.items():
        count = document.count(marker)
        if count != 1:
            raise ValueError(
                f"Expected code placeholder {marker!r} exactly once, found {count}."
            )
        document = document.replace(marker, literal, 1)
    return document
