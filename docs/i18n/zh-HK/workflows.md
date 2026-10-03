# 選擇你的工作流程

Co-op Translator 可以透過三種方式使用：CLI、Python API，以及 MCP 伺服器。它們共享相同的翻譯功能，但各自適合不同的工作流程。

當你決定從哪裡開始時，請使用此頁面。

**如果你手動編輯翻譯：** 預設的 CLI 與 Actions 工作流程會對已更改的來源檔案整段重新翻譯，因此那些檔案中的措辭可能會被覆蓋。在接受更新前請檢查 diff。要在 Markdown 區塊層級保留已接受的編輯，請使用可選的 [Python API 翻譯狀態提供者](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)。

## 快速決策

| 如果你想要... | 使用 | 從這裡開始 |
| --- | --- | --- |
| 從終端機翻譯或檢閱一個儲存庫 | CLI | [CLI 參考](cli.md) |
| 在 Python 腳本、服務、Notebook 或 CI 工作中加入翻譯 | Python API | [Python API](api.md) |
| 讓 agent、編輯器或與 MCP 相容的用戶端幫你翻譯內容 | MCP 伺服器 | [MCP 伺服器](mcp.md) |
| 翻譯你應用程式已載入的單一 Markdown 文件、Notebook 或影像 | Python API 或 MCP 伺服器 | [Python API](api.md) 或 [MCP 伺服器](mcp.md) |
| 翻譯整個儲存庫並使用標準輸出資料夾與中繼資料 | CLI 或 `run_translation` | [CLI 參考](cli.md) 或 [Python API](api.md) |

## 何時使用 CLI

當有人或 CI 工作從 shell 驅動儲存庫翻譯時，選擇 CLI。

當你希望 Co-op Translator 自動尋找專案檔案、建立翻譯輸出、保留專案佈局、更新中繼資料並執行檢閱命令時，CLI 是最直接的選擇。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

此範例會翻譯 Markdown 與 Notebook。只有在設定好 [Azure AI Vision](configuration.md#azure-ai-vision) 後才加入 `-img`。若要第一次僅翻譯 Markdown，請參照 [你的第一個翻譯](first-translation.md)。

適用情境：

- 你正從終端機翻譯一個儲存庫。
- 你想要一個可在 CI 或發行工作流程中重複使用的命令。
- 你想要內建的專案偵測、輸出路徑、中繼資料、清理與檢閱功能。
- 你偏好命令介面而不是撰寫 Python 程式碼。

## 何時使用 Python API

當你希望由自己的程式碼控制工作流程時，選擇 Python API。

API 適用於應用程式、自動化腳本、Notebook、服務以及自訂管線。它允許你呼叫針對單一檔案的低階內容翻譯 API，或執行與 CLI 相同的儲存庫級協調流程。

翻譯單一 Markdown 文件並決定儲存位置：

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

從 Python 執行儲存庫翻譯：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

適合情境：

- 你的應用程式已在讀取檔案、緩衝區、Notebook，或影像位元組。
- 你需要自訂的驗證、儲存、日誌、重試或審核流程。
- 你想在不處理整個儲存庫的情況下，翻譯單一文件、Notebook 或影像。
- 你想要翻譯儲存庫，但透過 Python 自動化而不是 shell 命令。

## 何時使用 MCP 伺服器

當 agent、編輯器或與 MCP 相容的用戶端需要呼叫 Co-op Translator 工具時，選擇 MCP 伺服器。

在一般的本地設定中，使用者不需要手動一直維持伺服器運行。當需要工具時，MCP 用戶端會透過 stdio 啟動 `co-op-translator-mcp`。

範例使用者請求，agent 可以處理：

- "將此 Markdown 檔案翻譯成韓文，並保持連結正確。"
- "使用 agent 協助的 MCP 工作流程將此 Markdown 檔案翻譯成韓文，並對翻譯的區塊使用你自己的模型。"
- "將此 Notebook 翻譯成韓文，保留程式碼區塊，並使用 Co-op Translator MCP 來重建 Notebook。"
- "將這張影像中的文字翻譯成日文並儲存結果。"
- "對儲存庫翻譯進行預覽（dry-run）成西班牙文，並告訴我會有哪些變更。"
- "檢閱韓文翻譯輸出是否為最新。"

對於 Markdown 與 Notebook，MCP 可以在兩種模式下運作：

| 模式 | 使用情境 | 主要工具 |
| --- | --- | --- |
| Agent-assisted | 當 MCP 主機的 agent 應使用其自己的模型翻譯區塊，而不使用 Co-op Translator 的 LLM 提供者憑證。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator 應直接呼叫 Azure OpenAI、OpenAI，或 Anthropic。 | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed 的 Markdown 工具呼叫格式：

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP 影像工具呼叫格式：

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

透過 MCP 的儲存庫翻譯預設為 dry-run：

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

適用情境：

- 你想在 agent 或編輯器內有自然語言的翻譯工作流程。
- 你想要 Markdown 或 Notebook 的翻譯，讓主機 agent 的模型翻譯已準備好的區塊。
- 你希望 agent 翻譯所選內容，而不是整個儲存庫。
- 你想要在對整個儲存庫寫入前有一個審批步驟。
- 你想要一個介面，能同時提供 Markdown、Notebook、影像、檢閱與路徑重寫工具。

## 它們如何配合

對於人工翻譯儲存庫，CLI 是最好的預設選擇；當你的程式碼掌控工作流程時，Python API 最適合；而當 agent 或編輯器主導工作流程時，MCP 伺服器最適合。

這三種方式都使用相同的公開 Co-op Translator API，因此你可以先從 CLI 開始，之後用 Python 自動化，當需要 agent 驅動的工作流程時，再向 MCP 用戶端提供相同的功能。