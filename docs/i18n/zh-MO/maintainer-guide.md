# 維護者指南

此頁面總結了 API、CLI 與文件網站如何互相串連。

## 公共 API 邊界

穩定的 Python API 從以下位置匯出：

```python
co_op_translator.api
```

公開的 API 組織為內容翻譯輔助、路徑重寫輔助、專案協調與審查：

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

當新增公開 API 時，請更新：

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- 相關的 API 測試於 `tests/co_op_translator/`，例如 `test_api.py` 或 `test_review_api.py`

除非專案打算直接支援，否則避免將較低階的 `core` 模組記錄為穩定 API。

## CLI 進入點

套件定義了下列 Poetry 腳本：

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` 依腳本名稱派送：

- `translate` 呼叫 `co_op_translator.cli.translate.translate_command`
- `evaluate` 呼叫 `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` 呼叫 `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` 呼叫 `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` 繞過 `__main__.py`，直接呼叫 `co_op_translator.mcp.server:main`。

在新增或更改 CLI 選項時，請更新：

- 相關的 `src/co_op_translator/cli/*.py` 命令
- `docs/cli.md`
- 若行為改變則更新 CLI 相關測試

## MCP 伺服器

MCP 伺服器實作於：

```python
co_op_translator.mcp.server
```

伺服器刻意包裝公開的 Python API，而非呼叫較低階的 `core` 模組。請保持此邊界完整，以便 MCP 用戶端、Python 呼叫端與 CLI 共享相同的行為。

在新增或更改 MCP 工具時，請更新：

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- 若公共 API 表面改變，請更新 `docs/api.md`

倉庫翻譯工具可透過 MCP 由模型呼叫並可寫入多個檔案。請保持 `dry_run=True` 為預設，並在非 dry-run 的專案翻譯前要求 `confirm_write=True`。

## 翻譯流程

高階的專案翻譯流程為：

1. 解析 CLI 參數或 API 參數。
2. 使用 `LLMConfig` 驗證 LLM 設定。
3. 當選擇影像翻譯時驗證 Azure AI Vision。
4. 正規化語言代碼。
5. 偵測舊有語言資料夾別名。
6. 預估翻譯量。
7. 在適用時更新 README 的語言/課程部分。
8. 將專案翻譯委派給 `ProjectTranslator`。
9. `ProjectTranslator` 將檔案處理委派給 `TranslationManager`。

`TranslationManager` 由專注於檔案類型的 mixins 組成：

- `ProjectMarkdownTranslationMixin` 處理 Markdown 檔案的讀取、內容翻譯、路徑重寫、metadata、免責聲明與寫入。
- `ProjectNotebookTranslationMixin` 處理筆記本檔案的讀取、Markdown 儲存格翻譯、路徑重寫、metadata、免責聲明與寫入。
- `ProjectImageTranslationMixin` 處理影像發現、文字擷取/翻譯、渲染影像寫入與 metadata。

較低階的內容 API 會跳過專案工作流程：

1. `translate_markdown_content` 與 `translate_notebook_content` 僅對記憶體中的內容進行翻譯。
2. `translate_image_content` 翻譯單一影像中的文字並回傳渲染後的影像物件。
3. `rewrite_markdown_paths` 與 `rewrite_notebook_paths` 為明確的後處理輔助。它們不執行翻譯，亦不進行專案寫入。

## 審查流程

確定性的審查流程為：

1. 解析 CLI 參數或 API 參數。
2. 正規化請求的語言代碼。
3. 從 `root_dir`、`root_dirs` 或 `groups` 建立一或多個審查目標。
4. 可選地使用 `--changed-from` 限制來源檔案。
5. 執行結構、翻譯新鮮度、Markdown 完整性與本地連結/影像路徑的確定性檢查。
6. 輸出純文字或 GitHub 風格的 Markdown。
7. 當發現審查錯誤時以失敗狀態退出。

審查流程不需要 API 金鑰，且應維持適合 pull request CI 使用。pull request 工作流程在每次執行時會寫入一份檢查摘要，僅在 `co-op-review` 失敗時發佈 PR 評論。

## 文件網站

文件網站由下列項目配置：

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 目錄是權威的文件來源。除非專案刻意引入另一個已發佈的文件介面，否則不要在此目錄外新增終端使用者指南。

本地建構：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

本地預覽：

```bash
python -m mkdocs serve
```

產生的網站會寫入 `site/`，該目錄被 git 忽略。

## GitHub Pages 工作流程

`.github/workflows/docs.yml` 在 pull requests 時建置網站，並在推送到 `main` 時部署。

該工作流程安裝：

```bash
pip install -r requirements-docs.txt
```

文件工作流程僅安裝文件工具鏈。`mkdocs.yml` 指向 `mkdocstrings` 到 `src/`，因此公共 API 頁面可以從原始碼樹呈現，而無需安裝完整的執行時相依集合。若未來 API 文件在建置時需要匯入選用的執行時提供者，請同時更新 `.github/workflows/docs.yml` 與本指南。

## 文件品質門檻

在合併文件變更之前，執行：

```bash
python -m mkdocs build --strict
git diff --check
```

使用嚴格的建置設定，以便損壞的連結、無效的導覽項目和 API 呈現問題能及早失敗。