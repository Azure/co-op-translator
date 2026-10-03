# CLI 參考

Co-op Translator 安裝以下命令列進入點：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

這些 `translate`、`evaluate`、`migrate-links` 與 `co-op-review` 命令會經由 `co_op_translator.__main__` 進行分派，該命令會根據被呼叫的腳本名稱選擇命令的實作。MCP 伺服器則直接使用 `co_op_translator.mcp.server`。

如果你在 CLI、Python API 和 MCP 之間抉擇，請從 [選擇你的工作流程](workflows.md) 開始。

## 主控台輸出

互動式終端會使用 Rich 格式化命令標頭、進度與摘要。CI 與非互動輸出會自動回退為純文字。

將 `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` 設為強制純文字輸出，或將 `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` 設為強制使用 Rich 輸出。將 `CO_OP_TRANSLATOR_NO_PROGRESS=1` 設定為在抑制即時進度條時保留摘要。

當其他系統需要機器可讀的進度時，使用 `translate --json-events progress.ndjson`。
CLI 仍會呈現人類可閱讀的輸出，而
NDJSON 檔案會接收版本化的 `co-op.translation.event.v1` 事件，包含
像 `type`、`stage_key`、`completed`、`total` 與
`current_path` 這類穩定欄位。

## 初次使用 CLI 的流程

如果你從終端機使用 Co-op Translator，請從這裡開始：

1. 依照 [設定](configuration.md) 中所述設定 LLM 提供者。
2. 選擇你要翻譯的內容類型。
3. 先執行一個聚焦的命令，例如只翻譯 Markdown。
4. 在對大型儲存庫進行更動前，先使用 `--dry-run`。
5. 翻譯後使用 `co-op-review` 檢查結構與新舊狀態。

| 目標 | 開始使用的命令 |
| --- | --- |
| 翻譯 Markdown 文件 | `translate -l "ko" -md` |
| 翻譯筆記本 | `translate -l "ko" -nb` |
| 翻譯影像文字 | `translate -l "ko" -img` |
| 預覽工作結果而不寫入檔案 | `translate -l "ko" -md --dry-run` |
| 檢閱現有翻譯 | `co-op-review -l "ko"` |
| 更新筆記本和 Markdown 連結 | `migrate-links -l "ko" --dry-run` |
| 向 MCP 用戶端提供工具 | 請設定 [MCP Server](mcp.md)，而不是直接執行 CLI 命令。 |

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

翻譯 Markdown 與影像：

```bash
translate -l "pt-BR" -md -img
```

透過刪除後重新建立來更新現有翻譯：

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

| 選項 | 是否必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的語言代碼，例如 `"es fr de"` 或 `"all"`. |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `-u`, `--update` | No | 刪除所選語言的現有翻譯並重新建立。 |
| `-img`, `--images` | No | 僅翻譯影像檔案。 |
| `-md`, `--markdown` | No | 僅翻譯 Markdown 檔案。 |
| `-nb`, `--notebook` | No | 僅翻譯 Jupyter 筆記本檔案。 |
| `-d`, `--debug` | No | 在主控台啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/`。 |
| `--json-events` | No | 以 NDJSON 寫入機器可讀的翻譯進度事件。 |
| `-x`, `--fix` | No | 根據先前評估結果重新翻譯低信心的 Markdown 檔案。 |
| `-c`, `--min-confidence` | No | 用於 `--fix` 的信心閾值。預設為 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | No | 加入或抑制機器翻譯免責聲明。CLI 中預設為啟用。 |
| `-f`, `--fast` | No | 已棄用的快速影像模式。 |
| `-y`, `--yes` | No | 自動確認提示，適用於 CI。 |
| `--repo-url` | No | 此儲存庫 URL 用於 README 語言表格的 sparse-checkout 建議。 |
| `--migrate-language-folders` | No | 重新命名舊有別名資料夾（例如 `cn` 或 `tw`）為標準 BCP 47 資料夾。 |
| `--dry-run` | No | 預覽語言資料夾遷移和翻譯估計而不寫入檔案。 |

如果沒有提供類型旗標，`translate` 會處理 Markdown、筆記本和影像。影像翻譯需要 Azure AI Vision 的設定。

## evaluate

評估單一語言的已翻譯 Markdown 品質。

!!! warning "實驗性"
    `evaluate` 為實驗性功能。它可以使用基於規則與基於 LLM 的品質檢查，將評估結果寫入翻譯的 metadata，且它的評分模型與 metadata 行為可能會變化。

```bash
evaluate -l "ko"
```

### 常見範例

使用更嚴格的低信心閾值：

```bash
evaluate -l "es" -c 0.8
```

只執行基於規則的檢查：

```bash
evaluate -l "fr" -f
```

只執行基於 LLM 的檢查：

```bash
evaluate -l "ja" -D
```

### 選項

| 選項 | 是否必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | 單一要評估的語言代碼。別名代碼會被正規化。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `-c`, `--min-confidence` | No | 在列出低信心翻譯時使用的閾值。預設為 `0.7`。 |
| `-d`, `--debug` | No | 啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/`。 |
| `-f`, `--fast` | No | 僅基於規則的評估。 |
| `-D`, `--deep` | No | 僅基於 LLM 的評估。 |

預設情況下，`evaluate` 會同時使用基於規則與基於 LLM 的評估。結果會寫入翻譯 metadata 並在主控台中摘要顯示。

## co-op-review

在無 API 憑證下執行確定性的翻譯維護檢查。

!!! note "測試版"
    `co-op-review` 是一個測試版的確定性審查命令。它不會呼叫模型提供者或寫入檔案，但其檢查項目與問題輸出結構可能會演進。

```bash
co-op-review -l "ko"
```

### 常見範例

從目前目錄檢閱韓文與日文翻譯：

```bash
co-op-review -l "ko ja"
```

檢閱特定的專案根目錄：

```bash
co-op-review -l "fr" -r ./my-course
```

在僅翻譯 README 後，僅檢閱 README：

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` 會忽略其他文件與巢狀的 README。若根目錄的 `README.md` 缺失，則會失敗。與 `--changed-from` 結合時，只有在該來源檔案有變更時才會僅檢閱 README。README-only 翻譯會保持來源 README 不變，包括任何共用區段標記。




只檢閱相對於某基準參考（base ref）有變更的原始檔案：

```bash
co-op-review -l "ko" --changed-from origin/main
```

列印 GitHub 風格的 Markdown 輸出以供 CI 摘要：

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 選項

| 選項 | 是否必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | No | 要檢閱的語言代碼。可以多次傳入或以空格分隔的值傳入。預設為所有發現的翻譯語言。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `--changed-from` | No | 用於限制檢閱至有變更之原始檔案的 Git 參考。 |
| `--readme-only` | No | 僅檢閱根目錄 `README.md` 的翻譯。 |
| `--format` | No | 輸出格式：`text` 或 `github`。預設為 `text`。 |

`co-op-review` 目前會檢查缺少的翻譯檔案、缺失或過期的翻譯 metadata、Markdown 的 frontmatter 與程式碼區塊完整性、無效的已翻譯筆記本 JSON，以及缺失的本地 Markdown 或影像連結目標。缺少的連結預設為警告；結構性與新舊性問題會導致命令失敗。

## co-op-translator-mcp

為 agents、編輯器與 MCP 相容的用戶端執行 Co-op Translator MCP 伺服器。

```bash
co-op-translator-mcp
```

預設傳輸為 `stdio`。請參閱 [MCP Server](mcp.md) 指南以瞭解用戶端設定、工具、資源與安全注意事項。

### 選項

| 選項 | 是否必要 | 說明 |
| --- | --- | --- |
| `--transport` | No | MCP 傳輸方式：`stdio`、`streamable-http` 或 `sse`。預設為 `stdio`。 |

## migrate-links

重新處理已翻譯的 Markdown 檔案並更新筆記本連結，使其在可用時指向已翻譯的筆記本。

```bash
migrate-links -l "ko ja"
```

### 常見範例

預覽連結更新：

```bash
migrate-links -l "ko" --dry-run
```

在不要求確認的情況下處理所有支援的語言：

```bash
migrate-links -l "all" -y
```

只有在已存在已翻譯筆記本時才重寫連結：

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 選項

| 選項 | 是否必要 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | 以空格分隔的語言代碼，或 `"all"`。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `--image-dir` | No | 相對於根目錄的已翻譯影像目錄。預設為 `translated_images`。 |
| `--dry-run` | No | 顯示將會變更的檔案而不寫入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | No | 當已翻譯筆記本缺失時使用原始筆記本連結。Enabled by default. |
| `-d`, `--debug` | No | 啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/`。 |
| `-y`, `--yes` | No | 在處理所有語言時自動確認提示。 |

## 環境

當命令需要提供者憑證時，請設定以下其中一組提供者設定。`translate --dry-run` 與 `co-op-review` 不需要提供者憑證：

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

影像翻譯另外需要 Azure AI Vision：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 輸出結構

文字翻譯會寫入：

```text
translations/<language-code>/<original-path>
```

翻譯後的影像輸出會寫入：

```text
translated_images/<language-code>/<original-path>
```

例如，將 `README.md` 與 `docs/setup.md` 翻譯成韓文會產生：

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 可複製貼上的 CLI 範例

將 Markdown 翻譯為三種語言：

```bash
translate -l "ko ja fr" -md
```

僅翻譯筆記本：

```bash
translate -l "zh-CN" -nb
```

僅翻譯影像：

```bash
translate -l "pt-BR" -img
```

預覽 Markdown 翻譯而不寫入檔案：

```bash
translate -l "de es" -md --dry-run
```

修復低信心的 Markdown 翻譯：

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

以 CI 友善方式執行 Markdown 翻譯：

```bash
translate -l "ko ja" -md -y -s
```

檢閱翻譯後的輸出：

```bash
co-op-review -l "ko ja"
```

預覽連結遷移：

```bash
migrate-links -l "ko" --dry-run
```