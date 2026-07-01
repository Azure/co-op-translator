# Python API

Стабильный публичный Python API экспортируется из `co_op_translator.api`. Большинство интеграций используют один из этих рабочих процессов:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Ваше приложение читает исходное содержимое, вызывает Co-op Translator для перевода и решает, куда сохранить результат. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Ваш MCP-хост или модель приложения будет переводить фрагменты, в то время как Co-op Translator обрабатывает разбиение на части и реконструкцию. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Вы хотите, чтобы Python API вел себя как CLI и выполнял обнаружение, выбор путей вывода, запись метаданных, очистку и запись файлов. | `run_translation` |

Большинство низкоуровневых модулей под `core`, `config`, `review` и `utils` — это детали реализации, используемые этими точками входа API.

Клиенты MCP используют тот же публичный API через [MCP Server](mcp.md). Используйте эту страницу при вызове Python напрямую, а руководство MCP — при экспонировании Co-op Translator агенту или редактору. Если вы выбираете между CLI, Python API и MCP, начните с [Choose Your Workflow](workflows.md).

## First-Time API Flow

Начните здесь, если вы вызываете Co-op Translator из кода на Python:

1. Настройте поставщика LLM, как описано в [Configuration](configuration.md), если вы не только подготавливаетеMarkdown или фрагменты блокнота для перевода хост-агентом.
2. Решите, будет ли ваше приложение отвечать за ввод/вывод файлов.
3. Используйте API для работы с содержимым, когда ваше приложение читает и записывает отдельные файлы.
4. Используйте `run_translation`, когда Co-op Translator должен обрабатывать репозиторий как CLI.
5. Используйте `run_review` после перевода, если вам нужны детерминированные проверки в автоматизации.

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

Используйте этот рабочий процесс, когда у вас уже есть файл, буфер редактора, полезная нагрузка блокнота, запрос MCP или вход в кастомном конвейере. Ваш код отвечает за ввод/вывод файлов:

1. Прочитайте исходное содержимое.
2. Вызовите API перевода содержимого.
3. При необходимости вызовите API переписывания путей, если переводимое содержимое будет записано в папку перевода проекта.
4. Сохраните или верните результат из вашего приложения.

API перевода содержимого не выполняют обнаружение проекта, не записывают метаданные, не добавляют дисклеймеры и автоматически не переписывают ссылки.

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

Если переведённый Markdown не будет находиться в структуре проекта Co-op Translator, пропустите `rewrite_markdown_paths` и сохраните переведённую строку напрямую.

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

`translate_notebook_content` переводит Markdown-ячейки и сохраняет не-Markdown ячейки. Переписывание путей применяется только к Markdown-ячейкам.

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

`translate_image_content` читает исходное изображение и возвращает отрисованное `PIL.Image.Image`. Он не записывает метаданные переведённого изображения.

## Scenario 2: Translate an Entire Repository

Используйте этот рабочий процесс, когда вы хотите, чтобы Python API вел себя как `translate` CLI. `run_translation` обнаруживает поддерживаемые файлы, переводит выбранные типы содержимого, переписывает пути, записывает выходные файлы, обновляет метаданные и выполняет задачи обслуживания перевода, такие как очистка.

`run_translation` — предпочтительная точка входа для оркестрации проекта. `translate_project` экспортируется как псевдоним совместимости с тем же поведением.

Перевести файлы Markdown в текущем репозитории на корейский и японский:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Перевести только блокноты из конкретного корня проекта:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Просмотреть объём перевода без записи файлов:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Перевести несколько корней содержимого за один вызов:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Записать переводы в явные группы вывода:

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

Использовать плейсхолдер для каждого языка, когда для каждого языка должен быть вложенный подкаталог:

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

Если ни один из параметров `markdown`, `notebook` или `images` не установлен, API переводит все поддерживаемые типы: Markdown, блокноты и изображения.

## Review Translated Output

`run_review` выполняет детерминированные проверки перевода без учетных данных LLM или Vision.

!!! note "Beta"
    `run_review` is a beta deterministic review API. It does not call model providers or write files, but checks and issue schemas may evolve.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Проверять только файлы, изменённые относительно базового ref, и печатать вывод в формате GitHub:

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

Перевести содержимое Markdown без записи файлов:

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

Перевести и переписать ссылки в Markdown:

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

Перевести репозиторий из Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Перевести несколько корней:

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

Сохранить термины из глоссария:

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

API перевода содержимого предназначены для интеграций, которые уже имеют содержимое в памяти, таких как расширение редактора, инструмент MCP, процессор блокнотов или кастомный конвейер.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Переводит только содержимое Markdown. Не переписывает ссылки, не записывает метаданные и не добавляет дисклеймеры. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Переводит Markdown-ячейки и сохраняет не-Markdown ячейки. Не переписывает ссылки, не записывает метаданные и не добавляет дисклеймеры. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Синхронно. Извлекает и переводит текст изображения, затем возвращает отрисованное изображение. Не сохраняет метаданные переведённого изображения. |

`translate_markdown_content` и `translate_notebook_content` принимают необязательный `source_path` через свои опции. Путь передаётся как контекст переводчику; вызывающие стороны остаются ответственными за любое проектно-специфическое переписывание путей после перевода.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Тем же опциям можно передать словари:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

API перевода с поддержкой агента не вызывают Azure OpenAI или OpenAI из Co-op Translator. Они подготавливают фрагменты Markdown или блокнота для перевода хост-агентом, затем реконструируют итоговое содержимое из переведённых фрагментов.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Возвращает автономную задачу Markdown с фрагментами, подсказками и состоянием реконструкции. |
| `finish_markdown_agent_translation` | Реконструирует Markdown из задачи и фрагментов, переведённых хост-агентом. |
| `start_notebook_agent_translation` | Возвращает задачу блокнота с фрагментами Markdown-ячееек для перевода хост-агентом. |
| `finish_notebook_agent_translation` | Реконструирует JSON блокнота, сохраняя кодовые ячейки, выводы и метаданные. |

Этот рабочий процесс в основном предназначен для MCP-хостов. Если вам нужен промышленный перевод репозитория с тем, чтобы Co-op Translator управлял вызовами провайдеров, используйте `translate_markdown_content`, `translate_notebook_content` или `run_translation`.

## Path Rewriting APIs

API переписывания путей не выполняют перевод. Они обновляют ссылки и поля фронтмета после того, как вызывающие стороны знают исходный путь, переведённый целевой путь и структуру проекта.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Переписывает Markdown-ссылки и поддерживаемые поля фронтмета путей для переведённой цели. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Применяет переписывание Markdown-путей к каждой Markdown-ячейке и оставляет не-Markdown ячейки без изменений. |

Аргумент `policy` может быть словарём со следующими полями:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Целевой код языка, например `"ko"` или `"pt-BR"`. |
| `root_dir` | No | Корень исходного проекта. По умолчанию `"."`. |
| `translations_dir` | No | Каталог вывода текстовых переводов. По умолчанию `translations` под `root_dir`. |
| `translated_images_dir` | No | Каталог вывода переведённых изображений. По умолчанию `translated_images` под `root_dir`. |
| `translation_types` | No | Включённые типы перевода. По умолчанию Markdown, блокноты и изображения. |
| `lang_subdir` | No | Необязательный подкаталог в каждой папке языка. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Коды целевых языков, разделённые пробелом, например `"ko ja fr"`, или `"all"`. Алиасы кодов нормализуются до канонических значений BCP 47. |
| `root_dir` | `str` | `"."` | Корень проекта для одной цели перевода. Игнорируется, когда указаны `root_dirs` или `groups`. |
| `update` | `bool` | `False` | Удалять и воссоздавать существующие переводы для выбранных языков. |
| `images` | `bool` | `False` | Включать перевод изображений. Требует настройки Azure AI Vision. |
| `markdown` | `bool` | `False` | Включать перевод Markdown. |
| `notebook` | `bool` | `False` | Включать перевод Jupyter-блокнотов. |
| `debug` | `bool` | `False` | Включить отладочный лог. |
| `save_logs` | `bool` | `False` | Сохранять лог-файлы уровня DEBUG в корневой директории `logs/`. |
| `yes` | `bool` | `True` | Авто-подтверждение запросов для программного и CI-использования. |
| `add_disclaimer` | `bool` | `False` | Добавлять дисклеймеры машинного перевода в переведённые Markdown и блокноты. |
| `translations_dir` | `str \| None` | `None` | Пользовательский каталог вывода текстовых переводов. Относительные пути разрешаются относительно каждого корня. |
| `image_dir` | `str \| None` | `None` | Пользовательский каталог переведённых изображений. Относительные пути разрешаются относительно каждого корня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Несколько корней, которые разделяют одни и те же настройки вывода. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явные пары `(root_dir, translations_dir)`. Имеют приоритет над `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL репозитория, используемый при рендеринге таблицы языков в README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Термины глоссария для сохранения во время перевода. Дубликаты и пустые термины нормализуются. |
| `dry_run` | `bool` | `False` | Оценить объём перевода и просмотреть поведение миграции без записи файлов. |

## Review Parameters

`run_review` намеренно повторяет сигнатуру `run_translation`, где это возможно, чтобы автоматизация могла переключаться между рабочими процессами перевода и проверки с минимальными ветвлениями.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Папки целевых языков для проверки. Принимаются строки, разделённые пробелом, и итерируемые объекты. `"all"` проверяет все обнаруженные языки перевода. |
| `root_dir` | `str` | `"."` | Корень проекта для одной цели проверки. Игнорируется, когда указаны `root_dirs` или `groups`. |
| `markdown` | `bool` | `False` | Включать исходные файлы Markdown и MDX. |
| `notebook` | `bool` | `False` | Включать исходные файлы Jupyter-блокнотов. |
| `images` | `bool` | `False` | Зарезервировано для соответствия с опциями перевода. Ссылки на изображения проверяются из Markdown. |
| `translations_dir` | `str \| None` | `None` | Каталог вывода пользовательского перевода текста. Относительные пути разрешаются относительно каждого корня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Несколько корней, которые используют одни и те же параметры вывода. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явные пары `(root_dir, translations_dir)`. Имеют приоритет над `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-реф, используемый для ограничения проверки изменённых исходных файлов. |
| `output_format` | `str` | `"text"` | Формат вывода ревью. Поддерживаемые значения: `"text"` и `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Рассматривать предупреждения как ошибки, помимо обычных ошибок. |
| `debug` | `bool` | `False` | Включить отладочное логирование. |
| `save_logs` | `bool` | `False` | Сохранять файлы логов уровня DEBUG в корневом каталоге `logs/`. |

Если ни один из параметров `markdown`, `notebook` или `images` не задан, API проверяет Markdown, ноутбуки и ссылки на изображения там, где это применимо. Проверка не вызывает LLM-провайдер и не требует API-ключей.

## Требования к конфигурации

API перевода, использующие провайдеров, требуют настройки провайдера перед началом перевода:

- Для перевода Markdown и ноутбуков требуется LLM-провайдер. Настройте либо Azure OpenAI, либо OpenAI.
- Для перевода изображений требуется Azure AI Vision в дополнение к LLM-провайдеру.
- `run_translation` выполняет простые проверки соединения перед началом перевода проекта.
- API с помощью агентов `start_*_agent_translation` и `finish_*_agent_translation` не вызывают LLM-провайдеров Co-op Translator. Хост-приложение или MCP-агент переводит подготовленные фрагменты.
- Функции `rewrite_markdown_paths`, `rewrite_notebook_paths` и `run_review` детерминированы и не требуют учетных данных провайдера.

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

`run_review` детерминирован и не требует конфигурации Azure OpenAI, OpenAI или Azure AI Vision.

## Примечания к поведению

- API перевода контента отделяют сам перевод от переписывания путей проекта. Явно вызовите `rewrite_markdown_paths` или `rewrite_notebook_paths`, когда переведённому контенту нужно скорректировать проект-относительные ссылки для целевого расположения.
- API оркестрации проекта добавляют поведение проекта вокруг перевода контента, включая обнаружение файлов, запись, переписывание путей, метаданные, очистку и необязательные дисклеймеры.
- `run_translation` выводит прогресс и краткие оценки через Click, соответствуя опыту работы в CLI.
- `dry_run=True` вычисляет оценки, используя виртуальные обновления README, но не записывает README или файлы перевода.
- `groups` обрабатываются последовательно. Перед началом работы печатается единая агрегированная оценка.
- Когда выбран перевод изображений, отсутствие конфигурации Vision вызывает ошибку до начала перевода.
- Существующие папки языковых псевдонимов обнаруживаются и могут быть мигрированы в канонические имена папок языка в рамках запуска.
- `run_review` завершается с ошибкой при отсутствии переведённых файлов, отсутствии или устаревших метаданных перевода, неверном frontmatter или кодовых блоках (code fences) Markdown и недействительном JSON переведённого ноутбука.
- `run_review` по умолчанию сообщает об отсутствии локальных целей ссылок Markdown и изображений как предупреждения.

## Внутренний путь вызовов

API делегирует той же базовой реализации, что используется CLI:

Перевод:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` для перевода в памяти.
2. `co_op_translator.api.translation.rewrite_markdown_paths` или `rewrite_notebook_paths` для явной постобработки путей.
3. `co_op_translator.api.translation.run_translation` для полной оркестрации проекта.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Фокусированные миксины проектного перевода для Markdown, ноутбуков и изображений.
8. Переводчики Markdown, ноутбуков, текста и изображений в `co_op_translator.core`.

Проверка:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерминированные проверки в `co_op_translator.review.checks`

Следующие классы полезны для сопровождающих, но не экспортируются как стабильный API на уровне пакета.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координирует перевод на уровне проекта, управление каталогами, нормализацию метаданных по языкам и делегирование переводчикам Markdown, ноутбуков и изображений. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Выполняет асинхронную обработку файлов для Markdown, ноутбуков, изображений, обнаружения устаревших файлов и обновления метаданных перевода. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркестрирует чтение файлов Markdown, перевод содержимого, переписывание путей, метаданные, дисклеймеры и запись. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркестрирует чтение файлов ноутбуков, перевод Markdown-ячеек, переписывание путей, метаданные, дисклеймеры и запись. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркестрирует обнаружение исходных изображений, перевод изображений, пути вывода, метаданные и запись. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Находит пары переведённых Markdown, оценивает качество перевода и читает метаданные уверенности для процессов исправления с низкой уверенностью. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координирует детерминированные проверки обзора среди исходных файлов, целевых языков и настроенных корней перевода. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описывает исходный корень и каталог вывода перевода, проверяемый для этого корня. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Обнаруживает устаревшие папки-языковые псевдонимы и готовит планы миграции в канонические папки BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Загружает `.env` файлы и проверяет, настроены ли требуемые LLM и необязательные провайдеры Vision. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Автоопределяет Azure OpenAI или OpenAI, проверяет требуемые переменные окружения и выполняет проверки соединения с провайдером. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Обнаруживает конфигурацию Azure AI Vision и выполняет проверки соединения для перевода изображений. |