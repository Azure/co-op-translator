"""Helpers for reading and updating markdown cells in Jupyter notebooks."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any


def iter_markdown_cells(notebook: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Yield markdown cells from a parsed notebook payload."""

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            yield cell


def get_cell_source_text(cell: dict[str, Any]) -> str:
    """Return a notebook cell source as a single string."""

    source = cell.get("source", [])
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def set_cell_source_text(cell: dict[str, Any], content: str) -> None:
    """Set a cell source while preserving the original source shape."""

    source = cell.get("source", [])
    if isinstance(source, list):
        translated_lines = content.splitlines(keepends=True)
        cell["source"] = [
            line if line.endswith("\n") else line + "\n" for line in translated_lines
        ]
    else:
        cell["source"] = content
