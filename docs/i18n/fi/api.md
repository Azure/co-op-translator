# Python-API

Julkinen, vakaa Python-API viedään moduulista `co_op_translator.api`. Useimmat integraatiot käyttävät jotakin näistä työnkuluista:

| Tapaus | Käytä tätä kun | Pää-API:t |
| --- | --- | --- |
| Käännä yksittäisiä tiedostoja tai asiakirjoja | Sovelluksesi lukee lähdesisällön, kutsuu Co-op Translatoria käännöstä varten ja päättää, mihin tulos tallennetaan. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Valmistele sisältö isäntäagentin käännöstä varten | MCP-isäntäsi tai sovellusmallisi kääntää paloja, kun taas Co-op Translator huolehtii paloituksesta ja uudelleenrakennuksesta. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Käännä koko repositorio | Haluat, että Python-API käyttäytyy kuten CLI ja hoitaa tiedostojen löydön, tulostuspolut, metatiedot, siivouksen ja kirjoitukset. | `run_translation` |

Suurin osa alemman tason moduuleista `core`-, `config`-, `review`- ja `utils`-hakemistoissa on toteutusyksityiskohtia, joita nämä API-päätepisteet käyttävät.

MCP-asiakkaat käyttävät samaa julkista API:a [MCP-palvelin](mcp.md) kautta. Käytä tätä sivua kutsuessasi Pythonia suoraan, ja MCP-opasta kun altistat Co-op Translatorin agentille tai editorille. Jos olet päättämässä CLI:n, Python-API:n ja MCP:n välillä, aloita kohdasta [Valitse työnkulku](workflows.md).

## Ensimmäisen käyttökerran API-työnkulku

Aloita tästä, jos kutsut Co-op Translatoria Python-koodista:

1. Määritä LLM-palveluntarjoaja kuten on kuvattu kohdassa [Konfigurointi](configuration.md), ellei tarkoituksesi ole vain valmistella Markdown- tai notebook-paloja isäntäagentin käännöstä varten.
2. Päätä, hoitaako sovelluksesi tiedosto-I/O:n.
3. Käytä sisältö-APIja, kun sovelluksesi lukee ja kirjoittaa yksittäisiä tiedostoja.
4. Käytä `run_translation`, kun Co-op Translatorin tulee käsitellä repositorio kuten CLI.
5. Käytä `run_review` käännöksen jälkeen, jos tarvitset deterministisiä tarkistuksia automaatiossa.

| Tavoite | Aloitus-API |
| --- | --- |
| Käännä yksi Markdown-merkkijono tai tiedosto | `translate_markdown_content` |
| Käännä yksi notebook-sisältö | `translate_notebook_content` |
| Käännä yksi kuva | `translate_image_content` |
| Anna isäntäagentin kääntää Markdown- tai notebook-paloja | `start_markdown_agent_translation` tai `start_notebook_agent_translation` |
| Kirjoita uudelleen käännetyt linkit valitun tulostuspolun jälkeen | `rewrite_markdown_paths` tai `rewrite_notebook_paths` |
| Käännä koko repositorio | `run_translation` |
| Tarkista käännetty tulos | `run_review` |

## Tapaus 1: Käännä yksittäisiä tiedostoja tai asiakirjoja

Käytä tätä työnkulkua, kun sinulla on jo tiedosto, editorin muistinpuskuri, notebook-kuorma, MCP-pyyntö tai mukautetun putken syöte. Koodisi vastaa tiedosto-I/O:sta:

1. Lue lähdesisältö.
2. Kutsu sisältöjen käännös-APIa.
3. Valinnaisesti kutsu polkujen uudelleenkirjoitus-APIa, jos käännetty sisältö kirjoitetaan projekti-käännöskansioon.
4. Tallenna tai palauta tulos sovelluksestasi.

Sisällön käännös-API:t eivät suorita projektin löytöä, eivät kirjoita metatietoja, eivät lisää vastuuvapauslausekkeita eikä uudelleenkirjoita linkkejä automaattisesti.

### Markdown-tiedosto

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Jos käännetty Markdown ei tule osaksi Co-op Translatorin projektirakennetta, ohita `rewrite_markdown_paths` ja tallenna käännetty merkkijono suoraan.

### Notebook-tiedosto

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` kääntää Markdown-solut ja säilyttää ei-Markdown-solut. Polkujen uudelleenkirjoitus kohdistuu vain Markdown-soluihin.

### Kuvatiedosto

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` lukee lähdekuvan ja palauttaa renderöidyn `PIL.Image.Image`-olion. Se ei kirjoita käännetyn kuvan metatietoja.

## Tapaus 2: Käännä koko repositorio

Käytä tätä työnkulkua, kun haluat Python-API:n käyttäytyvän kuten `translate`-CLI. `run_translation` löytää tuetut tiedostot, kääntää valitut sisältötyypit, uudelleenkirjoittaa polut, kirjoittaa tulostiedostot, päivittää metatiedot ja suorittaa käännöksen ylläpitotehtäviä kuten siivouksen.

`run_translation` on suositeltu projekti-orchestrointin päätepiste. `translate_project` viedään yhteensopivuusaliasina samalla käyttäytymisellä.

Käännä Markdown-tiedostot nykyisessä repositoriossa koreaksi ja japaniksi:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Käännä vain notebook-tiedostoja tietystä projektin juurihakemistosta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Esikatsele käännösmäärää ilman tiedostojen kirjoittamista:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Tallenna jäsenneltyjä etenemistapahtumia integraatiota varten:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Tallenna hyötykuorma työn tapahtumatauluun tai suoratoista se käyttöliittymääsi.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Tapahtumat käyttävät versionoitua skeemaa `co-op.translation.event.v1`. Integraatioiden tulisi nojautua vakaisiin kenttiin kuten `type` ja `stage_key`, ei ihmislukuisaan konsolitekstiin tai `stage_label`.



Käännä useita sisältöjuuria yhdellä kutsulla:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Kirjoita käännökset eksplisiittisiin tulosryhmiin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Käytä kielikohtaista paikkamerkkiä, kun jokaisen kielen alla tulee olla upotettu alihakemisto:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Jos mikään `markdown`, `notebook` tai `images` ei ole asetettu, API kääntää kaikki tuetut tyypit: Markdown, notebookit ja kuvat.

### Säilytä hyväksytyt ihmismuutokset käännystilan tarjoajalla

Oletuksena Co-op Translator säilyttää nykyisen tiedostotason käyttäytymisensä: kun
Markdown-lähde on vanhentunut, koko käännetty tiedosto generoidaan uudelleen. Isännöidyissä
integraatioissa voidaan valinnaisesti välittää `TranslationStateProvider` säilyttämään ihmisten
muokkauksia lähdeblokeissa, joita ei ole muutettu.

Tarjoaja toimittaa viimeksi hyväksytyn lähde-/kohdeparin ja tallentaa jokaisen uuden
ehdokkaan. Hyväksyminen on edelleen integraation vastuulla—for example,
kun käännöspull-request on yhdistetty:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Markdown-tiedostoille, joilla on voimassa oleva hyväksytty perusta, Co-op Translator kohdistaa
ylimmän tason Markdown-blokit. Muuttumattomat lähdeblokit käyttävät uudelleen nykyisiä käännettyjä
blokkeja, mukaan lukien ihmisten tekemät muokkaukset; muutetut tai lisätyt lähdeblokit lähetetään
käännettäväksi; poistetut lähdeblokit poistetaan. Jos kohdistus on epäselvä,
kohdekokonaisuus muuttui, blokin käännös on virheellinen tai perustaa ei ole
saatavilla, Co-op Translator palaa turvallisesti olemassa olevaan koko-tiedoston
käännöspolkuun.

Tämä API tallentaa dokumentin käännöstilan, ei dokumenttien välistä fraasi- tai
segmenttikäännösmuistia. Se koskee tällä hetkellä Markdown-projektin
käännöksiä. Notebook- ja kuvauskäyttäytyminen pysyy muuttumattomana. `update=True`-parametrin välittäminen
pyytää silti täyttä uudelleengenerointia.

Jos yhtä tai useampaa tiedostoa ei voida kääntää, `run_translation` nostaa
`RuntimeError`-poikkeuksen projektityönkulun päätyttyä sen sijaan, että raportoitaisiin
onnistuneesta suorituksesta puuttuvalla tulostuksella. Integraatioiden tulisi käsitellä tätä epäonnistuneena
työnä ja säilyttää aiempi hyväksytty käännöstila.

## Tarkista käännetty tulos

`run_review` suorittaa deterministisiä käännöstarkistuksia ilman LLM- tai Vision-tunnuksia.

!!! note "Beta"
    `run_review` on beta-vaiheen deterministinen tarkastus-API. Se ei kutsu mallitoimittajia eikä kirjoita tiedostoja, mutta tarkastukset ja ongelmaskeemat saattavat kehittyä.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-tiedostoon rajoitetun käännöksen jälkeen käytä samaa laajuutta tarkistuksessa:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` tarkistaa vain kunkin konfiguroidun lähdejuuren `README.md`-tiedoston,
mukaan lukien mukautetut `groups` ja tulostuskansiot. Muut dokumentit ja sisäkkäiset
README-tiedostot jätetään pois. Puuttuva lähde-README nostaa `ValueError`-poikkeuksen; epäonnistuneet
käännöstarkistukset nostavat `RuntimeError`-poikkeuksen.

Tarkista vain base-refiin verrattuna muuttuneet tiedostot ja tulosta GitHub-muotoinen ulostulo:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Kopioi-liitä API-esimerkit

Käännä Markdown-sisältö ilman tiedostokirjoituksia:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Käännä ja uudelleenkirjoita Markdown-linkit:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Käännä repositorio Pythonista:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Käännä useita juuria:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Säilytä sanaston termit:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Julkiset päätepisteet

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Sisällön käännös-API:t

Sisällön käännös-API:t on tarkoitettu integraatioille, joilla on sisältö jo muistissa, kuten editor-laajennus, MCP-työkalu, notebook-prosessori tai mukautettu putki.

| Funktio | Syöte | Tuloste | Tiedosto-I/O | Huomautukset |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Kääntää vain Markdown-sisällön. Se ei uudelleenkirjoita linkkejä, kirjoita metatietoja tai lisää vastuuvapauslausekkeita. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Kääntää Markdown-solut ja säilyttää ei-Markdown-solut. Se ei uudelleenkirjoita linkkejä, kirjoita metatietoja tai lisää vastuuvapauslausekkeita. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Erottaa ja kääntää kuvan tekstin, minkä jälkeen palauttaa renderöidyn kuvan. Se ei tallenna käännetyn kuvan metatietoja. |

`translate_markdown_content` ja `translate_notebook_content` hyväksyvät valinnaisen `source_path`-vaihtoehdon. Polku välitetään kontekstina kääntäjälle; kutsujat ovat edelleen vastuussa mahdollisesta projektikohtaisesta polkujen uudelleenkirjoituksesta käännöksen jälkeen.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Samat asetukset voidaan välittää sanakirjoina:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agentin avustamat käännös-API:t

Agentin avustamat API:t eivät kutsu Co-op Translatorissa konfiguroitua LLM-palveluntarjoajaa. Ne valmistelevat Markdown- tai notebook-palat isäntäagentin käännettäväksi ja sitten rekonstruoivat lopullisen sisällön käännetyistä paloista.

| Funktio | Tarkoitus |
| --- | --- |
| `start_markdown_agent_translation` | Palauta itsenäinen Markdown-tehtävä paloilla, kehotteilla ja uudelleenrakennustilalla. |
| `finish_markdown_agent_translation` | Uudelleenrakenna Markdown tehtävästä ja isäntäagentin kääntämistä paloista. |
| `start_notebook_agent_translation` | Palauta notebook-tehtävä, jossa on Markdown-solupaloja isäntäagentin käännöstä varten. |
| `finish_notebook_agent_translation` | Uudelleenrakenna notebookin JSON säilyttäen koodisolut, tulosteet ja metatiedot. |

Tämä työnkulku on pääasiassa tarkoitettu MCP-isännille. Jos tarvitset tuotantorepositorion käännöstä siten, että Co-op Translator hallinnoi palveluntarjoajakutsuja, käytä `translate_markdown_content`, `translate_notebook_content` tai `run_translation`.

## Polkujen uudelleenkirjoitus-API:t

Polkujen uudelleenkirjoitus-API:t eivät suorita käännöstä. Ne päivittävät linkkejä ja frontmatter-polkuja sen jälkeen, kun kutsujat tietävät lähdepolun, käännetyn kohdepolun ja projektirakenteen.

| Funktio | Laajuus | Huomautukset |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown-runko ja frontmatter | Uudelleenkirjoittaa Markdown-linkit ja tuetut frontmatter-polukentät käännetylle kohteelle. |
| `rewrite_notebook_paths` | Markdown-solut notebookin JSON:issa | Soveltaa Markdown-polkujen uudelleenkirjoitusta jokaiseen Markdown-soluun ja jättää ei-Markdown-solut muuttumattomiksi. |

`policy`-argumentti voi olla sanakirja, jossa on seuraavat kentät:

| Kenttä | Pakollinen | Tarkoitus |
| --- | --- | --- |
| `language_code` | Kyllä | Kohdekielen koodi, esimerkiksi `"ko"` tai `"pt-BR"`. |
| `root_dir` | Ei | Lähdeprojektin juurihakemisto. Oletuksena `"."`. |
| `translations_dir` | Ei | Tekstikäännösten tulostuskansio. Oletuksena `translations` `root_dir`-hakemiston alla. |
| `translated_images_dir` | Ei | Käännettyjen kuvien tulostuskansio. Oletuksena `translated_images` `root_dir`-hakemiston alla. |
| `translation_types` | Ei | Sallitut käännöstyypit. Oletuksena Markdown, notebookit ja kuvat. |
| `lang_subdir` | Ei | Valinnainen alihakemisto kunkin kielikansion alle. |

## Projektin käännösparametrit

| Parametri | Tyyppi | Oletus | Tarkoitus |
| --- | --- | --- | --- |
| `language_codes` | `str` | Pakollinen | Välilyönnillä erotetut kohdekielikoodit, kuten `"ko ja fr"`, tai `"all"`. Aliaskoodit normalisoidaan kanonisiin BCP 47 -arvoihin. |
| `root_dir` | `str` | `"."` | Projektin juurihakemisto yhdelle käännöskielelle. Ohitetaan, kun `root_dirs` tai `groups` on annettu. |
| `update` | `bool` | `False` | Poista ja luo uudelleen olemassa olevat käännökset valituille kielille. |
| `images` | `bool` | `False` | Sisällytä kuvakäännös. Vaatii Azure AI Vision -konfiguraation. |
| `markdown` | `bool` | `False` | Sisällytä Markdown-käännös. |
| `notebook` | `bool` | `False` | Sisällytä Jupyter-notebook-käännös. |
| `debug` | `bool` | `False` | Ota debug-lokin kirjaus käyttöön. |
| `save_logs` | `bool` | `False` | Tallenna DEBUG-tason lokitiedostot juurihakemiston `logs/`-kansioon. |
| `yes` | `bool` | `True` | Vahvista kehotteet automaattisesti ohjelmallista ja CI-käyttöä varten. |
| `add_disclaimer` | `bool` | `False` | Lisää konekäännöksiä koskevat vastuuvapauslausekkeet käännettyihin Markdown- ja muistikirjatiedostoihin. |
| `translations_dir` | `str \| None` | `None` | Mukautettu tekstikäännösten tuloshakemisto. Suhteelliset polut ratkaistaan kunkin juuren mukaan. |
| `image_dir` | `str \| None` | `None` | Mukautettu käännettyjen kuvien tuloshakemisto. Suhteelliset polut ratkaistaan kunkin juuren mukaan. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Useita juurihakemistoja, jotka jakavat samat ulostuloasetukset. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Nimenomaiset `(root_dir, translations_dir)`-parit. Ylittää `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Arkiston URL, jota käytetään README:n kielitaulukon ohjeistuksen luomiseen. |
| `glossaries` | `Iterable[str] \| None` | `None` | Sanaston termit, jotka säilytetään käännöksen aikana. Päällekkäisyydet ja tyhjät termit normalisoidaan. |
| `dry_run` | `bool` | `False` | Arvioi käännösmäärän ja esikatsele migraatiokäyttäytymistä kirjoittamatta tiedostoja. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Valinnainen accepted-baseline- ja candidate-persistenssisovitin inkrementaalisia Markdown-päivityksiä varten. Jättämällä tämä pois säilyy olemassa oleva kokotiedostokäyttäytyminen. |

## Tarkastusparametrit

`run_review` jäljittelee tarkoituksella `run_translation`-allekirjoitusta aina kun mahdollista, jotta automaatio voi vaihtaa käännös- ja tarkistustyönkulkujen välillä mahdollisimman vähällä haarautumisella.

| Parametri | Tyyppi | Oletus | Tarkoitus |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Tarkastettavat kohdekielihakemistot. Hyväksyy välilyönnillä erotetut merkkijonot ja iteroitavat kokoelmat. `"all"` tarkastaa kaikki löydetyt käännöskielet. |
| `root_dir` | `str` | `"."` | Projektin juurihakemisto yksittäiselle tarkastuskohteelle. Ohitetaan kun `root_dirs` tai `groups` on annettu. |
| `markdown` | `bool` | `False` | Sisällytä Markdown- ja MDX-lähdetiedostot. |
| `notebook` | `bool` | `False` | Sisällytä Jupyter-muistikirjan lähdetiedostot. |
| `images` | `bool` | `False` | Varattu vastaavuuden vuoksi käännösasetusten kanssa. Kuvien linkkiviitteet tarkistetaan Markdownista. |
| `translations_dir` | `str \| None` | `None` | Mukautettu tekstikäännösten tuloshakemisto. Suhteelliset polut ratkaistaan kunkin juuren mukaan. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Useita juurihakemistoja, jotka jakavat samat ulostuloasetukset. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Nimenomaiset `(root_dir, translations_dir)`-parit. Ylittää `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-ref, jota käytetään rajaamaan tarkastus muutettuihin lähdetiedostoihin. |
| `readme_only` | `bool` | `False` | Tarkasta vain kunkin lähdejuuren `README.md`. Puuttuva lähde-README aiheuttaa `ValueError`-poikkeuksen. |
| `output_format` | `str` | `"text"` | Tarkastuksen tulosteen muoto. Tuetut arvot ovat `"text"` ja `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Käsittele varoitukset virheinä virheiden lisäksi. |
| `debug` | `bool` | `False` | Ota debug-kirjaus käyttöön. |
| `save_logs` | `bool` | `False` | Tallenna DEBUG-tason lokitiedostot juurihakemistoon `logs/`. |

If `markdown`, `notebook`, or `images` eivät ole asetettuja, API tarkastaa Markdownit, muistikirjat ja kuvien linkkiviitteet soveltuvin osin. Tarkastus ei kutsu LLM-palveluntarjoajaa eikä vaadi API-avaimia.

## Konfiguraation vaatimukset

Palveluntarjoajaan perustuvat käännös-API:t vaativat palveluntarjoajan konfiguroinnin ennen kääntämistä:

- Markdown- ja muistikirjakäännös vaativat LLM-palveluntarjoajan. Konfiguroi Azure OpenAI, OpenAI tai Anthropic.
- Kuvakäännös vaatii LLM-palveluntarjoajan lisäksi Azure AI Visionin.
- `run_translation` suorittaa kevyet yhteyden tarkistukset ennen projektin käännöksen aloittamista.
- Agentin avulla avustetut `start_*_agent_translation`- ja `finish_*_agent_translation`-APIt eivät kutsu Co-op Translatorin LLM-palveluntarjoajia. Isäntäohjelma tai MCP-agentti kääntää valmistellut palaset.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ja `run_review` ovat deterministisiä eivätkä vaadi palveluntarjoajan tunnistetietoja.

Vaaditut Azure OpenAI -muuttujat:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Vaaditut OpenAI -muuttujat:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Vaaditut Anthropic-muuttujat:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ja `ANTHROPIC_MAX_TOKENS` ovat valinnaisia. Microsoft Agent Framework on oletusmalliasiakas kaikille tarjoajille alkaen Co-op Translator 0.22.0:sta. Semantic Kernel voidaan silti valita väliaikaisesti asettamalla `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, mutta tämän tekeminen aiheuttaa vanhentumisvaroituksen; katso [konfigurointi](configuration.md#model-client-backend) vaiheistetusta poistosuunnitelmasta.

Vaaditut Azure AI Vision -muuttujat kuvakäännöstä varten:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` on deterministinen eikä vaadi LLM- tai Azure AI Vision -konfiguraatiota.

## Käyttäytymismuistiinpanot

- Sisällönkäännös-API:t pitävät käännöksen erillään projektin polkujen uudelleenkirjoituksesta. Kutsu `rewrite_markdown_paths` tai `rewrite_notebook_paths` erikseen, kun käännettyä sisältöä tarvitsee säätää projektisuhteisia linkkejä kohdesijaintia varten.
- Projektin orkestrointi-API:t lisäävät projektikäyttäytymistä sisältökäännöksen ympärille, mukaan lukien tiedostojen löytäminen, kirjoitukset, polkujen uudelleenkirjoitus, metatiedot, siivous ja valinnaiset vastuuvapauslausekkeet.
- `run_translation` tulostaa etenemisen ja arvioyhteenvetot Rich-pohjaisen raportointityökalun kautta, jota CLI käyttää. Ei-interaktiivinen tulostus palaa tavalliseen tekstiin.
- `dry_run=True` laskee arviot käyttäen virtuaalisia README-päivityksiä, mutta ei kirjoita README:tä eikä käännöstiedostoja.
- `groups` käsitellään peräkkäin. Yksi yhteenlaskettu arvio tulostetaan ennen työn aloittamista.
- Kun kuvakäännös on valittu, puuttuva Vision-konfiguraatio aiheuttaa virheen ennen käännöksen alkamista.
- Olemassa olevat alias-pohjaiset kielihakemistot tunnistetaan ja ne voidaan siirtää kanonisiin BCP 47 -kielihakemistonimiin osana ajoa.
- `run_review` epäonnistuu puuttuviin käännettyihin tiedostoihin, puuttuviin tai vanhentuneisiin käännösmetatietoihin, virheellisesti muotoiltuun Markdown-frontmatteriin/koodiaitoihin sekä virheelliseen käännettyyn muistikirjan JSON:iin.
- `run_review` raportoi puuttuvat paikalliset Markdown- ja kuvalinkkien kohteet oletuksena varoituksina.

## Sisäinen kutsupolku

API delegoi samaan ydintoteutukseen, jota CLI käyttää:

Käännös:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content` tai `translate_image_content` muistissa tapahtuvalle käännökselle.
2. `co_op_translator.api.translation.rewrite_markdown_paths` tai `rewrite_notebook_paths` eksplisiittiseen polkujen jälkikäsittelyyn.
3. `co_op_translator.api.translation.run_translation` täydelliseen projektin orkestrointiin.
4. `co_op_translator.config.Config`, `LLMConfig` ja `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Kohdennetut projektin käännösmixinat Markdownille, muistikirjoille ja kuville.
8. Markdown-, muistikirja-, teksti- ja kuvakääntäjät `co_op_translator.core`-kansiossa.

Tarkastus:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiset tarkistukset `co_op_translator.review.checks`-moduulin alla

Seuraavat luokat ovat hyödyllisiä ylläpitäjille, mutta niitä ei tarjota paketin tasoisena vakaana API:na.

| Luokka | Moduuli | Vastuualue |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinoi projektitason käännöstä, hakemistojen hallintaa, kielikohtaisten metatietojen normalisointia ja delegointia Markdown-, muistikirja- ja kuvakääntäjille. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Suorittaa asynkronisen tiedostokäsittelyn Markdownille, muistikirjoille, kuville, vanhentuneisuuden tunnistamisen ja käännösmetatietojen päivitykset. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestroi Markdown-tiedostojen lukemisen, sisällön käännöksen, polkujen uudelleenkirjoituksen, metatiedot, vastuuvapauslausekkeet ja kirjoitukset. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestroi muistikirjatiedostojen lukemisen, Markdown-solujen käännöksen, polkujen uudelleenkirjoituksen, metatiedot, vastuuvapauslausekkeet ja kirjoitukset. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestroi lähdekuvien löydön, kuvien käännöksen, lähtöpolut, metatiedot ja kirjoitukset. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Löytää käännetyt Markdown-parit, arvioi käännösten laatua ja lukee luottamusmetatietoja alhaisen luottamuksen korjaustyönkulkuihin. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinoi deterministisiä tarkistuksia lähdetiedostoissa, kohdekielissä ja konfiguroiduissa käännösjuurissa. |
| `ReviewTarget` | `co_op_translator.review.targets` | Kuvaa lähdejuuren ja sitä varten tarkastettavan käännösten ulostulohakemiston. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Havaitsee vanhat alias-kielihakemistot ja valmistaa kanonisten BCP 47 -hakemistomigraatiosuunnitelmia. |
| `Config` | `co_op_translator.config.base_config` | Lataa `.env`-tiedostot ja tarkistaa, onko vaaditut LLM- ja valinnaiset Vision-palveluntarjoajat konfiguroitu. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Tunnistaa automaattisesti Azure OpenAI:n, OpenAI:n tai Anthropicin, validoi vaaditut ympäristömuuttujat ja suorittaa tarjoajan yhteyden tarkistukset. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Havaitsee Azure AI Vision -konfiguraation ja suorittaa yhteyden tarkistuksia kuvakäännöstä varten. |