# CLI 參考

Co-op Translator 安裝以下命令列入口點：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

命令 `translate`、`evaluate`、`migrate-links` 和 `co-op-review` 會透過 `co_op_translator.__main__` 派發，該程式會根據所呼叫的腳本名稱選擇命令實作。MCP 伺服器會直接使用 `co_op_translator.mcp.server`。

如果您在 CLI、Python API 和 MCP 之間選擇，請從 [選擇您的工作流程](workflows.md) 開始。

## 主控台輸出

互動式終端會使用 Rich 格式來顯示命令標頭、進度與摘要。CI 與非互動輸出會自動回退為純文字。

設定 `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` 可強制純文字輸出，或設定 `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` 可強制 Rich 輸出。設定 `CO_OP_TRANSLATOR_NO_PROGRESS=1` 可保留摘要但隱藏即時進度條。

使用 `translate --json-events progress.ndjson` 當另一個系統需要
機器可讀的進度。CLI 同時繼續渲染面向人的輸出，而
NDJSON 檔案會接收版本化的 `co-op.translation.event.v1` 事件，包含
穩定欄位，例如 `type`、`stage_key`、`completed`、`total`，以及
`current_path`。

## 初次使用 CLI 流程

若從終端機使用 Co-op Translator，請從此處開始：

1. 按照 [設定](configuration.md) 中的說明設定 LLM 提供者。
2. 選擇要翻譯的內容類型。
3. 先執行針對性的命令，例如僅翻譯 Markdown。
4. 在大型儲存庫變更前使用 `--dry-run`。
5. 翻譯後使用 `co-op-review` 檢查結構與新鮮度。

| 目標 | 開始指令 |
| --- | --- |
| 翻譯 Markdown 文件 | `translate -l "ko" -md` |
| 翻譯筆記本 | `translate -l "ko" -nb` |
| 翻譯圖片文字 | `translate -l "ko" -img` |
| 預覽作業而不寫入檔案 | `translate -l "ko" -md --dry-run` |
| 審查現有翻譯 | `co-op-review -l "ko"` |
| 更新筆記本與 Markdown 連結 | `migrate-links -l "ko" --dry-run` |
| 將工具暴露給 MCP 用戶端 | 請設定 [MCP Server](mcp.md)，而不是直接執行 CLI 指令。 |

## translate

將 Markdown 檔案、筆記本和影像文字翻譯成一種或多種目標語言。

```bash
translate -l "ko ja fr"
```

### 常見範例

僅翻譯 Markdown：

```bash
translate -l "de" -md
```

僅翻譯筆記本：

```bash
translate -l "zh-CN" -nb
```

翻譯 Markdown 與圖片：

```bash
translate -l "pt-BR" -md -img
```

透過刪除並重新建立來更新現有翻譯：

```bash
translate -l "ko" -u
```

在不顯示互動提示的情況下執行：

```bash
translate -l "ko ja" -md -y
```

儲存日誌：

```bash
translate -l "ko" -s
```

寫入結構化進度事件：

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的語言代碼，例如 `"es fr de"`，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `-u`, `--update` | 否 | 刪除所選語言的既有翻譯並重新建立。 |
| `-img`, `--images` | 否 | 僅翻譯圖片檔案。 |
| `-md`, `--markdown` | 否 | 僅翻譯 Markdown 檔案。 |
| `-nb`, `--notebook` | 否 | 僅翻譯 Jupyter 筆記本檔案。 |
| `-d`, `--debug` | 否 | 在主控台啟用除錯日誌。 |
| `-s`, `--save-logs` | 否 | 在 `<root-dir>/logs/` 下儲存 DEBUG 級別日誌。 |
| `--json-events` | 否 | 將翻譯進度事件以 NDJSON 寫入機器可讀格式。 |
| `-x`, `--fix` | 否 | 根據先前評估結果重新翻譯低信心的 Markdown 檔案。 |
| `-c`, `--min-confidence` | 否 | `--fix` 使用的信心閾值。預設為 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | 否 | 新增或抑制機器翻譯免責聲明。CLI 預設為啟用。 |
| `-f`, `--fast` | 否 | 已棄用的快速圖片模式。 |
| `-y`, `--yes` | 否 | 自動確認提示，適用於 CI。 |
| `--repo-url` | 否 | 用於 README 語言表格 sparse-checkout 建議的儲存庫 URL。 |
| `--migrate-language-folders` | 否 | 將舊有別名資料夾（例如 `cn` 或 `tw`）重新命名為標準的 BCP 47 資料夾。 |
| `--dry-run` | 否 | 預覽語言資料夾遷移與翻譯估算，但不寫入檔案。 |

如果未提供類型標誌，`translate` 會處理 Markdown、notebooks 與 images。影像翻譯需要配置 Azure AI Vision。

## evaluate

評估單一語言的翻譯後 Markdown 的品質。

!!! warning "實驗性"
    `evaluate` 是實驗性的。它可以使用基於規則和基於 LLM 的品質檢查，將評估結果寫入翻譯的中繼資料，且其評分模型與中繼資料的行為可能會變更。

```bash
evaluate -l "ko"
```

### 常見範例

使用更嚴格的低信心閾值：

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | 是 | 要評估的單一語言代碼。別名代碼會被正規化。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `-c`, `--min-confidence` | 否 | 列出低信心翻譯時使用的閾值。預設為 `0.7`。 |
| `-d`, `--debug` | 否 | 啟用除錯日誌。 |
| `-s`, `--save-logs` | 否 | 在 `<root-dir>/logs/` 下儲存 DEBUG 級別日誌。 |
| `-f`, `--fast` | 否 | 僅基於規則的評估。 |
| `-D`, `--deep` | 否 | 僅基於 LLM 的評估。 |

預設情況下，`evaluate` 同時使用基於規則和基於 LLM 的評估。結果會寫入翻譯的中繼資料，並在主控台中摘要顯示。

## co-op-review

在不使用 API 憑證的情況下執行確定性翻譯維護檢查。

!!! note "測試版"
    `co-op-review` 是測試版的確定性審查命令。它不會呼叫模型提供者或寫入檔案，但其檢查與問題輸出結構可能會變動。

```bash
co-op-review -l "ko"
```

### 常見範例

檢查當前目錄中的韓文與日文翻譯：

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

在僅翻譯 README 後只檢查 README：

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` 會忽略其他文件與巢狀的 README。當根目錄的
`README.md` 缺失。與 `--changed-from` 結合時，它僅在該來源檔案變更時才審查 README。
當該來源檔案發生變更時。
僅翻譯 README 的做法會保留原始 README 不變，包括任何共用區段標記。

僅審查相對某個基礎參考有變更的來源檔案：

```bash
co-op-review -l "ko" --changed-from origin/main
```

為 CI 摘要輸出 GitHub 風格的 Markdown:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | 否 | 要審查的語言代碼。可多次傳入或以空格分隔。預設為所有偵測到的翻譯語言。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `--changed-from` | 否 | 用於限制審查到已變更原始檔案的 Git 參考。 |
| `--readme-only` | 否 | 僅審查根目錄的 `README.md` 翻譯。 |
| `--format` | 否 | 輸出格式：`text` 或 `github`。預設為 `text`。 |

`co-op-review` 目前會檢查遺失的翻譯檔案、遺失或過時的翻譯元資料、Markdown 前置欄位（frontmatter）與程式碼區塊（code fence）的完整性、無效的已翻譯筆記本 JSON，以及遺失的本地 Markdown 或圖片連結目標。遺失的連結預設會視為警告；結構性與時效性問題會使此命令失敗。

## co-op-translator-mcp

為代理、編輯器，和 MCP 相容的用戶端執行 Co-op Translator MCP 伺服器。

```bash
co-op-translator-mcp
```

預設的傳輸為 `stdio`。請參閱 [MCP 伺服器](mcp.md) 指南，了解用戶端設定、工具、資源與安全注意事項。

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `--transport` | 否 | MCP 傳輸方式：`stdio`、`streamable-http`，或 `sse`。預設為 `stdio`。 |

## migrate-links

重新處理已翻譯的 Markdown 檔案，並更新筆記本連結，使其在有翻譯筆記本時指向翻譯後的版本。

```bash
migrate-links -l "ko ja"
```

### 常見範例

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

在不需確認的情況下處理所有支援的語言:

```bash
migrate-links -l "all" -y
```

僅在已存在翻譯後的筆記本時重寫連結:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的語言代碼，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `--image-dir` | 否 | 相對於根目錄的已翻譯圖片資料夾。預設為 `translated_images`。 |
| `--dry-run` | 否 | 顯示將會變更的檔案但不寫入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | 否 | 在缺少翻譯筆記本時使用原始筆記本連結。預設為啟用。 |
| `-d`, `--debug` | 否 | 啟用除錯日誌。 |
| `-s`, `--save-logs` | 否 | 在 `<root-dir>/logs/` 下儲存 DEBUG 級別日誌。 |
| `-y`, `--yes` | 否 | 在處理所有語言時自動確認提示。 |

## 環境

當指令需要提供者憑證時，請設定下列其中一組提供者設定。`translate --dry-run` 和 `co-op-review` 不需要提供者憑證：

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 或 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# 或 Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

影像翻譯另外需要 Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 輸出佈局

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

翻譯後的影像輸出會寫入:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 複製貼上 CLI 範例

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

預覽 Markdown 翻譯而不寫入檔案:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```