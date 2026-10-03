# 選擇你的工作流程

Co-op Translator 可透過三種方式使用：CLI、Python API 和 MCP 伺服器。它們共享相同的翻譯功能，但各自適合不同的工作流程。

當你在決定從哪裡開始時，請使用此頁面。

**如果你手動編輯翻譯：** 預設的 CLI 和 Actions 工作流程會完整地重新翻譯已變更的原始檔案，因此你在那些檔案中的文字可能會被覆寫。接受更新前請檢視差異。若要在 Markdown 區塊層級保留已接受的編輯，請使用可選的 [Python API 翻譯狀態提供者](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)。

## 快速決定

| 如果你想要... | 使用 | 從這裡開始 |
| --- | --- | --- |
| 從終端機翻譯或審查一個倉庫 | CLI | [CLI 參考](cli.md) |
| 將翻譯新增到 Python 腳本、服務、筆記本或 CI 工作 | Python API | [Python API](api.md) |
| 讓代理、編輯器或 MCP 相容的用戶端為你翻譯內容 | MCP Server | [MCP Server](mcp.md) |
| 翻譯你的應用程式已載入的一個 Markdown 文件、筆記本或影像 | Python API 或 MCP Server | [Python API](api.md) 或 [MCP Server](mcp.md) |
| 使用標準輸出資料夾與 metadata 翻譯整個倉庫 | CLI 或 `run_translation` | [CLI 參考](cli.md) 或 [Python API](api.md) |

## 何時使用 CLI

當有人或 CI 工作從 shell 操作倉庫翻譯時，選擇 CLI。

當你希望 Co-op Translator 自動發現專案檔案、建立翻譯輸出、保留專案佈局、更新 metadata，並執行檢閱指令時，CLI 是最直接的方式。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

此範例會翻譯 Markdown 和筆記本。只有在設定 [Azure AI Vision](configuration.md#azure-ai-vision) 之後才加入 `-img`。若只想首次執行 Markdown，請參考 [你的首次翻譯](first-translation.md)。

適合的情境：

- 你正在從終端機翻譯一個倉庫。
- 你想要一個可在 CI 或發佈工作流程中重複使用的指令。
- 你想要內建的專案偵測、輸出路徑、metadata、清理與檢閱。
- 你偏好使用指令介面而不是撰寫 Python 程式碼。

## 何時使用 Python API

當你的程式碼需要控制工作流程時，選擇 Python API。

API 對於應用程式、自動化腳本、筆記本、服務和自訂管線很有用。它讓你可以對單一檔案呼叫低階的內容翻譯 API，或執行與 CLI 相同的倉庫層級協調程序。

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

從 Python 執行倉庫翻譯：

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

適合的情境：

- 你的應用程式已經讀取檔案、緩衝區、筆記本或影像位元組。
- 你需要自訂的驗證、儲存、記錄、重試或核准流程。
- 你想要翻譯單一文件、筆記本或影像，而不處理整個倉庫。
- 你想要倉庫翻譯，但由 Python 自動化而非 shell 指令執行。

## 何時使用 MCP 伺服器

當代理、編輯器或 MCP 相容的用戶端應呼叫 Co-op Translator 工具時，選擇 MCP 伺服器。

在一般的本機設定中，使用者不需手動保持伺服器執行。當需要工具時，MCP 用戶端會透過 `stdio` 啟動 `co-op-translator-mcp`。

代理可以處理的使用者請求範例:

- "將此 Markdown 檔案翻譯成韓文並保持連結正確。"
- "將此 Markdown 檔案翻譯成韓文，使用代理協助的 MCP 工作流程，並對翻譯的段落使用您自己的模型。"
- "將此筆記本翻譯成韓文，保留程式碼儲存格，並使用 Co-op Translator MCP 來重建筆記本。"
- "將此圖像中的文字翻譯成日文並儲存結果。"
- "對儲存庫的翻譯進行模擬執行成西班牙文，並告訴我會有哪些變更。"
- "檢查韓文翻譯輸出是否為最新。"

對於 Markdown 和筆記本，MCP 可以以兩種模式運作：

| 模式 | 使用時機 | 主要工具 |
| --- | --- | --- |
| 代理協助 | MCP 主機代理應使用其自身模型翻譯區塊，無需 Co-op Translator LLM 提供者的憑證。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 由提供者支援 | Co-op Translator 應直接呼叫 Azure OpenAI、OpenAI 或 Anthropic。 | `translate_markdown_content`, `translate_notebook_content` |

由 MCP 提供者支援的 Markdown 工具呼叫格式:

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

MCP image tool call shape:

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

透過 MCP，倉庫翻譯預設為模擬執行：

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

適合的情境：

- 你想要在代理或編輯器內使用自然語言的翻譯工作流程。
- 你想要由主機代理模型翻譯已準備的 Markdown 或筆記本區塊。
- 你希望代理翻譯選取的內容，而不是整個倉庫。
- 你想在對整個倉庫寫入之前加入核准步驟。
- 你想要一個介面，提供 Markdown、筆記本、影像、檢閱與路徑重寫等工具。

## 它們如何互相搭配

CLI 是人類翻譯倉庫時最合適的預設選擇。當你的程式碼掌控工作流程時，Python API 最適合。當代理或編輯器掌控工作流程時，MCP 伺服器最合適。

這三種方式都使用相同的公開 Co-op Translator API，因此你可以先從 CLI 開始，之後用 Python 自動化，並在需要代理驅動的工作流程時將相同功能提供給 MCP 用戶端。