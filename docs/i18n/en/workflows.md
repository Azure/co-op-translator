# Choose Your Workflow

Co-op Translator can be used in three ways: the CLI, the Python API, and the MCP server. They share the same translation capabilities, but each one fits a different workflow.

Use this page when you are deciding where to start.

## Quick Decision

| If you want to... | Use | Start here |
| --- | --- | --- |
| Translate or review a repository from a terminal | CLI | [CLI Reference](cli.md) |
| Add translation to a Python script, service, notebook, or CI job | Python API | [Python API](api.md) |
| Let an agent, editor, or MCP-compatible client translate content for you | MCP Server | [MCP Server](mcp.md) |
| Translate one Markdown document, notebook, or image that your app already loaded | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Translate an entire repository with standard output folders and metadata | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Use the CLI when

Choose the CLI when a person or CI job is driving repository translation from a shell.

The CLI is the most direct path when you want Co-op Translator to discover project files, create translated outputs, preserve the project layout, update metadata, and run review commands.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Good fits:

- You are translating a repository from your terminal.
- You want a repeatable command for CI or release workflows.
- You want built-in project discovery, output paths, metadata, cleanup, and review.
- You prefer a command interface over writing Python code.

## Use the Python API when

Choose the Python API when your own code should control the workflow.

The API is useful for applications, automation scripts, notebooks, services, and custom pipelines. It lets you call low-level content translation APIs for individual files, or run the same repository-level orchestration used by the CLI.

Translate one Markdown document and decide where to save it:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Run a repository translation from Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Good fits:

- Your application already reads files, buffers, notebooks, or image bytes.
- You need custom validation, storage, logging, retries, or approval flows.
- You want to translate one document, notebook, or image without processing a whole repository.
- You want repository translation, but from Python automation instead of a shell command.

## Use the MCP Server when

Choose the MCP server when an agent, editor, or MCP-compatible client should call Co-op Translator tools.

In the normal local setup, the user does not manually keep a server running. The MCP client starts `co-op-translator-mcp` over `stdio` when it needs the tools.

Example user requests an agent could handle:

- "Translate this Markdown file to Korean and keep the links correct."
- "Translate this Markdown file to Korean with the agent-assisted MCP workflow, using your own model for the translated chunks."
- "Translate this notebook to Korean, preserve code cells, and use Co-op Translator MCP to reconstruct the notebook."
- "Translate the text in this image to Japanese and save the result."
- "Dry-run a repository translation to Spanish and tell me what would change."
- "Review whether the Korean translation output is up to date."

For Markdown and notebooks, MCP can work in two modes:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | The MCP host agent should translate chunks with its own model, without Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator should call Azure OpenAI or OpenAI directly. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP image tool call shape:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Repository translation is dry-run by default through MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Good fits:

- You want natural-language translation workflows inside an agent or editor.
- You want Markdown or notebook translation where the host agent model translates prepared chunks.
- You want the agent to translate selected content instead of an entire repository.
- You want an approval step before repository-wide writes.
- You want one interface that exposes Markdown, notebook, image, review, and path-rewriting tools.

## How They Fit Together

The CLI is the best default for humans translating repositories. The Python API is best when your code owns the workflow. The MCP server is best when an agent or editor owns the workflow.

All three paths use the same public Co-op Translator API, so you can start with the CLI, automate with Python later, and expose the same capabilities to MCP clients when you need agent-driven workflows.