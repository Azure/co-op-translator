# Python API

Стабилан јаван Python API је експортован из `co_op_translator.api`. Већина интеграција користи један од ових токова рада:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Вашa апликацијa учитава изворни садржај, позива Co-op Translator за превод и одлучује где ће сачувати резултат. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Ваш MCP хост или апликацијски модел ће преводити делове, док Co-op Translator обрађује разбијање на делове и реконструкцију. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Желите да Python API ради као CLI и обавља претрагу, управља путањама за излаз, метаподацима, чишћењем и записивањем резултата. | `run_translation` |

Већина нижих модула у оквиру `core`, `config`, `review`, и `utils` су имплементацијски детаљи које користе ове улазне тачке API-ја.

MCP клијенти користе исти јавни API преко [MCP Server](mcp.md). Користите ову страницу када позивате Python директно, а MCP водич када излажете Co-op Translator агенту или уређивачу. Ако одлучујете између CLI, Python API и MCP, почните са [Choose Your Workflow](workflows.md).

## First-Time API Flow

Почните овде ако позивате Co-op Translator из Python кода:

1. Конфигуришите LLM провајдера као што је описано у [Configuration](configuration.md), осим ако само припремате Markdown или notebook делове за host-agent превод.
2. Одлучите да ли ваша апликација управља I/O датотекама.
3. Користите content API-је када ваша апликација чита и записује појединачне датотеке.
4. Користите `run_translation` када Co-op Translator треба да обради репозиторијум као CLI.
5. Користите `run_review` након превода ако су вам потребне детерминистичке провере у аутоматизацији.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Користите овај ток рада када већ имате датотеку, уређивачки бафер, notebook payload, MCP захтев или прилагођени улазни ток. Ваш код контролише I/O датотека:

1. Прочитајте изворни садржај.
2. Позовите content translation API.
3. По потреби позовите path rewriting API ако ће преведени садржај бити записан у фолдер за превод пројекта.
4. Сачувајте или вратите резултат из ваше апликације.

Content translation API-ји не покрећу претрагу пројекта, не записују метаподатке, не додају дисклејмере и не преписују аутоматски линкове.

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

Ако преведени Markdown неће бити унутар Co-op Translator распореда пројекта, прескочите `rewrite_markdown_paths` и сачувајте преведени низ директно.

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

`translate_notebook_content` преводи Markdown ћелије и задржава не-Markdown ћелије. Преписивање путања се примењује само на Markdown ћелије.

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

`translate_image_content` учитава извornu слику и враћа рендеровани `PIL.Image.Image`. Не записује метаподатке преведене слике.

## Scenario 2: Translate an Entire Repository

Користите овај ток рада када желите да Python API ради као `translate` CLI. `run_translation` открива подржане датотеке, преводи изабране типове садржаја, преписује путање, записује излазне датотеке, ажурира метаподатке и обавља задатке одржавања превода као што је чишћење.

`run_translation` је препоручена улазна тачка за оркестрацију пројекта. `translate_project` је експортован као алијас за компатибилност са истим понашањем.

Преведите Markdown датотеке у тренутном репозиторијуму на корејски и јапански:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Преведите само notebook-ове из специфичног корена пројекта:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Прегледајте обим превода без записивања датотека:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Преведите више корена садржаја у једном позиву:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Запишите преводе у експлицитне групе за излаз:

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

Користите заменицу по језику када сваки језик треба да садржи угнежђени поддиректоријум:

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

Ако ниједно од `markdown`, `notebook`, или `images` није подешено, API преводи све подржане типове: Markdown, notebook-ове и слике.

## Review Translated Output

`run_review` покреће детерминистичке провере превода без LLM или Vision акредитива.

!!! note "Бета"
    `run_review` је бета детерминистички review API. Не позива провајдере модела нити записује датотеке, али шеме провера и проблема могу еволуирати.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Прегледајте само датотеке које су измењене у односу на базни ref и исписујте GitHub-flavored излаз:

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

## Copy-Paste API Examples

Преведите Markdown садржај без записивања датотека:

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

Преведите и препишите Markdown линкове:

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

Преведите репозиторијум из Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Преведите више корена:

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

Задржите појмове из глосара:

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

## Public Entry Points

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

## Content Translation APIs

Content translation API-ји су намењени интеграцијама које већ имају садржај у меморији, као што су екстензија уређивача, MCP алат, процесор за notebook-ове или прилагођени ток.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Преводи само Markdown садржај. Не преписује линкове, не записује метаподатке и не додаје дисклејмере. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Преводи Markdown ћелије и задржава не-Markdown ћелије. Не преписује линкове, не записује метаподатке и не додаје дисклејмере. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Извлачи и преводи текст са слике, затим враћа рендеровану слику. Не чува метаподатке преведене слике. |

`translate_markdown_content` и `translate_notebook_content` прихватају опциони `source_path` кроз своје опције. Путања се прослеђује као контекст преводиоцу; позиваоци остају одговорни за било које специфично преписивање путања пројекта након превода.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Исте опције могу бити прослеђене као речници:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted API-ји не позивају Azure OpenAI или OpenAI из Co-op Translator-а. Они припремају Markdown или notebook делове за host агента да преведе, а затим реконструишу финални садржај из преведених делова.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Врати самосталан Markdown job са деловима, промптовима и стањем за реконструкцију. |
| `finish_markdown_agent_translation` | Реконструише Markdown из job-а и host-agent преведених делова. |
| `start_notebook_agent_translation` | Врати notebook job са Markdown-ћелијским деловима за host-agent превод. |
| `finish_notebook_agent_translation` | Реконструише notebook JSON уз задржавање code ћелија, output-ова и метаподатака. |

Овај ток рада је углавном намењен MCP хостовима. Ако вам је потребан production превод репозиторијума где Co-op Translator управља позивима провајдера, користите `translate_markdown_content`, `translate_notebook_content`, или `run_translation`.

## Path Rewriting APIs

Path rewriting API-ји не обављају превод. Они ажурирају линкове и frontmatter путање након што позиваоци знају изворну путању, преведену циљну путању и распореда пројекта.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Преписује Markdown линкове и подржана frontmatter пољa путања за преведену цел. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Примeњује Markdown преписивање путања на сваку Markdown ћелију и оставља не-Markdown ћелије непромењене. |

Аргумент `policy` може бити речник са следећим пољима:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Код циљног језика, као што је `"ko"` или `"pt-BR"`. |
| `root_dir` | No | Изворни корен пројекта. Подразумевано `"."`. |
| `translations_dir` | No | Директоријум за излазни текст превода. Подразумевано `translations` у оквиру `root_dir`. |
| `translated_images_dir` | No | Директоријум за преведене слике. Подразумевано `translated_images` у оквиру `root_dir`. |
| `translation_types` | No | Омогућени типови превода. Подразумевано Markdown, notebook-ови и слике. |
| `lang_subdir` | No | Опционални поддиректоријум под сваким језичким фолдером. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Целине циљних језичких кодова раздвојених размаком, као што су `"ko ja fr"`, или `"all"`. Алијас кодови се нормализују на канонске BCP 47 вредности. |
| `root_dir` | `str` | `"."` | Корен пројекта за један преводни циљ. Игнорише се када су `root_dirs` или `groups` прослеђени. |
| `update` | `bool` | `False` | Обриши и поново креира постојеће преводе за изабране језике. |
| `images` | `bool` | `False` | Укључи превод слика. Захтева Azure AI Vision конфигурацију. |
| `markdown` | `bool` | `False` | Укључи Markdown превод. |
| `notebook` | `bool` | `False` | Укључи Jupyter notebook превод. |
| `debug` | `bool` | `False` | Омогући debug логовање. |
| `save_logs` | `bool` | `False` | Сачувај DEBUG нивое лог фајлова унутар корена у `logs/` директоријуму. |
| `yes` | `bool` | `True` | Аутоматски потврђује упите за програмско и CI коришћење. |
| `add_disclaimer` | `bool` | `False` | Додаје дисклејмере машинског превода у преведени Markdown и notebook-ове. |
| `translations_dir` | `str \| None` | `None` | Прилагођени директоријум за излазни текст превода. Релативне путање се решавају у односу на сваки корен. |
| `image_dir` | `str \| None` | `None` | Прилагођени директоријум за преведене слике. Релативне путање се решавају у односу на сваки корен. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Више корена који деле иста излазна подешавања. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Експлицитне `(root_dir, translations_dir)` парове. Преовладава над `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL репозиторијума који се користи при рендеровању упутства у README табели језика. |
| `glossaries` | `Iterable[str] \| None` | `None` | Појмови из глосара које треба задржати током превода. Дупликати и празни појмови се нормализују. |
| `dry_run` | `bool` | `False` | Процени обим превода и прегледај понашање миграције без записивања датотека. |

## Review Parameters

`run_review` намерно огледа signature `run_translation` када је то могуће тако да аутоматизација може да пребацује између преводних и ревизионих токова са минималним гранама.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Језички фолдери које треба рецензирати. Прихватају се низови раздвојени размаком и итерабли. `"all"` рецензира све откривене језике превода. |
| `root_dir` | `str` | `"."` | Корен пројекта за један ревизорски циљ. Игнорише се када су `root_dirs` или `groups` прослеђени. |
| `markdown` | `bool` | `False` | Укључи Markdown и MDX изворне фајлове. |
| `notebook` | `bool` | `False` | Укључи Jupyter notebook изворне фајлове. |
| `images` | `bool` | `False` | Резервисано за паритет са опцијама превода. Референце на слике се проверавају из Markdown-а. |
| `translations_dir` | `str \| None` | `None` | Прилагођени директоријум за излаз превода текста. Релативне путање се тумаче у односу на сваки root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Више root директоријума који деле исте поставке за излаз. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Експлицитни парови `(root_dir, translations_dir)`. Има приоритета над `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git референца која се користи да ограничи преглед на измењене изворне фајлове. |
| `output_format` | `str` | `"text"` | Формат излаза прегледа. Подржане вредности су `"text"` и `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Сматрајте упозорења као неуспехе поред грешака. |
| `debug` | `bool` | `False` | Омогућите debug логовање. |
| `save_logs` | `bool` | `False` | Сачувајте DEBUG-ниво лог фајлове унутар root директоријума `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Захтеви за конфигурацију

Provider-backed translation APIs require provider configuration before translating:

- Превод Markdown-а и notebook-ова захтева LLM провајдера. Конфигуришите или Azure OpenAI или OpenAI.
- Превод слика захтева Azure AI Vision поред LLM провајдера.
- `run_translation` покреће лагане провере повезаности пре почетка превођења пројекта.
- Agent-помогнути `start_*_agent_translation` и `finish_*_agent_translation` API-ји не позивају Co-op Translator LLM провајдере. Домаћин апликација или MCP агент преводи припремљене делове.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` и `run_review` су детерминистички и не захтевају акредитиве провајдера.

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

`run_review` је детерминистички и не захтева конфигурацију Azure OpenAI, OpenAI, или Azure AI Vision.

## Напомене о понашању

- API-ји за превод садржаја одржавају превод одвојеним од пренамештања путева у пројекту. Позовите експлицитно `rewrite_markdown_paths` или `rewrite_notebook_paths` када преведени садржај треба да прилагоди пројектно-релативне везе за циљну локацију.
- API-ји за оркестрацију пројекта додају пројектно понашање око превода садржаја, укључујући проналажење фајлова, записивање, пренамештање путева, метаподатке, чишћење и опционалне одрицања одговорности.
- `run_translation` исписује резиме прогреса и процена преко Click-а, усклађујући се са CLI корисничким искуством.
- `dry_run=True` рачуна процене користећи виртуелне измене README-а, али не уписује README или фајлове превода.
- `groups` се обрађују секвенцијално. Једна агрегатна процена се исписује пре почетка рада.
- Када је изабран превод слика, недостатак Vision конфигурације изазива грешку пре него што превод почне.
- Постојећи језички фолдери засновани на алијасима се детектују и могу бити мигрирани у канонска имена језичких фолдера као део покретања.
- `run_review` неуспева на недостајућим преведеним фајловима, недостајућим или застарелим метаподацима превода, неисправном Markdown frontmatter-у/код оградама и неважећем преведеном notebook JSON-у.
- `run_review` подразумевано пријављује недостајуће локалне Markdown и циљеве сликовних веза као упозорења.

## Интерна путања позива

The API delegates to the same core implementation used by the CLI:

Превођење:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` за превод у меморији.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` за експлицитну постобраду путева.
3. `co_op_translator.api.translation.run_translation` за пуну оркестрацију пројекта.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Фокусирани пројектни миксини за превод Markdown-а, notebook-ова и слика.
8. Markdown, notebook, текст и преводиоци слика у оквиру `co_op_translator.core`.

Преглед:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерминистичке провере у оквиру `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Класа | Модул | Одговорност |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Кооординише превод на нивоу пројекта, управљање директоријумима, нормализацију метаподатака по језику и делегирање на Markdown, notebook и преводиоце слика. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Обавља асинхрони рад на обради фајлова за Markdown, notebook-ове, слике, детекцију застарелости и ажурирања метаподатака превода. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркестрира читање Markdown фајлова, превод садржаја, пренамештање путева, метаподатке, одрицања одговорности и записивања. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркестрира читање notebook фајлова, превод Markdown ћелија, пренамештање путева, метаподатке, одрицања одговорности и записивања. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркестрира откривање изворних слика, превод слика, излазне путеве, метаподатке и записивања. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Проналази парове преведених Markdown-ова, оцењује квалитет превода и чита метаподатке поверења за радне токове поправке ниског поверења. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координише детерминистичке провере прегледа преко изворних фајлова, циљних језика и конфигурисаних корена превода. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описује изворни root и директоријум излаза превода који се прегледа за тај root. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Детектује наследне алијас језичке фолдере и припрема планове миграције у канонске BCP 47 фолдере. |
| `Config` | `co_op_translator.config.base_config` | Учитава `.env` фајлове и проверава да ли су потребни LLM и опциони Vision провајдери конфигурисани. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Аутоматски детектује Azure OpenAI или OpenAI, валида потребне променљиве окружења и покреће провере повезаности провајдера. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Детектује Azure AI Vision конфигурацију и покреће провере повезаности за превод слика. |