# MCP сервер

Co-op Translator укључује Model Context Protocol сервер за агенте, уреднике и MCP-скомпатибилне клијенте.

За подразумевану локалну конфигурацију, корисници не покрећу засебан сервер ручно. Они конфигуришу свој MCP клијент, а клијент аутоматски покреће `co-op-translator-mcp` преко `stdio` кад год су му потребни алати Co-op Translator-а.

Ако бираете између CLI, Python API и MCP, почните са [Изаберите ваш радни ток](workflows.md).

Користите MCP када агент или уредник треба да позове Co-op Translator директно:

| Циљ корисника | MCP алати |
| --- | --- |
| Превести један Markdown документ, нотебук или слику | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Превести Markdown или садржај нотебука помоћу модела домаћинског агента | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Преписати преведене линкове у Markdown-у или нотебуку након избора путање за излаз | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Превести цео репозиторијум као CLI | `run_translation`, `translate_project` |
| Прегледати преведени резултат без LLM креденцијала | `run_review` |
| Испитати могућности и статус окружења | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP сервер омотава исти јавни Python API документаран у [Python API](api.md). Алати који користе провајдере користе исте конфигурисане провајдере као CLI и Python API. Алати помоћу агента припремају делове за MCP домаћинског агента да преведе, а затим користе Co-op Translator за реконструкцију коначног Markdown-а или нотебука.

## Корак 1: Инсталирајте и конфигуришите Co-op Translator

Инсталирајте Co-op Translator у Python окружење које ће ваш MCP клијент користити:

```bash
pip install co-op-translator
```

За локални развој из овог репозиторијума, инсталирајте пакет у режиму за уређивање:

```bash
pip install -e .
```

Одаберите режим превођења који ће ваш MCP клијент користити:

| Режим | Користи се за | Креденцијали |
| --- | --- | --- |
| Подржано провајдером | Co-op Translator позива `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, или `run_translation`. | Превођење захтева Azure OpenAI, OpenAI, или Anthropic. Превођење слика такође захтева Azure AI Vision. |
| Помоћ агента | MCP домаћински агент преводи делове које враћају `start_markdown_agent_translation` или `start_notebook_agent_translation`. | За Markdown или делове нотебука нису потребни LLM провајдер креденцијали Co-op Translator-а. Превођење слика још није покривено режимом помоћи агента. |

Ако почињете са превођењем Markdown-а или нотебука унутар агента као што су Codex или Claude Code, почните са режимом помоћи агента. Користите режим подржан провајдером када желите да сам Co-op Translator позове ваше конфигурисане провајдере, када преводите слике, или када покрећете превођење на нивоу репозиторијума као CLI.

Конфигуришите једног провајдера за радне токове подржане провајдером:

```bash
# Азуре ОпенАИ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Или ОпенАИ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Или Антропик
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Превођење слика подржано провајдером додатно захтева:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Режим уз помоћ агента тренутно покрива Markdown и Markdown ћелије нотебука. Превођење слика и даље користи провајдерски потпрт конвејер за слике и захтева Azure AI Vision за OCR и рендеровање осетљиво на распоред.

## Корак 2: Конфигуришите ваш MCP клијент

За нормалну локалну `stdio` конфигурацију, додајте Co-op Translator у конфигурацију вашег MCP клијента. Клијент ће аутоматски покренути и зауставити процес.

Конфигурација за инсталирани пакет:

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

Конфигурација извора (source checkout) на macOS или Linux:

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

Након промене конфигурације MCP клијента, рестартујте или поново учитајте клијента да би открио нови сервер.

## Корак 3: Верификујте сервер у клијенту

Замолите MCP клијента да листа доступне алате, или најпре позовите један од помоћних алата само за читање:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Корисне прве провере:

| Алат | Шта проверити |
| --- | --- |
| `get_api_overview` | Потврђује да је сервер доступан и приказује доступне радне токове. |
| `list_supported_languages` | Потврђује да се пакетирани подаци о језицима могу учитати. |
| `get_configuration_status` | Потврђује доступност LLM и Vision провајдера без откривања тајних вредности. |

## Корак 4: Изаберите радни ток

### Преведите појединачне датотеке или документе

Користите алате подржане провајдером када MCP клијент већ има садржај документа или путању до слике и када Co-op Translator треба да позове конфигурисане провајдере за превод.

За Markdown:

1. Позовите `translate_markdown_content` са `document`, `language_code`, и опционално `source_path`.
2. Ако ће преведени резултат бити уписан у Co-op Translator излазни изглед, позовите `rewrite_markdown_paths`.
3. Нека клијент упише или врати коначни `content`.

За нотебуке:

1. Позовите `translate_notebook_content` са нотебук JSON-ом и `language_code`.
2. Позовите `rewrite_notebook_paths` ако је потребно прилагодити преведене линкове нотебука за циљану путању.
3. Упишите или вратите коначни нотебук JSON.

За слике:

1. Позовите `translate_image_content` са `image_path`, `language_code`, и опционалним `root_dir` или `fast_mode`.
2. Прочитајте враћени `data_base64` и `mime_type`.
3. Ако је наведен `output_path`, преведена слика се такође сачува на тој путањи.

Алати за садржај не обављају откривање пројекта, ажурирања метаподатака, одрицања или аутоматско преписивање путева. Ако желите да домаћински агент преведе Markdown или делове нотебука без LLM провајдер креденцијала Co-op Translator-а, користите радни ток помоћу агента у наставку.

### Превођење уз модел домаћинског агента

Користите алате помоћу агента када желите да MCP домаћински агент, као помоћник за кодирање, генерише преведени текст уместо да конфигуришете LLM провајдера за Co-op Translator.

У чат-базираном MCP клијенту обично не морате сами да пишете JSON за алат. Замолите агента да користи радни ток помоћу агента:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

За нотебуке, користите исти образац:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ако ваш MCP клијент подржава серверске упуте (server prompts), користите `agent_assisted_markdown_translation_prompt` да би клијент учитао исте инструкције радног тока.

За Markdown:

1. Позовите `start_markdown_agent_translation` са `document`, `language_code`, и опционално `source_path`.
2. Преведите сваки враћени део у домаћинском агенту пратећи `prompt` дела.
3. Позовите `finish_markdown_agent_translation` са оригиналним `job` и преведеним деловима користећи `chunk_id` и `translated_text`.
4. Ако ће садржај бити уписан у преведену циљну путању, позовите `rewrite_markdown_paths`.

За нотебуке:

1. Позовите `start_notebook_agent_translation` са нотебук JSON-ом и `language_code`.
2. Преведите сваки враћени део у домаћинском агенту.
3. Позовите `finish_notebook_agent_translation` са оригиналним `job` и преведеним деловима.
4. Позовите `rewrite_notebook_paths` ако преведени линкови у нотебуку захтевају прилагођавање циљне путање.

Алати помоћу агента не позивају конфигурисаног LLM провајдера из Co-op Translator-а. Домаћински агент је одговоран за превођење враћених делова. Co-op Translator обрађује разбијање Markdown-а на делове, очување замена (placeholders), реконструкцију frontmatter-а, замену ћелија у нотебуку и нормализацију после превођења.

### Преведите цео репозиторијум

Користите `run_translation` када корисник жели да Co-op Translator понаша као `translate` CLI.

Превођење репозиторијума подразумевано користи `dry_run=true` тако да агент може да испита опсег пре промена у фајловима:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Резултат `run_translation` садржи низ `events` са верзионисаним
`co-op.translation.event.v1` догађајима напредка. MCP клијенти треба да користе поља као
као што су `type`, `stage_key`, `completed`, `total`, и `current_path` уместо
парсирања снимљеног текста из конзоле. Проследите `json_events_path` да бисте те догађаје
уписали и у NDJSON датотеку.

Да бисте дозволили уписе, позивач мора подесити и `dry_run=false` и `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` је изложен као компатибилни алијас за `run_translation`.

### Преглед преведеног излаза

Користите `run_review` за детерминистичке провере које не захтевају LLM или Vision креденцијале:

!!! note "Beta"
    MCP нуди бета API `run_review`. Погодан је за токове рада прегледа само за читање, али провере при прегледу и шеме проблема могу се мењати.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Резултат укључује снимљени текстуални излаз и структурисани резиме прегледа када је доступан.

## Ручно покретање сервера

Ручни покретачи се углавном користе за дебаговање или за транспорте који се понашају као дугорочни сервери.

Дебагујте подразумевани stdio сервер:

```bash
co-op-translator-mcp
```

Покрените из source checkout-а:

```bash
python -m co_op_translator.mcp.server
```

Покрените дугоживи HTTP или SSE сервер:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

За локалне интеграције уредника и агената, дајте преференцију конфигурацији `stdio` коју управља клијент у Кораку 2.

## Алати

| Алат | Намена | Пише датотеке |
| --- | --- | --- |
| `translate_markdown_content` | Преведе Markdown садржај. | Не |
| `translate_notebook_content` | Преведе Markdown ћелије у нотебук JSON-у. | Не |
| `translate_image_content` | Преведе текст на једној слици и врати base64 податке слике. | Опционо, само када је наведен `output_path` |
| `start_markdown_agent_translation` | Припреми Markdown делове за домаћинског агента да преведе без LLM креденцијала Co-op Translator-а. | Не |
| `finish_markdown_agent_translation` | Реконструише Markdown из делова преведених од стране домаћинског агента. | Не |
| `start_notebook_agent_translation` | Припреми делове Markdown-ћелија нотебука за превођење од стране домаћинског агента. | Не |
| `finish_notebook_agent_translation` | Реконструише нотебук JSON из делова преведених од домаћинског агента. | Не |
| `rewrite_markdown_paths` | Преуреди путеве у телу Markdown-а и frontmatter-у за преведени циљ. | Не |
| `rewrite_notebook_paths` | Преуреди путеве унутар Markdown ћелија нотебука. | Не |
| `run_translation` | Покреће превођење на нивоу пројекта као CLI. | Да када је `dry_run=false` и `confirm_write=true` |
| `translate_project` | Компатибилни алијас за `run_translation`. | Да када је `dry_run=false` и `confirm_write=true` |
| `run_review` | Извршава детерминистичке провере прегледа. | Не |
| `get_configuration_status` | Извештава о конфигурисаним LLM и Vision провајдерима без откривања тајни. | Не |
| `list_supported_languages` | Листа подржаних кодова циљних језика. | Не |
| `get_api_overview` | Описује доступне MCP радне токове и алате. | Не |

## Ресурси

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON преглед радних токова и алата. |
| `co-op://supported-languages` | JSON листа подржаних кодова језика. |
| `co-op://configuration` | JSON резиме доступности провајдера без тајних података. |

## Подсетници

| Подсетник | Намена |
| --- | --- |
| `translate_markdown_document_prompt` | Упутити MCP клијента кроз превођење садржаја и опционално преписивање путева. |
| `agent_assisted_markdown_translation_prompt` | Упутити MCP клијента кроз превођење Markdown-а помоћу домаћинског агента без LLM креденцијала Co-op Translator-а. |
| `translate_repository_prompt` | Упутити MCP клијента кроз превођење репозиторијума које прво ради као dry-run. |

## Примери за копирање и лепљење

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

Преуреди преведене Markdown линкове:

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

Преведите Markdown уз модел домаћинског агента:

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

Након што домаћински агент преведе сваки враћени део, завршите посао помоћу комплетног објекта `job` који враћа `start_markdown_agent_translation`:

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

## Решавање проблема

| Проблем | Шта пробати |
| --- | --- |
| MCP клијент не може да пронађе `co-op-translator-mcp`. | Користите апсолутну путању до Python извршне датотеке и `["-m", "co_op_translator.mcp.server"]` конфигурацију за source checkout. |
| Сервер је наведен али превођење не успева. | Позовите `get_configuration_status` и потврдите да је доступан LLM провајдер. |
| Желите превођење Markdown-а или нотебука без провајдер креденцијала. | Користите `start_markdown_agent_translation` / `finish_markdown_agent_translation` или еквиваленте за нотебук тако да домаћински агент преведе делове. |
| Превођење слика не ради. | Потврдите да су Azure AI Vision променљиве постављене и позовите `get_configuration_status`. |
| Превођење репозиторијума не уписује фајлове. | Подесите `dry_run=false` и `confirm_write=true` само након изричитог одобрења корисника. |
| Промене у конфигурацији клијента се не појављују. | Рестартујте или поново учитајте MCP клијента. |

## Безбедносне белешке

- MCP позиви алата контролише модел домаћинске апликације, па је превођење репозиторијума подразумевано у режиму dry-run.
- Потпуно превођење репозиторијума може да креира, ажурира или уклони многе фајлове. Захтевајте изричито одобрење корисника пре подешавања `confirm_write=true`.
- Алат за статус конфигурације никада не враћа API кључеве, крајње тачке или друге тајне вредности.
- Превођење слика враћа base64 податке слике. Велике слике могу произвести велике одговоре алата.
- Алати помоћу агента враћају изворне делове и подсетнике (prompts) домаћинском агенту. Користите их само са садржајем који је корисник спреман да пошаље том моделу домаћинског агента.