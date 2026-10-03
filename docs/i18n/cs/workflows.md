# Vyberte svůj pracovní postup

Co-op Translator lze používat třemi způsoby: CLI, Python API a MCP server. Sdílejí stejné možnosti překladu, ale každý vyhovuje jinému pracovnímu postupu.

Použijte tuto stránku, když se rozhodujete, kde začít.

**Pokud upravujete překlady ručně:** výchozí pracovní toky CLI a Actions přepřekládají změněné zdrojové soubory celé, takže vaše znění v těchto souborech může být přepsáno. Před přijetím aktualizace si prohlédněte diff. Pro zachování úprav na úrovni bloků Markdownu použijte volitelný [poskytovatel stavu překladu Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Rychlé rozhodnutí

| Pokud chcete... | Použijte | Začněte zde |
| --- | --- | --- |
| Překládat nebo revidovat repozitář z terminálu | CLI | [Reference k CLI](cli.md) |
| Přidat překlad do Python skriptu, služby, notebooku nebo CI úlohy | Python API | [Python API](api.md) |
| Nechte agenta, editor nebo MCP-kompatibilního klienta přeložit obsah za vás | MCP Server | [MCP Server](mcp.md) |
| Přeložit jeden Markdown dokument, notebook nebo obrázek, který vaše aplikace již načetla | Python API nebo MCP Server | [Python API](api.md) nebo [MCP Server](mcp.md) |
| Přeložit celý repozitář se standardními výstupními složkami a metadata | CLI nebo `run_translation` | [Reference k CLI](cli.md) nebo [Python API](api.md) |

## Použijte CLI, když

Zvolte CLI, když člověk nebo CI úloha řídí překlad repozitáře ze shellu.

CLI je nejpřímější cesta, když chcete, aby Co-op Translator objevil soubory projektu, vytvořil přeložené výstupy, zachoval rozložení projektu, aktualizoval metadata a spustil příkazy pro revizi.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Tento příklad překládá Markdown a notebooky. Přidejte `-img` až po nakonfigurování [Azure AI Vision](configuration.md#azure-ai-vision). Pro první běh pouze s Markdownem postupujte podle [Váš první překlad](first-translation.md).

Vhodné pro:

- Překládáte repozitář z terminálu.
- Chcete opakovatelný příkaz pro CI nebo vydávací workflow.
- Chcete vestavěné objevování projektu, výstupní cesty, metadata, čištění a revizi.
- Upřednostňujete rozhraní příkazového řádku před psaním Python kódu.

## Použijte Python API, když

Zvolte Python API, když má váš vlastní kód řídit pracovní postup.

API je užitečné pro aplikace, skripty automatizace, notebooky, služby a vlastní pipeline. Umožňuje volat nízkoúrovňová API pro překlad obsahu pro jednotlivé soubory nebo spustit tu samou orchestraci na úrovni repozitáře, kterou používá CLI.

Přeložte jeden Markdown dokument a rozhodněte, kam ho uložit:

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Vhodné pro:

- Vaše aplikace již čte soubory, bufory, notebooky nebo bajty obrázků.
- Potřebujete vlastní validaci, úložiště, logování, opakování pokusů nebo schvalovací toky.
- Chcete přeložit jeden dokument, notebook nebo obrázek, aniž byste zpracovávali celý repozitář.
- Chcete překlad repozitáře, ale pomocí Python automatizace místo příkazu v shellu.

## Použijte MCP Server, když

Zvolte MCP server, když by agent, editor nebo MCP-kompatibilní klient měl volat nástroje Co-op Translator.

V běžném lokálním nastavení uživatel server ručně nespouští. MCP klient spustí `co-op-translator-mcp` přes `stdio`, když potřebuje nástroje.

Příklady uživatelských požadavků, které by agent mohl zpracovat:

- "Přeložte tento Markdown soubor do korejštiny a zachovejte správné odkazy."
- "Přeložte tento Markdown soubor do korejštiny v agentem asistovaném MCP pracovním postupu a použijte svůj vlastní model pro přeložené části."
- "Přeložte tento notebook do korejštiny, zachovejte kódové buňky a použijte Co-op Translator MCP k rekonstrukci notebooku."
- "Přeložte text na tomto obrázku do japonštiny a uložte výsledek."
- "Proveďte suchý běh překladu repozitáře do španělštiny a řekněte mi, co by se změnilo."
- "Zkontrolujte, zda je korejský překlad aktuální."

Pro Markdown a notebooky může MCP fungovat ve dvou režimech:

| Režim | Používejte když | Hlavní nástroje |
| --- | --- | --- |
| Asistováno agentem | Když by hostitelský MCP agent měl překládat části vlastním modelem, bez přihlašovacích údajů poskytovatele LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Podporované poskytovatelem | Když by Co-op Translator měl volat Azure OpenAI, OpenAI nebo Anthropic přímo. | `translate_markdown_content`, `translate_notebook_content` |

Tvar volání nástroje Markdownu podporovaného poskytovatelem přes MCP:

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

Tvar volání nástroje pro obrázky přes MCP:

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

Překlad repozitáře je přes MCP ve výchozím nastavení proveden jako suchý běh:

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

Vhodné pro:

- Chcete pracovní postupy překladu v přirozeném jazyce uvnitř agenta nebo editoru.
- Chcete překlad Markdownu nebo notebooku, kde hostitelský model agenta překládá připravené části.
- Chcete, aby agent přeložil vybraný obsah namísto celého repozitáře.
- Chcete schvalovací krok před zápisy do celého repozitáře.
- Chcete jedno rozhraní, které zpřístupňuje nástroje pro Markdown, notebooky, obrázky, revizi a přepisování cest.

## Jak do sebe zapadají

CLI je nejlepší výchozí volba pro lidi překládající repozitáře. Python API je nejlepší, když váš kód řídí pracovní postup. MCP server je nejlepší, když workflow řídí agent nebo editor.

Všechny tři cesty používají stejné veřejné API Co-op Translator, takže můžete začít s CLI, později automatizovat pomocí Pythonu a vystavit stejné možnosti klientům MCP, když budete potřebovat pracovní postupy řízené agentem.