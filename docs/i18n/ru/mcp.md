# Сервер MCP

Co-op Translator включает сервер Model Context Protocol для агентов, редакторов и клиентов, совместимых с MCP.

В типичной локальной установке пользователям не нужно запускать отдельный сервер вручную. Они настраивают свой MCP-клиент, и клиент автоматически запускает `co-op-translator-mcp` через `stdio`, когда нужны инструменты Co-op Translator.

Если вы выбираете между CLI, Python API и MCP, начните с [Выберите рабочий процесс](workflows.md).

Используйте MCP, когда агент или редактор должен вызывать Co-op Translator напрямую:

| Цель пользователя | Инструменты MCP |
| --- | --- |
| Перевести один Markdown-документ, ноутбук или изображение | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Перевести содержимое Markdown или ноутбука с помощью модели хост-агента | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Перезаписать пути в переведённых Markdown или ноутбуке после выбора пути вывода | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Перевести весь репозиторий, как при использовании CLI | `run_translation`, `translate_project` |
| Просмотреть переведённый результат без учётных данных LLM | `run_review` |
| Проверить возможности и состояние окружения | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Сервер MCP оборачивает тот же публичный Python API, документированный в [Python API](api.md). Инструменты с поддержкой провайдеров используют те же настроенные провайдеры, что и CLI и Python API. Инструменты с помощью хост-агента подготавливают фрагменты для перевода хост-агентом MCP, затем Co-op Translator используется для реконструкции окончательного Markdown или ноутбука.

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

| Режим | Используется для | Учетные данные |
| --- | --- | --- |
| С поддержкой провайдера | Co-op Translator вызывает `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, или `run_translation`. | Для перевода требуются Azure OpenAI, OpenAI или Anthropic. Для перевода изображений также требуется Azure AI Vision. |
| С помощью хост-агента | Хост-агент MCP переводит фрагменты, возвращаемые `start_markdown_agent_translation` или `start_notebook_agent_translation`. | Для фрагментов Markdown или ноутбука не требуются учетные данные LLM-провайдера Co-op Translator. Перевод изображений пока не поддерживается режимом с хост-агентом. |

Если вы начинаете с перевода Markdown или ноутбуков внутри агента, такого как Codex или Claude Code, начните с режима с хост-агентом. Используйте режим с поддержкой провайдера, когда вы хотите, чтобы Co-op Translator сам вызывал настроенных провайдеров, когда переводите изображения или когда выполняете перевод на уровне репозитория, как в CLI.

Настройте одного провайдера для рабочих процессов с поддержкой провайдера:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Или OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Или Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Дополнительно для перевода изображений в режиме с поддержкой провайдера требуется:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Режим с хост-агентом в настоящее время охватывает Markdown и Markdown-ячейки ноутбуков. Перевод изображений по-прежнему использует конвейер изображений с поддержкой провайдера и требует Azure AI Vision для OCR и рендеринга с учётом раскладки.

## Шаг 2: Настройте ваш MCP-клиент

Для обычной локальной конфигурации через `stdio` добавьте Co-op Translator в конфигурацию вашего MCP-клиента. Клиент будет автоматически запускать и останавливать процесс.

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

Конфигурация при проверке исходников в Windows:

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

Конфигурация при проверке исходников на macOS или Linux:

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

После изменения конфигурации MCP-клиента перезапустите или перезагрузите клиент, чтобы он обнаружил новый сервер.

## Шаг 3: Проверьте сервер в клиенте

Попросите MCP-клиент перечислить доступные инструменты или сначала вызовите один из помощников только для чтения:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Полезные первые проверки:

| Инструмент | Что проверить |
| --- | --- |
| `get_api_overview` | Подтверждает доступность сервера и показывает доступные рабочие процессы. |
| `list_supported_languages` | Подтверждает, что данные по языкам из пакета можно загрузить. |
| `get_configuration_status` | Подтверждает доступность провайдеров LLM и Vision без раскрытия секретных значений. |

## Шаг 4: Выберите рабочий процесс

### Перевод отдельных файлов или документов

Используйте инструменты с поддержкой провайдера, когда MCP-клиент уже имеет содержимое документа или путь к изображению, и Co-op Translator должен вызывать настроенных провайдеров для перевода.

Для Markdown:

1. Вызовите `translate_markdown_content` с `document`, `language_code` и опционально `source_path`.
2. Если переведённый результат будет записан в выходной макет Co-op Translator, вызовите `rewrite_markdown_paths`.
3. Позвольте клиенту записать или вернуть финальный `content`.

Для ноутбуков:

1. Вызовите `translate_notebook_content` с JSON ноутбука и `language_code`.
2. Вызовите `rewrite_notebook_paths`, если ссылки в переведённом ноутбуке нужно скорректировать под целевой путь.
3. Запишите или верните финальный JSON ноутбука.

Для изображений:

1. Вызовите `translate_image_content` с `image_path`, `language_code` и опционально `root_dir` или `fast_mode`.
2. Прочитайте возвращённые `data_base64` и `mime_type`.
3. Если указан `output_path`, переведённое изображение также будет сохранено по этому пути.

Инструменты для содержимого не выполняют обнаружение проекта, обновление метаданных, уведомления или автоматическое переписывание путей. Если вы хотите, чтобы хост-агент переводил фрагменты Markdown или ноутбука без учетных данных LLM-провайдера Co-op Translator, используйте нижеописанный рабочий процесс с хост-агентом.

### Перевод с помощью модели хост-агента

Используйте инструменты с хост-агентом, когда вы хотите, чтобы хост-агент MCP, например помощник по программированию, генерировал переведённый текст вместо настройки LLM-провайдера для Co-op Translator.

В чат-ориентированном MCP-клиенте обычно не нужно самостоятельно писать JSON инструмента. Попросите агента использовать рабочий процесс с хост-агентом:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Для ноутбуков используйте тот же паттерн:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Если ваш MCP-клиент поддерживает серверные подсказки (server prompts), используйте `agent_assisted_markdown_translation_prompt`, чтобы клиент загрузил те же инструкции рабочего процесса.

Для Markdown:

1. Вызовите `start_markdown_agent_translation` с `document`, `language_code` и опционально `source_path`.
2. Переведите каждый возвращённый фрагмент в хост-агенте, следуя `prompt` для фрагмента.
3. Вызовите `finish_markdown_agent_translation` с оригинальным `job` и переведёнными фрагментами, используя `chunk_id` и `translated_text`.
4. Если содержимое будет записано в целевой переведённый путь, вызовите `rewrite_markdown_paths`.

Для ноутбуков:

1. Вызовите `start_notebook_agent_translation` с JSON ноутбука и `language_code`.
2. Переведите каждый возвращённый фрагмент в хост-агенте.
3. Вызовите `finish_notebook_agent_translation` с оригинальным `job` и переведёнными фрагментами.
4. Вызовите `rewrite_notebook_paths`, если ссылки в переведённом ноутбуке нужно скорректировать под целевой путь.

Инструменты с хост-агентом не вызывают настроенного LLM-провайдера из Co-op Translator. Хост-агент отвечает за перевод возвращённых фрагментов. Co-op Translator выполняет разбиение Markdown на фрагменты, сохранение заполнителей, восстановление frontmatter, замену ячеек ноутбука и нормализацию после перевода.

### Перевести весь репозиторий

Используйте `run_translation`, когда пользователь хочет, чтобы Co-op Translator вел себя как CLI-команда `translate`.

Перевод репозитория по умолчанию использует `dry_run=true`, чтобы агент мог оценить объём работ перед изменением файлов:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Результат `run_translation` включает массив `events` с версионированными
`co-op.translation.event.v1` событиями прогресса. MCP-клиенты должны использовать поля такие
как `type`, `stage_key`, `completed`, `total` и `current_path` вместо
разбора захваченного текста консоли. Передайте `json_events_path`, чтобы также записать эти события
в NDJSON-файл.

Чтобы разрешить запись, вызывающий должен установить и `dry_run=false`, и `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` предоставлен как совместимый псевдоним для `run_translation`.

### Просмотр переведённого результата

Используйте `run_review` для детерминированных проверок, которые не требуют учетных данных LLM или Vision:

!!! note "Beta"
    MCP предоставляет бета-API `run_review`. Оно безопасно для рабочих процессов только для чтения, но проверки ревью и схемы проблем могут изменяться.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Результат включает захваченный текстовый вывод и структурированное резюме ревью, если оно доступно.

## Ручной запуск сервера

Ручной запуск в основном используется для отладки или для транспортов, которые ведут себя как долгоживущие серверы.

Отладьте сервер по умолчанию через stdio:

```bash
co-op-translator-mcp
```

Запустить из исходной копии (source checkout):

```bash
python -m co_op_translator.mcp.server
```

Запустить долгоживущий HTTP- или SSE-сервер:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Для локальной интеграции редактора и агента предпочтительна управляемая клиентом конфигурация `stdio`, описанная в Шаге 2.

## Инструменты

| Инструмент | Назначение | Записывает файлы |
| --- | --- | --- |
| `translate_markdown_content` | Переводит строку Markdown. | Нет |
| `translate_notebook_content` | Переводит Markdown-ячейки в JSON ноутбука. | Нет |
| `translate_image_content` | Переводит текст на изображении и возвращает данные изображения в base64. | Опционально, только если указан `output_path` |
| `start_markdown_agent_translation` | Подготавливает фрагменты Markdown для перевода хост-агентом без учетных данных LLM Co-op Translator. | Нет |
| `finish_markdown_agent_translation` | Восстанавливает Markdown из фрагментов, переведённых хост-агентом. | Нет |
| `start_notebook_agent_translation` | Подготавливает фрагменты Markdown-ячeек ноутбука для перевода хост-агентом. | Нет |
| `finish_notebook_agent_translation` | Восстанавливает JSON ноутбука из фрагментов, переведённых хост-агентом. | Нет |
| `rewrite_markdown_paths` | Переписывает пути в теле Markdown и frontmatter для целевого перевода. | Нет |
| `rewrite_notebook_paths` | Переписывает пути внутри Markdown-ячeек ноутбука. | Нет |
| `run_translation` | Выполняет перевод на уровне проекта, как в CLI. | Да, когда `dry_run=false` и `confirm_write=true` |
| `translate_project` | Совместимый псевдоним для `run_translation`. | Да, когда `dry_run=false` и `confirm_write=true` |
| `run_review` | Выполняет детерминированные проверки ревью. | Нет |
| `get_configuration_status` | Отчёт о настроенных провайдерах LLM и Vision без раскрытия секретов. | Нет |
| `list_supported_languages` | Перечисляет поддерживаемые коды целевых языков. | Нет |
| `get_api_overview` | Описывает доступные рабочие процессы и инструменты MCP. | Нет |

## Ресурсы

| URI ресурса | Назначение |
| --- | --- |
| `co-op://api` | JSON-обзор рабочих процессов и инструментов. |
| `co-op://supported-languages` | JSON-список поддерживаемых кодов языков. |
| `co-op://configuration` | JSON-сводка доступности провайдеров без секретов. |

## Подсказки

| Подсказка | Назначение |
| --- | --- |
| `translate_markdown_document_prompt` | Направляет MCP-клиент при переводе содержимого и опциональном переписывании путей. |
| `agent_assisted_markdown_translation_prompt` | Направляет MCP-клиент при переводе Markdown хост-агентом без учетных данных LLM-провайдера Co-op Translator. |
| `translate_repository_prompt` | Направляет MCP-клиент при переводе репозитория с предварительным dry-run. |

## Примеры для копирования

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

Переписать ссылки в переведённом Markdown:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

После того как хост-агент переведёт каждый возвращённый фрагмент, завершите задачу с полным объектом `job`, возвращённым `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Просмотр перевода репозитория:

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
| MCP-клиент не может найти `co-op-translator-mcp`. | Используйте абсолютный путь к исполняемому файлу Python и конфигурацию source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Сервер перечислен, но перевод не выполняется. | Вызовите `get_configuration_status` и убедитесь, что провайдер LLM доступен. |
| Вы хотите перевод Markdown или ноутбука без учетных данных провайдера. | Используйте `start_markdown_agent_translation` / `finish_markdown_agent_translation` или эквивалентные для ноутбука, чтобы хост-агент переводил фрагменты. |
| Перевод изображения не выполняется. | Убедитесь, что переменные Azure AI Vision установлены, и вызовите `get_configuration_status`. |
| Перевод репозитория не записывает файлы. | Устанавливайте `dry_run=false` и `confirm_write=true` только после явного одобрения пользователя. |
| Изменения в конфигурации клиента не отображаются. | Перезапустите или перезагрузите MCP-клиент. |

## Замечания по безопасности

- Вызовы инструментов MCP контролируются моделью хост-приложения, поэтому перевод репозитория по умолчанию выполняется в режиме dry-run.
- Полный перевод репозитория может создать, обновить или удалить множество файлов. Требуйте явного одобрения пользователя перед установкой `confirm_write=true`.
- Инструмент состояния конфигурации никогда не возвращает API-ключи, эндпоинты или другие секретные значения.
- Перевод изображений возвращает данные изображения в base64. Большие изображения могут привести к большим ответам инструмента.
- Инструменты с хост-агентом возвращают исходные фрагменты и подсказки хосту MCP. Используйте их только с содержимым, которое пользователь согласен отправлять модели хост-агента.