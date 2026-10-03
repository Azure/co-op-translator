# Довідник CLI

Co-op Translator встановлює ці точки входу командного рядка:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Команди `translate`, `evaluate`, `migrate-links` і `co-op-review` делегують виконання через `co_op_translator.__main__`, який обирає реалізацію команди на основі імені викликаного скрипта. MCP-сервер використовує `co_op_translator.mcp.server` безпосередньо.

Якщо ви вагаєтесь між CLI, Python API та MCP, почніть з [Вибору робочого процесу](workflows.md).

## Вивід консолі

Інтерактивні термінали використовують форматування Rich для заголовка команди, індикаторів прогресу та підсумків. CI та неінтерактивний вивід автоматично повертаються до простого тексту.

Встановіть `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain`, щоб примусово виводити простий текст, або `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich`, щоб примусово використовувати Rich. Встановіть `CO_OP_TRANSLATOR_NO_PROGRESS=1`, щоб зберегти підсумки та приховати живі смуги прогресу.

Використовуйте `translate --json-events progress.ndjson`, коли іншій системі потрібен машинозчитуваний прогрес. CLI продовжує відображати інформацію для людей, у той час як NDJSON-файл отримує версіоновані події `co-op.translation.event.v1` зі стабільними полями, такими як `type`, `stage_key`, `completed`, `total` і `current_path`.





## Потік першого запуску CLI

Почніть тут, якщо ви використовуєте Co-op Translator з терміналу:

1. Налаштуйте постачальника LLM, як описано в [Configuration](configuration.md).
2. Виберіть тип вмісту, який ви хочете перекласти.
3. Спочатку запустіть цільову команду, наприклад, лише переклад Markdown.
4. Використовуйте `--dry-run` перед масштабними змінами в репозиторії.
5. Використовуйте `co-op-review` після перекладу, щоб перевірити структуру та актуальність.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Надати інструменти клієнту MCP | Налаштуйте [сервер MCP](mcp.md) замість безпосереднього виконання команд CLI. |

## translate

Перекладає файли Markdown, блокноти та текст на зображеннях на одну або кілька цільових мов.

```bash
translate -l "ko ja fr"
```

### Поширені приклади

Перекласти лише Markdown:

```bash
translate -l "de" -md
```

Перекласти лише блокноти:

```bash
translate -l "zh-CN" -nb
```

Перекласти Markdown та зображення:

```bash
translate -l "pt-BR" -md -img
```

Оновити існуючі переклади шляхом їх видалення та повторного створення:

```bash
translate -l "ko" -u
```

Запустити без інтерактивних підказок:

```bash
translate -l "ko ja" -md -y
```

Зберегти журнали:

```bash
translate -l "ko" -s
```

Записати структуровані події прогресу:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Так | Коди мов, розділені пробілами, наприклад `"es fr de"`, або `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | Ні | Видалити існуючі переклади для вибраних мов і створити їх заново. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | Ні | Увімкнути налагоджувальне логування в консолі. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `--json-events` | Ні | Записувати події прогресу перекладу у машинозчитуваному вигляді у форматі NDJSON. |
| `-x`, `--fix` | Ні | Повторно перекласти файли Markdown з низькою довірою на основі результатів попередньої оцінки. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ні | Додавати або приховувати застереження щодо машинного перекладу. За замовчуванням увімкнено в CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | Ні | Автоматично підтверджувати запити, корисно у CI. |
| `--repo-url` | Ні | URL репозиторію, який використовується в попередженні таблиці мов у README щодо sparse-checkout. |
| `--migrate-language-folders` | Ні | Перейменувати застарілі папки-аліаси, такі як `cn` або `tw`, на канонічні папки BCP 47. |
| `--dry-run` | Ні | Попередній перегляд міграції папок мов і оцінок перекладу без запису файлів. |

Якщо не вказано прапорець типу, `translate` обробляє Markdown, блокноти та зображення. Для перекладу зображень потрібна конфігурація Azure AI Vision.

## evaluate

Оцінює якість перекладів Markdown для однієї мови.

!!! warning "Experimental"
    `evaluate` є експериментальним. Він може використовувати перевірки на основі правил і на основі LLM, записує результати оцінки в метадані перекладу, і його модель оцінювання та поведінка метаданих можуть змінюватися.

```bash
evaluate -l "ko"
```

### Поширені приклади

Використати жорсткіший поріг для низької довіри:

```bash
evaluate -l "es" -c 0.8
```

Запустити лише перевірки на основі правил:

```bash
evaluate -l "fr" -f
```

Запустити лише перевірки на основі LLM:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | Ні | Поріг, який використовується при переліку перекладів з низькою довірою. За замовчуванням `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

За замовчуванням `evaluate` використовує як перевірки на основі правил, так і на основі LLM. Результати записуються в метадані перекладу та підсумовуються в консолі.

## co-op-review

Запустіть детерміністичні перевірки обслуговування перекладів без облікових даних API.

!!! note "Beta"
    `co-op-review` — це бета-версія детерміністичної команди огляду. Вона не викликає постачальників моделей і не записує файли, але її перевірки та схема виводу проблем можуть змінюватися.

```bash
co-op-review -l "ko"
```

### Поширені приклади

Переглянути переклади корейською та японською з поточної директорії:

```bash
co-op-review -l "ko ja"
```

Переглянути конкретний корінь проекту:

```bash
co-op-review -l "fr" -r ./my-course
```

Переглянути лише README після перекладу тільки README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ігнорує інші документи та вкладені README. Він завершується із помилкою, якщо кореневий
`README.md` відсутній. У поєднанні з `--changed-from` він переглядає лише README
коли цей вихідний файл було змінено. Переклад тільки README залишає вихідний README
незмінним, включно з будь-якими маркерами спільних секцій.

Переглянути лише вихідні файли, змінені відносно базового ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Надрукувати вивід у форматі GitHub-flavored Markdown для підсумків CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Ні | Код мови для перевірки. Може передаватися кілька разів або як значення, розділене пробілами. За замовчуванням — всі виявлені мови перекладу. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref, що використовується для обмеження перегляду змінених вихідних файлів. |
| `--readme-only` | No | Review only the root `README.md` translation. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` наразі перевіряє на відсутність перекладених файлів, відсутні або застарілі метадані перекладу, цілісність Markdown frontmatter та блоків коду, недійсний JSON перекладених блокнотів та відсутні локальні цільові посилання Markdown або зображень. Відсутні посилання за замовчуванням є попередженнями; проблеми зі структурою та актуальністю спричиняють помилку команди.

## co-op-translator-mcp

Запустіть MCP-сервер Co-op Translator для агентів, редакторів та MCP-сумісних клієнтів.

```bash
co-op-translator-mcp
```

Транспорт за замовчуванням — `stdio`. Див. посібник [MCP Server](mcp.md) для налаштування клієнта, інструментів, ресурсів та зауважень щодо безпеки.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Повторно обробляє перекладені файли Markdown і оновлює посилання в блокнотах, щоб вони вказували на перекладені блокноти, коли такі доступні.

```bash
migrate-links -l "ko ja"
```

### Поширені приклади

Попередній перегляд оновлень посилань:

```bash
migrate-links -l "ko" --dry-run
```

Обробити всі підтримувані мови без підтвердження:

```bash
migrate-links -l "all" -y
```

Переписувати посилання лише коли існують перекладені блокноти:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | No | Каталог перекладених зображень відносно кореня. За замовчуванням — `translated_images`. |
| `--dry-run` | No | Показувати файли, які змінилися б без запису оновлень. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ні | Використовувати посилання на оригінальні ноутбуки, коли перекладені ноутбуки відсутні. Увімкнено за замовчуванням. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Автоматично підтверджувати запити під час обробки всіх мов. |

## Environment

Коли команда вимагає облікових даних постачальника, налаштуйте один із цих наборів постачальників. `translate --dry-run` і `co-op-review` не вимагають облікових даних постачальника:

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

Переклад зображень додатково вимагає Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Структура виводу

Текстові переклади записуються під:

```text
translations/<language-code>/<original-path>
```

Вивід перекладених зображень записується під:

```text
translated_images/<language-code>/<original-path>
```

Наприклад, переклад `README.md` і `docs/setup.md` корейською створює:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Приклади CLI для копіювання та вставки

Перекласти Markdown на три мови:

```bash
translate -l "ko ja fr" -md
```

Перекласти лише блокноти:

```bash
translate -l "zh-CN" -nb
```

Перекласти лише зображення:

```bash
translate -l "pt-BR" -img
```

Попередній перегляд перекладу Markdown без запису файлів:

```bash
translate -l "de es" -md --dry-run
```

Виправити переклади Markdown з низькою довірою:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Запустити CI-дружній переклад Markdown:

```bash
translate -l "ko ja" -md -y -s
```

Переглянути перекладений вивід:

```bash
co-op-review -l "ko ja"
```

Попередній перегляд міграції посилань:

```bash
migrate-links -l "ko" --dry-run
```