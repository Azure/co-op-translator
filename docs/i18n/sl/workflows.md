# Izberite svoj delovni tok

Co-op Translator je mogoče uporabljati na tri načine: CLI, Python API in MCP strežnik. Vsi ponujajo enake možnosti prevajanja, a vsak ustreza drugačnemu poteku dela.

Uporabite to stran, ko se odločate, kje začeti.

**Če urejate prevode ročno:** privzeta dela z CLI in Actions ponovno prevedeta spremenjene izvorne datoteke v celoti, zato se lahko vaša besedila v teh datotekah prepišejo. Pred sprejetjem posodobitve preglejte razliko. Za ohranjanje blokovne strukture Markdown pri sprejetih uredbah uporabite izbirni [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Hitra odločitev

| Če želite... | Uporabite | Začnite tukaj |
| --- | --- | --- |
| Prevajati ali pregledovati repozitorij iz terminala | CLI | [CLI Reference](cli.md) |
| Dodati prevajanje v Python skripto, storitev, zvezek (notebook) ali CI opravilo | Python API | [Python API](api.md) |
| Dovolite agentu, urejevalniku ali MCP-kompatibilnemu odjemalcu, da za vas prevede vsebino | MCP Server | [MCP Server](mcp.md) |
| Prevesti en Markdown dokument, zvezek ali sliko, ki jih je vaša aplikacija že naložila | Python API ali MCP Server | [Python API](api.md) ali [MCP Server](mcp.md) |
| Prevesti celoten repozitorij s standardnimi izhodnimi mapami in metapodatki | CLI ali `run_translation` | [CLI Reference](cli.md) ali [Python API](api.md) |

## Uporabite CLI, ko

Izberite CLI, kadar oseba ali CI opravilo vodi prevajanje repozitorija iz ukazne vrstice.

CLI je najbolj neposredna pot, kadar želite, da Co-op Translator poišče projektne datoteke, ustvari prevedene izhode, ohrani postavitev projekta, posodobi metapodatke in izvede ukaze za pregled.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Ta primer prevaja Markdown in zvezke. Dodajte `-img` šele po konfiguraciji [Azure AI Vision](configuration.md#azure-ai-vision). Za prvi zagon samo z Markdown sledite [Vašemu prvemu prevodu](first-translation.md).

Primerna uporaba:

- Prevajate repozitorij iz ukazne vrstice.
- Želite ponovljiv ukaz za CI ali poteke izdaje.
- Želite vgrajeno odkrivanje projektov, izhodne poti, metapodatke, čiščenje in pregled.
- Raje imate ukazni vmesnik kot pisanje Python kode.

## Uporabite Python API, ko

Izberite Python API, kadar naj potek dela nadzoruje vaša koda.

API je uporaben za aplikacije, avtomatizirane skripte, zvezke, storitve in prilagojene cevovode (pipelines). Omogoča klic nizkonivojskih API-jev za prevajanje vsebine za posamezne datoteke ali izvajanje iste orkestracije na ravni repozitorija, kot jo uporablja CLI.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Primerna uporaba:

- Vaša aplikacija že bere datoteke, medpomnilnike, zvezke ali bajte slik.
- Potrebujete prilagojeno validacijo, shranjevanje, beleženje, ponovitve ali postopke odobritve.
- Želite prevesti en dokument, zvezek ali sliko, ne da bi obdelali celoten repozitorij.
- Želite prevajanje repozitorija, vendar iz Pythona (avtomatizacija) namesto prek ukazne vrstice.

## Uporabite MCP strežnik, ko

Izberite MCP strežnik, kadar naj agent, urejevalnik ali MCP-kompatibilen odjemalec kliče orodja Co-op Translatorja.

V običajni lokalni postavitvi uporabnik strežnika ne pusti stalno zagnanega. MCP odjemalec zažene `co-op-translator-mcp` prek `stdio`, ko potrebuje orodja.

Primeri zahtev uporabnika, ki bi jih lahko obdelal agent:

- "Prevedite to Markdown datoteko v korejščino in poskrbite, da bodo povezave pravilne."
- "Prevedite to Markdown datoteko v korejščino z agentom podprtim MCP delovnim tokom in uporabite svoj model za prevedene koščke."
- "Prevedite ta zvezek v korejščino, ohranite celice s kodo in uporabite Co-op Translator MCP za obnovo zvezka."
- "Prevedite besedilo na tej sliki v japonščino in shranite rezultat."
- "Naredite suhi zagon prevajanja repozitorija v španščino in povejte, kaj bi se spremenilo."
- "Preverite, ali je korejski prevod ažuren."

Za Markdown in zvezke lahko MCP deluje v dveh načinih:

| Način | Uporabite, kadar | Glavna orodja |
| --- | --- | --- |
| S pomočjo agenta | Ko naj gostiteljski agent MCP prevede koščke z lastnim modelom, brez poverilnic LLM ponudnika Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Podprto s strani ponudnika | Co-op Translator naj neposredno kliče Azure OpenAI, OpenAI ali Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Oblika klica orodja MCP za Markdown pri podpori ponudnika:

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

MCP oblika klica orodja za slike:

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

Primerna uporaba:

- Želite prevajalske poteke dela v naravnem jeziku znotraj agenta ali urejevalnika.
- Želite prevajanje Markdowna ali zvezkov, kjer model gostiteljskega agenta prevaja pripravljene koščke.
- Želite, da agent prevede izbrano vsebino namesto celotnega repozitorija.
- Želite korak odobritve pred pisanjem v celoten repozitorij.
- Želite en vmesnik, ki nudi orodja za Markdown, zvezke, slike, pregled in prepisovanje poti.

## Kako se ujemajo

CLI je najboljša privzeta izbira za ljudi, ki prevajajo repozitorije. Python API je najboljši, kadar vaša koda nadzoruje potek dela. MCP strežnik je najboljši, kadar potek dela nadzoruje agent ali urejevalnik.

Vse tri poti uporabljajo isti javni Co-op Translator API, zato lahko začnete s CLI, pozneje avtomatizirate s Pythonom in iste zmogljivosti ponudite MCP odjemalcem, ko potrebujete poteke, ki jih vodijo agenti.