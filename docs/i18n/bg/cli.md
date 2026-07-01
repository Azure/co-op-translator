# CLI справочник

Co-op Translator инсталира следните командни входни точки:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Командите `translate`, `evaluate`, `migrate-links` и `co-op-review` се изпълняват чрез `co_op_translator.__main__`, който избира реализацията на командата въз основа на името на извикания скрипт. MCP сървърът използва `co_op_translator.mcp.server` директно.

Ако се колебаете между CLI, Python API и MCP, започнете с [Choose Your Workflow](workflows.md).

## Първи стъпки с CLI

Започнете тук, ако използвате Co-op Translator от терминал:

1. Конфигурирайте доставчик на LLM, както е описано в [Configuration](configuration.md).
2. Изберете типа съдържание, което искате да превеждате.
3. Стартирайте фокусирана команда първо, например превод само на Markdown.
4. Използвайте `--dry-run` преди големи промени в хранилището.
5. Използвайте `co-op-review` след превода, за да проверите структурата и актуалността.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Често срещани примери

Превеждане само на Markdown:

```bash
translate -l "de" -md
```

Превеждане само на notebooks:

```bash
translate -l "zh-CN" -nb
```

Превеждане на Markdown и изображения:

```bash
translate -l "pt-BR" -md -img
```

Актуализиране на съществуващи преводи чрез изтриване и пресъздаване:

```bash
translate -l "ko" -u
```

Изпълнение без интерактивни подсказки:

```bash
translate -l "ko ja" -md -y
```

Запазване на логове:

```bash
translate -l "ko" -s
```

### Опции

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Езикови кодове, разделени с интервал, например `"es fr de"`, или `"all"`. |
| `-r`, `--root-dir` | No | Корен на проекта. По подразбиране е текущата директория. |
| `-u`, `--update` | No | Изтрива съществуващите преводи за избраните езици и ги пресъздава. |
| `-img`, `--images` | No | Превежда само файлове с изображения. |
| `-md`, `--markdown` | No | Превежда само Markdown файлове. |
| `-nb`, `--notebook` | No | Превежда само Jupyter notebook файлове. |
| `-d`, `--debug` | No | Активира debug логване в конзолата. |
| `-s`, `--save-logs` | No | Запазва логове с ниво DEBUG под `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Превежда отново Markdown файлове с ниско доверие въз основа на предишните резултати от оценката. |
| `-c`, `--min-confidence` | No | Праг за доверие при `--fix`. По подразбиране `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Добавя или премахва предупреждение за машинен превод. По подразбиране е включено в CLI. |
| `-f`, `--fast` | No | Остарял бърз режим за изображения. |
| `-y`, `--yes` | No | Автоматично потвърждава подсказки, полезно за CI. |
| `--repo-url` | No | URL на хранилището, използван в таблицата с езици в README за съвет по sparse-checkout. |
| `--migrate-language-folders` | No | Преименува наследени алтернативни папки, като `cn` или `tw`, в канонични BCP 47 папки. |
| `--dry-run` | No | Преглед на миграцията на папки с езици и оценки за превода без записване на файлове. |

Ако не е зададен флаг за тип, `translate` обработва Markdown, notebooks и изображения. Преводът на изображения изисква конфигурация на Azure AI Vision.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Експериментално"
    `evaluate` е експериментална команда. Може да използва проверки, базирани на правила, и проверки, базирани на LLM; записва резултатите от оценката в метаданните за превода и моделът за оценяване и поведението на метаданните могат да се променят.

```bash
evaluate -l "ko"
```

### Често срещани примери

Използване на по-строг праг за ниско доверие:

```bash
evaluate -l "es" -c 0.8
```

Изпълнение само на проверки, базирани на правила:

```bash
evaluate -l "fr" -f
```

Изпълнение само на проверки, базирани на LLM:

```bash
evaluate -l "ja" -D
```

### Опции

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Един езиков код за оценка. Алиас кодовете се нормализират. |
| `-r`, `--root-dir` | No | Корен на проекта. По подразбиране е текущата директория. |
| `-c`, `--min-confidence` | No | Праг, използван при изброяване на преводи с ниско доверие. По подразбиране `0.7`. |
| `-d`, `--debug` | No | Активира debug логване. |
| `-s`, `--save-logs` | No | Запазва логове с ниво DEBUG под `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Само оценка, базирана на правила. |
| `-D`, `--deep` | No | Само оценка, базирана на LLM. |

По подразбиране `evaluate` използва както оценки, базирани на правила, така и оценки, базирани на LLM. Резултатите се записват в метаданните за превода и се обобщават в конзолата.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Бета"
    `co-op-review` е бета команда за детерминистичен преглед. Тя не извиква доставчици на модели и не записва файлове, но нейните проверки и схемата за извеждане на проблеми могат да се развиват.

```bash
co-op-review -l "ko"
```

### Често срещани примери

Преглед на корейски и японски преводи от текущата директория:

```bash
co-op-review -l "ko ja"
```

Преглед на конкретен корен на проекта:

```bash
co-op-review -l "fr" -r ./my-course
```

Преглед само на изходните файлове, променени спрямо базов ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Отпечатване на изход във формат GitHub-flavored Markdown за CI обобщения:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Опции

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Езиков код за преглед. Може да се подаде многократно или като стойност, разделена с интервали. По подразбиране всички открити езици за превод. |
| `-r`, `--root-dir` | No | Корен на проекта. По подразбиране е текущата директория. |
| `--changed-from` | No | Git ref, използван за ограничаване на прегледа до променените изходни файлове. |
| `--format` | No | Формат на изхода: `text` или `github`. По подразбиране `text`. |

`co-op-review` в момента проверява за липсващи преведени файлове, липсващи или неактуални метаданни за превода, целостта на Markdown frontmatter и code fence, невалиден преведен notebook JSON и липсващи локални Markdown или image цели на връзките. Липсващите връзки са предупреждения по подразбиране; структурните и проблемите с актуалността водят до провал на командата.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP транспорт: `stdio`, `streamable-http`, или `sse`. По подразбиране `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Често срещани примери

Преглед на актуализации на връзки:

```bash
migrate-links -l "ko" --dry-run
```

Обработване на всички поддържани езици без потвърждение:

```bash
migrate-links -l "all" -y
```

Пренаписване на връзки само когато съществуват преведени notebooks:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Опции

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Езикови кодове, разделени с интервал, или `"all"`. |
| `-r`, `--root-dir` | No | Корен на проекта. По подразбиране е текущата директория. |
| `--image-dir` | No | Папка за преведени изображения спрямо корена. По подразбиране `translated_images`. |
| `--dry-run` | No | Показва файловете, които биха се променили, без да записва актуализации. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Използва оригиналните notebook връзки, когато преведени notebooks липсват. По подразбиране е разрешено. |
| `-d`, `--debug` | No | Активира debug логване. |
| `-s`, `--save-logs` | No | Запазва логове с ниво DEBUG под `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Автоматично потвърждава подсказки при обработка на всички езици. |

## Environment

All commands require one configured LLM provider:

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
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Изходна структура

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Примери за копиране и поставяне в CLI

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Preview Markdown translation without writing files:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```