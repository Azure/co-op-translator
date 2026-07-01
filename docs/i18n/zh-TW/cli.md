# CLI 參考

Co-op Translator 安裝這些命令列進入點：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`、`evaluate`、`migrate-links` 與 `co-op-review` 指令會透過 `co_op_translator.__main__` 轉派，該模組會根據被呼叫的腳本名稱選擇指令實作。MCP 伺服器則直接使用 `co_op_translator.mcp.server`。

如果您在 CLI、Python API 與 MCP 之間做選擇，請從 [選擇您的工作流程](workflows.md) 開始。

## First-Time CLI Flow

如果您從終端機使用 Co-op Translator，請從這裡開始：

1. 如 [設定](configuration.md) 所述，配置一個 LLM 提供者。
2. 選擇您想要翻譯的內容類型。
3. 先執行一個專注的指令，例如僅翻譯 Markdown。
4. 在對大型儲存庫做出更改前，先使用 `--dry-run`。
5. 翻譯後使用 `co-op-review` 來檢查結構與是否為最新。

| 目標 | 建議起始指令 |
| --- | --- |
| 翻譯 Markdown 文件 | `translate -l "ko" -md` |
| 翻譯筆記本 | `translate -l "ko" -nb` |
| 翻譯影像文字 | `translate -l "ko" -img` |
| 預覽作業而不寫入檔案 | `translate -l "ko" -md --dry-run` |
| 審查現有翻譯 | `co-op-review -l "ko"` |
| 更新筆記本與 Markdown 的連結 | `migrate-links -l "ko" --dry-run` |
| 將工具暴露給 MCP 用戶端 | 改為設定 [MCP Server](mcp.md)，而不是直接執行 CLI 指令。 |

## translate

將 Markdown 文件、筆記本與影像文字翻譯成一種或多種目標語言。

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

在非互動模式下執行：

```bash
translate -l "ko ja" -md -y
```

儲存日誌：

```bash
translate -l "ko" -s
```

### 選項

| 選項 | 必填 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | 以空格分隔的語言代碼，例如 "es fr de"，或 `"all"`。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `-u`, `--update` | No | 刪除所選語言的現有翻譯並重新建立之。 |
| `-img`, `--images` | No | 僅翻譯影像檔案。 |
| `-md`, `--markdown` | No | 僅翻譯 Markdown 檔案。 |
| `-nb`, `--notebook` | No | 僅翻譯 Jupyter 筆記本檔案。 |
| `-d`, `--debug` | No | 在主控台啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 級別日誌儲存於 `<root-dir>/logs/` 下。 |
| `-x`, `--fix` | No | 根據先前的評估結果，重新翻譯低信心的 Markdown 檔案。 |
| `-c`, `--min-confidence` | No | `--fix` 使用的信心門檻。預設為 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | No | 新增或抑制機器翻譯免責聲明。CLI 預設為啟用。 |
| `-f`, `--fast` | No | 已棄用的快速影像模式。 |
| `-y`, `--yes` | No | 自動確認提示，適用於 CI。 |
| `--repo-url` | No | 用於 README 語言表稀疏檢出建議的儲存庫 URL。 |
| `--migrate-language-folders` | No | 重新命名舊版別名資料夾（例如 `cn` 或 `tw`）為標準的 BCP 47 資料夾。 |
| `--dry-run` | No | 預覽語言資料夾遷移與翻譯估計，但不寫入檔案。 |

如果未提供類型旗標，`translate` 會處理 Markdown、筆記本與影像。影像翻譯需要 Azure AI Vision 的設定。

## evaluate

評估單一語言的已翻譯 Markdown 品質。

!!! warning "實驗性"
    `evaluate` 為實驗性功能。它可以使用基於規則與基於 LLM 的品質檢查，將評估結果寫入翻譯的 metadata，且其評分模型與 metadata 行為可能會變動。

```bash
evaluate -l "ko"
```

### 常見範例

使用較嚴格的低信心門檻：

```bash
evaluate -l "es" -c 0.8
```

僅執行基於規則的檢查：

```bash
evaluate -l "fr" -f
```

僅執行基於 LLM 的檢查：

```bash
evaluate -l "ja" -D
```

### 選項

| 選項 | 必填 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | 要評估的單一語言代碼。別名代碼會被正規化。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `-c`, `--min-confidence` | No | 列出低信心翻譯時使用的門檻。預設為 `0.7`。 |
| `-d`, `--debug` | No | 啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 級別日誌儲存於 `<root-dir>/logs/` 下。 |
| `-f`, `--fast` | No | 僅進行基於規則的評估。 |
| `-D`, `--deep` | No | 僅進行基於 LLM 的評估。 |

預設情況下，`evaluate` 會同時使用基於規則與基於 LLM 的評估。結果會寫入翻譯 metadata 並在主控台中摘要顯示。

## co-op-review

在不使用 API 憑證的情況下執行確定性的翻譯維護檢查。

!!! note "測試版"
    `co-op-review` 為測試版的確定性審查指令。它不會呼叫模型提供者或寫入檔案，但其檢查項目與問題輸出結構可能會演化。

```bash
co-op-review -l "ko"
```

### 常見範例

從目前目錄審查韓文與日文翻譯：

```bash
co-op-review -l "ko ja"
```

審查特定的專案根目錄：

```bash
co-op-review -l "fr" -r ./my-course
```

僅審查相對於某個基準 ref 已變更的原始檔案：

```bash
co-op-review -l "ko" --changed-from origin/main
```

為 CI 摘要列印 GitHub-flavored Markdown 的輸出：

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 選項

| 選項 | 必填 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | No | 要審查的語言代碼。可以多次傳入或以空格分隔。預設為所有已發現的翻譯語言。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `--changed-from` | No | 用於限制審查僅包含變更過的原始檔案的 Git ref。 |
| `--format` | No | 輸出格式：`text` 或 `github`。預設為 `text`。 |

`co-op-review` 目前會檢查缺少的已翻譯檔案、缺失或已過時的翻譯 metadata、Markdown frontmatter 與 code fence 的完整性、無效的已翻譯筆記本 JSON，以及本地 Markdown 或影像連結目標缺失。連結缺失預設為警告；結構性與新鮮度問題會使指令失敗。

## co-op-translator-mcp

為 agent、編輯器和 MCP 相容的用戶端執行 Co-op Translator MCP 伺服器。

```bash
co-op-translator-mcp
```

預設傳輸為 `stdio`。請參閱 [MCP Server](mcp.md) 指南，了解用戶端設定、工具、資源與安全注意事項。

### 選項

| 選項 | 必填 | 說明 |
| --- | --- | --- |
| `--transport` | No | MCP 傳輸：`stdio`、`streamable-http` 或 `sse`。預設為 `stdio`。 |

## migrate-links

重新處理已翻譯的 Markdown 檔案並更新筆記本連結，當有對應的已翻譯筆記本時指向該翻譯版本。

```bash
migrate-links -l "ko ja"
```

### 常見範例

預覽連結更新：

```bash
migrate-links -l "ko" --dry-run
```

在不需確認的情況下處理所有支援的語言：

```bash
migrate-links -l "all" -y
```

只有當已存在翻譯筆記本時才重寫連結：

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 選項

| 選項 | 必填 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | 以空格分隔的語言代碼，或 `"all"`。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為目前目錄。 |
| `--image-dir` | No | 相對於根目錄的已翻譯影像資料夾。預設為 `translated_images`。 |
| `--dry-run` | No | 顯示會被修改的檔案但不寫入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | No | 當缺少已翻譯筆記本時是否使用原始筆記本連結。預設為啟用。 |
| `-d`, `--debug` | No | 啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 級別日誌儲存於 `<root-dir>/logs/` 下。 |
| `-y`, `--yes` | No | 在處理所有語言時自動確認提示。 |

## Environment

所有指令都需要配置一個 LLM 提供者：

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

影像翻譯另需 Azure AI Vision：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

文字翻譯輸出會寫在：

```text
translations/<language-code>/<original-path>
```

翻譯後的影像輸出會寫在：

```text
translated_images/<language-code>/<original-path>
```

例如，將 `README.md` 與 `docs/setup.md` 翻譯成韓語時會產生：

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

將 Markdown 翻譯成三種語言：

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

審查翻譯輸出：

```bash
co-op-review -l "ko ja"
```

預覽連結遷移：

```bash
migrate-links -l "ko" --dry-run
```