# MCP 伺服器

Co-op Translator 包含一個 Model Context Protocol 伺服器，供代理（agents）、編輯器和相容 MCP 的用戶端使用。

對於預設的本機設定，用戶不需要手動另外維持一個獨立伺服器。使用者只需在 MCP 用戶端中設定，當需要 Co-op Translator 工具時，用戶端會自動在 `stdio` 上啟動 `co-op-translator-mcp`。

如果你正在於 CLI、Python API 與 MCP 之間做選擇，請先參考 [選擇你的工作流程](workflows.md)。

當代理或編輯器應該直接呼叫 Co-op Translator 時，請使用 MCP：

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 伺服器包裝了在 [Python API](api.md) 中記錄的相同公開 Python API。由提供者支援的工具使用與 CLI 和 Python API 相同的已設定提供者。由代理協助的工具會準備要供 MCP 主機代理翻譯的區塊，然後使用 Co-op Translator 重建最終的 Markdown 或 notebook。

## 第 1 步：安裝並設定 Co-op Translator

在你的 MCP 用戶端將會使用的 Python 環境中安裝 Co-op Translator：

```bash
pip install co-op-translator
```

對於來自此 repository 的本機開發，請以可編輯模式安裝套件：

```bash
pip install -e .
```

選擇你的 MCP 用戶端將使用的翻譯模式：

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

如果你要在像 Codex 或 Claude Code 這類代理中開始處理 Markdown 或 notebook 翻譯，請先使用 agent-assisted 模式。當你希望 Co-op Translator 本身呼叫你已設定的提供者、當你在翻譯影像或當你要執行像 CLI 那樣的倉庫層級翻譯時，請使用 provider-backed 模式。

僅對 provider-backed 工作流程設定提供者憑證：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

provider-backed 的影像翻譯另外還需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## 第 2 步：設定你的 MCP 用戶端

對於一般的本機 `stdio` 設定，將 Co-op Translator 新增到你的 MCP 用戶端設定中。用戶端會自動啟動與停止該程序。

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

在 Windows 上的原始程式碼 checkout 設定：

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

在 macOS 或 Linux 上的原始程式碼 checkout 設定：

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

變更 MCP 用戶端設定後，請重新啟動或重新載入用戶端，以便它能夠偵測到新的伺服器。

## 第 3 步：在用戶端驗證伺服器

請求 MCP 用戶端列出可用的工具，或先呼叫其中一個唯讀的輔助工具：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步檢查：

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirms the server is reachable and shows available workflows. |
| `list_supported_languages` | Confirms packaged language data can be loaded. |
| `get_configuration_status` | Confirms LLM and Vision provider availability without exposing secret values. |

## 第 4 步：選擇工作流程

### 翻譯單一檔案或文件

當 MCP 用戶端已經擁有文件內容或影像路徑，且你希望 Co-op Translator 呼叫已設定的翻譯提供者時，請使用 provider-backed 內容工具。

對於 Markdown：

1. 使用 `document`、`language_code`（以及可選的 `source_path`）呼叫 `translate_markdown_content`。
2. 如果翻譯結果會寫入 Co-op Translator 的輸出佈局，請呼叫 `rewrite_markdown_paths`。
3. 讓用戶端寫入或回傳最終的 `content`。

對於 notebooks：

1. 使用 notebook 的 JSON 與 `language_code` 呼叫 `translate_notebook_content`。
2. 如果翻譯後的 notebook 連結需要針對目標路徑調整，呼叫 `rewrite_notebook_paths`。
3. 寫入或回傳最終的 notebook JSON。

對於影像：

1. 使用 `image_path`、`language_code` 和可選的 `root_dir` 或 `fast_mode` 呼叫 `translate_image_content`。
2. 讀取回傳的 `data_base64` 與 `mime_type`。
3. 如果提供了 `output_path`，翻譯後的影像也會儲存到該路徑。

內容工具不會執行專案發現、更新 metadata、加入免責聲明或自動重寫路徑。如果你希望主機代理在沒有 Co-op Translator LLM 提供者憑證的情況下翻譯 Markdown 或 notebook 區塊，請使用下面的 agent-assisted 工作流程。

### 使用主機代理模型進行翻譯

當你希望 MCP 主機代理（例如程式編寫助手）產生翻譯文字，而不是為 Co-op Translator 設定 Azure OpenAI 或 OpenAI 時，請使用 agent-assisted 工具。

在基於聊天的 MCP 用戶端中，通常不需要你手動撰寫工具 JSON。請求代理使用 agent-assisted 工作流程：

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

對於 notebooks，使用相同的模式：

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

如果你的 MCP 用戶端支援 server prompts，請使用 `agent_assisted_markdown_translation_prompt` 讓用戶端載入相同的工作流程指示。

對於 Markdown：

1. 使用 `document`、`language_code`（以及可選的 `source_path`）呼叫 `start_markdown_agent_translation`。
2. 在主機代理中依據每個回傳的區塊 `prompt` 翻譯每個區塊。
3. 使用原始的 `job` 與包含 `chunk_id` 與 `translated_text` 的翻譯後區塊呼叫 `finish_markdown_agent_translation`。
4. 如果內容會被寫入翻譯後的目標路徑，呼叫 `rewrite_markdown_paths`。

對於 notebooks：

1. 使用 notebook JSON 與 `language_code` 呼叫 `start_notebook_agent_translation`。
2. 在主機代理中翻譯每個回傳的區塊。
3. 使用原始的 `job` 與翻譯後的區塊呼叫 `finish_notebook_agent_translation`。
4. 如果翻譯後的 notebook 連結需要針對目標路徑調整，呼叫 `rewrite_notebook_paths`。

Agent-assisted 工具不會從 Co-op Translator 呼叫 Azure OpenAI 或 OpenAI。主機代理負責翻譯回傳的區塊。Co-op Translator 處理 Markdown 分塊、保留佔位符、frontmatter 重建、notebook 儲存格替換，以及翻譯後的正規化處理。

### 翻譯整個倉庫

當使用者希望 Co-op Translator 的行為類似 `translate` CLI 時，使用 `run_translation`。

倉庫翻譯預設為 `dry_run=true`，以便代理先檢查範圍再進行檔案變更：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

要允許寫入，呼叫方必須同時設為 `dry_run=false` 與 `confirm_write=true`：

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` 被暴露為 `run_translation` 的相容別名。

### 審查翻譯後的輸出

對於不需要 LLM 或 Vision 憑證的確定性檢查，請使用 `run_review`：

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

結果會包含擷取到的文字輸出以及在可用時的結構化審查摘要。

## 手動啟動伺服器

手動執行主要用於除錯或類似長期執行伺服器的傳輸層。

除錯預設的 stdio 伺服器：

```bash
co-op-translator-mcp
```

從原始程式碼 checkout 執行：

```bash
python -m co_op_translator.mcp.server
```

執行長期存在的 HTTP 或 SSE 伺服器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

對於本機編輯器與代理整合，建議優先使用第 2 步中由用戶端管理的 `stdio` 設定。

## 工具

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

## 資源

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## 提示詞

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## 複製貼上範例

翻譯 Markdown 內容：

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

重寫翻譯後的 Markdown 連結：

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

使用主機代理模型翻譯 Markdown：

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

在主機代理翻譯每個回傳的區塊後，使用 `start_markdown_agent_translation` 回傳的完整 `job` 物件來完成工作：

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

預覽倉庫翻譯：

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

## 疑難排解

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## 安全注意事項

- MCP 工具呼叫由主機應用程式控制模型，因此倉庫翻譯預設為 dry-run。
- 完整的倉庫翻譯可能會建立、更新或移除大量檔案。在將 `confirm_write=true` 設為 true 之前，務必取得明確的使用者批准。
- 設定狀態工具絕不會回傳 API keys、端點或其他祕密值。
- 影像翻譯會回傳 base64 影像資料。大型影像可能會產生龐大的工具回應。
- Agent-assisted 工具會回傳來源區塊與提示給 MCP 主機。僅在使用者願意將內容傳送給該主機代理模型時才使用它們。