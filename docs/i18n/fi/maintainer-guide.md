# Ylläpitäjän opas

Tämä sivu tiivistää, miten API, CLI ja dokumentaatiosivusto on kytketty yhteen.

## Julkinen API-raja

Vakaa Python-API viedään seuraavasta:

```python
co_op_translator.api
```

Julkinen API on järjestetty sisällön käännösapumoduuleihin, polun uudelleenkirjoitusapumoduuleihin, projektin orkestrointiin ja tarkasteluun:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

Kun lisäät uusia julkisia API-rajapintoja, päivitä:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevantit API-testit hakemistossa `tests/co_op_translator/`, kuten `test_api.py` tai `test_review_api.py`

Vältä dokumentoimasta alempitasoisia `core`-moduuleja vakaana API:na, ellei projekti aio tukea niitä suoraan.

## CLI:n sisäänkäynnit

Paketti määrittelee nämä Poetry-skriptit:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ohjaa skriptiä nimen perusteella:

- `translate` kutsuu `co_op_translator.cli.translate.translate_command`
- `evaluate` kutsuu `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kutsuu `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kutsuu `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ohittaa `__main__.py` ja kutsuu suoraan `co_op_translator.mcp.server:main`.

Kun lisäät tai muutat CLI-asetuksia, päivitä:

- vastaava `src/co_op_translator/cli/*.py` -komento
- `docs/cli.md`
- CLI:hin liittyvät testit, jos toiminta muuttuu

## MCP-palvelin

MCP-palvelin on toteutettu:

```python
co_op_translator.mcp.server
```

Palvelin käärii tahallaan julkisen Python-API:n sen sijaan, että kutsuisi alempitasoisia `core`-moduuleja. Säilytä tämä raja ennallaan, jotta MCP-asiakkaat, Python-kutsujat ja CLI noudattavat samaa käyttäytymistä.

Kun lisäät tai muutat MCP-työkaluja, päivitä:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jos julkisen API:n pinta muuttuu

Repositoryn käännöstyökalut ovat mallin kutsuttavissa MCP:n kautta ja voivat kirjoittaa monia tiedostoja. Pidä `dry_run=True` oletuksena ja vaadi `confirm_write=True` ennen ei-kuiva-ajon projektikäännöstä.

## Käännösprosessi

Korkean tason projektin käännösprosessi on:

1. Parse CLI arguments or API parameters.
2. Validate LLM configuration with `LLMConfig`.
3. Validate Azure AI Vision when image translation is selected.
4. Normalize language codes.
5. Detect legacy language folder aliases.
6. Estimate translation volume.
7. Update README language/course sections when applicable.
8. Delegate project translation to `ProjectTranslator`.
9. `ProjectTranslator` delegates file processing to `TranslationManager`.

`TranslationManager` koostuu tiedostotyyppeihin keskittyvistä mixin-luokista:

- `ProjectMarkdownTranslationMixin` hoitaa Markdown-tiedostojen lukemiset, sisällön käännöksen, polkujen uudelleenkirjoittamisen, metatiedot, vastuutekstit ja kirjoitukset.
- `ProjectNotebookTranslationMixin` käsittelee muistikirjatiedostojen lukemiset, Markdown-solujen käännökset, polkujen uudelleenkirjoitukset, metatiedot, vastuutekstit ja kirjoitukset.
- `ProjectImageTranslationMixin` hoitaa kuvien löytämisen, tekstin poiminnan/käännöksen, renderöityjen kuvien kirjoittamisen ja metatiedot.

Alemmantasoiset sisällön API:t ohittavat projektityönkulun:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` translates text in a single image and returns a rendered image object.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` are explicit post-processing helpers. They perform no translation and no project writes.

## Tarkastusprosessi

Deterministinen tarkastusprosessi on:

1. Parse CLI arguments or API parameters.
2. Normalize requested language codes.
3. Build one or more review targets from `root_dir`, `root_dirs`, or `groups`.
4. Optionally limit source files with `--changed-from`.
5. Run deterministic checks for structure, translation freshness, Markdown integrity, and local link/image paths.
6. Print either text output or GitHub-flavored Markdown.
7. Exit with a failure when review errors are found.

Tarkastusprosessi ei vaadi API-avaimia ja sen tulisi pysyä sopivana pull request -CI:lle. Pull request -työnkulku kirjoittaa tarkistusyhteenvedon jokaisella ajokerralla ja julkaisee PR-kommentin vain, kun `co-op-review` epäonnistuu.

## Dokumentaatiosivusto

Dokumentaatiosivusto on konfiguroitu seuraavilla:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/`-hakemisto on kanoninen dokumentaation lähde. Älä lisää uusia loppukäyttäjän oppaita tämän hakemiston ulkopuolelle, ellei projekti tarkoituksellisesti ota käyttöön toista julkaistavaa dokumentaatiopintaa.

Rakenna paikallisesti:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Esikatsele paikallisesti:

```bash
python -m mkdocs serve
```

Luotu sivusto kirjoitetaan hakemistoon `site/`, joka on gitin ohittama.

## GitHub Pages -työnkulku

.github/workflows/docs.yml rakentaa sivuston pull requesteissa ja ottaa sen käyttöön push-tapahtumissa `main`-haaraan.

Työnkulku asentaa:

```bash
pip install -r requirements-docs.txt
```

Dokumentaation työnkulku asentaa vain dokumentaation työkaluketjun. `mkdocs.yml` osoittaa `mkdocstrings`-laajennuksen `src/`-hakemistoon, jotta julkiset API-sivut voidaan renderöidä lähdekoodipuun lähteistä ilman koko ajoaikariippuvuuksien asentamista. Jos tulevat API-dokumentit vaativat valinnaisten ajoaikaisten providerien tuonnin rakennuksen aikana, päivitä sekä `.github/workflows/docs.yml` että tämä opas samanaikaisesti.

## Dokumentaation laatuvaatimus

Ennen dokumentaation muutosten yhdistämistä, suorita:

```bash
python -m mkdocs build --strict
git diff --check
```

Käytä tiukkoja rakennusasetuksia, jotta rikkinäiset linkit, virheelliset navigaatiomerkinnät ja API:n renderöinti-ongelmat havaitaan ajoissa.