# 設定

Co-op Translator 需要一個語言模型提供者。圖像翻譯還需要 Azure AI Vision。

設定從環境變數讀取。對於本地專案，請將它們放在專案根目錄的 `.env` 檔案中。

有關 Azure 資源的設定，請參閱 [Azure AI 設定](azure-ai-setup.md).

## 本地執行環境設定

在本地執行 CLI 前，請使用虛擬環境。Co-op Translator 支援 Python 3.11 到 3.14。

一般 CLI 使用情況下，請在虛擬環境內安裝已發佈的套件：

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### 儲存庫開發

對於儲存庫開發，請從專案根目錄安裝相依套件：

```bash
poetry install
poetry run translate --help
```

在 CLI 可用之後，於 `.env` 中設定一個語言模型提供者。

## 提供者選擇

工具會按以下順序自動偵測提供者：

1. Azure OpenAI
2. OpenAI
3. Anthropic

翻譯需要提供者憑證，但像 `translate -l "ko" -md --dry-run` 這類預覽除外。`migrate-links`、`co-op-review` 和 `run_review` 是確定性的維護操作，無需提供者憑證。

## 模型客戶端後端

從 Co-op Translator 0.22.0 開始，Azure OpenAI、OpenAI 與 Anthropic 預設使用 Microsoft Agent Framework。一般使用不需要設定後端。

Semantic Kernel 暫時仍可用以維持相容性。要明確選擇它，設定：

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

使用 Semantic Kernel 會發出棄用警告。計劃在 0.23.0 將 Semantic Kernel 移為可選相依套件，並在 0.24.0 移除整合（視相容性結果與使用者反饋而定）。Anthropic 需要 `agent-framework`；若與 Anthropic 一起明確選擇 `semantic-kernel`，會因設定錯誤而失敗。無效值在以提供者為後端的翻譯器初始化期間會失敗，而不是默默回退。請在 [GitHub 問題 #543](https://github.com/Azure/co-op-translator/issues/543) 追蹤推出進度並回報阻礙事項。

## Azure OpenAI

當您的模型部署在 Azure AI Foundry 或 Azure OpenAI Service 時，請使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

連線檢查會在翻譯開始前使用端點、API 金鑰、API 版本和部署名稱。

## OpenAI

直接呼叫 OpenAI API 時，請使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` 為必要項，因為翻譯器在進行 API 呼叫時需要明確的聊天模型。

預設設定下請不要設定 `OPENAI_ORG_ID` 與 `OPENAI_BASE_URL`。只有當您的帳戶需要組織 ID 時才加入，或只有在使用自訂端點時才設定 base URL。請勿將替代用的範例值複製到可選設定。

## Anthropic Claude

直接呼叫 Claude API 時，請使用 Anthropic。建立一個 [Anthropic API 金鑰](https://platform.claude.com/docs/en/get-started)，並選擇支援的 [Claude 模型 ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)。

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` 與 `ANTHROPIC_MODEL` 為必要項。您不需設定 `CO_OP_TRANSLATOR_MODEL_CLIENT`；Agent Framework 為預設後端。

對於 Anthropic API，請不要設定 `ANTHROPIC_BASE_URL`。只有在使用自訂端點時才設定它。

`ANTHROPIC_MAX_TOKENS` 預設為 `8192`，可為像 Meitei Mayek 這類 token 密集的文字留出空間。如果您的模型或相容 Anthropic 的端點將輸出上限設定在此值以下，請將其調低。

## Azure AI Vision

圖像翻譯需要 Azure AI Vision，以便工具在設定的語言模型翻譯之前先從圖片中擷取文字。Anthropic 可以像 Azure OpenAI 或 OpenAI 一樣翻譯擷取出的文字。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果選擇 `-img`、`images=True` 或沒有內容類型過濾器來執行圖像翻譯，工具會在翻譯開始前驗證 Vision 的設定。

## 多組憑證集

設定層支援透過在變數後加上相同索引來維護多組憑證集：

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

每組憑證必須完整。健康檢查會在翻譯進行前選擇一組可用的憑證。

OpenAI 與 Anthropic 支援相同的後綴慣例。請在同一後綴下保留憑證集中每個變數，包括可選值（例如 `OPENAI_BASE_URL_1` 或 `ANTHROPIC_BASE_URL_1`）。

## 指令需求

| 指令或 API | 需要 LLM | 需要 Vision | 備註 |
| --- | --- | --- | --- |
| `translate -md` | 是 | 否 | 僅翻譯 Markdown。 |
| `translate -nb` | 是 | 否 | 僅翻譯筆記本。 |
| `translate -img` | 是 | 是 | 僅翻譯圖像。 |
| `translate` (不帶類型旗標) | 是 | 是 | 預設模式包含 Markdown、筆記本和圖像。 |
| `evaluate` | 是 | 否 | 使用 LLM 評估，除非選擇了 `--fast`。 |
| `migrate-links` | 否 | 否 | 在不呼叫提供者的情況下執行本地連結遷移。 |
| `co-op-review` | 否 | 否 | 執行確定性的翻譯結構、新鮮度、Markdown、筆記本及本地連結檢查。 |
| `run_translation(markdown=True)` | 是 | 否 | 以程式方式執行 Markdown 翻譯。 |
| `run_translation(images=True)` | 是 | 是 | 以程式方式執行圖像翻譯。 |
| `run_review(...)` | 否 | 否 | 以程式方式執行確定性檢閱。 |

## 輸出目錄

預設文字翻譯輸出：

```text
translations/<language-code>/<source-relative-path>
```

預設翻譯後圖像輸出：

```text
translated_images/<language-code>/<source-relative-path>
```

Python API 可以使用 `translations_dir` 與 `image_dir` 覆寫這些目錄。