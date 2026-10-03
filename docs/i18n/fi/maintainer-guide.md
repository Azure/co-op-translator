# Ylläpitäjän opas

Tämä sivu tiivistää, miten API, CLI ja dokumentaatiosivusto on kytketty yhteen.

## Julkinen API-raja

Vakaa Python-API viedään seuraavasta:

```python
co_op_translator.api
```

Julkinen API on järjestetty sisältökäännösapuihin, polun uudelleenkirjoitusapuihin, projektin orkestrointiin ja tarkastukseen:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` on isännöityjen integraatioiden säilytysrajapinta.
Sen on pidettävä generoidut ehdokkaat erillään hyväksytyistä perusversioista, jotta
yhdistämätön käännös ei voi tulla totuuden lähteeksi.

Kun lisäät uusia julkisia API-rajapintoja, päivitä:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- asiaankuuluvat API-testit hakemistossa `tests/co_op_translator/`, kuten `test_api.py` tai `test_review_api.py`

Vältä dokumentoimasta alempitasoisia `core`-moduuleja vakaina API-rajapintoina, ellei projekti aio tukea niitä suoraan.

## CLI-käynnistyspisteet

Paketti määrittelee nämä Poetry-skriptit:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ohjaa skriptin nimen mukaan:

- `translate` kutsuu `co_op_translator.cli.translate.translate_command`
- `evaluate` kutsuu `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kutsuu `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kutsuu `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ohittaa `__main__.py` ja kutsuu suoraan `co_op_translator.mcp.server:main`.

Kun lisäät tai muutat CLI-vaihtoehtoja, päivitä:

- vastaava `src/co_op_translator/cli/*.py`-komento
- `docs/cli.md`
- CLI:hin liittyvät testit, jos käyttäytyminen muuttuu

## MCP-palvelin

MCP-palvelin on toteutettu tiedostossa:

```python
co_op_translator.mcp.server
```

Palvelin käärii tarkoituksellisesti julkista Python-APIa sen sijaan, että kutsuisi alempitasoisia `core`-moduuleja. Säilytä tämä raja ennallaan, jotta MCP-asiakkaat, Python-kutsujat ja CLI jakavat saman käyttäytymisen.

Kun lisäät tai muutat MCP-työkaluja, päivitä:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jos julkinen API-rajapinta muuttuu

Repositorion käännöstyökalut ovat mallikutsuttavissa MCP:n kautta ja voivat kirjoittaa monia tiedostoja. Pidä `dry_run=True` oletuksena ja vaadi `confirm_write=True` ennen kuin ajetaan projektikäännös ei-kuivakäynnillä.

## Käännösprosessi

Projektin korkean tason käännösprosessi on:

1. Jäsennä CLI-argumentit tai API-parametrit.
2. Vahvista LLM-konfiguraatio `LLMConfig`-luokan avulla.
3. Vahvista Azure AI Vision, kun kuvien käännös on valittu.
4. Normalisoi kielikoodit.
5. Tunnista vanhat kielihakemistojen aliasit.
6. Arvioi käännösmäärä.
7. Päivitä README-tiedoston kieli-/kurssiosiot tarvittaessa.
8. Delegoi projektin käännös `ProjectTranslator`-luokalle.
9. `ProjectTranslator` delegoi tiedostojen käsittelyn `TranslationManager`-luokalle.

`TranslationManager` koostuu tiedostotyyppeihin keskittyvistä mixineistä:

- `ProjectMarkdownTranslationMixin` käsittelee Markdown-tiedostojen lukemisen, sisällön kääntämisen, polkujen uudelleenkirjoittamisen, metatiedot, vastuuvapauslausekkeet ja kirjoitukset.
- `ProjectNotebookTranslationMixin` käsittelee muistikirjatiedostojen lukemista, Markdown-solujen käännöstä, polkujen uudelleenkirjoitusta, metatietoja, vastuuvapauslausekkeita ja kirjoituksia.
- `ProjectImageTranslationMixin` käsittelee kuvien etsintää, tekstin poimintaa/kääntämistä, renderoitujen kuvien kirjoittamista ja metatietoja.

Alempitasoiset sisältö-API:t ohittavat projektityönkulun:

1. `translate_markdown_content` ja `translate_notebook_content` kääntävät ainoastaan muistiin ladattua sisältöä.
2. `translate_image_content` kääntää tekstin yhdessä kuvassa ja palauttaa renderöidyn kuvaobjektin.
3. `rewrite_markdown_paths` ja `rewrite_notebook_paths` ovat eksplisiittisiä jälkikäsittelyapureita. Ne eivät tee käännöksiä eivätkä projektikirjoituksia.

## Tarkastusprosessi

Deterministinen tarkastusprosessi on:

1. Jäsennä CLI-argumentit tai API-parametrit.
2. Normalisoi pyydetyt kielikoodit.
3. Rakenna yksi tai useampi tarkastuskohde `root_dir`, `root_dirs` tai `groups` -arvoista.
4. Valinnaisesti rajoita lähdetiedostoja `--changed-from`-lipulla.
5. Suorita deterministisiä tarkistuksia rakenteelle, käännösten ajankohtaisuudelle, Markdownin eheydelle ja paikallisille linkki-/kuvapoluille.
6. Tulosta joko teksti- tai GitHub-maustettua Markdownia.
7. Lopeta virhetilaan, jos tarkastusvirheitä löytyy.

Tarkastusprosessi ei vaadi API-avaimia ja on käytettävissä paikallisiin tarkastuksiin tai valinnaiseen CI-ympäristöön. Tämä repositorio ei aja `co-op-review`-työkalua automaattisesti jokaisessa pull requestissa.

## Dokumentaatiopalvelu

Docs-sivusto on konfiguroitu seuraavasti:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Hakemisto `docs/` on kanoninen dokumentaation lähde. Älä lisää uusia loppukäyttäjän oppaita tämän hakemiston ulkopuolelle, ellei projekti tarkoituksellisesti ota käyttöön toista julkaistavaa dokumentaatiosivustoa.

Rakenna paikallisesti:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Esikatsele paikallisesti:

```bash
python -m mkdocs serve
```

Generoitava sivusto kirjoitetaan hakemistoon `site/`, joka on gitin seurannan ulkopuolella.

## GitHub Pages -työnkulku

Tiedosto `.github/workflows/docs.yml` rakentaa sivuston pull requestien yhteydessä ja ottaa sen käyttöön puskittaessa `main`-haaraan.

Työnkulku asentaa:

```bash
pip install -r requirements-docs.txt
```

Dokumentaation työnkulku asentaa vain dokumentaatiotyökaluketjun. `mkdocs.yml` osoittaa `mkdocstrings`-työkalun hakemistoon `src/`, joten julkiset API-sivut voidaan renderöidä lähdekoodipuun pohjalta ilman koko ajonaikaisen riippuvuusjoukon asentamista. Jos tulevat API-dokumentit vaativat valinnaisten ajonaikaisten toimittajien tuomista rakennusvaiheessa, päivitä sekä `.github/workflows/docs.yml` että tämä opas yhdessä.

## Dokumentaation laatutaso

Ennen dokumentaatiomuutosten yhdistämistä suorita:

```bash
python -m mkdocs build --strict
git diff --check
```

Käytä tiukkoja build-asetuksia, niin rikkinäiset linkit, virheelliset navigaatiomerkinnät ja API:n renderöintiongelmat havaitaan aikaisin.