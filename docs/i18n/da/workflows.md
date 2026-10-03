# Vælg din arbejdsgang

Co-op Translator kan bruges på tre måder: CLI'en, Python-API'en og MCP-serveren. De deler de samme oversættelsesmuligheder, men hver passer til en forskellig arbejdsgang.

Brug denne side, når du skal beslutte, hvor du skal starte.

**Hvis du redigerer oversættelser manuelt:** de standardmæssige CLI- og Actions-arbejdsgange oversætter ændrede kildefiler fuldstændigt igen, så dine formuleringer i disse filer kan blive overskrevet. Gennemgå diff'en før du accepterer en opdatering. For bevaring på blokniveau af accepterede redigeringer i Markdown, brug den valgfrie [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Hurtigt valg

| Hvis du vil... | Brug | Start her |
| --- | --- | --- |
| Oversætte eller gennemgå et repository fra en terminal | CLI | [CLI Reference](cli.md) |
| Tilføj oversættelse til et Python-script, en tjeneste, en notebook eller et CI-job | Python API | [Python API](api.md) |
| Lad en agent, editor eller MCP-kompatibel klient oversætte indhold for dig | MCP Server | [MCP Server](mcp.md) |
| Oversæt et enkelt Markdown-dokument, en notebook eller et billede, som din app allerede har indlæst | Python API eller MCP Server | [Python API](api.md) eller [MCP Server](mcp.md) |
| Oversæt et helt repository med standard output-mapper og metadata | CLI eller `run_translation` | [CLI Reference](cli.md) eller [Python API](api.md) |

## Brug CLI'en når

Vælg CLI'en, når en person eller et CI-job styrer repository-oversættelsen fra en shell.

CLI'en er den mest direkte vej, når du vil have Co-op Translator til at finde projektfiler, oprette oversatte output, bevare projektlayoutet, opdatere metadata og køre review-kommandoer.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Dette eksempel oversætter Markdown og notebooks. Tilføj `-img` først efter at have konfigureret [Azure AI Vision](configuration.md#azure-ai-vision). For et førstekørsel kun for Markdown, følg [Your first translation](first-translation.md).

Passer godt til:

- Du oversætter et repository fra din terminal.
- Du ønsker en gentagelig kommando til CI- eller release-arbejdsgange.
- Du vil have indbygget projektopdagelse, output-stier, metadata, oprydning og review.
- Du foretrækker en kommandolinjegrænseflade frem for at skrive Python-kode.

## Brug Python API'en når

Vælg Python API'en, når din egen kode skal kontrollere arbejdsgangen.

API'en er nyttig til applikationer, automatiseringsscripts, notebooks, tjenester og tilpassede pipelines. Den giver dig mulighed for at kalde lavniveau-API'er til indholdsoversættelse for enkelte filer eller køre den samme repository-niveau orkestrering, som CLI'en bruger.

Oversæt ét Markdown-dokument og beslut hvor det skal gemmes:

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

Kør en repository-oversættelse fra Python:

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

Passer godt til:

- Din applikation læser allerede filer, buffere, notebooks eller billedbytes.
- Du har brug for tilpasset validering, lagring, logging, genforsøg eller godkendelsesflow.
- Du vil oversætte et enkelt dokument, notebook eller billede uden at behandle et helt repository.
- Du vil have repository-oversættelse, men fra Python-automatisering i stedet for en shell-kommando.

## Brug MCP-serveren når

Vælg MCP-serveren, når en agent, editor eller MCP-kompatibel klient skal kalde Co-op Translator-værktøjer.

I den normale lokale opsætning holder brugeren ikke manuelt en server kørende. MCP-klienten starter `co-op-translator-mcp` over `stdio`, når den har brug for værktøjerne.

Eksempler på brugerforespørgsler, en agent kunne håndtere:

- "Oversæt denne Markdown-fil til koreansk og behold linkene korrekte."
- "Oversæt denne Markdown-fil til koreansk med den agent-assisterede MCP-arbejdsgang, og brug din egen model til de oversatte dele."
- "Oversæt denne notebook til koreansk, bevar kodeceller og brug Co-op Translator MCP til at rekonstruere notebook'en."
- "Oversæt teksten i dette billede til japansk og gem resultatet."
- "Kør en dry-run af en repository-oversættelse til spansk og fortæl mig, hvad der ville ændre sig."
- "Gennemgå, om den koreanske oversættelse er opdateret."

For Markdown og notebooks kan MCP arbejde i to tilstande:

| Tilstand | Brug når | Hovedværktøjer |
| --- | --- | --- |
| Agent-assisteret | MCP-værtsagenten bør oversætte chunks med sin egen model, uden Co-op Translator LLM-udbyder-legitimationsoplysninger. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Udbyder-understøttet | Co-op Translator bør kalde Azure OpenAI, OpenAI eller Anthropic direkte. | `translate_markdown_content`, `translate_notebook_content` |

MCP udbyder-understøttet Markdown-værktøjskaldsform:

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

MCP billedeværktøjskaldsform:

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

Repository-oversættelse er som standard dry-run via MCP:

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

- Du ønsker oversættelsesarbejdsgange i naturligt sprog inde i en agent eller editor.
- Du ønsker Markdown- eller notebook-oversættelse, hvor værtsagentens model oversætter forberedte chunks.
- Du ønsker, at agenten oversætter udvalgt indhold i stedet for et helt repository.
- Du ønsker et godkendelsestrin før skrivning på tværs af repository'et.
- Du ønsker en enkelt grænseflade, der eksponerer værktøjer til Markdown, notebook, billede, review og sti-omskrivning.

## Hvordan de passer sammen

CLI'en er det bedste standardvalg for mennesker, der oversætter repositories. Python API'en er bedst, når din kode ejer arbejdsgangen. MCP-serveren er bedst, når en agent eller editor ejer arbejdsgangen.

Alle tre veje bruger den samme offentlige Co-op Translator API, så du kan starte med CLI'en, automatisere med Python senere, og eksponere de samme muligheder til MCP-klienter, når du har brug for agent-drevne arbejdsgange.