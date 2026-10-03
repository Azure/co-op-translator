# MCP 伺服器

Co-op Translator 包含一個供代理、編輯器和相容 MCP 的用戶端使用的 Model Context Protocol 伺服器。

在預設的本地設定中，用戶不需要手動另外運行一個伺服器。用戶只要配置其 MCP 用戶端，當需要 Co-op Translator 的工具時，該用戶端會自動透過 `stdio` 啟動 `co-op-translator-mcp`。

如果你正在在 CLI、Python API 與 MCP 之間抉擇，請從 [選擇你的工作流程](workflows.md) 開始。

當代理或編輯器應直接呼叫 Co-op Translator 時，使用 MCP：

| 用戶目標 | MCP 工具 |
| --- | --- |
| 翻譯一個 Markdown 文件、筆記本或圖像 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| 用主機代理模型翻譯 Markdown 或筆記本內容 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 在選擇輸出路徑後重寫已翻譯的 Markdown 或筆記本連結 | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 像 CLI 一樣翻譯整個儲存庫 | `run_translation`, `translate_project` |
| 在沒有 LLM 憑證的情況下審閱翻譯輸出 | `run_review` |
| 檢查功能與環境狀態 | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 伺服器包裹了在 [Python API](api.md) 文件中說明的相同公開 Python API。以 provider 為後端的工具會使用與 CLI 及 Python API 相同配置的提供者。由代理協助的工具會為 MCP 主機代理準備要翻譯的片段，然後使用 Co-op Translator 重建最終的 Markdown 或筆記本。

## 第一步：安裝並配置 Co-op Translator

在你的 MCP 用戶端所使用的 Python 環境中安裝 Co-op Translator：

```bash
pip install co-op-translator
```

如果要從此倉庫進行本地開發，請以可編輯模式安裝套件：

```bash
pip install -e .
```

選擇你的 MCP 用戶端將使用的翻譯模式：

| 模式 | 使用情境 | 憑證 |
| --- | --- | --- |
| 以提供者為後端 | Co-op Translator 會呼叫 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, 或 `run_translation`。 | 翻譯需要 Azure OpenAI、OpenAI 或 Anthropic。影像翻譯還需要 Azure AI Vision。 |
| 代理協助 | MCP 主機代理會翻譯由 `start_markdown_agent_translation` 或 `start_notebook_agent_translation` 回傳的片段。 | Markdown 或筆記本片段不需要 Co-op Translator 的 LLM 提供者憑證。影像翻譯尚未包含在代理協助模式中。 |

如果你是在像 Codex 或 Claude Code 這樣的代理內開始處理 Markdown 或筆記本翻譯，請從代理協助模式開始。當你希望 Co-op Translator 自行呼叫你已配置的提供者、或要翻譯影像、或要執行像 CLI 那樣的儲存庫層級翻譯時，請使用以提供者為後端的模式。

為以提供者為後端的工作流程配置一個提供者：

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

以提供者為後端的影像翻譯額外需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    代理協助模式目前涵蓋 Markdown 和筆記本的 Markdown 儲存格。影像翻譯仍然使用以提供者為後端的影像流程，並且需要 Azure AI Vision 以支援 OCR 與版面感知的呈現。

## 第二步：配置你的 MCP 用戶端

對於一般的本地 `stdio` 設定，將 Co-op Translator 新增到你的 MCP 用戶端配置中。用戶端會自動啟動與停止該程序。

已安裝套件的配置：

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

在 Windows 上從原始碼檢出 (source checkout) 的配置：

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

在 macOS 或 Linux 上從原始碼檢出 (source checkout) 的配置：

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

在更改 MCP 用戶端配置後，重新啟動或重新載入該用戶端，以便它能發現新的伺服器。

## 第三步：在用戶端驗證伺服器

請求 MCP 用戶端列出可用工具，或先呼叫其中一個只讀的輔助工具：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步檢查：

| 工具 | 要檢查的項目 |
| --- | --- |
| `get_api_overview` | 確認伺服器可連線並顯示可用的工作流程。 |
| `list_supported_languages` | 確認已打包的語言資料可以載入。 |
| `get_configuration_status` | 在不暴露機密值的情況下，確認 LLM 與 Vision 提供者的可用性。 |

## 第四步：選擇工作流程

### 翻譯單一檔案或文件

當 MCP 用戶端已經有文件內容或影像路徑，且希望 Co-op Translator 呼叫已配置的翻譯提供者時，請使用以提供者為後端的內容工具。

對於 Markdown：

1. 呼叫 `translate_markdown_content`，傳入 `document`、`language_code`，以及可選的 `source_path`。
2. 如果翻譯結果會寫入 Co-op Translator 的輸出版面，則呼叫 `rewrite_markdown_paths`。
3. 讓用戶端寫入或回傳最終的 `content`。

對於筆記本：

1. 以筆記本 JSON 和 `language_code` 呼叫 `translate_notebook_content`。
2. 如需針對目標路徑調整已翻譯筆記本的連結，則呼叫 `rewrite_notebook_paths`。
3. 寫入或回傳最終的筆記本 JSON。

對於影像：

1. 使用 `image_path`、`language_code`，以及可選的 `root_dir` 或 `fast_mode` 呼叫 `translate_image_content`。
2. 讀取回傳的 `data_base64` 與 `mime_type`。
3. 如果提供了 `output_path`，翻譯後的影像也會儲存到該路徑。

內容工具不會執行專案探索、更新 metadata、加上免責聲明，或自動重寫路徑。如果你希望主機代理在沒有 Co-op Translator LLM 提供者憑證的情況下翻譯 Markdown 或筆記本片段，請使用下方的代理協助工作流程。

### 使用主機代理模型進行翻譯

當你希望 MCP 主機代理（例如程式輔助工具）產生翻譯文本，而不是為 Co-op Translator 配置 LLM 提供者時，請使用代理協助工具。

在基於聊天的 MCP 用戶端中，通常不需要自行撰寫工具的 JSON。請求代理使用代理協助工作流程：

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

對於筆記本，使用相同模式：

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

如果你的 MCP 用戶端支援伺服器提示 (server prompts)，請使用 `agent_assisted_markdown_translation_prompt` 讓用戶端載入相同的工作流程指示。

對於 Markdown：

1. 呼叫 `start_markdown_agent_translation`，傳入 `document`、`language_code`，以及可選的 `source_path`。
2. 在主機代理中依據每個片段的 `prompt` 翻譯回傳的每個片段。
3. 使用原始的 `job` 與已翻譯的片段（以 `chunk_id` 和 `translated_text`）呼叫 `finish_markdown_agent_translation`。
4. 如果內容會寫入翻譯後的目標路徑，則呼叫 `rewrite_markdown_paths`。

對於筆記本：

1. 使用筆記本 JSON 與 `language_code` 呼叫 `start_notebook_agent_translation`。
2. 在主機代理中翻譯每個回傳的片段。
3. 使用原始的 `job` 與已翻譯的片段呼叫 `finish_notebook_agent_translation`。
4. 若已翻譯的筆記本連結需要針對目標路徑調整，則呼叫 `rewrite_notebook_paths`。

代理協助工具不會讓 Co-op Translator 呼叫已配置的 LLM 提供者。主機代理負責翻譯回傳的片段。Co-op Translator 負責 Markdown 切片、占位符保留、frontmatter 重建、筆記本儲存格替換，以及翻譯後的標準化處理。

### 翻譯整個儲存庫

當使用者希望 Co-op Translator 表現得像 `translate` CLI 時，使用 `run_translation`。

儲存庫翻譯預設為 `dry_run=true`，以便代理在檔案更動前檢視範圍：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` 的結果包含一個帶版本的 `events` 陣列，
包含 `co-op.translation.event.v1` 的進度事件。MCP 用戶端應該使用像是
`type`、`stage_key`、`completed`、`total` 和 `current_path` 等欄位，而不是
解析擷取的主控台文字。傳入 `json_events_path` 也可將這些事件寫入
NDJSON 檔案。

要允許寫入，呼叫方必須同時設定 `dry_run=false` 與 `confirm_write=true`：

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` 作為 `run_translation` 的相容別名公開。

### 審閱翻譯輸出

使用 `run_review` 進行不需要 LLM 或 Vision 憑證的確定性檢查：

!!! note "Beta"
    MCP 暴露了測試階段的 `run_review` API。它對唯讀的審查工作流程是安全的，但審查檢查項目與問題 schema 未來可能會有所變動。

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

結果會包含擷取的文字輸出以及（如有）結構化的審查摘要。

## 手動執行伺服器

手動執行主要用於除錯或類似長期運行伺服器的傳輸方式。

偵錯預設的 stdio 伺服器：

```bash
co-op-translator-mcp
```

從原始碼檢出執行：

```bash
python -m co_op_translator.mcp.server
```

執行長期運行的 HTTP 或 SSE 伺服器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

對於本地編輯器與代理整合，優先使用步驟 2 中由用戶端管理的 `stdio` 配置。

## 工具

| 工具 | 用途 | 是否寫入檔案 |
| --- | --- | --- |
| `translate_markdown_content` | 翻譯一段 Markdown 字串。 | 否 |
| `translate_notebook_content` | 翻譯筆記本 JSON 中的 Markdown 儲存格。 | 否 |
| `translate_image_content` | 翻譯圖片中的文字並回傳 base64 影像資料。 | 選用（僅在提供 `output_path` 時） |
| `start_markdown_agent_translation` | 準備 Markdown 片段讓主機代理在沒有 Co-op Translator LLM 憑證的情況下翻譯。 | 否 |
| `finish_markdown_agent_translation` | 從主機代理已翻譯的片段重建 Markdown。 | 否 |
| `start_notebook_agent_translation` | 準備筆記本中 Markdown 儲存格的片段讓主機代理翻譯。 | 否 |
| `finish_notebook_agent_translation` | 從主機代理已翻譯的片段重建筆記本 JSON。 | 否 |
| `rewrite_markdown_paths` | 為翻譯後的目標重寫 Markdown 內容與 frontmatter 中的路徑。 | 否 |
| `rewrite_notebook_paths` | 重寫筆記本 Markdown 儲存格內的路徑。 | 否 |
| `run_translation` | 像 CLI 一樣執行專案層級翻譯。 | 是（當 `dry_run=false` 且 `confirm_write=true`） |
| `translate_project` | `run_translation` 的相容別名。 | 是（當 `dry_run=false` 且 `confirm_write=true`） |
| `run_review` | 執行確定性的審查檢查。 | 否 |
| `get_configuration_status` | 報告已配置的 LLM 與 Vision 提供者而不暴露機密值。 | 否 |
| `list_supported_languages` | 列出支援的目標語言代碼。 | 否 |
| `get_api_overview` | 描述可用的 MCP 工作流程與工具。 | 否 |

## 資源

| 資源 URI | 用途 |
| --- | --- |
| `co-op://api` | 工作流程與工具的 JSON 概覽。 |
| `co-op://supported-languages` | 支援語言代碼的 JSON 列表。 |
| `co-op://configuration` | 不含機密的提供者可用性摘要（JSON）。 |

## 提示詞

| 提示詞 | 用途 |
| --- | --- |
| `translate_markdown_document_prompt` | 引導 MCP 用戶端完成內容翻譯以及可選的路徑重寫。 |
| `agent_assisted_markdown_translation_prompt` | 引導 MCP 用戶端在沒有 Co-op Translator LLM 提供者憑證的情況下，透過主機代理進行 Markdown 翻譯。 |
| `translate_repository_prompt` | 引導 MCP 用戶端進行以 dry-run 為先的儲存庫翻譯。 |

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

在主機代理翻譯每個回傳片段後，使用 `start_markdown_agent_translation` 回傳的完整 `job` 物件完成該工作：

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

預覽儲存庫翻譯：

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

| 問題 | 建議作法 |
| --- | --- |
| MCP 用戶端找不到 `co-op-translator-mcp`。 | 使用絕對的 Python 執行檔路徑及 `["-m", "co_op_translator.mcp.server"]` 的 source checkout 配置。 |
| 伺服器已列出但翻譯失敗。 | 呼叫 `get_configuration_status` 並確認有可用的 LLM 提供者。 |
| 你想在沒有提供者憑證的情況下進行 Markdown 或筆記本翻譯。 | 使用 `start_markdown_agent_translation` / `finish_markdown_agent_translation` 或對應的筆記本 API，讓主機代理翻譯那些片段。 |
| 影像翻譯失敗。 | 確認已設定 Azure AI Vision 的變數，並呼叫 `get_configuration_status`。 |
| 儲存庫翻譯沒有寫入檔案。 | 只有在明確取得使用者批准後，才設定 `dry_run=false` 與 `confirm_write=true`。 |
| 對用戶端配置的變更沒有生效。 | 重新啟動或重新載入 MCP 用戶端。 |

## 安全注意事項

- MCP 工具呼叫由主機應用程式控制，因此儲存庫翻譯預設為 dry-run。
- 完整的儲存庫翻譯可能會建立、更新或刪除大量檔案。在設定 `confirm_write=true` 之前，應取得明確的使用者批准。
- 配置狀態工具絕不會回傳 API 金鑰、端點或其他機密值。
- 影像翻譯會回傳 base64 影像資料。大型影像可能導致產生很大的工具回應。
- 代理協助工具會將原始片段與提示詞回傳給 MCP 主機。僅在使用者願意將內容傳送給該主機代理模型的情況下使用它們。