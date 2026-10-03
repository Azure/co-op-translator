# 設定

Co-op Translator 需要一個語言模型提供者。圖像翻譯另外需要 Azure AI Vision。

設定會從環境變數讀取。對於本地專案，請將它們放在專案根目錄的 `.env` 檔案中。

有關 Azure 資源設定，請參閱 [Azure AI 設定](azure-ai-setup.md)。

## 本機執行環境設定

在本機執行 CLI 之前，請先使用虛擬環境。Co-op Translator 支援 Python 3.11 到 3.14。

對於一般的 CLI 使用，請在虛擬環境內安裝已發佈的套件：

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

對於儲存庫開發，請改從專案根目錄安裝相依套件：

```bash
poetry install
poetry run translate --help
```

當 CLI 可用後，請在 `.env` 中設定一個語言模型提供者。

## 提供者選擇

工具會依照下列順序自動偵測提供者：

1. Azure OpenAI
2. OpenAI
3. Anthropic

翻譯需要提供者憑證，但預覽情況（例如 `translate -l "ko" -md --dry-run`）除外。`migrate-links`、`co-op-review` 和 `run_review` 是決定性維護操作，不需要提供者憑證。

## 模型用戶端後端

從 Co-op Translator 0.22.0 開始，Azure OpenAI、OpenAI 和 Anthropic 預設使用 Microsoft Agent Framework。一般使用不需要設定後端。

Semantic Kernel 仍暫時保留以維持相容性。若要明確選擇它，請設定：

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

使用 Semantic Kernel 會發出棄用警告。計劃在 0.23.0 將 Semantic Kernel 移為可選相依套件，並在 0.24.0 移除該整合，具體取決於相容性結果與使用者回饋。Anthropic 需要 `agent-framework`；在 Anthropic 上明確選擇 `semantic-kernel` 會導致設定錯誤。無效的值會在有提供者支援的翻譯器初始化期間失敗，而不是靜默回退。請在 [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) 追蹤部署情況並回報阻礙因素。

## Azure OpenAI

當您的模型部署在 Azure AI Foundry 或 Azure OpenAI Service 時，請使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

在開始翻譯之前，連線檢查會使用 endpoint、API key、API version 與 deployment 名稱。

## OpenAI

當直接呼叫 OpenAI API 時，請使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` 為必填，因為翻譯器在進行 API 呼叫時需要明確的 chat 模型。

對於預設設定，請不要設定 `OPENAI_ORG_ID` 與 `OPENAI_BASE_URL`。只有在您的帳戶需要時才新增組織 ID，只有在使用自訂端點時才設定 base URL。不要為可選設定複製範例或佔位值。

## Anthropic Claude

當直接呼叫 Claude API 時，請使用 Anthropic。建立一個 [Anthropic API 金鑰](https://platform.claude.com/docs/en/get-started)，並選擇受支援的 [Claude 模型 ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)。

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` 和 `ANTHROPIC_MODEL` 為必填。您不需要設定 `CO_OP_TRANSLATOR_MODEL_CLIENT`；Agent Framework 是預設後端。

對於 Anthropic API，請不要設定 `ANTHROPIC_BASE_URL`。只有在使用自訂端點時才設定它。

`ANTHROPIC_MAX_TOKENS` 預設為 `8192`，足以容納像 Meitei Mayek 這類高 token 密度的腳本。如果您的模型或相容 Anthropic 的端點將輸出限制在此以下，請將其調低。

## Azure AI Vision

圖像翻譯需要 Azure AI Vision，使工具能在設定的語言模型翻譯之前從圖像中擷取文字。Anthropic 可以像 Azure OpenAI 或 OpenAI 一樣翻譯擷取出來的文字。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果以 `-img`、`images=True` 或沒有內容類型過濾器選擇圖像翻譯，工具會在開始翻譯前驗證 Vision 的設定。

## 多組憑證

設定層支援透過在變數後加相同索引來使用多組憑證：

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

每一組必須完整。健康檢查會在翻譯繼續之前選擇一組可用的組合。

OpenAI 與 Anthropic 支援相同的後綴慣例。請在同一後綴中保留憑證組的所有變數，包括像 `OPENAI_BASE_URL_1` 或 `ANTHROPIC_BASE_URL_1` 這樣的可選值。

## 指令需求

| 指令或 API | 需要 LLM | 需要 Vision | 說明 |
| --- | --- | --- | --- |
| `translate -md` | 是 | 否 | 僅翻譯 Markdown。 |
| `translate -nb` | 是 | 否 | 僅翻譯筆記本。 |
| `translate -img` | 是 | 是 | 僅翻譯圖像。 |
| `translate` 在未指定類型旗標時 | 是 | 是 | 預設模式包含 Markdown、筆記本和圖像。 |
| `evaluate` | 是 | 否 | 使用 LLM 評估，除非選擇 `--fast`。 |
| `migrate-links` | 否 | 否 | 執行本機連結遷移，不會呼叫提供者。 |
| `co-op-review` | 否 | 否 | 執行決定性的翻譯結構、新鮮度、Markdown、筆記本與本機連結檢查。 |
| `run_translation(markdown=True)` | 是 | 否 | 程式化的 Markdown 翻譯。 |
| `run_translation(images=True)` | 是 | 是 | 程式化的圖像翻譯。 |
| `run_review(...)` | 否 | 否 | 程式化的決定性審查。 |

## 輸出目錄

預設文字翻譯輸出：

```text
translations/<language-code>/<source-relative-path>
```

預設翻譯後的圖像輸出：

```text
translated_images/<language-code>/<source-relative-path>
```

Python API 可以用 `translations_dir` 和 `image_dir` 覆寫這些目錄。