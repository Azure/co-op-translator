# MCP Server

Co-op Translator укључује Model Context Protocol сервер за агенте, уређиваче и MCP-компатибилне клијенте.

За подразумевану локалну конфигурацију, корисници не морају ручно да покрећу посебан сервер. Конфигуришу свој MCP клијент, а клијент аутоматски покреће `co-op-translator-mcp` преко `stdio` када му затребају алати Co-op Translator-а.

Ако одлучујете између CLI, Python API и MCP, почните са [Choose Your Workflow](workflows.md).

Користите MCP када агент или уређивач треба да позове Co-op Translator директно:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP сервер омотава исти јавни Python API који је документован у [Python API](api.md). Алатке које користе провајдере користе исте конфигурисане провајдере као CLI и Python API. Алатке помоћу агента припремају делове за MCP host агента да их преведе, а затим користе Co-op Translator да реконструишу коначни Markdown или ноутбук.

## Step 1: Install and Configure Co-op Translator

Инсталирајте Co-op Translator у Python окружење које ће ваш MCP клијент користити:

```bash
pip install co-op-translator
```

За локални развој из овог репозиторијума, инсталирајте пакет у edit-овом режиму:

```bash
pip install -e .
```

Изаберите режим превођења који ће ваш MCP клијент користити:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator позива `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, или `run_translation`. | Превођење Markdown-а и notebook-а захтева Azure OpenAI или OpenAI. За превођење слика је потребан и Azure AI Vision. |
| Agent-assisted | MCP host агент преводи делове које врати `start_markdown_agent_translation` или `start_notebook_agent_translation`. | За Markdown или notebook делове нису потребне Co-op Translator LLM провајдер акредитиве. Превођење слика још није покривено agent-assisted режимом. |

Ако почињете са превођењем Markdown-а или notebook-а унутар агента као што су Codex или Claude Code, почните са agent-assisted режимом. Користите provider-backed режим када желите да Co-op Translator сам позива ваше конфигурисане провајдере, када преводите слике, или када покрећете превођење целог репозиторијума као CLI.

Конфигуришите акредитиве провајдера само за provider-backed токове:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

За provider-backed превођење слика додатно је потребно:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted режим тренутно покрива Markdown и ноутбук Markdown ћелије. Превођење слика и даље користи pipeline са провајдером и захтева Azure AI Vision за OCR и рендеровање са очувањем распореда.

## Step 2: Configure Your MCP Client

За нормалну локалну `stdio` конфигурацију, додајте Co-op Translator у вашу MCP client конфигурацију. Клијент ће аутоматски покретати и заустављати процес.

Инсталациони пакет конфигурација:

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

Конфигурација извора (source checkout) на Windows:

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

Конфигурација извора на macOS или Linux:

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

Након промене MCP client конфигурације, рестартујте или поново учитајте клијента да би могао да открије нови сервер.

## Step 3: Verify the Server in the Client

Затражите од MCP клијента да наброји доступне алате, или прво позовите један од read-only помоћника:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Корисне прве провере:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Потврђује да је сервер достижан и приказује доступне токове рада. |
| `list_supported_languages` | Потврђује да се паковани језички подаци могу учитати. |
| `get_configuration_status` | Потврђује доступност LLM и Vision провајдера без откривања тајних вредности. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Користите provider-backed алатке за садржај када MCP клијент већ има садржај документа или пут до слике и када Co-op Translator треба да позове конфигурисане провајдере.

За Markdown:

1. Позовите `translate_markdown_content` са `document`, `language_code`, и по жељи `source_path`.
2. Ако ће преведени резултат бити уписан у Co-op Translator output layout, позовите `rewrite_markdown_paths`.
3. Нека клијент упише или врати коначни `content`.

За notebook-ове:

1. Позовите `translate_notebook_content` са notebook JSON и `language_code`.
2. Позовите `rewrite_notebook_paths` ако је потребно прилагодити преведене линкове за циљну путању.
3. Упишите или вратите коначни notebook JSON.

За слике:

1. Позовите `translate_image_content` са `image_path`, `language_code`, и опционално `root_dir` или `fast_mode`.
2. Прочитајте враћени `data_base64` и `mime_type`.
3. Ако је наведен `output_path`, преведена слика ће такође бити сачувана на том путу.

Алатке за садржај не извршавају откривање пројекта, ажурирања метаподатака, одрицања одговорности или аутоматско преписивање путања. Ако желите да host агент преведе Markdown или notebook делове без Co-op Translator LLM провајдер акредитива, користите agent-assisted радни ток који следи.

### Translate with the Host Agent Model

Користите agent-assisted алатке када желите да MCP host агент, као помоћник за кодирање, генерише преведени текст уместо да конфигуришете Azure OpenAI или OpenAI за Co-op Translator.

У chat-базираном MCP клијенту, обично не морате сами да пишете JSON за алат. Замолите агента да користи agent-assisted радни ток:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

За notebook-е, користите исти образац:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ако ваш MCP клијент подржава server prompts, употребите `agent_assisted_markdown_translation_prompt` да клијент учита исте инструкције радног тока.

За Markdown:

1. Позовите `start_markdown_agent_translation` са `document`, `language_code`, и по жељи `source_path`.
2. Преводите сваки враћени део у host агенту пратећи `prompt` за тај део.
3. Позовите `finish_markdown_agent_translation` са оригиналним `job` и преведеним деловима користећи `chunk_id` и `translated_text`.
4. Ако ће садржај бити уписан на преведену циљну путању, позовите `rewrite_markdown_paths`.

За notebook-ове:

1. Позовите `start_notebook_agent_translation` са notebook JSON и `language_code`.
2. Преведите сваки враћени део у host агенту.
3. Позовите `finish_notebook_agent_translation` са оригиналним `job` и преведеним деловима.
4. Позовите `rewrite_notebook_paths` ако треба прилагодити преведене линкове за циљну путању.

Agent-assisted алатке не позивају Azure OpenAI или OpenAI из Co-op Translator-а. Host агент је одговоран за превођење враћених делова. Co-op Translator се бави разбијањем Markdown-а на делове, очувањем плейсхолдера, реконструкцијом frontmatter-a, заменом ћелија у notebook-у и пост-преводном нормализацијом.

### Translate an Entire Repository

Користите `run_translation` када корисник жели да Co-op Translator ради као `translate` CLI.

Превођење репозиторијума подразумевано користи `dry_run=true` тако да агент може да пре ружних измена прегледа обим:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Да бисте дозволили уписе, позивач мора да подесити и `dry_run=false` и `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` је изложен као алијас за ускомпатибилност са `run_translation`.

### Review Translated Output

Користите `run_review` за детерминистичке провере које не захтевају LLM или Vision акредитиве:

!!! note "Beta"
    MCP изложи бета `run_review` API. Безбедан је за read-only токове за рецензију, али провере и шеме проблема у рецензији могу еволуирати.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Резултат укључује ухваћени текстуални излаз и структурисани резиме рецензије када је доступан.

## Manual Server Runs

Ручни покретачи сервера углавном су за дебаговање или за транспорте који се понашају као дугорајну серверску службу.

Отклоните грешке подразумеваног stdio сервера:

```bash
co-op-translator-mcp
```

Покретање из source checkout-а:

```bash
python -m co_op_translator.mcp.server
```

Покрените дуговечни HTTP или SSE сервер:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

За локалне интеграције уређивача и агената, преферирајте конфигурацију коју управља клијент `stdio` из Степа 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Преведе Markdown стринг. | No |
| `translate_notebook_content` | Преведе Markdown ћелије у notebook JSON. | No |
| `translate_image_content` | Преведе текст на једној слици и врати base64 податке слике. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Припреми Markdown делове да их host агент преведе без Co-op Translator LLM провајдер акредитива. | No |
| `finish_markdown_agent_translation` | Реконструише Markdown из host-agent преведених делова. | No |
| `start_notebook_agent_translation` | Припреми notebook Markdown-ћелијске делове да их host агент преведе. | No |
| `finish_notebook_agent_translation` | Реконструише notebook JSON из host-agent преведених делова. | No |
| `rewrite_markdown_paths` | Препише путање у телу Markdown-а и frontmatter-у за преведену циљну путању. | No |
| `rewrite_notebook_paths` | Препише путање унутар Markdown ћелија у notebook-у. | No |
| `run_translation` | Покреће превођење пројекта као CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Алијас за ускомпатибилност са `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Покреће детерминистичке провере рецензије. | No |
| `get_configuration_status` | Извештава о конфигурисаним LLM и Vision провајдерима без откривања тајни. | No |
| `list_supported_languages` | Набраја подржане кодове циљних језика. | No |
| `get_api_overview` | Описује доступне MCP токове рада и алате. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON преглед токова рада и алата. |
| `co-op://supported-languages` | JSON листа подржаних кодова језика. |
| `co-op://configuration` | JSON резиме доступности провајдера без тајни. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Упутство MCP клијенту кроз превођење садржаја уз опционално преписивање путања. |
| `agent_assisted_markdown_translation_prompt` | Упутство MCP клијенту за host-agent превођење Markdown-а без Co-op Translator LLM провајдер акредитива. |
| `translate_repository_prompt` | Упутство MCP клијенту за превођење репозиторијума које почиње сухим покретањем (dry-run). |

## Copy-Paste Examples

Преведи Markdown садржај:

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

Препиши преведене Markdown линкове:

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

Преведи Markdown уз host agent модел:

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

Након што host агент преведе сваки враћени део, завршите задатак са комплетним `job` објектом који врати `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Преглед превођења репозиторијума:

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
| The MCP client cannot find `co-op-translator-mcp`. | Користите апсолутну путању до Python извршног фајла и `["-m", "co_op_translator.mcp.server"]` source checkout конфигурацију. |
| The server is listed but translation fails. | Позовите `get_configuration_status` и потврдите да је LLM провајдер доступан. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Користите `start_markdown_agent_translation` / `finish_markdown_agent_translation` или еквиваленте за notebook тако да host агент преведе делове. |
| Image translation fails. | Потврдите да су Azure AI Vision променљиве постављене и позовите `get_configuration_status`. |
| Repository translation does not write files. | Поставите `dry_run=false` и `confirm_write=true` само након јасног одобрења корисника. |
| Changes to client config do not appear. | Рестартујте или поново учитајте MCP клијента. |

## Safety Notes

- MCP позиви алата контролишу се моделом у host апликацији, тако да је превођење репозиторијума подразумевано у режиму dry-run.
- Потпуно превођење репозиторијума може да креира, ажурира или уклони много фајлова. Захтевајте јасно одобрење корисника пре подешавања `confirm_write=true`.
- Алат за проверу статуса конфигурације никада не враћа API кључеве, ендпойнте или друге тајне вредности.
- Превођење слика враћа base64 податке слике. Велике слике могу произвести велике одговоре алата.
- Agent-assisted алатке враћају оригиналне делове и упите (prompts) host агенту. Користите их само са садржајем који је корисник спреман да пошаље том host agent моделу.