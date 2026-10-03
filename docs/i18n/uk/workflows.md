# Виберіть свій робочий процес

Co-op Translator можна використовувати трьома способами: через CLI, Python API та MCP Server. Вони мають однакові можливості перекладу, але кожен підходить для іншого робочого процесу.

Використовуйте цю сторінку, коли вирішуєте, з чого почати.

**Якщо ви редагуєте переклади вручну:** за замовчуванням робочі процеси CLI та Actions повторно перекладають змінені вихідні файли повністю, тому ваші формулювання в тих файлах можуть бути перезаписані. Перегляньте diff перед прийняттям оновлення. Для збереження блокової структури Markdown у прийнятих правках використовуйте опціональний [Постачальник стану перекладу Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Швидке рішення

| Якщо ви хочете... | Використовуйте | Почніть тут |
| --- | --- | --- |
| Перекладати або переглядати репозиторій з терміналу | CLI | [Довідник CLI](cli.md) |
| Додати переклад у Python-скрипт, сервіс, ноутбук або CI-завдання | Python API | [Python API](api.md) |
| Дозволити агенту, редактору або сумісному з MCP клієнту перекласти вміст для вас | MCP Server | [MCP Server](mcp.md) |
| Перекласти один документ Markdown, ноутбук або зображення, яке ваш додаток уже завантажив | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Перекласти весь репозиторій зі стандартними папками виводу та метаданими | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Коли використовувати CLI

Оберіть CLI, коли людина або CI-завдання запускає переклад репозиторію з терміналу.

CLI — найпряміший шлях, коли ви хочете, щоб Co-op Translator виявляв файли проєкту, створював перекладені вихідні файли, зберігав структуру проєкту, оновлював метадані та виконував команди перегляду.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

У цьому прикладі перекладаються Markdown і ноутбуки. Додавайте `-img` лише після налаштування [Azure AI Vision](configuration.md#azure-ai-vision). Для першого запуску, що лише перекладає Markdown, дотримуйтесь [Вашого першого перекладу](first-translation.md).

Підходить для:

- Ви перекладаєте репозиторій з терміналу.
- Вам потрібна повторювана команда для CI або робочих процесів релізу.
- Ви хочете вбудоване виявлення проєкту, шляхи виводу, метадані, очищення та перегляд.
- Ви віддаєте перевагу інтерфейсу команд замість написання коду на Python.

## Коли використовувати Python API

Виберіть Python API, коли ваш код має контролювати робочий процес.

API корисний для додатків, скриптів автоматизації, ноутбуків, сервісів і користувацьких конвеєрів. Він дозволяє викликати низькорівневі API перекладу вмісту для окремих файлів або запускати ту саму оркестрацію на рівні репозиторію, яку використовує CLI.

Перекладіть один документ Markdown і вирішіть, куди його зберегти:

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Підходить для:

- Ваш додаток вже читає файли, буфери, ноутбуки або байти зображень.
- Вам потрібна власна валідація, зберігання, логування, повторні спроби або процеси затвердження.
- Ви хочете перекласти один документ, ноутбук або зображення без обробки всього репозиторію.
- Ви хочете переклад репозиторію, але через автоматизацію на Python замість командного рядка.

## Коли використовувати MCP Server

Оберіть MCP Server, коли агент, редактор або сумісний з MCP клієнт має викликати інструменти Co-op Translator.

У типовій локальній конфігурації користувач не підтримує сервер запущеним вручну. MCP-клієнт запускає `co-op-translator-mcp` через `stdio`, коли йому потрібні інструменти.

Приклади запитів користувача, які агент може обробити:

- "Перекладіть цей файл Markdown на корейську та збережіть правильність посилань."
- "Перекладіть цей файл Markdown корейською за допомогою MCP-робочого процесу з підтримкою агента, використовуючи вашу модель для перекладених фрагментів."
- "Перекладіть цей ноутбук на корейську, збережіть кодові клітини і використайте Co-op Translator MCP для відновлення ноутбука."
- "Перекладіть текст на цьому зображенні японською та збережіть результат."
- "Запустіть пробний переклад репозиторію іспанською та скажіть мені, що змінилося б."
- "Перегляньте, чи переклад корейською актуальний."

Для Markdown і ноутбуків MCP може працювати в двох режимах:

| Режим | Коли використовувати | Основні інструменти |
| --- | --- | --- |
| З участю агента | Хост-агент MCP має перекладати фрагменти власною моделлю, без облікових даних постачальника LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| З підтримкою провайдера | Co-op Translator має викликати Azure OpenAI, OpenAI або Anthropic безпосередньо. | `translate_markdown_content`, `translate_notebook_content` |

Форма виклику Markdown-інструмента з підтримкою провайдера через MCP:

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

MCP image tool call shape:

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

Переклад репозиторію за замовчуванням виконується як пробний запуск через MCP:

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

Підходить для:

- Ви хочете робочі процеси перекладу природною мовою всередині агента або редактора.
- Ви хочете переклад Markdown або ноутбуків, де хост-агентська модель перекладає підготовлені фрагменти.
- Ви хочете, щоб агент переклав обраний вміст замість всього репозиторію.
- Ви хочете етап затвердження перед записами по всьому репозиторію.
- Ви хочете один інтерфейс, який надає інструменти для Markdown, ноутбуків, зображень, перегляду та переписування шляхів.

## Як вони взаємодіють

CLI є найкращим варіантом за замовчуванням для людей, які перекладають репозиторії. Python API найкраще підходить, коли ваш код керує робочим процесом. MCP Server найкраще підходить, коли робочим процесом керує агент або редактор.

Усі три підходи використовують один і той же публічний API Co-op Translator, тож ви можете почати з CLI, потім автоматизувати з Python і надати ті ж можливості MCP-клієнтам, коли вам потрібні робочі процеси під управлінням агента.