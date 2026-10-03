# 設定

Co-op Translator 需要一個語言模型提供者。圖像翻譯另外還需要 Azure AI Vision。

設定從環境變數讀取。對於本機專案，請將它們放在專案根目錄的 `.env` 檔案中。

有關 Azure 資源設定，請參閱 [Azure AI 設定](azure-ai-setup.md)。

## 本機執行環境設定

在本機執行 CLI 之前請使用虛擬環境。Co-op Translator 支援 Python 3.11 到 3.14。

一般 CLI 使用情況下，請在虛擬環境中安裝已發佈的套件：

### Windows（PowerShell）

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

對於儲存庫開發，請從專案根目錄安裝相依性：

```bash
poetry install
poetry run translate --help
```

在 CLI 可用之後，請在 `.env` 中設定一個語言模型提供者。

## 提供者選擇

工具會依照以下順序自動偵測提供者：

1. Azure OpenAI
2. OpenAI
3. Anthropic

翻譯需要提供者憑證，但像 `translate -l "ko" -md --dry-run` 的預覽例外。`migrate-links`、`co-op-review` 和 `run_review` 是確定性的維護操作，且不需要提供者憑證。

## 模型客戶端後端

從 Co-op Translator 0.22.0 開始，Azure OpenAI、OpenAI 與 Anthropic 預設使用 Microsoft Agent Framework。一般使用不需要設定後端。

為了相容性，Semantic Kernel 暫時仍可使用。若要明確選擇它，請設定：

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

使用 Semantic Kernel 會顯示棄用警告。此套件計畫在 0.23.0 將 Semantic Kernel 變為選用相依，並在 0.24.0 移除該整合，視相容性結果與使用者回饋而定。Anthropic 需要 `agent-framework`；在 Anthropic 下明確選擇 `semantic-kernel` 會導致設定錯誤。無效的值會在以提供者為後端的翻譯器初始化時失敗，而不會靜默回退。請追蹤發佈進度並在 [GitHub 議題 #543](https://github.com/Azure/co-op-translator/issues/543) 回報阻礙。

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

若直接呼叫 OpenAI API，請使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` 是必需的，因為翻譯器在進行 API 呼叫時需要一個明確的 chat 模型。

預設設定下請不要設定 `OPENAI_ORG_ID` 與 `OPENAI_BASE_URL`。只有在帳戶需要組織 ID 時才新增 `OPENAI_ORG_ID`，或只有在使用自訂端點時才設定 `OPENAI_BASE_URL`。不要套用可選設定的佔位值。

## Anthropic Claude

若直接呼叫 Claude API，請使用 Anthropic。建立一個 [Anthropic API 金鑰](https://platform.claude.com/docs/en/get-started)，並選擇受支援的 [Claude 模型 ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)。

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` 和 `ANTHROPIC_MODEL` 為必填。您不需要設定 `CO_OP_TRANSLATOR_MODEL_CLIENT`；Agent Framework 為預設後端。

對 Anthropic API，請將 `ANTHROPIC_BASE_URL` 保持未設定。只有在使用自訂端點時才設定它。

`ANTHROPIC_MAX_TOKENS` 預設為 `8192`，可為像 Meitei Mayek 這類 token 密集的文字保留空間。如果您的模型或相容的 Anthropic 端點將輸出上限設得比這個低，請降低它。

## Azure AI Vision

圖像翻譯需要 Azure AI Vision，讓工具在設定的語言模型翻譯之前能從影像中擷取文字。Anthropic 能像 Azure OpenAI 或 OpenAI 一樣翻譯擷取出的文字。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果以 `-img`、`images=True` 或未指定內容類型過濾器來選擇圖像翻譯，工具會在翻譯開始前驗證 Vision 的設定。

## 多組憑證設定

設定層支援透過在變數名稱後加上相同索引來使用多組憑證：

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

每一組都必須完整。健康檢查會在翻譯進行前選擇一組可用的憑證。

OpenAI 與 Anthropic 支援相同的後綴慣例。請將憑證集合中的每個變數都放在相同的後綴上，包括像 `OPENAI_BASE_URL_1` 或 `ANTHROPIC_BASE_URL_1` 這類的選用值。

## 指令需求

| 指令或 API | 需要 LLM | 需要 Vision | 備註 |
| --- | --- | --- | --- |
| `translate -md` | 是 | 否 | 僅翻譯 Markdown。 |
| `translate -nb` | 是 | 否 | 僅翻譯筆記本。 |
| `translate -img` | 是 | 是 | 僅翻譯圖像。 |
| `translate` 未帶類型旗標 | 是 | 是 | 預設模式包含 Markdown、筆記本和圖像。 |
| `evaluate` | 是 | 否 | 使用 LLM 評估，除非選擇 `--fast`。 |
| `migrate-links` | 否 | 否 | 在不呼叫提供者的情況下執行本機連結遷移。 |
| `co-op-review` | 否 | 否 | 執行確定性的翻譯結構、新鮮度、Markdown、筆記本與本機連結檢查。 |
| `run_translation(markdown=True)` | 是 | 否 | 程式化的 Markdown 翻譯。 |
| `run_translation(images=True)` | 是 | 是 | 程式化的圖像翻譯。 |
| `run_review(...)` | 否 | 否 | 程式化的確定性審查。 |

## 輸出目錄

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API 可以使用 `translations_dir` 和 `image_dir` 覆寫這些目錄。
