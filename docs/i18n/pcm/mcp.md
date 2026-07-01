# MCP Server

Co-op Translator get one Model Context Protocol server wey agents, editors, and MCP-compatible clients fit use.

For the default local setup, users no dey run separate server by hand. Dem configure dia MCP client, and the client go start `co-op-translator-mcp` automatically over `stdio` when e need Co-op Translator tools.

If you dey decide between CLI, Python API, and MCP, start wit [Choose Your Workflow](workflows.md).

Use MCP when an agent or editor suppose call Co-op Translator direct:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

The MCP server wrap the same public Python API wey dem document for [Python API](api.md). Provider-backed tools dey use the same configured providers as the CLI and Python API. Agent-assisted tools dey prepare chunks for the MCP host agent to translate, then dem use Co-op Translator to reconstruct the final Markdown or notebook.

## Step 1: Install and Configure Co-op Translator

Install Co-op Translator for the Python environment wey your MCP client go use:

```bash
pip install co-op-translator
```

For local development from this repository, install the package in editable mode:

```bash
pip install -e .
```

Choose the translation mode wey your MCP client go use:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator go call `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation need Azure OpenAI or OpenAI. Image translation sef need Azure AI Vision. |
| Agent-assisted | The MCP host agent go translate chunks wey `start_markdown_agent_translation` or `start_notebook_agent_translation` return. | No Co-op Translator LLM provider credentials required for Markdown or notebook chunks. Image translation no dey cover by agent-assisted mode yet. |

If you dey start with Markdown or notebook translation inside agent like Codex or Claude Code, start with agent-assisted mode. Use provider-backed mode when you want Co-op Translator make e call your configured providers, when you dey translate images, or when you dey run repository-level translation like the CLI.

Configure provider credentials only for provider-backed workflows:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed image translation still need:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode right now dey cover Markdown and notebook Markdown cells. Image translation still dey use the provider-backed image pipeline and e need Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

For the normal local `stdio` setup, add Co-op Translator to your MCP client configuration. The client go start and stop the process automatically.

Installed package configuration:

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

Source checkout configuration on Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Source checkout configuration on macOS or Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

After you change MCP client configuration, restart or reload the client so e fit discover the new server.

## Step 3: Verify the Server in the Client

Ask the MCP client to list available tools, or call one of the read-only helpers first:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Useful first checks:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirm say the server dey reachable and show available workflows. |
| `list_supported_languages` | Confirm say packaged language data fit load. |
| `get_configuration_status` | Confirm LLM and Vision provider dey available without exposing secret values. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Use provider-backed content tools when the MCP client don already get document content or image path and you want Co-op Translator to call the configured translation providers.

For Markdown:

1. Call `translate_markdown_content` with `document`, `language_code`, and optionally `source_path`.
2. If the translated result go write into a Co-op Translator output layout, call `rewrite_markdown_paths`.
3. Make the client write or return the final `content`.

For notebooks:

1. Call `translate_notebook_content` with notebook JSON and `language_code`.
2. Call `rewrite_notebook_paths` if translated notebook links need adjust for a target path.
3. Write or return the final notebook JSON.

For images:

1. Call `translate_image_content` with `image_path`, `language_code`, and optional `root_dir` or `fast_mode`.
2. Read the returned `data_base64` and `mime_type`.
3. If `output_path` dey provided, the translated image go still save to that path.

The content tools no dey do project discovery, metadata updates, disclaimers, or automatic path rewriting. If you want the host agent to translate Markdown or notebook chunks without Co-op Translator LLM provider credentials, use the agent-assisted workflow wey dey below.

### Translate with the Host Agent Model

Use agent-assisted tools when you want the MCP host agent, like coding assistant, make e produce the translated text instead of you configuring Azure OpenAI or OpenAI for Co-op Translator.

For chat-based MCP client, normally you no need to write tool JSON yourself. Ask the agent to use the agent-assisted workflow:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

For notebooks, use the same pattern:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

If your MCP client support server prompts, use `agent_assisted_markdown_translation_prompt` to make the client load the same workflow instructions.

For Markdown:

1. Call `start_markdown_agent_translation` with `document`, `language_code`, and optionally `source_path`.
2. Translate each returned chunk for the host agent by following the chunk `prompt`.
3. Call `finish_markdown_agent_translation` with the original `job` and translated chunks using `chunk_id` and `translated_text`.
4. If the content go write to a translated target path, call `rewrite_markdown_paths`.

For notebooks:

1. Call `start_notebook_agent_translation` with notebook JSON and `language_code`.
2. Translate each returned chunk for the host agent.
3. Call `finish_notebook_agent_translation` with the original `job` and translated chunks.
4. Call `rewrite_notebook_paths` if translated notebook links need target-path adjustment.

Agent-assisted tools no dey call Azure OpenAI or OpenAI from Co-op Translator. The host agent responsible to translate the returned chunks. Co-op Translator dey handle Markdown chunking, placeholder preservation, frontmatter reconstruction, notebook cell replacement, and post-translation normalization.

### Translate an Entire Repository

Use `run_translation` when the user want Co-op Translator behave like the `translate` CLI.

Repository translation by default dey `dry_run=true` so agent fit inspect scope before file changes:

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

`translate_project` dey exposed as compatibility alias for `run_translation`.

### Review Translated Output

Use `run_review` for deterministic checks wey no need LLM or Vision credentials:

!!! note "Beta"
    MCP dey expose the beta `run_review` API. E safe for read-only review workflows, but review checks and issue schemas fit still change.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

The result dey include captured text output and structured review summary when e available.

## Manual Server Runs

Manual runs usually na for debugging or for transports wey behave like long-running servers.

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

Run a long-lived HTTP or SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

For local editor and agent integrations, prefer the client-managed `stdio` configuration wey dey Step 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
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
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Copy-Paste Examples

Translate Markdown content:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Rewrite translated Markdown links:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Translate Markdown with the host agent model:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider dey available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent go translate the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables don set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- MCP tool calls dey model-controlled by the host application, so repository translation na dry-run by default.
- Full repository translation fit create, update, or remove plenti files. Make sure you get explicit user approval before you set `confirm_write=true`.
- The configuration status tool no go ever return API keys, endpoints, or other secret values.
- Image translation go return base64 image data. Big images fit produce large tool responses.
- Agent-assisted tools go return source chunks and prompts to the MCP host. Use dem only with content wey the user comfortable to send to that host agent model.