# 維護者指南

本頁總結了 API、CLI 與文件網站如何串接。

## 公共 API 邊界

穩定的 Python API 從以下位置匯出：

```python
co_op_translator.api
```

公共 API 組織為內容翻譯輔助、路徑重寫輔助、專案協調，以及審查：

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` 是託管整合的持久層邊界。
它必須將產生的候選項目與已接受的基線分開，以便
尚未合併的翻譯不會成為事實來源。

新增公共 API 時，請更新：

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- 位於 `tests/co_op_translator/` 下的相關 API 測試，例如 `test_api.py` 或 `test_review_api.py`

避免將低階的 `core` 模組記錄為穩定 API，除非專案打算直接支援它們。

## CLI 進入點

此套件定義了這些 Poetry 腳本：

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` 依腳本名稱分派：

- `translate` 會呼叫 `co_op_translator.cli.translate.translate_command`
- `evaluate` 會呼叫 `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` 會呼叫 `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` 會呼叫 `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` 會繞過 `__main__.py`，直接呼叫 `co_op_translator.mcp.server:main`。

新增或變更 CLI 選項時，請更新：

- 相關的 `src/co_op_translator/cli/*.py` 指令
- `docs/cli.md`
- 相關的 CLI 測試（若行為改變）

## MCP 伺服器

MCP 伺服器實作於：

```python
co_op_translator.mcp.server
```

伺服器刻意包裝公共 Python API，而不是呼叫較低階的 `core` 模組。請保持此邊界完整，讓 MCP 用戶端、Python 呼叫方與 CLI 擁有相同的行為。

新增或變更 MCP 工具時，請更新：

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- 若公共 API 介面變更，更新 `docs/api.md`

倉庫翻譯工具可透過 MCP 以模型方式呼叫，並可能寫入許多檔案。請維持 `dry_run=True` 為預設，並在非 dry-run 的專案翻譯前要求 `confirm_write=True`。

## 翻譯流程

高階的專案翻譯流程如下：

1. 解析 CLI 參數或 API 參數。
2. 使用 `LLMConfig` 驗證 LLM 設定。
3. 當選擇影像翻譯時，驗證 Azure AI Vision。
4. 正規化語言代碼。
5. 偵測舊有的語言資料夾別名。
6. 估算翻譯量。
7. 在適用時更新 README 的語言/課程章節。
8. 將專案翻譯委派給 `ProjectTranslator`。
9. `ProjectTranslator` 將檔案處理委派給 `TranslationManager`。

`TranslationManager` 由專注於檔案類型的 mixin 組成：

- `ProjectMarkdownTranslationMixin` 處理 Markdown 檔案的讀取、內容翻譯、路徑重寫、元資料、免責聲明與寫入。
- `ProjectNotebookTranslationMixin` 處理 notebook 檔案的讀取、Markdown 單元格翻譯、路徑重寫、元資料、免責聲明與寫入。
- `ProjectImageTranslationMixin` 處理影像探索、文字擷取/翻譯、渲染影像寫入以及元資料。

較低階的內容 API 會略過專案工作流程：

1. `translate_markdown_content` 與 `translate_notebook_content` 僅翻譯記憶體中的內容。
2. `translate_image_content` 翻譯單一影像中的文字並回傳渲染後的影像物件。
3. `rewrite_markdown_paths` 與 `rewrite_notebook_paths` 是明確的後處理輔助工具。它們不執行任何翻譯，也不會進行專案寫入。

## 審查流程

確定性的審查流程如下：

1. 解析 CLI 參數或 API 參數。
2. 正規化請求的語言代碼。
3. 從 `root_dir`、`root_dirs` 或 `groups` 建構一個或多個審查目標。
4. 可選地使用 `--changed-from` 限制來源檔案。
5. 執行確定性檢查，檢視結構、翻譯新鮮度、Markdown 完整性，以及本地連結/影像路徑。
6. 輸出文字或 GitHub 風格的 Markdown。
7. 若發現審查錯誤則以失敗狀態退出。

審查流程不需要 API 金鑰，可用於本地檢查或選擇加入的消費者 CI。本倉庫不會在每個 pull request 自動執行 `co-op-review`。

## 文件網站

文件網站的設定由以下檔案決定：

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 目錄為正規的文件來源。除非專案刻意新增另一個對外發布的文件面向，否則不要在此目錄之外新增終端使用者指南。

在本機建置：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

在本機預覽：

```bash
python -m mkdocs serve
```

產生的網站會寫入 `site/`，此目錄已被 git 忽略。

## GitHub Pages 工作流程

`.github/workflows/docs.yml` 會在 pull request 時建置網站，並在推送到 `main` 時部署。

該工作流程會安裝：

```bash
pip install -r requirements-docs.txt
```

文件工作流程僅安裝文件工具鏈。`mkdocs.yml` 將 `mkdocstrings` 指向 `src/`，因此可以在不安裝完整執行時相依集合的情況下，從原始碼樹渲染公共 API 頁面。如果未來的 API 文件在建置期間需要匯入可選的執行時供應者，請同時更新 `.github/workflows/docs.yml` 和本指南。

## 文件品質門檻

在合併文件變更之前，執行：

```bash
python -m mkdocs build --strict
git diff --check
```

使用嚴格的建置，讓斷鏈、無效的導覽項目與 API 渲染問題能及早失敗。