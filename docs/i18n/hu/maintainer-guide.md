# Fenntartói útmutató

Ez az oldal összefoglalja, hogyan kapcsolódnak egymáshoz az API, a CLI és a dokumentációs oldal.

## Nyilvános API határa

A stabil Python API innen kerül exportálásra:

```python
co_op_translator.api
```

A nyilvános API tartalomfordítást segítő, útvonal-átírást segítő, projekt-orchesztrációs és ellenőrzési részekre van felosztva:

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

A `TranslationStateProvider` jelenti a hosztolt integrációk perzisztencia-határát.
El kell különítenie a generált jelölteket az elfogadott alapvonalaktól, így egy
össze nem olvasztott fordítás ne válhasson az igazság forrásává.

Új nyilvános API-k hozzáadásakor frissítse:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- a releváns API-tesztek a `tests/co_op_translator/` alatt, például a `test_api.py` vagy `test_review_api.py`

Kerülje az alacsonyabb szintű `core` modulok dokumentálását stabil API-ként, hacsak a projekt nem szándékozik közvetlenül támogatni azokat.

## CLI belépési pontok

A csomag a következő Poetry szkripteket határozza meg:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` scriptnév alapján irányít:

- `translate` meghívja a `co_op_translator.cli.translate.translate_command`
- `evaluate` meghívja a `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` meghívja a `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` meghívja a `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` kikerüli a `__main__.py`-t, és közvetlenül a `co_op_translator.mcp.server:main`-t hívja.

CLI-opciók hozzáadása vagy módosítása esetén frissítse:

- a megfelelő `src/co_op_translator/cli/*.py` parancs
- `docs/cli.md`
- CLI-hoz kapcsolódó tesztek, ha a viselkedés megváltozik

## MCP szerver

Az MCP szerver az alábbi fájlban van megvalósítva:

```python
co_op_translator.mcp.server
```

A szerver szándékosan a nyilvános Python API-t csomagolja be ahelyett, hogy az alacsonyabb szintű `core` modulokat hívná. Ezt a határt tartsa érintetlenül, hogy az MCP kliens, a Python hívók és a CLI ugyanazt a viselkedést osszák.

MCP eszközök hozzáadásakor vagy módosításakor frissítse:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ha a nyilvános API felülete megváltozik

A repozitórium fordítási eszközei MCP-n keresztül modellként hívhatók, és sok fájlt írhatnak. Tartsa alapértelmezettnek a `dry_run=True`-t, és követelje a `confirm_write=True` engedélyezését, mielőtt nem-dry-run projektfordítást indít.

## Fordítási folyamat

A magas szintű projektfordítási folyamat a következő:

1. CLI-argumentumok vagy API-paraméterek elemzése.
2. Az LLM konfiguráció érvényesítése `LLMConfig` segítségével.
3. Azure AI Vision ellenőrzése, ha képfordítás van kiválasztva.
4. Nyelvkódok normalizálása.
5. Régi nyelvi mappa aliasok felismerése.
6. A fordítás mennyiségének becslése.
7. A README nyelvi/kurzus szakaszainak frissítése, ha alkalmazható.
8. A projektfordítás delegálása a `ProjectTranslator`-hez.
9. `ProjectTranslator` átadja a fájlfeldolgozást a `TranslationManager`-nek.

A `TranslationManager` fókuszált fájltípusú mixinekből épül fel:

- `ProjectMarkdownTranslationMixin` kezeli a Markdown fájlok olvasását, a tartalom fordítását, az útvonal-átírást, a metaadatokat, a felelősségkizárásokat és a fájlok írását.
- `ProjectNotebookTranslationMixin` kezeli a notebook fájlok olvasását, a Markdown-cellák fordítását, az útvonal-átírást, a metaadatokat, a felelősségkizárásokat és a fájlok írását.
- `ProjectImageTranslationMixin` kezeli a képek felfedezését, a szöveg kinyerését/fordítását, a renderelt képek írását és a metaadatokat.

Az alacsonyabb szintű tartalom-API-k kihagyják a projekt munkafolyamatát:

1. A `translate_markdown_content` és `translate_notebook_content` csak a memóriában lévő tartalmat fordítja.
2. A `translate_image_content` egyetlen képből fordítja a szöveget és egy renderelt képobjektumot ad vissza.
3. A `rewrite_markdown_paths` és a `rewrite_notebook_paths` explicit utófeldolgozó segédek. Nem végeznek fordítást és nem írnak projektfájlokat.

## Áttekintési folyamat

A determinisztikus áttekintési folyamat a következő:

1. CLI-argumentumok vagy API-paraméterek elemzése.
2. A kért nyelvkódok normalizálása.
3. Egy vagy több áttekintési célt épít a `root_dir`, `root_dirs` vagy `groups` alapján.
4. Opcionálisan korlátozza a forrásfájlokat a `--changed-from` opcióval.
5. Futtasson determinisztikus ellenőrzéseket a struktúrára, a fordítás frissességére, a Markdown integritására és a helyi link/kép útvonalakra.
6. Szöveges kimenetet vagy GitHub-stílusú Markdown-t jelenítsen meg.
7. Sikertelenséggel lépjen ki, ha áttekintési hibákat talál.

Az áttekintési folyamat nem igényel API-kulcsokat, és elérhető helyi ellenőrzésekhez vagy opt-in fogyasztói CI-hez. Ez a repozitórium nem futtatja automatikusan a `co-op-review`-t minden pull requestnél.

## Dokumentációs oldal

A dokumentációs oldal a következővel van konfigurálva:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

A `docs/` könyvtár a kanonikus dokumentációs forrás. Ne adjon hozzá új végfelhasználói útmutatókat ezen a könyvtáron kívül, hacsak a projekt szándékosan nem vezet be egy másik közzétett dokumentációs felületet.

Helyben építés:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Előnézet helyben:

```bash
python -m mkdocs serve
```

A generált oldal a `site/` könyvtárba kerül, amelyet a git figyelmen kívül hagy.

## GitHub Pages munkafolyamat

`.github/workflows/docs.yml` a pull requesteken építi az oldalt és a `main`-re történő pushokkor telepíti.

A workflow a következőket telepíti:

```bash
pip install -r requirements-docs.txt
```

A dokumentációs workflow csak a dokumentációs eszközkészletet telepíti. A `mkdocs.yml` a `mkdocstrings`-et a `src/`-ra mutatja, így a nyilvános API-oldalak a forrásfáról renderelhetők a teljes futtatásidejű függőségek telepítése nélkül. Ha a jövőbeni API-dokumentációk a build során opcionális futtatói szolgáltatók importálását igénylik, frissítse együtt mindkettőt: `.github/workflows/docs.yml` és ezt az útmutatót.

## Dokumentációs minőségi követelmények

Mielőtt egyesítené a dokumentációs változtatásokat, futtassa:

```bash
python -m mkdocs build --strict
git diff --check
```

Használjon szigorú buildet, hogy a törött linkek, érvénytelen navigációs bejegyzések és az API-renderelési problémák korán hibát okozzanak.