# Python API

A stabil, nyilvános Python API a `co_op_translator.api`-ból van exportálva. A legtöbb integráció az alábbi munkafolyamatok egyikét használja:

| Forgatókönyv | Használd ezt, amikor | Fő API-k |
| --- | --- | --- |
| Egyéni fájlok vagy dokumentumok fordítása | Az alkalmazásod beolvassa a forrástartalmat, a Co-op Translator-hoz fordul a fordításhoz, és eldönti, hova mentse az eredményt. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tartalom előkészítése host-ügynök fordításhoz | Az MCP hosztod vagy az alkalmazásmodell darabokat fordít, míg a Co-op Translator a darabolást és az újraépítést kezeli. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Egy teljes repozitórium fordítása | Azt szeretnéd, hogy a Python API a CLI-hez hasonlóan viselkedjen és kezelje a felfedezést, kimeneti útvonalakat, metaadatokat, takarítást és az írásokat. | `run_translation` |

A `core`, `config`, `review` és `utils` alatti alacsonyabb szintű modulok többsége implementációs részlet, amelyet ezek az API belépési pontok használnak.

Az MCP kliensek ugyanazt a nyilvános API-t használják az [MCP szerver](mcp.md)on keresztül. Ezt az oldalt használd, amikor közvetlenül Pythont hívsz, és az MCP útmutatót használd, amikor a Co-op Translatort egy ügynöknek vagy szerkesztőnek teszed elérhetővé. Ha a CLI, a Python API és az MCP között döntesz, kezdd a [Válassza ki a munkafolyamatot](workflows.md)-tal.

## Első API-folyamat

Kezdd itt, ha Python kódból hívod a Co-op Translatort:

1. Állíts be egy LLM szolgáltatót a [Konfiguráció](configuration.md) szerint, hacsak nem csak Markdown vagy notebook darabokat készítesz elő host-ügynök fordításhoz.
2. Döntsd el, hogy az alkalmazásod kezeli-e a fájl I/O-t.
3. Használd a tartalom API-kat, amikor az alkalmazásod egyedi fájlokat olvas és ír.
4. Használd a `run_translation`-t, amikor a Co-op Translator-nek úgy kell feldolgoznia egy repozitóriumot, mint a CLI.
5. Használd a `run_review`-t a fordítás után, ha determinisztikus ellenőrzésekre van szükséged automatizálásban.

| Cél | Kezdő API |
| --- | --- |
| Egy Markdown sztring vagy fájl fordítása | `translate_markdown_content` |
| Egy jegyzetfüzet payload fordítása | `translate_notebook_content` |
| Egy kép fordítása | `translate_image_content` |
| Hagyj egy hoszt ügynököt Markdown vagy jegyzetfüzet darabok fordítására | `start_markdown_agent_translation` vagy `start_notebook_agent_translation` |
| A lefordított linkek átírása miután kiválasztottad a kimeneti útvonalat | `rewrite_markdown_paths` vagy `rewrite_notebook_paths` |
| Egy teljes repozitórium fordítása | `run_translation` |
| A lefordított kimenet ellenőrzése | `run_review` |

## 1. forgatókönyv: Egyes fájlok vagy dokumentumok fordítása

Használd ezt a munkafolyamatot, ha már van egy fájlod, szerkesztő puffered, notebook payloadod, MCP kérésetek, vagy egy egyedi pipeline bemenet. A kódod kezeli a fájl I/O-t:

1. Olvasd be a forrástartalmat.
2. Hívd meg a tartalom fordítási API-t.
3. Opcionálisan hívd meg az útvonal-átíró API-t, ha a lefordított tartalmat egy projekt fordítási mappájába fogod írni.
4. Mentsd el vagy add vissza az eredményt az alkalmazásodból.

A tartalom fordítási API-k nem futtatnak projekt-felfedezést, nem írnak metaadatot, nem fűznek hozzá nyilatkozatot és nem írják át automatikusan a linkeket.

### Markdown fájl

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Ha a lefordított Markdown nem egy Co-op Translator projekt elrendezésében fog élni, hagyd ki a `rewrite_markdown_paths`-t és mentsd el közvetlenül a lefordított stringet.

### Notebook fájl

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

A `translate_notebook_content` lefordítja a Markdown cellákat és megtartja a nem-Markdown cellákat. Az útvonal-átírás csak a Markdown cellákra vonatkozik.

### Kép fájl

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

A `translate_image_content` beolvassa a forrásképet és egy renderelt `PIL.Image.Image`-t ad vissza. Nem ír lefordított kép metaadatot.

## 2. forgatókönyv: Egy teljes repozitórium fordítása

Használd ezt a munkafolyamatot, amikor azt szeretnéd, hogy a Python API úgy viselkedjen, mint a `translate` CLI. A `run_translation` felderíti a támogatott fájlokat, lefordítja a kiválasztott tartalomtípusokat, átírja az útvonalakat, írja a kimeneti fájlokat, frissíti a metaadatokat és elvégzi a fordítással kapcsolatos karbantartási feladatokat, például a tisztítást.

A `run_translation` az ajánlott projekt-orchestration belépési pont. A `translate_project` kompatibilitási aliaszként ugyanazzal a viselkedéssel van exportálva.

Fordítsd a Markdown fájlokat a jelenlegi repozitóriumban koreaira és japánra:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Csak a jegyzetfüzeteket fordítsd egy adott projektgyökérből:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Tekintsd meg a fordítás volumenét fájlok írása nélkül:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Strukturált előrehaladási események rögzítése egy integrációhoz:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Tárolja a payloadot a job-event táblájában, vagy streamelje azt a felhasználói felületére.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Az események a verziózott sémát használják: `co-op.translation.event.v1`. Az integrációknak stabil mezőktől kell függeniük, mint például a `type` és a `stage_key`, nem az emberi olvasatú konzol szövegtől vagy a `stage_label`-től.



Több tartalomgyökér fordítása egy hívásban:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Írd a fordításokat explicit kimeneti csoportokba:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Használj nyelvenkénti helykitöltőt, amikor minden nyelvnek egy beágyazott alkönyvtárat kell tartalmaznia:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Ha a `markdown`, `notebook` vagy `images` egyik sem van beállítva, az API minden támogatott típust fordít: Markdown, notebookokat és képeket.

### Az elfogadott emberi szerkesztések megőrzése egy fordítási állapot-szolgáltatóval

Alapértelmezés szerint a Co-op Translator megtartja a meglévő fájlszintű viselkedést: amikor egy
Markdown forrás elavult, a teljes lefordított fájl újragenerálódik. A hosztolt
integrációk opcionálisan átadhatnak egy `TranslationStateProvider`-t az emberi
szerkesztések megőrzéséhez a nem változott forrásblokkokban.

A szolgáltató biztosítja az utoljára elfogadott forrás/cél párost és rögzíti az összes új
jelöltet. Az elfogadás továbbra is az integráció felelőssége — például
egy fordítási pull request egyesítése után:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Markdown fájlok esetén, amelyeknél érvényes elfogadott kiindulási állapot van, a Co-op Translator igazítja a
felső szintű Markdown blokkokat. A változatlan forrásblokkok újrahasználják a jelenlegi lefordított
blokkokat, beleértve az emberek által végzett szerkesztéseket; a megváltozott vagy hozzáadott forrásblokkok fordításra kerülnek;
a törölt forrásblokkok eltávolításra kerülnek. Ha az igazítás kétértelmű,
a célstruktúra megváltozott, egy blokk fordítása érvénytelen, vagy nem áll rendelkezésre kiindulási állapot,
a Co-op Translator biztonságosan visszatér a meglévő teljes fájl
fordítási úthoz.

Ez az API dokumentum szintű fordítási állapotot tárol, nem több-dokumentumos kifejezés- vagy szegmens fordítási memóriát. Jelenleg a Markdown projektfordításra vonatkozik.
A jegyzetfüzetek és a képek viselkedése változatlan. Az `update=True` átadása továbbra is teljes újragenerálást kér.



Ha egy vagy több fájl nem fordítható le, a `run_translation` egy
`RuntimeError`-t dob a projekt munkafolyamat befejezése után ahelyett, hogy sikeres futást jelentene hiányzó kimenettel.
Az integrációknak ezt egy sikertelen feladatként kell kezelniük, és meg kell őrizniük az előző elfogadott fordítási állapotot.


## A lefordított kimenet áttekintése

A `run_review` determinisztikus fordítási ellenőrzéseket futtat LLM vagy Vision hitelesítési adatok nélkül.

!!! note "Beta"
    A `run_review` egy béta determinisztikus ellenőrző API. Nem hív modell-szolgáltatókat és nem ír fájlokat, de a vizsgálati és hibasémák változhatnak.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-only fordítás után ugyanazzal a terjedelemmel végezd az ellenőrzést:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

A `readme_only=True` csak az egyes konfigurált forrásgyökerek alatti `README.md`-eket ellenőrzi,
beleértve az egyedi `groups`-okat és kimeneti könyvtárakat. Más dokumentumok és beágyazott
README-k ki vannak zárva. Egy hiányzó forrás README `ValueError`-t dob; sikertelen
fordítási ellenőrzések `RuntimeError`-t váltanak ki.

Ellenőrizd csak az alaprefhez képest megváltozott fájlokat és nyomtass GitHub-stílusú kimenetet:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Másolás-beillesztés API példák

Fordíts Markdown tartalmat fájlírás nélkül:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Fordítsd le és írd át a Markdown linkeket:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Fordíts egy repozitóriumot Pythonból:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Több gyökér fordítása:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Szójegyzék kifejezéseinek megőrzése:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Nyilvános belépési pontok

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Tartalomfordítási API-k

A tartalomfordítási API-k azoknak az integrációknak szólnak, amelyeknél a tartalom már memóriában van, például egy szerkesztő bővítmény, MCP eszköz, notebook feldolgozó vagy egy egyedi pipeline.

| Funkció | Bemenet | Kimenet | Fájl I/O | Megjegyzések |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nincs | Aszinkron. Csak a Markdown tartalmat fordítja. Nem ír át linkeket, nem ír metaadatot, és nem fűz hozzá nyilatkozatot. |
| `translate_notebook_content` | Notebook JSON `str` vagy `dict` | Notebook JSON `str` | Nincs | Aszinkron. Markdown cellákat fordít és megtartja a nem-Markdown cellákat. Nem ír át linkeket, nem ír metaadatot, és nem fűz hozzá nyilatkozatot. |
| `translate_image_content` | Kép útvonal | `PIL.Image.Image` | Csak a forrásképet olvassa | Szinkron. Kinyeri és lefordítja a képen található szöveget, majd egy renderelt képet ad vissza. Nem menti a lefordított kép metaadatait. |

A `translate_markdown_content` és a `translate_notebook_content` opcionálisan elfogad egy `source_path`-ot az opcióikon keresztül. Az útvonalat kontextusként továbbítják a fordítónak; a hívók felelőssége marad a projekt-specifikus útvonal-átírás a fordítás után.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Ugyanezek az opciók szótárként is átadhatók:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Ügynök által támogatott fordítási API-k

Az ügynök által segített API-k nem hívják a Co-op Translatorhoz konfigurált LLM szolgáltatót. Elkészítik a Markdown vagy notebook darabokat egy hoszt ügynök számára fordításra, majd rekonstruálják a végleges tartalmat a lefordított darabokból.

| Funkció | Cél |
| --- | --- |
| `start_markdown_agent_translation` | Visszaad egy önálló Markdown munkát darabokkal, promptokkal és rekonstruálási állapottal. |
| `finish_markdown_agent_translation` | Rekonstruálja a Markdown-t egy munkából és a hoszt-ügynök által lefordított darabokból. |
| `start_notebook_agent_translation` | Visszaad egy notebook munkát Markdown-cellás darabokkal a hoszt-ügynök fordításához. |
| `finish_notebook_agent_translation` | Rekonstruálja a notebook JSON-t miközben megtartja a kódcella-kat, kimeneteket és metaadatokat. |

Ezt a munkafolyamatot elsősorban MCP hosztoknak szánják. Ha gyártási repozitórium fordításra van szükséged úgy, hogy a Co-op Translator kezeli a szolgáltató hívásokat, használd a `translate_markdown_content`, `translate_notebook_content` vagy `run_translation`-t.

## Útvonal újraíró API-k

Az útvonal-átíró API-k nem végeznek fordítást. Frissítik a linkeket és a frontmatter útvonalakat miután a hívók ismerik a forrás útvonalat, a lefordított cél útvonalát és a projekt elrendezését.

| Funkció | Hatókör | Megjegyzések |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown törzs és frontmatter | Átírja a Markdown linkeket és a támogatott frontmatter útvonal mezőket egy lefordított célhoz. |
| `rewrite_notebook_paths` | Notebook JSON-ban lévő Markdown cellák | Alkalmazza a Markdown útvonal-átírást minden Markdown cellára és a nem-Markdown cellákat változatlanul hagyja. |

A `policy` argumentum lehet egy szótár a következő mezőkkel:

| Mező | Kötelező | Cél |
| --- | --- | --- |
| `language_code` | Igen | Cél nyelvkód, például `"ko"` vagy `"pt-BR"`. |
| `root_dir` | Nem | Forrás projekt gyökér. Alapértelmezett `"."`. |
| `translations_dir` | Nem | Szöveg fordítás kimeneti könyvtára. Alapértelmezett a `root_dir` alatti `translations`. |
| `translated_images_dir` | Nem | Lefordított képek kimeneti könyvtára. Alapértelmezett a `root_dir` alatti `translated_images`. |
| `translation_types` | Nem | Engedélyezett fordítási típusok. Alapértelmezett: Markdown, notebookok és képek. |
| `lang_subdir` | Nem | Opcionális alkönyvtár minden nyelvi mappa alatt. |

## Projektfordítási paraméterek

| Paraméter | Típus | Alapértelmezett | Cél |
| --- | --- | --- | --- |
| `language_codes` | `str` | Kötelező | Szóközzel elválasztott cél nyelvi kódok, például `"ko ja fr"`, vagy `"all"`. Alias kódok normalizálódnak kanonikus BCP 47 értékekre. |
| `root_dir` | `str` | `"."` | Projekt gyökér egyetlen fordítási célhoz. Figyelmen kívül hagyott, ha `root_dirs` vagy `groups` meg vannak adva. |
| `update` | `bool` | `False` | Töröld és hozd létre újra a meglévő fordításokat a kiválasztott nyelvekhez. |
| `images` | `bool` | `False` | Tartalmazza a kép fordítást. Azure AI Vision konfigurációt igényel. |
| `markdown` | `bool` | `False` | Tartalmazza a Markdown fordítást. |
| `notebook` | `bool` | `False` | Tartalmazza a Jupyter notebook fordítást. |
| `debug` | `bool` | `False` | Engedélyezze a hibakeresési naplózást. |
| `save_logs` | `bool` | `False` | Mentse a DEBUG szintű naplófájlokat a gyökér `logs/` könyvtár alá. |
| `yes` | `bool` | `True` | A promptok automatikus megerősítése programozott és CI használat esetén. |
| `add_disclaimer` | `bool` | `False` | Gépi fordításra vonatkozó nyilatkozatok hozzáadása a lefordított Markdown fájlokhoz és notebookokhoz. |
| `translations_dir` | `str \| None` | `None` | Egyéni szövegfordítás-kimeneti könyvtár. A relatív útvonalak minden gyökérhez viszonyítva értelmeződnek. |
| `image_dir` | `str \| None` | `None` | Egyéni lefordított képek kimeneti könyvtára. A relatív útvonalak minden gyökérhez viszonyítva értelmeződnek. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Több gyökér, amelyek közösen használják ugyanazokat a kimeneti beállításokat. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` párok. Elsőbbséget élvez a `root_dirs`. |
| `repo_url` | `str \| None` | `None` | A README nyelvi táblázathoz használt tároló URL-je. |
| `glossaries` | `Iterable[str] \| None` | `None` | A fordítás során megőrzendő szószedeti kifejezések. A duplikátumok és üres kifejezések normalizálódnak. |
| `dry_run` | `bool` | `False` | A fordítási mennyiség becslése és a migrációs viselkedés előnézete fájlírás nélkül. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Opcionális 'accepted-baseline' és 'candidate' perzisztencia-adapter inkrementális Markdown-frissítésekhez. Ennek elhagyása megőrzi a meglévő teljes fájl viselkedést. |

## Felülvizsgálati paraméterek

`run_review` szándékosan tükrözi a `run_translation` aláírását, ahol lehetséges, hogy az automatizálás minimális elágazással tudjon átváltani fordítási és felülvizsgálati munkafolyamatok között.

| Paraméter | Típus | Alapértelmezett | Cél |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | A felülvizsgálandó cél nyelvi mappák. Szóközzel elválasztott karakterláncok és iterálhatók is elfogadottak. `"all"` minden felismert fordítási nyelvet felülvizsgál. |
| `root_dir` | `str` | `"."` | Egyetlen felülvizsgálati cél projektgyökere. Figyelmen kívül hagyva, ha `root_dirs` vagy `groups` van megadva. |
| `markdown` | `bool` | `False` | Markdown és MDX forrásfájlok bevonása. |
| `notebook` | `bool` | `False` | Jupyter notebook forrásfájlok bevonása. |
| `images` | `bool` | `False` | A fordítási opciókkal való párhuzam miatt fenntartott. A képekre mutató hivatkozások ellenőrzése a Markdown alapján történik. |
| `translations_dir` | `str \| None` | `None` | Egyéni szövegfordítás-kimeneti könyvtár. A relatív útvonalak minden gyökérhez viszonyítva értelmeződnek. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Több gyökér, amelyek ugyanazokat a kimeneti beállításokat használják. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` párok. Elsőbbséget élvez a `root_dirs`. |
| `changed_from` | `str \| None` | `None` | A felülvizsgálatot korlátozó Git ref a megváltozott forrásfájlokra. |
| `readme_only` | `bool` | `False` | Csak az egyes forrásgyökerek alatti `README.md`-eket vizsgálja. Hiányzó forrás README esetén `ValueError` kerül kiváltásra. |
| `output_format` | `str` | `"text"` | A felülvizsgálat kimeneti formátuma. Támogatott értékek: `"text"` és `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Figyelmeztetéseket a hibák mellett hibaként kezelni. |
| `debug` | `bool` | `False` | Debug naplózás engedélyezése. |
| `save_logs` | `bool` | `False` | DEBUG szintű naplófájlok mentése a gyökér `logs/` könyvtár alá. |

Ha egyike sem `markdown`, `notebook` vagy `images` van beállítva, az API ahol alkalmazható, felülvizsgálja a Markdown-t, a notebookokat és a képhivatkozásokat. A felülvizsgálat nem hív LLM szolgáltatót és nem igényel API kulcsokat.

## Konfigurációs követelmények

A szolgáltató által támogatott fordítási API-k fordítás előtt szolgáltató konfigurációt igényelnek:

- A Markdown és notebook fordításhoz LLM szolgáltató szükséges. Konfiguráljon Azure OpenAI-t, OpenAI-t vagy Anthropic-ot.
- A képfordításhoz az LLM szolgáltató mellett Azure AI Vision szükséges.
- A `run_translation` könnyű kapcsolatellenőrzéseket futtat, mielőtt a projektfordítás elkezdődik.
- Az ügynök által segített `start_*_agent_translation` és `finish_*_agent_translation` API-k nem hívják a Co-op Translator LLM szolgáltatókat. A host alkalmazás vagy az MCP ügynök fordítja le az előkészített darabokat.
- A `rewrite_markdown_paths`, `rewrite_notebook_paths` és `run_review` determinisztikusak és nem igényelnek szolgáltatói hitelesítő adatokat.

Szükséges Azure OpenAI változók:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Szükséges OpenAI változók:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Szükséges Anthropic változók:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` és `ANTHROPIC_MAX_TOKENS` opcionálisak. A Microsoft Agent Framework az alapértelmezett modellkliens minden szolgáltatóhoz a Co-op Translator 0.22.0 verziójától kezdve. A Semantic Kernel ideiglenesen még kiválasztható a `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` beállítással, de ez elavulási figyelmeztetést okoz; lásd a [konfigurációt](configuration.md#model-client-backend) az ütemezett eltávolítási tervért.

A képfordításhoz szükséges Azure AI Vision változók:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` determinisztikus és nem igényel LLM vagy Azure AI Vision konfigurációt.

## Viselkedési megjegyzések

- A tartalomfordító API-k elkülönítik a fordítást és a projektútvonalak átírását. Ha a lefordított tartalomhoz meg kell igazítani a projektrelív útvonalakat egy célhelyhez, hívja meg kifejezetten a `rewrite_markdown_paths` vagy `rewrite_notebook_paths` függvényt.
- A projekt-orchestration API-k projektviselkedést adnak a tartalomfordítás köré, beleértve a fájl-felderítést, írásokat, útvonal-átírást, metaadatokat, takarítást és opcionális lemondásokat.
- A `run_translation` a CLI által használt Rich-alapú riporteren keresztül jeleníti meg az előrehaladást és a becslési összefoglalókat. Nem interaktív kimenet esetén egyszerű szövegre esik vissza.
- A `dry_run=True` virtuális README frissítéseket használva számítja ki a becsléseket, de nem írja a README-t vagy a fordítási fájlokat.
- A `groups`-ok egymás után kerülnek feldolgozásra. Egyetlen összesített becslés kerül kiírásra, mielőtt a munka elkezdődik.
- Ha képfordítás van kiválasztva, a hiányzó Vision konfiguráció hibát okoz a fordítás megkezdése előtt.
- A meglévő alias-alapú nyelvi mappákat észleli, és a futás során átmigrálhatók kanonikus nyelvi mappanevekre.
- A `run_review` hibát jelez hiányzó lefordított fájlok, hiányzó vagy elavult fordítási metaadatok, hibás Markdown frontmatter/kódkorlátok és érvénytelen lefordított notebook JSON esetén.
- A `run_review` alapértelmezés szerint hiányzó helyi Markdown és képhivatkozási célokat figyelmeztetésként jelenti.

## Belső hívási útvonal

Az API ugyanarra a magmegvalósításra delegál, amelyet a CLI használ:

Fordítás:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, notebookok és képek számára készített fókuszált projektfordítási mixinek.
8. Markdown, notebook, szöveg és kép fordítók a `co_op_translator.core` alatt.

Felülvizsgálat:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. A `co_op_translator.review.checks` alatt futó determinisztikus ellenőrzések

A következő osztályok hasznosak a karbantartók számára, de nem exportáltak a csomag szintű stabil API részeként.

| Osztály | Modul | Felelősség |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinálja a projekt-szintű fordítást, könyvtárkezelést, nyelvenkénti metaadat-normalizálást, és delegál a Markdown-, notebook- és képfordítók felé. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Végrehajtja az aszinkron fájlfeldolgozási munkát a Markdownok, notebookok, képek esetén, valamint az elavultság észlelését és a fordítási metaadatok frissítését. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Szervezi a Markdown fájlok beolvasását, tartalom fordítását, útvonal-átírást, metaadatokat, lemondásokat és az írásokat. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Szervezi a notebook fájlok beolvasását, a Markdown-cellák fordítását, útvonal-átírást, metaadatokat, lemondásokat és az írásokat. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Szervezi a forrásképek felderítését, képfordítást, kimeneti útvonalakat, metaadatokat és az írásokat. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Megtalálja a lefordított Markdown párokat, értékeli a fordítás minőségét, és olvassa a bizalmi metaadatokat alacsony bizalmi szintű javító munkafolyamatokhoz. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinálja a determinisztikus felülvizsgálati ellenőrzéseket a forrásfájlok, célnyelvek és konfigurált fordítási gyökerek között. |
| `ReviewTarget` | `co_op_translator.review.targets` | Leírja a forrásgyökeret és az adott gyökérhez felülvizsgált fordítási kimeneti könyvtárat. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Felismeri a régi alias nyelvi mappákat és előkészíti a kanonikus BCP 47 mappamigrációs terveket. |
| `Config` | `co_op_translator.config.base_config` | Betölti a `.env` fájlokat, és ellenőrzi, hogy a szükséges LLM és opcionális Vision szolgáltatók konfigurálva vannak-e. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatikusan felismeri az Azure OpenAI-t, OpenAI-t vagy Anthropic-ot, érvényesíti a szükséges környezeti változókat, és futtatja a szolgáltató-kapcsolatellenőrzéseket. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Felismeri az Azure AI Vision konfigurációt, és kapcsolatellenőrzéseket futtat a képfordításhoz. |