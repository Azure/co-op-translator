from __future__ import annotations

from co_op_translator.optional_dependencies import raise_for_optional_dependency


def main(argv: list[str] | None = None) -> None:
    try:
        from co_op_translator.mcp.server import main as server_main
    except ImportError as exc:
        raise_for_optional_dependency(
            feature="The MCP server",
            extra="mcp",
            exc=exc,
        )

    server_main(argv)
