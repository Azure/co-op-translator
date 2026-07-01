# Choose Your Workflow

Co-op Translator 可透過三種方式使用：CLI、Python API，及 MCP server。它們共享相同的翻譯功能，但各自適合不同的工作流程。

當你決定從哪裡開始時，請使用此頁面。

## Quick Decision

| If you want to... | Use | Start here |
| --- | --- | --- |
| Translate or review a repository from a terminal | CLI | [CLI 參考](cli.md) |
| Add translation to a Python script, service, notebook, or CI job | Python API | [Python API 參考](api.md) |
| Let an agent, editor, or MCP-compatible client translate content for you | MCP Server | [MCP Server 參考](mcp.md) |
| Translate one Markdown document, notebook, or image that your app already loaded | Python API or MCP Server | [Python API 參考](api.md) or [MCP Server 參考](mcp.md) |
| Translate an entire repository with standard output folders and metadata | CLI or `run_translation` | [CLI 參考](cli.md) or [Python API 參考](api.md) |

## Use the CLI when

當有使用者或 CI 作業從 shell 主導儲存庫翻譯時，請選擇 CLI。

當你想讓 Co-op Translator 自動發現專案檔案、建立翻譯輸出、保留專案佈局、更新元資料，並執行審查指令時，CLI 是最直接的方式。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

適合情況：

- 你正在從終端機翻譯一個儲存庫。
- 你想為 CI 或發布工作流程建立可重複的指令。
- 你想要內建的專案發現、輸出路徑、元資料、清理與審查功能。
- 你偏好指令介面而不是撰寫 Python 程式碼。

## Use the Python API when

當你的程式碼需要掌控工作流程時，請選擇 Python API。

API 對應用程式、自動化腳本、筆記本、服務和自訂管線很有用。它讓你能為單一檔案呼叫低階的內容翻譯 API，或執行與 CLI 相同的儲存庫層級協調程序。

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

適合情況：

- 你的應用程式已經讀取檔案、緩衝區、筆記本或影像位元組。
- 你需要自訂的驗證、儲存、記錄、重試或核准流程。
- 你想在不處理整個儲存庫的情況下，翻譯單一文件、筆記本或影像。
- 你想執行儲存庫翻譯，但透過 Python 自動化而非 shell 指令。

## Use the MCP Server when

當代理、編輯器或相容 MCP 的客戶端應該呼叫 Co-op Translator 工具時，請選擇 MCP server。

在一般的本機設定中，使用者不需手動讓伺服器持續執行。當需要工具時，MCP 客戶端會透過 `stdio` 啟動 `co-op-translator-mcp`。

Example user requests an agent could handle:

- "Translate this Markdown file to Korean and keep the links correct."
- "Translate this Markdown file to Korean with the agent-assisted MCP workflow, using your own model for the translated chunks."
- "Translate this notebook to Korean, preserve code cells, and use Co-op Translator MCP to reconstruct the notebook."
- "Translate the text in this image to Japanese and save the result."
- "Dry-run a repository translation to Spanish and tell me what would change."
- "Review whether the Korean translation output is up to date."

For Markdown and notebooks, MCP can work in two modes:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | The MCP host agent should translate chunks with its own model, without Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator should call Azure OpenAI or OpenAI directly. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

Repository translation is dry-run by default through MCP:

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

適合情況：

- 你希望在代理或編輯器內使用自然語言的翻譯工作流程。
- 你想要 Markdown 或筆記本 的翻譯，由主機代理模型翻譯已準備好的段落。
- 你希望代理翻譯選定內容，而不是整個儲存庫。
- 你希望在進行整個儲存庫寫入之前有審批步驟。
- 你想要一個介面，能同時提供 Markdown、筆記本、影像、審查和路徑重寫工具。

## How They Fit Together

對人類翻譯儲存庫來說，CLI 是最合適的預設選擇。當你的程式碼掌控工作流程時，Python API 最合適。當代理或編輯器掌控工作流程時，MCP server 是最佳選擇。

這三種路徑都使用相同的公開 Co-op Translator API，所以你可以從 CLI 開始，之後用 Python 自動化，並在需要代理驅動的工作流程時，向 MCP 客戶端暴露相同的功能。