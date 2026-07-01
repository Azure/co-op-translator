# Choose Your Workflow

Co-op Translator can be used in three ways: the CLI, the Python API, and the MCP server. They share the same translation capabilities, but each one fits a different workflow.

Use this page when you are deciding where to start.

## Quick Decision

| If you want to... | Use | Start here |
| --- | --- | --- |
| Oversæt eller gennemgå et repository fra en terminal | CLI | [CLI-reference](cli.md) |
| Tilføj oversættelse til et Python-script, en service, en notebook eller et CI-job | Python API | [Python API](api.md) |
| Lad en agent, editor eller en MCP-kompatibel klient oversætte indhold for dig | MCP Server | [MCP-server](mcp.md) |
| Oversæt ét Markdown-dokument, en notebook eller et billede, som din app allerede har indlæst | Python API or MCP Server | [Python API](api.md) or [MCP-server](mcp.md) |
| Oversæt et helt repository med standard output-mapper og metadata | CLI or `run_translation` | [CLI-reference](cli.md) or [Python API](api.md) |

## Use the CLI when

Choose the CLI when a person or CI job is driving repository translation from a shell.

The CLI is the most direct path when you want Co-op Translator to discover project files, create translated outputs, preserve the project layout, update metadata, and run review commands.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Passer godt til:

- Du oversætter et repository fra din terminal.
- Du ønsker en gentagelig kommando til CI- eller release-workflows.
- Du ønsker indbygget projekt-opdagelse, output-stier, metadata, oprydning og review.
- Du foretrækker et kommandogrænseflade frem for at skrive Python-kode.

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

Passer godt til:

- Din applikation læser allerede filer, buffere, notebooks eller billedbytes.
- Du har brug for brugerdefineret validering, lagring, logging, retries eller godkendelsesflows.
- Du ønsker at oversætte ét dokument, en notebook eller et billede uden at behandle et helt repository.
- Du ønsker repository-oversættelse, men via Python-automatisering i stedet for en shell-kommando.

## Use the MCP Server when

Choose the MCP server when an agent, editor, or MCP-compatible client should call Co-op Translator tools.

In the normal local setup, the user does not manually keep a server running. The MCP client starts `co-op-translator-mcp` over `stdio` when it needs the tools.

Example user requests an agent could handle:

- "Oversæt denne Markdown-fil til koreansk og behold linkene korrekte."
- "Oversæt denne Markdown-fil til koreansk med agent-assisteret MCP-workflow, ved at bruge din egen model til de oversatte bidder."
- "Oversæt denne notebook til koreansk, behold kodeceller, og brug Co-op Translator MCP til at rekonstruere notebooken."
- "Oversæt teksten i dette billede til japansk og gem resultatet."
- "Kør en dry-run af en repository-oversættelse til spansk og fortæl mig, hvad der ville ændre sig."
- "Gennemse om den koreanske oversættelses-output er ajour."

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

Repository-oversættelse er som standard en dry-run gennem MCP:

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

Passer godt til:

- Du ønsker naturligt-sprog-oversættelsesworkflows inde i en agent eller editor.
- Du ønsker Markdown- eller notebook-oversættelse, hvor host-agentens model oversætter forberedte bidder.
- Du ønsker, at agenten oversætter udvalgt indhold i stedet for et helt repository.
- Du ønsker et godkendelsestrin før repository-omfattende skrivninger.
- Du ønsker en enkelt grænseflade, der eksponerer Markdown-, notebook-, billede-, review- og sti-omskrivningsværktøjer.

## How They Fit Together

The CLI is the best default for humans translating repositories. The Python API is best when your code owns the workflow. The MCP server is best when an agent or editor owns the workflow.

All three paths use the same public Co-op Translator API, so you can start with the CLI, automate with Python later, and expose the same capabilities to MCP clients when you need agent-driven workflows.