# 選擇你的工作流程

Co-op Translator 可透過三種方式使用：CLI、Python API 與 MCP 伺服器。它們具有相同的翻譯能力，但各自適合不同的工作流程。

當你正在決定從何開始時，請使用此頁。

**如果你手動編輯翻譯：** 預設的 CLI 和 Actions 工作流程會對已變更的來源檔案進行完整重新翻譯，因此你在那些檔案中的措辭可能會被覆寫。在接受更新之前請檢查 diff。要在 Markdown 區塊層級保留已接受的編輯，請使用可選的 [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)。

## 快速決策

| 如果你想要... | 使用 | 從這裡開始 |
| --- | --- | --- |
| 從終端機翻譯或審閱一個程式庫 | CLI | [CLI 參考](cli.md) |
| 將翻譯新增到 Python 腳本、服務、筆記本或 CI 工作 | Python API | [Python API](api.md) |
| 讓代理程式、編輯器或相容 MCP 的用戶端為你翻譯內容 | MCP Server | [MCP Server](mcp.md) |
| 翻譯一份你的應用程式已載入的 Markdown 文件、筆記本或影像 | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| 將整個程式庫翻譯，並建立標準的輸出資料夾與元資料 | CLI or `run_translation` | [CLI 參考](cli.md) or [Python API](api.md) |

## 在以下情況使用 CLI

當有人或 CI 工作從 shell 驅動程式庫翻譯時，請選擇 CLI。

當你希望 Co-op Translator 自動發現專案檔案、產生翻譯輸出、保留專案佈局、更新元資料，並執行審閱命令時，CLI 是最直接的途徑。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

此範例會翻譯 Markdown 與筆記本。僅在設定好 [Azure AI Vision](configuration.md#azure-ai-vision) 後才加入 `-img`。若只想首次執行 Markdown，請參閱 [你的第一次翻譯](first-translation.md)。

適合的情況：

- 你正在從終端機翻譯一個程式庫。
- 你想要在 CI 或發佈工作流程中使用可重複執行的命令。
- 你想要內建的專案發現、輸出路徑、元資料、清理與審閱功能。
- 你偏好命令介面而非撰寫 Python 程式。

## 在以下情況使用 Python API

當你的程式碼需要掌控工作流程時，請選擇 Python API。

此 API 適用於應用程式、自動化腳本、筆記本、服務與自訂管線。它允許你對單一檔案呼叫低階的內容翻譯 API，或執行與 CLI 相同的程式庫級協作流程。

翻譯一個 Markdown 文件並決定保存位置：

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

從 Python 執行程式庫翻譯：

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

適合的情況：

- 你的應用程式已在讀取檔案、緩衝區、筆記本或影像位元組。
- 你需要自訂的驗證、儲存、記錄、重試或核准流程。
- 你想要只翻譯一個文件、筆記本或影像，而不處理整個程式庫。
- 你想要程式庫翻譯，但由 Python 自動化而非 shell 命令執行。

## 在以下情況使用 MCP 伺服器

當代理程式、編輯器或相容 MCP 的用戶端應呼叫 Co-op Translator 工具時，請選擇 MCP 伺服器。

在一般的本機設定中，使用者不需手動讓伺服器持續執行。當需要工具時，MCP 用戶端會透過 `stdio` 啟動 `co-op-translator-mcp`。

代理程式可處理的示例使用者請求：

- "將此 Markdown 檔案翻譯成韓語並保持連結正確。"
- "使用代理協助的 MCP 工作流程將此 Markdown 檔案翻譯成韓語，並對被翻譯的區塊使用你自己的模型。"
- "將此筆記本翻譯成韓語，保留程式碼儲存格，並使用 Co-op Translator MCP 重建該筆記本。"
- "將此影像中的文字翻譯成日語並儲存結果。"
- "對程式庫翻譯做模擬執行 (dry-run) 成西班牙語，並告訴我會改變哪些內容。"
- "審查韓語翻譯輸出是否為最新。"

對於 Markdown 與筆記本，MCP 可在兩種模式下運作：

| 模式 | 使用時機 | 主要工具 |
| --- | --- | --- |
| 代理協助 | MCP 主機代理應使用其自身模型來翻譯區塊，而不使用 Co-op Translator 的 LLM 提供者憑證。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 由提供者支援 | Co-op Translator 應直接呼叫 Azure OpenAI、OpenAI 或 Anthropic。 | `translate_markdown_content`, `translate_notebook_content` |

MCP 由提供者支援的 Markdown 工具呼叫範例：

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

MCP 影像工具呼叫範例：

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

透過 MCP 對程式庫翻譯預設為模擬執行：

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

適合的情況：

- 你想要在代理程式或編輯器內使用自然語言的翻譯工作流程。
- 你想要讓主機代理模型翻譯已準備好的 Markdown 或筆記本區塊。
- 你希望代理翻譯選取的內容，而不是整個程式庫。
- 你想要在對整個程式庫寫入之前加入核准步驟。
- 你想要一個介面，暴露 Markdown、筆記本、影像、審閱與路徑重寫工具。

## 這些方式如何互補

對於由人操作的程式庫翻譯，CLI 是最佳預設選擇。當你的程式碼掌握工作流程時，Python API 為最佳選擇。當代理或編輯器掌握工作流程時，MCP 伺服器為最佳選擇。

這三種路徑都使用相同的公開 Co-op Translator API，因此你可以先從 CLI 開始，之後使用 Python 自動化，並在需要代理驅動的工作流程時向 MCP 用戶端暴露相同的功能。