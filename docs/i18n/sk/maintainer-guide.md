# Sprievodca pre správcu

Táto stránka zhrňuje, ako sú API, CLI a dokumentačná stránka navzájom prepojené.

## Verejná hranica API

Stabilné Python API je exportované z:

```python
co_op_translator.api
```

Verejné API je usporiadané do pomocníkov pre preklad obsahu, pomocníkov pre prepisovanie ciest, orchestráciu projektov a revíziu:

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

Pri pridávaní nových verejných API aktualizujte:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevantné testy API v `tests/co_op_translator/`, napríklad `test_api.py` alebo `test_review_api.py`

Vyhnite sa dokumentovaniu nižších modulov `core` ako stabilné API, pokiaľ projekt neplánuje priamo ich podporovať.

## Vstupné body CLI

Balík definuje tieto Poetry skripty:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` smeruje podľa názvu skriptu:

- `translate` volá `co_op_translator.cli.translate.translate_command`
- `evaluate` volá `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` volá `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` volá `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` obchádza `__main__.py` a priamo volá `co_op_translator.mcp.server:main`.

Pri pridávaní alebo zmene možností CLI aktualizujte:

- príslušný príkaz v `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testy týkajúce sa CLI, ak sa zmení správanie

## MCP server

MCP server je implementovaný v:

```python
co_op_translator.mcp.server
```

Server zámerne obaluje verejné Python API namiesto volania nižších modulov `core`. Zachovajte túto hranicu nedotknutú, aby klienti MCP, Python volania a CLI zdieľali rovnaké správanie.

Pri pridávaní alebo zmene nástrojov MCP aktualizujte:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`, ak sa zmení povrch verejného API

Nástroje na preklad repozitára sú volateľné modelom cez MCP a môžu zapisovať množstvo súborov. Zachovajte `dry_run=True` ako predvolenú hodnotu a vyžadujte `confirm_write=True` pred prekladom projektu, ktorý nie je v režime `dry_run`.

## Tok prekladu

Vysokoúrovňový priebeh prekladu projektu je:

1. Rozparsovať argumenty CLI alebo parametre API.
2. Overiť konfiguráciu LLM pomocou `LLMConfig`.
3. Overiť Azure AI Vision, keď je zvolený preklad obrázkov.
4. Normalizovať kódy jazykov.
5. Zistiť aliasy starších jazykových priečinkov.
6. Odhadnúť objem prekladu.
7. Aktualizovať sekcie README o jazyku/kurze, keď je to vhodné.
8. Delegovať preklad projektu na `ProjectTranslator`.
9. `ProjectTranslator` deleguje spracovanie súborov na `TranslationManager`.

`TranslationManager` sa skladá z mixinov zameraných na typy súborov:

- `ProjectMarkdownTranslationMixin` spracováva čítanie Markdown súborov, preklad obsahu, prepisovanie ciest, metadata, vyhlásenia o zodpovednosti a zápisy.
- `ProjectNotebookTranslationMixin` spracováva čítanie notebook súborov, preklad Markdown buniek, prepisovanie ciest, metadata, vyhlásenia o zodpovednosti a zápisy.
- `ProjectImageTranslationMixin` spracováva zisťovanie obrázkov, extrakciu/preklad textu, zápisy renderovaných obrázkov a metadata.

Nižšie úrovňové obsahové API obchádzajú projektový pracovný postup:

1. `translate_markdown_content` a `translate_notebook_content` prekladajú iba obsah v pamäti.
2. `translate_image_content` prekladá text v jednom obrázku a vracia renderovaný objekt obrázka.
3. `rewrite_markdown_paths` a `rewrite_notebook_paths` sú explicitné pomocné nástroje po spracovaní. Nevykonávajú žiadny preklad ani žiadne zápisy do projektu.

## Priebeh kontroly

Deterministický priebeh kontroly je:

1. Rozparsovať argumenty CLI alebo parametre API.
2. Normalizovať požadované kódy jazykov.
3. Vytvoriť jeden alebo viac cieľov kontroly z `root_dir`, `root_dirs` alebo `groups`.
4. Voliteľne obmedziť zdrojové súbory pomocou `--changed-from`.
5. Spustiť deterministické kontroly štruktúry, čerstvosti prekladu, integrity Markdown a lokálnych ciest odkazov/obrázkov.
6. Vytlačiť buď textový výstup alebo Markdown vo formáte GitHub.
7. Ukončiť s chybou, keď sa nájdu chyby kontroly.

Priebeh kontroly nevyžaduje API kľúče a mal by zostať vhodný pre CI pull requestov. Workflow pull requestu zapisuje súhrn kontroly pri každom spustení a komentár do PR sa uverejní len keď `co-op-review` zlyhá.

## Dokumentačná stránka

Stránka dokumentácie je konfigurovaná pomocou:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Adresár `docs/` je kanonický zdroj dokumentácie. Nepridávajte nové návody pre koncových používateľov mimo tohto adresára, pokiaľ projekt zámerne nepredstaví inú publikovanú dokumentačnú plochu.

Zostavenie lokálne:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Náhľad lokálne:

```bash
python -m mkdocs serve
```

Vygenerovaná stránka sa zapíše do `site/`, ktorý je ignorovaný gitom.

## Workflow pre GitHub Pages

.github/workflows/docs.yml zostavuje stránku pri pull requestoch a nasadí ju pri pushoch do `main`.

Workflow inštaluje:

```bash
pip install -r requirements-docs.txt
```

Workflow dokumentácie inštaluje iba nástroje dokumentácie. `mkdocs.yml` smeruje `mkdocstrings` na `src/`, takže stránky verejného API je možné vyrenderovať zo zdrojového stromu bez inštalácie kompletnej sady runtime závislostí. Ak budú budúce dokumenty API vyžadovať importovanie voliteľných runtime providerov počas zostavovania, aktualizujte súčasne `.github/workflows/docs.yml` a tento sprievodca.

## Prah kvality dokumentácie

Pred zlúčením zmien dokumentácie spustite:

```bash
python -m mkdocs build --strict
git diff --check
```

Používajte prísne zostavenia, aby chyby ako rozbité odkazy, neplatné položky navigácie a problémy s renderovaním API zlyhali včas.