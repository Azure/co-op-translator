# Hooldaja juhend

See lehekülg võtab kokku, kuidas API, CLI ja dokumentatsioonisait on omavahel seotud.

## Avaliku API piir

Stabiilne Python API eksporditakse järgmisest:

```python
co_op_translator.api
```

Avalik API on organiseeritud sisu tõlkimise abivahenditeks, failiteede ümberkirjutamise abivahenditeks, projekti orkestreerimiseks ja ülevaatuseks:

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

`TranslationStateProvider` on majutatud integratsioonide püsivuse piir.
See peab hoidma genereeritud kandidaadid eraldi aktsepteeritud baasversioonidest, nii et
mitteühendatud tõlge ei muutuks tõeallikaks.

Uute avalike API-de lisamisel uuenda:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- vastavad API testid kataloogis `tests/co_op_translator/`, näiteks `test_api.py` või `test_review_api.py`

Väldi madalama taseme `core` moodulite dokumenteerimist kui stabiilset API-d, välja arvatud juhul, kui projekt kavatseb neid otseselt toetada.

## CLI käivituspunktid

Pakett määratleb need Poetry skriptid:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

Fail `src/co_op_translator/__main__.py` juhib käivitamist skripti nime alusel:

- `translate` kutsub `co_op_translator.cli.translate.translate_command`
- `evaluate` kutsub `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kutsub `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kutsub `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` möödub `__main__.py`-st ja kutsub otse `co_op_translator.mcp.server:main`.

CLI valikute lisamisel või muutmisel uuenda:

- vastav käsk `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- CLI-ga seotud testid, kui käitumine muutub

## MCP server

MCP server on realiseeritud failis:

```python
co_op_translator.mcp.server
```

Server ümbritseb teadlikult avalikku Python API-d, selle asemel et kutsuda madalama taseme `core` mooduleid. Hoia see piir puutumata, et MCP kliendid, Python-kõnelejad ja CLI jagaksid sama käitumist.

MCP tööriistade lisamisel või muutmisel uuenda:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` kui avaliku API pind muutub

Repositooriumi tõlketööriistad on MCP kaudu mudeli-kõnetavad ja võivad kirjutada palju faile. Jäta `dry_run=True` vaikeseisundiks ja nõua `confirm_write=True` enne mitte-dry-run projekti tõlkimist.

## Tõlkevoog

Projekti kõrgetasemeline tõlkevoog on:

1. Analüüsi CLI argumendid või API parameetrid.
2. Kinnita LLM konfiguratsioon `LLMConfig`-iga.
3. Kinnita Azure AI Vision, kui on valitud pilditõlge.
4. Normaliseeri keelekoodid.
5. Tuvasta pärandkeele kaustade aliasid.
6. Hinda tõlkemahu.
7. Uuenda README keele või kursuse jaotisi vastavalt vajadusele.
8. Delegeeri projekti tõlkimine `ProjectTranslator`-ile.
9. `ProjectTranslator` delegeerib failitöötluse `TranslationManager`-ile.

`TranslationManager` koosneb fookustatud failitüüpide mixin'itest:

- `ProjectMarkdownTranslationMixin` haldab Markdown-failide lugemist, sisu tõlget, failiteede ümberkirjutamist, metaandmeid, lahtiütlusi (disclaimers) ja kirjutamist.
- `ProjectNotebookTranslationMixin` haldab notebook-failide lugemist, Markdown-rakkude tõlget, failiteede ümberkirjutamist, metaandmeid, lahtiütlusi ja kirjutamist.
- `ProjectImageTranslationMixin` haldab piltide avastamist, teksti ekstraheerimist/tõlkimist, renderdatud piltide kirjutamist ja metaandmeid.

Madalama taseme sisu API-d jätavad projekti töövoo vahele:

1. `translate_markdown_content` ja `translate_notebook_content` tõlgivad ainult mälus olevat sisu.
2. `translate_image_content` tõlgib teksti ühes pildis ja tagastab renderdatud pildi objekti.
3. `rewrite_markdown_paths` ja `rewrite_notebook_paths` on eksplicitseid järeltöötluse abimehi. Need ei tee tõlget ega projekti kirjutisi.

## Ülevaatamise töövoog

Deterministlik ülevaatuse töövoog on:

1. Analüüsi CLI argumendid või API parameetrid.
2. Normaliseeri soovitud keelekoodid.
3. Koosta üks või mitu ülevaatussihti `root_dir`, `root_dirs` või `groups` alusel.
4. Vajadusel piira algfaile `--changed-from` abil.
5. Käivita deterministlikud kontrollid struktuuri, tõlke värskuse, Markdowni terviklikkuse ja kohalike linkide/pilditeede jaoks.
6. Väljastab kas tekstiväljundi või GitHub-laadse Markdowni.
7. Välju ebaõnnestumisega, kui leitakse ülevaatusvigu.

Ülevaatuse töövoog ei nõua API-võtmeid ja on saadaval lokaalsete kontrollide või valikulise tarbija CI jaoks. See hoidla ei käivita `co-op-review` automaatselt igal pull requestil.

## Dokumentatsioonisait

Dokumentatsioonisaiti konfigureeritakse failiga:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Kaust `docs/` on ametlik dokumentatsiooni allikas. Ära lisa uusi lõppkasutaja juhendeid väljaspool seda kausta, välja arvatud juhul, kui projekt teadlikult lisab teise avaldatava dokumentatsioonipinna.

Ehita lokaalselt:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Eelvaata lokaalselt:

```bash
python -m mkdocs serve
```

Genereeritud sait kirjutatakse kataloogi `site/`, mida git ignoreerib.

## GitHub Pages töövoog

`.github/workflows/docs.yml` ehitab saiti pull requestide puhul ja juurutab selle pushide korral harule `main`.

Töövoog installeerib:

```bash
pip install -r requirements-docs.txt
```

Dokumentatsiooni töövoog installeerib ainult dokumentatsiooni tööriistaketi. Fail `mkdocs.yml` suunab `mkdocstrings`-i kausta `src/`, nii et avalike API lehekülgi saab renderdada lähtekoorest ilma kogu käitusaja sõltuvuste komplekti installimata. Kui tulevased API dokumendid nõuavad ehituse käigus valikuliste käitusaja pakkujate importimist, uuenda nii `.github/workflows/docs.yml` kui ka seda juhendit.

## Dokumentatsiooni kvaliteedistandard

Enne dokumentatsiooni muudatuste ühendamist käivita:

```bash
python -m mkdocs build --strict
git diff --check
```

Kasuta rangeid ehitusi, et katkised lingid, vigased navigeerimisentrüüd ja API renderdamise probleemid ebaõnnestuksid varakult.