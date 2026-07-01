# Příručka pro správce

Tato stránka shrnuje, jak jsou API, CLI a dokumentační web propojeny.

## Hranice veřejného API

Stabilní Python API je exportováno z:

```python
co_op_translator.api
```

Veřejné API je uspořádáno do pomocníků pro překlad obsahu, přepisování cest, orchestraci projektů a revize:

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

Při přidání nových veřejných API aktualizujte:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevantní API testy pod `tests/co_op_translator/`, jako `test_api.py` nebo `test_review_api.py`

Vyvarujte se dokumentování nižších modulů `core` jako stabilního API, pokud projekt nezamýšlí tyto moduly přímo podporovat.

## Vstupní body CLI

Balíček definuje tyto skripty Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` přeposílá podle názvu skriptu:

- `translate` volá `co_op_translator.cli.translate.translate_command`
- `evaluate` volá `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` volá `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` volá `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` obchází `__main__.py` a volá `co_op_translator.mcp.server:main` přímo.

Při přidávání nebo změně možností CLI aktualizujte:

- příslušný `src/co_op_translator/cli/*.py` příkaz
- `docs/cli.md`
- testy související s CLI, pokud se chování změní

## MCP server

MCP server je implementován v:

```python
co_op_translator.mcp.server
```

Server záměrně obaluje veřejné Python API místo volání nižších modulů `core`. Zachovejte tuto hranici, aby klienti MCP, volající z Pythonu a CLI sdíleli stejné chování.

Při přidávání nebo změně nástrojů MCP aktualizujte:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` pokud se změní veřejné rozhraní API

Nástroje pro překlad repozitáře jsou volatelné modelem přes MCP a mohou zapisovat mnoho souborů. Zachovejte `dry_run=True` jako výchozí a vyžadujte `confirm_write=True` před překladem projektu mimo režim dry-run.

## Překladový tok

Vysoká úroveň toku překladu projektu je:

1. Zpracovat argumenty CLI nebo parametry API.
2. Ověřit konfiguraci LLM pomocí `LLMConfig`.
3. Ověřit Azure AI Vision, když je vybrán překlad obrázků.
4. Normalizovat kódy jazyků.
5. Detekovat zastaralé aliasy složek jazyků.
6. Odhadnout objem překladu.
7. Aktualizovat sekce README týkající se jazyka/kurzu, je-li to relevantní.
8. Přenechat překlad projektu `ProjectTranslator`.
9. `ProjectTranslator` deleguje zpracování souborů na `TranslationManager`.

`TranslationManager` je složen z mixinů zaměřených na typy souborů:

- `ProjectMarkdownTranslationMixin` zpracovává čtení Markdown souborů, překlad obsahu, přepisování cest, metadata, prohlášení o vyloučení odpovědnosti a zápisy.
- `ProjectNotebookTranslationMixin` zpracovává čtení notebooků, překlad buňek Markdown, přepisování cest, metadata, prohlášení o vyloučení odpovědnosti a zápisy.
- `ProjectImageTranslationMixin` zpracovává objevování obrázků, extrakci/překlad textu, zápisy renderovaných obrázků a metadata.

Nižší obsahová API vynechávají pracovní postup projektu:

1. `translate_markdown_content` a `translate_notebook_content` překládají pouze obsah v paměti.
2. `translate_image_content` překládá text v jednom obrázku a vrací renderovaný objekt obrázku.
3. `rewrite_markdown_paths` a `rewrite_notebook_paths` jsou explicitní pomocníci pro post-processing. Nevykonávají žádný překlad ani zápisy projektu.

## Revizní tok

Deterministický průběh revize je:

1. Zpracovat argumenty CLI nebo parametry API.
2. Normalizovat požadované kódy jazyků.
3. Vytvořit jeden nebo více revizních cílů z `root_dir`, `root_dirs` nebo `groups`.
4. Volitelně omezit zdrojové soubory pomocí `--changed-from`.
5. Spustit deterministické kontroly struktury, čerstvosti překladu, integrity Markdownu a lokálních cest odkazů/obrázků.
6. Vytisknout buď textový výstup, nebo Markdown ve stylu GitHubu.
7. Ukončit s chybou, pokud jsou nalezeny chyby revize.

Revizní tok nevyžaduje API klíče a měl by zůstat vhodný pro CI v pull requestech. Workflow pro pull request zapíše souhrn kontroly při každém spuštění a zveřejní komentář k PR pouze tehdy, když `co-op-review` selže.

## Dokumentační web

Dokumentační web je konfigurován pomocí:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Adresář `docs/` je kanonickým zdrojem dokumentace. Nepřidávejte nové příručky pro koncové uživatele mimo tento adresář, pokud projekt záměrně nezavádí další publikovanou dokumentační plochu.

Sestavit lokálně:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Náhled lokálně:

```bash
python -m mkdocs serve
```

Vygenerovaný web je zapsán do `site/`, který je ignorován gitem.

## GitHub Pages workflow

`.github/workflows/docs.yml` sestavuje web při pull requestech a nasazuje jej při pushích do `main`.

Workflow instaluje:

```bash
pip install -r requirements-docs.txt
```

Workflow dokumentace instaluje pouze nástroje dokumentačního řetězce. `mkdocs.yml` směruje `mkdocstrings` na `src/`, takže stránky veřejného API lze vykreslit ze stromu zdrojů bez instalace celého souboru runtime závislostí. Pokud budou budoucí dokumentace API vyžadovat import volitelných poskytovatelů runtime během sestavení, aktualizujte současně `.github/workflows/docs.yml` i tuto příručku.

## Kvalita dokumentace

Před sloučením změn v dokumentaci spusťte:

```bash
python -m mkdocs build --strict
git diff --check
```

Používejte přísné sestavení, aby se vadné odkazy, neplatné položky navigace a problémy s vykreslováním API projevily brzy.