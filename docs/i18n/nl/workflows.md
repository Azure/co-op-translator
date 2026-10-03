# Kies uw workflow

Co-op Translator kan op drie manieren worden gebruikt: de CLI, de Python API en de MCP-server. Ze delen dezelfde vertaalmogelijkheden, maar elk past bij een andere workflow.

Gebruik deze pagina wanneer u besluit waar te beginnen.

**If you edit translations by hand:** de standaard CLI- en Actions-workflows vertalen gewijzigde bronbestanden volledig opnieuw, dus uw bewoordingen in die bestanden kunnen worden overschreven. Bekijk het verschil voordat u een update accepteert. Voor behoud van geaccepteerde bewerkingen op Markdown-blokniveau, gebruik de optionele [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Snelle keuze

| Als u wilt... | Gebruik | Begin hier |
| --- | --- | --- |
| Een repository vertalen of beoordelen vanuit een terminal | CLI | [CLI-referentie](cli.md) |
| Vertaling toevoegen aan een Python-script, service, notebook of CI-taak | Python API | [Python API](api.md) |
| Laat een agent, editor of MCP-compatibele client inhoud voor u vertalen | MCP Server | [MCP Server](mcp.md) |
| Vertaal één Markdown-document, notebook of afbeelding die uw app al heeft geladen | Python API of MCP Server | [Python API](api.md) of [MCP Server](mcp.md) |
| Vertaal een volledige repository met standaard uitvoermappen en metadata | CLI of `run_translation` | [CLI-referentie](cli.md) of [Python API](api.md) |

## Gebruik de CLI wanneer

Kies de CLI wanneer een persoon of een CI-taak de vertaling van een repository vanaf een shell uitvoert.

De CLI is het meest directe pad wanneer u wilt dat Co-op Translator projectbestanden ontdekt, vertaalde uitvoer maakt, de projectindeling behoudt, metadata bijwerkt en review-opdrachten uitvoert.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Dit voorbeeld vertaalt Markdown en notebooks. Voeg `-img` alleen toe nadat u [Azure AI Vision](configuration.md#azure-ai-vision) hebt geconfigureerd. Voor een eerste run alleen met Markdown volgt u [Your first translation](first-translation.md).

Geschikt voor:

- U vertaalt een repository vanaf uw terminal.
- U wilt een herhaalbare opdracht voor CI- of release-workflows.
- U wilt ingebouwde projectdetectie, uitvoerpaden, metadata, opschoning en review.
- U geeft de voorkeur aan een opdrachtinterface boven het schrijven van Python-code.

## Gebruik de Python API wanneer

Kies de Python API wanneer uw eigen code de workflow moet aansturen.

De API is nuttig voor applicaties, automatiseringsscripts, notebooks, services en aangepaste pipelines. Hiermee kunt u low-level contentvertaal-API's voor afzonderlijke bestanden aanroepen, of dezelfde repository-niveau orkestratie uitvoeren die door de CLI wordt gebruikt.

Vertaal één Markdown-document en bepaal waar u het wilt opslaan:

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

Voer een repositoryvertaling uit vanuit Python:

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

Geschikt voor:

- Uw toepassing leest al bestanden, buffers, notebooks of afbeeldingsbytes.
- U heeft aangepaste validatie, opslag, logging, herhaalde pogingen of goedkeuringsstromen nodig.
- U wilt één document, notebook of afbeelding vertalen zonder een hele repository te verwerken.
- U wilt repositoryvertaling, maar vanuit Python-automatisering in plaats van een shell-opdracht.

## Gebruik de MCP-server wanneer

Kies de MCP-server wanneer een agent, editor of MCP-compatibele client Co-op Translator-tools moet aanroepen.

In de normale lokale configuratie houdt de gebruiker niet handmatig een server draaiend. De MCP-client start `co-op-translator-mcp` via `stdio` wanneer hij de tools nodig heeft.

Voorbeeldverzoeken van gebruikers die een agent zou kunnen afhandelen:

- "Vertaal dit Markdown-bestand naar het Koreaans en houd de links correct."
- "Vertaal dit Markdown-bestand naar het Koreaans met de agent-ondersteunde MCP-workflow, waarbij u uw eigen model gebruikt voor de vertaalde chunks."
- "Vertaal dit notebook naar het Koreaans, behoud codecellen en gebruik Co-op Translator MCP om het notebook te reconstrueren."
- "Vertaal de tekst in deze afbeelding naar het Japans en sla het resultaat op."
- "Voer een dry-run uit van een repositoryvertaling naar het Spaans en vertel me wat er zou veranderen."
- "Controleer of de Koreaanse vertaling actueel is."

Voor Markdown en notebooks kan MCP in twee modi werken:

| Modus | Gebruik wanneer | Belangrijkste tools |
| --- | --- | --- |
| Agent-ondersteund | De MCP-hostagent zou chunks met zijn eigen model moeten vertalen, zonder Co-op Translator LLM-providerreferenties. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-ondersteund | Co-op Translator zou Azure OpenAI, OpenAI of Anthropic rechtstreeks moeten aanroepen. | `translate_markdown_content`, `translate_notebook_content` |

Vorm van MCP provider-ondersteunde Markdown-toolaanroep:

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

Vorm van MCP afbeeldings-toolaanroep:

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

Repositoryvertaling is standaard een dry-run via MCP:

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

Geschikt voor:

- U wilt vertaalworkflows in natuurlijke taal binnen een agent of editor.
- U wilt Markdown- of notebookvertaling waarbij het hostagentmodel voorbereide chunks vertaalt.
- U wilt dat de agent geselecteerde inhoud vertaalt in plaats van een hele repository.
- U wilt een goedkeuringsstap voordat er repository-brede schrijfbewerkingen plaatsvinden.
- U wilt één interface die Markdown-, notebook-, afbeelding-, review- en padherschrijf-tools aanbiedt.

## Hoe ze samenwerken

De CLI is de beste standaard voor mensen die repositories vertalen. De Python API is het beste wanneer uw code de workflow beheert. De MCP-server is het beste wanneer een agent of editor de workflow beheert.

Alle drie paden gebruiken dezelfde publieke Co-op Translator API, dus u kunt beginnen met de CLI, later automatiseren met Python en dezelfde mogelijkheden aan MCP-clients blootstellen wanneer u agentgestuurde workflows nodig hebt.