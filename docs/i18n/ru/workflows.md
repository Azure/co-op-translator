# Выберите рабочий процесс

Co-op Translator можно использовать тремя способами: через CLI, Python API и MCP-сервер. У них одинаковые возможности перевода, но каждый подходит для своего рабочего процесса.

Используйте эту страницу, когда решаете, с чего начать.

## Быстрый выбор

| Если вы хотите... | Использовать | Начать здесь |
| --- | --- | --- |
| Перевести или проверить репозиторий из терминала | CLI | [Справочник CLI](cli.md) |
| Добавить перевод в скрипт Python, сервис, блокнот или задачу CI | Python API | [Python API](api.md) |
| Позволить агенту, редактору или клиенту, совместимому с MCP, переводить контент для вас | MCP Server | [MCP Server](mcp.md) |
| Перевести один Markdown-документ, блокнот или изображение, которое уже загрузило ваше приложение | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Перевести весь репозиторий с использованием стандартных папок вывода и метаданных | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Используйте CLI, когда

Выбирайте CLI, когда за переводом репозитория из оболочки стоит человек или задача CI.

CLI — самый прямой путь, когда вы хотите, чтобы Co-op Translator обнаруживал файлы проекта, создавал переведённые результаты, сохранял структуру проекта, обновлял метаданные и запускал команды для проверки.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Хорошо подходит:

- Вы переводите репозиторий из терминала.
- Вам нужна повторяемая команда для CI или рабочих процессов релиза.
- Вам нужны встроенное обнаружение проекта, пути вывода, метаданные, очистка и проверка.
- Вы предпочитаете интерфейс командной строки вместо написания кода на Python.

## Используйте Python API, когда

Выбирайте Python API, когда рабочим процессом должен управлять ваш код.

API полезен для приложений, скриптов автоматизации, блокнотов, сервисов и пользовательских конвейеров. Он позволяет вызывать низкоуровневые API перевода контента для отдельных файлов или запускать ту же оркестрацию на уровне репозитория, которую использует CLI.

Переведите один Markdown-документ и решите, куда его сохранить:

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

Запустите перевод репозитория из Python:

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

Хорошо подходит:

- Ваше приложение уже читает файлы, буферы, блокноты или байты изображений.
- Вам нужны пользовательские проверки, хранение, логирование, повторы или потоки утверждения.
- Вы хотите перевести один документ, блокнот или изображение без обработки всего репозитория.
- Вам нужен перевод репозитория, но с помощью Python-автоматизации, а не команды оболочки.

## Используйте MCP-сервер, когда

Выбирайте MCP-сервер, когда агент, редактор или клиент, совместимый с MCP, должен вызывать инструменты Co-op Translator.

В обычной локальной настройке пользователь не держит сервер запущенным вручную. MCP-клиент запускает `co-op-translator-mcp` через `stdio`, когда ему нужны инструменты.

Примеры пользовательских запросов, которые агент мог бы обработать:

- "Переведите этот Markdown-файл на корейский и сохраните корректность ссылок."
- "Переведите этот Markdown-файл на корейский с помощью рабочего процесса MCP с поддержкой агента, используя вашу модель для переводимых фрагментов."
- "Переведите этот блокнот на корейский, сохраните кодовые ячейки и используйте Co-op Translator MCP для восстановления блокнота."
- "Переведите текст на этом изображении на японский и сохраните результат."
- "Выполните пробный перевод репозитория на испанский и скажите, что бы изменилось."
- "Проверьте, актуален ли корейский перевод."

Для Markdown и блокнотов MCP может работать в двух режимах:

| Режим | Используйте когда | Основные инструменты |
| --- | --- | --- |
| Agent-assisted | Хост-агент MCP должен переводить фрагменты своей собственной моделью, без учетных данных провайдера LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator должен напрямую вызывать Azure OpenAI или OpenAI. | `translate_markdown_content`, `translate_notebook_content` |

Формат вызова инструмента Markdown при использовании провайдера MCP:

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

Формат вызова инструмента для изображений MCP:

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

Перевод репозитория по умолчанию выполняется как пробный запуск (dry-run) через MCP:

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

Хорошо подходит:

- Вам нужны рабочие процессы перевода на естественном языке внутри агента или редактора.
- Вам нужен перевод Markdown или блокнотов, при котором модель хост-агента переводит подготовленные фрагменты.
- Вы хотите, чтобы агент переводил выбранный контент, а не весь репозиторий.
- Вам нужен шаг утверждения перед записью изменений во всем репозитории.
- Вам нужен единый интерфейс, который предоставляет инструменты для Markdown, блокнотов, изображений, проверки и переписывания путей.

## Как они работают вместе

CLI — лучший вариант по умолчанию для людей, переводящих репозитории. Python API подходит, когда рабочим процессом управляет ваш код. MCP-сервер лучше, когда рабочим процессом управляет агент или редактор.

Все три пути используют один и тот же публичный API Co-op Translator, поэтому вы можете начать с CLI, затем автоматизировать с помощью Python, а когда понадобятся рабочие процессы, управляемые агентами, открыть те же возможности для MCP-клиентов.