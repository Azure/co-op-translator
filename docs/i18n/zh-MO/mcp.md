# MCP Server

Co-op Translator 包括一個 Model Context Protocol 伺服器，供代理、編輯器和相容 MCP 的用戶端使用。

在預設的本地設定中，用戶不需要手動維持一個獨立的伺服器。用戶設定其 MCP 用戶端，當需要使用 Co-op Translator 工具時，該用戶端會自動透過 `stdio` 啟動 `co-op-translator-mcp`。

如果你在 CLI、Python API 與 MCP 之間抉擇，請先參考 [Choose Your Workflow](workflows.md)。

當代理或編輯器需要直接呼叫 Co-op Translator 時，使用 MCP：

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 伺服器包裝了在 [Python API](api.md) 中記載的相同公開 Python API。由提供者支援的工具使用與 CLI 及 Python API 相同的已設定提供者。由代理協助的工具會為 MCP 主機代理準備區塊以供翻譯，然後使用 Co-op Translator 重建最終的 Markdown 或筆記本。

## Step 1: Install and Configure Co-op Translator

在你的 MCP 用戶端會使用的 Python 環境中安裝 Co-op Translator：

```bash
pip install co-op-translator
```

若要從此版本庫進行本地開發，請以可編輯模式安裝套件：

```bash
pip install -e .
```

選擇你的 MCP 用戶端將使用的翻譯模式：

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

如果你在像 Codex 或 Claude Code 這類代理內開始進行 Markdown 或筆記本翻譯，請從 agent-assisted 模式開始。當你希望 Co-op Translator 自行呼叫你所設定的提供者、要翻譯影像，或要執行像 CLI 一樣的整個儲存庫翻譯時，請使用 provider-backed 模式。

僅為 provider-backed 工作流程設定提供者憑證：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed 的影像翻譯另外需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

對於一般的本地 `stdio` 設定，將 Co-op Translator 加到你的 MCP 用戶端設定中。用戶端會自動啟動與停止該程序。

已安裝套件的設定：

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

Windows 上的原始碼取出（source checkout）設定：

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

macOS 或 Linux 上的原始碼取出（source checkout）設定：

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

在變更 MCP 用戶端設定後，重新啟動或重新載入該用戶端，以便它能發現新的伺服器。

## Step 3: Verify the Server in the Client

請求 MCP 用戶端列出可用工具，或先呼叫其中一個唯讀輔助工具：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步檢查：

| Tool | What to check |
| --- | --- |
| `get_api_overview` | 確認伺服器可達並顯示可用的工作流程。 |
| `list_supported_languages` | 確認可載入打包的語言資料。 |
| `get_configuration_status` | 確認 LLM 與 Vision 提供者可用性而不暴露機密值。 |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

當 MCP 用戶端已經擁有文件內容或影像路徑，且你希望 Co-op Translator 呼叫已設定的翻譯提供者時，使用 provider-backed 的內容工具。

對於 Markdown：

1. 呼叫 `translate_markdown_content`，傳入 `document`、`language_code`，以及選擇性的 `source_path`。
2. 如果翻譯結果將寫入 Co-op Translator 的輸出佈局，呼叫 `rewrite_markdown_paths`。
3. 讓用戶端寫入或返回最終的 `content`。

對於筆記本：

1. 呼叫 `translate_notebook_content`，傳入筆記本 JSON 與 `language_code`。
2. 如需將翻譯後的筆記本連結調整為目標路徑，呼叫 `rewrite_notebook_paths`。
3. 寫入或返回最終的筆記本 JSON。

對於影像：

1. 呼叫 `translate_image_content`，傳入 `image_path`、`language_code`，以及選擇性的 `root_dir` 或 `fast_mode`。
2. 讀取回傳的 `data_base64` 與 `mime_type`。
3. 若提供了 `output_path`，翻譯後的影像也會儲存到該路徑。

內容工具不會執行專案發現、metadata 更新、免責聲明或自動路徑重寫。若你希望主機代理在沒有 Co-op Translator 的 LLM 提供者憑證下翻譯 Markdown 或筆記本區塊，請使用下方的 agent-assisted 工作流程。

### Translate with the Host Agent Model

當你希望 MCP 主機代理（例如程式助理）產生翻譯文本，而不是為 Co-op Translator 設定 Azure OpenAI 或 OpenAI 時，使用 agent-assisted 工具。

在以聊天為基礎的 MCP 用戶端中，通常不需要你自己撰寫工具 JSON。請求代理使用 agent-assisted 工作流程：

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

對於筆記本，使用相同的模式：

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

如果你的 MCP 用戶端支援伺服器提示（server prompts），使用 `agent_assisted_markdown_translation_prompt` 讓用戶端載入相同的工作流程指示。

對於 Markdown：

1. 呼叫 `start_markdown_agent_translation`，傳入 `document`、`language_code`，以及選擇性的 `source_path`。
2. 在主機代理中依照區塊的 `prompt` 翻譯每個回傳的區塊。
3. 使用原始的 `job` 與以 `chunk_id` 和 `translated_text` 傳回的翻譯區塊呼叫 `finish_markdown_agent_translation`。
4. 如果內容會寫入翻譯後的目標路徑，呼叫 `rewrite_markdown_paths`。

對於筆記本：

1. 呼叫 `start_notebook_agent_translation`，傳入筆記本 JSON 與 `language_code`。
2. 在主機代理中翻譯每個回傳的區塊。
3. 使用原始的 `job` 與翻譯後的區塊呼叫 `finish_notebook_agent_translation`。
4. 若需要將翻譯後的筆記本連結調整成目標路徑，呼叫 `rewrite_notebook_paths`。

Agent-assisted 工具不會從 Co-op Translator 呼叫 Azure OpenAI 或 OpenAI。主機代理負責翻譯回傳的區塊。Co-op Translator 負責 Markdown 分段、保留佔位符、frontmatter 重建、筆記本儲存格替換以及翻譯後的正規化處理。

### Translate an Entire Repository

當用戶希望 Co-op Translator 的行為像 `translate` CLI 時，使用 `run_translation`。

專案翻譯預設為 `dry_run=true`，以便代理在檔案變更前能先檢查範圍：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

若要允許寫入，呼叫方必須同時設定 `dry_run=false` 與 `confirm_write=true`：

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` 被作為 `run_translation` 的相容別名公開。

### Review Translated Output

在不需要 LLM 或 Vision 憑證的情況下，使用 `run_review` 進行決定性檢查：

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

當可用時，結果包含擷取的文字輸出與結構化的審查摘要。

## Manual Server Runs

手動執行主要用於除錯或當傳輸層像長期運行的伺服器時使用。

除錯預設的 stdio 伺服器：

```bash
co-op-translator-mcp
```

從原始碼取出執行：

```bash
python -m co_op_translator.mcp.server
```

執行長期運行的 HTTP 或 SSE 伺服器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

對於本地編輯器與代理整合，偏好在第 2 步中由用戶端管理的 `stdio` 設定。

## Tools

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
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.