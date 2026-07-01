# CLI 參考

Co-op Translator 安裝了以下命令列執行點：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`、`evaluate`、`migrate-links` 與 `co-op-review` 命令會透過 `co_op_translator.__main__` 轉派，該模組會根據被呼叫的腳本名稱選擇命令實作。MCP 伺服器則直接使用 `co_op_translator.mcp.server`。

如果你在 CLI、Python API 與 MCP 之間抉擇，請從 [Choose Your Workflow](workflows.md) 開始。

## 首次使用 CLI 流程

如果你從終端機使用 Co-op Translator，從這裡開始：

1. 如 [Configuration](configuration.md) 所述，設定一個 LLM 提供者。
2. 選擇你想要翻譯的內容類型。
3. 先執行較聚焦的命令，例如僅翻譯 Markdown。
4. 在對大型原始碼庫變更之前使用 `--dry-run`。
5. 翻譯後使用 `co-op-review` 檢查結構和新鮮度。

| 目標 | 建議開始的命令 |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

將 Markdown 檔案、筆記本與圖片文字翻譯成一個或多個目標語言。

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

透過刪除並重建來更新現有翻譯：

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

### 選項

| 選項 | 必須 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的語言代碼，例如 `"es fr de"`，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為當前目錄。 |
| `-u`, `--update` | 否 | 刪除選定語言的現有翻譯並重新建立。 |
| `-img`, `--images` | 否 | 僅翻譯圖片檔案。 |
| `-md`, `--markdown` | 否 | 僅翻譯 Markdown 檔案。 |
| `-nb`, `--notebook` | 否 | 僅翻譯 Jupyter 筆記本檔案。 |
| `-d`, `--debug` | 否 | 在主控台啟用除錯日誌。 |
| `-s`, `--save-logs` | 否 | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/`。 |
| `-x`, `--fix` | 否 | 根據先前的評估結果，重新翻譯低信心的 Markdown 檔案。 |
| `-c`, `--min-confidence` | 否 | `--fix` 使用的信心門檻。預設為 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | 否 | 新增或抑制機器翻譯免責聲明。CLI 預設為啟用。 |
| `-f`, `--fast` | 否 | 已停用的快速圖片模式。 |
| `-y`, `--yes` | 否 | 自動確認提示，適用於 CI。 |
| `--repo-url` | 否 | 用於 README 語言表格 sparse-checkout 建議的儲存庫 URL。 |
| `--migrate-language-folders` | 否 | 將舊版別名資料夾（例如 `cn` 或 `tw`）重新命名為正規的 BCP 47 資料夾。 |
| `--dry-run` | 否 | 預覽語言資料夾遷移與翻譯估計，而不寫入檔案。 |

若未提供類型標誌，`translate` 會處理 Markdown、筆記本與圖片。圖片翻譯需要 Azure AI Vision 的設定。

## evaluate

評估單一語言之翻譯 Markdown 的品質。

!!! warning "實驗性"
    `evaluate` 屬於實驗性功能。它可以使用規則式與 LLM 為基礎的品質檢查，將評估結果寫入翻譯的 metadata，且其評分模型與 metadata 行為可能會變更。

```bash
evaluate -l "ko"
```

### 常見範例

使用更嚴格的低信心門檻：

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

| 選項 | 必須 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | 是 | 要評估的單一語言代碼。別名代碼會被正規化。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為當前目錄。 |
| `-c`, `--min-confidence` | 否 | 用於列出低信心翻譯的門檻。預設為 `0.7`。 |
| `-d`, `--debug` | 否 | 啟用除錯日誌。 |
| `-s`, `--save-logs` | 否 | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/`。 |
| `-f`, `--fast` | 否 | 僅使用規則式評估。 |
| `-D`, `--deep` | 否 | 僅使用基於 LLM 的評估。 |

預設情況下，`evaluate` 同時使用規則式與 LLM 為基礎的評估。結果會寫入翻譯的 metadata 並在主控台摘要顯示。

## co-op-review

在不需要 API 憑證的情況下，執行確定性的翻譯維護檢查。

!!! note "測試版"
    `co-op-review` 是一個測試版的確定性審查命令。它不會呼叫模型提供者或寫入檔案，但其檢查項目與問題輸出結構可能會演進。

```bash
co-op-review -l "ko"
```

### 常見範例

從當前目錄審查韓文與日文翻譯：

```bash
co-op-review -l "ko ja"
```

審查指定的專案根目錄：

```bash
co-op-review -l "fr" -r ./my-course
```

僅審查相對於基準 ref 有變更的原始檔案：

```bash
co-op-review -l "ko" --changed-from origin/main
```

輸出 GitHub-flavored Markdown 以供 CI 摘要：

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 選項

| 選項 | 必須 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | 否 | 要審查的語言代碼。可多次傳入或以空格分隔傳入。預設為所有已發現的翻譯語言。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為當前目錄。 |
| `--changed-from` | 否 | 用來限制僅審查已變更原始檔案的 Git ref。 |
| `--format` | 否 | 輸出格式：`text` 或 `github`。預設為 `text`。 |

`co-op-review` 目前會檢查遺失的翻譯檔案、遺失或過時的翻譯 metadata、Markdown frontmatter 與程式碼區塊完整性、無效的已翻譯筆記本 JSON，以及遺失的本地 Markdown 或圖片連結目標。遺失連結預設為警告；結構性與新鮮度問題會使命令失敗。

## co-op-translator-mcp

為代理人、編輯器和相容 MCP 的用戶端執行 Co-op Translator MCP 伺服器。

```bash
co-op-translator-mcp
```

預設傳輸為 `stdio`。請參閱 [MCP Server](mcp.md) 指南以取得用戶端設定、工具、資源與安全性說明。

### 選項

| 選項 | 必須 | 說明 |
| --- | --- | --- |
| `--transport` | 否 | MCP 傳輸：`stdio`、`streamable-http` 或 `sse`。預設為 `stdio`。 |

## migrate-links

重新處理已翻譯的 Markdown 檔案並更新筆記本連結，使其在有已翻譯筆記本可用時指向已翻譯的筆記本。

```bash
migrate-links -l "ko ja"
```

### 常見範例

預覽連結更新：

```bash
migrate-links -l "ko" --dry-run
```

在不需確認下處理所有支援的語言：

```bash
migrate-links -l "all" -y
```

僅在已存在已翻譯筆記本時重寫連結：

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 選項

| 選項 | 必須 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | 是 | 以空格分隔的語言代碼，或 `"all"`。 |
| `-r`, `--root-dir` | 否 | 專案根目錄。預設為當前目錄。 |
| `--image-dir` | 否 | 相對於根目錄的已翻譯圖片目錄。預設為 `translated_images`。 |
| `--dry-run` | 否 | 顯示會變更的檔案但不寫入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | 否 | 當已翻譯筆記本缺失時使用原始筆記本連結。預設為啟用。 |
| `-d`, `--debug` | 否 | 啟用除錯日誌。 |
| `-s`, `--save-logs` | 否 | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/`。 |
| `-y`, `--yes` | 否 | 在處理所有語言時自動確認提示。 |

## 環境

所有命令皆需要至少一個已設定的 LLM 提供者：

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
```

圖片翻譯此外還需要 Azure AI Vision：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 輸出佈局

文字翻譯會寫入：

```text
translations/<language-code>/<original-path>
```

已翻譯的圖片輸出會寫入：

```text
translated_images/<language-code>/<original-path>
```

例如，將 `README.md` 與 `docs/setup.md` 翻譯成韓文會產生：

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 複製貼上 CLI 範例

將 Markdown 翻譯成三種語言：

```bash
translate -l "ko ja fr" -md
```

僅翻譯筆記本：

```bash
translate -l "zh-CN" -nb
```

僅翻譯圖片：

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

審查翻譯輸出：

```bash
co-op-review -l "ko ja"
```

預覽連結遷移：

```bash
migrate-links -l "ko" --dry-run
```