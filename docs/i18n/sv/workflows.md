# Välj ditt arbetsflöde

Co-op Translator kan användas på tre sätt: CLI, Python API och MCP-servern. De delar samma översättningsfunktioner, men varje passar för ett annat arbetsflöde.

Använd den här sidan när du bestämmer var du ska börja.

**Om du redigerar översättningar manuellt:** standardarbetsflödena för CLI och Actions översätter om ändrade källfiler i sin helhet, så din formulering i dessa filer kan skrivas över. Granska diffen innan du accepterar en uppdatering. För bevarande på blocknivå av accepterade redigeringar i Markdown, använd den valfria [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Snabbt beslut

| Om du vill... | Använd | Börja här |
| --- | --- | --- |
| Översätta eller granska ett repository från en terminal | CLI | [CLI-referens](cli.md) |
| Lägga till översättning i ett Python-skript, en tjänst, en notebook eller ett CI-jobb | Python API | [Python API](api.md) |
| Låt en agent, redigerare eller MCP-kompatibel klient översätta innehåll åt dig | MCP Server | [MCP Server](mcp.md) |
| Översätt ett Markdown-dokument, en notebook eller en bild som din app redan har laddat | Python API eller MCP Server | [Python API](api.md) eller [MCP Server](mcp.md) |
| Översätt ett helt repository med standardutmatningsmappar och metadata | CLI eller `run_translation` | [CLI-referens](cli.md) eller [Python API](api.md) |

## Använd CLI när

Välj CLI när en person eller ett CI-jobb styr översättningen av ett repository från ett skal.

CLI är den mest direkta vägen när du vill att Co-op Translator ska upptäcka projektfiler, skapa översatta utdata, bevara projektlayouten, uppdatera metadata och köra granskningskommandon.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Detta exempel översätter Markdown och notebooks. Lägg till `-img` endast efter att du har konfigurerat [Azure AI Vision](configuration.md#azure-ai-vision). För en första körning med endast Markdown, följ [Din första översättning](first-translation.md).

Lämpligt när:

- Du översätter ett repository från din terminal.
- Du vill ha ett upprepbart kommando för CI- eller releasearbetsflöden.
- Du vill ha inbyggd projektdetektering, utmatningsvägar, metadata, städning och granskning.
- Du föredrar ett kommandogränssnitt framför att skriva Python-kod.

## Använd Python API när

Välj Python API när din egen kod ska styra arbetsflödet.

API:et är användbart för applikationer, automatiseringsskript, notebooks, tjänster och anpassade pipelines. Det låter dig anropa låg-nivå API:er för innehållsöversättning för enstaka filer, eller köra samma orkestrering på repository-nivå som används av CLI.

Översätt ett Markdown-dokument och bestäm var du ska spara det:

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

Kör en repository-översättning från Python:

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

Lämpligt när:

- Din applikation läser redan filer, buffrar, notebooks eller bildbytes.
- Du behöver anpassad validering, lagring, loggning, retry-mekanismer eller godkännandeflöden.
- Du vill översätta ett dokument, en notebook eller en bild utan att bearbeta ett helt repository.
- Du vill ha repository-översättning, men med Python-automation istället för ett skalkommando.

## Använd MCP-servern när

Välj MCP-servern när en agent, redigerare eller MCP-kompatibel klient ska anropa Co-op Translator-verktyg.

I den normala lokala installationen håller användaren inte manuellt en server igång. MCP-klienten startar `co-op-translator-mcp` över `stdio` när den behöver verktygen.

Exempel på användarförfrågningar som en agent kan hantera:

- "Översätt den här Markdown-filen till koreanska och se till att länkarna är korrekta."
- "Översätt den här Markdown-filen till koreanska med det agentassisterade MCP-arbetsflödet, och använd din egen modell för de översatta delarna."
- "Översätt den här notebooken till koreanska, bevara kodcellerna och använd Co-op Translator MCP för att rekonstruera notebooken."
- "Översätt texten i den här bilden till japanska och spara resultatet."
- "Kör en torrkörning av en repository-översättning till spanska och berätta vad som skulle förändras."
- "Granska om den koreanska översättningsutgången är uppdaterad."

För Markdown och notebooks kan MCP arbeta i två lägen:

| Läge | Använd när | Huvudverktyg |
| --- | --- | --- |
| Agentassisterat | MCP-värdagenten ska översätta delar med sin egen modell, utan Co-op Translator LLM-leverantörens autentiseringsuppgifter. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Providerstödd | Co-op Translator bör anropa Azure OpenAI, OpenAI eller Anthropic direkt. | `translate_markdown_content`, `translate_notebook_content` |

MCP-leverantörsunderstödd Markdown-verktygsanropsform:

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

Repository-översättning körs som torrkörning som standard via MCP:

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

Lämpligt när:

- Du vill ha naturliga språk-översättningsarbetsflöden inuti en agent eller redigerare.
- Du vill ha Markdown- eller notebook-översättning där värdagentens modell översätter förberedda delar.
- Du vill att agenten översätter valt innehåll istället för ett helt repository.
- Du vill ha ett godkännandesteg innan skrivningar över hela repositoryt.
- Du vill ha ett gränssnitt som exponerar verktyg för Markdown, notebook, bild, granskning och sökvägs-omskrivning.

## Hur de passar ihop

CLI är det bästa standardvalet för människor som översätter repositories. Python API är bäst när din kod äger arbetsflödet. MCP-servern är bäst när en agent eller redigerare äger arbetsflödet.

Alla tre vägar använder samma publika Co-op Translator API, så du kan börja med CLI, automatisera med Python senare och exponera samma funktioner för MCP-klienter när du behöver agentstyrda arbetsflöden.