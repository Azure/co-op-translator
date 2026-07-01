# Сервер MCP

Co-op Translator включает сервер Model Context Protocol для агентов, редакторов и клиентов, совместимых с MCP.

Для стандартной локальной настройки пользователям не нужно вручную запускать отдельный сервер. Они настраивают свой MCP-клиент, и клиент автоматически запускает `co-op-translator-mcp` через `stdio`, когда ему нужны инструменты Co-op Translator.

Если вы выбираете между CLI, Python API и MCP, начните с [Выберите свой рабочий процесс](workflows.md).

Используйте MCP, когда агент или редактор должен вызывать Co-op Translator напрямую:

| Цель пользователя | Инструменты MCP |
| --- | --- |
| Перевести один Markdown документ, блокнот или изображение | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Перевести содержимое Markdown или блокнота с моделью хост-агента | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Переписать переведённые ссылки Markdown или блокнота после выбора пути вывода | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Перевести весь репозиторий, как CLI | `run_translation`, `translate_project` |
| Просмотреть переведённый вывод без учетных данных LLM | `run_review` |
| Проверить возможности и статус окружения | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Сервер MCP оборачивает тот же публичный Python API, документированный в [Python API](api.md). Инструменты с поддержкой провайдеров используют тех же настроенных провайдеров, что и CLI и Python API. Инструменты с помощью хост-агента подготавливают куски для перевода хост-агентом MCP, а затем используют Co-op Translator для реконструкции финального Markdown или блокнота.

## Шаг 1: Установите и настройте Co-op Translator

Установите Co-op Translator в Python-окружение, которое будет использовать ваш MCP-клиент:

```bash
pip install co-op-translator
```

Для локальной разработки из этого репозитория установите пакет в режиме editable:

```bash
pip install -e .
```

Выберите режим перевода, который будет использовать ваш MCP-клиент:

| Режим | Используйте для | Учётные данные |
| --- | --- | --- |
| Provider-backed | Co-op Translator вызывает `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` или `run_translation`. | Для перевода Markdown и блокнотов требуются Azure OpenAI или OpenAI. Для перевода изображений также требуется Azure AI Vision. |
| Agent-assisted | Хост-агент MCP переводит куски, возвращённые `start_markdown_agent_translation` или `start_notebook_agent_translation`. | Для перевода кусков Markdown или блокнотов не требуются провайдерные учетные данные Co-op Translator LLM. Режим с хост-агентом пока не покрывает перевод изображений. |

Если вы начинаете с перевода Markdown или блокнота внутри агента, такого как Codex или Claude Code, начните с режима с хост-агентом. Используйте режим provider-backed, когда вы хотите, чтобы сам Co-op Translator вызывал настроенных провайдеров, при переводе изображений или при запуске перевода на уровне репозитория, как в CLI.

Настройте учётные данные провайдера только для рабочих процессов с поддержкой провайдеров:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Дополнительно для provider-backed перевода изображений требуется:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Режим с хост-агентом в настоящее время охватывает Markdown и Markdown-ячейки блокнотов. Перевод изображений по-прежнему использует pipeline изображений с поддержкой провайдера и требует Azure AI Vision для OCR и рендеринга с учётом макета.

## Шаг 2: Настройте клиент MCP

Для обычной локальной настройки через `stdio` добавьте Co-op Translator в конфигурацию вашего MCP-клиента. Клиент будет автоматически запускать и останавливать процесс.

Конфигурация для установленного пакета:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Конфигурация при использовании исходного кода на Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Конфигурация при использовании исходного кода на macOS или Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

После изменения конфигурации MCP-клиента перезапустите или перезагрузите клиент, чтобы он мог обнаружить новый сервер.

## Шаг 3: Проверьте сервер в клиенте

Попросите MCP-клиент перечислить доступные инструменты или сначала вызовите один из вспомогательных read-only инструментов:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Полезные первые проверки:

| Инструмент | Что проверить |
| --- | --- |
| `get_api_overview` | Подтверждает, что сервер доступен и показывает доступные рабочие процессы. |
| `list_supported_languages` | Подтверждает, что упакованные данные языков можно загрузить. |
| `get_configuration_status` | Подтверждает доступность провайдеров LLM и Vision без раскрытия секретных значений. |

## Шаг 4: Выберите рабочий процесс

### Перевод отдельных файлов или документов

Используйте инструменты provider-backed для контента, когда MCP-клиент уже имеет содержимое документа или путь к изображению и Co-op Translator должен вызывать настроенные провайдеры перевода.

Для Markdown:

1. Вызовите `translate_markdown_content` с `document`, `language_code` и при необходимости `source_path`.
2. Если переведённый результат будет записан в layout вывода Co-op Translator, вызовите `rewrite_markdown_paths`.
3. Позвольте клиенту записать или вернуть итоговое `content`.

Для блокнотов:

1. Вызовите `translate_notebook_content` с JSON блокнота и `language_code`.
2. Вызовите `rewrite_notebook_paths`, если переведённые ссылки в блокноте нужно скорректировать для целевого пути.
3. Запишите или верните итоговый JSON блокнота.

Для изображений:

1. Вызовите `translate_image_content` с `image_path`, `language_code` и опционально `root_dir` или `fast_mode`.
2. Прочитайте возвращённые `data_base64` и `mime_type`.
3. Если указан `output_path`, переведённое изображение также сохраняется по этому пути.

Инструменты для работы с контентом не выполняют обнаружение проекта, обновление метаданных, добавление оговорок или автоматическое переписывание путей. Если вы хотите, чтобы хост-агент переводил куски Markdown или блокнота без провайдерных LLM-учётных данных Co-op Translator, используйте приведённый ниже рабочий процесс с хост-агентом.

### Перевод с помощью модели хост-агента

Используйте инструменты с хост-агентом, когда вы хотите, чтобы модель хост-агента MCP, например ассистент по программированию, генерировала переведённый текст вместо настройки Azure OpenAI или OpenAI для Co-op Translator.

В чат-ориентированном MCP-клиенте обычно не нужно самим писать JSON для инструмента. Попросите агента использовать рабочий процесс с хост-агентом:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Для блокнотов используйте ту же схему:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Если ваш MCP-клиент поддерживает server prompts, используйте `agent_assisted_markdown_translation_prompt`, чтобы клиент загрузил те же инструкции рабочего процесса.

Для Markdown:

1. Вызовите `start_markdown_agent_translation` с `document`, `language_code` и при необходимости `source_path`.
2. Переведите каждый возвращённый кусок в хост-агенте, следуя `prompt` для куска.
3. Вызовите `finish_markdown_agent_translation` с оригинальной `job` и переведёнными кусками, используя `chunk_id` и `translated_text`.
4. Если содержимое будет записано в целевой путь перевода, вызовите `rewrite_markdown_paths`.

Для блокнотов:

1. Вызовите `start_notebook_agent_translation` с JSON блокнота и `language_code`.
2. Переведите каждый возвращённый кусок в хост-агенте.
3. Вызовите `finish_notebook_agent_translation` с оригинальной `job` и переведёнными кусками.
4. Вызовите `rewrite_notebook_paths`, если переведённые ссылки в блокноте нужно скорректировать под целевой путь.

Инструменты с хост-агентом не вызывают Azure OpenAI или OpenAI из Co-op Translator. Хост-агент отвечает за перевод возвращённых кусков. Co-op Translator выполняет разбиение Markdown на куски, сохранение заполнителей, восстановление frontmatter, замену ячеек в блокноте и нормализацию после перевода.

### Перевод всего репозитория

Используйте `run_translation`, когда пользователь хочет, чтобы Co-op Translator вёл себя как CLI `translate`.

Перевод репозитория по умолчанию выполняется с `dry_run=true`, чтобы агент мог проверить масштаб до изменения файлов:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Чтобы разрешить записи, вызывающий должен установить одновременно `dry_run=false` и `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` предоставляется как совместимый псевдоним для `run_translation`.

### Просмотр переведённого вывода

Используйте `run_review` для детерминированных проверок, которые не требуют учётных данных LLM или Vision:

!!! note "Beta"
    MCP предоставляет бета-версию API `run_review`. Он безопасен для read-only рабочих процессов проверки, но проверки и схемы проблем могут эволюционировать.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Результат включает захваченный текстовый вывод и структурированное резюме проверки, когда оно доступно.

## Ручной запуск сервера

Ручные запуски в основном предназначены для отладки или для транспортов, которые ведут себя как долгоживущие серверы.

Отлажьте стандартный stdio-сервер:

```bash
co-op-translator-mcp
```

Запуск из исходного кода:

```bash
python -m co_op_translator.mcp.server
```

Запуск длительного HTTP или SSE сервера:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Для локальной интеграции с редакторами и агентами предпочитайте конфигурацию `stdio`, управляемую клиентом, описанную в Шаге 2.

## Инструменты

| Инструмент | Назначение | Записывает файлы |
| --- | --- | --- |
| `translate_markdown_content` | Перевести строку Markdown. | Нет |
| `translate_notebook_content` | Перевести Markdown-ячейки в JSON блокнота. | Нет |
| `translate_image_content` | Перевести текст на одном изображении и вернуть base64 данные изображения. | Опционально, только когда `output_path` предоставлен |
| `start_markdown_agent_translation` | Подготовить куски Markdown для перевода хост-агентом без провайдерных LLM-учётных данных Co-op Translator. | Нет |
| `finish_markdown_agent_translation` | Восстановить Markdown из переведённых хост-агентом кусков. | Нет |
| `start_notebook_agent_translation` | Подготовить куски Markdown-ячeек блокнота для перевода хост-агентом. | Нет |
| `finish_notebook_agent_translation` | Восстановить JSON блокнота из переведённых хост-агентом кусков. | Нет |
| `rewrite_markdown_paths` | Переписать пути в теле Markdown и frontmatter для целевого перевода. | Нет |
| `rewrite_notebook_paths` | Переписать пути внутри Markdown-ячeек блокнота. | Нет |
| `run_translation` | Запустить перевод проекта, как CLI. | Да, когда `dry_run=false` и `confirm_write=true` |
| `translate_project` | Совместимый псевдоним для `run_translation`. | Да, когда `dry_run=false` и `confirm_write=true` |
| `run_review` | Запустить детерминированные проверки. | Нет |
| `get_configuration_status` | Сообщить о настроенных провайдерах LLM и Vision без раскрытия секретов. | Нет |
| `list_supported_languages` | Перечислить поддерживаемые коды целевых языков. | Нет |
| `get_api_overview` | Описать доступные рабочие процессы и инструменты MCP. | Нет |

## Ресурсы

| Resource URI | Назначение |
| --- | --- |
| `co-op://api` | JSON-обзор рабочих процессов и инструментов. |
| `co-op://supported-languages` | JSON-список поддерживаемых кодов языков. |
| `co-op://configuration` | JSON-резюме доступности провайдеров без секретов. |

## Подсказки

| Подсказка | Назначение |
| --- | --- |
| `translate_markdown_document_prompt` | Направляет MCP-клиент через перевод содержимого с опциональным переписыванием путей. |
| `agent_assisted_markdown_translation_prompt` | Направляет MCP-клиент через перевод Markdown с помощью хост-агента без провайдерных LLM-учётных данных Co-op Translator. |
| `translate_repository_prompt` | Направляет MCP-клиент через перевод репозитория с первичным dry-run. |

## Примеры копирования и вставки

Перевести содержимое Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Перезаписать переведённые ссылки Markdown:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Перевести Markdown с помощью модели хост-агента:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

После того как хост-агент переведёт каждый возвращённый кусок, завершите задачу полным объектом `job`, возвращённым `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Просмотреть предварительный перевод репозитория:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Устранение неполадок

| Проблема | Что попробовать |
| --- | --- |
| MCP-клиент не может найти `co-op-translator-mcp`. | Используйте абсолютный путь к исполняемому файлу Python и конфигурацию исходного кода `["-m", "co_op_translator.mcp.server"]`. |
| Сервер в списке, но перевод не удаётся. | Вызовите `get_configuration_status` и подтвердите наличие провайдера LLM. |
| Нужен перевод Markdown или блокнота без ключей Azure OpenAI/OpenAI. | Используйте `start_markdown_agent_translation` / `finish_markdown_agent_translation` или эквиваленты для блокнотов, чтобы хост-агент переводил куски. |
| Перевод изображений не работает. | Подтвердите, что переменные Azure AI Vision установлены, и вызовите `get_configuration_status`. |
| Перевод репозитория не записывает файлы. | Устанавливайте `dry_run=false` и `confirm_write=true` только после явного одобрения пользователя. |
| Изменения в конфигурации клиента не отображаются. | Перезапустите или перезагрузите MCP-клиента. |

## Примечания по безопасности

- Вызовы инструментов MCP контролируются моделью в хост-приложении, поэтому перевод репозитория по умолчанию выполняется в режиме dry-run.
- Полный перевод репозитория может создать, обновить или удалить много файлов. Требуйте явного одобрения пользователя перед установкой `confirm_write=true`.
- Инструмент статуса конфигурации никогда не возвращает API-ключи, endpoints или другие секретные значения.
- Перевод изображений возвращает base64 данные изображения. Большие изображения могут привести к объёмным ответам инструментов.
- Инструменты с хост-агентом возвращают исходные куски и подсказки хосту MCP. Используйте их только с содержимым, которое пользователь согласен отправлять модели хост-агента.