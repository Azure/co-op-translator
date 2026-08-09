from __future__ import annotations

from markdown_it import MarkdownIt
from markdown_it.common.utils import isStrSpace
from markdown_it.rules_inline.image import image as parse_image
from markdown_it.rules_inline.link import link as parse_link
from markdown_it.rules_inline.state_inline import StateInline
from markdown_it.token import Token

_DESTINATION_SPANS_ENV_KEY = "co_op_translator_link_destination_spans"


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
    if not destination or destination.startswith("#"):
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
        state.env[_DESTINATION_SPANS_ENV_KEY].append(span)
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
        state.env[_DESTINATION_SPANS_ENV_KEY].append(span)
    return matched


def _build_destination_parser() -> MarkdownIt:
    parser = MarkdownIt("commonmark")
    parser.inline.ruler.at("link", _capture_link_destination)
    parser.inline.ruler.at("image", _capture_image_destination)
    return parser


_DESTINATION_PARSER = _build_destination_parser()


def _link_destination_spans(document: str) -> list[tuple[int, int]]:
    env: dict[str, list[tuple[int, int]]] = {_DESTINATION_SPANS_ENV_KEY: []}
    tokens: list[Token] = []
    _DESTINATION_PARSER.inline.parse(document, _DESTINATION_PARSER, env, tokens)
    return sorted(env[_DESTINATION_SPANS_ENV_KEY])


def replace_markdown_link_destinations(document: str) -> tuple[str, dict[str, str]]:
    """Replace non-anchor inline Markdown link destinations with placeholders."""

    placeholder_map: dict[str, str] = {}
    replacements: list[tuple[int, int, str]] = []
    marker_index = 0

    for start, end in _link_destination_spans(document):
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
        translated_document = translated_document.replace(placeholder, destination)
    return translated_document
