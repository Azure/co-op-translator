"""MCP server integration for Co-op Translator."""

from typing import Any

__all__ = ["create_server"]


def __getattr__(name: str) -> Any:
    if name == "create_server":
        from co_op_translator.mcp.server import create_server

        return create_server
    raise AttributeError(name)
