# CLI референца

Co-op Translator инсталира следеће улазне тачке командне линије:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [Изаберите свој радни ток](workflows.md).

## Први кораци са CLI

Почните овде ако користите Co-op Translator из терминала:

1. Конфигуришите LLM провајдера као што је описано у [Конфигурација](configuration.md).
2. Изаберите тип садржаја који желите да преведете.
3. Покрените фокусирану команду прво, на пример превод само Markdown фајлова.
4. Користите `--dry-run` пре већих промена у репозиторијуму.
5. Користите `co-op-review` након превода да бисте проверили структуру и актуелност.

| Циљ | Команда за почетак |
| --- | --- |
| Превести Markdown документе | `translate -l "ko" -md` |
| Превести notebook-ове | `translate -l "ko" -nb` |
| Превести текст на сликама | `translate -l "ko" -img` |
| Прегледајте рад без записивања фајлова | `translate -l "ko" -md --dry-run` |
| Преглед постојећих превода | `co-op-review -l "ko"` |
| Ажурирати линкове у notebook-има и Markdown-у | `migrate-links -l "ko" --dry-run` |
| Изложити алате MCP клијенту | Конфигуришите [MCP сервер](mcp.md) уместо да покрећете CLI команде директно. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Уобичајени примери

Превести само Markdown:

```bash
translate -l "de" -md
```

Превести само notebook-ове:

```bash
translate -l "zh-CN" -nb
```

Превести Markdown и слике:

```bash
translate -l "pt-BR" -md -img
```

Ажурирати постојеће преводе брисањем и поновним креирањем:

```bash
translate -l "ko" -u
```

Покренути без интерактивних упита:

```bash
translate -l "ko ja" -md -y
```

Сачувати логове:

```bash
translate -l "ko" -s
```

### Опције

| Опција | Обавезно | Опис |
| --- | --- | --- |
| `-l`, `--language-codes` | Да | Размаком одвојени кодови језика, као на пример `"es fr de"`, или `"all"`. |
| `-r`, `--root-dir` | Не | Корен пројекта. Подразумевано је тренутни директоријум. |
| `-u`, `--update` | Не | Обриши постојеће преводе за изабране језике и поново их креира. |
| `-img`, `--images` | Не | Преведи само фајлове са сликама. |
| `-md`, `--markdown` | Не | Преведи само Markdown фајлове. |
| `-nb`, `--notebook` | Не | Преведи само Jupyter notebook фајлове. |
| `-d`, `--debug` | Не | Омогући debug логовање у конзоли. |
| `-s`, `--save-logs` | Не | Сачувај DEBUG-ниво логова у `<root-dir>/logs/`. |
| `-x`, `--fix` | Не | Поново преведи Markdown фајлове са ниским поверењем на основу претходних резултата процене. |
| `-c`, `--min-confidence` | Не | Праг поверења за `--fix`. Подразумевано је `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Не | Додај или ускрати одрицање од одговорности за машински превод. Подразумевано омогућено у CLI-ју. |
| `-f`, `--fast` | Не | Застарели брзи режим за слике. |
| `-y`, `--yes` | Не | Аутоматски потврђује упите, корисно у CI-у. |
| `--repo-url` | Не | URL репозиторијума који се користи у скупим саветима за табелу језика у README-у. |
| `--migrate-language-folders` | Не | Преименујте застареле алтернативне фасцикле, као `cn` или `tw`, у канонске BCP 47 фасцикле. |
| `--dry-run` | Не | Прикажи миграцију фасцикли језика и процене превода без писања фајлова. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Експериментално"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Уобичајени примери

Use a stricter low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Опције

| Опција | Обавезно | Опис |
| --- | --- | --- |
| `-l`, `--language-code` | Да | Један код језика који се процењује. Алијас кодови се нормализују. |
| `-r`, `--root-dir` | Не | Корен пројекта. Подразумевано је тренутни директоријум. |
| `-c`, `--min-confidence` | Не | Праг који се користи приликом навођења превода са ниским поверењем. Подразумевано `0.7`. |
| `-d`, `--debug` | Не | Омогући debug логовање. |
| `-s`, `--save-logs` | Не | Сачувај DEBUG-ниво логова у `<root-dir>/logs/`. |
| `-f`, `--fast` | Не | Само правило-базирана процена. |
| `-D`, `--deep` | Не | Само LLM-базирана процена. |

Подразумевано, `evaluate` користи и правило-базиране и LLM-базиране процене. Резултати се записују у метаподатке превода и сумирани су у конзоли.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Бета"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Уобичајени примери

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Опције

| Опција | Обавезно | Опис |
| --- | --- | --- |
| `-l`, `--language-code` | Не | Код језика за преглед. Може се проследити више пута или као вредност раздвојена размаком. Подразумевано сви откривени језици превода. |
| `-r`, `--root-dir` | Не | Корен пројекта. Подразумевано је тренутни директоријум. |
| `--changed-from` | Не | Git референца која се користи за ограничење прегледа на измењене изворне фајлове. |
| `--format` | Не | Формат излаза: `text` или `github`. Подразумевано `text`. |

`co-op-review` тренутно проверава за недостајуће преведене фајлове, недостајуће или застареле метаподатке превода, интегритет frontmatter-а и code fence-ова у Markdown-у, неважећи преведени JSON notebook-а и недостајуће локалне Markdown или image линкове. Недостајући линкови су по подразумеваној вредности упозорења; структурни и проблеми са актуелношћу изазивају неуспех команде.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP сервер](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Опције

| Опција | Обавезно | Опис |
| --- | --- | --- |
| `--transport` | Не | MCP transport: `stdio`, `streamable-http`, or `sse`. Подразумевано `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Уобичајени примери

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Опције

| Опција | Обавезно | Опис |
| --- | --- | --- |
| `-l`, `--language-codes` | Да | Размаком одвојени кодови језика, или `"all"`. |
| `-r`, `--root-dir` | Не | Корен пројекта. Подразумевано је тренутни директоријум. |
| `--image-dir` | Не | Директоријум преведених слика релативан у односу на корен. Подразумевано `translated_images`. |
| `--dry-run` | Не | Прикажи фајлове који би се променили без писања измена. |
| `--fallback-to-original`, `--no-fallback-to-original` | Не | Користи оригиналне линкове ка notebook-има када преведени notebook-ови недостају. Омогућено по подразумеваној вредности. |
| `-d`, `--debug` | Не | Омогући debug логовање. |
| `-s`, `--save-logs` | Не | Сачувај DEBUG-ниво логова у `<root-dir>/logs/`. |
| `-y`, `--yes` | Не | Аутоматски потврђује упите при обради свих језика. |

## Окружење

Све команде захтевају један конфигурисан LLM провајдер:

```bash
# Ажур ОпенАИ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Или ОпенАИ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Излазна структура

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

## CLI примери које можете копирати и налепити

Превести Markdown на три језика:

```bash
translate -l "ko ja fr" -md
```

Превести само notebook-ове:

```bash
translate -l "zh-CN" -nb
```

Превести само слике:

```bash
translate -l "pt-BR" -img
```

Прегледати превод Markdown-а без записивања фајлова:

```bash
translate -l "de es" -md --dry-run
```

Поправити преводе Markdown-а са ниским поверењем:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Покренути CI-пријатељски превод Markdown-а:

```bash
translate -l "ko ja" -md -y -s
```

Прегледати преведени садржај:

```bash
co-op-review -l "ko ja"
```

Прегледати миграцију линкова:

```bash
migrate-links -l "ko" --dry-run
```