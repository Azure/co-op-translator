# CLI 參考

Co-op Translator 會安裝以下命令列入口點：

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`、`evaluate`、`migrate-links` 和 `co-op-review` 命令透過 `co_op_translator.__main__` 分派，該模組會根據被呼叫的腳本名稱選擇命令實作。MCP 伺服器則直接使用 `co_op_translator.mcp.server`。

如果你正在在 CLI、Python API 與 MCP 之間做選擇，請先參閱 [選擇你的工作流程](workflows.md)。

## 初次使用 CLI 流程

如果你從終端機使用 Co-op Translator，從這裡開始：

1. 如 [Configuration](configuration.md) 所述設定 LLM 提供者。
2. 選擇你要翻譯的內容類型。
3. 先執行專注的命令，例如僅翻譯 Markdown。
4. 在對大型倉庫做變更前請使用 `--dry-run`。
5. 翻譯後使用 `co-op-review` 檢查結構與新鮮度。

| 目標 | 開始使用的命令 |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### 常見範例

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Update existing translations by deleting and recreating them:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

### 選項

| 選項 | 必需 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | 以空格分隔的語言代碼，例如 `"es fr de"`，或 `"all"`。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為當前目錄。 |
| `-u`, `--update` | No | 刪除已存在的所選語言翻譯並重新建立。 |
| `-img`, `--images` | No | 僅翻譯圖片檔案。 |
| `-md`, `--markdown` | No | 僅翻譯 Markdown 檔案。 |
| `-nb`, `--notebook` | No | 僅翻譯 Jupyter 筆記本檔案。 |
| `-d`, `--debug` | No | 在主控台啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/` 底下。 |
| `-x`, `--fix` | No | 根據先前的評估結果，重新翻譯低可信度的 Markdown 檔案。 |
| `-c`, `--min-confidence` | No | `--fix` 使用的信心閾值。預設為 `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | No | 新增或抑制機器翻譯免責聲明。CLI 中預設為啟用。 |
| `-f`, `--fast` | No | 已棄用的快速圖片模式。 |
| `-y`, `--yes` | No | 自動確認提示，在 CI 中很有用。 |
| `--repo-url` | No | 用於 README 語言表格 sparse-checkout 建議的倉庫 URL。 |
| `--migrate-language-folders` | No | 將舊版別名資料夾（例如 `cn` 或 `tw`）重新命名為標準的 BCP 47 資料夾。 |
| `--dry-run` | No | 預覽語言資料夾遷移與翻譯估計，不寫入檔案。 |

若未提供任何類型旗標，`translate` 會處理 Markdown、筆記本與圖片。圖片翻譯需要 Azure AI Vision 的設定。

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "實驗性"
    `evaluate` 為實驗性功能。它可以使用規則式與 LLM 為基礎的品質檢查，將評估結果寫入翻譯的 metadata，且其評分模型與 metadata 行為可能會變動。

```bash
evaluate -l "ko"
```

### 常見範例

Use a stricter low-confidence threshold:

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

| 選項 | 必需 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | 要評估的單一語言代碼。別名代碼會被正規化。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為當前目錄。 |
| `-c`, `--min-confidence` | No | 列出低可信度翻譯時使用的閾值。預設為 `0.7`。 |
| `-d`, `--debug` | No | 啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/` 底下。 |
| `-f`, `--fast` | No | 僅執行規則式評估。 |
| `-D`, `--deep` | No | 僅執行 LLM 為基礎的深度評估。 |

預設情況下，`evaluate` 會同時使用規則式與 LLM 為基礎的評估。結果會寫入翻譯 metadata，並在主控台中摘要顯示。

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "測試版"
    `co-op-review` 是一個測試版的確定性檢查命令。它不會呼叫模型提供者或寫入檔案，但其檢查項目與問題輸出架構可能會演進。

```bash
co-op-review -l "ko"
```

### 常見範例

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 選項

| 選項 | 必需 | 說明 |
| --- | --- | --- |
| `-l`, `--language-code` | No | 要檢查的語言代碼。可多次傳入或以空格分隔。預設為所有發現的翻譯語言。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為當前目錄。 |
| `--changed-from` | No | 用以限制檢查僅針對變更過的來源檔案的 Git 參考。 |
| `--format` | No | 輸出格式：`text` 或 `github`。預設為 `text`。 |

`co-op-review` 目前會檢查遺失的翻譯檔案、遺失或過期的翻譯 metadata、Markdown frontmatter 與程式碼區塊完整性、無效的翻譯後筆記本 JSON，以及遺失的本地 Markdown 或圖片連結目標。遺失連結預設為警告；結構性與新鮮度問題則會讓命令失敗。

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### 選項

| 選項 | 必需 | 說明 |
| --- | --- | --- |
| `--transport` | No | MCP 傳輸：`stdio`、`streamable-http`，或 `sse`。預設為 `stdio`。 |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### 常見範例

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 選項

| 選項 | 必需 | 說明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | 以空格分隔的語言代碼，或 `"all"`。 |
| `-r`, `--root-dir` | No | 專案根目錄。預設為當前目錄。 |
| `--image-dir` | No | 相對於根目錄的已翻譯圖片目錄。預設為 `translated_images`。 |
| `--dry-run` | No | 顯示將被更改的檔案但不寫入更新。 |
| `--fallback-to-original`, `--no-fallback-to-original` | No | 在翻譯後筆記本缺失時使用原始筆記本連結。預設為啟用。 |
| `-d`, `--debug` | No | 啟用除錯日誌。 |
| `-s`, `--save-logs` | No | 將 DEBUG 等級日誌儲存在 `<root-dir>/logs/` 底下。 |
| `-y`, `--yes` | No | 在處理所有語言時自動確認提示。 |

## Environment

All commands require one configured LLM provider:

```bash
# Azure 的 OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 或 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

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

Preview Markdown translation without writing files:

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