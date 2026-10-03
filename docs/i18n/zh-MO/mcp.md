# MCP 伺服器

Co-op Translator 包含一個 Model Context Protocol 伺服器，供代理、編輯器，以及與 MCP 相容的用戶端使用。

在預設的本地設定中，使用者不需手動維持一個獨立的伺服器在執行。使用者設定他們的 MCP 用戶端，當需要 Co-op Translator 工具時，該用戶端會自動透過 `stdio` 啟動 `co-op-translator-mcp`。

如果你正要在 CLI、Python API 與 MCP 之間做選擇，請先參閱 [選擇你的工作流程](workflows.md)。

當代理或編輯器應該直接呼叫 Co-op Translator 時，請使用 MCP:

| 使用者目標 | MCP 工具 |
| --- | --- |
| 翻譯一份 Markdown 文件、筆記本或影像 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| 使用主機代理模型翻譯 Markdown 或筆記本內容 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 在選擇輸出路徑後重寫已翻譯的 Markdown 或筆記本連結 | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 像 CLI 一樣翻譯整個倉庫 | `run_translation`, `translate_project` |
| 在沒有 LLM 憑證下檢視已翻譯的輸出 | `run_review` |
| 檢查功能與環境狀態 | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 伺服器包裹了在 [Python API](api.md) 中記載的相同公開 Python API。提供者支援的工具使用與 CLI 和 Python API 相同配置的提供者。代理協助的工具會為 MCP 主機代理準備分段以進行翻譯，然後使用 Co-op Translator 重建最終的 Markdown 或筆記本。

## 第 1 步: 安裝並設定 Co-op Translator

在你的 MCP 用戶端將使用的 Python 環境中安裝 Co-op Translator：

```bash
pip install co-op-translator
```

若從此儲存庫做本地開發，請以可編輯（editable）模式安裝該套件：

```bash
pip install -e .
```

選擇你的 MCP 用戶端將使用的翻譯模式：

| 模式 | 使用情境 | 憑證 |
| --- | --- | --- |
| 提供者支援模式 | Co-op Translator 會呼叫 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, 或 `run_translation`。 | 翻譯需要 Azure OpenAI、OpenAI 或 Anthropic。影像翻譯還需要 Azure AI Vision。 |
| 代理協助模式 | MCP 主機代理翻譯由 `start_markdown_agent_translation` 或 `start_notebook_agent_translation` 回傳的分段。 | Markdown 或筆記本的分段不需要 Co-op Translator LLM 提供者憑證。影像翻譯尚未由代理協助模式涵蓋。 |

如果您在像 Codex 或 Claude Code 這類代理內開始進行 Markdown 或 notebook 的翻譯，請從 agent-assisted 模式開始。當您希望 Co-op Translator 本身去呼叫您已設定的提供者、在翻譯影像時，或在執行像 CLI 這類的倉庫級別翻譯時，請使用 provider-backed 模式。

為由提供者支援的工作流程設定一個提供者：

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

由提供者支援的影像翻譯還另外需要：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    代理協助模式目前涵蓋 Markdown 以及筆記本中的 Markdown 儲存格。影像翻譯仍然使用提供者支援的影像流程，並需要 Azure AI Vision 進行 OCR 與版面感知呈現。

## 第 2 步: 設定您的 MCP 用戶端

對於一般的本地 `stdio` 設定，將 Co-op Translator 新增到你的 MCP 用戶端設定中。該用戶端會自動啟動與停止該程序。

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

在 macOS 或 Linux 上的原始碼檢出設定：

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

更改 MCP 用戶端設定後，請重新啟動或重新載入用戶端，以便它可以發現新的伺服器。

## 第 3 步：在用戶端驗證伺服器

要求 MCP 用戶端列出可用的工具，或先呼叫其中一個唯讀輔助程式：

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Useful first checks:

| 工具 | 檢查項目 |
| --- | --- |
| `get_api_overview` | 確認伺服器可達並顯示可用工作流程。 |
| `list_supported_languages` | 確認已封裝的語言資料可以載入。 |
| `get_configuration_status` | 在不揭露祕密值的情況下，確認 LLM 與 Vision 提供者的可用性。 |

## 第 4 步：選擇工作流程

### 翻譯個別檔案或文件

當 MCP 用戶端已經擁有文件內容或圖像路徑，且 Co-op Translator 應呼叫已配置的翻譯供應商時，請使用由供應商支援的內容工具。

For Markdown:

1. Call `translate_markdown_content` with `document`, `language_code`, and optionally `source_path`.
2. 如果翻譯結果將被寫入 Co-op Translator 的輸出佈局，請呼叫 `rewrite_markdown_paths`。
3. 讓客戶端寫入或返回最終的 `content`。

For notebooks:

1. Call `translate_notebook_content` with notebook JSON and `language_code`.
2. 如果翻譯後的 notebook 連結需要為目標路徑進行調整，請呼叫 `rewrite_notebook_paths`。
3. 寫入或返回最終的筆記本 JSON。

For images:

1. Call `translate_image_content` with `image_path`, `language_code`, and optional `root_dir` or `fast_mode`.
2. Read the returned `data_base64` and `mime_type`.
3. 如果提供了 `output_path`，已翻譯的圖片也會儲存到該路徑。

內容工具不會執行專案偵測、元資料更新、免責聲明或自動路徑重寫。如果您想讓主機代理在沒有 Co-op Translator LLM 提供者憑證的情況下翻譯 Markdown 或 notebook 區塊，請使用下方的代理協助工作流程。

### 使用主機代理模型翻譯

當您希望由 MCP 主機代理（例如程式編碼助理）來產生翻譯文字，而不是為 Co-op Translator 設定 LLM 提供者時，請使用代理協助工具。

在以聊天為基礎的 MCP 用戶端中，你通常不需要自己撰寫 tool JSON。請要求代理使用代理協助的工作流程：

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

如果你的 MCP 用戶端支援伺服器提示，使用 `agent_assisted_markdown_translation_prompt` 讓用戶端載入相同的工作流程指示。

For Markdown:

1. Call `start_markdown_agent_translation` with `document`, `language_code`, and optionally `source_path`.
2. 在主機代理中，依照 chunk `prompt` 翻譯每個返回的區塊。
3. Call `finish_markdown_agent_translation` with the original `job` and translated chunks using `chunk_id` and `translated_text`.
4. 如果內容會寫入已翻譯的目標路徑，請呼叫 `rewrite_markdown_paths`。

For notebooks:

1. Call `start_notebook_agent_translation` with notebook JSON and `language_code`.
2. 在主機代理中翻譯每個返回的區塊。
3. Call `finish_notebook_agent_translation` with the original `job` and translated chunks.
4. 若已翻譯的 notebook 連結需要調整目標路徑，請呼叫 `rewrite_notebook_paths`。

由代理協助的工具不會從 Co-op Translator 呼叫已配置的 LLM 提供者。主機代理負責翻譯回傳的區塊。Co-op Translator 處理 Markdown 分塊、保留佔位符、frontmatter 重建、筆記本儲存格的替換，以及翻譯後的正規化。

### 翻譯整個儲存庫

當使用者希望 Co-op Translator 的行為像 `translate` CLI 時，使用 `run_translation`。

儲存庫翻譯預設為 `dry_run=true`，以便代理程式可以在檔案變更前檢查範圍：

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` result includes an `events` array with versioned
`co-op.translation.event.v1` progress events. MCP clients should use fields such
as `type`, `stage_key`, `completed`, `total`, and `current_path` instead of
parsing captured console text. Pass `json_events_path` to also write those events
to an NDJSON file.

若要允許寫入，呼叫者必須同時設定 `dry_run=false` 與 `confirm_write=true`：

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` 被公開為 `run_translation` 的相容別名。

### 審閱已翻譯的輸出

對於不需要 LLM 或 Vision 憑證的確定性檢查，請使用 `run_review`：

!!! note "Beta"
    MCP 揭露 beta 版的 `run_review` API。它對於唯讀的檢閱工作流程是安全的，但檢閱檢查與問題結構（issue schemas）可能會演進。

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

結果包含已擷取的文字輸出，以及在可用時的結構化審查摘要。

## 手動伺服器執行

手動執行主要用於偵錯，或用於那些像長時間運行的伺服器一樣運作的傳輸。

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

執行一個長期運行的 HTTP 或 SSE 伺服器：

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

對於本地編輯器和代理整合，請在步驟 2 中優先使用用戶端管理的 `stdio` 設定。

## Tools

| 工具 | 用途 | 是否寫入檔案 |
| --- | --- | --- |
| `translate_markdown_content` | 翻譯一個 Markdown 字串。 | 否 |
| `translate_notebook_content` | 翻譯筆記本 JSON 中的 Markdown 儲存格。 | 否 |
| `translate_image_content` | 翻譯單張影像中的文字並回傳 base64 影像資料。 | 選擇性，僅在提供 `output_path` 時 |
| `start_markdown_agent_translation` | 為主機代理準備 Markdown 分段以翻譯，無需 Co-op Translator 的 LLM 憑證。 | 否 |
| `finish_markdown_agent_translation` | 從主機代理翻譯回來的分段重建 Markdown。 | 否 |
| `start_notebook_agent_translation` | 為主機代理準備筆記本中 Markdown 儲存格的分段以翻譯。 | 否 |
| `finish_notebook_agent_translation` | 從主機代理已翻譯的分段重建筆記本 JSON。 | 否 |
| `rewrite_markdown_paths` | 為已翻譯的目標重寫 Markdown 主體與 frontmatter 的路徑。 | 否 |
| `rewrite_notebook_paths` | 重寫筆記本 Markdown 儲存格內的路徑。 | 否 |
| `run_translation` | 執行專案層級的翻譯，類似 CLI。 | 是，當 `dry_run=false` 與 `confirm_write=true` 時 |
| `translate_project` | `run_translation` 的相容別名。 | 是，當 `dry_run=false` 與 `confirm_write=true` 時 |
| `run_review` | 執行確定性檢閱檢查。 | 否 |
| `get_configuration_status` | 報告已配置的 LLM 與 Vision 提供者，且不揭露祕密。 | 否 |
| `list_supported_languages` | 列出支援的目標語言代碼。 | 否 |
| `get_api_overview` | 描述可用的 MCP 工作流程與工具。 | 否 |

## Resources

| 資源 URI | 用途 |
| --- | --- |
| `co-op://api` | 工作流程與工具的 JSON 概覽。 |
| `co-op://supported-languages` | 支援語言代碼的 JSON 列表。 |
| `co-op://configuration` | 在不包含祕密的情況下，提供者可用性摘要的 JSON。 |

## Prompts

| 提示 | 用途 |
| --- | --- |
| `translate_markdown_document_prompt` | 引導 MCP 用戶端完成內容翻譯並選擇性地重寫路徑。 |
| `agent_assisted_markdown_translation_prompt` | 引導 MCP 用戶端在沒有 Co-op Translator LLM 提供者憑證的情況下，由主機代理翻譯 Markdown。 |
| `translate_repository_prompt` | 引導 MCP 用戶端先以 dry-run 為先執行的倉庫翻譯。 |

## 可複製貼上的範例

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

在主機代理翻譯完每個回傳的區塊後，請使用 `start_markdown_agent_translation` 回傳的完整 `job` 物件來完成工作：

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
| MCP 用戶端找不到 `co-op-translator-mcp`。 | 請使用絕對的 Python 可執行檔路徑以及 `["-m", "co_op_translator.mcp.server"]` 的原始碼簽出設定。 |
| 伺服器已列出但翻譯失敗。 | 呼叫 `get_configuration_status` 並確認 LLM 提供者可用。 |
| 您想要在沒有提供者憑證的情況下進行 Markdown 或 notebook 的翻譯。 | 使用 `start_markdown_agent_translation` / `finish_markdown_agent_translation` 或 notebook 的對應項，讓主機代理翻譯這些區塊。 |
| 影像翻譯失敗。 | 確認已設定 Azure AI Vision 變數並呼叫 `get_configuration_status`。 |
| 儲存庫翻譯未寫入檔案。 | 僅在明確取得使用者核准後才設定 `dry_run=false` 與 `confirm_write=true`。 |
| 用戶端設定的變更未出現。 | 重新啟動或重新載入 MCP 用戶端。 |

## 安全注意事項

- MCP 工具呼叫由主機應用程式經由模型控制，因此倉庫翻譯預設為模擬執行。
- 完整的倉庫翻譯可能會建立、更新或移除大量檔案。在設定 `confirm_write=true` 之前，請取得使用者的明確批准。
- 設定狀態工具絕不會回傳 API 金鑰、端點或其他機密值。
- 影像翻譯會回傳 base64 圖像資料。大型圖片可能會產生大量工具回應。
- 代理輔助工具會將來源片段和提示回傳至 MCP 主機。只有在使用者願意將內容傳送給該主機代理模型時才使用它們。
