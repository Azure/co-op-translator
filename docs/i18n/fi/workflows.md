# Valitse työnkulku

Co-op Translatoria voi käyttää kolmella tavalla: CLI, Python API ja MCP-palvelin. Niillä on samat käännösominaisuudet, mutta kukin sopii eri työnkulkuun.

Käytä tätä sivua, kun päätät, mistä aloittaa.

**If you edit translations by hand:** oletuksena CLI- ja Actions-työnkulut uudelleenkääntävät muutetut lähdetiedostot kokonaan, joten tekstisi näissä tiedostoissa voi ylikirjoittua. Tarkista diff ennen päivityksen hyväksymistä. Hyväksyttyjen muokkausten Markdown-lohkotason säilyttämiseen käytä valinnaista [Python API:n käännystilan tarjoaja](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Nopea päätös

| Jos haluat... | Käytä | Aloita tästä |
| --- | --- | --- |
| Käännä tai tarkista repositorio terminaalista | CLI | [CLI Reference](cli.md) |
| Lisää käännös Python-skriptiin, palveluun, notebookiin tai CI-tehtävään | Python API | [Python API](api.md) |
| Anna agentin, editorin tai MCP-yhteensopivan asiakkaan kääntää sisältö puolestasi | MCP Server | [MCP Server](mcp.md) |
| Käännä yksi Markdown-dokumentti, notebook tai kuva, jonka sovelluksesi on jo ladannut | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Käännä koko repositorio standardeilla tulostuskansioilla ja metatiedoilla | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Käytä CLI:tä, kun

Valitse CLI, kun henkilö tai CI-tehtävä suorittaa repositorion käännöksen komentoriviltä.

CLI on suorin reitti, kun haluat Co-op Translatorin löytävän projektitiedostot, luovan käännetyt tulosteet, säilyttävän projektin rakenteen, päivittävän metatiedot ja suorittavan tarkastuskäskyt.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Tämä esimerkki kääntää Markdownin ja notebookit. Lisää `-img` vasta kun olet määrittänyt [Azure AI Vision](configuration.md#azure-ai-vision). Markdownia koskevaa ensimmäistä ajoa varten seuraa ohjetta [Ensimmäinen käännöksesi](first-translation.md).

Sopii hyvin:

- Käännät repositoriota komentoriviltä.
- Haluat toistettavan komennon CI- tai julkaisutyönkulkuihin.
- Haluat sisäänrakennetun projektin etsinnän, tulostuspolut, metatiedot, siivouksen ja tarkastuksen.
- Suosit komentoriviä Python-koodin kirjoittamisen sijaan.

## Käytä Python API:ta, kun

Valitse Python API, kun oma koodisi hallinnoi työnkulkua.

API on hyödyllinen sovelluksille, automaatioskripteille, notebookeille, palveluille ja räätälöidyille putkistoille. Sen avulla voit kutsua alhaisen tason sisältökäännös-APIt yksittäisille tiedostoille tai suorittaa saman repositoriotason orkestroinnin, jota CLI käyttää.

Käännä yksi Markdown-dokumentti ja päätä, mihin tallennat sen:

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Sopii hyvin:

- Sovelluksesi lukee jo tiedostoja, puskureita, notebookeja tai kuvadataa.
- Tarvitset mukautettua validointia, tallennusta, lokitusta, uudelleenyrityksiä tai hyväksyntäprosesseja.
- Haluat kääntää yhden dokumentin, notebookin tai kuvan käsittelemättä koko repositiota.
- Haluat repositorion käännöksen, mutta Python-automaatiossa komentorivin sijaan.

## Käytä MCP-palvelinta, kun

Valitse MCP-palvelin, kun agentin, editorin tai MCP-yhteensopivan asiakkaan pitäisi kutsua Co-op Translator -työkaluja.

Tavallisessa paikallisessa asetuksessa käyttäjä ei pidä palvelinta jatkuvasti käynnissä manuaalisesti. MCP-asiakas käynnistää `co-op-translator-mcp` `stdio`-yhteyden kautta tarvittaessa.

Esimerkkejä käyttäjäpyynnöistä, joita agentti voisi käsitellä:

- "Käännä tämä Markdown-tiedosto koreaksi ja pidä linkit oikein."
- "Käännä tämä Markdown-tiedosto koreaksi agentin avustamassa MCP-työnkulussa, käyttäen omaa malliasi käännetyille lohkoille."
- "Käännä tämä notebook koreaksi, säilytä koodisolut ja käytä Co-op Translator MCP:tä notebookin uudelleenrakentamiseen."
- "Käännä tämän kuvan teksti japaniksi ja tallenna tulos."
- "Tee kuiva-ajo repositorion käännöksestä espanjaksi ja kerro, mitä muuttuisi."
- "Tarkista, onko koreankielinen käännöstulos ajan tasalla."

Markdownien ja notebookien osalta MCP voi toimia kahdessa tilassa:

| Tila | Käytä kun | Päätyökalut |
| --- | --- | --- |
| Agentin avustama | MCP-isäntäagentin pitäisi kääntää lohkoja omalla mallillaan ilman Co-op Translatorin LLM-palveluntarjoajan tunnuksia. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Palveluntarjoajan tukema | Co-op Translatorin pitäisi kutsua Azure OpenAI:ta, OpenAI:ta tai Anthropicia suoraan. | `translate_markdown_content`, `translate_notebook_content` |

MCP:n tarjoajapohjaisen Markdown-työkalukutsun muoto:

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

MCP:n kuvatyökalukutsun muoto:

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

Repositorion käännös ajetaan oletusarvoisesti kuiva-ajona MCP:n kautta:

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

- Haluat luonnolliskielisiä käännöstyönkulkuja agentin tai editorin sisään.
- Haluat Markdown- tai notebook-käännöksiä, joissa isäntäagentin malli kääntää esivalmistellut lohkot.
- Haluat agentin kääntävän valitun sisällön koko repositorion sijaan.
- Haluat hyväksyntävaiheen ennen koko repositorion kattavia kirjoituksia.
- Haluat yhden käyttöliittymän, joka tarjoaa Markdown-, notebook-, kuva-, tarkastus- ja polkujen uudelleenkirjoitus-työkalut.

## Miten ne sopivat yhteen

CLI on paras oletus ihmisille, jotka kääntävät repositorioita. Python API on paras, kun koodisi hallitsee työnkulkua. MCP-palvelin on paras, kun agentti tai editori hallinnoi työnkulkua.

Kaikki kolme reittiä käyttävät samaa julkista Co-op Translator API:a, joten voit aloittaa CLI:llä, automatisoida myöhemmin Pythonilla ja tarjota samat mahdollisuudet MCP-asiakkaille, kun tarvitset agenttiohjattuja työnkulkuja.