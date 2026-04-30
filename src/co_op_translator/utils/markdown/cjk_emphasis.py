from __future__ import annotations

import re

from markdown_it import MarkdownIt

from co_op_translator.utils.common.lang_utils import normalize_language_code

CJK_CHAR_CLASS = r"\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uac00-\ud7af"
CJK_EMPHASIS_LANGUAGE_PREFIXES = ("ja", "ko", "zh")
_CJK_CHAR_RE = re.compile(rf"[{CJK_CHAR_CLASS}]")
_CJK_FULL_TEXT_RE = re.compile(rf"^[{CJK_CHAR_CLASS}]+$")

# Inner emphasis text must not contain '*' so a match cannot bleed into
# neighboring emphasis regions.
_EMPHASIS_INNER_TEXT_PATTERN = r"[^\n*]+?"


def _build_cjk_emphasis_pattern(delim: str) -> re.Pattern[str]:
    escaped = re.escape(delim)
    return re.compile(
        rf"(?<!\*){escaped}(?P<text>{_EMPHASIS_INNER_TEXT_PATTERN}){escaped}(?!\*)"
    )


_CJK_EMPHASIS_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (_build_cjk_emphasis_pattern("***"), "<strong><em>{text}</em></strong>"),
    (_build_cjk_emphasis_pattern("**"), "<strong>{text}</strong>"),
    (_build_cjk_emphasis_pattern("*"), "<em>{text}</em>"),
]


def _apply_cjk_emphasis_pattern(
    segment: str, pattern: re.Pattern[str], html_template: str
) -> str:
    def _replace(match: re.Match[str]) -> str:
        inner_text = match.group("text")
        if not inner_text:
            return match.group(0)

        source = match.string
        start, end = match.span()
        left_char = source[start - 1] if start > 0 else ""
        right_char = source[end] if end < len(source) else ""
        left_is_cjk = bool(_CJK_CHAR_RE.fullmatch(left_char))
        right_is_cjk = bool(_CJK_CHAR_RE.fullmatch(right_char))
        pure_cjk_inner = bool(_CJK_FULL_TEXT_RE.fullmatch(inner_text))

        if left_is_cjk or right_is_cjk or pure_cjk_inner:
            return html_template.format(text=inner_text)
        return match.group(0)

    return pattern.sub(_replace, segment)


def _collect_inline_code_spans_with_markdown_ast(content: str) -> list[tuple[int, int]]:
    """Collect absolute character ranges for inline code spans using Markdown AST context."""
    md = MarkdownIt("commonmark")
    tokens = md.parse(content)

    lines = content.splitlines(keepends=True)
    offsets = [0]
    for ln in lines:
        offsets.append(offsets[-1] + len(ln))

    inline_spans: list[tuple[int, int]] = []

    for tok in tokens:
        if tok.type != "inline" or not tok.map or not tok.children:
            continue

        if not any(child.type == "code_inline" for child in tok.children):
            continue

        start_line, end_line = tok.map
        seg_start = offsets[start_line]
        seg_end = offsets[end_line]
        segment = content[seg_start:seg_end]

        idx = 0
        while idx < len(segment):
            if segment[idx] != "`":
                idx += 1
                continue

            open_len = 1
            while idx + open_len < len(segment) and segment[idx + open_len] == "`":
                open_len += 1

            close_idx = idx + open_len
            while close_idx < len(segment):
                if segment[close_idx] != "`":
                    close_idx += 1
                    continue

                run_len = 1
                while (
                    close_idx + run_len < len(segment)
                    and segment[close_idx + run_len] == "`"
                ):
                    run_len += 1

                if run_len == open_len:
                    inline_spans.append(
                        (seg_start + idx, seg_start + close_idx + run_len)
                    )
                    idx = close_idx + run_len
                    break

                close_idx += run_len
            else:
                idx += open_len

    inline_spans.sort(key=lambda x: x[0])
    return inline_spans


def normalize_cjk_emphasis_markers(
    content: str,
    language_code: str | None = None,
    enabled_language_prefixes: tuple[str, ...] = CJK_EMPHASIS_LANGUAGE_PREFIXES,
) -> str:
    """Normalize emphasis markup around CJK text for renderer compatibility.

    Some Markdown renderers fail to apply `*`/`**` emphasis when delimiters are
    directly adjacent to CJK characters. To preserve visual intent without adding
    visible spaces, convert those cases into equivalent HTML tags.

    Args:
        content: Markdown text that may include emphasis markers near CJK chars.
        language_code: Optional translation target language code.
        enabled_language_prefixes: Language prefixes where normalization is enabled.

    Returns:
        Markdown text with CJK-adjacent emphasis markers converted to HTML tags.
    """

    if language_code:
        normalized_language = normalize_language_code(language_code).lower()
        if not any(
            normalized_language == prefix
            or normalized_language.startswith(f"{prefix}-")
            for prefix in enabled_language_prefixes
        ):
            return content

    if "*" not in content:
        return content

    def _normalize_text_segment(segment: str) -> str:
        for pattern, html_template in _CJK_EMPHASIS_PATTERNS:
            segment = _apply_cjk_emphasis_pattern(segment, pattern, html_template)
        return segment

    # Skip inline code spans so literal examples are never rewritten.
    # Use markdown-it AST to scope scanning to inline regions.
    output_parts: list[str] = []
    cursor = 0
    inline_code_spans = _collect_inline_code_spans_with_markdown_ast(content)

    for start, end in inline_code_spans:
        if start > cursor:
            output_parts.append(_normalize_text_segment(content[cursor:start]))
        output_parts.append(content[start:end])
        cursor = end

    if cursor < len(content):
        output_parts.append(_normalize_text_segment(content[cursor:]))

    return "".join(output_parts)
