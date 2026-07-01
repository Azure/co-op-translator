# Python API

Stabilní veřejné Python API je exportováno z `co_op_translator.api`. Většina integrací používá jeden z těchto pracovních postupů:

| Scénář | Použijte, když | Hlavní API |
| --- | --- | --- |
| Přeložit jednotlivé soubory nebo dokumenty | Vaše aplikace načte zdrojový obsah, zavolá Co-op Translator pro překlad a rozhodne, kam výsledek uložit. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Připravit obsah pro překlad hostitelským agentem | Váš MCP host nebo aplikační model přeloží části, zatímco Co-op Translator zajišťuje dělení do částí a rekonstrukci. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Přeložit celé úložiště (repozitář) | Chcete, aby se Python API chovalo jako CLI a zpracovávalo objevování souborů, výstupní cesty, metadata, úklid a zápisy. | `run_translation` |

Většina podpůrných modulů pod `core`, `config`, `review` a `utils` jsou implementační detaily používané těmito vstupními body API.

Klienti MCP používají stejné veřejné API přes [MCP Server](mcp.md). Použijte tuto stránku při volání z Pythonu přímo a příručku MCP při vystavování Co-op Translator agentovi nebo editoru. Pokud se rozhodujete mezi CLI, Python API a MCP, začněte s [Choose Your Workflow](workflows.md).

## První kroky s API

Začněte zde, pokud voláte Co-op Translator z Python kódu:

1. Nakonfigurujte poskytovatele LLM podle [Configuration](configuration.md), pokud pouze nepřipravujete části Markdownu nebo notebooku pro překlad hostitelským agentem.
2. Rozhodněte, zda vaše aplikace spravuje operace se soubory (file I/O).
3. Použijte API pro obsah, když vaše aplikace čte a zapisuje jednotlivé soubory.
4. Použijte `run_translation`, když má Co-op Translator zpracovat repozitář podobně jako CLI.
5. Použijte `run_review` po překladu, pokud potřebujete deterministické kontroly v automatizaci.

| Cíl | API pro zahájení |
| --- | --- |
| Přeložit jeden Markdown řetězec nebo soubor | `translate_markdown_content` |
| Přeložit jeden notebook payload | `translate_notebook_content` |
| Přeložit jeden obrázek | `translate_image_content` |
| Nechat hostitelského agenta přeložit části Markdownu nebo notebooku | `start_markdown_agent_translation` nebo `start_notebook_agent_translation` |
| Přepsat přeložené odkazy po výběru výstupní cesty | `rewrite_markdown_paths` nebo `rewrite_notebook_paths` |
| Přeložit celé úložiště | `run_translation` |
| Zkontrolovat přeložený výstup | `run_review` |

## Scénář 1: Překlad jednotlivých souborů nebo dokumentů

Použijte tento postup, když už máte soubor, buffer v editoru, notebook payload, požadavek MCP nebo vlastní vstupní pipeline. Vaše kód spravuje I/O souborů:

1. Přečtěte zdrojový obsah.
2. Zavolejte API pro překlad obsahu.
3. Volitelně zavolejte API pro přepis cest, pokud bude přeložený obsah zapisován do překladové složky projektu.
4. Uložte nebo vraťte výsledek z vaší aplikace.

API pro překlad obsahu nespouštějí objevování projektu, nezapisují metadata, nepřidávají upozornění o strojovém překladu a nepřepisují odkazy automaticky.

### Markdown File

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

Pokud přeložený Markdown nebude umístěn v rozložení projektu Co-op Translator, přeskočte `rewrite_markdown_paths` a uložte přeložený řetězec přímo.

### Notebook File

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

`translate_notebook_content` překládá Markdown buňky a zachovává buňky, které nejsou Markdown. Přepisování cest se aplikuje pouze na Markdown buňky.

### Image File

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

`translate_image_content` načte zdrojový obrázek a vrátí vykreslený `PIL.Image.Image`. Nezapíše metadata přeloženého obrázku.

## Scénář 2: Přeložit celé úložiště

Použijte tento postup, když chcete, aby se Python API chovalo jako příkaz `translate` v CLI. `run_translation` objeví podporované soubory, přeloží vybrané typy obsahu, přepíše cesty, zapíše výstupní soubory, aktualizuje metadata a provede údržbářské úkoly překladu, jako je úklid.

`run_translation` je preferovaný vstup pro orchestraci projektu. `translate_project` je exportováno jako alias pro kompatibilitu se stejným chováním.

Přeložte Markdown soubory v aktuálním repozitáři do korejštiny a japonštiny:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Přeložte pouze notebooky ze specifického kořenového adresáře projektu:

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

Použijte zástupný podadresář pro každý jazyk, když má každý jazyk obsahovat vnořený podadresář:

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

## Kontrola přeloženého výstupu

`run_review` provádí deterministické kontroly překladu bez pověření pro LLM nebo Vision.

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

Zkontrolujte pouze soubory změněné vůči základní referenci a vytiskněte výstup ve formátu GitHub:

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

## Příklady pro kopírování a vložení

Přeložte Markdown obsah bez zápisu souborů:

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
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Zachovejte termíny ze slovníku:

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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API pro překlad obsahu

API pro překlad obsahu jsou určena pro integrace, které už mají obsah v paměti, například rozšíření editoru, nástroj MCP, procesor notebooků nebo vlastní pipeline.

| Funkce | Vstup | Výstup | Práce se soubory | Poznámky |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ne | Async. Překládá pouze obsah Markdownu. Nepřepisuje odkazy, nezapisuje metadata ani nepřidává upozornění. |
| `translate_notebook_content` | Notebook JSON `str` nebo `dict` | Notebook JSON `str` | Ne | Async. Překládá Markdown buňky a zachovává ne-Markdown buňky. Nepřepisuje odkazy, nezapisuje metadata ani nepřidává upozornění. |
| `translate_image_content` | Cesta k obrázku | `PIL.Image.Image` | Čte pouze zdrojový obrázek | Synchronní. Extrahuje a přeloží text z obrázku, poté vrátí vykreslený obrázek. Neukládá metadata přeloženého obrázku. |

`translate_markdown_content` a `translate_notebook_content` přijímají volitelnou `source_path` přes své možnosti. Cesta je předána jako kontext překladači; volající zůstávají odpovědní za jakékoliv projektově specifické přepisování cest po překladu.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Stejné možnosti mohou být předány jako slovníky:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API asistovaného překladu agentem

API asistovaného překladu agentem nevolají Azure OpenAI ani OpenAI z Co-op Translator. Připraví části Markdownu nebo notebooku pro přeložení hostitelským agentem a poté rekonstruují finální obsah z přeložených částí.

| Funkce | Účel |
| --- | --- |
| `start_markdown_agent_translation` | Vrátí samostatný Markdown úkol s částmi, promptami a stavem rekonstrukce. |
| `finish_markdown_agent_translation` | Rekonstruuje Markdown z úkolu a přeložených částí od hostitelského agenta. |
| `start_notebook_agent_translation` | Vrátí úkol notebooku s částmi Markdown buněk pro překlad hostitelským agentem. |
| `finish_notebook_agent_translation` | Rekonstruuje JSON notebooku při zachování kódových buněk, výstupů a metadata. |

Tento postup je hlavně určen pro MCP hosty. Pokud potřebujete produkční překlad repozitáře s tím, že Co-op Translator spravuje volání poskytovatelů, použijte `translate_markdown_content`, `translate_notebook_content` nebo `run_translation`.

## API pro přepis cest

API pro přepis cest neprovádějí žádný překlad. Aktualizují odkazy a cesty ve frontmatteru poté, co volající znají zdrojovou cestu, přeloženou cílovou cestu a rozložení projektu.

| Funkce | Rozsah | Poznámky |
| --- | --- | --- |
| `rewrite_markdown_paths` | Tělo Markdownu a frontmatter | Přepisuje Markdown odkazy a podporovaná pole frontmatteru pro přeložený cíl. |
| `rewrite_notebook_paths` | Markdown buňky v JSONu notebooku | Aplikuje přepis cest Markdownu na každou Markdown buňku a nechává ne-Markdown buňky beze změny. |

Argument `policy` může být slovník s těmito poli:

| Pole | Požadováno | Účel |
| --- | --- | --- |
| `language_code` | Ano | Kód cílového jazyka, například `"ko"` nebo `"pt-BR"`. |
| `root_dir` | Ne | Kořenový adresář zdrojového projektu. Výchozí je `"."`. |
| `translations_dir` | Ne | Výstupní adresář pro textové překlady. Ve výchozím nastavení `translations` pod `root_dir`. |
| `translated_images_dir` | Ne | Výstupní adresář pro přeložené obrázky. Ve výchozím nastavení `translated_images` pod `root_dir`. |
| `translation_types` | Ne | Povolené typy překladu. Ve výchozím nastavení Markdown, notebooky a obrázky. |
| `lang_subdir` | Ne | Volitelný podadresář pod každou jazykovou složkou. |

## Parametry překladu projektu

| Parametr | Typ | Výchozí | Účel |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Kódy cílových jazyků oddělené mezerami, například `"ko ja fr"`, nebo `"all"`. Alias kódy jsou normalizovány na kanonické hodnoty BCP 47. |
| `root_dir` | `str` | `"."` | Kořen projektu pro jeden překladový cíl. Ignorováno, když jsou zadány `root_dirs` nebo `groups`. |
| `update` | `bool` | `False` | Smazat a znovu vytvořit existující překlady pro vybrané jazyky. |
| `images` | `bool` | `False` | Zahrnout překlad obrázků. Vyžaduje konfiguraci Azure AI Vision. |
| `markdown` | `bool` | `False` | Zahrnout překlad Markdownu. |
| `notebook` | `bool` | `False` | Zahrnout překlad Jupyter notebooků. |
| `debug` | `bool` | `False` | Zapnout debug logování. |
| `save_logs` | `bool` | `False` | Uložit log soubory úrovně DEBUG do kořenového adresáře `logs/`. |
| `yes` | `bool` | `True` | Automaticky potvrdit výzvy pro programové a CI použití. |
| `add_disclaimer` | `bool` | `False` | Přidat upozornění o strojovém překladu do přeloženého Markdownu a notebooků. |
| `translations_dir` | `str \| None` | `None` | Vlastní výstupní adresář pro textové překlady. Relativní cesty se řeší proti každému kořenu. |
| `image_dir` | `str \| None` | `None` | Vlastní výstupní adresář pro přeložené obrázky. Relativní cesty se řeší proti každému kořenu. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Více kořenů, které sdílí stejná výstupní nastavení. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicitní páry `(root_dir, translations_dir)`. Má prioritu před `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozitáře používané při vykreslování návodu v tabulce jazyků README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termíny slovníku, které je třeba zachovat během překladu. Duplikáty a prázdné položky jsou normalizovány. |
| `dry_run` | `bool` | `False` | Odhadnout objem překladu a zobrazit náhled chování migrace bez zápisu souborů. |

## Parametry kontroly

`run_review` záměrně zrcadlí podpis `run_translation` tam, kde je to možné, aby automatizace mohla přepínat mezi workflow pro překlad a kontrolu s minimem rozvětvování.

| Parametr | Typ | Výchozí | Účel |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Jazykové složky k revizi. Jsou akceptovány řetězce oddělené mezerami i iterovatelné kolekce. `"all"` zkontroluje všechny objevené překladové jazyky. |
| `root_dir` | `str` | `"."` | Kořen projektu pro jeden cíl kontroly. Ignorováno, když jsou zadány `root_dirs` nebo `groups`. |
| `markdown` | `bool` | `False` | Zahrnout zdrojové soubory Markdown a MDX. |
| `notebook` | `bool` | `False` | Zahrnout zdrojové soubory Jupyter notebooků. |
| `images` | `bool` | `False` | Rezervováno pro shodu s možnostmi překladu. Odkazy na obrázky jsou kontrolovány z Markdownu. |
| `translations_dir` | `str \| None` | `None` | Vlastní výstupní adresář pro překlady textů. Relativní cesty se řeší vůči každému kořeni. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Více kořenů, které sdílí stejné výstupní nastavení. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicitní `(root_dir, translations_dir)` páry. Mají přednost před `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref používaný k omezení kontroly na změněné zdrojové soubory. |
| `output_format` | `str` | `"text"` | Formát výstupu kontroly. Podporované hodnoty jsou `"text"` a `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Považovat varování za selhání (kromě chyb). |
| `debug` | `bool` | `False` | Povolit ladicí protokolování. |
| `save_logs` | `bool` | `False` | Uložit soubory protokolů na úrovni DEBUG do kořenového adresáře `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Požadavky na konfiguraci

Provider-backed translation APIs require provider configuration before translating:

- Překlad Markdownu a notebooků vyžaduje poskytovatele LLM. Nakonfigurujte buď Azure OpenAI nebo OpenAI.
- Překlad obrázků vyžaduje Azure AI Vision navíc k poskytovateli LLM.
- `run_translation` provádí lehké kontroly konektivity před zahájením překladu projektu.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` a `run_review` jsou deterministické a nevyžadují pověření poskytovatelů.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` je deterministické a nevyžaduje konfiguraci Azure OpenAI, OpenAI ani Azure AI Vision.

## Poznámky k chování

- API pro překlad obsahu oddělují překlad od přepisování cest projektu. Zavolejte explicitně `rewrite_markdown_paths` nebo `rewrite_notebook_paths`, když je potřeba upravit projektově relativní odkazy v přeloženém obsahu pro cílové umístění.
- Orkestrující API projektů přidávají chování kolem překladu obsahu, včetně vyhledávání souborů, zápisů, přepisování cest, metadat, úklidu a volitelných prohlášení.
- `run_translation` vypisuje průběh a souhrny odhadů přes Click, což odpovídá uživatelskému zážitku z CLI.
- `dry_run=True` vypočítá odhady pomocí virtuálních aktualizací README, ale README ani překladové soubory nezapisuje.
- `groups` jsou zpracovávány sekvenčně. Jediný souhrnný odhad se vypíše před zahájením práce.
- Když je vybrán překlad obrázků, chybějící konfigurace Vision vyvolá chybu ještě před zahájením překladu.
- Existující aliasové jazykové složky jsou detekovány a mohou být součástí běhu převedeny na kanonické názvy jazykových složek.
- `run_review` selže při chybějících přeložených souborech, chybějících nebo zastaralých metadatech překladu, poškozeném Markdown frontmatter/kódových blocích a neplatném JSONu přeloženého notebooku.
- `run_review` hlásí chybějící lokální cíle Markdownu a odkazů na obrázky jako varování ve výchozím nastavení.

## Interní volací cesta

The API delegates to the same core implementation used by the CLI:

Překlad:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Revize:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Třída | Modul | Odpovědnost |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinuje překlad na úrovni projektu, správu adresářů, normalizaci metadat pro jednotlivé jazyky a delegování na překladače Markdownu, notebooků a obrázků. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Provádí asynchronní zpracování souborů pro Markdown, notebooky, obrázky, detekci zastaralosti a aktualizace metadat překladu. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestruje čtení Markdown souborů, překlad obsahu, přepisování cest, metadata, prohlášení a zápisy. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestruje čtení notebooků, překlad buněk Markdown, přepisování cest, metadata, prohlášení a zápisy. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestruje hledání zdrojových obrázků, překlad obrázků, výstupní cesty, metadata a zápisy. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Najde přeložené páry Markdownů, hodnotí kvalitu překladu a čte metadata důvěryhodnosti pro pracovní postupy opravy s nízkou důvěrou. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinuje deterministické kontroly revize napříč zdrojovými soubory, cílovými jazyky a nakonfigurovanými kořeny překladu. |
| `ReviewTarget` | `co_op_translator.review.targets` | Popisuje zdrojový kořen a adresář výstupu překladu, který je pro tento kořen kontrolován. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detekuje starší aliasové jazykové složky a připravuje plány migrace na kanonické složky BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Načítá soubory `.env` a kontroluje, zda jsou nakonfigurováni povinní poskytovatelé LLM a volitelně Vision. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automaticky detekuje Azure OpenAI nebo OpenAI, ověřuje povinné proměnné prostředí a provádí kontroly konektivity poskytovatelů. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detekuje konfiguraci Azure AI Vision a provádí kontroly konektivity pro překlad obrázků. |