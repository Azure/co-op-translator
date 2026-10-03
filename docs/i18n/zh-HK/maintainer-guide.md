# 維護者指南

本頁總覽 API、CLI 及文件網站如何相互串接。

## 公共 API 邊界

穩定的 Python API 從下列位置匯出：

```python
co_op_translator.api
```

公開 API 組織為內容翻譯輔助工具、路徑重寫輔助工具、專案協調，以及審查：

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

`TranslationStateProvider` 是託管整合的持久化邊界。
它必須將生成的候選項與已接受的基準分開，所以一個
未合併的翻譯不能成為真實來源。

新增公開 API 時，更新：

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- 對應的 API 測試位於 `tests/co_op_translator/`，例如 `test_api.py` 或 `test_review_api.py`

除非專案打算直接支援，否則避免將較低層的 `core` 模組文件化為穩定 API。

## CLI 入口點

此套件定義了這些 Poetry 腳本：

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` 會根據腳本名稱分派：

- `translate` 會呼叫 `co_op_translator.cli.translate.translate_command`
- `evaluate` 會呼叫 `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` 會呼叫 `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` 會呼叫 `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` 會繞過 `__main__.py` 並直接呼叫 `co_op_translator.mcp.server:main`。

新增或更改 CLI 選項時，請更新：

- 相關的 `src/co_op_translator/cli/*.py` 指令
- `docs/cli.md`
- CLI 相關的測試（若行為變更）

## MCP server

MCP 伺服器實作於：

```python
co_op_translator.mcp.server
```

伺服器刻意包裝公開的 Python API，而不是直接呼叫較低層的 `core` 模組。請維持此邊界，以確保 MCP 客戶端、Python 呼叫端和 CLI 具有一致的行為。

新增或更改 MCP 工具時，請更新：

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`（若公開 API 範圍改變）

倉庫翻譯工具可以透過 MCP 被模型呼叫並能寫入多個檔案。預設請保持 `dry_run=True`，並在非 dry-run 的專案翻譯之前要求 `confirm_write=True`。

## 翻譯流程

高階專案翻譯流程如下：

1. 解析 CLI 參數或 API 參數。
2. 使用 `LLMConfig` 驗證 LLM 配置。
3. 當選擇圖像翻譯時，驗證 Azure AI Vision。
4. 正規化語言代碼。
5. 偵測舊版語言資料夾別名。
6. 估算翻譯量。
7. 在適用時更新 README 的語言/課程章節。
8. 將專案翻譯委派給 `ProjectTranslator`。
9. `ProjectTranslator` 將檔案處理委派給 `TranslationManager`。

`TranslationManager` 由專注於檔案類型的 mixin 組成：

- `ProjectMarkdownTranslationMixin` 處理 Markdown 檔案的讀取、內容翻譯、路徑重寫、元資料、免責聲明，以及寫入。
- `ProjectNotebookTranslationMixin` 處理 notebook 檔案的讀取、Markdown cell 的翻譯、路徑重寫、元資料、免責聲明，以及寫入。
- `ProjectImageTranslationMixin` 處理影像發現、文字抽取/翻譯、渲染後影像的寫入，以及元資料。

較低層的內容 API 會跳過專案工作流程：

1. `translate_markdown_content` 與 `translate_notebook_content` 僅翻譯記憶體中的內容。
2. `translate_image_content` 會翻譯單張影像中的文字並返回一個已渲染的影像物件。
3. `rewrite_markdown_paths` 與 `rewrite_notebook_paths` 是明確的後處理輔助工具。它們不進行翻譯，也不執行專案寫入。

## 審核流程

確定性審查流程如下：

1. 解析 CLI 參數或 API 參數。
2. 正規化所請求的語言代碼。
3. 從 `root_dir`、`root_dirs` 或 `groups` 建立一個或多個審查目標。
4. 可選地使用 `--changed-from` 限制來源檔案。
5. 執行確定性檢查以檢視結構、翻譯新鮮度、Markdown 完整性，以及本地連結/影像路徑。
6. 輸出文字或 GitHub 風格的 Markdown。
7. 若發現審查錯誤則以失敗狀態退出。

審查流程不需要 API 金鑰，仍可用於本地檢查或選擇加入的消費者 CI。本倉庫不會在每個 pull request 自動執行 `co-op-review`。

## 文件網站

文件網站由下列項目設定：

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 目錄是權威的文件來源。除非專案有意引入另一個已發佈的文件面向，否則不要在此目錄外新增終端使用者指南。

在本機建置：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

在本機預覽：

```bash
python -m mkdocs serve
```

產生的網站會寫入 `site/`，該目錄被 git 忽略。

## GitHub Pages 工作流程

`.github/workflows/docs.yml` 會在 pull request 上建置網站，並在推送到 `main` 時部署。

該工作流程會安裝：

```bash
pip install -r requirements-docs.txt
```

文件工作流程僅安裝文件工具鏈。`mkdocs.yml` 將 `mkdocstrings` 指向 `src/`，以便能夠從原始碼樹渲染公開 API 頁面，而不需安裝完整的執行時相依套件。如果未來的 API 文件在建置時需要匯入選用的執行時提供者，請同時更新 `.github/workflows/docs.yml` 與本指南。

## 文件質量門檻

在合併文件變更前，執行：

```bash
python -m mkdocs build --strict
git diff --check
```

使用嚴格的建置，讓壞掉的連結、無效的導覽項目和 API 渲染問題能夠及早失敗。