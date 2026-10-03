# Python API

Stabilní veřejné Python API je exportováno z `co_op_translator.api`. Většina integrací používá jeden z těchto pracovních postupů:

| Scénář | Použijte když | Hlavní API |
| --- | --- | --- |
| Přeložit jednotlivé soubory nebo dokumenty | Vaše aplikace načte zdrojový obsah, zavolá Co-op Translator pro překlad a rozhodne, kam uložit výsledek. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Připravit obsah pro překlad host-agentem | Váš MCP hostitel nebo aplikační model přeloží bloky, zatímco Co-op Translator se postará o dělení na bloky a rekonstukci. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Přeložit celý repozitář | Chcete, aby se Python API chovalo jako CLI a řešilo objevování souborů, výstupní cesty, metadata, úklid a zápisy. | `run_translation` |

Většina nízkoúrovňových modulů v `core`, `config`, `review` a `utils` jsou implementační detaily používané těmito vstupními body API.

Klienti MCP používají stejné veřejné API přes [MCP Server](mcp.md). Použijte tuto stránku při volání přímo z Pythonu a příručku MCP při zpřístupňování Co-op Translatoru agentovi nebo editoru. Pokud se rozhodujete mezi CLI, Python API a MCP, začněte s [Vyberte svůj pracovní postup](workflows.md).

## První použití API

Začněte zde, pokud voláte Co-op Translator z Python kódu:

1. Nakonfigurujte poskytovatele LLM podle popisu v [Konfigurace](configuration.md), pokud pouze nepřipravujete bloky Markdownu nebo notebooku pro překlad host-agentem.
2. Rozhodněte se, zda vaše aplikace spravuje vstupně-výstupní operace se soubory.
3. Použijte obsahová API, když vaše aplikace čte a zapisuje jednotlivé soubory.
4. Použijte `run_translation`, když má Co-op Translator zpracovat repozitář jako CLI.
5. Použijte `run_review` po překladu, pokud v automatizaci potřebujete deterministické kontroly.

| Cíl | API pro začátek |
| --- | --- |
| Přeložit jeden Markdown řetězec nebo soubor | `translate_markdown_content` |
| Přeložit jeden obsah notebooku | `translate_notebook_content` |
| Přeložit jeden obrázek | `translate_image_content` |
| Nechat hostitelského agenta přeložit bloky Markdownu nebo notebooku | `start_markdown_agent_translation` nebo `start_notebook_agent_translation` |
| Přepsat přeložené odkazy po výběru výstupní cesty | `rewrite_markdown_paths` nebo `rewrite_notebook_paths` |
| Přeložit celý repozitář | `run_translation` |
| Zkontrolovat přeložený výstup | `run_review` |

## Scénář 1: Překlad jednotlivých souborů nebo dokumentů

Použijte tento pracovní postup, když již máte soubor, buffer v editoru, obsah notebooku, MCP požadavek nebo vlastní vstup do pipeline. Vaše kód spravuje vstupně-výstupní operace se soubory:

1. Načtěte zdrojový obsah.
2. Zavolejte API pro překlad obsahu.
3. Volitelně zavolejte API pro přepisování cest, pokud bude přeložený obsah uložen do složky překladů v projektu.
4. Uložte nebo vraťte výsledek z vaší aplikace.

API pro překlad obsahu nespouštějí objevování projektu, nezapisují metadata, nepřipojují výhrady a automaticky nepřepisují odkazy.

### Markdownový soubor

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

Pokud přeložený Markdown nebude součástí rozložení projektu Co-op Translator, vynechte `rewrite_markdown_paths` a uložte přeložený řetězec přímo.

### Notebookový soubor

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

Funkce `translate_notebook_content` překládá Markdownové buňky a zachovává ne-Markdownové buňky. Přepisování cest se aplikuje pouze na Markdownové buňky.

### Obrázkový soubor

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

Funkce `translate_image_content` načte zdrojový obrázek a vrátí renderovaný `PIL.Image.Image`. Nezapíše metadata přeloženého obrázku.

## Scénář 2: Překlad celého repozitáře

Použijte tento pracovní postup, když chcete, aby se Python API chovalo jako `translate` CLI. `run_translation` objeví podporované soubory, přeloží vybrané typy obsahu, přepíše cesty, zapíše výstupní soubory, aktualizuje metadata a provede údržbové úlohy překladu, jako je úklid.

`run_translation` je preferovaný vstupní bod pro orchestraci projektu. `translate_project` je exportováno jako alias pro kompatibilitu se stejným chováním.

Přeložte Markdown soubory v aktuálním repozitáři do korejštiny a japonštiny:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Přeložte pouze notebooky z konkrétního kořenového adresáře projektu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Náhled objemu překladu bez zápisu souborů:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Zaznamenávejte strukturované události průběhu pro integraci:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Uložte payload do tabulky job-event nebo jej streamujte do uživatelského rozhraní.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Události používají verzované schéma `co-op.translation.event.v1`. Integrace by měly
spoléhat se na stabilní pole jako `type` a `stage_key`, nikoli na uživatelsky orientovaný
text v konzoli nebo `stage_label`.

Přeložte více kořenů obsahu v jednom volání:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapište překlady do explicitních výstupních skupin:

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

Použijte zástupný znak pro každý jazyk, pokud má každý jazyk obsahovat vnořený podadresář:

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

Pokud není nastaveno žádné z `markdown`, `notebook` nebo `images`, API přeloží všechny podporované typy: Markdown, notebooky a obrázky.

### Zachování přijatých lidských úprav pomocí poskytovatele stavu překladu

Ve výchozím nastavení Co-op Translator zachovává své stávající chování na úrovni souborů: když je
zdroj Markdownu zastaralý, celý přeložený soubor je znovu vygenerován. Hostované
integrace mohou volitelně předat `TranslationStateProvider` pro zachování lidských
úprav v blocích zdroje, které se nezměnily.

Poskytovatel dodává poslední přijatý pár zdroj/cíl a zaznamenává každý nový
kandidát. Schválení zůstává odpovědností integrace—například,
po sloučení pull requestu s překladem:

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

Pro Markdown soubory s platnou přijatou základnou Co-op Translator zarovnává
vrcholové bloky Markdownu. Nezměněné zdrojové bloky znovu použijí aktuální přeložené
bloky, včetně úprav provedených lidmi; změněné nebo přidané zdrojové bloky jsou odeslány
k překladu; smazané zdrojové bloky jsou odstraněny. Pokud je zarovnání nejednoznačné,
cílová struktura se změnila, překlad bloku je neplatný nebo není k dispozici žádná základna (baseline),
Co-op Translator bezpečně upustí k existující cestě překladu celého souboru.
translation path.

Toto API ukládá stav překladu dokumentu, nikoli mezi-dokumentovou slovní nebo
segmentovou paměť překladů. V současnosti se vztahuje na překlad Markdown projektů.
Chování notebooků a obrázků zůstává nezměněno. Předání `update=True`
stále požaduje plnou regeneraci.

Pokud nelze přeložit jeden nebo více souborů, `run_translation` vyvolá
`RuntimeError` po dokončení pracovního postupu projektu namísto nahlášení
úspěšného běhu s chybějícím výstupem. Integrace by to měly považovat za neúspěšnou
úlohu a zachovat předchozí přijatý stav překladu.

## Kontrola přeloženého výstupu

`run_review` provádí deterministické kontroly překladu bez přihlašovacích údajů LLM nebo Vision.

!!! note "Beta"
    `run_review` je beta deterministické revizní API. Nevolá poskytovatele modelů ani nezapisuje soubory, ale kontroly a schémata problémů se mohou vyvíjet.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Po překladu pouze README použijte stejný rozsah pro kontrolu:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` kontroluje pouze `README.md` v každém nakonfigurovaném zdrojovém kořeni,
včetně vlastních `groups` a výstupních adresářů. Ostatní dokumenty a vnořené
README jsou vyloučeny. Chybějící zdrojové README vyvolá `ValueError`; neúspěšné
kontroly překladu vyvolají `RuntimeError`.

Zkontrolujte pouze soubory změněné vůči základnímu ref a vytiskněte výstup ve stylu GitHubu:

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

## Příklady API pro kopírování a vložení

Přeložte obsah Markdownu bez zápisu souborů:

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

Přeložte a přepište odkazy v Markdownu:

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

Přeložte repozitář z Pythonu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Přeložte více kořenů:

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

Zachovejte termíny v glosáři:

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

## Veřejné vstupní body

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

## API pro překlad obsahu

API pro překlad obsahu jsou určena pro integrace, které již mají obsah v paměti, jako je rozšíření editoru, nástroj MCP, procesor notebooků nebo vlastní pipeline.

| Funkce | Vstup | Výstup | Práce se soubory | Poznámky |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ne | Asynchronní. Překládá pouze obsah Markdownu. Nepřepisuje odkazy, nezapisuje metadata ani nepřipojuje výhrady. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Ne | Asynchronní. Překládá Markdownové buňky a zachovává ne-Markdownové buňky. Nepřepisuje odkazy, nezapisuje metadata ani nepřipojuje výhrady. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Načítá pouze zdrojový obrázek | Synchronní. Extrahuje a přeloží text z obrázku, poté vrátí renderovaný obrázek. Neukládá metadata přeloženého obrázku. |

`translate_markdown_content` a `translate_notebook_content` přijímají volitelný parametr `source_path` prostřednictvím svých možností. Cesta je předána překladači jako kontext; volající zůstávají zodpovědní za jakékoli přepisování cest specifické pro projekt po překladu.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Stejné možnosti lze předat jako slovníky:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API pro překlad asistovaný agentem

API asistovaná agentem nevolají z Co-op Translator nakonfigurovaného poskytovatele LLM. Připraví bloky Markdownu nebo notebooku pro hostitelského agenta k překladu a poté rekonstruují finální obsah z přeložených bloků.

| Funkce | Účel |
| --- | --- |
| `start_markdown_agent_translation` | Vrátí samostatnou Markdown úlohu s bloky, výzvami a stavem rekonstrukce. |
| `finish_markdown_agent_translation` | Rekonstruuje Markdown z úlohy a host-agentem přeložených bloků. |
| `start_notebook_agent_translation` | Vrátí úlohu notebooku s bloky Markdown buněk pro překlad host-agentem. |
| `finish_notebook_agent_translation` | Rekonstruuje notebook JSON při zachování kódových buněk, výstupů a metadat. |

Tento pracovní postup je určen především pro MCP hostitele. Pokud potřebujete produkční překlad repozitáře s Co-op Translator, který řídí volání poskytovatelů, použijte `translate_markdown_content`, `translate_notebook_content` nebo `run_translation`.

## API pro přepisování cest

API pro přepisování cest neprovádějí žádný překlad. Aktualizují odkazy a cesty ve frontmatteru poté, co volající zná zdrojovou cestu, přeloženou cílovou cestu a rozložení projektu.

| Funkce | Rozsah | Poznámky |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Přepisuje Markdown odkazy a podporovaná pole frontmatter s cestami pro přeložený cíl. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Aplikuje přepisování cest Markdownu na každou Markdown buňku a nechává ne-Markdownové buňky nezměněné. |

Argument `policy` může být slovník s těmito poli:

| Pole | Povinné | Účel |
| --- | --- | --- |
| `language_code` | Ano | Kód cílového jazyka, například `"ko"` nebo `"pt-BR"`. |
| `root_dir` | Ne | Kořen zdrojového projektu. Výchozí hodnotou je `"."`. |
| `translations_dir` | Ne | Výstupní adresář pro textové překlady. Výchozí je `translations` pod `root_dir`. |
| `translated_images_dir` | Ne | Výstupní adresář pro přeložené obrázky. Výchozí je `translated_images` pod `root_dir`. |
| `translation_types` | Ne | Povolené typy překladu. Výchozí jsou Markdown, notebooky a obrázky. |
| `lang_subdir` | Ne | Volitelný podadresář pod každou složkou jazyka. |

## Parametry překladu projektu

| Parametr | Typ | Výchozí | Účel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Povinné | Mezerou oddělené kódy cílových jazyků, například `"ko ja fr"`, nebo `"all"`. Alias kódy jsou normalizovány na kanonické hodnoty BCP 47. |
| `root_dir` | `str` | `"."` | Kořen projektu pro jeden cílový překlad. Ignorováno, když jsou poskytnuty `root_dirs` nebo `groups`. |
| `update` | `bool` | `False` | Smaže a znovu vytvoří existující překlady pro vybrané jazyky. |
| `images` | `bool` | `False` | Zahrnout překlad obrázků. Vyžaduje konfiguraci Azure AI Vision. |
| `markdown` | `bool` | `False` | Zahrnout překlad Markdownu. |
| `notebook` | `bool` | `False` | Zahrnout překlad Jupyter notebooku. |
| `debug` | `bool` | `False` | Povolit debug logování. |
| `save_logs` | `bool` | `False` | Uložit logy na úrovni DEBUG do kořenového adresáře `logs/`. |
| `yes` | `bool` | `True` | Automaticky potvrzovat výzvy pro programové a CI použití. |
| `add_disclaimer` | `bool` | `False` | Přidat upozornění o strojovém překladu do přeložených Markdown souborů a notebooků. |
| `translations_dir` | `str \| None` | `None` | Vlastní adresář pro výstup překladu textu. Relativní cesty se vyhodnocují vůči každému kořeni. |
| `image_dir` | `str \| None` | `None` | Vlastní adresář pro výstup přeložených obrázků. Relativní cesty se vyhodnocují vůči každému kořeni. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Více kořenů, které sdílejí stejná výstupní nastavení. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicitní páry `(root_dir, translations_dir)`. Má přednost před `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozitáře použité při vykreslování pokynů tabulky jazyků v README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termíny slovníku, které se mají při překladu zachovat. Duplicitní a prázdné termíny jsou normalizovány. |
| `dry_run` | `bool` | `False` | Odhadnout objem překladu a zobrazit náhled chování migrace bez zápisu souborů. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Nepovinný adaptér pro perzistenci accepted-baseline a kandidátů pro inkrementální aktualizace Markdownu. Jeho vynechání zachová současné chování s celými soubory. |

## Parametry kontroly

`run_review` záměrně co nejvíce kopíruje signaturu `run_translation`, aby automatizace mohla přepínat mezi pracovními postupy překladu a kontroly s minimem rozvětvení.

| Parametr | Typ | Výchozí | Účel |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Cílové jazykové složky ke kontrole. Přijímají se řetězce oddělené mezerou i iterovatelné objekty. `"all"` zkontroluje všechny nalezené překlady. |
| `root_dir` | `str` | `"."` | Kořen projektu pro jediný cíl kontroly. Ignorováno, pokud jsou zadány `root_dirs` nebo `groups`. |
| `markdown` | `bool` | `False` | Zahrnout zdrojové soubory Markdown a MDX. |
| `notebook` | `bool` | `False` | Zahrnout zdrojové soubory Jupyter notebooků. |
| `images` | `bool` | `False` | Rezervováno pro shodu s možnostmi překladu. Odkazy na obrázky se kontrolují z Markdown souborů. |
| `translations_dir` | `str \| None` | `None` | Vlastní adresář pro výstup překladu textu. Relativní cesty se vyhodnocují vůči každému kořeni. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Více kořenů, které sdílejí stejná výstupní nastavení. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicitní páry `(root_dir, translations_dir)`. Má přednost před `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref použitý k omezení kontroly na změněné zdrojové soubory. |
| `readme_only` | `bool` | `False` | Kontrolovat pouze `README.md` pod každým zdrojovým kořenem. Chybějící zdrojový README vyvolá `ValueError`. |
| `output_format` | `str` | `"text"` | Formát výstupu kontroly. Podporované hodnoty jsou `"text"` a `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Považovat varování za chyby kromě chyb. |
| `debug` | `bool` | `False` | Povolit ladicí protokolování. |
| `save_logs` | `bool` | `False` | Uložit logy úrovně DEBUG do kořenového adresáře `logs/`. |

Pokud není nastaveno žádné z `markdown`, `notebook` nebo `images`, API zkontroluje Markdown, notebooky a odkazy na obrázky tam, kde je to relevantní. Kontrola nevolá poskytovatele LLM a nevyžaduje API klíče.

## Požadavky na konfiguraci

Překladová API, která stojí na poskytovateli, vyžadují před překladem konfiguraci poskytovatele:

- Překlad Markdownu a notebooků vyžaduje poskytovatele LLM. Nakonfigurujte Azure OpenAI, OpenAI nebo Anthropic.
- Překlad obrázků vyžaduje kromě poskytovatele LLM také Azure AI Vision.
- `run_translation` provádí lehké kontroly konektivity před zahájením překladu projektu.
- Agenty asistované API `start_*_agent_translation` a `finish_*_agent_translation` nevolají poskytovatele LLM Co-op Translator. Hostitelská aplikace nebo MCP agent překládá připravené bloky.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` a `run_review` jsou deterministické a nevyžadují přihlašovací údaje poskytovatele.

Požadované proměnné pro Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Požadované proměnné pro OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Požadované proměnné pro Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` a `ANTHROPIC_MAX_TOKENS` jsou volitelné. Microsoft Agent Framework je výchozí klient modelu pro všechny poskytovatele počínaje Co-op Translator 0.22.0. Semantic Kernel stále lze dočasně vybrat pomocí `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ale při tom se vygeneruje varování o zastarání; viz [configuration](configuration.md#model-client-backend) pro plán postupného odstranění.

Požadované proměnné Azure AI Vision pro překlad obrázků:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` je deterministický a nevyžaduje konfiguraci LLM ani Azure AI Vision.

## Poznámky k chování

- API pro překlad obsahu oddělují překlad od přepisování cest projektu. Zavolejte explicitně `rewrite_markdown_paths` nebo `rewrite_notebook_paths`, když je třeba upravit projektově relativní odkazy v přeloženém obsahu pro cílové umístění.
- API pro orchestraci projektu přidávají chování projektu kolem překladu obsahu, včetně vyhledávání souborů, zápisů, přepisování cest, metadat, úklidu a volitelných upozornění.
- `run_translation` vypisuje souhrny průběhu a odhadů přes stejný reportér založený na Rich, který používá CLI. Neinteraktivní výstup přechází na prostý text.
- `dry_run=True` počítá odhady pomocí virtuálních aktualizací README, ale neprovádí zápis README ani překladových souborů.
- `groups` se zpracovávají sekvenčně. Před zahájením práce se vytiskne jeden celkový odhad.
- Pokud je vybrán překlad obrázků, chybějící konfigurace Vision vyvolá chybu ještě před zahájením překladu.
- Stávající aliasové jazykové složky jsou detekovány a mohou být během běhu migrovány na kanonické názvy jazykových složek.
- `run_review` selže při chybějících přeložených souborech, chybějících nebo zastaralých metadatech překladu, poškozeném Markdown frontmatteru nebo code fence a neplatném JSONu přeloženého notebooku.
- `run_review` hlásí chybějící lokální cíle Markdownu a odkazů na obrázky jako varování ve výchozím nastavení.

## Interní volací cesta

API deleguje na stejnou základní implementaci, kterou používá CLI:

Překlad:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` pro překlad v paměti.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` pro explicitní dodatečné zpracování cest.
3. `co_op_translator.api.translation.run_translation` pro kompletní orchestraci projektu.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Zaměřené mixiny překladu projektů pro Markdown, notebooky a obrázky.
8. Překladače Markdownu, notebooků, textu a obrázků v `co_op_translator.core`.

Kontrola:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

Následující třídy jsou užitečné pro správce, ale nejsou exportovány jako stabilní API na úrovni balíčku.

| Třída | Modul | Odpovědnost |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinuje překlad na úrovni projektu, správu adresářů, normalizaci metadat pro jednotlivé jazyky a delegování na překladače Markdownu, notebooků a obrázků. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Provádí asynchronní zpracování souborů pro Markdown, notebooky, obrázky, detekci zastaralosti a aktualizace metadat překladu. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestruje čtení souborů Markdown, překlad obsahu, přepisování cest, metadata, upozornění a zápisy. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestruje čtení notebooků, překlad buněk Markdown, přepisování cest, metadata, upozornění a zápisy. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestruje vyhledávání zdrojových obrázků, překlad obrázků, výstupní cesty, metadata a zápisy. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Nalezne páry přeložených Markdownů, vyhodnotí kvalitu překladu a načte metadata důvěryhodnosti pro pracovní postupy opravy s nízkou důvěrou. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinuje deterministické kontroly napříč zdrojovými soubory, cílovými jazyky a nakonfigurovanými překladovými kořeny. |
| `ReviewTarget` | `co_op_translator.review.targets` | Popisuje zdrojový kořen a adresář s výstupy překladu, který se pro tento kořen kontroluje. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detekuje starší aliasové jazykové složky a připravuje plány migrace na kanonické BCP 47 složky. |
| `Config` | `co_op_translator.config.base_config` | Načítá soubory `.env` a kontroluje, zda jsou nakonfigurováni požadovaní poskytovatelé LLM a volitelně Vision. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automaticky detekuje Azure OpenAI, OpenAI nebo Anthropic, ověřuje požadované proměnné prostředí a spouští kontroly konektivity poskytovatele. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detekuje konfiguraci Azure AI Vision a provádí kontroly konektivity pro překlad obrázků. |