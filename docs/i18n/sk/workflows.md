# Vyberte si svoj pracovný postup

Co-op Translator je možné používať tromi spôsobmi: CLI, Python API a MCP serverom. Zdieľajú rovnaké prekladateľské možnosti, ale každý sa hodí pre iný pracovný postup.

Použite túto stránku, keď sa rozhodujete, kde začať.

## Rýchle rozhodnutie

| If you want to... | Use | Start here |
| --- | --- | --- |
| Preložiť alebo skontrolovať repozitár z terminálu | CLI | [Referencia CLI](cli.md) |
| Pridať preklad do Python skriptu, služby, notebooku alebo CI úlohy | Python API | [Python API](api.md) |
| Nechajte agenta, editor alebo MCP-kompatibilného klienta preložiť obsah za vás | MCP Server | [MCP Server](mcp.md) |
| Preložte jeden Markdown dokument, notebook alebo obrázok, ktorý vaša aplikácia už načítala | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Preložte celý repozitár so štandardnými výstupnými priečinkami a metadátami | CLI or `run_translation` | [Referencia CLI](cli.md) or [Python API](api.md) |

## Použite CLI, keď

Zvoľte CLI, keď človek alebo CI úloha riadi preklad repozitára zo shellu.

CLI je najpriamejšia cesta, keď chcete, aby Co-op Translator objavil súbory v projekte, vytvoril preložené výstupy, zachoval rozloženie projektu, aktualizoval metadáta a spustil príkazy na kontrolu.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Vhodné pre:

- Prekladáte repozitár z terminálu.
- Chcete opakovateľný príkaz pre CI alebo release pracovné postupy.
- Chcete zabudované vyhľadávanie projektu, výstupné cesty, metadáta, čistenie a kontrolu.
- Uprednostňujete rozhranie príkazového riadka pred písaním Python kódu.

## Použite Python API, keď

Zvoľte Python API, keď má váš vlastný kód riadiť pracovný postup.

API je užitočné pre aplikácie, automatizačné skripty, notebooky, služby a vlastné pipeline. Umožňuje volať nízkoúrovňové API pre preklad obsahu pre jednotlivé súbory alebo spustiť rovnakú orchestráciu na úrovni repozitára, ktorú používa CLI.

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

Vhodné pre:

- Vaša aplikácia už číta súbory, buffery, notebooky alebo bajty obrázkov.
- Potrebujete vlastnú validáciu, ukladanie, logovanie, opakovania alebo schvaľovacie toky.
- Chcete preložiť jeden dokument, notebook alebo obrázok bez spracovania celého repozitára.
- Chcete preklad repozitára, ale z Python automatizácie namiesto shell príkazu.

## Použite MCP Server, keď

Zvoľte MCP server, keď má agent, editor alebo MCP-kompatibilný klient volať nástroje Co-op Translator.

V bežnom lokálnom nastavení používateľ ručne server neudržiava. MCP klient spustí `co-op-translator-mcp` cez `stdio`, keď potrebuje nástroje.

Príklady požiadaviek používateľa, ktoré by agent mohol riešiť:

- "Prelož tento Markdown súbor do kórejčiny a zachovaj správne odkazy."
- "Prelož tento Markdown súbor do kórejčiny s MCP pracovným postupom asistovaným agentom, používajúc svoj vlastný model pre preložené časti."
- "Prelož tento notebook do kórejčiny, zachovaj kódové bunky a použite Co-op Translator MCP na rekonštrukciu notebooku."
- "Prelož text na tomto obrázku do japončiny a ulož výsledok."
- "Vykonaj suchý beh prekladu repozitára do španielčiny a povedz mi, čo by sa zmenilo."
- "Skontrolujte, či je kórejský preklad aktuálny."

Pre Markdown a notebooky môže MCP pracovať v dvoch režimoch:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | Hostiteľský agent MCP by mal prekladať časti svojím vlastným modelom, bez prihlasovacích údajov poskytovateľa LLM pre Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator by mal volať Azure OpenAI alebo OpenAI priamo. | `translate_markdown_content`, `translate_notebook_content` |

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

Preklad repozitára sa cez MCP predvolene vykonáva ako suchý beh (dry-run):

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

Vhodné pre:

- Chcete pracovné postupy prekladu v prirodzenom jazyku v agente alebo editore.
- Chcete preklad Markdown alebo notebookov, kde hostiteľský agentský model prekladá pripravené časti.
- Chcete, aby agent preložil vybraný obsah namiesto celého repozitára.
- Chcete krok schválenia pred zápismi do celého repozitára.
- Chcete jedno rozhranie, ktoré sprístupňuje nástroje pre Markdown, notebooky, obrázky, recenzie a prepisovanie ciest.

## Ako do seba zapadajú

CLI je najlepší predvolený nástroj pre ľudí, ktorí prekladajú repozitáre. Python API je najlepšie, keď váš kód vlastní pracovný postup. MCP server je najlepší, keď pracovný postup vlastní agent alebo editor.

Všetky tri cesty používajú rovnaké verejné Co-op Translator API, takže môžete začať s CLI, neskôr automatizovať s Python a sprístupniť rovnaké schopnosti MCP klientom, keď budete potrebovať pracovné postupy riadené agentom.