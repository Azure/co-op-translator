# MCP сървър

Co-op Translator включва сървър на Model Context Protocol за агенти, редактори и клиенти, съвместими с MCP.

За подразбиращата се локална конфигурация потребителите не пускат отделен сървър ръчно. Те конфигурират своя MCP клиент, а клиентът стартира `co-op-translator-mcp` автоматично през `stdio`, когато се нуждае от инструментите на Co-op Translator.

Ако се колебаете между CLI, Python API и MCP, започнете с [Изберете вашия работен поток](workflows.md).

Използвайте MCP когато агент или редактор трябва да извика директно Co-op Translator:

| Цел на потребителя | Инструменти в MCP |
| --- | --- |
| Превод на един Markdown документ, тетрадка или изображение | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Превод на Markdown или съдържание на тетрадка с модела на хост агента | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Пренаписване на преведени връзки в Markdown или тетрадка след избора на път за изхода | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Превод на цял репозиториум като при CLI | `run_translation`, `translate_project` |
| Преглед на преведеното съдържание без LLM идентификационни данни | `run_review` |
| Проверка на възможностите и състоянието на средата | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP сървърът обвива същото публично Python API, документирано в [Python API](api.md). Инструментите, базирани на доставчик, използват същите конфигурирани доставчици като CLI и Python API. Инструментите с помощта на агент подготвят фрагменти за хост агента на MCP да ги преведе, след което използват Co-op Translator за реконструиране на финалния Markdown или тетрадка.

## Стъпка 1: Инсталиране и конфигуриране на Co-op Translator

Инсталирайте Co-op Translator в Python средата, която ще използва вашият MCP клиент:

```bash
pip install co-op-translator
```

За локална разработка от това репозитори, инсталирайте пакета в editable режим:

```bash
pip install -e .
```

Изберете режима на превод, който ще използва вашият MCP клиент:

| Режим | Използва се за | Удостоверителни данни |
| --- | --- | --- |
| С доставчик | Co-op Translator извиква `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` или `run_translation`. | За превод са необходими Azure OpenAI, OpenAI или Anthropic. За превод на изображения се изисква и Azure AI Vision. |
| С помощта на агент | Хост агентът на MCP превежда фрагментите, върнати от `start_markdown_agent_translation` или `start_notebook_agent_translation`. | Не са необходими LLM доставчик удостоверителни данни за Co-op Translator за фрагменти от Markdown или тетрадки. Преводът на изображения все още не е покрит от режима с помощта на агент. |

Ако започвате с превод на Markdown или тетрадка вътре в агент като Codex или Claude Code, започнете с режима с помощта на агент. Използвайте режим с доставчик, когато искате самият Co-op Translator да извиква вашите конфигурирани доставчици, когато превеждате изображения или когато извършвате превод на ниво проект като при CLI.

Конфигурирайте един доставчик за работни потоци, базирани на доставчик:

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

За превод на изображения с доставчик допълнително е необходимо:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Режимът с помощта на агент в момента покрива Markdown и Markdown клетки в тетрадки. Преводът на изображения все още използва pipeline-а, базиран на доставчик, и изисква Azure AI Vision за OCR и рендиране, отчитащо оформлението.

## Стъпка 2: Конфигурирайте вашия MCP клиент

За нормалната локална `stdio` конфигурация добавете Co-op Translator към конфигурацията на вашия MCP клиент. Клиентът автоматично ще стартира и спира процеса.

Конфигурация за инсталиран пакет:

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

Конфигурация за source checkout на Windows:

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

Конфигурация за source checkout на macOS или Linux:

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

След промяна на конфигурацията на MCP клиента, рестартирайте или презаредете клиента, за да може да открие новия сървър.

## Стъпка 3: Проверете сървъра в клиента

Помолете MCP клиента да изброи наличните инструменти или първо извикайте един от помощните read-only инструменти:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Полезни първи проверки:

| Инструмент | Какво да проверите |
| --- | --- |
| `get_api_overview` | Потвърждава, че сървърът е достъпен и показва наличните работни потоци. |
| `list_supported_languages` | Потвърждава, че пакетните езикови данни могат да бъдат заредени. |
| `get_configuration_status` | Потвърждава наличността на LLM и Vision доставчици без разкриване на секретни стойности. |

## Стъпка 4: Изберете работен поток

### Превеждане на отделни файлове или документи

Използвайте инструментите, базирани на доставчик, когато MCP клиентът вече има съдържанието на документа или път до изображение и Co-op Translator трябва да извика конфигурираните доставчици за превод.

За Markdown:

1. Извикайте `translate_markdown_content` с `document`, `language_code` и по избор `source_path`.
2. Ако преведеният резултат ще бъде записан в изходната структура на Co-op Translator, извикайте `rewrite_markdown_paths`.
3. Нека клиентът запише или върне финалното `content`.

За тетрадки:

1. Извикайте `translate_notebook_content` с JSON на тетрадката и `language_code`.
2. Извикайте `rewrite_notebook_paths`, ако преведените връзки в тетрадката трябва да бъдат коригирани за целевия път.
3. Запишете или върнете крайния JSON на тетрадката.

За изображения:

1. Извикайте `translate_image_content` с `image_path`, `language_code` и по избор `root_dir` или `fast_mode`.
2. Прочетете върнатите `data_base64` и `mime_type`.
3. Ако е предоставен `output_path`, преведеното изображение също се записва на този път.

Инструментите за съдържание не извършват откриване на проект, актуализации на метаданни, откази за отговорност или автоматично пренаписване на пътища. Ако искате хост агентът да преведе фрагменти от Markdown или тетрадки без удостоверителни данни за LLM доставчик на Co-op Translator, използвайте работния поток с помощта на агент по-долу.

### Превод с модела на хост агента

Използвайте инструментите с помощта на агент, когато искате хост агентът на MCP, като кодиращ помощник, да генерира преведения текст вместо да конфигурирате LLM доставчик за Co-op Translator.

В чат-базиран MCP клиент обикновено не е нужно да пишете JSON за инструменти сами. Помолете агента да използва работния поток с помощта на агент:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

За тетрадки използвайте същия подход:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ако вашият MCP клиент поддържа server prompts, използвайте `agent_assisted_markdown_translation_prompt`, за да накарате клиента да зареди същите инструкции за работния поток.

За Markdown:

1. Извикайте `start_markdown_agent_translation` с `document`, `language_code` и по избор `source_path`.
2. Преведете всеки върнат фрагмент в хост агента, следвайки `prompt` на фрагмента.
3. Извикайте `finish_markdown_agent_translation` с оригиналната `job` и преведените фрагменти, използвайки `chunk_id` и `translated_text`.
4. Ако съдържанието ще бъде записано в преведен целеви път, извикайте `rewrite_markdown_paths`.

За тетрадки:

1. Извикайте `start_notebook_agent_translation` с JSON на тетрадката и `language_code`.
2. Преведете всеки върнат фрагмент в хост агента.
3. Извикайте `finish_notebook_agent_translation` с оригиналната `job` и преведените фрагменти.
4. Извикайте `rewrite_notebook_paths`, ако преведените връзки в тетрадката трябва да бъдат коригирани за целевия път.

Инструментите с помощта на агент не извикват конфигурирания LLM доставчик от Co-op Translator. Хост агентът е отговорен за превода на върнатите фрагменти. Co-op Translator обработва разделянето на Markdown на фрагменти, запазването на заместители, реконструкцията на frontmatter, замяната на клетки в тетрадки и нормализацията след превод.

### Превеждане на цял репозиториум

Използвайте `run_translation`, когато потребителят иска Co-op Translator да се държи като CLI командата `translate`.

Преводът на репозиториум по подразбиране използва `dry_run=true`, за да може агентът да прегледа обхвата преди промени във файловете:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Резултатът от `run_translation` включва масив `events` с версионирани
`co-op.translation.event.v1` събития за напредък. MCP клиентите трябва да използват полета като
`type`, `stage_key`, `completed`, `total` и `current_path` вместо
да парсират улавян текст от конзолата. Подайте `json_events_path`, за да запишете тези събития
в NDJSON файл.

За да разрешите записите, извикващият трябва да зададе както `dry_run=false`, така и `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` е изложен като съвместимостен псевдоним за `run_translation`.

### Преглед на преведеното съдържание

Използвайте `run_review` за детерминирани проверки, които не изискват LLM или Vision удостоверителни данни:

!!! note "Beta"
    MCP излага бета API-то `run_review`. То е безопасно за само-четене (read-only) работни потоци за преглед, но проверките и схемите за проблеми може да се променят.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Резултатът включва улавян текстов изход и структурирано резюме на прегледа, когато е налично.

## Ръчни стартирания на сървъра

Ръчните стартирания са основно за отстраняване на грешки или за транспорти, които се държат като дългоживотни сървъри.

Отстраняване на грешки на подразбиращия се stdio сървър:

```bash
co-op-translator-mcp
```

Стартирайте от source checkout:

```bash
python -m co_op_translator.mcp.server
```

Стартирайте дългоживотен HTTP или SSE сървър:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

За локална интеграция с редактор и агенти предпочитайте конфигурацията, управлявана от клиента `stdio` в Стъпка 2.

## Инструменти

| Инструмент | Цел | Записва файлове |
| --- | --- | --- |
| `translate_markdown_content` | Превежда Markdown низ. | Не |
| `translate_notebook_content` | Превежда Markdown клетки в JSON на тетрадката. | Не |
| `translate_image_content` | Превежда текст в едно изображение и връща base64 данни за изображението. | По избор, само когато е предоставен `output_path` |
| `start_markdown_agent_translation` | Подготвя фрагменти от Markdown за превод от хост агента без удостоверителни данни за LLM доставчик на Co-op Translator. | Не |
| `finish_markdown_agent_translation` | Реконструира Markdown от фрагменти преведени от хост агента. | Не |
| `start_notebook_agent_translation` | Подготвя фрагменти от Markdown клетки в тетрадки за превод от хост агента. | Не |
| `finish_notebook_agent_translation` | Реконструира JSON на тетрадката от фрагменти преведени от хост агента. | Не |
| `rewrite_markdown_paths` | Пренаписва пътища в тялото на Markdown и frontmatter за преведен целеви път. | Не |
| `rewrite_notebook_paths` | Пренаписва пътища вътре в Markdown клетки на тетрадката. | Не |
| `run_translation` | Извършва превод на ниво проект като CLI. | Да, когато `dry_run=false` и `confirm_write=true` |
| `translate_project` | Съвместимостен псевдоним за `run_translation`. | Да, когато `dry_run=false` и `confirm_write=true` |
| `run_review` | Извършва детерминирани проверки за преглед. | Не |
| `get_configuration_status` | Докладва конфигурираните LLM и Vision доставчици без разкриване на секрети. | Не |
| `list_supported_languages` | Изброява поддържаните кодове на целевите езици. | Не |
| `get_api_overview` | Описва наличните MCP работни потоци и инструменти. | Не |

## Ресурси

| Ресурс URI | Цел |
| --- | --- |
| `co-op://api` | JSON преглед на работните потоци и инструментите. |
| `co-op://supported-languages` | JSON списък с поддържани езикови кодове. |
| `co-op://configuration` | JSON обобщение на наличността на доставчиците без секрети. |

## Подсказки

| Подсказка | Цел |
| --- | --- |
| `translate_markdown_document_prompt` | Напътства MCP клиента през превода на съдържанието плюс опционално пренаписване на пътища. |
| `agent_assisted_markdown_translation_prompt` | Напътства MCP клиента през превода на Markdown от хост-агент без удостоверителни данни за LLM доставчик на Co-op Translator. |
| `translate_repository_prompt` | Напътства MCP клиента през превод на репозиториум, започващ първо с dry-run. |

## Примери за копиране и поставяне

Превеждане на Markdown съдържание:

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

Пренаписване на преведени връзки в Markdown:

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

Превеждане на Markdown с модела на хост агента:

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

След като хост агентът преведе всеки върнат фрагмент, завършете задачата с пълния обект `job`, върнат от `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Преглед на превод на репозиториум:

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

## Отстраняване на проблеми

| Проблем | Какво да опитате |
| --- | --- |
| MCP клиентът не може да намери `co-op-translator-mcp`. | Използвайте абсолютния път до изпълнимия Python и конфигурация за source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Сървърът е изброен, но преводът се проваля. | Извикайте `get_configuration_status` и потвърдете, че има наличен LLM доставчик. |
| Искате превод на Markdown или тетрадка без удостоверителни данни на доставчик. | Използвайте `start_markdown_agent_translation` / `finish_markdown_agent_translation` или еквивалентните за тетрадки, за да оставите хост агента да превежда фрагментите. |
| Преводът на изображения се проваля. | Потвърдете, че променливите за Azure AI Vision са зададени и извикайте `get_configuration_status`. |
| Преводът на репозиториум не записва файлове. | Задайте `dry_run=false` и `confirm_write=true` само след изрично одобрение от потребителя. |
| Промените в конфигурацията на клиента не се появяват. | Рестартирайте или презаредете MCP клиента. |

## Бележки за безопасност

- Повикванията на MCP инструментите се контролират от модела в хост приложението, затова преводът на репозиториум е по подразбиране в dry-run.
- Пълният превод на репозиториум може да създаде, актуализира или премахне много файлове. Изисквайте изрично одобрение от потребителя, преди да зададете `confirm_write=true`.
- Инструментът за статус на конфигурацията никога не връща API ключове, крайни точки или други секретни стойности.
- Преводът на изображения връща base64 данни за изображението. Големите изображения могат да произведат големи отговори от инструментите.
- Инструментите с помощта на агент връщат изходни фрагменти и подсказки на хост MCP. Използвайте ги само със съдържание, с което потребителят се чувства комфортно да изпраща към този хост агент модел.