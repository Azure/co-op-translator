# MCP Server

Kasama sa Co-op Translator ang isang Model Context Protocol server para sa mga agent, editor, at mga kliyenteng katugma ng MCP.

Para sa default na lokal na setup, hindi nagpapatakbo ang mga gumagamit ng hiwalay na server nang mano-mano. Kino-configure nila ang kanilang MCP client, at awtomatikong sinisimulan ng client ang `co-op-translator-mcp` sa pamamagitan ng `stdio` kapag kailangan nito ng mga tool ng Co-op Translator.

Kung nagdedesisyon ka sa pagitan ng CLI, Python API, at MCP, magsimula sa [Piliin ang Iyong Daloy ng Trabaho](workflows.md).

Gamitin ang MCP kapag ang isang agent o editor ay dapat tumawag nang direkta sa Co-op Translator:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Ang MCP server ay naglalaman ng parehong public Python API na dinokumento sa [Python API](api.md). Gumagamit ang mga tool na may provider ng parehong naka-configure na mga provider tulad ng CLI at Python API. Inihahanda ng mga agent-assisted na tool ang mga chunk para isalin ng MCP host agent, pagkatapos ay ginagamit ng Co-op Translator ang mga ito para muling buuin ang huling Markdown o notebook.

## Step 1: Install and Configure Co-op Translator

I-install ang Co-op Translator sa Python environment na gagamitin ng iyong MCP client:

```bash
pip install co-op-translator
```

Para sa lokal na pag-develop mula sa repositoryong ito, i-install ang package sa editable mode:

```bash
pip install -e .
```

Piliin ang modo ng pagsasalin na gagamitin ng iyong MCP client:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Tinatawagan ng Co-op Translator ang `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, o `run_translation`. | Kinakailangan ang Azure OpenAI o OpenAI para sa pagsasalin ng Markdown at notebook. Kinakailangan din ang Azure AI Vision para sa pagsasalin ng mga imahe. |
| Agent-assisted | Isinasalin ng MCP host agent ang mga chunk na ibinabalik ng `start_markdown_agent_translation` o `start_notebook_agent_translation`. | Hindi kinakailangan ang mga Co-op Translator LLM provider credentials para sa mga Markdown o notebook chunk. Hindi pa sakop ng agent-assisted mode ang pagsasalin ng mga imahe. |

Kung nagsisimula ka sa pagsasalin ng Markdown o notebook sa loob ng isang agent tulad ng Codex o Claude Code, magsimula sa agent-assisted mode. Gamitin ang provider-backed mode kapag gusto mong ang Co-op Translator mismo ang tumawag sa iyong naka-configure na mga provider, kapag nagsasalin ka ng mga imahe, o kapag nagpapatupad ka ng pagsasalin ng repositoryo tulad ng CLI.

I-configure lamang ang provider credentials para sa mga provider-backed na workflow:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kailangan din ng provider-backed image translation ang:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Sakop ng agent-assisted mode ngayon ang Markdown at mga cell ng notebook Markdown. Ang pagsasalin ng imahe ay gumagamit pa rin ng provider-backed image pipeline at nangangailangan ng Azure AI Vision para sa OCR at layout-aware rendering.

## Step 2: Configure Your MCP Client

Para sa normal na lokal na `stdio` setup, idagdag ang Co-op Translator sa configuration ng iyong MCP client. Awtomatikong sisimulan at ihihinto ng client ang proseso.

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

Source checkout configuration on macOS or Linux:

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

## Step 3: Verify the Server in the Client

Hilingin sa MCP client na ilista ang magagamit na mga tool, o tawagan muna ang isa sa mga read-only helper:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Mga kapaki-pakinabang na unang tseke:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Kinukumpirma na maaabot ang server at ipinapakita ang magagamit na mga workflow. |
| `list_supported_languages` | Kinukumpirma na maaaring i-load ang naka-package na language data. |
| `get_configuration_status` | Kinukumpirma ang availability ng LLM at Vision provider nang hindi inilalantad ang mga secret na halaga. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Gamitin ang provider-backed content tools kapag ang MCP client ay mayroon nang nilalaman ng dokumento o path ng imahe at ang Co-op Translator ang dapat tumawag sa mga naka-configure na provider para sa pagsasalin.

Para sa Markdown:

1. Tawagan ang `translate_markdown_content` na may `document`, `language_code`, at opsyonal na `source_path`.
2. Kung ang na-translate na resulta ay isusulat sa isang Co-op Translator output layout, tawagan ang `rewrite_markdown_paths`.
3. Hayaan ang client na isulat o ibalik ang panghuling `content`.

Para sa mga notebook:

1. Tawagan ang `translate_notebook_content` na may notebook JSON at `language_code`.
2. Tawagan ang `rewrite_notebook_paths` kung kailangang ayusin ang mga link ng na-translate na notebook para sa target na path.
3. Isulat o ibalik ang panghuling notebook JSON.

Para sa mga imahe:

1. Tawagan ang `translate_image_content` na may `image_path`, `language_code`, at opsyonal na `root_dir` o `fast_mode`.
2. Basahin ang ibinalik na `data_base64` at `mime_type`.
3. Kung ibinigay ang `output_path`, ang na-translate na imahe ay isinasave din sa path na iyon.

Hindi ginagawa ng mga content tool ang project discovery, mga pag-update ng metadata, disclaimers, o awtomatikong pag-rewrite ng mga path. Kung gusto mong ang host agent ang magsalin ng mga chunk ng Markdown o notebook nang walang Co-op Translator LLM provider credentials, gamitin ang agent-assisted workflow sa ibaba.

### Translate with the Host Agent Model

Gamitin ang agent-assisted tools kapag gusto mong ang MCP host agent, tulad ng isang coding assistant, ang gumawa ng na-translate na teksto sa halip na i-configure ang Azure OpenAI o OpenAI para sa Co-op Translator.

Sa isang chat-based MCP client, karaniwang hindi mo kailangang isulat ang tool JSON nang manu-mano. Hilingin sa agent na gamitin ang agent-assisted workflow:

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

Kung sinusuportahan ng iyong MCP client ang server prompts, gamitin ang `agent_assisted_markdown_translation_prompt` upang ipaload ng client ang parehong mga instruksyon ng workflow.

Para sa Markdown:

1. Tawagan ang `start_markdown_agent_translation` na may `document`, `language_code`, at opsyonal na `source_path`.
2. Isalin ang bawat ibinalik na chunk sa host agent sa pamamagitan ng pagsunod sa chunk `prompt`.
3. Tawagan ang `finish_markdown_agent_translation` na may orihinal na `job` at mga na-translate na chunk gamit ang `chunk_id` at `translated_text`.
4. Kung isusulat ang content sa isang na-translate na target path, tawagan ang `rewrite_markdown_paths`.

Para sa mga notebook:

1. Tawagan ang `start_notebook_agent_translation` na may notebook JSON at `language_code`.
2. Isalin ang bawat ibinalik na chunk sa host agent.
3. Tawagan ang `finish_notebook_agent_translation` na may orihinal na `job` at mga na-translate na chunk.
4. Tawagan ang `rewrite_notebook_paths` kung kailangan ang pagsasaayos ng mga link ng na-translate na notebook para sa target-path.

Hindi tumatawag ang agent-assisted tools ng Azure OpenAI o OpenAI mula sa Co-op Translator. Ang host agent ang may pananagutan sa pagsasalin ng mga ibinalik na chunk. Pinangangasiwaan ng Co-op Translator ang Markdown chunking, pagpapanatili ng placeholder, rekonstruksyon ng frontmatter, pagpapalit ng mga cell ng notebook, at post-translation normalization.

### Translate an Entire Repository

Gamitin ang `run_translation` kapag gusto ng user na kumilos ang Co-op Translator tulad ng `translate` CLI.

Ang pagsasalin ng repositoryo ay default sa `dry_run=true` upang makapagsiyasat muna ang isang agent bago magbago ng mga file:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Upang payagan ang pagsusulat, dapat itakda ng caller parehong `dry_run=false` at `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

Ibinubukas ang `translate_project` bilang compatibility alias para sa `run_translation`.

### Review Translated Output

Gamitin ang `run_review` para sa deterministic checks na hindi nangangailangan ng LLM o Vision credentials:

!!! note "Beta"
    Inilalantad ng MCP ang beta `run_review` API. Ligtas ito para sa read-only review workflows, ngunit maaaring magbago ang review checks at issue schemas.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Kasama sa resulta ang na-capture na text output at isang structured review summary kapag magagamit.

## Manual Server Runs

Pangunahin para sa debugging o para sa mga transport na kumikilos tulad ng mga long-running server ang mga manual run.

I-debug ang default na stdio server:

```bash
co-op-translator-mcp
```

Patakbuhin mula sa isang source checkout:

```bash
python -m co_op_translator.mcp.server
```

Patakbuhin ang isang long-lived HTTP o SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para sa lokal na editor at agent integrations, mas piliin ang client-managed na `stdio` configuration sa Hakbang 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | Hindi |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | Hindi |
| `translate_image_content` | Translate text in one image and return base64 image data. | Opsyonal, lamang kapag ibinigay ang `output_path` |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | Hindi |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | Hindi |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | Hindi |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | Hindi |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | Hindi |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | Hindi |
| `run_translation` | Run project-level translation like the CLI. | Oo kapag `dry_run=false` at `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Oo kapag `dry_run=false` at `confirm_write=true` |
| `run_review` | Run deterministic review checks. | Hindi |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | Hindi |
| `list_supported_languages` | List supported target language codes. | Hindi |
| `get_api_overview` | Describe available MCP workflows and tools. | Hindi |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Copy-Paste Examples

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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

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
| The MCP client cannot find `co-op-translator-mcp`. | Gamitin ang absolute na Python executable path at ang `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Tawagan ang `get_configuration_status` at kumpirmahin na may available na LLM provider. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Gamitin ang `start_markdown_agent_translation` / `finish_markdown_agent_translation` o ang mga katumbas para sa notebook upang ang host agent ang magsalin ng mga chunk. |
| Image translation fails. | Kumpirmahin na naka-set ang Azure AI Vision variables at tawagan ang `get_configuration_status`. |
| Repository translation does not write files. | Itakda lamang ang `dry_run=false` at `confirm_write=true` pagkatapos ng tahasang pag-apruba ng user. |
| Changes to client config do not appear. | I-restart o i-reload ang MCP client. |

## Safety Notes

- Ang mga tawag sa MCP tool ay kinokontrol ng modelo ng host application, kaya ang pagsasalin ng repositoryo ay dry-run bilang default.
- Ang buong pagsasalin ng repositoryo ay maaaring lumikha, mag-update, o mag-alis ng maraming mga file. Humingi ng tahasang pag-apruba ng user bago itakda ang `confirm_write=true`.
- Hindi ibinabalik ng configuration status tool ang mga API key, endpoint, o iba pang secret na halaga.
- Nagbabalik ang pagsasalin ng imahe ng base64 image data. Maaari mag-produce ng malalaking tugon ang malalaking imahe.
- Nagbabalik ang agent-assisted tools ng source chunks at mga prompt sa MCP host. Gamitin ang mga ito lamang sa content na komportable ang user na ipapadala sa host agent model.