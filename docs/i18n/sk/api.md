# Python API

Stabilné verejné Python API je exportované z `co_op_translator.api`. Väčšina integrácií používa jeden z týchto pracovných postupov:

| Scenár | Použite, keď | Hlavné API |
| --- | --- | --- |
| Prekladať jednotlivé súbory alebo dokumenty | Vaša aplikácia načíta zdrojový obsah, zavolá Co-op Translator na preklad a rozhodne, kam uloží výsledok. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Pripraviť obsah na preklad hostiteľským agentom | Váš MCP hostiteľ alebo aplikačný model bude prekladať kúsky, zatiaľ čo Co-op Translator sa postará o delenie na kúsky a rekonštrukciu. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Preložiť celé repozitár | Chcete, aby sa Python API správalo ako CLI a riešilo zistenie súborov, výstupné cesty, metadata, čistenie a zápisy. | `run_translation` |

Väčšina modulov nižšej úrovne v `core`, `config`, `review` a `utils` sú implementačné detaily používané týmito vstupnými bodmi API.

Klienti MCP používajú rovnaké verejné API cez [MCP Server](mcp.md). Použite túto stránku pri priamom volaní Pythona a MCP príručku pri vystavovaní Co-op Translator agentovi alebo editoru. Ak sa rozhodujete medzi CLI, Python API a MCP, začnite s [Vyberte svoj pracovný postup](workflows.md).

## Postup pri prvom použití API

Začnite tu, ak voláte Co-op Translator z Python kódu:

1. Nakonfigurujte poskytovateľa LLM podľa [Konfigurácia](configuration.md), pokiaľ len nepripravujete časti Markdown alebo notebooku na preklad hostiteľským agentom.
2. Rozhodnite sa, či vaša aplikácia spravuje vstupno-výstup súborov.
3. Použite obsahové API, keď vaša aplikácia číta a zapisuje jednotlivé súbory.
4. Použite `run_translation`, keď má Co-op Translator spracovať repozitár rovnakým spôsobom ako CLI.
5. Použite `run_review` po preklade, ak potrebujete deterministické kontroly v automatizácii.

| Cieľ | API, s ktorým začať |
| --- | --- |
| Preložiť jeden Markdown reťazec alebo súbor | `translate_markdown_content` |
| Preložiť obsah jedného notebooku | `translate_notebook_content` |
| Preložiť jeden obrázok | `translate_image_content` |
| Nechajte hostiteľského agenta prekladať časti Markdownu alebo notebooku | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Prepísať preložené odkazy po zvolení výstupnej cesty | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Preložiť celý repozitár | `run_translation` |
| Skontrolovať preložený výstup | `run_review` |

## Scenár 1: Preklad jednotlivých súborov alebo dokumentov

Použite tento pracovný postup, ak už máte súbor, buffer editora, obsah notebooku, požiadavku MCP alebo vlastný vstup do pipeline. Váš kód spravuje prístup k súborom (I/O):

1. Načítajte zdrojový obsah.
2. Zavolajte API na preklad obsahu.
3. Voliteľne zavolajte API na prepísanie ciest, ak bude preložený obsah zapísaný do priečinka pre preklady projektu.
4. Uložte alebo vráťte výsledok z vašej aplikácie.

Obsahové prekladové API nespúšťajú zisťovanie projektu, nezapisujú metadata, nepridávajú upozornenia a automaticky neprepíšu odkazy.

### Markdown súbor

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

Ak preložený Markdown nebude umiestnený v rozložení projektu Co-op Translator, preskočte `rewrite_markdown_paths` a uložte preložený reťazec priamo.

### Súbor notebooku

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

`translate_notebook_content` prekladá Markdown bunky a zachováva ne-Markdown bunky. Prepísanie ciest sa uplatňuje iba na Markdown bunky.

### Súbor obrázka

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

`translate_image_content` načíta zdrojový obrázok a vráti renderovaný `PIL.Image.Image`. Nezapisuje metadáta preloženého obrázka.

## Scenár 2: Preklad celého repozitára

Použite tento pracovný postup, keď chcete, aby sa Python API správalo ako príkazové rozhranie `translate`. `run_translation` zistí podporované súbory, preloží vybrané typy obsahu, prepíše cesty, zapíše výstupné súbory, aktualizuje metadáta a vykoná údržbové úkony prekladov, ako je čistenie.

`run_translation` je preferovaný vstupný bod pre orchestráciu projektu. `translate_project` je exportované ako alias pre kompatibilitu so zhodným správaním.

Preložte Markdown súbory v aktuálnom repozitári do kórejčiny a japončiny:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Preložte len notebooky z konkrétneho koreňového adresára projektu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Náhľad objemu prekladu bez zapisovania súborov:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Zaznamenávajte štruktúrované udalosti priebehu pre integráciu:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Uložte payload do vašej tabuľky job-event alebo ho streamujte do vášho UI.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Udalosti používajú verziovanú schému `co-op.translation.event.v1`. Integrácie by sa mali
spoliehať na stabilné polia, ako sú `type` a `stage_key`, a nie na konzolový text určený pre ľudí
alebo na `stage_label`.

Preložte viacero koreňov obsahu v jednom volaní:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapisujte preklady do explicitných výstupných skupín:

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

Použite zástupný symbol pre každý jazyk, ak má každý jazyk obsahovať vnorený podadresár:

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

Ak nie je nastavené žiadne z `markdown`, `notebook` alebo `images`, API preloží všetky podporované typy: Markdown, notebooky a obrázky.

### Zachovať akceptované ľudské úpravy pomocou poskytovateľa stavu prekladu

Štandardne Co-op Translator zachováva svoje existujúce správanie na úrovni súboru:
keď je zdrojový Markdown zastaraný, celý preložený súbor sa znovu vygeneruje. Hostované
integrácie môžu voliteľne poskytnúť `TranslationStateProvider` na zachovanie ľudských
úprav v zdrojových blokoch, ktoré sa nezmenili.

Poskytovateľ dodáva posledný akceptovaný pár zdroj/cieľ a zaznamenáva každý nový
kandidát. Akceptácia zostáva zodpovednosťou integrácie — napríklad,
po zlúčení pull requestu s prekladom:

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

Pre Markdown súbory s platným akceptovaným základom, Co-op Translator zarovná
vrcholové Markdown bloky. Nezmenené zdrojové bloky znovu použijú aktuálne preložené
bloky, vrátane úprav vykonaných ľuďmi; zmenené alebo pridané zdrojové bloky sú odoslané
na preklad; vymazané zdrojové bloky sa odstránia. Ak je zarovnanie nejednoznačné,
cieľová štruktúra sa zmenila, preklad bloku je neplatný alebo nie je k dispozícii žiadny základ,
Co-op Translator bezpečne prejde späť na existujúcu cestu úplného prekladu súboru.
translation path.

Toto API ukladá stav prekladu dokumentu, nie medzi-dokumentovú pamäť prekladu fráz alebo
segmentov. Momentálne sa to vzťahuje na preklad Markdown projektov.
Správanie notebookov a obrázkov sa nemení. Odovzdanie `update=True`
stále vyžiada úplnú regeneráciu.

Ak jeden alebo viac súborov sa nedá preložiť, `run_translation` vyhodí
`RuntimeError` po dokončení pracovného postupu projektu namiesto nahlásenia
úspešného behu s chýbajúcim výstupom. Integrácie by to mali považovať za neúspešnú
úlohu a zachovať predchádzajúci akceptovaný stav prekladu.

## Skontrolujte preložený výstup

`run_review` vykonáva deterministické kontroly prekladu bez poverení LLM alebo Vision.

!!! note "Beta"
    `run_review` je beta deterministické revízne API. Nevolá poskytovateľov modelov ani nezapisuje súbory, ale kontroly a schémy problémov sa môžu vyvíjať.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Po preklade iba README použite rovnaký rozsah pre revíziu:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` kontroluje iba `README.md` pod každým nakonfigurovaným zdrojovým koreňom,
vrátane vlastných `groups` a výstupných adresárov. Ostatné dokumenty a vnorené
README súbory sú vylúčené. Chýbajúce zdrojové README vyvolá `ValueError`; neúspešné
kontroly prekladu vyvolajú `RuntimeError`.

Skontrolujte len súbory zmenené oproti základnému ref a vytlačte výstup v štýle GitHubu:

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

## Príklady API pre kopírovanie a vkladanie

Preložte obsah Markdown bez zápisu súborov:

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

Preložte a prepíšte Markdown odkazy:

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

Preložte repozitár z Pythonu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Preložte viacero koreňov:

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

Zachovajte pojmy zo slovníka:

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

## Verejné vstupné body

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

## API na preklad obsahu

API na preklad obsahu sú určené pre integrácie, ktoré už majú obsah v pamäti, ako napríklad rozšírenie editora, nástroj MCP, procesor notebookov alebo vlastný pipeline.

| Funkcia | Vstup | Výstup | Práca so súbormi | Poznámky |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nie | Asynchrónne. Prekladá iba obsah Markdownu. Neprepisuje odkazy, nezapisuje metadáta ani nepripája zrieknutia sa zodpovednosti. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Nie | Asynchrónne. Prekladá Markdown bunky a zachováva ne-Markdown bunky. Neprepisuje odkazy, nezapisuje metadáta ani nepripája zrieknutia sa zodpovednosti. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchrónne. Extrahuje a preloží text z obrázka, potom vráti renderovaný obrázok. Neukladá metadáta preloženého obrázka. |

`translate_markdown_content` a `translate_notebook_content` akceptujú voliteľný `source_path` cez svoje možnosti. Cesta sa odovzdáva ako kontext pre prekladač; volajúci zostávajú zodpovední za akékoľvek projektovo-špecifické prepísanie ciest po preklade.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Rovnaké možnosti je možné odovzdať ako slovníky:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API pre preklady asistované agentom

API s asistenciou agenta nevolá nakonfigurovaného poskytovateľa LLM z Co-op Translatora. Pripravujú časti Markdownu alebo notebooku pre hostiteľského agenta na preklad a potom rekonštruujú výsledný obsah z preložených častí.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Vráti samostatnú úlohu vo formáte Markdown s časťami, promptami a stavom rekonštrukcie. |
| `finish_markdown_agent_translation` | Rekonštruovať Markdown z úlohy a častí preložených hostiteľom a agentom. |
| `start_notebook_agent_translation` | Vráti úlohu pre notebook s časťami Markdown buniek určenými na preklad hostiteľom a agentom. |
| `finish_notebook_agent_translation` | Rekonštruovať JSON notebooku pri zachovaní buniek s kódom, výstupov a metadát. |

Tento pracovný tok je určený hlavne pre MCP hostiteľov. Ak potrebujete preklad repozitára v produkcii, kde Co-op Translator spravuje volania poskytovateľa, použite `translate_markdown_content`, `translate_notebook_content` alebo `run_translation`.

## API pre prepísanie ciest

API na prepísanie ciest nevykonávajú žiadny preklad. Aktualizujú odkazy a frontmatter cesty po tom, čo volajúci poznajú cestu zdroja, preloženú cieľovú cestu a štruktúru projektu.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Prepíše Markdown odkazy a podporované polia frontmatteru s cestami pre preložený cieľ. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Uplatní prepísanie Markdown ciest na každú Markdown bunku a nechá ne-Markdown bunky nezmenené. |

Argument `policy` môže byť slovník s týmito poliami:

| Pole | Požadované | Účel |
| --- | --- | --- |
| `language_code` | Áno | Kód cieľového jazyka, napríklad `"ko"` alebo `"pt-BR"`. |
| `root_dir` | Nie | Koreň zdrojového projektu. Predvolené je `"."`. |
| `translations_dir` | Nie | Adresár výstupu pre preklady textu. Predvolené `translations` pod `root_dir`. |
| `translated_images_dir` | Nie | Adresár výstupu pre preložené obrázky. Predvolené `translated_images` pod `root_dir`. |
| `translation_types` | Nie | Povolené typy prekladu. Predvolené sú Markdown, notebooky a obrázky. |
| `lang_subdir` | Nie | Voliteľný podadresár pod každou zložkou jazyka. |

## Parametre prekladu projektu

| Parameter | Typ | Predvolené | Účel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Požadované | Cieľové kódy jazykov oddelené medzerami, napríklad `"ko ja fr"`, alebo `"all"`. Alias kódy sú normalizované na kanonické BCP 47 hodnoty. |
| `root_dir` | `str` | `"."` | Koreň projektu pre jeden cieľ prekladu. Ignorované keď sú poskytnuté `root_dirs` alebo `groups`. |
| `update` | `bool` | `False` | Vymazať a znovu vytvoriť existujúce preklady pre vybrané jazyky. |
| `images` | `bool` | `False` | Zahrnúť preklad obrázkov. Vyžaduje konfiguráciu Azure AI Vision. |
| `markdown` | `bool` | `False` | Zahrnúť preklad Markdownu. |
| `notebook` | `bool` | `False` | Zahrnúť preklad Jupyter notebookov. |
| `debug` | `bool` | `False` | Povoliť debug logovanie. |
| `save_logs` | `bool` | `False` | Uložiť DEBUG-level log súbory do koreňového adresára `logs/`. |
| `yes` | `bool` | `True` | Automaticky potvrdiť výzvy pre programatické a CI použitie. |
| `add_disclaimer` | `bool` | `False` | Pridať upozornenia o strojovom preklade do preložených súborov Markdown a notebookov. |
| `translations_dir` | `str \| None` | `None` | Vlastný adresár výstupu pre textové preklady. Relatívne cesty sa riešia vzhľadom na každý koreňový adresár. |
| `image_dir` | `str \| None` | `None` | Vlastný adresár výstupu pre preložené obrázky. Relatívne cesty sa riešia vzhľadom na každý koreňový adresár. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Viaceré koreňové adresáre, ktoré zdieľajú rovnaké výstupné nastavenia. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicitné páry `(root_dir, translations_dir)`. Má prednosť pred `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozitára používané pri vykresľovaní pokynov tabuľky jazykov v README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termíny slovníka, ktoré sa majú počas prekladu zachovať. Duplicitné a prázdne termíny sa normalizujú. |
| `dry_run` | `bool` | `False` | Odhadnúť objem prekladu a náhľad správania pri migrácii bez zápisu súborov. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Voliteľný adaptér perzistencie pre akceptovaný základ a kandidáta pre inkrementálne aktualizácie Markdownu. Ak sa vynechá, zachová sa existujúce správanie s celými súbormi. |

## Parametre revízie

`run_review` zámerne kopíruje signatúru `run_translation`, kde je to možné, aby sa automatizácia mohla prepínať medzi pracovnými postupmi prekladu a revízie s minimálnym rozvetvením.

| Parameter | Typ | Predvolené | Účel |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Cieľové zložky jazykov na revíziu. Akceptované sú reťazce oddelené medzerou aj iterovateľné kolekcie. `"all"` skontroluje všetky zistené prekladové jazyky. |
| `root_dir` | `str` | `"."` | Koreň projektu pre jediný revízny cieľ. Ignorované, keď sú poskytnuté `root_dirs` alebo `groups`. |
| `markdown` | `bool` | `False` | Zahrnúť zdrojové súbory Markdown a MDX. |
| `notebook` | `bool` | `False` | Zahrnúť zdrojové súbory Jupyter notebookov. |
| `images` | `bool` | `False` | Rezervované pre paritu s možnosťami prekladu. Odkazy na obrázky sa kontrolujú z Markdownu. |
| `translations_dir` | `str \| None` | `None` | Vlastný adresár výstupu pre textové preklady. Relatívne cesty sa riešia vzhľadom na každý koreňový adresár. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Viaceré koreňové adresáre, ktoré zdieľajú rovnaké výstupné nastavenia. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicitné páry `(root_dir, translations_dir)`. Má prednosť pred `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref používaný na obmedzenie revízie na zmenené zdrojové súbory. |
| `readme_only` | `bool` | `False` | Revízia len súboru `README.md` pod každým zdrojovým koreňom. Ak chýba zdrojový README, vyvolá sa `ValueError`. |
| `output_format` | `str` | `"text"` | Formát výstupu revízie. Podporované hodnoty sú `"text"` a `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Považovať varovania za zlyhania rovnako ako chyby. |
| `debug` | `bool` | `False` | Povoliť debug logovanie. |
| `save_logs` | `bool` | `False` | Uložiť log súbory úrovne DEBUG do koreňového adresára `logs/`. |

Ak nie je nastavené žiadne z `markdown`, `notebook` alebo `images`, API skontroluje Markdown, notebooky a odkazy na obrázky, kde je to relevantné. Revízia nevolá poskytovateľa LLM a nevyžaduje API kľúče.

## Požiadavky na konfiguráciu

Preklady závislé od poskytovateľa vyžadujú pred prekladom konfiguráciu poskytovateľa:

- Preklad Markdownu a notebookov vyžaduje poskytovateľa LLM. Nakonfigurujte Azure OpenAI, OpenAI alebo Anthropic.
- Preklad obrázkov vyžaduje Azure AI Vision okrem poskytovateľa LLM.
- `run_translation` spustí ľahké kontroly konektivity pred začiatkom prekladu projektu.
- Agentmi asistované API `start_*_agent_translation` a `finish_*_agent_translation` nevolajú poskytovateľov LLM Co-op Translator. Hostiteľská aplikácia alebo MCP agent prekladá pripravené časti.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` a `run_review` sú deterministické a nevyžadujú poverenia poskytovateľa.

Požadované premenné Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Požadované premenné OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Požadované premenné Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` a `ANTHROPIC_MAX_TOKENS` sú voliteľné. Microsoft Agent Framework je predvoleným klientom modelu pre všetkých poskytovateľov od verzie Co-op Translator 0.22.0. Semantic Kernel je stále možné dočasne vybrať pomocou `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ale takéto použitie vygeneruje varovanie o odstránení; pozrite [konfiguráciu](configuration.md#model-client-backend) pre plán postupného odstránenia.

Požadované premenné Azure AI Vision pre preklad obrázkov:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` je deterministické a nevyžaduje konfiguráciu LLM ani Azure AI Vision.

## Poznámky k správaniu

- API pre preklad obsahu udržujú preklad oddelene od prepísania ciest projektu. Zavolajte explicitne `rewrite_markdown_paths` alebo `rewrite_notebook_paths`, keď sa musí upraviť projektovo-relatívne odkazy v preloženom obsahu pre cieľové umiestnenie.
- API pre orchestráciu projektu pridávajú správanie projektu okolo prekladu obsahu, vrátane zisťovania súborov, zápisov, prepísania ciest, metadát, čistenia a voliteľných upozornení.
- `run_translation` vypisuje priebeh a súhrny odhadov cez toho istého Rich-podporovaného reportéra, ktorý používa CLI. Neinteraktívny výstup použije obyčajný text.
- `dry_run=True` vypočíta odhady pomocou virtuálnych aktualizácií README, ale nezapíše README ani prekladové súbory.
- `groups` sa spracúvajú postupne. Pred začiatkom práce sa vypíše jeden súhrnný odhad.
- Keď je zvolený preklad obrázkov, chýbajúca konfigurácia Vision vyvolá chybu pred začiatkom prekladu.
- Existujúce aliasy založené na jazykových priečinkoch sú detegované a môžu byť počas behu migrované na kanonické názvy jazykových priečinkov.
- `run_review` zlyhá pri chýbajúcich preložených súboroch, chýbajúcich alebo zastaraných metadátach prekladu, nesprávne formátovanom Markdown frontmatter alebo ohraničeniach kódu a neplatnom JSON-e preloženého notebooku.
- `run_review` štandardne hlási chýbajúce lokálne ciele odkazov v Markdown a na obrázky ako varovania.

## Interná volacia cesta

API deleguje na tú istú jadrovú implementáciu, ktorú používa CLI:

Preklad:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation. |
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing. |
3. `co_op_translator.api.translation.run_translation` for full project orchestration. |
4. `co_op_translator.config.Config`, `LLMConfig` a `VisionConfig`. |
5. `co_op_translator.core.project.ProjectTranslator`. |
6. `co_op_translator.core.project.TranslationManager`. |
7. Mixiny zamerané na projektový preklad pre Markdown, notebooky a obrázky. |
8. Prekladače Markdownu, notebookov, textu a obrázkov v rámci `co_op_translator.core`. |

Revízia:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministické kontroly v rámci `co_op_translator.review.checks`

Nasledujúce triedy sú užitočné pre udržiavateľov, ale nie sú exportované ako stabilné API na úrovni balíka.

| Trieda | Modul | Zodpovednosť |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinuje projektový preklad, správu adresárov, normalizáciu metadát pre každý jazyk a delegovanie na prekladače Markdownu, notebookov a obrázkov. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Vykonáva asynchrónnu prácu s spracovaním súborov pre Markdown, notebooky, obrázky, detekciu zastaraných položiek a aktualizácie metadát prekladu. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestrujuje načítavanie Markdown súborov, preklad obsahu, prepísanie ciest, metadát, upozornení a zápisu. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestrujuje načítavanie notebook súborov, preklad Markdown buniek, prepísanie ciest, metadát, upozornení a zápisov. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestrujuje objavovanie zdrojových obrázkov, preklad obrázkov, výstupné cesty, metadáta a zápisy. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Nájde páry preloženého Markdownu, vyhodnotí kvalitu prekladu a číta metadáta dôveryhodnosti pre pracovné postupy opráv pri nízkej dôvere. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinuje deterministické revízne kontroly naprieč zdrojovými súbormi, cieľovými jazykmi a nakonfigurovanými koreňmi prekladov. |
| `ReviewTarget` | `co_op_translator.review.targets` | Popisuje zdrojový koreň a výstupný adresár prekladov, ktorý sa pre tento koreň kontroluje. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Deteguje staršie aliasy jazykových priečinkov a pripravuje plány migrácie na kanonické priečinky podľa BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Načítava súbory `.env` a kontroluje, či sú nakonfigurovaní požadovaní poskytovatelia LLM a voliteľní poskytovatelia Vision. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automaticky deteguje Azure OpenAI, OpenAI alebo Anthropic, validuje požadované premenné prostredia a spúšťa kontroly konektivity poskytovateľov. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Deteguje konfiguráciu Azure AI Vision a spúšťa kontroly konektivity pre preklad obrázkov. |