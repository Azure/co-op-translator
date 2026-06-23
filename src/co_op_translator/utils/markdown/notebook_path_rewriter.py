"""Path rewriting for markdown cells inside Jupyter notebooks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from co_op_translator.utils.markdown.notebook_cells import (
    get_cell_source_text,
    iter_markdown_cells,
    set_cell_source_text,
)
from co_op_translator.utils.markdown.path_rewriter import (
    MarkdownPathRewritePolicy,
    rewrite_markdown_paths,
)


def _coerce_policy(
    policy: MarkdownPathRewritePolicy | Mapping[str, Any],
) -> MarkdownPathRewritePolicy:
    if isinstance(policy, MarkdownPathRewritePolicy):
        return policy
    return MarkdownPathRewritePolicy(**dict(policy))


def rewrite_notebook_paths(
    content: str,
    source_path: str | Path,
    target_path: str | Path,
    policy: MarkdownPathRewritePolicy | Mapping[str, Any],
) -> str:
    """Rewrite project paths in markdown cells for a translated notebook target."""

    resolved_policy = _coerce_policy(policy)
    notebook = json.loads(content)

    for cell in iter_markdown_cells(notebook):
        markdown_content = get_cell_source_text(cell)
        if not markdown_content.strip():
            continue

        rewritten_content = rewrite_markdown_paths(
            markdown_content,
            source_path=source_path,
            target_path=target_path,
            policy=resolved_policy,
        )
        set_cell_source_text(cell, rewritten_content)

    return json.dumps(notebook, ensure_ascii=False, indent=1)
