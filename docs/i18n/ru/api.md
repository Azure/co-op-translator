# Python API

Стабильный публичный Python API экспортируется из `co_op_translator.api`. Большинство интеграций используют один из этих рабочих процессов:

| Сценарий | Используйте это когда | Основные API |
| --- | --- | --- |
| Перевод отдельных файлов или документов | Ваше приложение читает исходный контент, вызывает Co-op Translator для перевода и решает, где сохранить результат. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Подготовка контента для перевода агентом хоста | Ваш MCP-хост или модель приложения будет переводить фрагменты, в то время как Co-op Translator выполняет разбиение на фрагменты и восстановление. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Перевести весь репозиторий | Вы хотите, чтобы Python API вел себя как CLI и осуществлял обнаружение, пути вывода, метаданные, очистку и запись файлов. | `run_translation` |

Большинство низкоуровневых модулей в `core`, `config`, `review` и `utils` — это детали реализации, используемые этими точками входа API.

Клиенты MCP используют тот же публичный API через [Сервер MCP](mcp.md). Используйте эту страницу при вызове Python напрямую, а руководство MCP — при предоставлении Co-op Translator агенту или редактору. Если вы выбираете между CLI, Python API и MCP, начните с [Выберите рабочий процесс](workflows.md).

## Первоначальный поток работы с API

Начните здесь, если вы вызываете Co-op Translator из кода на Python:

1. Настройте провайдера LLM, как описано в [Configuration](configuration.md), если вы не просто подготавливаете фрагменты Markdown или блокнотов для перевода агентом хоста.
2. Решите, отвечает ли ваше приложение за ввод/вывод файлов.
3. Используйте API контента, когда ваше приложение читает и записывает отдельные файлы.
4. Используйте `run_translation`, когда Co-op Translator должен обрабатывать репозиторий как CLI.
5. Используйте `run_review` после перевода, если вам нужны детерминированные проверки в автоматизации.

| Цель | API для начала |
| --- | --- |
| Перевести одну Markdown-строку или файл | `translate_markdown_content` |
| Перевести содержимое одного блокнота | `translate_notebook_content` |
| Перевести одно изображение | `translate_image_content` |
| Позволить агенту хоста переводить фрагменты Markdown или блокнота | `start_markdown_agent_translation` или `start_notebook_agent_translation` |
| Переписать переведённые ссылки после выбора пути вывода | `rewrite_markdown_paths` или `rewrite_notebook_paths` |
| Перевести весь репозиторий | `run_translation` |
| Проверить переведённый результат | `run_review` |

## Сценарий 1: Перевод отдельных файлов или документов

Используйте этот рабочий процесс, если у вас уже есть файл, буфер редактора, содержимое блокнота, запрос MCP или входные данные кастомного конвейера. Ваш код отвечает за ввод/вывод файлов:

1. Read the source content.
2. Call a content translation API.
3. При необходимости вызовите API переписывания путей, если переведенное содержимое будет записано в папку перевода проекта.
4. Сохраните результат или верните его из вашего приложения.

API перевода контента не выполняют обнаружение проекта, не записывают метаданные, не добавляют дисклеймеры и не переписывают ссылки автоматически.

### Файл Markdown

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

### Файл блокнота

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

`translate_notebook_content` переводит Markdown-ячейки и сохраняет ячейки, не являющиеся Markdown. Переписывание путей применяется только к Markdown-ячейкам.

### Файл изображения

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

`translate_image_content` читает исходное изображение и возвращает отрисованный `PIL.Image.Image`. Он не записывает метаданные переведённого изображения.

## Сценарий 2: Перевести весь репозиторий

Используйте этот рабочий процесс, когда вы хотите, чтобы Python API вел себя как CLI `translate`. `run_translation` обнаруживает поддерживаемые файлы, переводит выбранные типы контента, переписывает пути, записывает выходные файлы, обновляет метаданные и выполняет задачи обслуживания перевода, такие как очистка.

`run_translation` — предпочитаемая точка входа для оркестрации проекта. `translate_project` экспортируется как алиас для совместимости с тем же поведением.

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

Записывать структурированные события прогресса для интеграции:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Сохраните полезную нагрузку в таблице job-event или транслируйте её в интерфейс пользователя.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

События используют версионированную схему `co-op.translation.event.v1`. Интеграциям следует
опираться на стабильные поля, такие как `type` и `stage_key`, а не на отображаемый
консольный текст или `stage_label`.

Перевести несколько корней контента за один вызов:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Записывать переводы в явные группы вывода:

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

Используйте плейсхолдер для каждого языка, когда для каждого языка требуется вложенная подпапка:

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

Если ни `markdown`, ни `notebook`, ни `images` не заданы, API переводит все поддерживаемые типы: Markdown, блокноты и изображения.

### Сохранение принятых правок человеком с помощью поставщика состояния перевода

По умолчанию Co-op Translator сохраняет свое текущее поведение на уровне файлов: когда
исходный Markdown устарел, весь переведённый файл регенерируется. Размещённые
интеграции могут по желанию передать `TranslationStateProvider`, чтобы сохранить правки человека
в исходных блоках, которые не изменились.

Поставщик предоставляет последнюю принятую пару исходный/целевой и записывает каждую новую
кандидатуру. Принятие остается ответственностью интеграции — например,
после слияния pull request с переводом:

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

Для файлов Markdown с допустимым принятым базовым вариантом Co-op Translator выравнивает
верхнеуровневые Markdown-блоки. Неизменённые исходные блоки повторно используют текущие переведённые
блоки, включая правки, сделанные людьми; изменённые или добавленные исходные блоки отправляются
на перевод; удалённые исходные блоки удаляются. Если выравнивание неоднозначно,
структура целевого документа изменилась, перевод блока недействителен или базовый вариант
отсутствует, Co-op Translator безопасно откатывается к существующему полному
пути перевода.

Этот API хранит состояние перевода документа, а не междокументную память фраз или
сегментного переводческого памяти. В настоящее время это применяется к переводам Markdown-проектов.
Поведение для блокнотов и изображений не изменилось. Передача `update=True`
по-прежнему запрашивает полную регенерацию.

Если один или несколько файлов не могут быть переведены, `run_translation` возбуждает
`RuntimeError` после завершения рабочего процесса проекта, вместо того чтобы сообщить
об успешном запуске с отсутствующим выводом. Интеграции должны рассматривать это как сбой
задачи и сохранить предыдущее принятое состояние перевода.

## Проверка переведённого результата

`run_review` выполняет детерминированные проверки перевода без учётных данных LLM или Vision.

!!! note "Бета"
    `run_review` — бета-версия детерминированного API для проверки. Он не вызывает поставщиков моделей и не записывает файлы, однако схемы проверок и проблем могут изменяться.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

После перевода только README используйте ту же область для проверки:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` проверяет только `README.md` в каждом настроенном корневом каталоге исходников,
включая пользовательские `groups` и выходные директории. Другие документы и вложенные
README-файлы исключаются. Отсутствие исходного README вызывает `ValueError`; неудачные
проверки перевода вызывают `RuntimeError`.

Проверять только файлы, изменённые по сравнению с базовой ревизией (base ref), и выводить результат в формате GitHub:

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

## Примеры API для копирования и вставки

Перевод Markdown-контента без записи в файлы:

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

Перевод и переписывание Markdown-ссылок:

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

Перевести репозиторий с помощью Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Перевод нескольких корневых каталогов:

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

Сохранение терминов глоссария:

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

## Публичные точки входа

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

## API перевода содержимого

API перевода содержимого предназначены для интеграций, в которых содержимое уже находится в памяти, таких как расширение редактора, инструмент MCP, процессор ноутбуков или пользовательский конвейер.

| Function | Вход | Выход | Файловый ввод/вывод | Примечания |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Нет | Асинхронно. Переводит только содержимое Markdown. Не переписывает ссылки, не записывает метаданные и не добавляет дисклеймеры. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Нет | Асинхронно. Переводит Markdown-ячейки и сохраняет ячейки, не являющиеся Markdown. Не переписывает ссылки, не записывает метаданные и не добавляет дисклеймеры. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Читает только исходное изображение | Синхронно. Извлекает и переводит текст изображения, затем возвращает отрендеренное изображение. Не сохраняет метаданные переведённого изображения. |

`translate_markdown_content` и `translate_notebook_content` принимают необязательный параметр `source_path` через свои опции. Путь передаётся переводчику как контекст; вызывающая сторона остаётся ответственной за любое проектно-специфическое переписывание путей после перевода.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Те же опции можно передать в виде словарей:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API перевода с участием агента

API с участием агента не вызывают настроенного LLM-провайдера в Co-op Translator. Они подготавливают фрагменты Markdown или ноутбука для перевода агентом-хостом, затем восстанавливают итоговый контент из переведённых фрагментов.

| Function | Назначение |
| --- | --- |
| `start_markdown_agent_translation` | Возвращает автономную задачу Markdown с фрагментами, подсказками и состоянием реконструкции. |
| `finish_markdown_agent_translation` | Восстанавливает Markdown из задачи и переведённых хост-агентом фрагментов. |
| `start_notebook_agent_translation` | Возвращает задачу для ноутбука с фрагментами Markdown-ячейок для перевода хост-агентом. |
| `finish_notebook_agent_translation` | Восстанавливает JSON ноутбука, сохраняя ячейки кода, выводы и метаданные. |

Этот рабочий процесс в основном предназначен для хостов MCP. Если вам нужен продакшн-перевод репозитория с тем, чтобы Co-op Translator управлял вызовами провайдеров, используйте `translate_markdown_content`, `translate_notebook_content` или `run_translation`.

## API переписывания путей

API переписывания путей не выполняют перевода. Они обновляют ссылки и пути в frontmatter после того как вызывающая сторона знает исходный путь, переведённый путь назначения и структуру проекта.

| Function | Область | Примечания |
| --- | --- | --- |
| `rewrite_markdown_paths` | тело Markdown и frontmatter | Переписывает Markdown-ссылки и поддерживаемые поля путей в frontmatter для переведённой цели. |
| `rewrite_notebook_paths` | Markdown-ячейки в JSON ноутбука | Применяет переписывание путей Markdown к каждой Markdown-ячейке и оставляет не-Markdown ячейки без изменений. |

Аргумент `policy` может быть словарём со следующими полями:

| Field | Обязательно | Назначение |
| --- | --- | --- |
| `language_code` | Да | Код целевого языка, например `"ko"` или `"pt-BR"`. |
| `root_dir` | Нет | Корень исходного проекта. По умолчанию `"."`. |
| `translations_dir` | Нет | Каталог вывода переводов текста. По умолчанию `translations` в `root_dir`. |
| `translated_images_dir` | Нет | Каталог вывода переведённых изображений. По умолчанию `translated_images` в `root_dir`. |
| `translation_types` | Нет | Включённые типы перевода. По умолчанию: Markdown, ноутбуки и изображения. |
| `lang_subdir` | Нет | Необязательная подпапка в каждой языковой папке. |

## Параметры перевода проекта

| Parameter | Тип | По умолчанию | Назначение |
| --- | --- | --- | --- |
| `language_codes` | `str` | Обязательный | Коды целевых языков, разделённые пробелом, например `"ko ja fr"`, или `"all"`. Псевдонимы нормализуются до канонических значений BCP 47. |
| `root_dir` | `str` | `"."` | Корень проекта для одной цели перевода. Игнорируется, если заданы `root_dirs` или `groups`. |
| `update` | `bool` | `False` | Удаляет и воссоздаёт существующие переводы для выбранных языков. |
| `images` | `bool` | `False` | Включить перевод изображений. Требует конфигурации Azure AI Vision. |
| `markdown` | `bool` | `False` | Включить перевод Markdown. |
| `notebook` | `bool` | `False` | Включить перевод Jupyter notebook. |
| `debug` | `bool` | `False` | Включить отладочное логирование. |
| `save_logs` | `bool` | `False` | Сохранять лог-файлы уровня DEBUG в корневом каталоге `logs/`. |
| `yes` | `bool` | `True` | Автоматически подтверждать запросы для программного использования и CI. |
| `add_disclaimer` | `bool` | `False` | Добавлять уведомления о машинном переводе в переведённые Markdown и блокноты. |
| `translations_dir` | `str \| None` | `None` | Пользовательский каталог для вывода переведённого текста. Относительные пути разрешаются относительно каждого корня. |
| `image_dir` | `str \| None` | `None` | Пользовательский каталог для вывода переведённых изображений. Относительные пути разрешаются относительно каждого корня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Несколько корневых каталогов, которые используют одни и те же параметры вывода. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явные `(root_dir, translations_dir)` пары. Имеют приоритет над `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL репозитория, используемый при формировании подсказок в таблице языков README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Термины глоссария, которые нужно сохранять при переводе. Дубли и пустые термины нормализуются. |
| `dry_run` | `bool` | `False` | Оценивать объём перевода и просматривать поведение миграции без записи файлов. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Необязательный адаптер сохранения принятых эталонов и кандидатов для инкрементных обновлений Markdown. Пропуск сохраняет существующее поведение полной перезаписи файлов. |

## Параметры проверки

`run_review` намеренно во многом повторяет сигнатуру `run_translation`, чтобы автоматизация могла переключаться между рабочими процессами перевода и проверки с минимальным ответвлением.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Целевые языковые папки для проверки. Принимаются строки через пробел и итерируемые объекты. `"all"` проверяет все обнаруженные языки перевода. |
| `root_dir` | `str` | `"."` | Корень проекта для одной цели проверки. Игнорируется, когда заданы `root_dirs` или `groups`. |
| `markdown` | `bool` | `False` | Включать исходные файлы Markdown и MDX. |
| `notebook` | `bool` | `False` | Включать исходные Jupyter-блокноты. |
| `images` | `bool` | `False` | Зарезервировано для паритета с опциями перевода. Ссылки на изображения проверяются в Markdown. |
| `translations_dir` | `str \| None` | `None` | Пользовательский каталог для вывода переведённого текста. Относительные пути разрешаются относительно каждого корня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Несколько корневых каталогов, которые используют одни и те же параметры вывода. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явные `(root_dir, translations_dir)` пары. Имеют приоритет над `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-реф, используемый для ограничения проверки изменённых исходных файлов. |
| `readme_only` | `bool` | `False` | Проверять только `README.md` в каждом исходном корне. Отсутствие исходного README вызывает `ValueError`. |
| `output_format` | `str` | `"text"` | Формат вывода проверки. Поддерживаемые значения: `"text"` и `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Рассматривать предупреждения как сбои помимо ошибок. |
| `debug` | `bool` | `False` | Включить логирование отладки. |
| `save_logs` | `bool` | `False` | Сохранять DEBUG-level лог-файлы в каталоге `logs/` в корне. |

Если ни `markdown`, ни `notebook`, ни `images` не заданы, API проверяет Markdown, блокноты и ссылки на изображения, где это применимо. Проверка не вызывает провайдера LLM и не требует API-ключей.

## Требования к конфигурации

Для API перевода с поддержкой провайдеров требуется настройка провайдера перед переводом:

- Перевод Markdown и блокнотов требует провайдера LLM. Настройте Azure OpenAI, OpenAI или Anthropic.
- Для перевода изображений требуется Azure AI Vision в дополнение к LLM-провайдеру.
- `run_translation` выполняет лёгкие проверки соединения перед началом перевода проекта.
- API с поддержкой агентов `start_*_agent_translation` и `finish_*_agent_translation` не вызывают Co-op Translator LLM провайдеров. Хост-приложение или MCP-агент переводит подготовленные фрагменты.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` и `run_review` являются детерминированными и не требуют учётных данных провайдера.

Требуемые переменные Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Требуемые переменные OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Требуемые переменные Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` и `ANTHROPIC_MAX_TOKENS` необязательны. Microsoft Agent Framework является клиентом модели по умолчанию для всех провайдеров, начиная с Co-op Translator 0.22.0. Semantic Kernel всё ещё можно временно выбрать с помощью `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, но это вызовет предупреждение об устаревании; см. [конфигурация](configuration.md#model-client-backend) для плана поэтапного удаления.

Требуемые переменные Azure AI Vision для перевода изображений:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` детерминированен и не требует конфигурации LLM или Azure AI Vision.

## Примечания к поведению

- API перевода содержимого разделяют сам перевод и переписывание путей проекта. Вызывайте `rewrite_markdown_paths` или `rewrite_notebook_paths` явно, когда переведённому содержимому нужно скорректировать ссылки, относительные к проекту, для целевого расположения.
- API оркестрации проекта добавляют поведение проекта вокруг перевода содержимого, включая обнаружение файлов, запись файлов, переписывание путей, метаданные, очистку и необязательные дисклеймеры.
- `run_translation` выводит сводки прогресса и оценок через того же репортера на основе Rich, что используется CLI. Неинтерактивный вывод переходит в обычный текст.
- `dry_run=True` вычисляет оценки, используя виртуальные обновления README, но не записывает README или файлы перевода.
- `groups` обрабатываются последовательно. Перед началом работы печатается единая агрегированная оценка.
- Когда выбран перевод изображений, отсутствие конфигурации Vision вызывает ошибку до начала перевода.
- Существующие папки языков на основе псевдонимов обнаруживаются и могут быть мигрированы в канонические имена папок языков в процессе выполнения.
- `run_review` не проходит при отсутствии переведённых файлов, отсутствии или устаревших метаданных перевода, некорректном Markdown frontmatter/блоках кода и недопустимом JSON переведённого блокнота.
- `run_review` по умолчанию сообщает об отсутствующих локальных целях для Markdown и ссылок на изображения как о предупреждениях.

## Внутренний путь вызовов

API делегирует той же основной реализации, что и CLI:

Перевод:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Специализированные миксины перевода проекта для Markdown, блокнотов и изображений.
8. Переводчики Markdown, блокнотов, текста и изображений в `co_op_translator.core`.

Проверка:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерминированные проверки в `co_op_translator.review.checks`

Следующие классы полезны для сопровождения, но не экспортируются как стабильный API на уровне пакета.

| Класс | Модуль | Назначение |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координирует перевод на уровне проекта, управление каталогами, нормализацию метаданных по каждому языку и делегирование переводчикам Markdown, блокнотов и изображений. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Выполняет асинхронную обработку файлов для Markdown, блокнотов, изображений, обнаружение устаревших данных и обновления метаданных перевода. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркеструет чтение Markdown-файлов, перевод содержимого, переписывание путей, метаданные, дисклеймеры и запись файлов. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркеструет чтение файлов блокнотов, перевод Markdown-ячеек, переписывание путей, метаданные, дисклеймеры и запись. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркеструет обнаружение исходных изображений, перевод изображений, выходные пути, метаданные и запись. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Находит пары переведённых Markdown, оценивает качество перевода и читает метаданные уверенности для рабочих процессов исправления низкой уверенности. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координирует детерминированные проверки по исходным файлам, целевым языкам и настроенным корням перевода. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описывает исходный корень и каталог вывода перевода, проверяемый для этого корня. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Обнаруживает устаревшие папки языков-псевдонимов и подготавливает планы миграции в канонические папки по BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Загружает `.env` файлы и проверяет, настроены ли требуемые LLM и необязательные провайдеры Vision. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Автоматически обнаруживает Azure OpenAI, OpenAI или Anthropic, проверяет требуемые переменные окружения и выполняет проверки доступности провайдера. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Обнаруживает конфигурацию Azure AI Vision и выполняет проверки соединения для перевода изображений. |