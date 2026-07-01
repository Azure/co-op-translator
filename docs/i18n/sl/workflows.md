# Izberite svoj potek dela

Co-op Translator je mogoče uporabljati na tri načine: ukazna vrstica (CLI), Python API in MCP strežnik. Vsi uporabljajo enake prevajalske zmogljivosti, vendar se vsak bolj prilega drugačnemu poteku dela.

Uporabite to stran, ko se odločate, kje začeti.

## Hitra odločitev

| If you want to... | Use | Start here |
| --- | --- | --- |
| Prevesti ali pregledati repozitorij iz terminala | CLI | [Referenca CLI](cli.md) |
| Dodajte prevajanje v Python skripto, storitev, zvezek ali CI opravilo | Python API | [Python API](api.md) |
| Dovolite agentu, urejevalniku ali MCP-kompatibilnemu odjemalcu, da prevede vsebino namesto vas | MCP Server | [MCP strežnik](mcp.md) |
| Prevedite en Markdown dokument, zvezek ali sliko, ki ga je vaša aplikacija že naložila | Python API or MCP Server | [Python API](api.md) or [MCP strežnik](mcp.md) |
| Prevedite celoten repozitorij s standardnimi izhodnimi mapami in metapodatki | CLI or `run_translation` | [Referenca CLI](cli.md) or [Python API](api.md) |

## Uporabite CLI, ko

Izberite CLI, kadar oseba ali CI opravilo izvaja prevajanje repozitorija iz ukazne vrstice.

CLI je najdirektnejša pot, kadar želite, da Co-op Translator odkrije datoteke projekta, ustvari prevedene izhode, ohrani postavitev projekta, posodobi metapodatke in izvede ukaze za pregled.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Primerno za:

- Prev
ajate repozitorij iz terminala.
- Želite ponovljiv ukaz za CI ali poteke izdaj.
- Želite vgrajeno odkrivanje projektov, izhodne poti, metapodatke, čiščenje in pregled.
- Raje uporabljate ukazni vmesnik, namesto pisanja Python kode.

## Uporabite Python API, ko

Izberite Python API, kadar naj vaš lasten program nadzoruje potek dela.

API je uporaben za aplikacije, avtomatizirane skripte, zvezke, storitve in prilagojene poteke. Omogoča klic nizkonivojskih API-jev za prevajanje vsebine za posamezne datoteke ali izvajanje iste orkestracije na ravni repozitorija, ki jo uporablja CLI.

Prevedite en Markdown dokument in se odločite, kam ga shraniti:

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

Zaženite prevajanje repozitorija iz Pythona:

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

Primerno za:

- Vaša aplikacija že bere datoteke, medpomnilnike, zvezke ali bajtne vsebine slik.
- Potrebujete prilagojeno validacijo, shranjevanje, beleženje, ponovitve ali postopke odobritve.
- Želite prevesti en dokument, zvezek ali sliko, brez obdelave celotnega repozitorija.
- Želite prevajanje repozitorija, vendar iz Python avtomatizacije namesto ukaza v lupini.

## Uporabite MCP strežnik, ko

Izberite MCP strežnik, kadar mora agent, urejevalnik ali MCP-kompatibilen odjemalec klicati orodja Co-op Translatorja.

V običajni lokalni namestitvi uporabnik strežnika ne poganja ročno. MCP odjemalec zažene `co-op-translator-mcp` prek `stdio`, ko potrebuje orodja.

Primeri uporabniških zahtev, ki jih lahko agent obdela:

- "Prevedite to Markdown datoteko v korejščino in ohranite pravilne povezave."
- "Prevedite to Markdown datoteko v korejščino z delovnim tokom MCP, ki ga pomaga agent, in uporabite vaš lasten model za prevedene dele."
- "Prevedite ta zvezek v korejščino, ohranite celice s kodo in uporabite Co-op Translator MCP za ponovno sestavljanje zvezka."
- "Prevedite besedilo na tej sliki v japonščino in shranite rezultat."
- "Naredite suhi zagon prevajanja repozitorija v španščino in povejte, kaj bi se spremenilo."
- "Preverite, ali je izhod korejskega prevoda posodobljen."

Za Markdown in zvezke lahko MCP deluje v dveh načinih:

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

Prevajanje repozitorija je privzeto izvedeno kot suhi zagon preko MCP:

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

Primerno za:

- Želite poteke prevajanja v naravnem jeziku znotraj agenta ali urejevalnika.
- Želite prevajanje Markdowna ali zvezkov, kjer gostiteljski agentni model prevaja pripravljene kose.
- Želite, da agent prevede izbrano vsebino namesto celotnega repozitorija.
- Želite korak odobritve pred pisanjem po celotnem repozitoriju.
- Želite en vmesnik, ki ponuja orodja za Markdown, zvezke, slike, pregled in prepisovanje poti.

## Kako se povezujejo

CLI je najboljša privzeta izbira za ljudi, ki prevajajo repozitorije. Python API je najboljši, ko vaša koda upravlja potek dela. MCP strežnik je najboljši, ko agent ali urejevalnik upravlja potek dela.

Vse tri poti uporabljajo isti javni Co-op Translator API, zato lahko začnete z CLI, kasneje avtomatizirate z Pythonom in iste zmožnosti izpostavite MCP odjemalcem, kadar potrebujete poteke dela, ki jih poganjajo agenti.