# Karbantartói útmutató

Ez az oldal összefoglalja, hogyan kapcsolódnak egymáshoz az API, a CLI és a dokumentációs oldal.

## Publikus API határ

A stabil Python API innen kerül exportálásra:

```python
co_op_translator.api
```

A publikus API a következőkre tagolódik: tartalomfordítási segédletek, útvonal-átírási segédletek, projekt-orchesztráció és ellenőrzés:

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

Új publikus API-k hozzáadásakor frissítsd:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Kerüld a legalacsonyabb szintű `core` modulok dokumentálását stabil API-ként, kivéve ha a projekt kifejezetten támogatni kívánja azokat.

## CLI belépési pontok

A csomag az alábbi Poetry script-eket definiálja:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

A `src/co_op_translator/__main__.py` fájl a script név alapján irányít:

- `translate` meghívja `co_op_translator.cli.translate.translate_command`
- `evaluate` meghívja `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` meghívja `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` meghívja `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` megkerüli a `__main__.py`-t és közvetlenül meghívja a `co_op_translator.mcp.server:main`-t.

CLI opciók hozzáadásakor vagy módosításakor frissítsd:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP szerver

Az MCP szerver a következő helyen van megvalósítva:

```python
co_op_translator.mcp.server
```

A szerver szándékosan a publikus Python API-t burkolja be ahelyett, hogy az alacsonyabb szintű `core` modulokat hívná. Tartsd érintetlenül ezt a határt, hogy az MCP kliens, a Python hívók és a CLI ugyanazt a viselkedést osszák.

MCP eszközök hozzáadásakor vagy módosításakor frissítsd:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ha a publikus API felület változik

A repository fordító eszközök modellel hívhatók az MCP-n keresztül és sok fájlt képesek írni. Tartsd alapértelmezettként a `dry_run=True`-t, és kérj `confirm_write=True`-t nem-dry-run projektfordítás előtt.

## Fordítási folyamat

A magas szintű projektfordítási folyamat a következő:

1. CLI argumentumok vagy API paraméterek elemzése.
2. Az LLM konfiguráció érvényesítése a `LLMConfig` segítségével.
3. Az Azure AI Vision ellenőrzése, ha a képek fordítása van kiválasztva.
4. Nyelvkódok normalizálása.
5. Régi nyelvi mappa aliasainak felismerése.
6. A fordítási mennyiség becslése.
7. README nyelvi/tanfolyam szakaszainak frissítése, ha alkalmazható.
8. A projekt fordításának delegálása a `ProjectTranslator`-nek.
9. A `ProjectTranslator` a fájlfeldolgozást a `TranslationManager`-nek delegálja.

A `TranslationManager` különálló fájltípus-mixinekből áll:

- A `ProjectMarkdownTranslationMixin` kezeli a Markdown fájlok beolvasását, a tartalom fordítását, az útvonalak átírását, a metaadatokat, a felelősségkizárásokat és az írást.
- A `ProjectNotebookTranslationMixin` kezeli a notebook fájlok beolvasását, a Markdown-cellák fordítását, az útvonalak átírását, a metaadatokat, a felelősségkizárásokat és az írást.
- A `ProjectImageTranslationMixin` kezeli a képek felderítését, a szöveg kivonatolását/fordítását, a renderelt képek írását és a metaadatokat.

Az alacsonyabb szintű tartalom API-k kihagyják a projekt munkafolyamatot:

1. A `translate_markdown_content` és a `translate_notebook_content` csak memóriabeli tartalmat fordít.
2. A `translate_image_content` egyetlen képen található szöveget fordít és visszaad egy renderelt kép objektumot.
3. A `rewrite_markdown_paths` és a `rewrite_notebook_paths` explicit utófeldolgozó segédfüggvények. Nem végeznek fordítást és nem írnak projektfájlokat.

## Ellenőrzési folyamat

A determinisztikus ellenőrzési folyamat a következő:

1. CLI argumentumok vagy API paraméterek elemzése.
2. A kért nyelvkódok normalizálása.
3. Egy vagy több ellenőrzési célpont létrehozása a `root_dir`, `root_dirs` vagy `groups`-ból.
4. Opcionálisan szűkítheted a forrásfájlokat a `--changed-from` opcióval.
5. Futtasd a determinisztikus ellenőrzéseket a struktúra, a fordítás frissessége, a Markdown integritása és a helyi link/kép útvonalak ellen.
6. Nyomtasd ki szöveges formában vagy GitHub-stílusú Markdown-ként.
7. Kilép hibaállapottal, ha ellenőrzési hibákat talált.

Az ellenőrzési folyamat nem igényel API kulcsokat, és alkalmas kell maradjon pull request CI-hez. A pull request munkafolyamat minden futtatáskor egy ellenőrzési összefoglalót ír, és csak akkor tesz PR megjegyzést, ha a `co-op-review` sikertelen.

## Dokumentációs oldal

A dokumentációs oldal az alábbiakkal van konfigurálva:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

A `docs/` könyvtár a kanonikus dokumentációs forrás. Ne adj hozzá új végfelhasználói útmutatókat ezen könyvtáron kívülre, hacsak a projekt nem vezet be szándékosan egy másik közzétett dokumentációs felületet.

Helyben építés:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Helyi előnézet:

```bash
python -m mkdocs serve
```

A generált oldal a `site/` könyvtárba kerül, amelyet a git figyelmen kívül hagy.

## GitHub Pages munkafolyamat

A .github/workflows/docs.yml a pull requestek során építi az oldalt, és push esetén telepíti a `main`-re.

A munkafolyamat telepíti:

```bash
pip install -r requirements-docs.txt
```

A dokumentációs munkafolyamat csak a dokumentációs eszközkészletet telepíti. A `mkdocs.yml` a `mkdocstrings`-et a `src/`-ra mutatja, így a publikus API oldalak a forrásfából renderelhetők telepített teljes futtatási függőségek nélkül. Ha a jövőbeli API dokumentációkhoz szükség lesz opcionális futtatási providerek importálására a build során, frissítsd egyszerre a `.github/workflows/docs.yml`-t és ezt az útmutatót.

## Dokumentáció minőségi küszöb

A dokumentációs változtatások egyesítése előtt futtasd:

```bash
python -m mkdocs build --strict
git diff --check
```

Használj szigorú build beállításokat, hogy a törött linkek, érvénytelen navigációs bejegyzések és az API renderelési problémák korán hibára fussanak.