# Příručka správce

Tato stránka shrnuje, jak jsou API, CLI a dokumentační web provázány.

## Veřejná hranice API

Stabilní Python API je exportováno z:

```python
co_op_translator.api
```

Veřejné API je rozděleno na pomocníky pro překlad obsahu, pomocníky pro přepisování cest, orchestraci projektů a revizi:

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

`TranslationStateProvider` je perzistenční hranice pro hostované integrace.
Musí uchovávat vygenerované kandidáty odděleně od přijatých základních verzí, aby
nesloučený překlad nemohl stát zdrojem pravdy.

Při přidávání nových veřejných API aktualizujte:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- příslušné testy API v `tests/co_op_translator/`, například `test_api.py` nebo `test_review_api.py`

Vyvarujte se dokumentování nízkoúrovňových modulů `core` jako stabilního API, pokud projekt neplánuje jejich přímou podporu.

## Vstupní body CLI

Balíček definuje tyto Poetry skripty:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` směruje podle názvu skriptu:

- `translate` volá `co_op_translator.cli.translate.translate_command`
- `evaluate` volá `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` volá `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` volá `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` obchází `__main__.py` a volá `co_op_translator.mcp.server:main` přímo.

Při přidávání nebo změně možností CLI aktualizujte:

- příslušný příkaz v `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testy související s CLI, pokud se chování změní

## MCP server

Server MCP je implementován v:

```python
co_op_translator.mcp.server
```

Server úmyslně obaluje veřejné Python API místo volání nízkoúrovňových modulů `core`. Zachovejte tuto hranici, aby klienti MCP, volající z Pythonu a CLI sdíleli stejné chování.

Při přidávání nebo změně nástrojů MCP aktualizujte:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` pokud se změní veřejné API

Nástroje pro překlad repozitáře jsou volatelné modelem přes MCP a mohou zapisovat mnoho souborů. Zachovejte `dry_run=True` jako výchozí a vyžadujte `confirm_write=True` před překladem projektu mimo dry-run.

## Průběh překladu

Vysokoúrovňový průběh překladu projektu je:

1. Zpracovat argumenty CLI nebo parametry API.
2. Ověřit konfiguraci LLM pomocí `LLMConfig`.
3. Ověřit Azure AI Vision, pokud je vybrán překlad obrázků.
4. Normalizovat kódy jazyků.
5. Detekovat aliasy starších jazykových složek.
6. Odhadnout objem překladu.
7. Aktualizovat sekce README týkající se jazyka/kurzu, pokud je to relevantní.
8. Delegovat překlad projektu na `ProjectTranslator`.
9. `ProjectTranslator` deleguje zpracování souborů na `TranslationManager`.

`TranslationManager` se skládá z mixinů zaměřených na typy souborů:

- `ProjectMarkdownTranslationMixin` zpracovává čtení Markdown souborů, překlad obsahu, přepis cest, metadata, prohlášení o vyloučení odpovědnosti a zápisy.
- `ProjectNotebookTranslationMixin` zpracovává čtení notebooků, překlad Markdown buněk, přepis cest, metadata, prohlášení o vyloučení odpovědnosti a zápisy.
- `ProjectImageTranslationMixin` zajišťuje objevování obrázků, extrakci/překlad textu, zápisy renderovaných obrázků a metadata.

Nízkoúrovňová API pro obsah přeskočí projektový pracovní postup:

1. `translate_markdown_content` a `translate_notebook_content` překládají pouze obsah v paměti.
2. `translate_image_content` překládá text v jednom obrázku a vrací objekt renderovaného obrázku.
3. `rewrite_markdown_paths` a `rewrite_notebook_paths` jsou explicitní pomocníci pro post-processing. Neprovádějí žádný překlad ani žádné zápisy do projektu.

## Průběh revize

Deterministický průběh revize je:

1. Zpracovat argumenty CLI nebo parametry API.
2. Normalizovat požadované kódy jazyků.
3. Vytvořit jeden nebo více cílů revize z `root_dir`, `root_dirs` nebo `groups`.
4. Nepovinně omezit zdrojové soubory pomocí `--changed-from`.
5. Spustit deterministické kontroly struktury, aktuálnosti překladu, integrity Markdownu a lokálních cest odkazů/obrázků.
6. Vytisknout buď textový výstup, nebo Markdown ve stylu GitHubu.
7. Ukončit s chybou, když jsou nalezeny chyby revize.

Průběh revize nevyžaduje API klíče a zůstává dostupný pro lokální kontroly nebo volitelný CI spotřebitele. Tento repozitář nespouští `co-op-review` automaticky na každém pull requestu.

## Dokumentační web

Dokumentační web je konfigurován pomocí:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Adresář `docs/` je kanonickým zdrojem dokumentace. Přidávejte nové návody pro koncové uživatele mimo tento adresář pouze tehdy, pokud projekt záměrně zavádí jinou publikovanou dokumentační plochu.

Sestavte lokálně:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Náhled lokálně:

```bash
python -m mkdocs serve
```

Vygenerovaný web je zapsán do `site/`, které je ignorováno gitem.

## Pracovní postup GitHub Pages

`.github/workflows/docs.yml` sestavuje web při pull requestech a nasazuje jej při pushích do `main`.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

Workflow instaluje pouze nástroje dokumentace. `mkdocs.yml` ukazuje `mkdocstrings` na `src/` tak, aby stránky veřejného API mohly být vykresleny ze zdrojového stromu bez instalace plné sady runtime závislostí. Pokud budoucí API dokumentace budou vyžadovat import volitelných runtime providerů během sestavení, aktualizujte zároveň `.github/workflows/docs.yml` a tuto příručku.

## Prah kvality dokumentace

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Používejte přísné sestavení, aby se poškozené odkazy, neplatné položky navigace a problémy s vykreslením API odhalily brzy.