from __future__ import annotations

import re
from dataclasses import dataclass

from markdown_it import MarkdownIt
from markdown_it.common.utils import isStrSpace
from markdown_it.rules_inline.autolink import autolink as parse_autolink
from markdown_it.rules_inline.html_inline import html_inline as parse_html_inline
from markdown_it.rules_inline.image import image as parse_image
from markdown_it.rules_inline.link import link as parse_link
from markdown_it.rules_inline.state_inline import StateInline
from markdown_it.token import Token

from co_op_translator.utils.markdown.spans import mask_markdown_code

_DESTINATION_SPANS_ENV_KEY = "co_op_translator_link_destination_spans"
_HTML_ATTRIBUTE_RE = re.compile(
    r"(?ix)\b(?P<name>href|src)\s*=\s*"
    r'(?:"(?P<double>[^"]*)"|\'(?P<single>[^\']*)\'|(?P<bare>[^\s\"\'=<>`]+))'
)
_BARE_URL_PREFIXES = ("http://", "https://")
_TRAILING_URL_PUNCTUATION = ".,;:!?"


@dataclass(frozen=True, order=True)
class _DestinationSpan:
    start: int
    end: int
    kind: str


def _record_span(state: StateInline, start: int, end: int, kind: str) -> None:
    destination = state.src[start:end]
    if destination:
        state.env.setdefault(_DESTINATION_SPANS_ENV_KEY, []).append(
            _DestinationSpan(start, end, kind)
        )


def _destination_span_from_markdown_it(
    state: StateInline, marker_start: int, *, is_image: bool
) -> tuple[int, int] | None:
    label_marker = marker_start + 1 if is_image else marker_start
    label_end = state.md.helpers.parseLinkLabel(
        state,
        label_marker,
        not is_image,
    )
    if label_end < 0:
        return None

    position = label_end + 1
    if position >= state.posMax or state.src[position] != "(":
        return None

    position += 1
    while position < state.posMax:
        char = state.src[position]
        if not isStrSpace(char) and char != "\n":
            break
        position += 1

    result = state.md.helpers.parseLinkDestination(
        state.src,
        position,
        state.posMax,
    )
    if not result.ok:
        return None

    start = position
    end = result.pos
    if state.src[start] == "<":
        start += 1
        end -= 1

    destination = state.src[start:end]
    if not destination:
        return None
    return start, end


def _capture_link_destination(state: StateInline, silent: bool) -> bool:
    marker_start = state.pos
    span = (
        None
        if silent
        else _destination_span_from_markdown_it(state, marker_start, is_image=False)
    )
    matched = parse_link(state, silent)
    if matched and span is not None:
        _record_span(state, *span, "link")
    return matched


def _capture_image_destination(state: StateInline, silent: bool) -> bool:
    marker_start = state.pos
    span = (
        None
        if silent
        else _destination_span_from_markdown_it(state, marker_start, is_image=True)
    )
    matched = parse_image(state, silent)
    if matched and span is not None:
        _record_span(state, *span, "image")
    return matched


def _capture_autolink_destination(state: StateInline, silent: bool) -> bool:
    marker_start = state.pos
    matched = parse_autolink(state, silent)
    if matched and not silent and state.pos >= marker_start + 2:
        _record_span(state, marker_start + 1, state.pos - 1, "autolink")
    return matched


def _capture_html_destinations(state: StateInline, silent: bool) -> bool:
    marker_start = state.pos
    matched = parse_html_inline(state, silent)
    if not matched or silent:
        return matched

    html = state.src[marker_start : state.pos]
    tag_match = re.match(r"</?\s*([A-Za-z][\w:.-]*)", html)
    tag_name = tag_match.group(1).lower() if tag_match else ""
    for match in _HTML_ATTRIBUTE_RE.finditer(html):
        value_group = next(
            group
            for group in ("double", "single", "bare")
            if match.group(group) is not None
        )
        kind = (
            "image"
            if tag_name == "img" and match.group("name").lower() == "src"
            else "html"
        )
        _record_span(
            state,
            marker_start + match.start(value_group),
            marker_start + match.end(value_group),
            kind,
        )
    return matched


def _trim_bare_url_end(source: str, start: int, end: int) -> int:
    """Exclude prose punctuation while retaining balanced URL delimiters."""

    while end > start and source[end - 1] in _TRAILING_URL_PUNCTUATION:
        end -= 1

    delimiter_pairs = {")": "(", "]": "[", "}": "{"}
    while end > start and source[end - 1] in delimiter_pairs:
        closing = source[end - 1]
        opening = delimiter_pairs[closing]
        candidate = source[start:end]
        if candidate.count(closing) <= candidate.count(opening):
            break
        end -= 1

    return end


def _capture_bare_url_destination(state: StateInline, silent: bool) -> bool:
    """Tokenize an HTTP(S) URL that appears as plain Markdown text."""

    start = state.pos
    source = state.src
    lowered = source[start:].lower()
    prefix = next(
        (
            candidate
            for candidate in _BARE_URL_PREFIXES
            if lowered.startswith(candidate)
        ),
        None,
    )
    if prefix is None:
        return False

    result = state.md.helpers.parseLinkDestination(source, start, state.posMax)
    if not result.ok:
        return False

    end = _trim_bare_url_end(source, start, result.pos)
    if end <= start + len(prefix):
        return False

    if not silent:
        _record_span(state, start, end, "bare_url")
        state.pending += source[start:end]
    state.pos = end
    return True


def _build_destination_parser() -> MarkdownIt:
    parser = MarkdownIt("commonmark")
    parser.inline.ruler.before(
        "text", "bare_url_destination", _capture_bare_url_destination
    )
    parser.inline.add_terminator_char("h")
    parser.inline.add_terminator_char("H")
    parser.inline.ruler.at("link", _capture_link_destination)
    parser.inline.ruler.at("image", _capture_image_destination)
    parser.inline.ruler.at("autolink", _capture_autolink_destination)
    parser.inline.ruler.at("html_inline", _capture_html_destinations)
    return parser


_DESTINATION_PARSER = _build_destination_parser()
_DEFINITION_PARSER = MarkdownIt("commonmark", {"inline_definitions": True})


def _line_offsets(document: str) -> list[int]:
    offsets = [0]
    for line in document.splitlines(keepends=True):
        offsets.append(offsets[-1] + len(line))
    return offsets


def _is_unescaped(text: str, position: int) -> bool:
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return backslashes % 2 == 0


def _reference_destination_spans(document: str) -> list[_DestinationSpan]:
    """Locate reference-definition URLs using markdown-it's parsed line maps."""

    offsets = _line_offsets(document)
    spans: list[_DestinationSpan] = []

    for token in _DEFINITION_PARSER.parse(document):
        if token.type != "definition" or token.map is None:
            continue

        expected_url = str(token.meta.get("url", ""))
        if not expected_url:
            continue

        region_start = offsets[token.map[0]]
        region_end = offsets[token.map[1]]
        search_position = region_start

        while True:
            label_end = document.find("]:", search_position, region_end)
            if label_end < 0:
                break
            search_position = label_end + 2
            if not _is_unescaped(document, label_end):
                continue

            destination_start = search_position
            while destination_start < region_end:
                char = document[destination_start]
                if not isStrSpace(char) and char != "\n":
                    break
                destination_start += 1

            result = _DEFINITION_PARSER.helpers.parseLinkDestination(
                document, destination_start, region_end
            )
            if not result.ok:
                continue
            if _DEFINITION_PARSER.normalizeLink(result.str) != expected_url:
                continue

            start = destination_start
            end = result.pos
            if document[start] == "<":
                start += 1
                end -= 1
            spans.append(_DestinationSpan(start, end, "reference"))
            break

    return spans


def _link_destination_spans(document: str) -> list[_DestinationSpan]:
    parse_document = mask_markdown_code(document)
    env: dict[str, list[_DestinationSpan]] = {_DESTINATION_SPANS_ENV_KEY: []}
    tokens: list[Token] = []
    _DESTINATION_PARSER.inline.parse(parse_document, _DESTINATION_PARSER, env, tokens)
    spans = env[_DESTINATION_SPANS_ENV_KEY] + _reference_destination_spans(
        parse_document
    )
    unique_spans = {(span.start, span.end): span for span in spans}
    return sorted(unique_spans.values())


def markdown_image_destination_spans(document: str) -> list[tuple[int, int]]:
    """Return exact source spans for Markdown and HTML image destinations."""

    return [
        (span.start, span.end)
        for span in _link_destination_spans(document)
        if span.kind == "image"
    ]


@dataclass(frozen=True)
class MarkdownLinkDestination:
    start: int
    end: int
    destination: str
    kind: str


def markdown_link_destinations(document: str) -> list[MarkdownLinkDestination]:
    """Return parsed link destinations outside Markdown code spans."""

    return [
        MarkdownLinkDestination(
            start=span.start,
            end=span.end,
            destination=document[span.start : span.end],
            kind=span.kind,
        )
        for span in _link_destination_spans(document)
    ]


def rewrite_markdown_link_destinations(document: str, rewriter) -> str:
    """Rewrite parsed destinations without touching labels, prose, or code."""

    replacements: list[tuple[int, int, str]] = []
    for link in markdown_link_destinations(document):
        replacement = rewriter(link)
        if replacement is not None and replacement != link.destination:
            replacements.append((link.start, link.end, replacement))

    for start, end, replacement in reversed(replacements):
        document = document[:start] + replacement + document[end:]
    return document


def replace_markdown_link_destinations(document: str) -> tuple[str, dict[str, str]]:
    """Replace parsed Markdown destinations and URLs with placeholders."""

    placeholder_map: dict[str, str] = {}
    replacements: list[tuple[int, int, str]] = []
    marker_index = 0

    for span in _link_destination_spans(document):
        start, end = span.start, span.end
        placeholder = f"@@LINK_DESTINATION_{marker_index}@@"
        while placeholder in document or placeholder in placeholder_map:
            marker_index += 1
            placeholder = f"@@LINK_DESTINATION_{marker_index}@@"

        placeholder_map[placeholder] = document[start:end]
        replacements.append((start, end, placeholder))
        marker_index += 1

    protected_document = document
    for start, end, placeholder in reversed(replacements):
        protected_document = (
            protected_document[:start] + placeholder + protected_document[end:]
        )

    return protected_document, placeholder_map


def restore_markdown_link_destinations(
    translated_document: str, placeholder_map: dict[str, str]
) -> str:
    """Restore original Markdown link destinations from placeholders."""

    for placeholder, destination in placeholder_map.items():
        count = translated_document.count(placeholder)
        if count != 1:
            raise ValueError(
                f"Expected link placeholder {placeholder!r} exactly once, found {count}."
            )
        translated_document = translated_document.replace(placeholder, destination, 1)
    return translated_document
