# CLI 參考

Co-op Translator 安裝以下命令列入口點：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`、`evaluate`、`migrate-links` 與 `co-op-review` 等命令均經由 `co_op_translator.__main__` 分發，該模組根據被呼叫的腳本名稱選擇命令實作。MCP 伺服器則直接使用 `co_op_translator.mcp.server`。

如果您在 CLI、Python API 與 MCP 之間抉擇，請從 [選擇您的工作流程](workflows.md) 開始。

## 主控台輸出

互動式終端會使用 Rich 格式來顯示命令標題、進度與摘要。CI 及非互動輸出則會自動回退為純文字。

若要強制純文字輸出，設定 `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain`；若要強制 Rich 輸出，設定 `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich`。設定 `CO_OP_TRANSLATOR_NO_PROGRESS=1` 可以在抑制即時進度條的同時保留摘要。

當其他系統需要機器可讀的進度時，使用 `translate --json-events progress.ndjson`。
CLI 會繼續呈現面向人類的輸出，同時
NDJSON 檔案會接收版本化的 `co-op.translation.event.v1` 事件，該事件含有穩定欄位例如
`type`、`stage_key`、`completed`、`total` 與
`current_path`。

## 初次使用 CLI 流程

如果您從終端機使用 Co-op Translator，請從這裡開始：

1. 設定一個 LLM 提供者，如 [設定](configuration.md) 所述。
2. 選擇您要翻譯的內容類型。
3. 先執行一個專注的命令，例如只翻譯 Markdown。
4. 在對大型儲存庫做變更前，使用 `--dry-run`。
5. 在翻譯之後使用 `co-op-review` 來檢查結構與新鮮度。

| 目標 | 建議啟動命令 |
| --- | --- |
| 翻譯 Markdown 文件 | `translate -l "ko" -md` |
| 翻譯筆記本 | `translate -l "ko" -nb` |
| 翻譯影像中的文字 | `translate -l "ko" -img` |
| 預覽作業而不寫入檔案 | `translate -l "ko" -md --dry-run` |
| 檢閱既有翻譯 | `co-op-review -l "ko"` |
| 更新筆記本與 Markdown 連結 | `migrate-links -l "ko" --dry-run` |
| 將工具暴露給 MCP 客戶端 | 設定 [MCP 伺服器](mcp.md)，而不是直接執行 CLI 命令。 |

## translate

將 Markdown 檔案、筆記本與影像文字翻譯成一種或多種目標語言。

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

翻譯 Markdown 與影像：

```bash
translate -l "pt-BR" -md -img
```

透過刪除並重新建立來更新現有翻譯：

```bash
translate -l "ko" -u
```

在無互動提示下執行：

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
| `-img`, `--images` | 否 | 僅翻譯影像檔案。 |
| `-md`, `--markdown` | 否 | 僅翻譯 Markdown 檔案。 |
| `-nb`, `--notebook` | 否 | 僅翻譯 Jupyter 筆記本檔案。 |
| `-d`, `--debug` | 否 | 在主控台啟用偵錯日誌。 |
| `-s`, `--save-logs` | 否 | 將 DEBUG 等級的日誌儲存在 `<root-dir>/logs/`。 |
| `--json-events` | 否 | 將機器可讀的翻譯進度事件寫成 NDJSON。 |
| `-x`, `--fix` | 否 | 根據先前評估結果，重新翻譯低信心的 Markdown 檔案。 |
| `-c`, `--min-confidence` | 否 | `--fix` 的信心閾值。預設為 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | 否 | 新增或抑制機器翻譯免責聲明。CLI 預設為啟用。 |
| `-f`, `--fast` | 否 | 已棄用的快速影像模式。 |
| `-y`, `--yes` | 否 | 自動確認提示，適用於 CI。 |
| `--repo-url` | 否 | 用於 README 語言表格稀疏檢出建議的儲存庫 URL。 |
| `--migrate-language-folders` | 否 | 將舊版別名資料夾，例如 `cn` 或 `tw`，重新命名為標準的 BCP 47 資料夾。 |
| `--dry-run` | 否 | 在不寫入檔案的情況下，預覽語言資料夾遷移與翻譯估算。 |

若未提供類型標誌，`translate` 會處理 Markdown、筆記本與影像。影像翻譯需設定 Azure AI Vision。

## evaluate

評估單一語言的已翻譯 Markdown 品質。

!!! warning "實驗性"
    `evaluate` 屬於實驗性功能。它可以使用基於規則與基於 LLM 的品質檢查，將評估結果寫入翻譯中繼資料，其評分模型與中繼資料行為可能會變動。

```bash
evaluate -l "ko"
```

### 常見範例

使用更嚴格的低信心閾值：

```bash
evaluate -l "es" -c 0.8
```

僅執行規則式檢查：

```bash
evaluate -l "fr" -f
```

僅執行基於 LLM 的檢查：

```bash
evaluate -l "ja" -D
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | 是 | 要評估的單一語言代碼。別名代碼會被標準化。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `-c`, `--min-confidence` | 否 | 用於列出低信心翻譯的閾值。預設為 `0.7`。 |
| `-d`, `--debug` | 否 | 啟用偵錯日誌。 |
| `-s`, `--save-logs` | 否 | 將 DEBUG 等級的日誌儲存在 `<root-dir>/logs/`。 |
| `-f`, `--fast` | 否 | 僅規則式評估。 |
| `-D`, `--deep` | 否 | 僅基於 LLM 的評估。 |

預設情況下，`evaluate` 同時使用規則式與基於 LLM 的評估。結果會寫入翻譯中繼資料，並在主控台中摘要顯示。

## co-op-review

在不需要 API 憑證的情況下執行可決定性的翻譯維護檢查。

!!! note "測試版"
    `co-op-review` 是一個測試版的可決定性審查命令。它不會呼叫模型提供者或寫入檔案，但其檢查與問題輸出架構可能會演進。

```bash
co-op-review -l "ko"
```

### 常見範例

從目前目錄檢視韓文與日文翻譯：

```bash
co-op-review -l "ko ja"
```

檢視特定專案根目錄：

```bash
co-op-review -l "fr" -r ./my-course
```

在只翻譯 README 之後，僅檢視 README：

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` 會忽略其他文件與巢狀的 README。若根目錄的 `README.md` 不存在則會失敗。與 `--changed-from` 結合時，它僅在該來源檔案有變更時檢視 README。README-only 的翻譯會保留原始 README 不變，包括任何共用段落標記。




僅檢視相對於基準 ref 有變更的來源檔案：

```bash
co-op-review -l "ko" --changed-from origin/main
```

列印 GitHub 風格的 Markdown 輸出以作為 CI 摘要：

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | 否 | 要檢視的語言代碼。可多次傳入或以空白分隔。預設為所有被發現的翻譯語言。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `--changed-from` | 否 | 用於限制檢視僅針對已變更來源檔案的 Git ref。 |
| `--readme-only` | 否 | 僅檢視根目錄 `README.md` 的翻譯。 |
| `--format` | 否 | 輸出格式：`text` 或 `github`。預設為 `text`。 |

`co-op-review` 目前會檢查缺少的翻譯檔案、缺少或過時的翻譯中繼資料、Markdown frontmatter 與程式碼區塊的完整性、無效的已翻譯筆記本 JSON，以及遺失的本地 Markdown 或影像連結目標。遺失連結預設為警告；結構性與新鮮度問題會導致命令失敗。

## co-op-translator-mcp

為代理人、編輯者與 MCP 相容的用戶端執行 Co-op Translator MCP 伺服器。

```bash
co-op-translator-mcp
```

預設傳輸為 `stdio`。請參閱 [MCP 伺服器](mcp.md) 指南以了解用戶端設定、工具、資源與安全注意事項。

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

重新處理已翻譯的 Markdown 檔案並更新筆記本連結，使其在有已翻譯筆記本時指向翻譯後的筆記本。

```bash
migrate-links -l "ko ja"
```

### 常見範例

預覽連結更新：

```bash
migrate-links -l "ko" --dry-run
```

在不需要確認的情況下處理所有支援的語言：

```bash
migrate-links -l "all" -y
```

僅在已存在已翻譯筆記本時重寫連結：

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 選項

| 選項 | 必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的語言代碼，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為目前目錄。 |
| `--image-dir` | 否 | 已翻譯影像目錄，相對於根目錄。預設為 `translated_images`。 |
| `--dry-run` | 否 | 顯示會被改變的檔案，但不寫入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | 否 | 當缺少已翻譯筆記本時改用原始筆記本連結。預設為啟用。 |
| `-d`, `--debug` | 否 | 啟用偵錯日誌。 |
| `-s`, `--save-logs` | 否 | 將 DEBUG 等級的日誌儲存在 `<root-dir>/logs/`。 |
| `-y`, `--yes` | 否 | 在處理所有語言時自動確認提示。 |

## Environment

當命令需要提供者憑證時，請設定下列其中一組提供者。`translate --dry-run` 與 `co-op-review` 不需要提供者憑證：

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

影像翻譯另需 Azure AI Vision：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 輸出佈局

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

翻譯後的圖片輸出會寫入：

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 可複製貼上的 CLI 範例

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

預覽 Markdown 翻譯而不寫入檔案：

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