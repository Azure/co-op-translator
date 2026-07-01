# 維護者指南

本頁概述 API、CLI 與文件網站如何互相連結。

## Public API boundary

穩定的 Python API 從以下位置匯出：

```python
co_op_translator.api
```

The public API is organized into content translation helpers, path rewriting helpers, project orchestration, and review:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

新增公開 API 時，請更新：

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

除非專案打算直接支援，否則避免將較低階的 `core` 模組記錄為穩定 API。

## CLI entry points

此套件定義了這些 Poetry 腳本：

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` 會根據腳本名稱進行派發：

- `translate` 會呼叫 `co_op_translator.cli.translate.translate_command`
- `evaluate` 會呼叫 `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` 會呼叫 `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` 會呼叫 `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` 會繞過 `__main__.py`，直接呼叫 `co_op_translator.mcp.server:main`。

新增或變更 CLI 選項時，請更新：

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP server

The MCP server is implemented in:

```python
co_op_translator.mcp.server
```

伺服器刻意包裝公開的 Python API，而不是呼叫較低階的 `core` 模組。請維持此邊界不變，以便 MCP 用戶端、Python 呼叫者與 CLI 共享相同行為。

新增或變更 MCP 工具時，請更新：

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository translation tools are model-callable through MCP and can write many files. Keep `dry_run=True` as the default and require `confirm_write=True` before non-dry-run project translation.

## Translation flow

高階的專案翻譯流程如下：

1. 解析 CLI 參數或 API 參數。
2. 使用 `LLMConfig` 驗證 LLM 配置。
3. 在選擇圖片翻譯時驗證 Azure AI Vision。
4. 正規化語言代碼。
5. 偵測舊版語言資料夾別名。
6. 估算翻譯量。
7. 在適用時更新 README 的語言/課程章節。
8. 將專案翻譯委派給 `ProjectTranslator`。
9. `ProjectTranslator` 將檔案處理委派給 `TranslationManager`。

`TranslationManager` 由專注於檔案類型的 mixins 組成：

- `ProjectMarkdownTranslationMixin` 處理 Markdown 檔案的讀取、內容翻譯、路徑改寫、元資料、免責聲明，以及寫入。
- `ProjectNotebookTranslationMixin` 處理 notebook 檔案的讀取、Markdown 欄位翻譯、路徑改寫、元資料、免責聲明，以及寫入。
- `ProjectImageTranslationMixin` 處理圖片發現、文字擷取/翻譯、渲染圖片寫入，及元資料。

較低階的內容 API 會跳過專案工作流程：

1. `translate_markdown_content` and `translate_notebook_content` 只翻譯記憶體中的內容。
2. `translate_image_content` 翻譯單張圖片中的文字並返回一個渲染後的圖片物件。
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` 是明確的後處理輔助工具。它們不執行翻譯也不進行專案寫入。

## Review flow

確定性的審查流程如下：

1. 解析 CLI 參數或 API 參數。
2. 正規化要求的語言代碼。
3. 從 `root_dir`、`root_dirs` 或 `groups` 建構一個或多個審查目標。
4. 可選地使用 `--changed-from` 限制來源檔案。
5. 執行針對結構、翻譯新鮮度、Markdown 完整性以及本地連結/圖片路徑的確定性檢查。
6. 輸出文字或 GitHub 風格的 Markdown。
7. 當發現審查錯誤時以失敗狀態退出。

審查流程不需要 API 金鑰，且應保持適用於 pull request 的 CI。pull request 的工作流程會在每次執行時寫入檢查摘要，並且只有在 `co-op-review` 失敗時才張貼 PR 評論。

## Documentation site

The docs site is configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 目錄是權威的文件來源。除非專案有意引入另一個已發佈的文件面向，否則不要在此目錄之外新增終端使用者指南。

本地建立：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

本地預覽：

```bash
python -m mkdocs serve
```

產生的網站會寫入 `site/`，該目錄已被 git 忽略。

## GitHub Pages workflow

.github/workflows/docs.yml 在 pull request 時建立網站，並在推送到 `main` 時部署。

該工作流程會安裝：

```bash
pip install -r requirements-docs.txt
```

文件工作流程只安裝文件工具鏈。`mkdocs.yml` 將 `mkdocstrings` 指向 `src/`，因此可以在不安裝完整執行時依賴集合的情況下，從原始碼樹渲染公開 API 頁面。如果未來 API 文件在建置期間需要匯入選用的執行時提供者，請同時更新 `.github/workflows/docs.yml` 與本指南。

## Docs quality bar

在合併文件變更之前，請執行：

```bash
python -m mkdocs build --strict
git diff --check
```

使用嚴格的建置設定，以便在早期讓錯誤連結、無效的導覽條目和 API 呈現問題失敗。