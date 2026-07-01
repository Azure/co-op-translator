# Kies uw workflow

Co-op Translator kan op drie manieren worden gebruikt: de CLI, de Python-API en de MCP-server. Ze delen dezelfde vertaalmogelijkheden, maar elk past in een andere workflow.

Gebruik deze pagina wanneer u beslist waar te beginnen.

## Snelle beslissing

| If you want to... | Use | Start here |
| --- | --- | --- |
| Een repository vertalen of beoordelen vanuit een terminal | CLI | [CLI-referentie](cli.md) |
| Vertaling toevoegen aan een Python-script, service, notebook of CI-taak | Python API | [Python-API](api.md) |
| Laat een agent, editor of MCP-compatibele client inhoud voor u vertalen | MCP Server | [MCP-server](mcp.md) |
| Vertaal één Markdown-document, notebook of afbeelding die uw app al heeft geladen | Python API or MCP Server | [Python-API](api.md) or [MCP-server](mcp.md) |
| Vertaal een volledige repository met standaard uitvoermap en metadata | CLI or `run_translation` | [CLI-referentie](cli.md) or [Python-API](api.md) |

## Gebruik de CLI wanneer

Kies de CLI wanneer een persoon of CI-taak de repositoryvertaling vanuit een shell uitvoert.

De CLI is het meest directe pad wanneer u wilt dat Co-op Translator projectbestanden ontdekt, vertaalde uitvoer maakt, de projectindeling behoudt, metadata bijwerkt en review-opdrachten uitvoert.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Past goed bij:

- U vertaalt een repository vanuit uw terminal.
- U wilt een herhaalbaar commando voor CI- of release-workflows.
- U wilt ingebouwde projectdetectie, uitvoerlocaties, metadata, opschoning en review.
- U geeft de voorkeur aan een opdrachtinterface boven het schrijven van Python-code.

## Gebruik de Python-API wanneer

Kies de Python-API wanneer uw eigen code de workflow moet aansturen.

De API is nuttig voor applicaties, automatiseringsscripts, notebooks, services en aangepaste pipelines. Hiermee kunt u laag-niveau contentvertaal-API's voor individuele bestanden aanroepen, of dezelfde repository-niveau orkestratie uitvoeren die door de CLI wordt gebruikt.

Vertaal één Markdown-document en beslis waar u het wilt opslaan:

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

Voer een repositoryvertaling vanuit Python uit:

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

Past goed bij:

- Uw applicatie leest al bestanden, buffers, notebooks of afbeeldingsbytes.
- U heeft aangepaste validatie, opslag, logregistratie, herhaalde pogingen of goedkeuringsstromen nodig.
- U wilt één document, notebook of afbeelding vertalen zonder een hele repository te verwerken.
- U wilt een repositoryvertaling, maar dan via Python-automatisering in plaats van een shell-opdracht.

## Gebruik de MCP-server wanneer

Kies de MCP-server wanneer een agent, editor of MCP-compatibele client de Co-op Translator-tools moet aanroepen.

In de normale lokale opzet houdt de gebruiker niet handmatig een server draaiend. De MCP-client start `co-op-translator-mcp` via `stdio` wanneer deze de tools nodig heeft.

Voorbeelden van gebruikersverzoeken die een agent zou kunnen afhandelen:

- Vertaal dit Markdown-bestand naar het Koreaans en houd de links correct.
- Vertaal dit Markdown-bestand naar het Koreaans met de agent-geassisteerde MCP-workflow, waarbij uw eigen model wordt gebruikt voor de vertaalde gedeelten.
- Vertaal deze notebook naar het Koreaans, behoud codecellen en gebruik Co-op Translator MCP om de notebook te reconstrueren.
- Vertaal de tekst in deze afbeelding naar het Japans en sla het resultaat op.
- Voer een proefrun uit van een repositoryvertaling naar het Spaans en vertel me wat er zou veranderen.
- Controleer of de Koreaanse vertaling up-to-date is.

Voor Markdown en notebooks kan MCP in twee modi werken:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-geassisteerd | De MCP-hostagent zou gedeelten moeten vertalen met zijn eigen model, zonder inloggegevens voor de LLM-provider van Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-ondersteund | Co-op Translator moet rechtstreeks Azure OpenAI of OpenAI aanroepen. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-ondersteunde Markdown-tool-aanroepvorm:

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

Vorm van de MCP image-tool-aanroep:

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

Repositoryvertaling wordt standaard als proefrun via MCP uitgevoerd:

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

Past goed bij:

- U wilt vertaalsworkflows in natuurlijke taal binnen een agent of editor.
- U wilt Markdown- of notebookvertaling waarbij het hostagentmodel voorbereide gedeelten vertaalt.
- U wilt dat de agent geselecteerde inhoud vertaalt in plaats van een hele repository.
- U wilt een goedkeuringsstap voordat er repository-brede schrijfbewerkingen plaatsvinden.
- U wilt één interface die Markdown-, notebook-, afbeelding-, review- en pad-herschrijf-tools aanbiedt.

## Hoe ze samenwerken

De CLI is de beste standaardkeuze voor mensen die repositories vertalen. De Python-API is het beste wanneer uw code de workflow beheert. De MCP-server is het beste wanneer een agent of editor de workflow beheert.

Alle drie de paden gebruiken dezelfde openbare Co-op Translator API, dus u kunt beginnen met de CLI, later automatiseren met Python, en dezelfde mogelijkheden blootstellen aan MCP-clients wanneer u agentgestuurde workflows nodig heeft.