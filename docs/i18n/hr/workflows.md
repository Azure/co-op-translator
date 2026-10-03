# Odaberite svoj radni tijek

Co-op Translator se može koristiti na tri načina: CLI, Python API i MCP server. Dijele iste mogućnosti prevođenja, ali svaki odgovara drugačijem radnom tijeku.

Koristite ovu stranicu kada odlučujete gdje započeti.

**Ako ručno uređujete prijevode:** zadani CLI i Actions radni tijekovi ponovno prevode promijenjene izvorne datoteke u cjelini, pa se vaša formulacija u tim datotekama može prebrisati. Pregledajte razliku (diff) prije prihvaćanja ažuriranja. Za očuvanje prihvaćenih izmjena na razini Markdown blokova koristite opcionalni [Python API pružatelj stanja prijevoda](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Brza odluka

| Ako želite... | Upotrijebite | Počnite ovdje |
| --- | --- | --- |
| Prevesti ili pregledati spremište iz terminala | CLI | [Referenca za CLI](cli.md) |
| Dodati prijevod u Python skriptu, servis, bilježnicu (notebook) ili CI posao | Python API | [Python API](api.md) |
| Neka agent, uređivač ili MCP-kompatibilni klijent prevede sadržaj umjesto vas | MCP Server | [MCP Server](mcp.md) |
| Prevesti jedan Markdown dokument, bilježnicu ili sliku koju je vaša aplikacija već učitala | Python API ili MCP Server | [Python API](api.md) ili [MCP Server](mcp.md) |
| Prevesti cijelo spremište s uobičajenim izlaznim mapama i metapodacima | CLI or `run_translation` | [Referenca za CLI](cli.md) or [Python API](api.md) |

## Koristite CLI kada

Odaberite CLI kada osoba ili CI posao pokreće prevođenje spremišta iz terminala.

CLI je najizravniji put kada želite da Co-op Translator otkrije projektne datoteke, stvori prevedene izlaze, očuva raspored projekta, ažurira metapodatke i pokrene naredbe za pregled.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Ovaj primjer prevodi Markdown i bilježnice. Dodajte `-img` tek nakon konfiguriranja [Azure AI Vision](configuration.md#azure-ai-vision). Za prvo pokretanje samo za Markdown slijedite [Vaš prvi prijevod](first-translation.md).

Prikladno za:

- Prevodite spremište iz terminala.
- Želite ponovljivu naredbu za CI ili release radne tijekove.
- Želite ugrađeno otkrivanje projekta, izlazne puteve, metapodatke, čišćenje i pregled.
- Dajete prednost naredbenom sučelju umjesto pisanju Python koda.

## Koristite Python API kada

Odaberite Python API kada vaš kod treba kontrolirati radni tijek.

API je koristan za aplikacije, automatizirane skripte, bilježnice, servise i prilagođene pipelineove. Omogućuje pozivanje niskorazinskih API-ja za prevođenje sadržaja za pojedinačne datoteke ili pokretanje iste orkestracije na razini spremišta koju koristi CLI.

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

Pokrenite prevođenje spremišta iz Pythona:

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

Prikladno za:

- Vaša aplikacija već čita datoteke, buffere, bilježnice ili bajtove slike.
- Potrebna vam je prilagođena validacija, pohrana, zapisivanje (logging), ponovna pokušavanja ili tokovi odobravanja.
- Želite prevesti jedan dokument, bilježnicu ili sliku bez obrade cijelog spremišta.
- Želite prevođenje spremišta, ali iz Python automatizacije umjesto naredbe u shellu.

## Koristite MCP Server kada

Odaberite MCP server kada agent, uređivač ili MCP-kompatibilni klijent treba pozvati Co-op Translator alate.

U normalnoj lokalnoj konfiguraciji korisnik ne održava server ručno. MCP klijent pokreće `co-op-translator-mcp` preko `stdio` kada mu trebaju alati.

Primjeri korisničkih zahtjeva koje bi agent mogao obraditi:

- "Prevedi ovu Markdown datoteku na korejski i zadrži ispravne poveznice."
- "Prevedi ovu Markdown datoteku na korejski koristeći MCP radni tijek uz pomoć agenta, koristeći vlastiti model za prevedene dijelove."
- "Prevedi ovu bilježnicu na korejski, sačuvaj kodne ćelije i upotrijebi Co-op Translator MCP za rekonstrukciju bilježnice."
- "Prevedi tekst na ovoj slici na japanski i spremi rezultat."
- "Napravite probno (dry-run) prevođenje spremišta na španjolski i recite mi što bi se promijenilo."
- "Provjeri je li izlaz korejskog prijevoda ažuriran."

Za Markdown i bilježnice, MCP može raditi na dva načina:

| Način | Koristi se kada | Glavni alati |
| --- | --- | --- |
| Agent-assisted | Domaćinski MCP agent treba prevesti dijelove vlastitim modelom, bez vjerodajnica pružatelja LLM-a Co-op Translatora. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator bi trebao izravno pozivati Azure OpenAI, OpenAI ili Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Oblik poziva alata za Markdown podržanog MCP providerom:

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

Prevođenje spremišta putem MCP-a je po zadanom probno (dry-run):

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

Prikladno za:

- Želite radne tijekove prevođenja u prirodnom jeziku unutar agenta ili uređivača.
- Želite prevođenje Markdowna ili bilježnica gdje domaćinski agentov model prevodi pripremljene dijelove.
- Želite da agent prevede odabrani sadržaj umjesto cijelog spremišta.
- Želite korak odobrenja prije upisa promjena u cijelo spremište.
- Želite sučelje koje izlaže alate za Markdown, bilježnice, slike, pregled i prepisivanje putanja.

## Kako se uklapaju

CLI je najbolji zadani izbor za ljude koji prevode spremišta. Python API je najbolji kada vaš kod upravlja radnim tijekom. MCP server je najbolji kada agent ili uređivač upravlja radnim tijekom.

Sva tri puta koriste isti javni Co-op Translator API, pa možete započeti s CLI-jem, kasnije automatizirati s Pythonom i izložiti iste mogućnosti MCP klijentima kad trebate radne tijekove kojima upravlja agent.