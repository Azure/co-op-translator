# Valitse työnkulku

Co-op Translatoria voi käyttää kolmella tavalla: CLI, Python API ja MCP-palvelin. Niillä on samat käännösominaisuudet, mutta kukin sopii eri työnkulkuun.

Käytä tätä sivua, kun päätät, mistä aloittaa.

## Nopea päätös

| Jos haluat... | Käytä | Start here |
| --- | --- | --- |
| Kääntää tai tarkistaa repositorion terminaalista | CLI | [CLI Reference](cli.md) |
| Lisätä käännöksen Python-skriptiin, palveluun, muistioon tai CI-tehtävään | Python API | [Python API](api.md) |
| Anna agentin, editorin tai MCP-yhteensopivan asiakkaan kääntää sisältö puolestasi | MCP Server | [MCP Server](mcp.md) |
| Kääntää yhden Markdown-asiakirjan, muistion tai kuvan, jonka sovelluksesi on jo ladannut | Python API tai MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Kääntää koko repositorion käyttäen standardeja tulostuskansioita ja metatietoja | CLI tai `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Käytä CLI:tä, kun

Valitse CLI, kun henkilö tai CI-tehtävä käynnistää repositorion käännöksen kuoresta.

CLI on suorin tapa, kun haluat, että Co-op Translator löytää projektitiedostot, luo käännetyt tulosteet, säilyttää projektin rakenteen, päivittää metatiedot ja suorittaa tarkistuskomennot.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Sopii hyvin:

- Käännät repositorion terminaalista.
- Haluat toistettavan komennon CI- tai julkaisuputkiin.
- Haluat sisäänrakennetun projektin etsinnän, tulostuspolut, metatiedot, siivouksen ja tarkistustoiminnot.
- Haluat komentorajapinnan mieluummin kuin kirjoittaa Python-koodia.

## Käytä Python-APIa, kun

Valitse Python-API, kun oma koodisi hallitsee työnkulkua.

API on hyödyllinen sovelluksille, automaatioskripeille, muistioille, palveluille ja mukautetuille putkille. Sen avulla voit kutsua matalan tason sisältökäännös-API:a yksittäisille tiedostoille tai suorittaa saman repositoriotason orkestroinnin, jota CLI käyttää.

Käännä yksi Markdown-asiakirja ja päätä, mihin tallennat sen:

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

Suorita repositorion käännös Pythonista:

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

Sopii hyvin:

- Sovelluksesi lukee jo tiedostoja, puskureita, muistioita tai kuvan tavuja.
- Tarvitset mukautettua validointia, tallennusta, lokitusta, uudelleentyrityksiä tai hyväksyntäprosesseja.
- Haluat kääntää yhden asiakirjan, muistion tai kuvan käsittelemättä koko repositoriota.
- Haluat repositorion käännöksen, mutta Python-automaatioista sen sijaan että käyttäisit kuorikomentoa.

## Käytä MCP-palvelinta, kun

Valitse MCP-palvelin, kun agentin, editorin tai MCP-yhteensopivan asiakkaan tulisi kutsua Co-op Translatorin työkaluja.

Normaalissa paikallisessa asetuksessa käyttäjä ei pidä palvelinta käynnissä manuaalisesti. MCP-asiakas käynnistää `co-op-translator-mcp` `stdio`n yli, kun se tarvitsee työkaluja.

Esimerkkejä käyttäjän pyynnöistä, joita agentti voisi käsitellä:

- "Käännä tämä Markdown-tiedosto koreaksi ja pidä linkit oikein."
- "Käännä tämä Markdown-tiedosto koreaksi agentin avustamassa MCP-työnkulussa, käyttäen omaa malliasi käännetyille osioille."
- "Käännä tämä muistio koreaksi, säilytä koodisolut ja käytä Co-op Translator MCP:tä kootaksesi muistion uudelleen."
- "Käännä tämän kuvan teksti japaniksi ja tallenna tulos."
- "Suorita kuiva-ajona repositorion käännös espanjaksi ja kerro, mitä muuttuisi."
- "Tarkista, onko koreankielinen käännös ajantasainen."

Markdownin ja muistioiden osalta MCP voi toimia kahdessa tilassa:

| Tila | Käytä kun | Päätyökalut |
| --- | --- | --- |
| Agentin avustama | MCP-isäntäagentin tulisi kääntää osiot omalla mallillaan ilman Co-op Translatorin LLM-palveluntarjoajan tunnuksia. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Palveluntarjoajan tukema | Co-op Translatorin tulisi kutsua Azure OpenAI:ta tai OpenAI:ta suoraan. | `translate_markdown_content`, `translate_notebook_content` |

MCP:n palveluntarjoajan tukema Markdown-työkalukutsu:

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

MCP-kuvatyökalukutsun muoto:

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

Repositorion käännös ajetaan oletuksena kuiva-ajona MCP:n kautta:

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

Sopii hyvin:

- Haluat luonnollisen kielen käännöstyönkulkuja agentin tai editorin sisällä.
- Haluat Markdown- tai muistion käännöksen, jossa isäntäagentin malli kääntää valmiit osiot.
- Haluat agentin kääntävän valitun sisällön koko repositorion sijaan.
- Haluat hyväksyntävaiheen ennen koko repositorion laajuisten kirjoitusten tekemistä.
- Haluat yhden rajapinnan, joka tarjoaa Markdown-, muistio-, kuva-, tarkistus- ja polun uudelleenkirjoitustyökaluja.

## Miten ne sopivat yhteen

CLI on paras oletus ihmisille, jotka kääntävät repositorioita. Python-API on paras, kun koodisi hallinnoi työnkulkua. MCP-palvelin on paras, kun agentti tai editori hallitsee työnkulkua.

Kaikki kolme polkua käyttävät samaa julkista Co-op Translator -API:a, joten voit aloittaa CLI:llä, automatisoida myöhemmin Pythonilla ja tarjota samat ominaisuudet MCP-asiakkaille, kun tarvitset agenttiohjattuja työnkulkuja.