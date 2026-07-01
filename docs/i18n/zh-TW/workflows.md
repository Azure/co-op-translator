# 選擇您的工作流程

Co-op Translator 可以用三種方式操作：CLI、Python API 和 MCP server。它們共享相同的翻譯功能，但各自適合不同的工作流程。

在決定從哪裡開始時請使用此頁面。

## 快速決策

| 如果您想要... | 使用 | 從此開始 |
| --- | --- | --- |
| 從終端機翻譯或審閱儲存庫 | CLI | [CLI 參考](cli.md) |
| 將翻譯加入 Python 腳本、服務、筆記本或 CI 工作 | Python API | [Python API](api.md) |
| 讓 agent、編輯器或 MCP 相容的客戶端為您翻譯內容 | MCP Server | [MCP Server](mcp.md) |
| 翻譯您的應用程式已載入的單一 Markdown 文件、筆記本或影像 | Python API 或 MCP Server | [Python API](api.md) 或 [MCP Server](mcp.md) |
| 翻譯整個儲存庫並建立標準輸出資料夾與 metadata | CLI 或 `run_translation` | [CLI 參考](cli.md) 或 [Python API](api.md) |

## 何時使用 CLI

當由人或 CI 工作從 shell 操控儲存庫翻譯時，選擇 CLI。

當您希望 Co-op Translator 探索專案檔案、建立翻譯輸出、保留專案結構、更新 metadata，以及執行審閱指令時，CLI 是最直接的方式。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

適合的情況：

- 您正在從終端機翻譯一個儲存庫。
- 您想要一個可在 CI 或發行工作流程中重複使用的指令。
- 您想要內建的專案探索、輸出路徑、metadata、清理與審閱功能。
- 您偏好命令介面而非撰寫 Python 程式碼。

## 何時使用 Python API

當您的程式應該掌控工作流程時，選擇 Python API。

API 對應用程式、自動化腳本、筆記本、服務與自訂流程都很有用。它讓您能呼叫針對單一檔案的低階內容翻譯 API，或執行 CLI 使用的相同儲存庫層級協調。

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

適合的情況：

- 您的應用程式已經讀取檔案、緩衝區、筆記本或影像位元組。
- 您需要自訂的驗證、儲存、日誌、重試或審核流程。
- 您想要翻譯單一文件、筆記本或影像，而不處理整個儲存庫。
- 您想要儲存庫翻譯，但從 Python 自動化而非 shell 指令執行。

## 何時使用 MCP Server

當 agent、編輯器或 MCP 相容客戶端應呼叫 Co-op Translator 工具時，選擇 MCP server。

在一般的本機設定中，使用者不會手動持續執行伺服器。當需要工具時，MCP client 會透過 `stdio` 啟動 `co-op-translator-mcp`。

範例使用者請求（agent 可處理）：

- 「將此 Markdown 檔案翻譯為韓文，並保持連結正確。」
- 「使用 agent 協助的 MCP 工作流程將此 Markdown 檔案翻譯成韓文，並對已翻譯的區塊使用您自己的模型。」
- 「將此筆記本翻譯成韓文，保留程式碼儲存格，並使用 Co-op Translator MCP 重建筆記本。」
- 「將此影像中的文字翻譯成日文並儲存結果。」
- 「對儲存庫翻譯執行模擬執行（dry-run）至西班牙文，並告訴我會有哪些變更。」
- 「檢查韓文翻譯輸出是否為最新。」

對於 Markdown 和筆記本，MCP 可以以兩種模式運作：

| 模式 | 使用時機 | 主要工具 |
| --- | --- | --- |
| Agent 輔助 | 當 MCP 主機 agent 應使用其自己的模型翻譯區塊，而不使用 Co-op Translator 的 LLM 提供者憑證時。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider 支援 | Co-op Translator 應直接呼叫 Azure OpenAI 或 OpenAI。 | `translate_markdown_content`, `translate_notebook_content` |

MCP 提供者支援的 Markdown 工具呼叫格式：

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

透過 MCP 執行儲存庫翻譯預設為模擬執行（dry-run）：

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

- 您想在 agent 或編輯器內使用自然語言的翻譯工作流程。
- 您想要由主機 agent 模型翻譯已準備的 Markdown 或筆記本區塊。
- 您希望 agent 翻譯選取的內容，而非整個儲存庫。
- 您希望在寫入整個儲存庫之前有一個核可步驟。
- 您想要一個介面，提供 Markdown、筆記本、影像、審閱與路徑重寫工具。

## 它們如何整合

CLI 是人類翻譯儲存庫時的最佳預設選擇。當您的程式掌控工作流程時，Python API 最適合。當 agent 或編輯器掌控工作流程時，MCP server 最合適。

這三種方式都使用相同的公開 Co-op Translator API，因此您可以先從 CLI 開始，之後用 Python 自動化，並在需要 agent 驅動的工作流程時向 MCP 用戶端暴露相同的功能。