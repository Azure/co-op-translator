"""MCP server integration for Co-op Translator."""

from typing import Any

from co_op_translator.optional_dependencies import raise_for_optional_dependency

__all__ = ["create_server"]


def __getattr__(name: str) -> Any:
    if name == "create_server":
        try:
            from co_op_translator.mcp.server import create_server
        except ImportError as exc:
            raise_for_optional_dependency(
                feature="The MCP server",
                extra="mcp",
                exc=exc,
            )

        return create_server
    raise AttributeError(name)
