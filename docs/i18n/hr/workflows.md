# Odaberite svoj tijek rada

Co-op Translator se može koristiti na tri načina: CLI, Python API i MCP server. Dijele iste mogućnosti prevođenja, ali svaki odgovara drugačijem tijeku rada.

Upotrijebite ovu stranicu kada odlučujete gdje početi.

## Brza odluka

| Ako želite... | Koristite | Počnite ovdje |
| --- | --- | --- |
| Prevesti ili pregledati repozitorij iz terminala | CLI | [CLI referenca](cli.md) |
| Dodati prijevod u Python skriptu, servis, bilježnicu ili CI zadatak | Python API | [Python API](api.md) |
| Neka agent, uređivač ili MCP-kompatibilni klijent prevede sadržaj za vas | MCP Server | [MCP Server](mcp.md) |
| Prevesti jedan Markdown dokument, bilježnicu ili sliku koji je vaša aplikacija već učitala | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Prevesti čitav repozitorij s uobičajenim izlaznim mapama i metapodacima | CLI or `run_translation` | [CLI referenca](cli.md) or [Python API](api.md) |

## Koristite CLI kada

Odaberite CLI kada osoba ili CI zadatak pokreće prevođenje repozitorija iz terminala.

CLI je najizravniji put kada želite da Co-op Translator otkrije datoteke projekta, stvori prevedene izlaze, sačuva strukturu projekta, ažurira metapodatke i pokrene naredbe za pregled.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Dobro odgovara:

- Prevodi­te repozitorij iz terminala.
- Želite ponovljivu naredbu za CI ili release tijekove rada.
- Želite ugrađeno otkrivanje projekta, izlazne putanje, metapodatke, čišćenje i pregled.
- Preferirate sučelje naredbenog retka umjesto pisanja Python koda.

## Koristite Python API kada

Odaberite Python API kada vaš kod treba kontrolirati tijek rada.

API je koristan za aplikacije, automatizirane skripte, bilježnice, servise i prilagođene pipelineove. Omogućuje vam pozivanje niskorazinskih API-ja za prevođenje sadržaja za pojedinačne datoteke ili pokretanje iste orkestracije na razini repozitorija koju koristi CLI.

Prevedite jedan Markdown dokument i odlučite gdje ga spremiti:

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

Pokrenite prevođenje repozitorija iz Pythona:

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

Dobro odgovara:

- Vaša aplikacija već čita datoteke, buffere, bilježnice ili bajtove slike.
- Trebate prilagođenu validaciju, pohranu, evidentiranje, ponovne pokušaje ili tokove odobravanja.
- Želite prevesti jedan dokument, bilježnicu ili sliku bez obrade čitavog repozitorija.
- Želite prevođenje repozitorija, ali iz Python automatizacije umjesto naredbe u terminalu.

## Koristite MCP Server kada

Odaberite MCP server kada agent, uređivač ili MCP-kompatibilni klijent treba pozvati alate Co-op Translatora.

U uobičajenoj lokalnoj postavci korisnik ne pokreće ručno server. MCP klijent pokreće `co-op-translator-mcp` preko `stdio` kada mu trebaju alati.

Primjeri korisničkih zahtjeva koje bi agent mogao obraditi:

- "Prevedite ovu Markdown datoteku na korejski i zadržite ispravne poveznice."
- "Prevedite ovu Markdown datoteku na korejski s MCP tijek rada uz pomoć agenta, koristeći vlastiti model za prevedene dijelove."
- "Prevedite ovu bilježnicu na korejski, sačuvajte ćelije s kodom i upotrijebite Co-op Translator MCP za rekonstrukciju bilježnice."
- "Prevedite tekst na ovoj slici na japanski i spremite rezultat."
- "Izvedite probni (dry-run) prijevod repozitorija na španjolski i recite mi što bi se promijenilo."
- "Provjerite je li korejski prijevod ažuran."

Za Markdown i bilježnice, MCP može raditi u dva načina rada:

| Način | Koristite kada | Glavni alati |
| --- | --- | --- |
| Uz pomoć agenta | Kada MCP host agent treba prevesti dijelove koristeći vlastiti model, bez vjerodajnica Co-op Translator LLM providera. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Podržano od providera | Kada Co-op Translator treba izravno pozvati Azure OpenAI ili OpenAI. | `translate_markdown_content`, `translate_notebook_content` |

Oblik poziva Markdown alata za MCP s podrškom providera:

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

Oblik poziva za MCP alat za slike:

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

Po zadanim postavkama, prevođenje repozitorija putem MCP-a je probni (dry-run):

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

Dobro odgovara:

- Želite tijekove rada za prevođenje na prirodnom jeziku unutar agenta ili uređivača.
- Želite prevođenje Markdowna ili bilježnica gdje model host agenta prevodi pripremljene dijelove.
- Želite da agent prevede odabrani sadržaj umjesto cijelog repozitorija.
- Želite korak odobrenja prije pisanja po cijelom repozitoriju.
- Želite jedno sučelje koje izlaže alate za Markdown, bilježnice, slike, pregled i prepisivanje putanja.

## Kako se uklapaju

CLI je najbolji zadani izbor za ljude koji prevode repozitorije. Python API je najbolji kada vaš kod upravlja tijekom rada. MCP server je najbolji kada agent ili uređivač upravlja tijekom rada.

Sva tri pristupa koriste isti javni Co-op Translator API, pa možete početi s CLI-jem, kasnije automatizirati s Pythonom i izložiti iste mogućnosti MCP klijentima kada trebate tijekove rada vođene agentom.