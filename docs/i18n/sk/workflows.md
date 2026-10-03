# Vyberte si pracovný postup

Co-op Translator sa dá používať tromi spôsobmi: CLI, Python API a MCP server. Zdieľajú rovnaké prekladateľské schopnosti, ale každý sa hodí pre iný pracovný postup.

Použite túto stránku, keď sa rozhodujete, kde začať.

**Ak upravujete preklady ručne:** predvolené pracovné postupy CLI a Actions prekladajú zmenené zdrojové súbory kompletne znova, takže vaše znenie v týchto súboroch môže byť prepísané. Pred prijatím aktualizácie si prezrite diff. Pre zachovanie blokových úprav Markdownu použite voliteľný [poskytovateľ stavu prekladu Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Rýchle rozhodnutie

| Ak chcete... | Použite | Začnite tu |
| --- | --- | --- |
| Prekladať alebo skontrolovať repozitár z terminálu | CLI | [Referenčná príručka CLI](cli.md) |
| Pridať preklad do Python skriptu, služby, notebooku alebo CI úlohy | Python API | [Python API](api.md) |
| Nechajte agenta, editor alebo klienta kompatibilného s MCP preložiť obsah za vás | MCP Server | [MCP Server](mcp.md) |
| Preložiť jeden Markdown dokument, notebook alebo obrázok, ktorý vaša aplikácia už načítala | [Python API](api.md) alebo [MCP Server](mcp.md) | |
| Preložiť celý repozitár so štandardnými výstupnými priečinkami a metadátami | CLI alebo `run_translation` | [Referenčná príručka CLI](cli.md) alebo [Python API](api.md) |

## Použite CLI, keď

Zvoľte CLI, keď osoba alebo CI úloha riadi preklad repozitára zo shellu.

CLI je najpriamejšia cesta, keď chcete, aby Co-op Translator objavil projektové súbory, vytvoril preložené výstupy, zachoval rozloženie projektu, aktualizoval metadáta a spustil príkazy na revíziu.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Tento príklad prekladá Markdown a notebooky. Parameter `-img` pridajte iba po nakonfigurovaní [Azure AI Vision](configuration.md#azure-ai-vision). Pre prvé spustenie len s Markdownom postupujte podľa [Váš prvý preklad](first-translation.md).

Dobre sa hodí:

- Prekladáte repozitár z terminálu.
- Chcete opakovateľný príkaz pre CI alebo uvoľňovacie pracovné postupy.
- Chcete vstavané zisťovanie projektu, výstupné cesty, metadáta, čistenie a revízie.
- Dávate prednosť príkazovému rozhraniu pred písaním Python kódu.

## Použite Python API, keď

Zvoľte Python API, keď má váš vlastný kód riadiť pracovný postup.

API je užitočné pre aplikácie, skripty na automatizáciu, notebooky, služby a vlastné pipeline. Umožňuje volať nízkoúrovňové API prekladu obsahu pre jednotlivé súbory alebo spustiť rovnakú orchestráciu na úrovni repozitára, akú používa CLI.

Preložte jeden Markdown dokument a rozhodnite, kam ho uložiť:

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

Spustite preklad repozitára z Pythonu:

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

Dobre sa hodí:

- Vaša aplikácia už číta súbory, buffre, notebooky alebo bajty obrázkov.
- Potrebujete vlastnú validáciu, ukladanie, logovanie, opakované pokusy alebo schvaľovacie toky.
- Chcete preložiť jeden dokument, notebook alebo obrázok bez spracovania celého repozitára.
- Chcete preklad repozitára, ale prostredníctvom Python automatizácie namiesto shell príkazu.

## Použite MCP Server, keď

Zvoľte MCP server, keď by agent, editor alebo klient kompatibilný s MCP mal volať nástroje Co-op Translator.

V bežnom lokálnom nastavení používateľ manuálne nepúšťa server neustále. MCP klient spustí `co-op-translator-mcp` cez `stdio`, keď potrebuje nástroje.

Príklady požiadaviek používateľa, ktoré by agent mohol spracovať:

- "Preložte tento Markdown súbor do kórejčiny a zachovajte správnosť odkazov."
- "Preložte tento Markdown súbor do kórejčiny s workflowom MCP asistovaným agentom, pričom prekladajte kúsky pomocou vášho modelu."
- "Preložte tento notebook do kórejčiny, zachovajte kódové bunky a použite Co-op Translator MCP na rekonštrukciu notebooku."
- "Preložte text na tomto obrázku do japončiny a uložte výsledok."
- "Simulujte preklad repozitára do španielčiny a povedzte mi, čo by sa zmenilo."
- "Skontrolujte, či je kórejský preklad aktuálny."

Pre Markdown a notebooky môže MCP pracovať v dvoch režimoch:

| Režim | Použite keď | Hlavné nástroje |
| --- | --- | --- |
| Asistovaný agentom | Hostiteľský agent MCP by mal prekladať kúsky svojim vlastným modelom, bez poverení poskytovateľa LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| S podporou poskytovateľa | Co-op Translator má volať Azure OpenAI, OpenAI alebo Anthropic priamo. | `translate_markdown_content`, `translate_notebook_content` |

Tvar volania Markdown nástroja podporovaného poskytovateľom MCP:

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

Preklad repozitára je predvolene suchý beh cez MCP:

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

Dobre sa hodí:

- Chcete pracovné postupy prekladu v prirodzenom jazyku v agentovi alebo editore.
- Chcete preklad Markdownu alebo notebookov, kde hostiteľský agentný model prekladá pripravené kúsky.
- Chcete, aby agent preložil vybraný obsah namiesto celého repozitára.
- Chcete krok schválenia pred zápismi do celého repozitára.
- Chcete jedno rozhranie, ktoré poskytuje nástroje na Markdown, notebooky, obrázky, revízie a prepísanie ciest.

## Ako do seba zapadajú

CLI je najlepší predvolený nástroj pre ľudí prekladajúcich repozitáre. Python API je najlepšie, keď váš kód vlastní pracovný postup. MCP server je najlepší, keď pracovný postup vlastní agent alebo editor.

Všetky tri cesty používajú rovnaké verejné Co-op Translator API, takže môžete začať s CLI, neskôr automatizovať pomocou Pythonu a sprístupniť rovnaké schopnosti klientom MCP, keď potrebujete pracovné postupy riadené agentom.