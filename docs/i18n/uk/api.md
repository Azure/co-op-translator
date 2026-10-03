# Python API

Стабільний публічний Python API експортується з `co_op_translator.api`. Більшість інтеграцій використовують один із цих робочих потоків:

| Сценарій | Використовуйте, коли | Основні API |
| --- | --- | --- |
| Переклад окремих файлів або документів | Ваш додаток читає вихідний вміст, викликає Co-op Translator для перекладу та вирішує, куди зберегти результат. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Підготовка вмісту для перекладу хост-агентом | Ваш MCP хост або модель додатку перекладатиме частини, тоді як Co-op Translator займається розбиттям на частини та реконструкцією. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Переклад цілого репозиторію | Ви хочете, щоб Python API поводився як CLI та обробляв виявлення файлів, шляхи виводу, метадані, очищення й запис файлів. | `run_translation` |

Більшість нижчорівневих модулів у `core`, `config`, `review` та `utils` — це деталі реалізації, які використовуються цими точками входу API.

Клієнти MCP використовують той самий публічний API через [Сервер MCP](mcp.md). Використовуйте цю сторінку при прямому виклику з Python, а посібник MCP — коли ви надаєте доступ до Co-op Translator агенту або редактору. Якщо ви обираєте між CLI, Python API та MCP, почніть із [Виберіть робочий процес](workflows.md).

## Початковий потік роботи з API

Почніть тут, якщо ви викликаєте Co-op Translator з коду Python:

1. Налаштуйте провайдера LLM як описано в [Конфігурація](configuration.md), якщо лише не готуєте Markdown або частини блокнота для перекладу хост-агентом.
2. Вирішіть, чи ваша програма відповідає за введення/виведення файлів.
3. Використовуйте API для вмісту, коли ваша програма читає та записує окремі файли.
4. Використовуйте `run_translation`, коли Co-op Translator повинен обробляти репозиторій як CLI.
5. Використовуйте `run_review` після перекладу, якщо вам потрібні детерміністичні перевірки в автоматизації.

| Мета | API для початку |
| --- | --- |
| Перекласти один Markdown рядок або файл | `translate_markdown_content` |
| Перекласти один вміст блокнота | `translate_notebook_content` |
| Перекласти одне зображення | `translate_image_content` |
| Дозволити хост-агенту перекладати частини Markdown або блокноту | `start_markdown_agent_translation` або `start_notebook_agent_translation` |
| Переписати перекладені посилання після вибору шляху виводу | `rewrite_markdown_paths` або `rewrite_notebook_paths` |
| Перекласти весь репозиторій | `run_translation` |
| Перевірити перекладений вивід | `run_review` |

## Сценарій 1: Переклад окремих файлів або документів

Використовуйте цей робочий процес, коли у вас вже є файл, буфер редактора, вміст блокнота, запит MCP або вхід для кастомного конвеєра. Ваш код відповідає за введення/виведення файлів:

1. Прочитайте вихідний вміст.
2. Викличте API перекладу вмісту.
3. За потреби викличте API переписування шляхів, якщо перекладений вміст буде записано в папку перекладів проєкту.
4. Збережіть або поверніть результат із вашої програми.

API перекладу вмісту не виконують пошук проєкту, не записують метадані, не додають відмови від відповідальності та не переписують посилання автоматично.

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

Якщо перекладений Markdown не буде розміщено в макеті проєкту Co-op Translator, пропустіть `rewrite_markdown_paths` і збережіть перекладений рядок безпосередньо.

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

`translate_notebook_content` перекладає Markdown-клітинки та зберігає не-Markdown-клітинки. Переписування шляхів застосовується лише до Markdown-клітинок.

### Файл зображення

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

`translate_image_content` читає вихідне зображення та повертає відрендерений `PIL.Image.Image`. Він не записує метадані перекладеного зображення.

## Сценарій 2: Переклад цілого репозиторію

Використовуйте цей робочий процес, коли ви хочете, щоб Python API поводився як CLI `translate`. `run_translation` знаходить підтримувані файли, перекладає вибрані типи вмісту, переписує шляхи, записує вихідні файли, оновлює метадані та виконує завдання технічного обслуговування перекладу, такі як очищення.

`run_translation` — це рекомендована точка входу для оркестрації проєкту. `translate_project` експортується як сумісний псевдонім з тією ж поведінкою.

Перекласти файли Markdown в поточному репозиторії корейською та японською:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Перекласти лише блокноти з певного кореня проєкту:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Попередній перегляд обсягу перекладу без запису файлів:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Реєструвати структуровані події прогресу для інтеграції:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Збережіть корисне навантаження в таблиці job-event або передавайте його в інтерфейс користувача (UI) у потоковому режимі.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Події використовують версійну схему `co-op.translation.event.v1`. Інтеграціям слід
залежати від стабільних полів, таких як `type` та `stage_key`, а не від тексту, орієнтованого на людину
консольного виводу або `stage_label`.

Перекладіть кілька коренів вмісту за одним викликом:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Записувати переклади у явні групи виводу:

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

Використовуйте заповнювач для кожної мови, коли кожна мова має містити вкладений підкаталог:

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

Якщо жоден із `markdown`, `notebook` або `images` не встановлений, API перекладає всі підтримувані типи: Markdown, блокноти та зображення.

### Збереження прийнятих змін, внесених людиною, за допомогою постачальника стану перекладу

За замовчуванням Co-op Translator зберігає існуючу поведінку на рівні файлів: коли
джерело Markdown застаріле, весь перекладений файл генерується заново. Розміщені
інтеграції можуть опційно передати `TranslationStateProvider`, щоб зберегти правки, внесені людиною,
у блоках джерела, які не змінились.

Постачальник надає останню прийняту пару джерело/ціль і фіксує кожен новий
варіант. Прийняття залишається відповідальністю інтеграції — наприклад,
після злиття pull request з перекладом:

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

Для файлів Markdown з дійсною прийнятою базовою версією Co-op Translator вирівнює
верхньорівневі Markdown-блоки. Незмінені блоки джерела повторно використовують поточні перекладені
блоки, включно з правками, внесеними людьми; змінені або додані блоки джерела відправляються
на переклад; видалені блоки джерела видаляються. Якщо вирівнювання нечітке,
структура цілі змінилась, переклад блоку недійсний або базова версія відсутня,
Co-op Translator безпечно повертається до існуючого шляху повнофайлового
перекладу файлу.

Цей API зберігає стан перекладу документа, а не міждокументну пам'ять фраз або
сегментів перекладу. Наразі він застосовується до перекладу Markdown-проєктів.
Поведінка щодо блокнотів і зображень не змінилась. Передача `update=True`
все ще запитує повну регенерацію.

Якщо один або кілька файлів не можуть бути перекладені, `run_translation` викидає
`RuntimeError` після завершення робочого процесу проєкту, замість того щоб відзвітувати про
успішний запуск з відсутнім виводом. Інтеграції повинні розглядати це як невдале
завдання і зберегти попередній прийнятий стан перекладу.

## Перевірка перекладеного виводу

`run_review` виконує детерміністичні перевірки перекладу без облікових даних LLM або Vision.

!!! note "Beta"
    `run_review` — це бета-версія детерміністичного API перевірки. Він не викликає провайдерів моделей і не записує файли, проте схеми перевірок і проблем можуть змінюватися.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Після перекладу лише README використовуйте той самий обсяг для перевірки:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` перевіряє лише `README.md` у кожному налаштованому корені джерела,
включаючи кастомні `groups` та каталоги виводу. Інші документи та вкладені
README виключені. Відсутній вихідний README викликає `ValueError`; невдалі
перевірки перекладу викликають `RuntimeError`.

Перевіряти лише файли, змінені щодо базового референсу, і виводити формат, сумісний з GitHub:

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

## Приклади API для копіювання та вставки

Перекласти вміст Markdown без запису файлів:

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

Перекласти та переписати посилання в Markdown:

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

Перекласти репозиторій з Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Перекласти кілька коренів:

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

Зберегти терміни глосарія:

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

## API перекладу вмісту

API перекладу вмісту призначені для інтеграцій, які вже мають вміст у пам'яті, наприклад розширення редактора, інструмент MCP, обробник блокнотів або кастомний конвеєр.

| Функція | Вхід | Вихід | Ввід/вивід файлів | Примітки |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ні | Асинхронно. Перекладає лише вміст Markdown. Не переписує посилання, не записує метадані і не додає відмови від відповідальності. |
| `translate_notebook_content` | Notebook JSON `str` або `dict` | Notebook JSON `str` | Ні | Асинхронно. Перекладає Markdown-клітинки та зберігає не-Markdown-клітинки. Не переписує посилання, не записує метадані і не додає відмови від відповідальності. |
| `translate_image_content` | Шлях до зображення | `PIL.Image.Image` | Читає лише вихідне зображення | Синхронно. Витягує і перекладає текст з зображення, потім повертає відрендерене зображення. Не зберігає метадані перекладеного зображення. |

`translate_markdown_content` та `translate_notebook_content` приймають необов'язковий параметр `source_path` через свої опції. Шлях передається як контекст до перекладача; клієнти залишаються відповідальними за будь-яке специфічне для проєкту переписування шляхів після перекладу.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Ті самі опції можна передати у вигляді словників:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API перекладу за участю агента

API з підтримкою агента не викликають налаштованого провайдера LLM з Co-op Translator. Вони готують частини Markdown або блокнота для перекладу хост-агентом, а потім реконструюють кінцевий вміст з перекладених частин.

| Функція | Призначення |
| --- | --- |
| `start_markdown_agent_translation` | Повертає автономну задачу Markdown з частинами, підказками та станом реконструкції. |
| `finish_markdown_agent_translation` | Реконструює Markdown з задачі та перекладених хост-агентом частин. |
| `start_notebook_agent_translation` | Повертає задачу блокнота з частинами Markdown-клітинок для перекладу хост-агентом. |
| `finish_notebook_agent_translation` | Реконструює JSON блокнота, зберігаючи кодові клітинки, виводи та метадані. |

Цей робочий процес призначений головним чином для MCP хостів. Якщо вам потрібен продукційний переклад репозиторію з тим, щоб Co-op Translator керував викликами провайдерів, використовуйте `translate_markdown_content`, `translate_notebook_content` або `run_translation`.

## API переписування шляхів

API переписування шляхів не виконують перекладу. Вони оновлюють посилання та шляхи у frontmatter після того, як клієнти знають вихідний шлях, перекладений цільовий шлях та структуру проєкту.

| Функція | Область | Примітки |
| --- | --- | --- |
| `rewrite_markdown_paths` | Тіло Markdown та frontmatter | Переписує посилання в Markdown та підтримувані поля шляху в frontmatter для перекладеної цілі. |
| `rewrite_notebook_paths` | Markdown-клітинки в JSON блокнота | Застосовує переписування шляхів Markdown до кожної Markdown-клітинки та залишає не-Markdown-клітинки без змін. |

Аргумент `policy` може бути словником з такими полями:

| Поле | Обов'язкове | Призначення |
| --- | --- | --- |
| `language_code` | Так | Код цільової мови, наприклад `"ko"` або `"pt-BR"`. |
| `root_dir` | Ні | Корінь проєкту-джерела. За замовчуванням `"."`. |
| `translations_dir` | Ні | Каталог виводу текстових перекладів. За замовчуванням `translations` під `root_dir`. |
| `translated_images_dir` | Ні | Каталог виводу перекладених зображень. За замовчуванням `translated_images` під `root_dir`. |
| `translation_types` | Ні | Увімкнені типи перекладів. За замовчуванням Markdown, блокноти та зображення. |
| `lang_subdir` | Ні | Опційний підкаталог у кожній папці мови. |

## Параметри перекладу проєкту

| Параметр | Тип | Значення за замовчуванням | Призначення |
| --- | --- | --- | --- |
| `language_codes` | `str` | Обов'язкове | Коди цільових мов, розділені пробілами, наприклад `"ko ja fr"` або `"all"`. Псевдоніми кодів нормалізуються до канонічних значень BCP 47. |
| `root_dir` | `str` | `"."` | Корінь проєкту для одного цільового перекладу. Ігнорується, коли надані `root_dirs` або `groups`. |
| `update` | `bool` | `False` | Видалити та пересоздати існуючі переклади для обраних мов. |
| `images` | `bool` | `False` | Включити переклад зображень. Вимагає конфігурації Azure AI Vision. |
| `markdown` | `bool` | `False` | Включити переклад Markdown. |
| `notebook` | `bool` | `False` | Включити переклад Jupyter-блокнотів. |
| `debug` | `bool` | `False` | Увімкнути відлагоджувальне логування. |
| `save_logs` | `bool` | `False` | Зберігати лог-файли рівня DEBUG у кореневому каталозі `logs/`. |
| `yes` | `bool` | `True` | Автоматично підтверджувати підказки для програмного та CI-використання. |
| `add_disclaimer` | `bool` | `False` | Додавати застереження про машинний переклад у перекладені Markdown-файли та блокноти. |
| `translations_dir` | `str \| None` | `None` | Користувацький каталог виводу перекладів тексту. Відносні шляхи розв'язуються відносно кожного кореня. |
| `image_dir` | `str \| None` | `None` | Користувацький каталог виводу перекладених зображень. Відносні шляхи розв'язуються відносно кожного кореня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Кілька кореневих каталогів, що використовують однакові налаштування виводу. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явні пари `(root_dir, translations_dir)`. Має пріоритет над `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL репозиторію, який використовується при формуванні таблиці мов у README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Терміни глосарію, які слід зберегти під час перекладу. Дублікати та пусті терміни нормалізуються. |
| `dry_run` | `bool` | `False` | Оцінити обсяг перекладу та переглянути поведінку міграції без запису файлів. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Необов'язковий адаптер збереження accepted-baseline та candidate для інкрементних оновлень Markdown. Якщо не вказано, зберігається існуюча поведінка обробки повних файлів. |

## Параметри перевірки

`run_review` навмисно віддзеркалює сигнатуру `run_translation`, де це можливо, щоб автоматизація могла перемикатися між процесами перекладу та перевірки з мінімальною розгалуженістю.

| Параметр | Тип | За замовчуванням | Призначення |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Цільові папки мов для перевірки. Приймаються рядки з пробілами та ітеровані значення. `"all"` перевіряє всі виявлені мови перекладу. |
| `root_dir` | `str` | `"."` | Корінь проекту для однієї цілі перевірки. Ігнорується, коли вказані `root_dirs` або `groups`. |
| `markdown` | `bool` | `False` | Включати вихідні файли Markdown та MDX. |
| `notebook` | `bool` | `False` | Включати вихідні файли Jupyter-блокнотів. |
| `images` | `bool` | `False` | Зарезервовано для відповідності опціям перекладу. Посилання на зображення перевіряються з Markdown. |
| `translations_dir` | `str \| None` | `None` | Користувацький каталог виводу перекладів тексту. Відносні шляхи розв'язуються відносно кожного кореня. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Кілька кореневих каталогів, що використовують однакові налаштування виводу. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Явні пари `(root_dir, translations_dir)`. Має пріоритет над `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-реф, який використовується для обмеження перевірки лише зміненими файлами джерела. |
| `readme_only` | `bool` | `False` | Перевіряти лише `README.md` у кожному корені джерела. Відсутність README у джерелі викликає `ValueError`. |
| `output_format` | `str` | `"text"` | Формат виводу перевірки. Підтримуються значення `"text"` та `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Розглядати попередження як відмови на додаток до помилок. |
| `debug` | `bool` | `False` | Увімкнути налагоджувальне логування. |
| `save_logs` | `bool` | `False` | Зберігати файли журналів рівня DEBUG у кореневій теці `logs/`. |

Якщо жоден з параметрів `markdown`, `notebook` або `images` не вказано, API перевіряє Markdown, блокноти та посилання на зображення там, де це застосовно. Перевірка не викликає LLM-провайдера і не вимагає API-ключів.

## Вимоги до конфігурації

API перекладу з підтримкою провайдерів вимагають налаштування провайдера перед перекладом:

- Для перекладу Markdown та блокнотів потрібен LLM-провайдер. Налаштуйте Azure OpenAI, OpenAI або Anthropic.
- Для перекладу зображень потрібен Azure AI Vision на додаток до LLM-провайдера.
- `run_translation` виконує легкі перевірки підключення перед початком перекладу проекту.
- API з підтримкою агента `start_*_agent_translation` та `finish_*_agent_translation` не викликають LLM-провайдерів Co-op Translator. Гостьовий додаток або агент MCP перекладає підготовлені частини.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` та `run_review` є детермінованими і не потребують облікових даних провайдера.

Обов'язкові змінні для Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Обов'язкові змінні для OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Обов'язкові змінні для Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` та `ANTHROPIC_MAX_TOKENS` є необов'язковими. Microsoft Agent Framework є клієнтом моделі за замовчуванням для всіх провайдерів, починаючи з Co-op Translator 0.22.0. Semantic Kernel все ще можна тимчасово вибрати за допомогою `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, але це викликає попередження про застарівання; див. [configuration](configuration.md#model-client-backend) для плану поетапного видалення.

Обов'язкові змінні Azure AI Vision для перекладу зображень:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` є детермінованою і не вимагає налаштування LLM або Azure AI Vision.

## Примітки щодо поведінки

- API перекладу контенту розділяють сам переклад і переписування шляхів проекту. Викликайте `rewrite_markdown_paths` або `rewrite_notebook_paths` явно, коли перекладеному вмісту потрібно відкоригувати посилання, відносні до проекту, для цільового розташування.
- API оркестрації проекту додають функціональність навколо перекладу контенту, включно з виявленням файлів, записом файлів, переписуванням шляхів, метаданими, прибиранням та опційними застереженнями.
- `run_translation` виводить прогрес і підсумки оцінок через того ж репортера на базі Rich, що використовується CLI. Неінтерактивний вивід повертається до простого тексту.
- `dry_run=True` обчислює оцінки, використовуючи віртуальні оновлення README, але не записує README чи файли перекладу.
- `groups` обробляються послідовно. Один загальний агрегований звіт з оцінками виводиться перед початком роботи.
- Коли вибрано переклад зображень, відсутність конфігурації Vision викликає помилку перед початком перекладу.
- Існуючі папки мов на основі псевдонімів виявляються і можуть бути мігровані на канонічні назви папок мов у процесі виконання.
- `run_review` завершується помилкою при відсутності перекладених файлів, відсутніх або застарілих метаданих перекладу, пошкодженому frontmatter або кодових блоках Markdown, та некоректному JSON перекладеного блокнота.
- За замовчуванням `run_review` повідомляє про відсутні локальні цілі посилань у Markdown та зображеннях як попередження.

## Внутрішній шлях викликів

API делегує ту саму основну реалізацію, яку використовує CLI:

Переклад:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` для перекладу в пам'яті.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` для явної постобробки шляхів.
3. `co_op_translator.api.translation.run_translation` для повної оркестрації проекту.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Спеціалізовані міксини перекладу проекту для Markdown, блокнотів та зображень.
8. Перекладачі Markdown, блокнотів, тексту та зображень у `co_op_translator.core`.

Перевірка:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерміновані перевірки у `co_op_translator.review.checks`

Наступні класи корисні для розробників, але не експортуються як стабільний API на рівні пакета.

| Клас | Модуль | Відповідальність |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координує переклад на рівні проекту, управління каталогами, нормалізацію метаданих для кожної мови та делегування перекладачам Markdown, блокнотів і зображень. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Виконує асинхронну обробку файлів для Markdown, блокнотів, зображень, виявлення застарілих елементів та оновлення метаданих перекладу. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркеструє читання Markdown-файлів, переклад вмісту, переписування шляхів, метадані, застереження та запис файлів. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркеструє читання файлів блокнотів, переклад Markdown-клітин, переписування шляхів, метадані, застереження та запис файлів. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркеструє виявлення початкових зображень, переклад зображень, шляхи виводу, метадані та запис файлів. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Знаходить пари перекладених Markdown, оцінює якість перекладу та читає метадані про довіру для робочих процесів відновлення при низькій довірі. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координує детерміновані перевірки серед файлів джерела, цільових мов та налаштованих коренів перекладу. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описує корінь джерела та директорію виводу перекладу, що перевіряється для цього кореня. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Виявляє застарілі папки-псевдоніми мов і готує плани міграції до канонічних папок BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Завантажує файли `.env` і перевіряє, чи налаштовані обов'язкові LLM та необов'язкові Vision провайдери. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Автовизначає Azure OpenAI, OpenAI або Anthropic, перевіряє обов'язкові змінні оточення та запускає перевірки підключення до провайдера. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Визначає конфігурацію Azure AI Vision та виконує перевірки підключення для перекладу зображень. |