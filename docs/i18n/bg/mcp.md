# MCP сървър

Co-op Translator включва MCP (Model Context Protocol) сървър за агенти, редактори и MCP-съвместими клиенти.

За стандартната локална конфигурация потребителите не поддържат отделен сървър ръчно. Те конфигурират своя MCP клиент и клиентът стартира `co-op-translator-mcp` автоматично по `stdio`, когато се нуждае от инструментите на Co-op Translator.

Ако се колебаете между CLI, Python API и MCP, започнете с [Изберете своя работен процес](workflows.md).

Използвайте MCP, когато агент или редактор трябва директно да извика Co-op Translator:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP сървърът обвива същия публичен Python API, документиран в [Python API](api.md). Инструментите, поддържани от доставчици, използват същите конфигурирани доставчици като CLI и Python API. Инструментите с помощта на агент подготвят парчета (chunks) за MCP хост агента да ги преведе, след което използват Co-op Translator за реконструкция на крайния Markdown или бележник.

## Стъпка 1: Инсталиране и конфигуриране на Co-op Translator

Инсталирайте Co-op Translator в Python средата, която ще използва вашият MCP клиент:

```bash
pip install co-op-translator
```

За локална разработка от това хранилище, инсталирайте пакета в editable режим:

```bash
pip install -e .
```

Изберете режима на превод, който ще използва вашият MCP клиент:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Ако започвате с превод на Markdown или бележници вътре в агент като Codex или Claude Code, започнете с agent-assisted режим. Използвайте provider-backed режим, когато искате самият Co-op Translator да извика конфигурираните доставчици, когато превеждате изображения или когато изпълнявате превод на ниво репозитория като CLI.

Конфигурирайте данните за доставчиците само за provider-backed работни потоци:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed преводът на изображения изисква допълнително:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted режимът в момента покрива Markdown и Markdown клетки в бележниците. Преводът на изображения все още използва provider-backed изображенческия pipeline и изисква Azure AI Vision за OCR и рендиране, което отчита оформлението.

## Стъпка 2: Конфигурирайте вашия MCP клиент

За нормалната локална `stdio` конфигурация добавете Co-op Translator към конфигурацията на вашия MCP клиент. Клиентът ще стартира и спре процеса автоматично.

Конфигуриране за инсталиран пакет:

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

Конфигурация при източников checkout в Windows:

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

Конфигурация при източников checkout в macOS или Linux:

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

След промяна на конфигурацията на MCP клиента, рестартирайте или презаредете клиента, за да открие новия сървър.

## Стъпка 3: Проверете сървъра в клиента

Помолете MCP клиента да изброи наличните инструменти или извикайте един от read-only помощниците първо:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Полезни първи проверки:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Потвърждава, че сървърът е достъпен и показва наличните работни потоци. |
| `list_supported_languages` | Потвърждава, че пакетните данни за езици могат да бъдат заредени. |
| `get_configuration_status` | Потвърждава наличието на LLM и Vision доставчици без да разкрива секретни стойности. |

## Стъпка 4: Изберете работен поток

### Превод на отделни файлове или документи

Използвайте provider-backed инструменти за съдържание, когато MCP клиентът вече разполага със съдържанието на документа или път към изображение и Co-op Translator трябва да извика конфигурираните доставчици.

За Markdown:

1. Извикайте `translate_markdown_content` с `document`, `language_code` и по избор `source_path`.
2. Ако преведеният резултат ще бъде записан в изходен layout на Co-op Translator, извикайте `rewrite_markdown_paths`.
3. Нека клиентът запише или върне крайното `content`.

За бележници:

1. Извикайте `translate_notebook_content` с JSON на бележника и `language_code`.
2. Извикайте `rewrite_notebook_paths` ако преведените връзки в бележника трябва да бъдат коригирани за целев път.
3. Запишете или върнете крайния JSON на бележника.

За изображения:

1. Извикайте `translate_image_content` с `image_path`, `language_code` и по избор `root_dir` или `fast_mode`.
2. Прочетете върнатите `data_base64` и `mime_type`.
3. Ако е предоставен `output_path`, преведеното изображение също се запазва на този път.

Инструментите за съдържание не извършват откриване на проекти, актуализации на метаданни, отказни бележки или автоматично пренаписване на пътища. Ако искате хост агентът да преведе Markdown или парчета от бележник без Co-op Translator LLM доставчик данни, използвайте agent-assisted работния поток по-долу.

### Превод с хост агентния модел

Използвайте agent-assisted инструменти, когато искате MCP хост агентът, като например помощник за програмиране, да произведе преведения текст вместо да конфигурирате Azure OpenAI или OpenAI за Co-op Translator.

В чат-базиран MCP клиент обикновено не е нужно сами да пишете JSON за инструмента. Помолете агента да използва agent-assisted работния поток:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

За бележници използвайте същия модел:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ако вашият MCP клиент поддържа server prompts, използвайте `agent_assisted_markdown_translation_prompt`, за да накарате клиента да зареди същите инструкции за работния поток.

За Markdown:

1. Извикайте `start_markdown_agent_translation` с `document`, `language_code` и по избор `source_path`.
2. Превеждайте всяко върнато парче в хост агента, следвайки парчето `prompt`.
3. Извикайте `finish_markdown_agent_translation` с оригиналната `job` и преведените парчета, използвайки `chunk_id` и `translated_text`.
4. Ако съдържанието ще бъде записано в преведен целев път, извикайте `rewrite_markdown_paths`.

За бележници:

1. Извикайте `start_notebook_agent_translation` с JSON на бележника и `language_code`.
2. Превеждайте всяко върнато парче в хост агента.
3. Извикайте `finish_notebook_agent_translation` с оригиналния `job` и преведените парчета.
4. Извикайте `rewrite_notebook_paths` ако преведените връзки в бележника трябва да бъдат коригирани за целев път.

Agent-assisted инструментите не извикват Azure OpenAI или OpenAI от Co-op Translator. Хост агентът е отговорен за превода на върнатите парчета. Co-op Translator се занимава с chunking на Markdown, запазване на плейсхолдери, реконструкция на frontmatter, замяна на клетки в бележника и нормализиране след превода.

### Превод на цял репозиторий

Използвайте `run_translation`, когато потребителят иска Co-op Translator да се държи като `translate` CLI.

Преводът на репозитория по подразбиране е с `dry_run=true`, така че агентът да може да инспектира обхвата преди промени във файловете:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

За да разрешите запис, извикващият трябва да зададе както `dry_run=false`, така и `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` е изложен като съвместим alias за `run_translation`.

### Преглед на преведеното съдържание

Използвайте `run_review` за детерминирани проверки, които не изискват LLM или Vision креденшъли:

!!! note "Beta"
    MCP излага бета API `run_review`. Той е безопасен за read-only review работни потоци, но проверките за преглед и схемите на проблемите могат да се развиват.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Резултатът включва засечен текстов изход и структурирано обобщение на прегледа, когато е налично.

## Ръчни стартирания на сървъра

Ръчните стартирания са предимно за отстраняване на грешки или за транспортни механизми, които се държат като дълго работещи сървъри.

Отстраняване на грешки в стандартния stdio сървър:

```bash
co-op-translator-mcp
```

Стартиране от източников checkout:

```bash
python -m co_op_translator.mcp.server
```

Стартиране на дълго живеещ HTTP или SSE сървър:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

За локални интеграции с редактори и агенти, предпочитайте client-managed `stdio` конфигурацията от Стъпка 2.

## Инструменти

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

## Подсказки

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Примери за копиране и поставяне

Превод на Markdown съдържание:

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

Пренаписване на преведени Markdown връзки:

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

Превод на Markdown с хост агентния модел:

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

След като хост агентът преведе всяко върнато парче, завършете задачата с пълния `job` обект, върнат от `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Преглед на превод на репозитория:

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

## Отстраняване на неизправности

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Забележки за безопасност

- MCP повикванията на инструменти се контролират от модела на хост приложението, затова преводът на репозитории е по подразбиране dry-run.
- Пълният превод на репозитории може да създаде, актуализира или премахне много файлове. Изисквайте изрично одобрение от потребителя преди задаване на `confirm_write=true`.
- Инструментът за състоянието на конфигурацията никога не връща API ключове, endpoints или други секретни стойности.
- Преводът на изображения връща base64 данни за изображение. Големите изображения могат да произведат големи отговори от инструмента.
- Agent-assisted инструментите връщат изходни парчета и подсказки на MCP хоста. Използвайте ги само със съдържание, с което потребителят се чувства удобно да бъде изпратено към този хост агентен модел.