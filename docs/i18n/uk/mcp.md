# MCP Server

Co-op Translator включає сервер Model Context Protocol для агентів, редакторів і клієнтів, сумісних із MCP.

Для типової локальної конфігурації користувачі не запускають окремий сервер вручну. Вони налаштовують свій MCP-клієнт, і клієнт автоматично запускає `co-op-translator-mcp` через `stdio`, коли йому потрібні інструменти Co-op Translator.

Якщо ви обираєте між CLI, Python API і MCP, почніть з [Виберіть свій робочий процес](workflows.md).

Використовуйте MCP, коли агент або редактор має викликати Co-op Translator безпосередньо:

| User goal | MCP tools |
| --- | --- |
| Перекласти один документ Markdown, блокнот або зображення | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Перекладати вміст Markdown або блокнота за допомогою моделі хост-агента | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Переписати посилання у перекладеному Markdown або блокноті після вибору шляху виводу | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Перекласти весь репозиторій, як це робить CLI | `run_translation`, `translate_project` |
| Переглянути перекладений результат без облікових даних LLM | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Сервер MCP обгортає той самий публічний Python API, задокументований у [Python API](api.md). Інструменти з підтримкою провайдерів використовують ті самі налаштовані провайдери, що й CLI та Python API. Інструменти за участі агента готують фрагменти для перекладу хост-агентом MCP, а потім використовують Co-op Translator для відновлення остаточного Markdown або блокнота.

## Крок 1: Встановлення та налаштування Co-op Translator

Встановіть Co-op Translator у Python-середовище, яке використовуватиме ваш MCP-клієнт:

```bash
pip install co-op-translator
```

Для локальної розробки з цього репозиторію встановіть пакет у режимі редагування:

```bash
pip install -e .
```

Виберіть режим перекладу, який використовуватиме ваш MCP-клієнт:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Підтримано провайдером | Co-op Translator викликає `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, або `run_translation`. | Для перекладу потрібні Azure OpenAI, OpenAI або Anthropic. Для перекладу зображень також потрібен Azure AI Vision. |
| З підтримкою агента | Агент хоста MCP перекладає блоки, повернені `start_markdown_agent_translation` або `start_notebook_agent_translation`. | Облікові дані провайдера LLM Co-op Translator не потрібні для фрагментів Markdown або ноутбука. Переклад зображень наразі не підтримується в режимі з підтримкою агента. |

Якщо ви починаєте з перекладу Markdown або ноутбуків у середині агента, такого як Codex або Claude Code, почніть з режиму з підтримкою агента. Використовуйте режим із підтримкою провайдера, коли ви хочете, щоб сам Co-op Translator звертався до ваших налаштованих провайдерів, коли ви перекладаєте зображення, або коли ви виконуєте переклад на рівні репозиторію, наприклад через CLI.

Налаштуйте одного провайдера для робочих процесів, що підтримуються провайдером:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Або OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Або Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Для перекладу образу через провайдера додатково потрібно:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Режим з підтримкою агента наразі охоплює Markdown та Markdown-ячейки ноутбуків. Переклад зображень все ще використовує конвеєр з підтримкою провайдера для зображень і вимагає Azure AI Vision для OCR та рендерингу з урахуванням макету.

## Крок 2: Налаштуйте свій MCP-клієнт

Для звичайної локальної конфігурації `stdio` додайте Co-op Translator до конфігурації вашого MCP-клієнта. Клієнт автоматично запускатиме та зупинятиме цей процес.

Installed package configuration:

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

Source checkout configuration on Windows:

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

Налаштування checkout джерела на macOS або Linux:

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

Після зміни конфігурації MCP-клієнта перезапустіть або перезавантажте клієнт, щоб він зміг виявити новий сервер.

## Крок 3: Перевірте сервер у клієнті

Попросіть клієнта MCP перерахувати доступні інструменти або спочатку викличте один із допоміжних засобів тільки для читання:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Useful first checks:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Підтверджує, що сервер досяжний, і показує доступні робочі процеси. |
| `list_supported_languages` | Підтверджує, що упаковані мовні дані можуть бути завантажені. |
| `get_configuration_status` | Підтверджує наявність LLM та провайдера Vision без розкриття секретних значень. |

## Крок 4: Виберіть робочий процес

### Переклад окремих файлів або документів

Використовуйте інструменти контенту, що підтримуються провайдерами, коли клієнт MCP вже має вміст документа або шлях до зображення, і Co-op Translator має викликати налаштованих постачальників перекладу.

For Markdown:

1. Call `translate_markdown_content` with `document`, `language_code`, and optionally `source_path`.
2. Якщо перекладений результат буде записано у вихідний макет Co-op Translator, викличте `rewrite_markdown_paths`.
3. Дозвольте клієнту записати або повернути фінальний `content`.

For notebooks:

1. Call `translate_notebook_content` with notebook JSON and `language_code`.
2. Викличте `rewrite_notebook_paths`, якщо посилання в перекладеному блокноті потрібно відкоригувати для цільового шляху.
3. Запишіть або поверніть фінальний JSON ноутбука.

For images:

1. Call `translate_image_content` with `image_path`, `language_code`, and optional `root_dir` or `fast_mode`.
2. Read the returned `data_base64` and `mime_type`.
3. Якщо надано `output_path`, перекладене зображення також зберігається за цим шляхом.

Інструменти для вмісту не виконують виявлення проєктів, оновлення метаданих, відмови від відповідальності або автоматичне переписування шляхів. Якщо ви хочете, щоб хост-агент перекладав фрагменти Markdown або ноутбуків без облікових даних постачальника Co-op Translator LLM, використайте наведений нижче робочий процес з підтримкою агента.

### Переклад за допомогою моделі хост-агента

Використовуйте інструменти з підтримкою агента, коли ви хочете, щоб хост-агент MCP, наприклад асистент з програмування, створював перекладений текст замість налаштування постачальника LLM для Co-op Translator.

У клієнті MCP на основі чату зазвичай не потрібно писати JSON інструментів самостійно. Попросіть агента використовувати робочий процес з підтримкою агента:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Для ноутбуків використовуйте той самий шаблон:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Якщо ваш клієнт MCP підтримує серверні підказки, використайте `agent_assisted_markdown_translation_prompt`, щоб клієнт завантажив ті самі інструкції робочого процесу.

For Markdown:

1. Call `start_markdown_agent_translation` with `document`, `language_code`, and optionally `source_path`.
2. Перекладіть кожний отриманий фрагмент у хост-агенті, дотримуючись фрагмента `prompt`.
3. Call `finish_markdown_agent_translation` with the original `job` and translated chunks using `chunk_id` and `translated_text`.
4. Якщо вміст буде записано до перекладеного цільового шляху, викличте `rewrite_markdown_paths`.

For notebooks:

1. Call `start_notebook_agent_translation` with notebook JSON and `language_code`.
2. Перекладіть кожен повернений фрагмент у хост-агенті.
3. Call `finish_notebook_agent_translation` with the original `job` and translated chunks.
4. Викличте `rewrite_notebook_paths`, якщо для перекладених посилань у ноутбуці потрібно відкоригувати шлях призначення.

Інструменти з підтримкою агента не викликають налаштованого провайдера LLM із Co-op Translator. Хост-агент відповідає за переклад повернутих фрагментів. Co-op Translator обробляє розбиття Markdown на фрагменти, збереження заповнювачів, відновлення frontmatter, заміну клітинок нотатника та пост-перекладну нормалізацію.

### Перекласти весь репозиторій

Використовуйте `run_translation`, коли користувач хоче, щоб Co-op Translator поводився як CLI `translate`.

Переклад репозиторію за замовчуванням встановлений на `dry_run=true`, щоб агент міг переглянути область перед змінами файлів:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` result includes an `events` array with versioned
`co-op.translation.event.v1` progress events. MCP clients should use fields such
as `type`, `stage_key`, `completed`, `total`, and `current_path` instead of
parsing captured console text. Pass `json_events_path` to also write those events
to an NDJSON file.

Щоб дозволити запис, викликач має встановити обидва `dry_run=false` та `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` доступний як сумісний псевдонім для `run_translation`.

### Перегляд перекладеного виводу

Використовуйте `run_review` для детермінованих перевірок, які не потребують облікових даних для LLM або Vision:

!!! note "Бета"
    MCP надає бета-версію API `run_review`. Воно безпечне для робочих процесів перегляду лише для читання, але перевірки перегляду та схеми проблем можуть змінюватися.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Результат включає захоплений текстовий вивід і структурований підсумок перегляду, коли він доступний.

## Ручні запуски сервера

Ручні прогони призначені переважно для налагодження або для транспортів, що поводяться як довго працюючі сервери.

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

Запустіть довготривалий HTTP або SSE сервер:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Для локальних інтеграцій редактора та агента віддавайте перевагу конфігурації `stdio`, керованій клієнтом, у кроці 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Перекладати Markdown-клітинки у JSON блокнота. | Ні |
| `translate_image_content` | Перекласти текст на одному зображенні та повернути дані зображення у форматі base64. | Необов'язково, тільки коли надано `output_path` |
| `start_markdown_agent_translation` | Підготувати фрагменти Markdown для перекладу хост-агентом без облікових даних LLM Co-op Translator. | Ні |
| `finish_markdown_agent_translation` | Відновити Markdown із фрагментів, перекладених хост-агентом. | Ні |
| `start_notebook_agent_translation` | Підготувати фрагменти Markdown-клітинок ноутбука для перекладу хост-агентом. | Ні |
| `finish_notebook_agent_translation` | Відновити JSON блокнота з фрагментів, перекладених хост-агентом. | Ні |
| `rewrite_markdown_paths` | Переписати тіло Markdown і шляхи у frontmatter для цільового перекладу. | Ні |
| `rewrite_notebook_paths` | Переписувати шляхи всередині Markdown-клітинок блокнота. | Ні |
| `run_translation` | Запускати переклад на рівні проєкту, як у CLI. | Так, коли `dry_run=false` та `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Повідомляти про налаштованих провайдерів LLM і Vision, не розкриваючи секретів. | Ні |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Описати доступні робочі процеси та інструменти MCP. | Ні |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | Огляд робочих процесів та інструментів у форматі JSON. |
| `co-op://supported-languages` | Список підтримуваних кодів мов у форматі JSON. |
| `co-op://configuration` | Підсумок доступності провайдерів у форматі JSON без секретних даних. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Провести клієнта MCP через переклад вмісту з опційним переписуванням шляхів. |
| `agent_assisted_markdown_translation_prompt` | Провести клієнта MCP через переклад Markdown хост-агентом без облікових даних провайдера LLM Co-op Translator. |
| `translate_repository_prompt` | Провести клієнта MCP через переклад репозиторію з попереднім тестовим запуском (dry-run). |

## Приклади для копіювання та вставлення

Translate Markdown content:

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

Rewrite translated Markdown links:

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

Перекладайте Markdown за допомогою моделі хост-агента:

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

Після того, як хост-агент перекладе кожен повернутий фрагмент, завершіть задачу повним об'єктом `job`, який повертає `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| Клієнт MCP не може знайти `co-op-translator-mcp`. | Використовуйте абсолютний шлях до виконуваного файлу Python та конфігурацію перевірки вихідного коду `["-m", "co_op_translator.mcp.server"]`. |
| Сервер зазначений, але переклад не вдається. | Викличте `get_configuration_status` та переконайтеся, що провайдер LLM доступний. |
| Ви хочете переклад Markdown або ноутбука без облікових даних провайдера. | Використовуйте `start_markdown_agent_translation` / `finish_markdown_agent_translation` або еквіваленти для ноутбука, щоб хост-агент переклав фрагменти. |
| Не вдається перекласти зображення. | Переконайтеся, що змінні Azure AI Vision встановлені, і викличте `get_configuration_status`. |
| Переклад репозиторію не записує файли. | Встановлюйте `dry_run=false` та `confirm_write=true` лише після явного дозволу користувача. |
| Зміни в конфігурації клієнта не відображаються. | Перезапустіть або перезавантажте клієнт MCP. |

## Зауваження щодо безпеки

- Виклики інструментів MCP контролюються моделлю хост-застосунку, тому переклад репозиторію за замовчуванням виконується у режимі пробного запуску.
- Повний переклад репозиторію може створити, оновити або видалити багато файлів. Потрібно отримати явну згоду користувача перед встановленням `confirm_write=true`.
- Інструмент стану конфігурації ніколи не повертає API-ключі, кінцеві точки або інші секретні значення.
- Переклад зображення повертає дані зображення у форматі base64. Великі зображення можуть призвести до великих відповідей інструментів.
- Інструменти за участю агента повертають фрагменти джерел та підказки хосту MCP. Використовуйте їх лише з вмістом, який користувач готовий надсилати цій моделі агента хоста.
