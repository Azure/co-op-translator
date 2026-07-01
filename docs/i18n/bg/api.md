# Python API

Стабилният публичен Python API се експортира от `co_op_translator.api`. Повечето интеграции използват един от следните работни потоци:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Вашето приложение чете изходното съдържание, извиква Co-op Translator за превод и решава къде да запази резултата. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Вашият MCP хост или модел на приложението ще превежда парчета, докато Co-op Translator се грижи за разделянето на парчетата и реконструкцията. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Искате Python API да се държи като CLI и да се занимава с откриване, пътища за изход, метаданни, почистване и запис. | `run_translation` |

Повечето по-ниско ниво модули под `core`, `config`, `review` и `utils` са детайли на имплементацията, използвани от тези входни точки на API.

Клиентите на MCP използват същия публичен API чрез [MCP Server](mcp.md). Използвайте тази страница когато извиквате Python директно, а ръководството за MCP когато експонирате Co-op Translator към агент или редактор. Ако решавате между CLI, Python API и MCP, започнете с [Choose Your Workflow](workflows.md).

## First-Time API Flow

Започнете тук ако извиквате Co-op Translator от Python код:

1. Конфигурирайте доставчик на LLM както е описано в [Configuration](configuration.md), освен ако само подготвяте Markdown или notebook парчета за превод от хост-агент.
2. Решете дали вашето приложение да отговаря за файловия I/O.
3. Използвайте content APIs когато вашето приложение чете и записва отделни файлове.
4. Използвайте `run_translation` когато Co-op Translator трябва да обработи репозитория като CLI.
5. Използвайте `run_review` след превода ако имате нужда от детерминирани проверки в автоматизация.

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

Използвайте този работен поток когато вече разполагате с файл, буфер от редактор, notebook payload, MCP заявка или персонализиран вход за конвейер. Вашият код отговаря за файловия I/O:

1. Прочетете изходното съдържание.
2. Извикайте content translation API.
3. По желание извикайте path rewriting API ако преведеният материал ще бъде записан в папка за преводи на проект.
4. Запазете или върнете резултата от вашето приложение.

Content translation API-тата не изпълняват откриване на проекти, не записват метаданни, не добавят отказ от отговорност и не пренаписват връзки автоматично.

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

Ако преведеният Markdown няма да живее в оформление на проект на Co-op Translator, пропуснете `rewrite_markdown_paths` и запазете преведения низ директно.

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

`translate_notebook_content` превежда Markdown клетки и запазва несвързаните с Markdown клетки. Пренаписването на пътища се прилага само към Markdown клетките.

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

`translate_image_content` чете изходното изображение и връща рендериран `PIL.Image.Image`. То не записва метаданни за преведеното изображение.

## Scenario 2: Translate an Entire Repository

Използвайте този работен поток когато искате Python API да се държи като `translate` CLI. `run_translation` открива поддържани файлове, превежда избраните типове съдържание, пренаписва пътища, записва изходни файлове, обновява метаданни и изпълнява задачи за поддръжка на превода като почистване.

`run_translation` е предпочитаната входна точка за оркестрация на проекти. `translate_project` е експортиран като алиас за съвместимост със същото поведение.

Преведете Markdown файлове в текущото хранилище на корейски и японски:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Преведете само notebooks от конкретен root на проекта:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Прегледайте обем на превод без записване на файлове:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Преведете няколко корена в едно извикване:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Запишете преводите в изрични output групи:

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

Използвайте заместител за всеки език когато всеки език трябва да съдържа вложена подпапка:

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

Ако никой от `markdown`, `notebook` или `images` не е зададен, API превежда всички поддържани типове: Markdown, notebooks и изображения.

## Review Translated Output

`run_review` изпълнява детерминирани проверки на превода без LLM или Vision удостоверения.

!!! note "Beta"
    `run_review` е бета детерминиран API за преглед. Той не извиква доставчици на модели и не записва файлове, но схемите за проверка и проблеми могат да се променят.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Прегледайте само файловете, променени спрямо базов ref и отпечатайте изход във формат GitHub:

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

Превеждане на Markdown съдържание без файлови записвания:

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

Превеждане и пренаписване на Markdown връзки:

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

Превеждане на репозитория от Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Превеждане на множество корени:

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

Запазване на термини от глосар:

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

Content translation API-тата са предназначени за интеграции, които вече имат съдържание в паметта, като разширение за редактор, MCP инструмент, процесор за notebooks или персонализиран конвейер.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Превежда само Markdown съдържание. Не пренаписва връзки, не записва метаданни и не добавя откази от отговорност. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Превежда Markdown клетки и запазва несвързаните с Markdown клетки. Не пренаписва връзки, не записва метаданни и не добавя откази от отговорност. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Извлича и превежда текста от изображението, след което връща рендерирано изображение. Не запазва метаданни за преведеното изображение. |

`translate_markdown_content` и `translate_notebook_content` приемат по избор `source_path` чрез техните опции. Пътят се предава като контекст на преводача; извикващите остават отговорни за всяко проектно-специфично пренаписване на пътища след превода.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Същите опции могат да бъдат предадени като речници:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted API-тата не извикват Azure OpenAI или OpenAI от Co-op Translator. Те подготвят Markdown или notebook парчета за превод от хост-агент, след което реконструират финалното съдържание от преведените парчета.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Връща самостоятелна Markdown задача с парчета, подсказки и състояние за реконструкция. |
| `finish_markdown_agent_translation` | Реконструира Markdown от задача и преведени от хост-агент парчета. |
| `start_notebook_agent_translation` | Връща notebook задача с Markdown-клетъчни парчета за превод от хост-агент. |
| `finish_notebook_agent_translation` | Реконструира notebook JSON като запазва кодовите клетки, изходите и метаданните. |

Този работен поток е основно предназначен за MCP хостове. Ако се нуждаете от продукционен превод на репозитория с Co-op Translator, който управлява извикванията към доставчиците, използвайте `translate_markdown_content`, `translate_notebook_content` или `run_translation`.

## Path Rewriting APIs

Path rewriting API-тата не изпълняват превод. Те обновяват връзки и полета в frontmatter след като извикващите познават изходния път, преведения целеви път и оформление на проекта.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Пренаписва Markdown връзки и поддържани полета от frontmatter за преведената цел. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Прилага пренаписване на Markdown пътища към всяка Markdown клетка и оставя несвързаните с Markdown клетки непроменени. |

Аргументът `policy` може да бъде речник с тези полета:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Код на целевия език, например `"ko"` или `"pt-BR"`. |
| `root_dir` | No | Изходен root на проекта. По подразбиране `"."`. |
| `translations_dir` | No | Директория за изход на текстовите преводи. По подразбиране `translations` под `root_dir`. |
| `translated_images_dir` | No | Директория за преведени изображения. По подразбиране `translated_images` под `root_dir`. |
| `translation_types` | No | Разрешени типове преводи. По подразбиране Markdown, notebooks и изображения. |
| `lang_subdir` | No | По избор подпапка под всяка езикова папка. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Цепка от кодове на целеви езици, разделени с интервал, например `"ko ja fr"`, или `"all"`. Алиас кодовете се нормализират до канонични BCP 47 стойности. |
| `root_dir` | `str` | `"."` | Root на проекта за една цел на превод. Игнорира се когато са подадени `root_dirs` или `groups`. |
| `update` | `bool` | `False` | Изтриване и повторно създаване на съществуващите преводи за избраните езици. |
| `images` | `bool` | `False` | Включване на превод на изображения. Изисква конфигурация на Azure AI Vision. |
| `markdown` | `bool` | `False` | Включване на превод на Markdown. |
| `notebook` | `bool` | `False` | Включване на превод на Jupyter notebooks. |
| `debug` | `bool` | `False` | Включване на debug логване. |
| `save_logs` | `bool` | `False` | Запазване на DEBUG ниво лог файлове под root директория `logs/`. |
| `yes` | `bool` | `True` | Авто-потвърждение на подсказвания за програмна и CI употреба. |
| `add_disclaimer` | `bool` | `False` | Добавяне на отказ от отговорност за машинен превод към преведените Markdown и notebooks. |
| `translations_dir` | `str \| None` | `None` | Потребителска директория за изход на текстов превод. Относителните пътища се решават спрямо всеки root. |
| `image_dir` | `str \| None` | `None` | Потребителска директория за изход на преведени изображения. Относителните пътища се решават спрямо всеки root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Множество корени, които споделят едни и същи настройки за изход. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явни `(root_dir, translations_dir)` двойки. Имплицитно има приоритет пред `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL на репозитория, използван при рендиране на ръководство за езиковата таблица в README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Термини от глосар, които да се запазят по време на превода. Дубликатите и празните термини се нормализират. |
| `dry_run` | `bool` | `False` | Оценява обема на превода и визуализира поведението на миграцията без записване на файлове. |

## Review Parameters

`run_review` умишлено огледално пресъздава подписа на `run_translation` където е възможно, така че автоматизацията да може да превключва между превод и преглед с минимални разклонения.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Целеви езикови папки за преглед. Приемат се стрингове с разделени с интервал и итерабълни стойности. `"all"` преглежда всички открити преводни езици. |
| `root_dir` | `str` | `"."` | Root на проекта за една цел на преглед. Игнорира се когато са подадени `root_dirs` или `groups`. |
| `markdown` | `bool` | `False` | Включва Markdown и MDX изходни файлове. |
| `notebook` | `bool` | `False` | Включва Jupyter notebook изходни файлове. |
| `images` | `bool` | `False` | Запазено за паритет с опциите за превод. Препратките към изображения се проверяват от Markdown. |
| `translations_dir` | `str \| None` | `None` | Папка за изход на превода на текст по избор. Относителните пътища се разрешават спрямо всеки root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Няколко root директории, които споделят еднакви настройки за изход. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явни двойки `(root_dir, translations_dir)`. Има предимство пред `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref, използван за ограничаване на прегледа до променените изходни файлове. |
| `output_format` | `str` | `"text"` | Формат на изхода на прегледа. Поддържаните стойности са `"text"` и `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Третира предупрежденията като неуспехи в допълнение към грешките. |
| `debug` | `bool` | `False` | Активира логване за отстраняване на грешки. |
| `save_logs` | `bool` | `False` | Запазва лог файлове с ниво DEBUG в директорията `logs/` под root. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Изисквания за конфигурация

Provider-backed translation APIs require provider configuration before translating:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

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

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Бележки за поведението

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Вътрешен път на извикване

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` за превод в паметта.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` за експлицитна последваща обработка на пътища.
3. `co_op_translator.api.translation.run_translation` за пълна оркестрация на проекта.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Фокусирани миксини за проектен превод за Markdown, notebooks, и изображения.
8. Markdown, notebook, текстови и преводачи на изображения под `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Клас | Модул | Отговорност |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координира превода на ниво проект, управлението на директории, нормализирането на метаданни за всеки език и делегирането към Markdown, notebook и преводачи на изображения. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Изпълнява асинхронната обработка на файлове за Markdown, notebooks, изображения, откриване на остарели елементи и актуализации на метаданните за превод. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркестрира четене на Markdown файлове, превод на съдържание, пренаписване на пътища, метаданни, уведомления и записване. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркестрира четене на notebook файлове, превод на Markdown клетки, пренаписване на пътища, метаданни, уведомления и записване. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркестрира намирането на изходни изображения, превод на изображения, пътища за изход, метаданни и записвания. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Намира преведени Markdown двойки, оценява качеството на превода и чете метаданни за увереност за работни потоци за поправка при ниска увереност. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координира детерминистични проверки на прегледа върху изходни файлове, целеви езици и конфигурирани корени за превод. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описва източников root и директорията за изход на превода, която се преглежда за този root. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Открива остарели алиас езикови папки и подготвя планове за миграция към канонични папки по BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Зарежда `.env` файлове и проверява дали задължителните LLM и опционалните Vision доставчици са конфигурирани. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Автоматично открива Azure OpenAI или OpenAI, валидира задължителните променливи на средата и изпълнява проверки на свързаност за доставчика. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Открива конфигурация за Azure AI Vision и изпълнява проверки на свързаност за превод на изображения. |