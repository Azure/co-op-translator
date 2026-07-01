# Prižiūrėtojo vadovas

Šiame puslapyje apibendrinta, kaip API, CLI ir dokumentacijos svetainė yra sujungti.

## Viešosios API riba

Stabili Python API eksportuojama iš:

```python
co_op_translator.api
```

Viešoji API suskirstyta į pagalbines priemones turinio vertimui, kelių perrašymui, projekto orkestravimui ir peržiūrai:

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

Pridėdami naujas viešąsias API, atnaujinkite:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Venkite dokumentuoti mažesnio lygio `core` modulių kaip stabilios API, nebent projektas ketina juos tiesiogiai palaikyti.

## CLI entry points

Paketas apibrėžia šiuos Poetry skriptus:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` paskirsto pagal skripto pavadinimą:

- `translate` kviečia `co_op_translator.cli.translate.translate_command`
- `evaluate` kviečia `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kviečia `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kviečia `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` apeina `__main__.py` ir tiesiogiai kviečia `co_op_translator.mcp.server:main`.

Pridėdami arba keisdami CLI parinktis, atnaujinkite:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- su CLI susijusius testus, jei elgesys pasikeičia

## MCP server

MCP serveris įgyvendintas:

```python
co_op_translator.mcp.server
```

Serveris sąmoningai apgaubia viešąją Python API vietoj to, kad kvietų mažesnio lygio `core` modulius. Išlaikykite šią ribą nepakitusią, kad MCP klientai, Python kvietėjai ir CLI turėtų tą pačią elgseną.

Pridėdami arba keisdami MCP įrankius, atnaujinkite:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Saugyklos vertimo įrankiai yra iškviečiami per MCP ir gali rašyti daug failų. Laikykite `dry_run=True` numatytąja reikšme ir reikalaukite `confirm_write=True` prieš ne-dry-run projekto vertimą.

## Vertimo eiga

Aukšto lygio projekto vertimo eiga yra:

1. Išanalizuoti CLI argumentus arba API parametrus.
2. Patikrinti LLM konfigūraciją naudojant `LLMConfig`.
3. Patikrinti Azure AI Vision, kai pasirenkamas vaizdų vertimas.
4. Normalizuoti kalbų kodus.
5. Aptikti pasenusius kalbų aplankų pavadinimus.
6. Įvertinti vertimo apimtį.
7. Atnaujinti README kalbos/kursų skyrius, kai taikoma.
8. Perduoti projekto vertimą `ProjectTranslator`.
9. `ProjectTranslator` perduoda failų apdorojimą `TranslationManager`.

`TranslationManager` sudarytas iš specializuotų failų tipų mixin'ų:

- `ProjectMarkdownTranslationMixin` tvarko Markdown failų nuskaitymą, turinio vertimą, kelių perrašymą, metaduomenis, atsisakymus ir rašymus.
- `ProjectNotebookTranslationMixin` tvarko užrašų (notebook) failų nuskaitymą, Markdown ląstelių vertimą, kelių perrašymą, metaduomenis, atsisakymus ir rašymus.
- `ProjectImageTranslationMixin` tvarko vaizdų aptikimą, teksto išgavimą/vertimą, sugeneruotų vaizdų įrašymą ir metaduomenis.

Žemesnio lygio turinio API praleidžia projekto darbo eigą:

1. `translate_markdown_content` and `translate_notebook_content` verčia tik atmintyje esantį turinį.
2. `translate_image_content` verčia tekstą viename vaizde ir grąžina sugeneruotą vaizdo objektą.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` yra aiškūs postapdorojimo pagalbiniai įrankiai. Jie neatlieka vertimo ir neatlieka projekto įrašymų.

## Peržiūros eiga

Deterministinė peržiūros eiga yra:

1. Išanalizuoti CLI argumentus arba API parametrus.
2. Normalizuoti prašomus kalbų kodus.
3. Sukurti vieną arba kelis peržiūros taikinius iš `root_dir`, `root_dirs` arba `groups`.
4. Pasirinktinai apriboti šaltinio failus su `--changed-from`.
5. Paleisti deterministinius patikrinimus dėl struktūros, vertimo šviežumo, Markdown vientisumo ir vietinių nuorodų/vaizdų kelių.
6. Išvesti arba tekstinę informaciją, arba GitHub stiliaus Markdown.
7. Išeiti su klaida, kai randamos peržiūros klaidos.

Peržiūros eiga nereikalauja API raktų ir turėtų likti tinkama pull request CI. Pull request darbo eiga rašo patikrinimo santrauką kiekvieno paleidimo metu ir skelbia PR komentarą tik tada, kai `co-op-review` nepavyksta.

## Dokumentacijos svetainė

Dokumentacijos svetainė konfigūruojama pagal:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` katalogas yra kanoninis dokumentacijos šaltinis. Neįtraukite naujų galutinio vartotojo vadovų už šio katalogo ribų, nebent projektas sąmoningai pristato kitą publikuojamą dokumentacijos paviršių.

Sukonstruoti lokaliai:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Peržiūrėti lokaliai:

```bash
python -m mkdocs serve
```

Sugeneruota svetainė rašoma į `site/` katalogą, kuris yra ignoruojamas git.

## GitHub Pages workflow

`.github/workflows/docs.yml` kuria svetainę pull request metu ir diegia ją, kai vykdomas push į `main`.

Darbo eiga įdiegia:

```bash
pip install -r requirements-docs.txt
```

Dokumentacijos darbo eiga įdiegia tik dokumentacijos įrankių grandinę. `mkdocs.yml` nukreipia `mkdocstrings` į `src/`, tad viešosios API puslapiai gali būti sugeneruoti iš šaltinio medžio be pilno vykdymo laiko priklausomybių įdiegimo. Jei ateityje API dokumentacijai reikės importuoti pasirenkamus vykdymo laiko tiekėjus statybos metu, atnaujinkite tiek `.github/workflows/docs.yml`, tiek ir šį vadovą.

## Dokumentacijos kokybės baras

Prieš sujungiant dokumentacijos pakeitimus, paleiskite:

```bash
python -m mkdocs build --strict
git diff --check
```

Naudokite griežtą build režimą, kad sulaužytos nuorodos, neteisingi naršymo įrašai ir API atvaizdavimo problemos būtų aptiktos anksti.