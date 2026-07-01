# Välj ditt arbetsflöde

Co-op Translator kan användas på tre sätt: CLI, Python-API och MCP-servern. De delar samma översättningsfunktioner, men varje sätt passar ett annat arbetsflöde.

Använd den här sidan när du ska bestämma var du ska börja.

## Snabbt beslut

| Om du vill... | Använd | Börja här |
| --- | --- | --- |
| Översätta eller granska ett repository från en terminal | CLI | [CLI-referens](cli.md) |
| Lägga till översättning i ett Python-skript, en tjänst, en notebook eller ett CI-jobb | Python-API | [Python-API](api.md) |
| Låta en agent, redigerare eller MCP-kompatibel klient översätta innehåll åt dig | MCP-server | [MCP-server](mcp.md) |
| Översätta ett Markdown-dokument, en notebook eller en bild som din app redan har laddat | Python-API eller MCP-server | [Python-API](api.md) eller [MCP-server](mcp.md) |
| Översätta ett helt repository med standardutdata-mappar och metadata | CLI eller `run_translation` | [CLI-referens](cli.md) eller [Python-API](api.md) |

## Använd CLI när

Välj CLI när en person eller ett CI-jobb styr repositoryöversättningen från ett shell.

CLI är den mest direkta vägen när du vill att Co-op Translator ska upptäcka projektfiler, skapa översatta utdata, bevara projektlayouten, uppdatera metadata och köra granskningskommandon.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Passar bra:

- Du översätter ett repository från din terminal.
- Du vill ha ett upprepningsbart kommando för CI- eller releasearbetsflöden.
- Du vill ha inbyggd projektupptäckt, utdatavägar, metadata, rensning och granskning.
- Du föredrar ett kommandogränssnitt framför att skriva Python-kod.

## Använd Python-API:t när

Välj Python-API:t när din egen kod ska styra arbetsflödet.

API:t är användbart för applikationer, automationsskript, notebooks, tjänster och anpassade pipelines. Det låter dig anropa lågnivå-API:er för innehållsöversättning för enskilda filer, eller köra samma repositorynivåorkestrering som används av CLI.

Översätt ett Markdown-dokument och bestäm var det ska sparas:

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

Kör en repositoryöversättning från Python:

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

Passar bra:

- Din applikation läser redan filer, buffrar, notebooks eller bildbytes.
- Du behöver anpassad validering, lagring, loggning, omförsök eller godkännandeflöden.
- Du vill översätta ett dokument, en notebook eller en bild utan att bearbeta ett helt repository.
- Du vill repositoryöversättning, men från Python-automation istället för ett shellkommando.

## Använd MCP-servern när

Välj MCP-servern när en agent, redigerare eller MCP-kompatibel klient ska anropa Co-op Translator-verktygen.

I den normala lokala konfigurationen håller användaren inte manuellt en server igång. MCP-klienten startar `co-op-translator-mcp` över `stdio` när den behöver verktygen.

Exempel på användarförfrågningar som en agent kan hantera:

- "Översätt den här Markdown-filen till koreanska och behåll länkarna korrekta."
- "Översätt den här Markdown-filen till koreanska med det agentassisterade MCP-arbetsflödet och använd din egen modell för de översatta delarna."
- "Översätt den här notebooken till koreanska, bevara kodceller och använd Co-op Translator MCP för att återskapa notebooken."
- "Översätt texten i den här bilden till japanska och spara resultatet."
- "Gör en torrkörning av en repositoryöversättning till spanska och berätta vad som skulle ändras."
- "Granska om den koreanska översättningen är uppdaterad."

För Markdown och notebooks kan MCP arbeta i två lägen:

| Läge | Använd när | Huvudverktyg |
| --- | --- | --- |
| Agent-assisterat | MCP-värdagenten ska översätta delar med sin egen modell, utan Co-op Translator LLM-leverantörsuppgifter. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Providerstödd | Co-op Translator ska anropa Azure OpenAI eller OpenAI direkt. | `translate_markdown_content`, `translate_notebook_content` |

MCP providerstödd Markdown-verktygsanropsform:

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

MCP bildverktygsanropsform:

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

Repositoryöversättning körs som torrkörning som standard via MCP:

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

Passar bra:

- Du vill ha naturliga språkbaserade översättningsarbetsflöden i en agent eller redigerare.
- Du vill ha Markdown- eller notebooköversättning där värdagentens modell översätter förberedda delar.
- Du vill att agenten översätter valt innehåll istället för ett helt repository.
- Du vill ha ett godkännandesteg innan ändringar skrivs över hela repositoryt.
- Du vill ha ett gränssnitt som exponerar verktyg för Markdown, notebook, bild, granskning och sökvägs-omskrivning.

## Hur de passar ihop

CLI är det bästa standardvalet för människor som översätter repositories. Python-API:t är bäst när din kod äger arbetsflödet. MCP-servern är bäst när en agent eller redigerare äger arbetsflödet.

Alla tre vägar använder samma publika Co-op Translator API, så du kan börja med CLI, automatisera med Python senare och exponera samma funktioner för MCP-klienter när du behöver agentdrivna arbetsflöden.