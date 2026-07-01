# Довідник CLI

Co-op Translator встановлює такі точки входу командного рядка:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Команди `translate`, `evaluate`, `migrate-links` та `co-op-review` делегуються через `co_op_translator.__main__`, який вибирає реалізацію команди залежно від імені викликаного скрипта. MCP-сервер використовує `co_op_translator.mcp.server` безпосередньо.

Якщо ви вагалися між CLI, Python API та MCP, почніть з [Виберіть робочий процес](workflows.md).

## Послідовність дій при першому використанні CLI

Почніть тут, якщо ви використовуєте Co-op Translator з терміналу:

1. Налаштуйте постачальника LLM, як описано в [Налаштування](configuration.md).
2. Виберіть тип вмісту, який потрібно перекласти.
3. Спочатку запустіть спеціалізовану команду, наприклад переклад тільки Markdown.
4. Використовуйте `--dry-run` перед великими змінами в репозиторії.
5. Використовуйте `co-op-review` після перекладу, щоб перевірити структуру й актуальність.

| Мета | Командa для початку |
| --- | --- |
| Перекласти Markdown-документи | `translate -l "ko" -md` |
| Перекласти ноутбуки | `translate -l "ko" -nb` |
| Перекласти текст на зображеннях | `translate -l "ko" -img` |
| Попередній перегляд роботи без запису файлів | `translate -l "ko" -md --dry-run` |
| Переглянути наявні переклади | `co-op-review -l "ko"` |
| Оновити посилання в ноутбуках і Markdown | `migrate-links -l "ko" --dry-run` |
| Надати доступ до інструментів клієнту MCP | Налаштуйте [Сервер MCP](mcp.md) замість прямого запуску CLI-команд. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Поширені приклади

Тільки переклад Markdown:

```bash
translate -l "de" -md
```

Тільки переклад ноутбуків:

```bash
translate -l "zh-CN" -nb
```

Перекладіть Markdown і зображення:

```bash
translate -l "pt-BR" -md -img
```

Оновити наявні переклади шляхом видалення та повторного створення:

```bash
translate -l "ko" -u
```

Запуск без інтерактивних підказок:

```bash
translate -l "ko ja" -md -y
```

Зберегти логи:

```bash
translate -l "ko" -s
```

### Параметри

| Параметр | Обов'язково | Опис |
| --- | --- | --- |
| `-l`, `--language-codes` | Так | Список кодів мов, розділених пробілом, наприклад `"es fr de"`, або `"all"`. |
| `-r`, `--root-dir` | Ні | Корінь проекту. За замовчуванням — поточний каталог. |
| `-u`, `--update` | Ні | Видалити наявні переклади для вибраних мов і створити їх заново. |
| `-img`, `--images` | Ні | Перекладати тільки файли зображень. |
| `-md`, `--markdown` | Ні | Перекладати тільки файли Markdown. |
| `-nb`, `--notebook` | Ні | Перекладати тільки файли Jupyter notebook. |
| `-d`, `--debug` | Ні | Увімкнути відлагоджувальне логування в консолі. |
| `-s`, `--save-logs` | Ні | Зберегти логи рівня DEBUG у `<root-dir>/logs/`. |
| `-x`, `--fix` | Ні | Переперекласти Markdown-файли з низькою впевненістю на основі попередніх результатів оцінювання. |
| `-c`, `--min-confidence` | Ні | Поріг впевненості для `--fix`. За замовчуванням `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ні | Додати або придушити застереження про машинний переклад. За замовчуванням в CLI увімкнено. |
| `-f`, `--fast` | Ні | Застарілий швидкий режим для зображень. |
| `-y`, `--yes` | Ні | Автоматично підтверджувати підказки, корисно в CI. |
| `--repo-url` | Ні | URL репозиторію, що використовується в рекомендації щодо sparse-checkout у таблиці мов README. |
| `--migrate-language-folders` | Ні | Перейменувати застарілі псевдоніми папок, такі як `cn` або `tw`, у канонічні папки BCP 47. |
| `--dry-run` | Ні | Попередній перегляд міграції папок мов і оцінок перекладу без запису файлів. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Поширені приклади

Використати жорсткіший поріг низької впевненості:

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

### Параметри

| Параметр | Обов'язково | Опис |
| --- | --- | --- |
| `-l`, `--language-code` | Так | Один код мови для оцінки. Псевдонімні коди нормалізуються. |
| `-r`, `--root-dir` | Ні | Корінь проекту. За замовчуванням — поточний каталог. |
| `-c`, `--min-confidence` | Ні | Поріг, який використовується при переліку перекладів з низькою впевненістю. За замовчуванням `0.7`. |
| `-d`, `--debug` | Ні | Увімкнути відлагоджувальне логування. |
| `-s`, `--save-logs` | Ні | Зберегти логи рівня DEBUG у `<root-dir>/logs/`. |
| `-f`, `--fast` | Ні | Тільки оцінювання на основі правил. |
| `-D`, `--deep` | Ні | Тільки оцінювання на основі LLM. |

За замовчуванням `evaluate` використовує як перевірки на основі правил, так і на основі LLM. Результати записуються в метадані перекладу та узагальнюються в консолі.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Поширені приклади

Переглянути переклади корейською та японською з поточного каталогу:

```bash
co-op-review -l "ko ja"
```

Переглянути конкретний корінь проекту:

```bash
co-op-review -l "fr" -r ./my-course
```

Переглянути лише файли джерела, змінені відносно базової ревізії:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Надрукувати вивід у форматі GitHub-flavored Markdown для зведень CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Параметри

| Параметр | Обов'язково | Опис |
| --- | --- | --- |
| `-l`, `--language-code` | Ні | Код мови для перевірки. Може бути переданий кілька разів або як значення, розділене пробілами. За замовчуванням — усі виявлені мови перекладу. |
| `-r`, `--root-dir` | Ні | Корінь проекту. За замовчуванням — поточний каталог. |
| `--changed-from` | Ні | Git ref, який використовується для обмеження перевірки лише до змінених файлів джерела. |
| `--format` | Ні | Формат виводу: `text` або `github`. За замовчуванням — `text`. |

`co-op-review` наразі перевіряє на наявність відсутніх перекладених файлів, відсутні або застарілі метадані перекладу, цілісність frontmatter у Markdown і кодових блоків, недійсний JSON перекладеного ноутбука та відсутні локальні цільові посилання у Markdown або на зображення. Відсутні посилання за замовчуванням є попередженнями; проблеми зі структурою та актуальністю призводять до збою команди.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

Транспорт за замовчуванням — `stdio`. Див. довідник [Сервер MCP](mcp.md) для налаштування клієнта, інструментів, ресурсів та зауважень безпеки.

### Параметри

| Параметр | Обов'язково | Опис |
| --- | --- | --- |
| `--transport` | Ні | Транспорт MCP: `stdio`, `streamable-http`, або `sse`. За замовчуванням — `stdio`. |

## migrate-links

Повторно обробити перекладені файли Markdown і оновити посилання в ноутбуках так, щоб вони вказували на перекладені ноутбуки, коли такі є.

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

Переписувати посилання лише коли перекладені ноутбуки існують:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Параметри

| Параметр | Обов'язково | Опис |
| --- | --- | --- |
| `-l`, `--language-codes` | Так | Коди мов, розділені пробілами, або `"all"`. |
| `-r`, `--root-dir` | Ні | Корінь проекту. За замовчуванням — поточний каталог. |
| `--image-dir` | Ні | Каталог перекладених зображень відносно кореня. За замовчуванням — `translated_images`. |
| `--dry-run` | Ні | Показати файли, які змінилися б, без запису оновлень. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ні | Використовувати оригінальні посилання на ноутбуки, коли перекладені ноутбуки відсутні. За замовчуванням увімкнено. |
| `-d`, `--debug` | Ні | Увімкнути відлагоджувальне логування. |
| `-s`, `--save-logs` | Ні | Зберегти логи рівня DEBUG у `<root-dir>/logs/`. |
| `-y`, `--yes` | Ні | Автоматично підтверджувати підказки при обробці всіх мов. |

## Середовище

Усі команди вимагають один налаштований постачальник LLM:

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
```

Для перекладу зображень додатково потрібна Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Структура виводу

Текстові переклади записуються в:

```text
translations/<language-code>/<original-path>
```

Вивід перекладених зображень записується в:

```text
translated_images/<language-code>/<original-path>
```

Наприклад, переклад `README.md` і `docs/setup.md` корейською мовою призводить до:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Приклади CLI для копіювання

Перекласти Markdown на три мови:

```bash
translate -l "ko ja fr" -md
```

Лише переклад ноутбуків:

```bash
translate -l "zh-CN" -nb
```

Лише переклад зображень:

```bash
translate -l "pt-BR" -img
```

Попередній перегляд перекладу Markdown без запису файлів:

```bash
translate -l "de es" -md --dry-run
```

Виправити переклади Markdown з низькою впевненістю:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Запустити переклад Markdown, дружній до CI:

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