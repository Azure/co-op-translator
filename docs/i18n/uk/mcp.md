# Сервер MCP

Co-op Translator включає сервер Model Context Protocol для агентів, редакторів та клієнтів, сумісних з MCP.

У типовій локальній конфігурації користувачі не запускають окремий сервер вручну. Вони налаштовують свій MCP-клієнт, і клієнт автоматично запускає `co-op-translator-mcp` через `stdio`, коли потрібні інструменти Co-op Translator.

Якщо ви обираєте між CLI, Python API та MCP, почніть з [Choose Your Workflow](workflows.md).

Використовуйте MCP, коли агент або редактор має викликати Co-op Translator безпосередньо:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Сервер MCP обгортає той самий публічний Python API, задокументований у [Python API](api.md). Інструменти з підтримкою провайдера використовують ті самі налаштовані провайдери, що й CLI та Python API. Інструменти з підтримкою агента готують шматки для перекладу хост-агентом MCP, а потім використовують Co-op Translator для відновлення фінального Markdown або блокнота.

## Крок 1: Встановлення та налаштування Co-op Translator

Встановіть Co-op Translator у Python-середовище, яке використовуватиме ваш MCP-клієнт:

```bash
pip install co-op-translator
```

Для локальної розробки з цього репозиторію встановіть пакет у режимі editable:

```bash
pip install -e .
```

Виберіть режим перекладу, який використовуватиме ваш MCP-клієнт:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Якщо ви починаєте з перекладу Markdown або блокнотів всередині агента, такого як Codex або Claude Code, почніть з режиму з підтримкою агента. Використовуйте режим з підтримкою провайдера, коли ви хочете, щоб сам Co-op Translator викликав налаштованих провайдерів, коли ви перекладаєте зображення, або коли ви виконуєте переклад на рівні репозиторію, як у CLI.

Налаштовуйте облікові дані провайдерів лише для робочих процесів з підтримкою провайдера:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Додатково для перекладу зображень у режимі з підтримкою провайдера потрібне:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Режим з підтримкою агента наразі охоплює Markdown і Markdown-осередки в блокнотах. Переклад зображень досі використовує канал обробки зображень із підтримкою провайдера і вимагає Azure AI Vision для OCR та рендерингу з урахуванням макета.

## Крок 2: Налаштуйте свій MCP-клієнт

Для типової локальної конфігурації `stdio` додайте Co-op Translator до конфігурації вашого MCP-клієнта. Клієнт автоматично запускатиме і зупинятиме процес.

Конфігурація для встановленого пакета:

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

Конфігурація при роботі з репозиторієм на Windows:

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

Конфігурація при роботі з репозиторієм на macOS або Linux:

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

Після зміни конфігурації MCP-клієнта перезапустіть або перезавантажте клієнт, щоб він міг виявити новий сервер.

## Крок 3: Перевірте сервер у клієнті

Попросіть MCP-клієнт перелічити доступні інструменти або спочатку викличте один із допоміжних методів лише для читання:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Корисні початкові перевірки:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Підтверджує, що сервер доступний, і показує доступні робочі процеси. |
| `list_supported_languages` | Підтверджує, що пакети мовних даних можна завантажити. |
| `get_configuration_status` | Підтверджує доступність провайдерів LLM і Vision без розкриття секретних значень. |

## Крок 4: Виберіть робочий процес

### Переклад окремих файлів або документів

Використовуйте інструменти з підтримкою провайдера, коли MCP-клієнт вже має вміст документа або шлях до зображення, і Co-op Translator має викликати налаштованих провайдерів перекладу.

Для Markdown:

1. Викличте `translate_markdown_content` з `document`, `language_code` і, за потреби, `source_path`.
2. Якщо перекладений результат буде записано у вихідну структуру Co-op Translator, викличте `rewrite_markdown_paths`.
3. Дозвольте клієнту записати або повернути остаточний `content`.

Для блокнотів:

1. Викличте `translate_notebook_content` з JSON блокнота і `language_code`.
2. Викличте `rewrite_notebook_paths`, якщо потрібно скорегувати посилання в перекладеному блокноті для цільового шляху.
3. Запишіть або поверніть остаточний JSON блокнота.

Для зображень:

1. Викличте `translate_image_content` з `image_path`, `language_code` і необов’язковими `root_dir` або `fast_mode`.
2. Прочитайте повернені `data_base64` і `mime_type`.
3. Якщо вказано `output_path`, перекладене зображення також буде збережено за цим шляхом.

Інструменти для вмісту не виконують виявлення проекту, оновлення метаданих, дисклеймери або автоматичне переписування шляхів. Якщо ви хочете, щоб хост-агент перекладав шматки Markdown або блокнотів без облікових даних LLM-провайдера Co-op Translator, використовуйте робочий процес з підтримкою агента нижче.

### Переклад за допомогою моделі хост-агента

Використовуйте інструменти з підтримкою агента, коли ви хочете, щоб хост-агент MCP, наприклад асистент кодування, генерував перекладений текст замість налаштування Azure OpenAI або OpenAI для Co-op Translator.

У чат-орієнтованому MCP-клієнті зазвичай не потрібно писати JSON інструменту вручну. Попросіть агента використовувати робочий процес з підтримкою агента:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Для блокнотів використовуйте той самий підхід:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Якщо ваш MCP-клієнт підтримує серверні підказки, використовуйте `agent_assisted_markdown_translation_prompt`, щоб клієнт завантажив ті самі інструкції робочого процесу.

Для Markdown:

1. Викличте `start_markdown_agent_translation` з `document`, `language_code` і, за потреби, `source_path`.
2. Перекладіть кожний повернений шматок у хост-агенті, слідуючи підказці `prompt` для шматка.
3. Викличте `finish_markdown_agent_translation` з оригінальною `job` і перекладеними шматками, використовуючи `chunk_id` і `translated_text`.
4. Якщо вміст буде записано до перекладеної цільової локації, викличте `rewrite_markdown_paths`.

Для блокнотів:

1. Викличте `start_notebook_agent_translation` з JSON блокнота і `language_code`.
2. Перекладіть кожний повернений шматок у хост-агенті.
3. Викличте `finish_notebook_agent_translation` з оригінальною `job` і перекладеними шматками.
4. Викличте `rewrite_notebook_paths`, якщо посилання в перекладених Markdown-осередках блокнота потребують корекції під цільовий шлях.

Інструменти з підтримкою агента не викликають Azure OpenAI або OpenAI з боку Co-op Translator. Хост-агент відповідає за переклад повернених шматків. Co-op Translator обробляє розбиття Markdown на шматки, збереження заповнювачів, реконструкцію frontmatter, заміну осередків блокнота та нормалізацію після перекладу.

### Переклад усього репозиторію

Використовуйте `run_translation`, коли користувач хоче, щоб Co-op Translator поводився як CLI `translate`.

Переклад репозиторію за замовчуванням виконується з `dry_run=true`, щоб агент міг переглянути обсяг змін перед редагуванням файлів:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Щоб дозволити запис, викликачу потрібно встановити як `dry_run=false`, так і `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` надається як сумісна псевдонім для `run_translation`.

### Перегляд перекладеного виводу

Використовуйте `run_review` для детерміністичних перевірок, які не потребують облікових даних LLM або Vision:

!!! note "Beta"
    MCP надає бета-версію API `run_review`. Він безпечний для робочих процесів лише для читання, але перевірки та схеми проблем можуть змінюватися.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Результат включає захоплений текстовий вивід та структурований підсумок огляду, коли він доступний.

## Ручні запуски сервера

Ручні запуски здебільшого призначені для налагодження або для транспортів, які поводяться як довготривалі сервери.

Налагодьте сервер stdio за замовчуванням:

```bash
co-op-translator-mcp
```

Запуск зі зчитуванням джерел:

```bash
python -m co_op_translator.mcp.server
```

Запуск довготривалого HTTP або SSE сервера:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Для локальних інтеграцій редактора та агента надавайте перевагу конфігурації `stdio`, керованій клієнтом у Кроці 2.

## Інструменти

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Ресурси

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Підказки

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Приклади копіювання

Перекласти вміст Markdown:

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

Переписати посилання в перекладеному Markdown:

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

Перекласти Markdown за допомогою моделі хост-агента:

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

Після того як хост-агент перекладе кожний повернений шматок, завершіть задачу з повним об'єктом `job`, який повертається `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Попередній перегляд перекладу репозиторію:

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

## Усунення несправностей

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Зауваги щодо безпеки

- Виклики інструментів MCP контролюються моделлю у хост-застосунку, тому переклад репозиторію за замовчуванням виконується в режимі dry-run.
- Повний переклад репозиторію може створити, оновити або видалити багато файлів. Вимагається явне підтвердження користувача перед встановленням `confirm_write=true`.
- Інструмент стану конфігурації ніколи не повертає API-ключі, кінцеві точки або інші секретні значення.
- Переклад зображень повертає дані зображення у base64. Великі зображення можуть призводити до великих відповідей інструменту.
- Інструменти з підтримкою агента повертають вихідні шматки і підказки хосту MCP. Використовуйте їх лише з вмістом, який користувач готовий пересилати до моделі хост-агента.