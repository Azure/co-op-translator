# Sprievodca pre udržiavateľa

Táto stránka zhrňuje, ako sú API, CLI a dokumentačný web navzájom prepojené.

## Hranica verejného API

Stabilné Python API je exportované z:

```python
co_op_translator.api
```

Verejné API je rozdelené na pomocníkov pre preklad obsahu, pomocníkov pre prepisovanie ciest, orchestráciu projektov a recenziu:

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

`TranslationStateProvider` predstavuje hranicu perzistencie pre hosťované integrácie.
Musí uchovávať generované kandidáty oddelene od akceptovaných základných verzií, tak
aby sa nezlúčený preklad nestal zdrojom pravdy.

Pri pridávaní nových verejných API aktualizujte:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- príslušné API testy v `tests/co_op_translator/`, napr. `test_api.py` alebo `test_review_api.py`

Vyhnite sa dokumentovaniu nižšej úrovne modulov `core` ako stabilného API, pokiaľ projekt nemá v úmysle ich priamo podporovať.

## Vstupné body CLI

Balík definuje tieto skripty v Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` rozhoduje podľa názvu skriptu:

- `translate` volá `co_op_translator.cli.translate.translate_command`
- `evaluate` volá `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` volá `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` volá `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` obchádza `__main__.py` a priamo volá `co_op_translator.mcp.server:main`.

Pri pridávaní alebo zmene možností CLI aktualizujte:

- príslušný príkaz v `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- testy súvisiace s CLI, ak sa zmení správanie

## MCP server

Server MCP je implementovaný v:

```python
co_op_translator.mcp.server
```

Server zámerne obalí verejné Python API namiesto priameho volania nižších modulov `core`. Zachovajte túto hranicu, aby MCP klienti, Python volajúci a CLI mali rovnaké správanie.

Pri pridávaní alebo zmene MCP nástrojov aktualizujte:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ak sa zmení verejné API

Nástroje pre preklad repozitára sú cez MCP volateľné modelom a môžu zapisovať veľa súborov. Nastavte `dry_run=True` ako predvolenú hodnotu a vyžadujte `confirm_write=True` pred prekladom projektu bez režimu dry-run.

## Priebeh prekladu

Hlavný postup prekladu projektu je:

1. Analyzujte argumenty CLI alebo parametre API.
2. Overte konfiguráciu LLM pomocou `LLMConfig`.
3. Overte Azure AI Vision, keď je vybraný preklad obrázkov.
4. Normalizujte kódy jazykov.
5. Zistite aliasy starších priečinkov jazykov.
6. Odhadnite objem prekladu.
7. Aktualizujte sekcie README pre jazyky/kurzy, ak je to vhodné.
8. Delegujte preklad projektu na `ProjectTranslator`.
9. `ProjectTranslator` deleguje spracovanie súborov na `TranslationManager`.

`TranslationManager` je zložený z mixinov zameraných na typy súborov:

- `ProjectMarkdownTranslationMixin` spracováva čítanie Markdown súborov, preklad obsahu, prepisovanie ciest, metadata, odmietnutia zodpovednosti a zápisy.
- `ProjectNotebookTranslationMixin` spracováva čítanie notebookov, preklad Markdown buniek, prepisovanie ciest, metadata, odmietnutia zodpovednosti a zápisy.
- `ProjectImageTranslationMixin` zabezpečuje vyhľadávanie obrázkov, extrakciu/preklad textu, zápis renderovaných obrázkov a metadata.

Nižšie úrovňové obsahové API obchádzajú projektový pracovný postup:

1. `translate_markdown_content` a `translate_notebook_content` prekladajú len obsah v pamäti.
2. `translate_image_content` preloží text v jednom obrázku a vráti renderovaný objekt obrázka.
3. `rewrite_markdown_paths` a `rewrite_notebook_paths` sú explicitní pomocníci pre postprocessing. Nevykonávajú žiadny preklad ani zápisy do projektu.

## Priebeh kontroly

Deterministický priebeh kontroly je:

1. Analyzujte argumenty CLI alebo parametre API.
2. Normalizujte požadované kódy jazykov.
3. Vytvorte jeden alebo viac cieľov kontroly z `root_dir`, `root_dirs` alebo `groups`.
4. Voliteľne obmedzte zdrojové súbory pomocou `--changed-from`.
5. Spustite deterministické kontroly štruktúry, čerstvosti prekladu, integrity Markdown a lokálnych ciest odkazov/obrázkov.
6. Vytlačte buď textový výstup alebo Markdown vo formáte GitHub.
7. Ukončite s chybou, ak sú zistené chyby kontroly.

Priebeh kontroly nevyžaduje API kľúče a zostáva dostupný pre lokálne kontroly alebo opt-in CI spotrebiteľov. Tento repozitár nespúšťa `co-op-review` automaticky pri každom pull requeste.

## Dokumentačná stránka

Dokumentačný web je nakonfigurovaný pomocou:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Adresár `docs/` je kanonický zdroj dokumentácie. Nepridávajte nové príručky pre koncových používateľov mimo tohto adresára, pokiaľ projekt zámerne nepredstaví ďalšiu publikovanú dokumentačnú plochu.

Zostavte lokálne:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Náhľad lokálne:

```bash
python -m mkdocs serve
```

Generovaný web je zapísaný do `site/`, ktorý je ignorovaný gitom.

## Pracovný postup GitHub Pages

`.github/workflows/docs.yml` zostavuje web pri pull requestoch a nasadí ho pri pushoch do `main`.

Pracovný postup inštaluje:

```bash
pip install -r requirements-docs.txt
```

Dokumentačný pracovný postup inštaluje iba nástroje pre dokumentáciu. `mkdocs.yml` ukazuje `mkdocstrings` na `src/`, takže stránky verejného API je možné vygenerovať zo zdrojového stromu bez inštalácie celého runtime balíka závislostí. Ak budú budúce API dokumenty vyžadovať importovanie voliteľných runtime providerov počas zostavovania, aktualizujte zároveň `.github/workflows/docs.yml` a tento sprievodca.

## Prah kvality dokumentácie

Pred zlúčením zmien v dokumentácii spustite:

```bash
python -m mkdocs build --strict
git diff --check
```

Použite prísne zostavenie, aby sa chybné odkazy, neplatné položky navigácie a problémy s renderovaním API odhalili včas.