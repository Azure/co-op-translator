# Prižiūrėtojo vadovas

Šiame puslapyje apibendrinama, kaip API, CLI ir dokumentacijos svetainė yra sujungti.

## Viešoji API riba

Stabili Python API eksportuojama iš:

```python
co_op_translator.api
```

Viešoji API yra suskirstyta į turinio vertimo pagalbininkus, kelių perrašymo pagalbininkus, projekto orkestraciją ir peržiūrą:

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

`TranslationStateProvider` yra patvarumo riba talpinamoms integracijoms.
Jis turi laikyti sugeneruotus kandidatus atskirai nuo priimtų bazinių versijų, kad
nesujungtas vertimas negalėtų tapti tiesos šaltiniu.

Pridėjus naujas viešąsias API, atnaujinkite:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- atitinkami API testai kataloge `tests/co_op_translator/`, pavyzdžiui `test_api.py` arba `test_review_api.py`

Venkite dokumentuoti žemesnio lygio `core` modulius kaip stabilias API, nebent projektas ketina juos tiesiogiai palaikyti.

## CLI įėjimo taškai

Paketas apibrėžia šiuos Poetry skriptus:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` paleidžia pagal skripto pavadinimą:

- `translate` kviečia `co_op_translator.cli.translate.translate_command`
- `evaluate` kviečia `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kviečia `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kviečia `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` apeina `__main__.py` ir tiesiogiai kviečia `co_op_translator.mcp.server:main`.

Pridėjus arba pakeitus CLI parinktis, atnaujinkite:

- atitinkamą `src/co_op_translator/cli/*.py` komandą
- `docs/cli.md`
- su CLI susijusius testus, jei elgsena pasikeičia

## MCP serveris

MCP serveris įgyvendintas faile:

```python
co_op_translator.mcp.server
```

Serveris sąmoningai apgaubia viešąją Python API, o ne kviečia žemesnio lygio `core` modulius. Išlaikykite šią ribą nepakitusią, kad MCP klientai, Python kvietėjai ir CLI turėtų tą patį elgesį.

Pridėjus arba pakeitus MCP įrankius, atnaujinkite:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jei keičiasi viešosios API apimtis

Repozitorijos vertimo įrankius galima kviesti per MCP ir jie gali įrašyti daug failų. Laikykite `dry_run=True` numatytąja reikšme ir reikalaukite `confirm_write=True` prieš vykdant projekto vertimą be dry-run režimo.

## Vertimo eiga

Aukšto lygio projekto vertimo eiga yra:

1. Išanalizuoti CLI argumentus arba API parametrus.
2. Patikrinti LLM konfigūraciją su `LLMConfig`.
3. Patikrinti Azure AI Vision, kai pasirenkamas vaizdų vertimas.
4. Normalizuoti kalbų kodus.
5. Aptikti senus kalbų aplankų slapyvardžius.
6. Įvertinti vertimo apimtį.
7. Atnaujinti README kalbos/kursų skirsnius, kai taikoma.
8. Deleguoti projekto vertimą `ProjectTranslator`.
9. `ProjectTranslator` perduoda failų apdorojimą `TranslationManager`.

`TranslationManager` susideda iš specializuotų failų tipo mixinų:

- `ProjectMarkdownTranslationMixin` tvarko Markdown failų nuskaitymą, turinio vertimą, kelių perrašymą, metaduomenis, atsakomybės išlygas ir įrašymus.
- `ProjectNotebookTranslationMixin` tvarko notebook failų nuskaitymą, Markdown langelių vertimą, kelių perrašymą, metaduomenis, atsakomybės išlygas ir įrašymus.
- `ProjectImageTranslationMixin` tvarko vaizdų paiešką, teksto išgavimą/vertimą, sugeneruotų vaizdų įrašymą ir metaduomenis.

Žemesnio lygio turinio API praleidžia projekto darbo eigą:

1. `translate_markdown_content` ir `translate_notebook_content` verčia tik atmintyje esantį turinį.
2. `translate_image_content` verčia tekstą viename vaizde ir grąžina sugeneruotą vaizdo objektą.
3. `rewrite_markdown_paths` ir `rewrite_notebook_paths` yra aiškūs post-procesavimo pagalbininkai. Jie neatlieka vertimo ir neatlieka projekto įrašymų.

## Peržiūros eiga

Deterministinė peržiūros eiga yra:

1. Išanalizuoti CLI argumentus arba API parametrus.
2. Normalizuoti prašomus kalbų kodus.
3. Sukurti vieną ar daugiau peržiūros taikinių iš `root_dir`, `root_dirs` arba `groups`.
4. Pasirinktinai apriboti šaltinio failus naudojant `--changed-from`.
5. Vykdyti deterministinius patikrinimus dėl struktūros, vertimo naujumo, Markdown vientisumo ir vietinių nuorodų/vaizdų kelių.
6. Išvesti arba tekstinę informaciją, arba GitHub stiliaus Markdown.
7. Baigti su klaida, kai randamos peržiūros klaidos.

Peržiūros eiga nereikalauja API raktų ir lieka prieinama vietiniams patikrinimams arba pasirinktinam vartotojo CI. Šis repozitorijus automatiškai nevykdo `co-op-review` kiekvienam pull request'ui.

## Dokumentacijos svetainė

Dokumentacijos svetainė konfigūruojama pagal:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Katalogas `docs/` yra kanoninis dokumentacijos šaltinis. Nepildykite naujų galutinių vartotojų gairių už šio katalogo ribų, nebent projektas sąmoningai įveda kitą publikuojamą dokumentacijos sritį.

Kurkite lokaliai:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Peržiūrėti lokaliai:

```bash
python -m mkdocs serve
```

Sugeneruota svetainė įrašoma į `site/`, kuris yra ignoruojamas git.

## GitHub Pages darbo eiga

`.github/workflows/docs.yml` sukuria svetainę per pull request'us ir diegia ją, kai vykdomas push į `main`.

Darbo eiga įdiegia šiuos paketus:

```bash
pip install -r requirements-docs.txt
```

Dokumentacijos darbo eiga įdiegia tik dokumentacijai reikalingą įrankių grandinę. `mkdocs.yml` nukreipia `mkdocstrings` į `src/`, tad viešosios API puslapiai gali būti renderinami iš šaltinio medžio be viso vykdymo laiko priklausomybių diegimo. Jei ateityje API dokumentacijai bus būtina importuoti pasirenkamus vykdymo laiko teikėjus statybos metu, atnaujinkite tiek `.github/workflows/docs.yml`, tiek šį vadovą.

## Dokumentacijos kokybės slenkstis

Prieš sujungiant dokumentacijos pakeitimus, paleiskite:

```bash
python -m mkdocs build --strict
git diff --check
```

Naudokite griežtą sudarymą, kad sulaužytos nuorodos, netinkami naršymo įrašai ir API atvaizdavimo klaidos būtų aptiktos anksti.