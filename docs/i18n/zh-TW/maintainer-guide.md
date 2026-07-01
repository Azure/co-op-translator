# 維護者指南

本頁摘要說明 API、CLI 與文件網站如何串接在一起。

## 公開 API 邊界

穩定的 Python API 匯出自：

```python
co_op_translator.api
```

公開 API 組織為內容翻譯輔助、路徑重寫輔助、專案協調與審查：

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
- 位於 `tests/co_op_translator/` 下的相關 API 測試，例如 `test_api.py` 或 `test_review_api.py`

避免將較低階的 `core` 模組記錄為穩定 API，除非專案打算直接支援它們。

## CLI 進入點

套件定義了這些 Poetry 腳本：

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` 會根據腳本名稱進行分派：

- `translate` 會呼叫 `co_op_translator.cli.translate.translate_command`
- `evaluate` 會呼叫 `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` 會呼叫 `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` 會呼叫 `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` 會繞過 `__main__.py`，直接呼叫 `co_op_translator.mcp.server:main`。

新增或變更 CLI 選項時，請更新：

- 相關的 `src/co_op_translator/cli/*.py` 指令
- `docs/cli.md`
- 若行為變更，更新 CLI 相關測試

## MCP 伺服器

MCP 伺服器實作位於：

```python
co_op_translator.mcp.server
```

伺服器有意封裝公開的 Python API，而不是直接呼叫較低階的 `core` 模組。請保持此邊界不變，以確保 MCP 用戶端、Python 呼叫端與 CLI 有相同的行為。

新增或變更 MCP 工具時，請更新：

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`（如果公開 API 介面有變更）

儲存庫翻譯工具可以透過 MCP 作為模型呼叫，並可能寫入多個檔案。請將 `dry_run=True` 保持為預設，且在非 dry-run 的專案翻譯前要求 `confirm_write=True`。

## 翻譯流程

高階的專案翻譯流程為：

1. 解析 CLI 參數或 API 參數。
2. 使用 `LLMConfig` 驗證 LLM 配置。
3. 當選擇圖片翻譯時，驗證 Azure AI Vision。
4. 標準化語言代碼。
5. 偵測舊版語言資料夾別名。
6. 估算翻譯量。
7. 在適用時更新 README 的語言/課程章節。
8. 將專案翻譯委派給 `ProjectTranslator`。
9. `ProjectTranslator` 將檔案處理委派給 `TranslationManager`。

`TranslationManager` 由專注於檔案類型的 mixin 組成：

- `ProjectMarkdownTranslationMixin` 處理 Markdown 檔案的讀取、內容翻譯、路徑重寫、metadata、免責聲明與寫入。
- `ProjectNotebookTranslationMixin` 處理筆記本檔案的讀取、Markdown 儲存格翻譯、路徑重寫、metadata、免責聲明與寫入。
- `ProjectImageTranslationMixin` 處理影像發現、文字擷取/翻譯、渲染後影像的寫入，以及 metadata。

較低層級的內容 API 則會跳過專案工作流程：

1. `translate_markdown_content` 和 `translate_notebook_content` 僅翻譯記憶體中的內容。
2. `translate_image_content` 會翻譯單張影像中的文字並回傳一個渲染後的影像物件。
3. `rewrite_markdown_paths` 和 `rewrite_notebook_paths` 是明確的後處理輔助工具。它們不執行任何翻譯，也不進行專案寫入。

## 審查流程

確定性的審查流程為：

1. 解析 CLI 參數或 API 參數。
2. 標準化所要求的語言代碼。
3. 從 `root_dir`、`root_dirs` 或 `groups` 建立一個或多個審查目標。
4. 可選地使用 `--changed-from` 限制來源檔案。
5. 執行針對結構、翻譯新鮮度、Markdown 完整性，以及本地連結/影像路徑的確定性檢查。
6. 輸出純文字或 GitHub 風格的 Markdown。
7. 當發現審查錯誤時以失敗狀態退出。

審查流程不需要 API 金鑰，應當仍適用於 pull request 的 CI。pull request 工作流程在每次執行時都會寫入檢查摘要，僅在 `co-op-review` 失敗時才張貼 PR 評論。

## 文件網站

文件網站由下列設定：

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 目錄是權威的文件來源。除非專案有意引入其他發佈的文件介面，否則請勿在此目錄之外新增終端使用者指南。

在本機建置：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

在本機預覽：

```bash
python -m mkdocs serve
```

產生的網站會寫入 `site/`，該目錄已被 git 忽略。

## GitHub Pages 工作流程

`.github/workflows/docs.yml` 在 pull request 時建置網站，並在推送到 `main` 時部署它。

該工作流程會安裝：

```bash
pip install -r requirements-docs.txt
```

文件工作流程僅安裝文件工具鏈。`mkdocs.yml` 將 `mkdocstrings` 指向 `src/`，以便可以從原始碼樹渲染公開 API 頁面，而無需安裝完整的執行時相依集合。如果未來 API 文件在建置期間需要匯入可選的執行時提供者，請同時更新 `.github/workflows/docs.yml` 與本指南。

## 文件品質門檻

在合併文件變更之前，請執行：

```bash
python -m mkdocs build --strict
git diff --check
```

使用嚴格的建置，使破損的連結、無效的導覽項目與 API 呈現問題能及早失敗。