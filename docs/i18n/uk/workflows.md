# Виберіть свій робочий процес

Co-op Translator можна використовувати трьома способами: CLI, Python API і MCP server. Вони мають однакові можливості перекладу, але кожен підходить для різного робочого процесу.

Використовуйте цю сторінку, коли вирішуєте, з чого почати.

## Швидке рішення

| Якщо ви хочете... | Використати | Почніть тут |
| --- | --- | --- |
| Перекласти або перевірити репозиторій з терміналу | CLI | [Довідник CLI](cli.md) |
| Додати переклад до Python-скрипта, сервісу, ноутбука або CI-завдання | Python API | [API для Python](api.md) |
| Дозвольте агенту, редактору або сумісному з MCP клієнту перекласти вміст для вас | MCP Server | [MCP Server](mcp.md) |
| Перекласти один Markdown-документ, ноутбук або зображення, яке ваша програма вже завантажила | Python API або MCP Server | [API для Python](api.md) або [MCP Server](mcp.md) |
| Перекласти весь репозиторій з типовими папками виводу та метаданими | CLI або `run_translation` | [Довідник CLI](cli.md) або [API для Python](api.md) |

## Використовуйте CLI коли

Вибирайте CLI, коли переклад репозиторію виконується людиною або CI-завданням з оболонки.

CLI — найпряміший шлях, коли ви хочете, щоб Co-op Translator виявляв файли проекту, створював перекладені вихідні файли, зберігав структуру проєкту, оновлював метадані та запускали команди перевірки.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Добре підходить:

- Ви перекладаєте репозиторій з вашого терміналу.
- Вам потрібна відтворювана команда для CI або релізних робочих процесів.
- Вам потрібне вбудоване виявлення проекту, шляхи виводу, метадані, очищення та перевірка.
- Ви віддаєте перевагу інтерфейсу командного рядка замість написання коду на Python.

## Використовуйте Python API коли

Вибирайте Python API, коли ваш код має контролювати робочий процес.

API корисний для додатків, автоматизаційних скриптів, ноутбуків, сервісів і кастомних конвеєрів. Воно дозволяє викликати низькорівневі API перекладу вмісту для окремих файлів або запускати ту ж саму оркестрацію на рівні репозиторію, що й CLI.

Перекладіть один Markdown-документ і вирішіть, куди його зберегти:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Запустіть переклад репозиторію з Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Добре підходить:

- Ваш додаток вже читає файли, буфери, ноутбуки або байти зображень.
- Потрібна власна валідація, зберігання, логування, повторні спроби або процеси затвердження.
- Ви хочете перекласти один документ, ноутбук або зображення без обробки всього репозиторію.
- Ви хочете переклад репозиторію, але з автоматизації Python замість командного рядка.

## Використовуйте MCP Server коли

Вибирайте MCP server, коли агент, редактор або сумісний з MCP клієнт має викликати інструменти Co-op Translator.

У звичайній локальній конфігурації користувач вручну не тримає сервер увімкненим. MCP клієнт запускає `co-op-translator-mcp` через `stdio`, коли йому потрібні інструменти.

Приклади запитів користувача, які може обробити агент:

- "Перекладіть цей Markdown-файл корейською та збережіть посилання коректними."
- "Перекладіть цей Markdown-файл корейською за допомогою MCP-воркфлоу з підтримкою агента, використовуючи вашу власну модель для перекладених фрагментів."
- "Перекладіть цей ноутбук корейською, збережіть кодові клітинки та використайте Co-op Translator MCP для відновлення ноутбука."
- "Перекладіть текст на цьому зображенні японською та збережіть результат."
- "Виконайте сухий прогін перекладу репозиторію і скажіть, що змінилося б."
- "Перевірте, чи є корейський переклад актуальним."

Для Markdown і ноутбуків MCP може працювати в двох режимах:

| Режим | Коли використовувати | Основні інструменти |
| --- | --- | --- |
| За участю агента | Агент-хост MCP повинен перекладати фрагменти власною моделлю без облікових даних провайдера LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Підтримується провайдером | Co-op Translator повинен викликати Azure OpenAI або OpenAI безпосередньо. | `translate_markdown_content`, `translate_notebook_content` |

Форма виклику інструмента Markdown в режимі підтримки провайдера MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

Форма виклику інструмента зображень MCP:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Переклад репозиторію за умовчанням виконується у режимі сухого прогону через MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Добре підходить:

- Вам потрібні робочі процеси перекладу на природній мові всередині агента або редактора.
- Ви хочете переклад Markdown або ноутбука, де модель агента-хоста перекладає підготовлені фрагменти.
- Ви хочете, щоб агент переклав вибраний вміст замість усього репозиторію.
- Вам потрібен крок затвердження перед записами по всьому репозиторію.
- Вам потрібен один інтерфейс, що надає інструменти для Markdown, ноутбуків, зображень, перевірки та переписування шляхів.

## Як вони поєднуються

CLI — найкращий варіант за замовчуванням для людей, які перекладають репозиторії. Python API найкраще підходить, коли робочим процесом керує ваш код. MCP server найкраще підходить, коли робочим процесом керує агент або редактор.

Усі три шляхи використовують той самий публічний Co-op Translator API, тому ви можете почати з CLI, автоматизувати з Python пізніше і надати ті самі можливості клієнтам MCP, коли вам потрібні робочі процеси під керуванням агента.