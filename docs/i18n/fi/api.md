# Python-rajapinta

Julkinen, vakaa Python-rajapinta viedään paketista `co_op_translator.api`. Useimmat integraatiot käyttävät jotain näistä työnkuluista:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Useimmat alemmat moduulit `core`-, `config`-, `review`- ja `utils`-kansioissa ovat toteutuksen yksityiskohtia, joita nämä API:n sisäänpääsyt käyttävät.

MCP-asiakkaat käyttävät samaa julkista rajapintaa kautta [MCP-palvelin](mcp.md). Käytä tätä sivua kun kutsut Pythonia suoraan, ja MCP-opasta kun altistat Co-op Translatorin agentille tai editorille. Jos olet päättämässä CLI:n, Python-rajapinnan ja MCP:n välillä, aloita kohdasta [Valitse työnkulku](workflows.md).

## Ensimmäisen käyttökerran API-työnkulku

Aloita tästä, jos kutsut Co-op Translatoria Python-koodista:

1. Määritä LLM-palveluntarjoaja kuten on kuvattu kohdassa [Configuration](configuration.md), ellei tarkoituksesi ole vain valmistella Markdown- tai muistikirjapalasia isäntäagentin kääntämistä varten.
2. Päätä, hoitaako sovelluksesi tiedostojen I/O:n.
3. Käytä sisältö-API:a kun sovelluksesi lukee ja kirjoittaa yksittäisiä tiedostoja.
4. Käytä `run_translation` kun Co-op Translatorin tulisi käsitellä projektia kuten CLI.
5. Käytä `run_review` käännöksen jälkeen, jos tarvitset deterministisiä tarkistuksia automaatiossa.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Tapaus 1: Käännä yksittäisiä tiedostoja tai dokumentteja

Käytä tätä työnkulkua, kun sinulla on jo tiedosto, editorin puskuri, muistikirjakuorma, MCP-pyyntö tai mukautettu pipelinen syöte. Koodisi hoitaa tiedostojen I/O:n:

1. Lue lähdesisältö.
2. Kutsu sisällön käännös-API:a.
3. Valinnaisesti kutsu polkujen uudelleenkirjoitus-API:a, jos käännetty sisältö tullaan kirjoittamaan projektiin.
4. Tallenna tai palauta tulos sovelluksestasi.

Sisällön käännös-API:t eivät aja projektin löydystä, eivät kirjoita metatietoa, eivät lisää vastuuvapauslausekkeita eikä uudelleenkirjoita linkkejä automaattisesti.

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

Jos käännetty Markdown ei tule elämään Co-op Translator -projektin rakenteessa, ohita `rewrite_markdown_paths` ja tallenna käännetty merkkijono suoraan.

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

`translate_image_content` lukee lähdekuvan ja palauttaa renderöidyn `PIL.Image.Image`-olion. Se ei kirjoita käännettyjen kuvien metatietoja.

## Tapaus 2: Käännä koko repositorio

Käytä tätä työnkulkua, kun haluat Python-rajapinnan käyttäytyvän kuten `translate`-CLI. `run_translation` löytää tuetut tiedostot, kääntää valitut sisältötyypit, uudelleenkirjoittaa polut, kirjoittaa ulostulotiedostot, päivittää metatiedot ja suorittaa käännöksen ylläpitotehtäviä kuten siivouksen.

`run_translation` on suositeltu projektin orkestrointipiste. `translate_project` viedään yhteensopivuusaliasina, jolla on sama käyttäytyminen.

Käännä Markdown-tiedostot nykyisessä repositoriossa koreaksi ja japaniksi:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Käännä vain muistikirjoja tietystä projektijuuresta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Esikatsele käännösmäärää kirjoittamatta tiedostoja:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Käännä useita sisältöjuuria yhdessä kutsussa:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Kirjoita käännökset nimenomaisiin ulostuloryhmiin:

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

Käytä kielenmukaista paikkamerkkiä, kun jokaisen kielen pitäisi sisältää alihakemisto:

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

Jos mikään `markdown`, `notebook` tai `images` ei ole asetettu, API kääntää kaikki tuetut tyypit: Markdown, muistikirjat ja kuvat.

## Tarkista käännetty sisältö

`run_review` suorittaa deterministisiä käännöstarkistuksia ilman LLM- tai Vision-tunnuksia.

!!! note "Beta"
    `run_review` on beta-vaiheen deterministinen tarkistus-API. Se ei kutsu mallipalveluntarjoajia eikä kirjoita tiedostoja, mutta tarkistukset ja issue-skeemat saattavat kehittyä.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Tarkista vain tiedostot, jotka ovat muuttuneet verrattuna base-refiin, ja tulosta GitHub-muotoiluinen output:

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
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Käännä useita juuri-hakemistoja:

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

Säilytä sanastotermit:

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

## Julkiset sisäänkäynnit

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Sisällön käännös-API:t

Sisällön käännös-API:t on tarkoitettu integraatioille, joilla sisältö on jo muistissa, kuten editorilaajennus, MCP-työkalu, muistikirjakäsittelijä tai mukautettu pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ei | Asynkroninen. Kääntää vain Markdown-sisällön. Se ei uudelleenkirjoita linkkejä, kirjoita metatietoa tai lisää vastuuvapauslausekkeita. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Ei | Asynkroninen. Kääntää Markdown-soluja ja säilyttää ei-Markdown-solut. Se ei uudelleenkirjoita linkkejä, kirjoita metatietoa tai lisää vastuuvapauslausekkeita. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Lukee vain lähdekuvan | Synkroninen. Poimii ja kääntää kuvan tekstin ja palauttaa renderöidyn kuvan. Se ei tallenna käännettyjen kuvien metatietoja. |

`translate_markdown_content` ja `translate_notebook_content` hyväksyvät valinnaisen `source_path`-parametrin optioidensa kautta. Polku välitetään kääntäjälle kontekstina; kutsujat ovat edelleen vastuussa mahdollisesta projektiin liittyvästä polkujen uudelleenkirjoituksesta käännöksen jälkeen.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Samat optiot voidaan antaa myös sanakirjoina:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agentin avustamat käännös-API:t

Agentin avustamat API:t eivät kutsu Azure OpenAI:ta tai OpenAI:ta Co-op Translatorista käsin. Ne valmistavat Markdown- tai muistikirjapalasia isäntäagentin käännettäviksi ja rekonstruoivat lopullisen sisällön käännetyistä paloista.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Tätä työnkulkua on pääasiassa tarkoitettu MCP-isännille. Jos tarvitset tuotantotason repositorion kääntämistä siten, että Co-op Translator hallinnoi palveluntarjoajakutsuja, käytä `translate_markdown_content`, `translate_notebook_content` tai `run_translation`.

## Polkujen uudelleenkirjoitus-API:t

Polkujen uudelleenkirjoitus-API:t eivät tee käännöstä. Ne päivittävät linkit ja frontmatter-polut sen jälkeen, kun kutsujat tietävät lähdepolun, käännetyn kohdepolun ja projektin rakenteen.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Uudelleenkirjoittaa Markdown-linkit ja tuetut frontmatter-polukentät käännetylle kohteelle. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Soveltaa Markdown-polkujen uudelleenkirjoitusta jokaiseen Markdown-soluun ja jättää ei-Markdown-solut muuttumattomiksi. |

`policy`-argumentti voi olla sanakirja, joka sisältää nämä kentät:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Kyllä | Kohdekielen koodi, esimerkiksi `"ko"` tai `"pt-BR"`. |
| `root_dir` | Ei | Lähdeprojektin juurihakemisto. Oletus `"."`. |
| `translations_dir` | Ei | Tekstikäännösten ulostulohakemisto. Oletuksena `translations` `root_dir`-hakemiston alla. |
| `translated_images_dir` | Ei | Käännettyjen kuvien ulostulohakemisto. Oletuksena `translated_images` `root_dir`-hakemiston alla. |
| `translation_types` | Ei | Käytössä olevat käännöstyypit. Oletuksena Markdown, muistikirjat ja kuvat. |
| `lang_subdir` | Ei | Valinnainen alihakemisto kunkin kielikansion sisällä. |

## Projektin käännösparametrit

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Pakollinen | Välilyönnillä erotetut kohdekielikoodit, esimerkiksi `"ko ja fr"`, tai `"all"`. Alias-koodit normalisoidaan kanonisiin BCP 47 -arvoihin. |
| `root_dir` | `str` | `"."` | Projektin juurihakemisto yksittäiselle käännöskohteelle. Ohitetaan, kun `root_dirs` tai `groups` on annettu. |
| `update` | `bool` | `False` | Poistaa ja luo uudelleen olemassa olevat käännökset valituille kielille. |
| `images` | `bool` | `False` | Sisällytä kuvien käännös. Edellyttää Azure AI Vision -määritystä. |
| `markdown` | `bool` | `False` | Sisällytä Markdown-käännökset. |
| `notebook` | `bool` | `False` | Sisällytä Jupyter-muistikirjojen käännökset. |
| `debug` | `bool` | `False` | Ota käyttöön debug-lokinointi. |
| `save_logs` | `bool` | `False` | Tallenna DEBUG-tason lokitiedostot juuren `logs/`-hakemistoon. |
| `yes` | `bool` | `True` | Vahvista kehotteet automaattisesti ohjelmallista ja CI-käyttöä varten. |
| `add_disclaimer` | `bool` | `False` | Lisää konekäännösvakuutus käännettyihin Markdown- ja muistikirjatiedostoihin. |
| `translations_dir` | `str \| None` | `None` | Mukautettu tekstikäännösten ulostulohakemisto. Relatiiviset polut ratkaistaan kutakin juurta vastaan. |
| `image_dir` | `str \| None` | `None` | Mukautettu käännettyjen kuvien ulostulohakemisto. Relatiiviset polut ratkaistaan kutakin juurta vastaan. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Useita juuria, jotka jakavat samat ulostuloasetukset. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Nimenomaiset `(root_dir, translations_dir)`-parit. Ylittää `root_dirs`-asetuksen. |
| `repo_url` | `str \| None` | `None` | Repositorion URL, jota käytetään README-kielitaulukon ohjeistuksen renderöinnissä. |
| `glossaries` | `Iterable[str] \| None` | `None` | Säilytettäviä sanastotermejä käännöksen aikana. Duplikaatit ja tyhjät termit normalisoidaan. |
| `dry_run` | `bool` | `False` | Arvioi käännösmäärä ja esikatsele migraation käyttäytymistä kirjoittamatta tiedostoja. |

## Tarkistuksen parametrit

`run_review` on tarkoituksella mallinnettu vastaamaan `run_translation`-allekirjoitusta mahdollisimman pitkälle, jotta automaatio voi vaihtaa käännös- ja tarkistustyönkulkujen välillä minimoidulla haarautumisella.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Tarkistettavat kohdekielikansiot. Hyväksyy välilyönnillä erotetut merkkijonot ja iteraatit. `"all"` tarkistaa jokaisen löydetyn käännöskielen. |
| `root_dir` | `str` | `"."` | Projektin juurihakemisto yksittäiselle tarkistuskohteelle. Ohitetaan, kun `root_dirs` tai `groups` on annettu. |
| `markdown` | `bool` | `False` | Sisällytä Markdown- ja MDX-lähdetiedostot. |
| `notebook` | `bool` | `False` | Sisällytä Jupyter-muistikirjojen lähdetiedostot. |
| `images` | `bool` | `False` | Varattu pariteetin vuoksi käännösasetusten kanssa. Kuvien viittaukset tarkistetaan Markdownista. |
| `translations_dir` | `str \| None` | `None` | Mukautettu tekstikäännösten tulostuskansio. Relatiiviset polut ratkaistaan kunkin juuren mukaan. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Useita juurihakemistoja, jotka käyttävät samoja tulostusasetuksia. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Eksplisiittiset `(root_dir, translations_dir)`-parit. Nämä menevät `root_dirs`-asetuksen edelle. |
| `changed_from` | `str \| None` | `None` | Git-viite, jota käytetään rajoittamaan tarkastus muutettuihin lähdetiedostoihin. |
| `output_format` | `str` | `"text"` | Tarkastustulosteen muoto. Tuetut arvot ovat `"text"` ja `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Käsittele varoitukset virheinä virheiden ohella. |
| `debug` | `bool` | `False` | Ota debug-lokitus käyttöön. |
| `save_logs` | `bool` | `False` | Tallenna DEBUG-tason lokitiedostot juuren `logs/`-hakemistoon. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfiguraation vaatimukset

Palveluntarjoajaan perustuvat käännös‑APIt vaativat palveluntarjoajan konfiguroinnin ennen käännöstä:

- Markdown- ja notebook-käännökset vaativat LLM‑palveluntarjoajan. Konfiguroi joko Azure OpenAI tai OpenAI.
- Kuvien käännös vaatii Azure AI Visionin lisäksi LLM‑palveluntarjoajan.
- `run_translation` suorittaa kevyitä yhteystarkistuksia ennen projektin käännöksen aloittamista.
- Agentin avustamat `start_*_agent_translation` ja `finish_*_agent_translation` API:t eivät kutsu Co-op Translatorin LLM‑palveluntarjoajia. Isäntä­sovellus tai MCP‑agentti kääntää valmistellut palaset.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ja `run_review` ovat deterministisiä eivätkä vaadi palveluntarjoajan tunnuksia.

Vaadittavat Azure OpenAI -muuttujat:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Vaadittavat OpenAI‑muuttujat:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Vaadittavat Azure AI Vision -muuttujat kuvien kääntämistä varten:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` on deterministinen eikä vaadi Azure OpenAI-, OpenAI- tai Azure AI Vision -konfiguraatiota.

## Toimintamuistiinpanot

- Sisällön käännös‑API:t pitävät käännöksen erillään projektin polkujen uudelleenkirjoituksesta. Kutsu `rewrite_markdown_paths` tai `rewrite_notebook_paths` erikseen, kun käännetty sisältö tarvitsee projektisuhteisten linkkien säätöä kohdepaikkaa varten.
- Projektin orkestrointi‑API:t lisäävät projektikäyttäytymistä sisällön käännöksen ympärille, mukaan lukien tiedostojen haku, kirjoitukset, polkujen uudelleenkirjoitus, metatiedot, siivous ja valinnaiset vastuuvapauslausekkeet.
- `run_translation` tulostaa etenemis- ja arvioyhteenvetoja Clickin kautta, vastaten CLI‑käyttäjäkokemusta.
- `dry_run=True` laskee arviot käyttämällä virtuaalisia README‑päivityksiä, mutta ei kirjoita README:tä tai käännöstiedostoja.
- `groups` käsitellään peräkkäin. Yksi yhteenlaskettu arvio tulostetaan ennen työn aloittamista.
- Kun kuvien käännös on valittu, puuttuva Vision‑konfiguraatio aiheuttaa virheen ennen käännöksen aloittamista.
- Olemassa olevat alias‑pohjaiset kielihakemistot havaitaan ja ne voidaan siirtää kanonisiin BCP 47 -kielihakemistonimiin ajon yhteydessä.
- `run_review` epäonnistuu puuttuvien käännettyjen tiedostojen, puuttuvien tai vanhentuneiden käännösmetatietojen, virheellisten Markdown-frontmatterien tai koodiaitausten sekä virheellisen käännetyn notebook‑JSONin vuoksi.
- `run_review` raportoi puuttuvat paikalliset Markdown- ja kuva­linkkikohteet oletuksena varoituksina.

## Sisäinen kutsupolku

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Luokka | Moduuli | Vastuualue |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinoi projektitason käännöstä, hakemistonhallintaa, kielikohtaisten metatietojen normalisointia ja delegointia Markdown-, notebook- ja kuvan kääntäjille. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Suorittaa asynkronisen tiedostojenkäsittelyn Markdownille, notebookeille, kuville, vanhentuneisuuden tunnistukselle ja käännösmetatietopäivityksille. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestroi Markdown-tiedostojen lukemisen, sisällön käännöksen, polkujen uudelleenkirjoituksen, metatiedot, vastuuvapauslausekkeet sekä kirjoitukset. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestroi notebook-tiedostojen lukemisen, Markdown-solujen käännöksen, polkujen uudelleenkirjoituksen, metatiedot, vastuuvapauslausekkeet sekä kirjoitukset. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestroi lähdekuvien löydön, kuvien käännöksen, tulostuspolut, metatiedot sekä kirjoitukset. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Löytää käännetyt Markdown-parit, arvioi käännösten laatua ja lukee luottamusmetatietoja matalan luottamuksen korjaustyönkulkuihin. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinoi deterministisiä tarkastusvarmistuksia lähdetiedostoissa, kohdekielissä ja konfiguroiduissa käännösjuurissa. |
| `ReviewTarget` | `co_op_translator.review.targets` | Kuvaa lähdejuuren ja kyseiselle juurelle tarkastetun käännösten tulostuskansion. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Havaitsee vanhat alias‑kielihakemistot ja valmistelee kanoniset BCP 47 -kielihakemistojen migraatiosuunnitelmat. |
| `Config` | `co_op_translator.config.base_config` | Lataa `.env`-tiedostot ja tarkistaa, onko vaaditut LLM- ja valinnaiset Vision‑palveluntarjoajat konfiguroitu. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automaattisesti tunnistaa Azure OpenAI:n tai OpenAI:n, validoi vaaditut ympäristömuuttujat ja suorittaa palveluntarjoajan yhteystarkistuksia. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Havaitsee Azure AI Vision -konfiguraation ja suorittaa yhteystarkistuksia kuvien käännöstä varten. |