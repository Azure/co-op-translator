# MCP 伺服器

Co-op Translator 包含一個供代理、編輯器與 MCP 相容用戶端使用的 Model Context Protocol 伺服器。

在預設的本機設定中，使用者不需要手動維持一個獨立伺服器執行。使用者只要設定其 MCP 用戶端，當需要 Co-op Translator 工具時，該用戶端會自動透過 `stdio` 啟動 `co-op-translator-mcp`。

如果您在 CLI、Python API 與 MCP 之間猶豫，請從 [選擇您的工作流程](workflows.md) 開始。

當代理或編輯器應直接呼叫 Co-op Translator 時，請使用 MCP：

| 使用者目標 | MCP 工具 |
| --- | --- |
| 翻譯單一 Markdown 文件、筆記本或影像 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| 使用主機代理模型翻譯 Markdown 或筆記本內容 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 在選擇輸出路徑後重寫已翻譯的 Markdown 或筆記本連結 | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 如同 CLI 般翻譯整個倉庫 | `run_translation`, `translate_project` |
| 在沒有 LLM 憑證下審閱翻譯輸出 | `run_review` |
| 檢視能力與環境狀態 | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 伺服器封裝了在 [Python API](api.md) 中記載的相同公開 Python API。依賴提供者的工具使用與 CLI 與 Python API 相同的已配置提供者。代理協助工具會為 MCP 主機代理準備要翻譯的區塊，然後使用 Co-op Translator 重建最終的 Markdown 或筆記本。

## 第一步：安裝並設定 Co-op Translator

在 MCP 用戶端會使用的 Python 環境中安裝 Co-op Translator：

```bash
pip install co-op-translator
```

若從此儲存庫進行本機開發，請以可編輯模式安裝此套件：

```bash
pip install -e .
```

選擇您的 MCP 用戶端將使用的翻譯模式：

| 模式 | 用途 | 憑證 |
| --- | --- | --- |
| Provider-backed | Co-op Translator 呼叫 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, 或 `run_translation`。 | 翻譯需要 Azure OpenAI、OpenAI 或 Anthropic。影像翻譯還需要 Azure AI Vision。 |
| Agent-assisted | MCP 主機代理會翻譯由 `start_markdown_agent_translation` 或 `start_notebook_agent_translation` 回傳的區塊。 | Markdown 或筆記本區塊不需要 Co-op Translator 的 LLM 提供者憑證。影像翻譯目前尚未包含在代理協助模式中。 |

如果您在像 Codex 或 Claude Code 這類代理內開始進行 Markdown 或筆記本翻譯，請從代理協助模式開始。當您希望由 Co-op Translator 本身呼叫您設定的提供者、翻譯影像，或執行如同 CLI 的倉庫層級翻譯時，請使用 provider-backed 模式。

為依賴提供者的工作流程設定一個提供者：

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 或 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# 或 Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

依賴提供者的影像翻譯另外需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    代理協助模式目前涵蓋 Markdown 與筆記本的 Markdown 儲存格。影像翻譯仍然使用依賴提供者的影像流程，並且需要 Azure AI Vision 來進行 OCR 與版面感知的渲染。

## 第二步：設定您的 MCP 用戶端

對於一般的本機 `stdio` 設定，將 Co-op Translator 加入 MCP 用戶端設定。用戶端會自動啟動與停止該程序。

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

在 Windows 上以原始程式碼檢出（source checkout）的設定：

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

在 macOS 或 Linux 上以原始程式碼檢出（source checkout）的設定：

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

更改 MCP 用戶端設定後，重新啟動或重新載入用戶端以便其能夠偵測到新的伺服器。

## 第三步：在用戶端驗證伺服器

請求 MCP 用戶端列出可用工具，或先呼叫其中一個唯讀的輔助工具：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步檢查：

| 工具 | 檢查項目 |
| --- | --- |
| `get_api_overview` | 確認伺服器可連線並顯示可用的工作流程。 |
| `list_supported_languages` | 確認封裝的語言資料可以載入。 |
| `get_configuration_status` | 在不洩露秘密值的情況下，確認 LLM 與 Vision 提供者的可用性。 |

## 第四步：選擇工作流程

### 翻譯單一檔案或文件

當 MCP 用戶端已經擁有文件內容或影像路徑，且希望 Co-op Translator 呼叫已設定的翻譯提供者時，請使用依賴提供者的內容工具。

對於 Markdown：

1. 使用 `document`、`language_code`，以及可選的 `source_path` 呼叫 `translate_markdown_content`。
2. 如果翻譯結果將寫入 Co-op Translator 的輸出佈局，呼叫 `rewrite_markdown_paths`。
3. 讓用戶端寫入或回傳最終的 `content`。

對於筆記本：

1. 使用筆記本 JSON 與 `language_code` 呼叫 `translate_notebook_content`。
2. 如果已翻譯的筆記本連結需要針對目標路徑調整，呼叫 `rewrite_notebook_paths`。
3. 寫入或回傳最終的筆記本 JSON。

對於影像：

1. 使用 `image_path`、`language_code` 以及可選的 `root_dir` 或 `fast_mode` 呼叫 `translate_image_content`。
2. 讀取回傳的 `data_base64` 與 `mime_type`。
3. 如果提供了 `output_path`，翻譯後的影像也會儲存到該路徑。

這些內容工具不會執行專案偵測、更新 metadata、加入免責聲明或自動重寫路徑。如果您希望主機代理在沒有 Co-op Translator LLM 提供者憑證的情況下翻譯 Markdown 或筆記本的區塊，請使用下方的代理協助工作流程。

### 使用主機代理模型翻譯

當您希望 MCP 主機代理（例如程式助理）產生翻譯文本，而不是為 Co-op Translator 設定 LLM 提供者時，請使用代理協助工具。

在以聊天為基礎的 MCP 用戶端中，通常不需要自己撰寫工具的 JSON。請要求代理使用代理協助工作流程：

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

如果您的 MCP 用戶端支援伺服器提示（server prompts），使用 `agent_assisted_markdown_translation_prompt` 讓用戶端載入相同的工作流程指示。

對於 Markdown：

1. 使用 `document`、`language_code`，以及可選的 `source_path` 呼叫 `start_markdown_agent_translation`。
2. 在主機代理中依據各區塊的 `prompt` 翻譯每個回傳的區塊。
3. 使用原始的 `job` 以及以 `chunk_id` 和 `translated_text` 表示的已翻譯區塊呼叫 `finish_markdown_agent_translation`。
4. 如果內容將寫入翻譯後的目標路徑，呼叫 `rewrite_markdown_paths`。

對於筆記本：

1. 使用筆記本 JSON 與 `language_code` 呼叫 `start_notebook_agent_translation`。
2. 在主機代理中翻譯每個回傳的區塊。
3. 使用原始的 `job` 與已翻譯的區塊呼叫 `finish_notebook_agent_translation`。
4. 如果已翻譯的筆記本連結需要調整目標路徑，呼叫 `rewrite_notebook_paths`。

代理協助工具不會由 Co-op Translator 呼叫已配置的 LLM 提供者。主機代理負責翻譯回傳的區塊。Co-op Translator 負責 Markdown 分區、保留佔位符、重建 frontmatter、替換筆記本儲存格，以及翻譯後的正規化處理。

### 翻譯整個倉庫

當使用者希望 Co-op Translator 的行為像 `translate` CLI 時，使用 `run_translation`。

倉庫翻譯預設為 `dry_run=true`，以便代理在檔案變更前檢查範圍：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` 的結果包含一個帶版本的
`co-op.translation.event.v1` 進度事件。MCP 用戶端應使用像是
`type`、`stage_key`、`completed`、`total` 以及 `current_path` 這類欄位，而不是
解析擷取的主控台文字。若要將這些事件
寫入 NDJSON 檔案，請傳入 `json_events_path`。

為了允許寫入，呼叫者必須同時設定 `dry_run=false` 與 `confirm_write=true`：

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` 被當作 `run_translation` 的相容別名公開。

### 審查翻譯輸出

對於不需要 LLM 或 Vision 憑證的確定性檢查，使用 `run_review`：

!!! note "Beta"
    MCP 暴露了測試版的 `run_review` API。它對唯讀的審查工作流程是安全的，但檢查項目與問題的結構可能會演進。

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

結果包含擷取的文字輸出，以及在可用時的結構化審查摘要。

## 手動執行伺服器

手動執行主要用於除錯或用於像長時間執行的伺服器那樣運作的傳輸層。

除錯預設的 stdio 伺服器：

```bash
co-op-translator-mcp
```

從原始程式碼檢出執行：

```bash
python -m co_op_translator.mcp.server
```

執行長時間運行的 HTTP 或 SSE 伺服器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

對於本機的編輯器與代理整合，優先使用步驟 2 中由用戶端管理的 `stdio` 設定。

## 工具

| 工具 | 目的 | 是否寫入檔案 |
| --- | --- | --- |
| `translate_markdown_content` | 翻譯一個 Markdown 字串。 | 否 |
| `translate_notebook_content` | 翻譯筆記本 JSON 中的 Markdown 儲存格。 | 否 |
| `translate_image_content` | 翻譯單張影像中的文字並回傳 base64 影像資料。 | 選擇性，僅在提供 `output_path` 時會寫入 |
| `start_markdown_agent_translation` | 為主機代理準備 Markdown 區塊以便在沒有 Co-op Translator LLM 憑證的情況下翻譯。 | 否 |
| `finish_markdown_agent_translation` | 從主機代理翻譯的區塊重建 Markdown。 | 否 |
| `start_notebook_agent_translation` | 為主機代理準備筆記本中的 Markdown 儲存格區塊進行翻譯。 | 否 |
| `finish_notebook_agent_translation` | 從主機代理翻譯的區塊重建筆記本 JSON。 | 否 |
| `rewrite_markdown_paths` | 為翻譯後的目標重寫 Markdown 主體與 frontmatter 的路徑。 | 否 |
| `rewrite_notebook_paths` | 重寫筆記本 Markdown 儲存格內的路徑。 | 否 |
| `run_translation` | 執行如同 CLI 的專案層級翻譯。 | 當 `dry_run=false` 且 `confirm_write=true` 時會寫入 |
| `translate_project` | `run_translation` 的相容別名。 | 當 `dry_run=false` 且 `confirm_write=true` 時會寫入 |
| `run_review` | 執行確定性的審查檢查。 | 否 |
| `get_configuration_status` | 報告已配置的 LLM 與 Vision 提供者狀態而不暴露秘密。 | 否 |
| `list_supported_languages` | 列出支援的目標語言代碼。 | 否 |
| `get_api_overview` | 描述可用的 MCP 工作流程與工具。 | 否 |

## 資源

| 資源 URI | 目的 |
| --- | --- |
| `co-op://api` | 工作流程與工具的 JSON 概覽。 |
| `co-op://supported-languages` | 支援語言代碼的 JSON 列表。 |
| `co-op://configuration` | 不含秘密的提供者可用性摘要（JSON）。 |

## 提示詞

| 提示詞 | 目的 |
| --- | --- |
| `translate_markdown_document_prompt` | 指導 MCP 用戶端進行內容翻譯以及可選的路徑重寫。 |
| `agent_assisted_markdown_translation_prompt` | 指導 MCP 用戶端在沒有 Co-op Translator LLM 提供者憑證的情況下，透過主機代理進行 Markdown 翻譯。 |
| `translate_repository_prompt` | 指導 MCP 用戶端先以預覽（dry-run）方式再進行倉庫翻譯。 |

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

重寫已翻譯的 Markdown 連結：

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

在主機代理翻譯每個回傳的區塊後，使用 `start_markdown_agent_translation` 回傳的完整 `job` 物件完成該工作：

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

| 問題 | 嘗試項目 |
| --- | --- |
| MCP 用戶端無法找到 `co-op-translator-mcp`。 | 使用絕對的 Python 可執行檔路徑，以及 `["-m", "co_op_translator.mcp.server"]` 的原始程式碼檢出設定。 |
| 伺服器已列出但翻譯失敗。 | 呼叫 `get_configuration_status` 並確認有可用的 LLM 提供者。 |
| 想在沒有提供者憑證下進行 Markdown 或筆記本翻譯。 | 使用 `start_markdown_agent_translation` / `finish_markdown_agent_translation` 或對應的筆記本 API，讓主機代理翻譯這些區塊。 |
| 影像翻譯失敗。 | 確認已設定 Azure AI Vision 相關變數，並呼叫 `get_configuration_status`。 |
| 倉庫翻譯未寫入檔案。 | 僅在明確取得使用者同意後，將 `dry_run=false` 與 `confirm_write=true` 設定。 |
| 對用戶端設定的變更未出現。 | 重新啟動或重新載入 MCP 用戶端。 |

## 安全注意事項

- MCP 工具的呼叫由主機應用控制，因此倉庫翻譯預設為 dry-run。
- 完整的倉庫翻譯可能會建立、更新或移除大量檔案。在設定 `confirm_write=true` 前，務必取得使用者明確同意。
- 配置狀態工具絕不會回傳 API 金鑰、端點或其他秘密值。
- 影像翻譯會回傳 base64 影像資料。大型影像可能會產生龐大的工具回應。
- 代理協助工具會將原始區塊與提示詞回傳給 MCP 主機。僅在使用者願意將內容傳送給該主機代理模型的情況下使用。