# Choose How You Wan Work

Co-op Translator fit dey used for three ways: the CLI, the Python API, and the MCP server. Dem share di same translation capabilities, but each one dey fit different workflow.

Use dis page when you dey decide where to start.

**If you edit translations by hand:** di default CLI and Actions workflows go retranslate changed source files full, so wetin you write for those files fit get overwritten. Read di diff before you accept any update. For Markdown block-level preservation of accepted edits, use di optional [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Quick Decision

| If you wan... | Use | Start here |
| --- | --- | --- |
| Translate or review a repository from a terminal | CLI | [CLI Reference](cli.md) |
| Add translation to a Python script, service, notebook, or CI job | Python API | [Python API](api.md) |
| Let an agent, editor, or MCP-compatible client translate content for you | MCP Server | [MCP Server](mcp.md) |
| Translate one Markdown document, notebook, or image that your app already loaded | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Translate an entire repository with standard output folders and metadata | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Use the CLI when

Choose di CLI when person or CI job dey run repository translation from a shell.

Di CLI na di most direct way when you wan make Co-op Translator find project files, create translated outputs, preserve di project layout, update metadata, and run review commands.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

This example translates Markdown and notebooks. Add `-img` only after configuring [Azure AI Vision](configuration.md#azure-ai-vision). For a Markdown-only first run, follow [Your first translation](first-translation.md).

When e fit well:

- You dey translate a repository from your terminal.
- You want command wey you fit run again for CI or release workflows.
- You want built-in project discovery, output paths, metadata, cleanup, and review.
- You prefer command interface instead of writing Python code.

## Use the Python API when

Choose di Python API when your own code suppose control di workflow.

Di API dey useful for applications, automation scripts, notebooks, services, and custom pipelines. E dey let you call low-level content translation APIs for individual files, or run di same repository-level orchestration wey di CLI dey use.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

When e fit well:

- Your application don already dey read files, buffers, notebooks, or image bytes.
- You need custom validation, storage, logging, retries, or approval flows.
- You want to translate one document, notebook, or image without processing whole repository.
- You want repository translation, but from Python automation instead of a shell command.

## Use the MCP Server when

Choose di MCP server when an agent, editor, or MCP-compatible client suppose call Co-op Translator tools.

For normal local setup, di user no go dey keep server dey run by hand. Di MCP client go start `co-op-translator-mcp` over `stdio` when e need di tools.

Example user requests we agent fit handle:

- "Translate dis Markdown file to Korean and make di links correct."
- "Translate dis Markdown file to Korean with di agent-assisted MCP workflow, using your own model for di translated chunks."
- "Translate dis notebook to Korean, keep di code cells, and use Co-op Translator MCP to reconstruct di notebook."
- "Translate di text for this image to Japanese and save di result."
- "Dry-run a repository translation to Spanish and tell me wetin go change."
- "Check whether di Korean translation output dey up to date."

For Markdown and notebooks, MCP fit work for two modes:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | Di MCP host agent suppose translate chunks with its own model, without Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator go call Azure OpenAI, OpenAI, or Anthropic directly. | `translate_markdown_content`, `translate_notebook_content` |

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

Repository translation dey dry-run by default through MCP:

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

When e fit well:

- You want natural-language translation workflows inside an agent or editor.
- You want Markdown or notebook translation where di host agent model translate prepared chunks.
- You want di agent to translate selected content instead of di whole repository.
- You want one approval step before repository-wide writes.
- You want one interface wey show Markdown, notebook, image, review, and path-rewriting tools.

## How Dem Dey Fit Together

Di CLI na di best default for humans wey dey translate repositories. Di Python API best when your code dey own di workflow. Di MCP server best when agent or editor dey own di workflow.

All three paths dey use di same public Co-op Translator API, so you fit start with di CLI, automate with Python later, and expose di same capabilities to MCP clients when you need agent-driven workflows.