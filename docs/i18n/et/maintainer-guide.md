# Hooldaja juhend

See lehekülg võtab kokku, kuidas API, CLI ja dokumentatsioonisait on omavahel seotud.

## Avaliku API piir

Stabiilne Python API eksporditakse järgmisest:

```python
co_op_translator.api
```

Avalik API on korraldatud sisu tõlkimise abivahenditeks, tee ümberkirjutamise abivahenditeks, projekti orkestreerimiseks ja ülevaatuseks:

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

Uute avalike API-de lisamisel uuendage:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- vastavaid API teste kaustas `tests/co_op_translator/`, näiteks `test_api.py` või `test_review_api.py`

Vältige madalama taseme `core` moodulite dokumenteerimist kui stabiilset API-d, välja arvatud juhul kui projekt kavatseb neid otseselt toetada.

## CLI sisenemispunktid

Pakett määratleb need Poetry skriptid:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` suunab käsu nime alusel:

- `translate` käivitab `co_op_translator.cli.translate.translate_command`
- `evaluate` käivitab `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` käivitab `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` käivitab `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` jätab vahele `__main__.py` ja kutsub otse `co_op_translator.mcp.server:main`.

CLI valikute lisamisel või muutmisel uuendage:

- vastavat `src/co_op_translator/cli/*.py` käsku
- `docs/cli.md`
- CLI-ga seotud teste, kui käitumine muutub

## MCP server

MCP server on implementeeritud järgmisesse:

```python
co_op_translator.mcp.server
```

Server katab tahtlikult avalikku Python API-d, selle asemel et kutsuda madalama taseme `core` mooduleid. Hoidke see piir puutumata, nii et MCP kliendid, Python-kutsujad ja CLI jagaksid sama käitumist.

MCP tööriistade lisamisel või muutmisel uuendage:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`, kui avaliku API pind muutub

Repositooriumi tõlketööriistad on mudelilt kutsutavad läbi MCP ja võivad kirjutada palju faile. Hoidke `dry_run=True` vaikeseade ja nõudke `confirm_write=True` enne mitte-dry-run projektitõlget.

## Tõlkevoog

Kõrgetaseme projekti tõlkevoog on:

1. Analüüsi CLI argumente või API parameetreid.
2. Valideeri LLM konfiguratsioon `LLMConfig` abil.
3. Valideeri Azure AI Vision, kui on valitud pildi tõlge.
4. Normaliseeri keelekoodid.
5. Tuvasta pärandkeelte kaustade aliasid.
6. Hinda tõlke mahtu.
7. Uuenda README keele/õppekursuse sektsioone, kui see on asjakohane.
8. Delegeeri projekti tõlge `ProjectTranslator`-ile.
9. `ProjectTranslator` delegeerib failitöötluse `TranslationManager`-ile.

`TranslationManager` koosneb spetsiifilistest failitüüpi mixinidest:

- `ProjectMarkdownTranslationMixin` tegeleb Markdown-failide lugemise, sisu tõlkimise, tee ümberkirjutamise, metaandmete, lahtiütluste ja kirjutamisega.
- `ProjectNotebookTranslationMixin` tegeleb notebook-failide lugemise, Markdown-rakkude tõlkimise, tee ümberkirjutamise, metaandmete, lahtiütluste ja kirjutamisega.
- `ProjectImageTranslationMixin` tegeleb piltide avastamise, teksti ekstraheerimise/tõlkimise, renderdatud piltide kirjutamise ja metaandmetega.

Madalama taseme sisu API-d jätavad projekti töövoo vahele:

1. `translate_markdown_content` ja `translate_notebook_content` tõlgivad ainult mälus olevat sisu.
2. `translate_image_content` tõlgib teksti ühes pildis ja tagastab renderdatud pildi objekti.
3. `rewrite_markdown_paths` ja `rewrite_notebook_paths` on selgesõnalised järelprotsessi abivahendid. Need ei tee tõlget ega kirjuta ühtegi projekti faili.

## Ülevaatuse voog

Deterministlik ülevaatuse töövoog on:

1. Analüüsi CLI argumente või API parameetreid.
2. Normaliseeri soovitud keelekoodid.
3. Moodusta üks või mitu ülevaatuse sihtmärki kasutades `root_dir`, `root_dirs` või `groups`.
4. Soovi korral piira lähtefaile `--changed-from` abil.
5. Käivita deterministlikud kontrollid struktuuri, tõlke värskuse, Markdowni terviklikkuse ning kohalike linkide ja pildi teede jaoks.
6. Trüki kas tekstiväljund või GitHub-vormingus Markdown.
7. Välju ebaõnnestumisega, kui leiti ülevaatusvigu.

Ülevaatusvoog ei vaja API võtmeid ja peaks jääma sobivaks pull request CI-iks. Pull request töövoog kirjutab iga käivituse kohta kontrolli kokkuvõtte ja postitab PR kommentaari ainult siis, kui `co-op-review` ebaõnnestub.

## Dokumentatsioonisait

Dokumentatsioonisaiti konfigureeritakse järgmiste abil:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` kataloog on kanoniline dokumentatsiooni allikas. Ärge lisage uusi lõppkasutaja juhendeid väljaspool seda kataloogi, välja arvatud juhul kui projekt kavandab sihipäraselt teise avaldatud dokumentatsiooniala.

Ehita lokaalselt:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Eelvaata lokaalselt:

```bash
python -m mkdocs serve
```

Genereeritud sait kirjutatakse kausta `site/`, mida git ignoreerib.

## GitHub Pages töövoog

.github/workflows/docs.yml ehitab saidi pull requestide ajal ja juurutab selle pushide korral `main`-harule.

Töövoog installib:

```bash
pip install -r requirements-docs.txt
```

Dokumentatsiooni töövoog installib ainult dokumentatsiooni tööriistakomplekti. `mkdocs.yml` suunab `mkdocstrings`-i `src/`-ile, nii et avalikke API-lehti saab renderdida lähtepuust ilma kogu jooksuaegsete sõltuvuste komplekti installimata. Kui tulevikus API-dokumentatsioon nõuab valiklike jooksuaegsete pakkujate importimist ehituse käigus, uuendage nii `.github/workflows/docs.yml` kui ka seda juhendit.

## Dokumentatsiooni kvaliteeditase

Enne dokumentatsiooni muudatuste liitmist käivitage:

```bash
python -m mkdocs build --strict
git diff --check
```

Kasutage rangeid ehitusi, nii et katkised lingid, vigased navigeerimisüksused ja API renderdamise probleemid ilmneksid varakult.