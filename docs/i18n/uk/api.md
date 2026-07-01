# Python API

Стабільний публічний Python API експортується з `co_op_translator.api`. Більшість інтеграцій використовують один із цих сценаріїв:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Ваша програма читає вихідний вміст, викликає Co-op Translator для перекладу і вирішує, куди зберегти результат. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Ваш MCP-хост або модель програми перекладатиме фрагменти, тоді як Co-op Translator обробляє розбиття на фрагменти та реконструкцію. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Коли ви хочете, щоб Python API поводився як CLI і керував виявленням файлів, шляхами виводу, метаданими, очищенням та записом. | `run_translation` |

Більшість модулів нижчого рівня під `core`, `config`, `review` і `utils` — це деталі реалізації, які використовуються цими точками входу API.

Клієнти MCP використовують той самий публічний API через [MCP Server](mcp.md). Користуйтеся цією сторінкою при безпосередньому виклику Python, а керівництвом MCP — коли ви надаєте доступ Co-op Translator агенту або редактору. Якщо ви обираєте між CLI, Python API та MCP, почніть зі [Choose Your Workflow](workflows.md).

## Початковий потік роботи з API

Почніть тут, якщо ви викликаєте Co-op Translator з коду Python:

1. Налаштуйте постачальника LLM, як описано в [Configuration](configuration.md), якщо ви не лише готуєте фрагменти Markdown або ноутбука для перекладу хост-агентом.
2. Визначте, чи ваша програма відповідає за введення/виведення файлів.
3. Використовуйте API для вмісту, коли ваша програма читає і записує окремі файли.
4. Використовуйте `run_translation`, коли Co-op Translator повинен обробляти репозиторій так само, як CLI.
5. Використовуйте `run_review` після перекладу, якщо вам потрібні детерміновані перевірки в автоматизації.

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

Використовуйте цей робочий процес, коли у вас вже є файл, буфер редактора, вміст ноутбука, запит MCP або власний вхідний потік. Ваш код відповідає за введення/виведення файлів:

1. Прочитайте вихідний вміст.
2. Викличте API перекладу вмісту.
3. За потреби викличте API переписування шляхів, якщо перекладений вміст буде записано в папку перекладу проекту.
4. Збережіть або поверніть результат від вашої програми.

API перекладу вмісту не виконують виявлення проекту, не записують метадані, не додають дисклеймери і не переписують посилання автоматично.

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

Якщо перекладений Markdown не буде розміщений у структурі проекту Co-op Translator, пропустіть `rewrite_markdown_paths` і збережіть перекладений рядок безпосередньо.

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

`translate_notebook_content` перекладає Markdown-клітинки і зберігає немаркдаунні клітинки. Переписування шляхів застосовується лише до Markdown-клітинок.

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

`translate_image_content` читає вихідне зображення і повертає відрендерений `PIL.Image.Image`. Він не записує метадані перекладеного зображення.

## Scenario 2: Translate an Entire Repository

Використовуйте цей робочий процес, коли ви хочете, щоб Python API поводився як `translate` CLI. `run_translation` виявляє підтримувані файли, перекладає вибрані типи вмісту, переписує шляхи, записує вихідні файли, оновлює метадані та виконує завдання супроводу перекладу, такі як очищення.

`run_translation` — це рекомендована точка входу для оркестрації проекту. `translate_project` експортується як сумісний псевдонім з тим самим поведінкою.

Перекладіть файли Markdown у поточному репозиторії на корейську та японську:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Перекладіть лише ноутбуки з певного кореневого каталогу проекту:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Перегляньте обсяг перекладу без запису файлів:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Перекладіть кілька коренів вмісту одним викликом:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Запишіть переклади у явні групи виводу:

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

Використовуйте підстановник для кожної мови, коли кожна мова повинна містити вкладений підкаталог:

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

Якщо жоден з параметрів `markdown`, `notebook` або `images` не встановлено, API перекладає всі підтримувані типи: Markdown, ноутбуки та зображення.

## Review Translated Output

`run_review` виконує детерміновані перевірки перекладу без облікових даних LLM або Vision.

!!! note "Beta"
    `run_review` — це бета-версія детермінованого API перевірки. Він не викликає постачальників моделей і не записує файли, але схеми перевірок і виправлень можуть змінюватися.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Перевірте лише файли, змінені щодо базового ref, і виведіть результат у вигляді, сумісному з GitHub:

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

## Приклади API для копіювання й вставлення

Перекладіть вміст Markdown без запису файлів:

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

Перекладіть і перепишіть посилання в Markdown:

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

Перекладіть репозиторій з Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Перекладіть кілька коренів:

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

Збережіть терміни глосарію:

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

## Публічні точки входу

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

API перекладу вмісту призначені для інтеграцій, які вже мають вміст у пам'яті, наприклад розширення редактора, інструмент MCP, процесор ноутбуків або власний конвеєр.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ні | Async. Перекладає лише вміст Markdown. Не переписує посилання, не записує метадані і не додає дисклеймери. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Ні | Async. Перекладає Markdown-клітинки і зберігає немаркдаунні клітинки. Не переписує посилання, не записує метадані і не додає дисклеймери. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Читає лише вихідне зображення | Синхронно. Витягає та перекладає текст із зображення, потім повертає відрендерене зображення. Не зберігає метадані перекладеного зображення. |

`translate_markdown_content` і `translate_notebook_content` приймають необов'язковий `source_path` через свої опції. Шлях передається як контекст до перекладача; викликачі залишаються відповідальними за будь-яке проектно-специфічне переписування шляхів після перекладу.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Ті самі опції можна передати як словники:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

API з підтримкою агента не викликають Azure OpenAI або OpenAI з боку Co-op Translator. Вони готують фрагменти Markdown або ноутбука для перекладу хост-агентом, а потім реконструюють фінальний вміст із перекладених фрагментів.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Повертає автономну задачу Markdown з фрагментами, підказками та станом реконструкції. |
| `finish_markdown_agent_translation` | Реконструює Markdown з задачі та перекладених хост-агентом фрагментів. |
| `start_notebook_agent_translation` | Повертає задачу ноутбука з фрагментами Markdown-клітинок для перекладу хост-агентом. |
| `finish_notebook_agent_translation` | Реконструює JSON ноутбука, зберігаючи кодові клітинки, виводи та метадані. |

Цей робочий процес в основному призначений для MCP-хостів. Якщо вам потрібен виробничий переклад репозиторію з тим, щоб Co-op Translator керував викликами постачальників, використовуйте `translate_markdown_content`, `translate_notebook_content` або `run_translation`.

## Path Rewriting APIs

API переписування шляхів не виконують перекладу. Вони оновлюють посилання та шляхи у frontmatter після того, як викликачі знають початковий шлях, перекладений цільовий шлях і структуру проекту.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Тіло Markdown і frontmatter | Переписує посилання в Markdown і підтримувані поля frontmatter для перекладеної цілі. |
| `rewrite_notebook_paths` | Markdown-клітинки в JSON ноутбука | Застосовує переписування шляхів Markdown до кожної Markdown-клітинки і залишає немаркдаунні клітинки без змін. |

Аргумент `policy` може бути словником з такими полями:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Так | Код цільової мови, наприклад `"ko"` або `"pt-BR"`. |
| `root_dir` | Ні | Корінь проекту-джерела. За замовчуванням `"."`. |
| `translations_dir` | Ні | Каталог вихідних текстових перекладів. За замовчуванням `translations` під `root_dir`. |
| `translated_images_dir` | Ні | Каталог вихідних перекладених зображень. За замовчуванням `translated_images` під `root_dir`. |
| `translation_types` | Ні | Увімкнені типи перекладу. За замовчуванням Markdown, ноутбуки та зображення. |
| `lang_subdir` | Ні | Необов'язковий підкаталог під папкою кожної мови. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Коди цільових мов, розділені пробілами, наприклад `"ko ja fr"` або `"all"`. Псевдо-коди нормалізуються до канонічних значень BCP 47. |
| `root_dir` | `str` | `"."` | Корінь проекту для однієї цільової мови перекладу. Ігнорується, якщо вказано `root_dirs` або `groups`. |
| `update` | `bool` | `False` | Видалити і відтворити існуючі переклади для вибраних мов. |
| `images` | `bool` | `False` | Включити переклад зображень. Потребує конфігурації Azure AI Vision. |
| `markdown` | `bool` | `False` | Включити переклад Markdown. |
| `notebook` | `bool` | `False` | Включити переклад Jupyter-ноутбуків. |
| `debug` | `bool` | `False` | Увімкнути налагоджувальний логінг. |
| `save_logs` | `bool` | `False` | Зберегти файли журналів рівня DEBUG у кореневому каталозі `logs/`. |
| `yes` | `bool` | `True` | Автоматично підтверджувати підказки для програмного та CI-використання. |
| `add_disclaimer` | `bool` | `False` | Додати дисклеймери машинного перекладу до перекладених Markdown та ноутбуків. |
| `translations_dir` | `str \| None` | `None` | Користувацький каталог виходу текстових перекладів. Відносні шляхи розв'язуються відносно кожного кореня. |
| `image_dir` | `str \| None` | `None` | Користувацький каталог виходу перекладених зображень. Відносні шляхи розв'язуються відносно кожного кореня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Кілька коренів, які спільно використовують одні й ті ж налаштування виводу. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явні пари `(root_dir, translations_dir)`. Має пріоритет над `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL репозиторію, що використовується при рендерингу таблиці мов у README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Терміни глосарію, що зберігаються під час перекладу. Дублікати та порожні терміни нормалізуються. |
| `dry_run` | `bool` | `False` | Оціни обсяг перекладу та попередній перегляд поведінки міграції без запису файлів. |

## Review Parameters

`run_review` навмисно відтворює сигнатуру `run_translation`, де це можливо, щоб автоматизація могла перемикатися між робочими процесами перекладу і перевірки з мінімальними відгалуженнями.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Папки цільових мов для перевірки. Приймаються рядки, розділені пробілами, та ітерабельні об'єкти. `"all"` перевіряє всі виявлені мови перекладу. |
| `root_dir` | `str` | `"."` | Корінь проекту для однієї цілі перевірки. Ігнорується, якщо вказано `root_dirs` або `groups`. |
| `markdown` | `bool` | `False` | Включити вихідні файли Markdown та MDX. |
| `notebook` | `bool` | `False` | Включити вихідні файли Jupyter-ноутбуків. |
| `images` | `bool` | `False` | Зарезервовано для паритету з опціями перекладу. Посилання на зображення перевіряються з Markdown. |
| `translations_dir` | `str \| None` | `None` | Користувацький каталог виводу перекладеного тексту. Відносні шляхи інтерпретуються відносно кожного кореневого каталогу. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Кілька кореневих каталогів, які використовують однакові налаштування виводу. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явні `(root_dir, translations_dir)` пари. Має пріоритет над `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref, що використовується для обмеження перевірки файлами, які були змінені. |
| `output_format` | `str` | `"text"` | Формат виводу перевірки. Підтримувані значення: `"text"` та `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Розглядати попередження як відмови поряд із помилками. |
| `debug` | `bool` | `False` | Увімкнути налагоджувальне логування. |
| `save_logs` | `bool` | `False` | Зберігати файли журналу рівня DEBUG у кореневому каталозі `logs/`. |

Якщо жоден з `markdown`, `notebook` або `images` не встановлено, API переглядає Markdown, блокноти та посилання на зображення там, де це застосовано. Перегляд не викликає провайдера LLM і не вимагає ключів API.

## Вимоги до конфігурації

Провайдер-залежні API перекладу вимагають налаштування провайдера перед перекладом:

- Переклад Markdown та блокнотів вимагає провайдера LLM. Налаштуйте або Azure OpenAI, або OpenAI.
- Переклад зображень вимагає Azure AI Vision додатково до провайдера LLM.
- `run_translation` виконує прості перевірки підключення перед початком перекладу проекту.
- API з підтримкою агента `start_*_agent_translation` та `finish_*_agent_translation` не звертаються до LLM-провайдерів Co-op Translator. Хост-додаток або агент MCP перекладає підготовлені фрагменти.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` та `run_review` є детермінованими і не потребують облікових даних провайдерів.

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

`run_review` є детермінованою і не вимагає конфігурації Azure OpenAI, OpenAI або Azure AI Vision.

## Зауваги щодо поведінки

- API перекладу вмісту тримають переклад окремо від переписування шляхів проекту. Викликайте `rewrite_markdown_paths` або `rewrite_notebook_paths` явно, коли перекладеному вмісту потрібно відкоригувати посилання, відносні до проекту, для цільового розташування.
- API оркестрації проекту додають поведінку проекту довкола перекладу вмісту, включаючи пошук файлів, запис, переписування шляхів, метадані, очищення та необов'язкові застереження.
- `run_translation` виводить прогрес та зведення оцінок через Click, відтворюючи досвід користування CLI.
- `dry_run=True` обчислює оцінки, використовуючи віртуальні оновлення README, але не записує README або файли перекладу.
- `groups` обробляються послідовно. Перед початком роботи друкується єдина агрегована оцінка.
- Коли вибрано переклад зображень, відсутність конфігурації Vision призводить до помилки перед початком перекладу.
- Існуючі мовні теки на основі псевдонімів виявляються і можуть бути мігровані до канонічних назв мовних тек у процесі виконання.
- `run_review` завершується з помилкою при відсутності перекладених файлів, відсутніх або застарілих метаданих перекладу, пошкодженому Markdown frontmatter/огорожах коду та недійсному JSON перекладеного блокнота.
- `run_review` за замовчуванням повідомляє про відсутні локальні цілі посилань Markdown та посилання на зображення як попередження.

## Внутрішній шлях викликів

API делегує тій самій базовій реалізації, що використовується CLI:

Переклад:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` для перекладу в пам'яті.
2. `co_op_translator.api.translation.rewrite_markdown_paths` або `rewrite_notebook_paths` для явної постобробки шляхів.
3. `co_op_translator.api.translation.run_translation` для повної оркестрації проекту.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Спеціалізовані міксіни перекладу проекту для Markdown, блокнотів та зображень.
8. Перекладачі для Markdown, блокнотів, тексту та зображень під `co_op_translator.core`.

Перевірка:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерміновані перевірки під `co_op_translator.review.checks`

Наступні класи корисні для підтримувачів, але не експортуються як стабільний API на рівні пакета.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координує переклад на рівні проекту, управління каталогами, нормалізацію метаданих по мовах та делегування перекладачам для Markdown, блокнотів і зображень. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Виконує асинхронну обробку файлів для Markdown, блокнотів, зображень, виявлення застарілих даних та оновлення метаданих перекладу. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркеструє читання Markdown-файлів, переклад вмісту, переписування шляхів, метадані, застереження та запис. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркеструє читання файлів блокнотів, переклад клітинок Markdown, переписування шляхів, метадані, застереження та запис. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркеструє пошук вихідних зображень, переклад зображень, шляхи виводу, метадані та запис. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Знаходить пари перекладених Markdown, оцінює якість перекладу та читає метадані довіри для робочих потоків виправлення з низькою довірою. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координує детерміновані перевірки в межах файлів джерела, цільових мов та налаштованих коренів перекладу. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описує кореневий каталог джерела та каталог виводу перекладу, переглянутий для цього кореня. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Виявляє застарілі мовні теки-псевдоніми та готує плани міграції до канонічних тек згідно BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Завантажує `.env` файли та перевіряє, чи налаштовані необхідні LLM і необов'язкові провайдери Vision. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Автоматично виявляє Azure OpenAI або OpenAI, перевіряє необхідні змінні середовища та виконує перевірки підключення до провайдера. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Виявляє конфігурацію Azure AI Vision та виконує перевірки підключення для перекладу зображень. |