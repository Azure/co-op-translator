# 選擇您的工作流程

Co-op Translator 可以透過三種方式使用：CLI、Python API，與 MCP 伺服器。它們共享相同的翻譯能力，但各自適合不同的工作流程。

當您在決定從何開始時，請使用此頁。

## 快速決策

| If you want to... | Use | Start here |
| --- | --- | --- |
| 從終端機翻譯或審閱一個儲存庫 | CLI | [CLI 參考](cli.md) |
| 將翻譯新增到 Python 腳本、服務、筆記本，或 CI 工作 | Python API | [Python API](api.md) |
| 讓代理、編輯器，或相容 MCP 的客戶端為您翻譯內容 | MCP Server | [MCP Server](mcp.md) |
| 翻譯應用程式已載入的一份 Markdown 文件、筆記本，或影像 | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| 將整個儲存庫翻譯，並建立標準輸出資料夾與元資料 | CLI or `run_translation` | [CLI 參考](cli.md) or [Python API](api.md) |

## 何時使用 CLI

當由人員或 CI 工作從 shell 操作儲存庫翻譯時，選擇 CLI。

當您希望 Co-op Translator 探測專案檔案、建立翻譯輸出、保留專案佈局、更新元資料，並執行審查命令時，CLI 是最直接的方式。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

適用情境：

- 您正從終端機翻譯一個儲存庫。
- 您想要一個可重複執行於 CI 或發布流程的指令。
- 您需要內建的專案偵測、輸出路徑、元資料、清理與審查功能。
- 您偏好使用指令介面而非撰寫 Python 程式。

## 何時使用 Python API

當您的程式碼需要掌控工作流程時，選擇 Python API。

此 API 對於應用程式、自動化腳本、筆記本、服務，以及自訂管線十分有用。它讓您可以呼叫個別檔案的低階內容翻譯 API，或執行 CLI 使用的相同儲存庫層級協調。

翻譯一份 Markdown 文件並決定儲存位置：

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

適用情境：

- 您的應用程式已在讀取檔案、緩衝區、筆記本或影像位元組。
- 您需要自訂的驗證、儲存、紀錄、重試或核准流程。
- 您想翻譯單一文件、筆記本或影像，而無需處理整個儲存庫。
- 您想要儲存庫翻譯，但透過 Python 自動化而不是 shell 指令。

## 何時使用 MCP Server

當代理、編輯器，或相容 MCP 的客戶端應呼叫 Co-op Translator 工具時，選擇 MCP 伺服器。

在一般的本機設定中，使用者不會手動維持伺服器運行。當需要工具時，MCP 用戶端會透過 `stdio` 啟動 `co-op-translator-mcp`。

代理可以處理的範例使用者請求：

- "將此 Markdown 檔案翻譯成韓文並保持連結正確。"
- "將此 Markdown 檔案透過代理協助的 MCP 工作流程翻譯成韓文，並對要翻譯的區塊使用您自己的模型。"
- "將此筆記本翻譯成韓文，保留程式碼儲存格，並使用 Co-op Translator MCP 重建該筆記本。"
- "將此影像中的文字翻譯成日文並儲存結果。"
- "對儲存庫翻譯執行模擬運行（dry-run）為西班牙文，並告訴我會有哪些變更。"
- "檢查韓文翻譯輸出是否為最新。"

對於 Markdown 和筆記本，MCP 可以以兩種模式運作：

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | 當 MCP 主機代理應使用其自己的模型翻譯區塊，而不需要 Co-op Translator LLM 提供者憑證。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator 應直接呼叫 Azure OpenAI 或 OpenAI。 | `translate_markdown_content`, `translate_notebook_content` |

MCP 由提供者支援的 Markdown 工具調用格式：

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

MCP 影像工具調用格式：

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

透過 MCP 預設以模擬執行（dry-run）儲存庫翻譯：

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

- 您想在代理或編輯器內擁有以自然語言為基礎的翻譯工作流程。
- 您想要主機代理模型翻譯已準備好的 Markdown 或筆記本區塊的功能。
- 您希望代理翻譯選取的內容，而非整個儲存庫。
- 您希望在對整個儲存庫進行寫入前有一個核准步驟。
- 您想要一個介面，提供 Markdown、筆記本、影像、審查與路徑重寫工具。

## 它們如何協同運作

對於人員翻譯儲存庫，CLI 是最好的預設選擇。當您的程式掌控工作流程時，Python API 最合適。當代理或編輯器掌控工作流程時，MCP 伺服器最合適。

這三條路徑都使用相同的公開 Co-op Translator API，因此您可以從 CLI 開始，之後用 Python 自動化，並在需要代理驅動的工作流程時，向 MCP 用戶端開放相同的功能。