from __future__ import annotations

from urllib.parse import ParseResult


def replace_url_path(parsed_url: ParseResult, path: str) -> str:
    """Replace only a parsed URL's path, preserving params, query, and fragment."""

    return parsed_url._replace(path=path).geturl()
