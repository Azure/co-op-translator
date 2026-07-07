"""Console output helpers."""

from __future__ import annotations

import sys
from typing import TextIO


def _make_stream_encoding_safe(stream: TextIO | None) -> None:
    """Prevent UnicodeEncodeError on consoles with narrow legacy encodings."""
    if stream is None:
        return

    reconfigure = getattr(stream, "reconfigure", None)
    if not callable(reconfigure):
        return

    try:
        reconfigure(errors="replace")
    except (LookupError, TypeError, ValueError):
        return


def configure_safe_console_output() -> None:
    """Keep CLI output from crashing on Windows code pages like cp949."""
    _make_stream_encoding_safe(sys.stdout)
    _make_stream_encoding_safe(sys.stderr)
