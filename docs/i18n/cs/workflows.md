# Vyberte si pracovní postup

Co-op Translator lze používat třemi způsoby: CLI, Python API a MCP server. Sdílejí stejné překladové schopnosti, ale každý vyhovuje jinému pracovnímu postupu.

Použijte tuto stránku, když se rozhodujete, kde začít.

## Rychlé rozhodnutí

| Pokud chcete... | Použít | Začněte zde |
| --- | --- | --- |
| Přeložit nebo zkontrolovat repozitář z terminálu | CLI | [CLI Reference](cli.md) |
| Přidat překlad do Python skriptu, služby, notebooku nebo CI úlohy | Python API | [Python API](api.md) |
| Nechat agenta, editor nebo klienta kompatibilního s MCP přeložit obsah za vás | MCP Server | [MCP Server](mcp.md) |
| Přeložit jeden Markdown dokument, notebook nebo obrázek, který vaše aplikace už načetla | Python API nebo MCP Server | [Python API](api.md) nebo [MCP Server](mcp.md) |
| Přeložit celý repozitář se standardními výstupními složkami a metadaty | CLI nebo `run_translation` | [CLI Reference](cli.md) nebo [Python API](api.md) |

## Kdy používat CLI

Zvolte CLI, když člověk nebo CI úloha řídí překlad repozitáře ze shellem.

CLI je nejpřímější cesta, když chcete, aby Co-op Translator objevil soubory projektu, vytvořil přeložené výstupy, zachoval strukturu projektu, aktualizoval metadata a spustil příkazy pro kontrolu.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Vhodné použití:

- Překládáte repozitář z terminálu.
- Chcete opakovatelný příkaz pro CI nebo release workflow.
- Chcete vestavěné zjišťování projektu, výstupní cesty, metadata, úklid a revizi.
- Preferujete příkazové rozhraní před psaním Python kódu.

## Kdy používat Python API

Zvolte Python API, když má váš vlastní kód kontrolovat pracovní postup.

API je užitečné pro aplikace, automatizační skripty, notebooky, služby a vlastní pipeline. Umožňuje volat nízkoúrovňová překladová API obsahu pro jednotlivé soubory nebo spustit stejnou orchestraci na úrovni repozitáře, jakou používá CLI.

Přeložte jeden Markdown dokument a rozhodněte, kam jej uložit:

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

Spusťte překlad repozitáře z Pythonu:

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

Vhodné použití:

- Vaše aplikace už čte soubory, buffery, notebooky nebo byty obrázků.
- Potřebujete vlastní validaci, úložiště, logování, opakování nebo schvalovací toky.
- Chcete přeložit jeden dokument, notebook nebo obrázek, aniž byste zpracovávali celý repozitář.
- Chcete překlad repozitáře, ale z Python automatizace místo příkazového řádku.

## Kdy používat MCP server

Zvolte MCP server, když by agent, editor nebo klient kompatibilní s MCP měl volat nástroje Co-op Translator.

V normálním lokálním nastavení uživatel server ručně nespouští. MCP klient spustí `co-op-translator-mcp` přes `stdio`, když potřebuje nástroje.

Příklady uživatelských požadavků, které by agent mohl vyřídit:

- "Přeložte tento Markdown soubor do korejštiny a zachovejte správné odkazy."
- "Přeložte tento Markdown soubor do korejštiny pomocí agentem asistovaného MCP workflow, používajícího váš vlastní model pro přeložené části."
- "Přeložte tento notebook do korejštiny, zachovejte kódové buňky a použijte Co-op Translator MCP k rekonstukci notebooku."
- "Přeložte text v tomto obrázku do japonštiny a uložte výsledek."
- "Proveďte suchý běh (dry-run) překladu repozitáře do španělštiny a řekněte mi, co by se změnilo."
- "Zkontrolujte, zda je korejský překlad aktuální."

Pro Markdown a notebooky může MCP pracovat ve dvou režimech:

| Režim | Kdy použít | Hlavní nástroje |
| --- | --- | --- |
| Agent-assisted | Hostitelský MCP agent by měl překládat části svým vlastním modelem, bez pověření poskytovatele LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator by měl volat Azure OpenAI nebo OpenAI přímo. | `translate_markdown_content`, `translate_notebook_content` |

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

Vhodné použití:

- Chcete pracovní postupy překladu v přirozeném jazyce uvnitř agenta nebo editoru.
- Chcete překlad Markdown nebo notebooku, kde hostitelský agent překládá připravené části modelem.
- Chcete, aby agent překládal vybraný obsah místo celého repozitáře.
- Chcete kroky schválení před provedením zápisů do celého repozitáře.
- Chcete jedno rozhraní, které vystavuje nástroje pro Markdown, notebook, obrázek, revizi a přepisování cest.

## Jak to spolu souvisí

CLI je nejlepší výchozí volba pro lidi překládající repozitáře. Python API je nejlepší, když váš kód vlastní pracovní postup. MCP server je nejlepší, když agent nebo editor vlastní pracovní postup.

Všechny tři cesty používají stejné veřejné Co-op Translator API, takže můžete začít s CLI, později automatizovat pomocí Pythonu a vystavit stejné schopnosti MCP klientům, když budete potřebovat workflow řízené agentem.