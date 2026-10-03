# Python API

Стабилният публичен Python API се експортира от `co_op_translator.api`. Повечето интеграции използват един от тези работни потоци:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Вашето приложение чете оригиналното съдържание, извиква Co-op Translator за превод и решава къде да запише резултата. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Подгответе съдържанието за превод от хост-агент | Вашият MCP хост или модел на приложението ще превежда сегментите, докато Co-op Translator се грижи за разбиването на части и реконструкцията. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Искате Python API да се държи като CLI и да се грижи за откриване, пътища на изход, метаданни, почистване и запис. | `run_translation` |

Повечето по-ниско ниво модули под `core`, `config`, `review`, и `utils` са детайли на имплементацията, използвани от тези входни точки на API.

Клиентите на MCP използват един и същ публичен API чрез [MCP сървър](mcp.md). Използвайте тази страница, когато извиквате Python директно, и ръководството за MCP, когато излагате Co-op Translator на агент или редактор. Ако решавате между CLI, Python API и MCP, започнете с [Изберете работния си поток](workflows.md).

## Първоначален API поток

Започнете тук, ако извиквате Co-op Translator от Python код:

1. Конфигурирайте доставчик на LLM, както е описано в [Configuration](configuration.md), освен ако не подготвяте само Markdown или фрагменти от notebook за превод от хост-агент.
2. Решете дали вашето приложение отговаря за файловия I/O.
3. Използвайте API-та за съдържание, когато вашето приложение чете и записва отделни файлове.
4. Използвайте `run_translation`, когато Co-op Translator трябва да обработи репозитория по същия начин като CLI.
5. Използвайте `run_review` след превода, ако имате нужда от детерминирани проверки в автоматизацията.

| Goal | API to start with |
| --- | --- |
| Преведете един Markdown низ или файл | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Позволете на хост агент да превежда фрагменти от Markdown или тетрадки | `start_markdown_agent_translation` или `start_notebook_agent_translation` |
| Презапишете преведените връзки след избор на изходен път | `rewrite_markdown_paths` или `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Сценарий 1: Превод на отделни файлове или документи

Използвайте този работен поток, когато вече имате файл, редакторски буфер, notebook payload, MCP заявка или вход за потребителски pipeline. Вашият код отговаря за четенето и записването на файлове:

1. Прочетете източниковото съдържание.
2. Извикайте API за превод на съдържание.
3. По желание извикайте API за пренаписване на пътища, ако преведеното съдържание ще бъде записано в папка за преводи на проекта.
4. Запазете или върнете резултата от вашето приложение.

API-тата за превод на съдържание не изпълняват откриване на проект, не записват метаданни, не добавят откази от отговорност и не пренаписват връзки автоматично.

### Markdown файл

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

Ако преведеният Markdown няма да бъде в структура на проект на Co-op Translator, пропуснете `rewrite_markdown_paths` и запазете преведения стринг директно.

### Notebook файл

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

`translate_notebook_content` превежда Markdown клетки и запазва немаркетиращите се (non-Markdown) клетки. Пренаписването на пътища се прилага само за Markdown клетки.

### Файл с изображение

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

`translate_image_content` чете изходното изображение и връща рендирано `PIL.Image.Image`. То не записва преведени метаданни за изображението.

## Сценарий 2: Превод на цялото хранилище

Използвайте този работен поток, когато искате Python API да се държи като `translate` CLI. `run_translation` открива поддържани файлове, превежда избрани типове съдържание, пренаписва пътища, записва изходни файлове, актуализира метаданни и изпълнява задачи за поддръжка на превода като почистване.

`run_translation` е предпочитаната входна точка за оркестрация на проекта. `translate_project` се експортира като алиас за съвместимост със същото поведение.

Преведете Markdown файловете в текущия репозитория на корейски и японски:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Превеждайте само тетрадки от конкретен корен на проекта:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Прегледайте обема на превода без записване на файлове:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Записвайте структурирани събития за напредъка на интеграцията:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Запазете payload в таблицата си с job-събития или го стриймвайте към вашия потребителски интерфейс.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

Преведете множество корени на съдържание в едно извикване:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Записвайте преводите в явни изходни групи:

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

Използвайте плейсхолдер за всеки език, когато всеки език трябва да съдържа вложена поддиректория:

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

Ако нито една от `markdown`, `notebook` или `images` не е зададена, API-то превежда всички поддържани типове: Markdown, notebooks и изображения.

### Запазване на приетите човешки редакции с доставчик на състоянието на превода

По подразбиране Co-op Translator запазва съществуващото си поведение на ниво файл: когато
източникът на Markdown е остарял, целият преведен файл се регенерира. Хостваните
интеграции могат по избор да предадат `TranslationStateProvider`, за да запазят човешки
редакции в изходните блокове, които не са се променили.

Доставчикът предоставя последната приета двойка източник/цел и записва всеки нов
кандидат. Приемането остава отговорност на интеграцията — например,
след като pull request за превод бъде слят:

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

За Markdown файлове с валиден приет базов вариант, Co-op Translator подравнява
Markdown блоковете от най-горно ниво. Непроменените източникови блокове използват отново текущите преведени
блокове, включително редакции, направени от хора; променените или добавени източникови блокове се изпращат
за превод; изтритите източникови блокове се премахват. Ако подравняването е нееднозначно,
структурата на целта се е променила, преводът на блок е невалиден, или няма
наличен базов вариант, Co-op Translator безопасно се връща към съществуващия пълен
път за превод на файла.

Този API съхранява състоянието на превода на документа, а не
памет за превод на фрази или сегменти между документи. В момента се прилага за преводи на Markdown проекти.
Поведението за notebook и изображения остава непроменено. Предаването на `update=True`
все още изисква пълна регенерация.

Ако един или повече файлове не могат да бъдат преведени, `run_translation` хвърля
`RuntimeError` след като работният процес по проекта приключи, вместо да отчита
успешно изпълнение с липсващ резултат. Интеграциите трябва да третират това като неуспешна
задача и да запазят предишното прието състояние на превода.

## Преглед на преведения резултат

`run_review` изпълнява детерминирани проверки на превода без LLM или Vision идентификационни данни.

!!! note "Бета"
    `run_review` е бета детерминиран API за преглед. Той не извиква доставчици на модели и не записва файлове, но проверките и схемите за проблеми могат да се променят.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

След превод само на README, използвайте същия обхват за преглед:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` преглежда само `README.md` под всеки конфигуриран изходен корен,
включително потребителските `groups` и директориите за извеждане. Други документи и вложени
README файлове са изключени. Липсващият изходен README предизвиква `ValueError`; неуспешните
проверките за превод предизвикват `RuntimeError`.

Преглеждайте само файлове, променени спрямо базов реф, и отпечатвайте изход във формат GitHub:

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

## Примери за копиране и поставяне на API

Превеждайте Markdown съдържание без записване във файлове:

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

Превеждайте и пренаписвайте Markdown връзки:

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

Преведете хранилище от Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Превеждайте няколко корена:

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

Запазване на термините от глосаря:

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

## Публични входни точки

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

## API-та за превод на съдържание

API-тата за превод на съдържание са предназначени за интеграции, които вече имат съдържание в паметта, като разширение за редактор, MCP инструмент, обработчик на тетрадки или потребителски конвейер.

| Функция | Вход | Изход | Файлови I/O | Бележки |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Не | Асинхронно. Превежда само Markdown съдържание. Не пренаписва връзки, не записва метаданни и не добавя откази от отговорност. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Не | Асинхронно. Превежда Markdown клетки и запазва не-Markdown клетките. Не пренаписва връзки, не записва метаданни и не добавя откази от отговорност. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Синхронно. Извлича и превежда текста от изображението, след което връща рендирано изображение. Не записва метаданни за преведеното изображение. |

`translate_markdown_content` и `translate_notebook_content` приемат опционален `source_path` чрез техните опции. Пътят се предава като контекст на преводача; повикващите остават отговорни за всяко специфично за проекта пренаписване на пътища след превода.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Същите опции могат да бъдат подадени като речници:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API-та за превод с помощта на агент

API-тата с помощта на агент не извикват конфигурирания LLM доставчик от Co-op Translator. Те подготвят парчета Markdown или тетрадка за превод от хост агент, след което реконструират финалното съдържание от преведените парчета.

| Функция | Цел |
| --- | --- |
| `start_markdown_agent_translation` | Връща самостоятелна Markdown задача с фрагменти, подсказки и състояние за реконструкция. |
| `finish_markdown_agent_translation` | Възстановява Markdown от задача и фрагменти, преведени от хост-агент. |
| `start_notebook_agent_translation` | Връща notebook задача с фрагменти от Markdown клетки за превод от хост-агент. |
| `finish_notebook_agent_translation` | Възстановява notebook JSON, като запазва кодовите клетки, изходите и метаданните. |

Този работен поток е предимно предназначен за MCP хостове. Ако се нуждаете от превод на продукционно репозитори, при който Co-op Translator управлява повикванията към доставчиците, използвайте `translate_markdown_content`, `translate_notebook_content`, или `run_translation`.

## API-та за пренаписване на пътища

API-тата за пренаписване на пътища не извършват превод. Те актуализират връзки и пътища във frontmatter след като повикващите знаят изходния път, преведения целеви път и структурата на проекта.

| Функция | Обхват | Бележки |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Пренаписва Markdown връзки и поддържаните полета с frontmatter пътища за преведения целеви ресурс. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Прилaга пренаписване на Markdown пътища към всяка Markdown клетка и оставя не-Markdown клетките непроменени. |

Аргументът `policy` може да бъде речник със следните полета:

| Поле | Задължително | Цел |
| --- | --- | --- |
| `language_code` | Yes | Код на целевия език, например `"ko"` или `"pt-BR"`. |
| `root_dir` | No | Изходен корен на проекта. По подразбиране `"."`. |
| `translations_dir` | No | Директория за извеждане на текстовия превод. По подразбиране `translations` под `root_dir`. |
| `translated_images_dir` | No | Директория за извеждане на преведените изображения. По подразбиране `translated_images` под `root_dir`. |
| `translation_types` | No | Разрешени типове превод. По подразбиране Markdown, тетрадки и изображения. |
| `lang_subdir` | No | Опционална поддиректория под всяка папка за език. |

## Параметри за превод на проекта

| Параметър | Тип | По подразбиране | Цел |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Целеви кодове на езици, разделени с интервал, като `"ko ja fr"`, или `"all"`. Псевдонимните кодове се нормализират до канонични BCP 47 стойности. |
| `root_dir` | `str` | `"."` | Корен на проекта за една цел на превод. Игнорира се когато са подадени `root_dirs` или `groups`. |
| `update` | `bool` | `False` | Изтрива и пресъздава съществуващите преводи за избраните езици. |
| `images` | `bool` | `False` | Включва превод на изображения. Изисква конфигурация на Azure AI Vision. |
| `markdown` | `bool` | `False` | Включва превод на Markdown. |
| `notebook` | `bool` | `False` | Включва превод на Jupyter notebook. |
| `debug` | `bool` | `False` | Активира регистриране за отстраняване на грешки. |
| `save_logs` | `bool` | `False` | Запазва лог файлове на ниво DEBUG в кореновата директория `logs/`. |
| `yes` | `bool` | `True` | Автоматично потвърждава подкани за програмна употреба и CI. |
| `add_disclaimer` | `bool` | `False` | Добавя откази от отговорност за машинен превод към преведените Markdown файлове и Jupyter бележници. |
| `translations_dir` | `str \| None` | `None` | Персонализирана директория за изход на текстов превод. Относителните пътища се разрешават спрямо всяка коренова директория. |
| `image_dir` | `str \| None` | `None` | Персонализирана директория за изход на преведени изображения. Относителните пътища се разрешават спрямо всяка коренова директория. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Множество коренови директории, които споделят едни и същи настройки за изход. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явни двойки `(root_dir, translations_dir)`. Имат предимство пред `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL на хранилището, използван при генериране на указанията в таблицата за езици в README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Термини от глосар, които да се запазят по време на превод. Дубликатите и празните термини се нормализират. |
| `dry_run` | `bool` | `False` | Оценява обема на превода и предварително показва поведението при миграция, без да записва файлове. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Незадължителен адаптер за съхранение на приетия базов вариант и кандидатите за инкрементални актуализации на Markdown. Пропускането му запазва съществуващото поведение за пълни файлове. |

## Параметри за преглед

`run_review` умишлено отразява подписа на `run_translation` където е възможно, така че автоматизацията да може да превключва между работни потоци за превод и преглед с минимални разклонения.

| Параметър | Тип | По подразбиране | Цел |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Целеви папки с езици за преглед. Приемат се низове, разделени с интервал, и итерируеми. `"all"` преглежда всички открити езици за превод. |
| `root_dir` | `str` | `"."` | Корен на проекта за една цел за преглед. Игнорира се когато са подадени `root_dirs` или `groups`. |
| `markdown` | `bool` | `False` | Включва Markdown и MDX изходни файлове. |
| `notebook` | `bool` | `False` | Включва Jupyter notebook изходни файлове. |
| `images` | `bool` | `False` | Запазено за съответствие с опциите за превод. Препратките към изображения се проверяват от Markdown. |
| `translations_dir` | `str \| None` | `None` | Персонализирана директория за изход на текстов превод. Относителните пътища се разрешават спрямо всяка коренова директория. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Множество коренови директории, които споделят едни и същи настройки за изход. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явни двойки `(root_dir, translations_dir)`. Имат предимство пред `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git референция, използвана за ограничаване на прегледа до променени изходни файлове. |
| `readme_only` | `bool` | `False` | Преглежда само `README.md` в рамките на всеки корен на източник. Ако липсва източниковият README, се вдига `ValueError`. |
| `output_format` | `str` | `"text"` | Формат на изхода за преглед. Поддържаните стойности са `"text"` и `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Счита предупрежденията за неуспехи, в допълнение към грешките. |
| `debug` | `bool` | `False` | Активира логване за отстраняване на грешки. |
| `save_logs` | `bool` | `False` | Записва лог файлове на ниво DEBUG под кореновата директория `logs/`. |

Ако нито `markdown`, нито `notebook`, нито `images` са зададени, API-то преглежда Markdown, notebooks и препратките към изображения, където е приложимо. Прегледът не извиква доставчик на LLM и не изисква API ключове.

## Изисквания за конфигурация

Преводните API-та, зависещи от доставчик, изискват конфигурация на доставчика преди превод:

- Преводът на Markdown и notebooks изисква доставчик на LLM. Конфигурирайте Azure OpenAI, OpenAI или Anthropic.
- Преводът на изображения изисква Azure AI Vision в допълнение към доставчика на LLM.
- `run_translation` изпълнява леки проверки на свързаността преди започване на превода на проекта.
- API-тата с помощ от агенти `start_*_agent_translation` и `finish_*_agent_translation` не извикват LLM доставчиците на Co-op Translator. Хост приложението или MCP агентът извършва превода на подготвените парчета.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` и `run_review` са детерминистични и не изискват идентификационни данни на доставчика.

Задължителни променливи за Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Задължителни променливи за OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Задължителни променливи за Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` и `ANTHROPIC_MAX_TOKENS` са незадължителни. Microsoft Agent Framework е подразбиращият се клиент за модели за всички доставчици, започвайки от Co-op Translator 0.22.0. Semantic Kernel все още може да бъде избран временно с `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, но това генерира предупреждение за прекратяване; вижте [configuration](configuration.md#model-client-backend) за плана за поетапно премахване.

Задължителни променливи за Azure AI Vision за превод на изображения:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Изпълнението на `run_review` е детерминистично и не изисква конфигурация на LLM или Azure AI Vision.

## Бележки относно поведението

- API-тата за превод на съдържание държат превода отделен от презаписването на пътищата на проекта. Извикайте явно `rewrite_markdown_paths` или `rewrite_notebook_paths`, когато преведеното съдържание изисква коригиране на проектно-относителни връзки за целево местоположение.
- API-тата за оркестрация на проекти добавят поведение на проекта около превода на съдържанието, включително откриване на файлове, запис, презаписване на пътища, метаданни, почистване и опционални откази от отговорност.
- `run_translation` отпечатва резюмета за напредъка и оценките чрез същия докладчик, базиран на Rich, използван от CLI. Неинтерактивният изход се връща към обикновен текст.
- `dry_run=True` изчислява оценки, използвайки виртуални актуализации на README, но не записва README или файловете с преводи.
- `groups` се обработват последователно. Една агрегирана оценка се отпечатва преди започване на работата.
- Когато е избран превод на изображения, липсващата Vision конфигурация вдига грешка преди започване на превода.
- Съществуващите папки за езици, базирани на псевдоними, се откриват и могат да бъдат мигрирани към канонични имена на папки за езици като част от изпълнението.
- `run_review` проваля при липсващи преведени файлове, липсващи или остарели метаданни за превод, неправилно оформен Markdown frontmatter или code fences и невалиден преведен notebook JSON.
- `run_review` съобщава липсващите локални Markdown и целеви връзки към изображения като предупреждения по подразбиране.

## Вътрешен път на извикване

API-то делегира на същата основна имплементация, използвана от CLI-то:

Превод:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Фокусирани миксини за превод в проекта за Markdown, notebooks и изображения.
8. Преводачи за Markdown, notebooks, текст и изображения под `co_op_translator.core`.

Преглед:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерминистични проверки под `co_op_translator.review.checks`

Следните класове са полезни за поддръжниците, но не са експортирани като стабилно API на ниво пакет.

| Клас | Модул | Отговорност |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координира превода на проектно ниво, управлението на директории, нормализацията на метаданните за всеки език и делегирането към преводачи за Markdown, notebooks и изображения. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Изпълнява асинхронната обработка на файлове за Markdown, notebooks, изображения, откриване на остарели елементи и обновяване на метаданни за превод. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркестрира четенията на Markdown файлове, превода на съдържанието, презаписването на пътища, метаданните, отказите от отговорност и записите. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркестрира четенията на notebook файлове, превода на Markdown клетки, презаписването на пътища, метаданните, отказите от отговорност и записите. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркестрира откриването на изходни изображения, превода на изображения, изходните пътища, метаданните и записите. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Намира двойки преведени Markdown файлове, оценява качеството на превода и чете метаданни за увереност за работни потоци за поправка при ниска увереност. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координира детерминистични проверки за преглед върху изходните файлове, целевите езици и конфигурираните корени за превод. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описва източников корен и директорията за изходни преводи, преглеждани за този корен. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Открива наследствени папки за езици с псевдоними и подготвя планове за миграция към канонични BCP 47 папки. |
| `Config` | `co_op_translator.config.base_config` | Зарежда `.env` файлове и проверява дали задължителните LLM и опционалните Vision доставчици са конфигурирани. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Автоматично открива Azure OpenAI, OpenAI или Anthropic, валидира задължителните променливи на средата и изпълнява проверки на свързаността с доставчиците. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Открива конфигурация на Azure AI Vision и изпълнява проверки на свързаността за превод на изображения. |