import logging
import re
from typing import Awaitable, Callable, Dict, List, Tuple

from co_op_translator.utils.llm.markdown_utils import SPLIT_DELIMITER

logger = logging.getLogger(__name__)

RunPromptFunc = Callable[[str, int | str, int], Awaitable[str]]


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
    style/class definitions) while translating only labels and comments.
    The entire fenced block is sent and expected back, so it can be restored
    via the placeholder map without additional processing.
    """
    instruction = (
        f"Translate the following Mermaid diagram code to {language_name} ({language_code}).\n"
        "Preserve all Mermaid syntax and structure exactly, including keywords (graph, subgraph, end), "
        "node IDs, arrows, style/class definitions, and URLs.\n"
        'Only translate human-readable text, such as labels in square brackets [Like this], text inside quotes "Like this", '
        "and comment text after %% markers.\n"
        "Do not change node IDs, arrow syntax, style declarations, or URLs/paths.\n"
        "Return only the translated Mermaid code block without any explanations or extra text.\n"
    )

    if is_rtl:
        instruction += "Write the translated labels from right to left if appropriate for the language.\n"
    else:
        instruction += "Write the translated labels from left to right.\n"

    prompt = instruction + SPLIT_DELIMITER + code_block

    translated = await run_prompt(prompt, "mermaid", 1)
    return translated or code_block


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
