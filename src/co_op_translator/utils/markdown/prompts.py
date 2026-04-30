from __future__ import annotations

import logging
from importlib import resources

from co_op_translator.glossary import inject_markdown_glossary

from .constants import SPLIT_DELIMITER

logger = logging.getLogger(__name__)


def _read_language_prompt_template(language_code: str) -> str:
    """Read a language-specific prompt template from packaged templates.

    Looks for `co_op_translator/templates/language/<language_code>.md`.
    Returns an empty string if not found or unreadable.
    """

    normalized_code = language_code.lower().strip()
    template_name = f"{normalized_code}.md"

    try:
        template_file = (
            resources.files("co_op_translator.templates")
            .joinpath("language")
            .joinpath(template_name)
        )
        return template_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""
    except Exception:
        logger.warning(
            "Failed to read language prompt template '%s'", template_name, exc_info=True
        )
        return ""


def generate_prompt_template(
    language_code: str, language_name: str, document_chunk: str, is_rtl: bool
) -> str:
    """
    Generate a safe and stable translation prompt that enforces strict
    markdown structure preservation and prevents HTML/markdown rewriting.
    """

    # --- 1) ONE-LINE CHUNKS (simple text or inline cases) ---
    if len(document_chunk.split("\n")) == 1:
        prompt = (
            f"Translate the following text to {language_name} ({language_code}). "
            "STRICT RULE: Do NOT add, remove, or modify any markdown characters. "
            "Do NOT introduce HTML tags. Translate ONLY text content. "
            "Return ONLY the translation."
        )

    # --- 2) MULTI-LINE CHUNKS (markdown documents) ---
    else:
        prompt = f"""
Translate the following markdown file to {language_name} ({language_code}).

STRICT RULES (NO EXCEPTIONS):

0. STRUCTURE PRESERVATION
   - You MUST preserve the exact markdown syntax from the input.
   - DO NOT canonicalize, optimize, reformat, or rewrite markdown.
   - DO NOT convert markdown links ([text](url)) into HTML <a> tags.
   - DO NOT convert existing HTML into markdown.
   - DO NOT introduce any new HTML tags.

1. OUTPUT FORMAT
   - Return ONLY the translated content.
   - Do NOT add ```markdown or ANY wrappers.
   - Do NOT add explanations, metadata, or comments.

2. TRANSLATION SCOPE
   - Translate written, human-readable text ONLY.
   - DO NOT translate:
     * URLs or file paths
     * Markdown syntax
     * Variable names, function names, class names
     * Placeholders like @@INLINE_CODE_x@@ and @@CODE_BLOCK_x@@
     * Tags such as [!NOTE], [!TIP], [!WARNING], [!IMPORTANT], [!CAUTION]

3. HTML HANDLING RULES
   - Preserve all HTML EXACTLY as provided. This includes inline and block elements
     such as <a>, <img>, <details>, <summary>, <div>, and any other HTML tags.
   - DO NOT alter tag names, attributes, URLs, paths, classes, IDs, or structure.
   - Translate ONLY the visible human-readable text content (e.g., link text, alt/title text,
     <summary> labels, descriptive text inside tags).
   - DO NOT convert HTML to Markdown or Markdown to HTML.
   - DO NOT add, remove, reorder, or rewrite ANY HTML. Maintain exact byte-for-byte
     fidelity for all tags and attributes.

4. FRONTMATTER RULE (YAML delimited by '---')
   - If a YAML frontmatter block exists at the top of the document:
       * KEEP the entire block EXACTLY.
       * DO NOT modify field names or file paths.
       * Translate ONLY human-readable values (e.g., title, description).
       * DO NOT “fix” or normalize layout/import paths.

5. SAFETY
   - Do NOT reorder lines.
   - Do NOT remove blank lines.
   - Do NOT merge or split paragraphs.
   - Preserve whitespace, indentation, and list structure exactly.
"""

    # Direction rule (minimal + unambiguous)
    if is_rtl:
        prompt += "\nWrite the output in right-to-left direction.\n"
    else:
        prompt += "\nWrite the output in left-to-right direction.\n"

    language_template = _read_language_prompt_template(language_code)
    if language_template:
        prompt += f"\n{language_template}\n"

    # Explicit delimiter between system rules and user content
    prompt += SPLIT_DELIMITER
    prompt += document_chunk

    return inject_markdown_glossary(prompt, SPLIT_DELIMITER)
