from dataclasses import dataclass
import logging
import re
from typing import Awaitable, Callable, Dict, List, Tuple

from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER

logger = logging.getLogger(__name__)

RunPromptFunc = Callable[[str, int | str, int], Awaitable[str]]


@dataclass(frozen=True)
class MermaidSlot:
    """A human-readable Mermaid span that can be translated in place."""

    line_index: int
    start: int
    end: int
    original: str


async def translate_comments_in_code_blocks(
    placeholder_map: Dict[str, str],
    language_code: str,
    language_name: str,
    is_rtl: bool,
    run_prompt: RunPromptFunc,
) -> Dict[str, str]:
    """Translate comments (and Mermaid labels) inside fenced code blocks.

    This function operates on the placeholder map returned by ``replace_code_blocks``.
    For each fenced code block, it will:

    - Detect the language hint from the fence (e.g. ```python, ```js, ```mermaid)
    - For regular code languages, translate only the comment text (# or // comments)
      using a COMMENT_n aggregation prompt
    - For Mermaid diagrams, translate human-readable labels and comments while
      preserving Mermaid syntax and structure

    Args:
        placeholder_map: Mapping from placeholder token to original fenced block text
        language_code: Target language code (e.g. "ko", "es")
        language_name: Human-readable language name (e.g. "Korean", "Spanish")
        is_rtl: Whether the target language is right-to-left
        run_prompt: Async callback that executes a prompt against the LLM

    Returns:
        A new placeholder map where each code block has translated comments/labels
        where applicable.
    """
    updated_map: Dict[str, str] = {}

    for placeholder, code_block in placeholder_map.items():
        try:
            translated_block = await _translate_single_code_block(
                code_block,
                language_code,
                language_name,
                is_rtl,
                run_prompt,
            )
        except Exception as e:  # pragma: no cover - defensive logging
            logger.error(
                "Failed to translate comments in code block for %s: %s",
                placeholder,
                e,
            )
            translated_block = code_block
        updated_map[placeholder] = translated_block

    return updated_map


async def _translate_single_code_block(
    code_block: str,
    language_code: str,
    language_name: str,
    is_rtl: bool,
    run_prompt: RunPromptFunc,
) -> str:
    lines = code_block.splitlines(keepends=True)
    if len(lines) < 2:
        return code_block

    first_line = lines[0]
    stripped = first_line.lstrip()
    if not (stripped.startswith("```") or stripped.startswith("~~~")):
        return code_block

    language_hint = _extract_language_from_fence(first_line)

    # Special handling for Mermaid diagrams: translate diagram text, not as code
    if language_hint == "mermaid":
        try:
            return await _translate_mermaid_block(
                code_block,
                language_code,
                language_name,
                is_rtl,
                run_prompt,
            )
        except Exception as e:  # pragma: no cover - defensive logging
            logger.error("Failed to translate Mermaid code block comments: %s", e)
            return code_block

    comment_style = _get_comment_style_for_language(language_hint)
    if comment_style is None:
        return code_block

    comments: List[str] = []
    slots: List[Tuple[int, str, str]] = []  # (line_index, prefix, line_ending)

    for idx in range(1, len(lines)):
        line = lines[idx]
        prefix, comment_text, line_ending = _extract_comment_from_line(
            line, comment_style
        )
        if comment_text is None:
            continue
        comments.append(comment_text)
        slots.append((idx, prefix, line_ending))

    if not comments:
        return code_block

    translated_comments = await _translate_comment_texts(
        comments,
        language_code,
        language_name,
        is_rtl,
        run_prompt,
    )

    if len(translated_comments) != len(slots):
        return code_block

    new_lines = list(lines)
    for i, (line_index, prefix, line_ending) in enumerate(slots):
        new_comment = translated_comments[i].strip()
        if not new_comment:
            new_comment = comments[i]
        new_lines[line_index] = prefix + new_comment + line_ending

    return "".join(new_lines)


async def _translate_mermaid_block(
    code_block: str,
    language_code: str,
    language_name: str,
    is_rtl: bool,
    run_prompt: RunPromptFunc,
) -> str:
    """Translate human-readable text inside a Mermaid fenced code block.

    Preserves Mermaid syntax and structure (graph keywords, node IDs, arrows,
    style/class definitions) while translating only labels and comments. The
    block structure is never sent for rewriting; only extracted text slots are
    translated and then injected back into the original lines.
    """
    lines = code_block.splitlines(keepends=True)
    slots = _extract_mermaid_slots(lines)
    if not slots:
        return code_block

    translated_slots = await _translate_mermaid_slot_texts(
        [slot.original for slot in slots],
        language_code,
        language_name,
        is_rtl,
        run_prompt,
    )

    if len(translated_slots) != len(slots):
        return code_block

    new_lines = list(lines)
    slots_by_line: Dict[int, List[Tuple[int, MermaidSlot]]] = {}
    for slot_index, slot in enumerate(slots):
        slots_by_line.setdefault(slot.line_index, []).append((slot_index, slot))

    for line_index, line_slots in slots_by_line.items():
        line_content, line_ending = _split_line_ending(new_lines[line_index])
        for slot_index, slot in sorted(
            line_slots, key=lambda item: item[1].start, reverse=True
        ):
            translated_text = _sanitize_slot_translation(
                translated_slots[slot_index], slot.original
            )
            line_content = (
                line_content[: slot.start] + translated_text + line_content[slot.end :]
            )
        new_lines[line_index] = line_content + line_ending

    return "".join(new_lines)


def _extract_mermaid_slots(lines: List[str]) -> List[MermaidSlot]:
    slots: List[MermaidSlot] = []
    if len(lines) < 3:
        return slots

    for line_index in range(1, len(lines) - 1):
        line_content, _ = _split_line_ending(lines[line_index])
        for start, end in _extract_mermaid_line_spans(line_content):
            text = line_content[start:end]
            if _should_translate_mermaid_text(text):
                slots.append(MermaidSlot(line_index, start, end, text))

    return slots


def _extract_mermaid_line_spans(line: str) -> List[Tuple[int, int]]:
    stripped = line.strip()
    if not stripped:
        return []

    if stripped.startswith(("%%{", "style ", "classDef ", "class ", "click ")):
        return []
    if stripped.startswith(("linkStyle ", "accTitle:", "accDescr:")):
        return []
    if stripped in {"end"}:
        return []

    spans: List[Tuple[int, int]] = []

    if stripped.startswith("%%"):
        comment_start = line.find("%%") + 2
        while comment_start < len(line) and line[comment_start].isspace():
            comment_start += 1
        _append_mermaid_span(spans, comment_start, len(line))
        return spans

    participant_match = re.match(
        r"^(\s*(?:participant|actor)\s+\S+\s+as\s+)(.+)$",
        line,
        flags=re.IGNORECASE,
    )
    if participant_match:
        _append_mermaid_span(
            spans,
            participant_match.start(2),
            participant_match.end(2),
        )
        return spans

    note_match = re.match(
        r"^(\s*note\s+(?:over|right of|left of)\s+[^:]+:\s*)(.+)$",
        line,
        flags=re.IGNORECASE,
    )
    if note_match:
        _append_mermaid_span(spans, note_match.start(2), note_match.end(2))
        return spans

    control_match = re.match(
        r"^(\s*(?:alt|else|opt|loop|par|and|critical|break)\s+)(.+)$",
        line,
        flags=re.IGNORECASE,
    )
    if control_match:
        _append_mermaid_span(spans, control_match.start(2), control_match.end(2))
        return spans

    subgraph_match = re.match(r"^(\s*subgraph\s+)(.+)$", line, flags=re.IGNORECASE)
    if subgraph_match and "[" not in subgraph_match.group(2):
        _append_mermaid_span(spans, subgraph_match.start(2), subgraph_match.end(2))
        return spans

    if _looks_like_mermaid_message(line):
        message_match = re.search(r":\s*(.+?)\s*;?\s*$", line)
        if message_match:
            _append_mermaid_span(spans, message_match.start(1), message_match.end(1))
            return spans

    for pattern in (
        r"\|([^|\r\n]+)\|",
        r"\[([^\]\r\n]+)\]",
        r"\{([^}\r\n]+)\}",
        r'"([^"\r\n]+)"',
    ):
        for match in re.finditer(pattern, line):
            _append_mermaid_span(spans, match.start(1), match.end(1))

    return spans


def _append_mermaid_span(spans: List[Tuple[int, int]], start: int, end: int) -> None:
    if start >= end:
        return
    for existing_start, existing_end in spans:
        if start < existing_end and end > existing_start:
            return
    spans.append((start, end))


def _looks_like_mermaid_message(line: str) -> bool:
    return bool(re.search(r"(?:-{1,2}|=|x)?>>?|--\)|-\)|==", line))


def _should_translate_mermaid_text(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if stripped.startswith(("http://", "https://", "/", "./", "../")):
        return False
    if stripped.startswith("@@") and stripped.endswith("@@"):
        return False
    return True


async def _translate_mermaid_slot_texts(
    slot_texts: List[str],
    language_code: str,
    language_name: str,
    is_rtl: bool,
    run_prompt: RunPromptFunc,
) -> List[str]:
    instruction = (
        f"Translate the following Mermaid label/comment text to {language_name} ({language_code}).\n"
        "Each line is in the form 'MERMAID_SLOT_n: <text>'.\n"
        "Translate only the text after the colon into the target language.\n"
        "Keep the 'MERMAID_SLOT_n:' prefix exactly the same and in English.\n"
        "Return the same number of slots, with the same MERMAID_SLOT_n numbers.\n"
        "Do not add, remove, or reorder slots.\n"
        "Preserve URLs, file paths, inline HTML tags such as <br/>, and markdown/code tokens exactly.\n"
        "Do not add any explanations or extra text.\n"
    )

    if is_rtl:
        instruction += "Write the translated labels and comments from right to left if appropriate for the language.\n"
    else:
        instruction += "Write the translated labels and comments from left to right.\n"

    user_lines = [
        f"MERMAID_SLOT_{idx}: {text}" for idx, text in enumerate(slot_texts, start=1)
    ]
    prompt = instruction + SPLIT_DELIMITER + "\n".join(user_lines)

    translated = await run_prompt(prompt, "mermaid_slots", 1)
    if not translated:
        return slot_texts

    return _parse_numbered_slot_response(translated, "MERMAID_SLOT", slot_texts)


def _parse_numbered_slot_response(
    translated: str, prefix: str, originals: List[str]
) -> List[str]:
    marker_pattern = re.compile(rf"\b{re.escape(prefix)}_(\d+):\s*")
    matches = list(marker_pattern.finditer(translated))
    if not matches:
        return originals

    mapping: Dict[int, str] = {}
    for match_index, match in enumerate(matches):
        slot_index = int(match.group(1))
        text_start = match.end()
        text_end = (
            matches[match_index + 1].start()
            if match_index + 1 < len(matches)
            else len(translated)
        )
        mapping[slot_index] = translated[text_start:text_end].strip()

    return [mapping.get(idx, original) for idx, original in enumerate(originals, 1)]


def _sanitize_slot_translation(translated: str, fallback: str) -> str:
    sanitized = re.sub(r"[ \t]*(?:\r\n|\r|\n)[ \t]*", " ", translated).strip()
    if not sanitized or "MERMAID_SLOT_" in sanitized:
        return fallback
    return sanitized


def _split_line_ending(line: str) -> Tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    if line.endswith("\r"):
        return line[:-1], "\r"
    return line, ""


def _normalize_mermaid_fence_boundaries(
    translated_block: str, original_block: str
) -> str:
    """Keep translated Mermaid fences parseable after LLM post-processing.

    LLMs sometimes preserve the fence markers but collapse the newline before or
    after the closing fence, producing invalid Markdown like ``end```Text``.
    Normalize only the fence boundaries; leave the diagram body untouched.
    """
    original_lines = original_block.splitlines(keepends=True)
    if not original_lines:
        return translated_block

    opening_line = original_lines[0]
    fence_match = re.match(r"^(\s*)(`{3,}|~{3,})", opening_line)
    if not fence_match:
        return translated_block

    fence_marker = fence_match.group(2)
    normalized = translated_block

    if not normalized.lstrip().startswith(fence_marker):
        inner = normalized.strip("\r\n")
        normalized = opening_line + inner
        if inner and not inner.endswith(("\n", "\r")):
            normalized += "\n"
        normalized += fence_marker

    escaped_marker = re.escape(fence_marker)
    normalized = re.sub(
        rf"([^\r\n])({escaped_marker})(?=\s*(?:\r?\n|$))",
        r"\1\n\2",
        normalized,
    )

    if original_block.endswith(("\r\n", "\n", "\r")) and not normalized.endswith(
        ("\r\n", "\n", "\r")
    ):
        normalized += "\n"

    return normalized


def _extract_language_from_fence(fence_line: str) -> str:
    stripped = fence_line.strip()
    if stripped.startswith("```"):
        rest = stripped.lstrip("`")
    elif stripped.startswith("~~~"):
        rest = stripped.lstrip("~")
    else:
        return ""

    parts = rest.split(None, 1)
    if not parts:
        return ""
    return parts[0].strip().lower()


def _get_comment_style_for_language(language_hint: str | None) -> str | None:
    if not language_hint:
        return None

    hash_langs = {
        "python",
        "py",
        "bash",
        "sh",
        "shell",
        "ps1",
        "powershell",
        "r",
        "ruby",
        "rb",
    }
    slash_slash_langs = {
        "javascript",
        "js",
        "typescript",
        "ts",
        "java",
        "c",
        "cpp",
        "c++",
        "c#",
        "cs",
        "go",
        "rust",
        "swift",
        "kotlin",
        "scala",
        "php",
    }

    if language_hint in hash_langs:
        return "hash"
    if language_hint in slash_slash_langs:
        return "slash"
    return None


def _extract_comment_from_line(
    line: str, comment_style: str
) -> Tuple[str, str | None, str]:
    if not line:
        return "", None, ""

    # Preserve original line ending
    line_ending = ""
    if line.endswith("\r\n"):
        core = line[:-2]
        line_ending = "\r\n"
    elif line.endswith("\n"):
        core = line[:-1]
        line_ending = "\n"
    elif line.endswith("\r"):
        core = line[:-1]
        line_ending = "\r"
    else:
        core = line

    comment_start = _find_comment_start(core, comment_style)
    if comment_start is None:
        return "", None, line_ending

    if comment_style == "hash":
        marker = "#"
    else:
        marker = "//"

    marker_end = comment_start + len(marker)
    after_marker = core[marker_end:]
    leading_ws_len = len(after_marker) - len(after_marker.lstrip())
    prefix = core[:marker_end] + after_marker[:leading_ws_len]
    comment_text = after_marker[leading_ws_len:]

    return prefix, comment_text, line_ending


def _find_comment_start(line: str, comment_style: str) -> int | None:
    in_single = False
    in_double = False
    in_backtick = False
    i = 0
    length = len(line)

    while i < length:
        ch = line[i]

        if ch == "'" and not in_double and not in_backtick:
            in_single = not in_single
            i += 1
            continue
        if ch == '"' and not in_single and not in_backtick:
            in_double = not in_double
            i += 1
            continue
        if ch == "`" and not in_single and not in_double:
            in_backtick = not in_backtick
            i += 1
            continue

        if in_single or in_double or in_backtick:
            i += 1
            continue

        if comment_style == "hash":
            if ch == "#":
                return i
            i += 1
            continue

        if comment_style == "slash":
            if ch == "/" and i + 1 < length and line[i + 1] == "/":
                return i
            i += 1
            continue

        i += 1

    return None


async def _translate_comment_texts(
    comments: List[str],
    language_code: str,
    language_name: str,
    is_rtl: bool,
    run_prompt: RunPromptFunc,
) -> List[str]:
    instruction = (
        f"Translate the following code comments to {language_name} ({language_code}).\n"
        "Each line is in the form 'COMMENT_n: <text>'.\n"
        "Translate only the text after the colon into the target language.\n"
        "Keep the 'COMMENT_n:' prefix exactly the same and in English.\n"
        "Return the same number of lines, with the same COMMENT_n numbers, one per line.\n"
        "Do not add, remove, or reorder lines.\n"
        "Do not add any explanations or extra text.\n"
    )

    if is_rtl:
        instruction += "Write the translated comments from right to left if appropriate for the language.\n"
    else:
        instruction += "Write the translated comments from left to right.\n"

    user_lines: List[str] = []
    for idx, text in enumerate(comments, start=1):
        user_lines.append(f"COMMENT_{idx}: {text}")

    prompt = instruction + SPLIT_DELIMITER + "\n".join(user_lines)

    translated = await run_prompt(prompt, "code_comments", 1)

    translated_lines = [
        line.strip() for line in translated.splitlines() if line.strip()
    ]

    mapping: Dict[int, str] = {}
    pattern = re.compile(r"^COMMENT_(\d+):\s*(.*)$")
    for line in translated_lines:
        match = pattern.match(line)
        if not match:
            continue
        index = int(match.group(1))
        text = match.group(2)
        mapping[index] = text

    results: List[str] = []
    for i, original in enumerate(comments, start=1):
        results.append(mapping.get(i, original))

    return results
