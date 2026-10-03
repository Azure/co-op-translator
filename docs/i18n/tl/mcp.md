# MCP Server

Naglalaman ang Co-op Translator ng isang Model Context Protocol (MCP) server para sa mga agent, editor, at mga kliyenteng MCP-compatible.

Para sa default na lokal na setup, hindi nagpapatakbo nang hiwalay ang mga gumagamit ng isang server. Ina-configure nila ang kanilang MCP client, at awtomatikong sinisimulan ng client ang `co-op-translator-mcp` sa pamamagitan ng `stdio` kapag kailangan nito ng mga tool ng Co-op Translator.

Kung pinipili mo sa pagitan ng CLI, Python API, at MCP, simulan sa [Piliin ang Iyong Workflow](workflows.md).

Gamitin ang MCP kapag dapat direktang tawagan ng isang agent o editor ang Co-op Translator:

| Layunin ng gumagamit | Mga tool ng MCP |
| --- | --- |
| Isalin ang isang dokumentong Markdown, notebook, o imahe | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Isalin ang nilalaman ng Markdown o notebook gamit ang host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| I-rewrite ang mga isinalin na link ng Markdown o notebook pagkatapos pumili ng output na path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Isalin ang buong repositoryo tulad ng CLI | `run_translation`, `translate_project` |
| Suriin ang isinaling output nang wala ang LLM credentials | `run_review` |
| Suriin ang mga kakayahan at katayuan ng kapaligiran | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Ang MCP server ay nagbabalot ng parehong public Python API na dokumentado sa [Python API](api.md). Gumagamit ang mga tool na suportado ng provider ng parehong naka-configure na mga provider tulad ng CLI at Python API. Inihahanda ng mga agent-assisted na tool ang mga chunk para isalin ng MCP host agent, pagkatapos ay ginagamit ang Co-op Translator upang mabuo muli ang panghuling Markdown o notebook.

## Hakbang 1: I-install at I-configure ang Co-op Translator

I-install ang Co-op Translator sa Python environment na gagamitin ng iyong MCP client:

```bash
pip install co-op-translator
```

Para sa lokal na pag-develop mula sa repositoryong ito, i-install ang package sa editable mode:

```bash
pip install -e .
```

Piliin ang translation mode na gagamitin ng iyong MCP client:

| Mode | Gamitin para sa | Mga kredensyal |
| --- | --- | --- |
| Provider-backed | Tumatawag ang Co-op Translator ng `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, o `run_translation`. | Nangangailangan ang pagsasalin ng Azure OpenAI, OpenAI, o Anthropic. Nangangailangan din ang image translation ng Azure AI Vision. |
| Agent-assisted | Isinasalin ng MCP host agent ang mga chunk na ibinalik ng `start_markdown_agent_translation` o `start_notebook_agent_translation`. | Hindi kinakailangan ang Co-op Translator LLM provider credentials para sa mga chunk ng Markdown o notebook. Hindi pa sakop ng agent-assisted mode ang image translation. |

Kung nagsisimula ka sa pagsasalin ng Markdown o notebook sa loob ng isang agent tulad ng Codex o Claude Code, magsimula sa agent-assisted mode. Gamitin ang provider-backed mode kapag gusto mong ang Co-op Translator mismo ang tumawag sa iyong naka-configure na mga provider, kapag nagsasalin ka ng mga imahe, o kapag nagpapatakbo ka ng translation sa antas ng repositoryo tulad ng CLI.

I-configure ang isang provider para sa provider-backed workflows:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# O OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# O Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Dagdag na kinakailangan para sa provider-backed image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Sa kasalukuyan, sinasaklaw ng agent-assisted mode ang Markdown at mga Markdown cell sa notebook. Ang image translation ay gumagamit pa rin ng provider-backed image pipeline at nangangailangan ng Azure AI Vision para sa OCR at layout-aware rendering.

## Hakbang 2: I-configure ang Iyong MCP Client

Para sa normal na lokal na `stdio` setup, idagdag ang Co-op Translator sa iyong MCP client configuration. Awtomatikong sisimulan at ihihinto ng client ang proseso.

Konfigurasyon para sa naka-install na package:

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

Konfigurasyon ng source checkout sa Windows:

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

Konfigurasyon ng source checkout sa macOS o Linux:

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

Pagkatapos baguhin ang MCP client configuration, i-restart o i-reload ang client upang madiskubre nito ang bagong server.

## Hakbang 3: Beripikahin ang Server sa Client

Hilingin sa MCP client na ilista ang mga available na tool, o tumawag muna ng isa sa mga read-only helper:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Mga kapaki-pakinabang na unang tsek:

| Tool | Ano ang susuriin |
| --- | --- |
| `get_api_overview` | Kinukumpirma na maaabot ang server at ipinapakita ang mga available na workflow. |
| `list_supported_languages` | Kinukumpirma na maaaring i-load ang naka-package na data ng wika. |
| `get_configuration_status` | Kinukumpirma ang availability ng LLM at Vision provider nang hindi ibinubunyag ang mga secret na halaga. |

## Hakbang 4: Pumili ng Workflow

### Isalin ang Indibidwal na Mga File o Dokumento

Gamitin ang provider-backed content tools kapag mayroon na ang MCP client ng content ng dokumento o image path at dapat tawagan ng Co-op Translator ang naka-configure na mga translation provider.

Para sa Markdown:

1. Tawagin ang `translate_markdown_content` kasama ang `document`, `language_code`, at opsyonal na `source_path`.
2. Kung ang isinaling resulta ay isusulat sa isang Co-op Translator output layout, tawagin ang `rewrite_markdown_paths`.
3. Hayaan ang client na isulat o ibalik ang pangwakas na `content`.

Para sa mga notebook:

1. Tawagin ang `translate_notebook_content` gamit ang notebook JSON at `language_code`.
2. Tawagin ang `rewrite_notebook_paths` kung kailangan i-adjust ang mga isinaling link ng notebook para sa target na path.
3. Isulat o ibalik ang pangwakas na notebook JSON.

Para sa mga imahe:

1. Tawagin ang `translate_image_content` kasama ang `image_path`, `language_code`, at opsyonal na `root_dir` o `fast_mode`.
2. Basahin ang ibinalik na `data_base64` at `mime_type`.
3. Kung ibinigay ang `output_path`, isasave din ang isinaling imahe sa path na iyon.

Hindi isinasagawa ng mga content tool ang project discovery, metadata updates, disclaimers, o awtomatikong path rewriting. Kung gusto mong isalin ng host agent ang mga chunk ng Markdown o notebook nang walang Co-op Translator LLM provider credentials, gamitin ang agent-assisted workflow sa ibaba.

### Isalin gamit ang Host Agent Model

Gamitin ang agent-assisted tools kapag gusto mong ang MCP host agent, tulad ng isang coding assistant, ang gumawa ng isinaling teksto sa halip na mag-configure ng LLM provider para sa Co-op Translator.

Sa isang chat-based na MCP client, karaniwan hindi mo kailangang isulat ang tool JSON mismo. Hilingin sa agent na gamitin ang agent-assisted workflow:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Para sa mga notebook, gamitin ang parehong pattern:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Kung sinusuportahan ng iyong MCP client ang server prompts, gamitin ang `agent_assisted_markdown_translation_prompt` para ipaload ng client ang parehong workflow instructions.

Para sa Markdown:

1. Tawagin ang `start_markdown_agent_translation` kasama ang `document`, `language_code`, at opsyonal na `source_path`.
2. Isalin ang bawat ibinalik na chunk sa host agent sa pamamagitan ng pagsunod sa chunk `prompt`.
3. Tawagin ang `finish_markdown_agent_translation` gamit ang orihinal na `job` at mga isinaling chunk na may `chunk_id` at `translated_text`.
4. Kung isusulat ang content sa isang isinaling target path, tawagin ang `rewrite_markdown_paths`.

Para sa mga notebook:

1. Tawagin ang `start_notebook_agent_translation` gamit ang notebook JSON at `language_code`.
2. Isalin ang bawat ibinalik na chunk sa host agent.
3. Tawagin ang `finish_notebook_agent_translation` gamit ang orihinal na `job` at mga isinaling chunk.
4. Tawagin ang `rewrite_notebook_paths` kung kailangan i-adjust ang mga isinaling link ng notebook para sa target-path.

Hindi tinatawag ng agent-assisted tools ang naka-configure na LLM provider mula sa Co-op Translator. Ang host agent ang responsable sa pagsasalin ng mga ibinalik na chunk. Hinahandle ng Co-op Translator ang Markdown chunking, pagpapanatili ng mga placeholder, rekonstruksyon ng frontmatter, pagpapalit ng notebook cell, at post-translation normalization.

### Isalin ang Buong Repositoryo

Gamitin ang `run_translation` kapag gusto ng user na kumilos ang Co-op Translator tulad ng `translate` CLI.

Ang repository translation ay default na `dry_run=true` upang makapag-inspect ang agent ng scope bago ang mga pagbabago sa file:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Ang resulta ng `run_translation` ay may kasamang `events` array na may versioned
`co-op.translation.event.v1` na progress events. Dapat gamitin ng mga MCP client ang mga field tulad ng
`type`, `stage_key`, `completed`, `total`, at `current_path` sa halip na
i-parse ang na-capture na console text. I-pass ang `json_events_path` para isulat din ang mga event na iyon
sa isang NDJSON na file.

Upang payagan ang pagsulat, dapat itakda ng tumatawag ang parehong `dry_run=false` at `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ay inihahayag bilang compatibility alias para sa `run_translation`.

### Suriin ang Isinaling Output

Gamitin ang `run_review` para sa deterministic checks na hindi nangangailangan ng LLM o Vision credentials:

!!! note "Beta"
    Ipinapakita ng MCP ang beta na `run_review` API. Ligtas ito para sa mga read-only na review workflow, ngunit ang mga review check at issue schema ay maaaring magbago.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Kasama sa resulta ang na-capture na text output at isang structured review summary kapag available.

## Manu-manong Pagpapatakbo ng Server

Ang manu-manong pagpapatakbo ay pangunahin para sa debugging o para sa mga transport na kumikilos na parang mga long-running server.

I-debug ang default na stdio server:

```bash
co-op-translator-mcp
```

Patakbuhin mula sa source checkout:

```bash
python -m co_op_translator.mcp.server
```

Patakbuhin ang isang pangmatagalang HTTP o SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para sa lokal na editor at agent integrations, mas piliin ang client-managed na `stdio` configuration sa Hakbang 2.

## Mga Tool

| Tool | Layunin | Nagsusulat ng mga file |
| --- | --- | --- |
| `translate_markdown_content` | Isalin ang isang Markdown string. | Hindi |
| `translate_notebook_content` | Isalin ang mga Markdown cell sa notebook JSON. | Hindi |
| `translate_image_content` | Isalin ang teksto sa isang imahe at ibalik ang base64 image data. | Opsyonal, lamang kapag ibinigay ang `output_path` |
| `start_markdown_agent_translation` | Ihanda ang mga Markdown chunk para isalin ng host agent nang walang Co-op Translator LLM credentials. | Hindi |
| `finish_markdown_agent_translation` | I-rekonstrak ang Markdown mula sa mga chunk na isinalin ng host agent. | Hindi |
| `start_notebook_agent_translation` | Ihanda ang mga notebook Markdown-cell chunk para isalin ng host agent. | Hindi |
| `finish_notebook_agent_translation` | I-rekonstrak ang notebook JSON mula sa mga chunk na isinalin ng host agent. | Hindi |
| `rewrite_markdown_paths` | I-rewrite ang katawan ng Markdown at mga path sa frontmatter para sa isinaling target. | Hindi |
| `rewrite_notebook_paths` | I-rewrite ang mga path sa loob ng mga notebook Markdown cell. | Hindi |
| `run_translation` | Patakbuhin ang project-level translation tulad ng CLI. | Oo kapag `dry_run=false` at `confirm_write=true` |
| `translate_project` | Compatibility alias para sa `run_translation`. | Oo kapag `dry_run=false` at `confirm_write=true` |
| `run_review` | Patakbuhin ang deterministic review checks. | Hindi |
| `get_configuration_status` | Iulat ang naka-configure na LLM at Vision providers nang hindi ibinubunyag ang mga lihim. | Hindi |
| `list_supported_languages` | Ilista ang mga suportadong target language codes. | Hindi |
| `get_api_overview` | Ilarawan ang mga available na MCP workflow at tool. | Hindi |

## Mga Resurso

| Resource URI | Layunin |
| --- | --- |
| `co-op://api` | JSON na overview ng mga workflow at tool. |
| `co-op://supported-languages` | JSON na listahan ng mga suportadong language codes. |
| `co-op://configuration` | JSON na buod ng availability ng provider nang walang mga lihim. |

## Mga Prompt

| Prompt | Layunin |
| --- | --- |
| `translate_markdown_document_prompt` | Gabayan ang MCP client sa content translation kasama ang opsyonal na path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Gabayan ang MCP client sa host-agent Markdown translation nang walang Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Gabayan ang MCP client sa dry-run-first na repository translation. |

## Mga Halimbawa na Kopyahin-I-paste

Isalin ang nilalaman ng Markdown:

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

I-rewrite ang mga isinaling link ng Markdown:

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

Isalin ang Markdown gamit ang host agent model:

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

Pagkatapos isalin ng host agent ang bawat ibinalik na chunk, tapusin ang job gamit ang kumpletong `job` object na ibinalik ng `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

I-preview ang pagsasalin ng repositoryo:

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

## Pag-troubleshoot

| Problema | Ano ang susubukan |
| --- | --- |
| Hindi mahanap ng MCP client ang `co-op-translator-mcp`. | Gamitin ang absolute na Python executable path at `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| Nakalista ang server pero nabigo ang pagsasalin. | Tawagin ang `get_configuration_status` at kumpirmahin na may available na LLM provider. |
| Gusto mong pagsalin ng Markdown o notebook nang walang provider credentials. | Gamitin ang `start_markdown_agent_translation` / `finish_markdown_agent_translation` o ang mga katumbas na notebook para isalin ng host agent ang mga chunk. |
| Nabibigo ang image translation. | Kumpirmahin na naka-set ang Azure AI Vision variables at tawagin ang `get_configuration_status`. |
| Hindi nagsusulat ng files ang repository translation. | Itakda ang `dry_run=false` at `confirm_write=true` lamang pagkatapos ng tahasang pag-apruba ng gumagamit. |
| Hindi lumilitaw ang mga pagbabago sa client config. | I-restart o i-reload ang MCP client. |

## Mga Tala sa Kaligtasan

- Ang mga pagtawag sa MCP tool ay kinokontrol ng modelo ng host application, kaya ang repository translation ay dry-run bilang default.
- Ang buong repository translation ay maaaring lumikha, mag-update, o mag-alis ng maraming file. Humiling ng tahasang pag-apruba ng gumagamit bago itakda ang `confirm_write=true`.
- Ang configuration status tool ay hindi kailanman nagbabalik ng API keys, endpoints, o iba pang mga secret na halaga.
- Nagbabalik ang image translation ng base64 image data. Ang malalaking imahe ay maaaring magresulta ng malaking mga tugon mula sa tool.
- Ang agent-assisted tools ay nagbabalik ng source chunks at prompts sa MCP host. Gamitin lamang ang mga ito sa content na komportable ang gumagamit na ipadala sa host agent model na iyon.