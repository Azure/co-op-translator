# MCP Server

Co-op Translator includes a Model Context Protocol server for agents, editors, and local automation that need translation tools without shelling out to the CLI for every operation.

Use the MCP server when an MCP client should call Co-op Translator directly:

| Scenario | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

The MCP server uses the same public Python API documented in [Python API](api.md). It does not reimplement translation logic.

## Start the Server

Install Co-op Translator, configure your environment variables, then run:

```bash
co-op-translator-mcp
```

The default transport is `stdio`, which is the usual choice for local MCP clients.

You can run the server from a source checkout without installing the script:

```bash
python -m co_op_translator.mcp.server
```

Explicit transport selection is also available:

```bash
co-op-translator-mcp --transport stdio
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

## Client Configuration

For a local MCP client that supports stdio servers, configure Co-op Translator with the installed command:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

When working directly from a repository checkout, point the client at Python instead:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "python",
      "args": ["-m", "co_op_translator.mcp.server"]
    }
  }
}
```

## Workflow 1: Translate Individual Files or Documents

Use content tools when the MCP client already has the document content or a path to one image.

For Markdown:

1. Call `translate_markdown_content` with `document`, `language_code`, and optionally `source_path`.
2. If the translated result will be written into a Co-op Translator output layout, call `rewrite_markdown_paths`.
3. Let the client write the returned `content` wherever the user wants it.

For notebooks:

1. Call `translate_notebook_content` with notebook JSON and `language_code`.
2. Call `rewrite_notebook_paths` if translated notebook links need to be adjusted for a target path.
3. Write the returned notebook JSON.

For images:

1. Call `translate_image_content` with `image_path`, `language_code`, and optional `root_dir` or `fast_mode`.
2. Read the returned `data_base64` and `mime_type`.
3. If `output_path` is provided, the translated image is also saved to that path.

The content tools do not perform project discovery, metadata updates, disclaimers, or automatic path rewriting.

## Workflow 2: Translate an Entire Repository

Use `run_translation` when the user wants Co-op Translator to behave like the `translate` CLI.

The MCP tool defaults to `dry_run=true` so an agent can inspect the scope before making file changes:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

To allow writes, the caller must set both `dry_run=false` and `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` is exposed as a compatibility alias for `run_translation`.

## Workflow 3: Review Translated Output

Use `run_review` for deterministic checks that do not require LLM or Vision credentials:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

The result includes captured text output and a structured review summary when available.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Safety Notes

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
