# Choose How You Wan Work

Co-op Translator fit dey used three ways: the CLI, the Python API, and the MCP server. Dem get the same translation abilities, but each one dey fit different workflow.

Use dis page when you dey decide where to start.

## Quick Decision

| If you want to... | Use | Start here |
| --- | --- | --- |
| Translate or review a repository from a terminal | CLI | [CLI Reference](cli.md) |
| Add translation to a Python script, service, notebook, or CI job | Python API | [Python API](api.md) |
| Let an agent, editor, or MCP-compatible client translate content for you | MCP Server | [MCP Server](mcp.md) |
| Translate one Markdown document, notebook, or image that your app already loaded | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Translate an entire repository with standard output folders and metadata | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Use the CLI when

Choose the CLI when person or CI job dey drive repository translation from shell.

The CLI na the most direct way when you wan make Co-op Translator discover project files, create translated outputs, preserve the project layout, update metadata, and run review commands.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Good fits:

- You dey translate repository from your terminal.
- You want repeatable command for CI or release workflows.
- You want built-in project discovery, output paths, metadata, cleanup, and review.
- You prefer command interface pass to dey write Python code.

## Use the Python API when

Choose the Python API when your own code suppose control the workflow.

The API useful for apps, automation scripts, notebooks, services, and custom pipelines. E allow you call low-level content translation APIs for individual files, or run the same repository-level orchestration wey the CLI dey use.

Translate one Markdown document and decide where to save am:

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

- Your application don already sabi read files, buffers, notebooks, or image bytes.
- You need custom validation, storage, logging, retries, or approval flows.
- You want translate one document, notebook, or image without to process whole repository.
- You want repository translation, but from Python automation instead of shell command.

## Use the MCP Server when

Choose the MCP server when agent, editor, or MCP-compatible client go dey call Co-op Translator tools.

Normally for local setup, user no dey manually keep server running. MCP client go start `co-op-translator-mcp` over `stdio` when e need the tools.

Example user requests wey agent fit handle:

- "Translate this Markdown file to Korean and keep the links correct."
- "Translate this Markdown file to Korean with the agent-assisted MCP workflow, using your own model for the translated chunks."
- "Translate this notebook to Korean, preserve code cells, and use Co-op Translator MCP to reconstruct the notebook."
- "Translate the text in this image to Japanese and save the result."
- "Dry-run a repository translation to Spanish and tell me wetin go change."
- "Review whether the Korean translation output dey up to date."

For Markdown and notebooks, MCP fit work for two modes:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | The MCP host agent suppose translate chunks with im own model, without Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator suppose call Azure OpenAI or OpenAI directly. | `translate_markdown_content`, `translate_notebook_content` |

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

Repository translation na dry-run by default through MCP:

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

- You want natural-language translation workflows inside agent or editor.
- You want Markdown or notebook translation where host agent model go translate prepared chunks.
- You want the agent to translate selected content instead of whole repository.
- You want approval step before repository-wide writes.
- You want one interface wey dey expose Markdown, notebook, image, review, and path-rewriting tools.

## How They Fit Together

CLI na best default for humans wey dey translate repositories. Python API best when your code dey manage the workflow. MCP server best when agent or editor dey manage the workflow.

All three ways dey use the same public Co-op Translator API, so you fit start with the CLI, automate with Python later, and expose the same capabilities to MCP clients when you need agent-driven workflows.