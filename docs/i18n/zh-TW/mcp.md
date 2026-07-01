# MCP Server

Co-op Translator 包含一個供代理、編輯器，以及相容 MCP 的客戶端使用的 Model Context Protocol 伺服器。

在預設的本機設定中，使用者不會手動維持一個獨立的伺服器執行。使用者只要設定他們的 MCP 客戶端，當需要 Co-op Translator 工具時，客戶端會自動透過 `stdio` 啟動 `co-op-translator-mcp`。

如果你在 CLI、Python API 和 MCP 之間做選擇，請從 [Choose Your Workflow](workflows.md) 開始。

當代理或編輯器應直接呼叫 Co-op Translator 時，使用 MCP：

| 使用者目標 | MCP 工具 |
| --- | --- |
| 翻譯單一 Markdown 文件、筆記本或圖像 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| 使用主機代理模型翻譯 Markdown 或筆記本內容 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 選擇輸出路徑後重新寫入已翻譯的 Markdown 或筆記本連結 | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 如同 CLI 一樣翻譯整個專案 | `run_translation`, `translate_project` |
| 在沒有 LLM 憑證的情況下審查翻譯輸出 | `run_review` |
| 檢查功能與環境狀態 | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 伺服器包裝了在 [Python API](api.md) 文件中記載的相同公開 Python API。由提供者支援的工具使用與 CLI 和 Python API 相同的已設定提供者。代理協助的工具會為 MCP 主機代理準備區塊進行翻譯，之後使用 Co-op Translator 重建最終的 Markdown 或筆記本。

## Step 1: Install and Configure Co-op Translator

在你的 MCP 客戶端將使用的 Python 環境中安裝 Co-op Translator：

```bash
pip install co-op-translator
```

若要從此資料庫進行本機開發，請以可編輯模式安裝此套件：

```bash
pip install -e .
```

選擇你的 MCP 客戶端將使用的翻譯模式：

| 模式 | 適用情境 | 憑證 |
| --- | --- | --- |
| Provider-backed | 當 Co-op Translator 要呼叫 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` 或 `run_translation` 時使用。 | Markdown 與筆記本翻譯需要 Azure OpenAI 或 OpenAI。圖像翻譯還需要 Azure AI Vision。 |
| Agent-assisted | MCP 主機代理會翻譯由 `start_markdown_agent_translation` 或 `start_notebook_agent_translation` 回傳的區塊。 | Markdown 或筆記本區塊不需要 Co-op Translator 的 LLM 提供者憑證。圖像翻譯目前尚未涵蓋在 agent-assisted 模式中。 |

如果你在像 Codex 或 Claude Code 之類的代理中開始進行 Markdown 或筆記本翻譯，請從 agent-assisted 模式開始。當你希望 Co-op Translator 自行呼叫已設定的提供者、或你正在翻譯圖像、或你要執行類似 CLI 的專案層級翻譯時，請使用 provider-backed 模式。

僅為 provider-backed 工作流程設定提供者憑證：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed 的圖像翻譯另外需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

對於一般的本機 `stdio` 設定，將 Co-op Translator 加入你的 MCP 客戶端設定。客戶端會自動啟動並停止該程序。

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

Windows 上的原始程式碼檢出設定：

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

macOS 或 Linux 上的原始程式碼檢出設定：

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

在變更 MCP 客戶端設定後，重新啟動或重新載入客戶端，以便它能發現新的伺服器。

## Step 3: Verify the Server in the Client

請求 MCP 客戶端列出可用工具，或先呼叫其中一個唯讀的輔助工具：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

有用的初步檢查：

| 工具 | 要檢查的項目 |
| --- | --- |
| `get_api_overview` | 確認伺服器可存取，並顯示可用的工作流程。 |
| `list_supported_languages` | 確認包裝的語言資料可以載入。 |
| `get_configuration_status` | 在不洩露秘密值的情況下，確認 LLM 與 Vision 提供者的可用性。 |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

當 MCP 客戶端已經有文件內容或圖像路徑，且希望 Co-op Translator 呼叫已設定的翻譯提供者時，使用 provider-backed 的內容工具。

對於 Markdown：

1. 使用 `document`、`language_code`，以及可選的 `source_path` 呼叫 `translate_markdown_content`。
2. 如果要將翻譯結果寫入 Co-op Translator 的輸出佈局，呼叫 `rewrite_markdown_paths`。
3. 讓客戶端寫入或回傳最終的 `content`。

對於筆記本：

1. 使用筆記本 JSON 與 `language_code` 呼叫 `translate_notebook_content`。
2. 若翻譯後的筆記本連結需要為目標路徑調整，呼叫 `rewrite_notebook_paths`。
3. 寫入或回傳最終的筆記本 JSON。

對於圖像：

1. 使用 `image_path`、`language_code` 與可選的 `root_dir` 或 `fast_mode` 呼叫 `translate_image_content`。
2. 讀取回傳的 `data_base64` 與 `mime_type`。
3. 如果提供了 `output_path`，翻譯後的圖像也會儲存到該路徑。

這些內容工具不會執行專案發現、更新 metadata、加入免責聲明或自動路徑重寫。如果你希望主機代理在沒有 Co-op Translator LLM 提供者憑證的情況下翻譯 Markdown 或筆記本區塊，請使用下述的 agent-assisted 工作流程。

### Translate with the Host Agent Model

當你希望 MCP 主機代理（例如程式碼助理）產生翻譯文字，而不是為 Co-op Translator 設定 Azure OpenAI 或 OpenAI 時，使用 agent-assisted 工具。

在以聊天為基礎的 MCP 客戶端中，通常不需要你自己編寫工具 JSON。請求代理使用 agent-assisted 工作流程：

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

如果你的 MCP 客戶端支援伺服器提示，使用 `agent_assisted_markdown_translation_prompt` 讓客戶端載入相同的工作流程指示。

對於 Markdown：

1. 使用 `document`、`language_code`，以及可選的 `source_path` 呼叫 `start_markdown_agent_translation`。
2. 在主機代理中依照區塊的 `prompt` 翻譯每個回傳的區塊。
3. 使用原始的 `job` 與包含 `chunk_id` 和 `translated_text` 的已翻譯區塊呼叫 `finish_markdown_agent_translation`。
4. 如果內容會被寫入已翻譯的目標路徑，呼叫 `rewrite_markdown_paths`。

對於筆記本：

1. 使用筆記本 JSON 與 `language_code` 呼叫 `start_notebook_agent_translation`。
2. 在主機代理中翻譯每個回傳的區塊。
3. 使用原始的 `job` 與已翻譯的區塊呼叫 `finish_notebook_agent_translation`。
4. 若翻譯後的筆記本連結需要為目標路徑調整，呼叫 `rewrite_notebook_paths`。

Agent-assisted 工具不會從 Co-op Translator 呼叫 Azure OpenAI 或 OpenAI。主機代理負責翻譯回傳的區塊。Co-op Translator 處理 Markdown 區塊化、保留佔位符、frontmatter 重建、筆記本儲存格替換，以及翻譯後的正規化。

### Translate an Entire Repository

當使用者希望 Co-op Translator 的行為像 `translate` CLI 時，使用 `run_translation`。

專案翻譯預設為 `dry_run=true`，以便代理可以在檔案變更前檢視範圍：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

要允許寫入，呼叫者必須同時設定 `dry_run=false` 與 `confirm_write=true`：

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

### Review Translated Output

在不需要 LLM 或 Vision 憑證的情況下，使用 `run_review` 進行確定性檢查：

!!! note "測試版"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

結果包含擷取的文字輸出與可用時的結構化審查摘要。

## Manual Server Runs

手動執行伺服器主要用於除錯或像長時間運行的伺服器一樣行為的傳輸。

除錯預設的 stdio 伺服器：

```bash
co-op-translator-mcp
```

從原始程式碼檢出執行：

```bash
python -m co_op_translator.mcp.server
```

執行長期存在的 HTTP 或 SSE 伺服器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

對於本機編輯器與代理整合，建議優先使用步驟 2 中由客戶端管理的 `stdio` 設定。

## Tools

| 工具 | 目的 | 是否寫入檔案 |
| --- | --- | --- |
| `translate_markdown_content` | 翻譯一個 Markdown 字串。 | 否 |
| `translate_notebook_content` | 翻譯筆記本 JSON 中的 Markdown 儲存格。 | 否 |
| `translate_image_content` | 翻譯一張圖像中的文字並回傳 base64 圖像資料。 | 選用，僅當提供 `output_path` 時 |
| `start_markdown_agent_translation` | 為主機代理準備 Markdown 區塊，以便在沒有 Co-op Translator LLM 憑證的情況下翻譯。 | 否 |
| `finish_markdown_agent_translation` | 從主機代理已翻譯的區塊重建 Markdown。 | 否 |
| `start_notebook_agent_translation` | 為主機代理準備筆記本的 Markdown 儲存格區塊以供翻譯。 | 否 |
| `finish_notebook_agent_translation` | 從主機代理已翻譯的區塊重建筆記本 JSON。 | 否 |
| `rewrite_markdown_paths` | 為已翻譯的目標重寫 Markdown 內容與 frontmatter 中的路徑。 | 否 |
| `rewrite_notebook_paths` | 重寫筆記本 Markdown 儲存格內的路徑。 | 否 |
| `run_translation` | 如同 CLI 一樣執行專案層級翻譯。 | 當 `dry_run=false` 並且 `confirm_write=true` 時會寫入 |
| `translate_project` | `run_translation` 的相容別名。 | 當 `dry_run=false` 並且 `confirm_write=true` 時會寫入 |
| `run_review` | 執行確定性審查檢查。 | 否 |
| `get_configuration_status` | 在不洩露秘密的情況下報告已設定的 LLM 與 Vision 提供者。 | 否 |
| `list_supported_languages` | 列出支援的目標語言代碼。 | 否 |
| `get_api_overview` | 描述可用的 MCP 工作流程與工具。 | 否 |

## Resources

| 資源 URI | 用途 |
| --- | --- |
| `co-op://api` | 工作流程與工具的 JSON 概覽。 |
| `co-op://supported-languages` | 支援的語言代碼 JSON 清單。 |
| `co-op://configuration` | 不含秘密的提供者可用性摘要 JSON。 |

## Prompts

| 提示 | 用途 |
| --- | --- |
| `translate_markdown_document_prompt` | 引導 MCP 客戶端完成內容翻譯以及可選的路徑重寫。 |
| `agent_assisted_markdown_translation_prompt` | 引導 MCP 客戶端在沒有 Co-op Translator LLM 提供者憑證的情況下進行主機代理的 Markdown 翻譯。 |
| `translate_repository_prompt` | 引導 MCP 客戶端先進行 dry-run 的專案翻譯。 |

## Copy-Paste Examples

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

在主機代理翻譯每個回傳的區塊後，使用 `start_markdown_agent_translation` 回傳的完整 `job` 物件完成工作：

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

預覽專案翻譯：

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

| 問題 | 建議做法 |
| --- | --- |
| MCP 客戶端找不到 `co-op-translator-mcp`。 | 使用絕對的 Python 可執行檔路徑以及 `["-m", "co_op_translator.mcp.server"]` 的原始程式碼檢出設定。 |
| 伺服器列出但翻譯失敗。 | 呼叫 `get_configuration_status` 並確認是否有 LLM 提供者可用。 |
| 你想在沒有 Azure OpenAI/OpenAI 金鑰的情況下進行 Markdown 或筆記本翻譯。 | 使用 `start_markdown_agent_translation` / `finish_markdown_agent_translation` 或對應的筆記本工具，讓主機代理翻譯那些區塊。 |
| 圖像翻譯失敗。 | 確認 Azure AI Vision 相關變數已設定，並呼叫 `get_configuration_status`。 |
| 專案翻譯沒有寫入檔案。 | 僅在明確取得使用者同意後設定 `dry_run=false` 與 `confirm_write=true`。 |
| 對客戶端設定的更動沒有出現。 | 重新啟動或重新載入 MCP 客戶端。 |

## Safety Notes

- MCP 工具呼叫由主機應用程式的模型控制，因此專案翻譯預設為 dry-run。
- 完整的專案翻譯可能會建立、更新或移除大量檔案。設定 `confirm_write=true` 前，務必取得使用者的明確同意。
- 配置狀態工具絕不會回傳 API 金鑰、端點或其他秘密值。
- 圖像翻譯會回傳 base64 圖像資料。大型圖像可能產生大量的工具回應。
- Agent-assisted 工具會回傳來源區塊與提示給 MCP 主機。僅在使用者願意將內容送交該主機代理模型的情況下使用。