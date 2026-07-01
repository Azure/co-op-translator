# 設定

Co-op Translator 需要至少一個語言模型供應者。圖片翻譯另外亦需要 Azure AI Vision。

設定從環境變數讀取。對於本地專案，請將它們放在專案根目錄的 `.env` 檔案中。

有關 Azure 資源的設定，請參閱 [Azure AI 設定](azure-ai-setup.md)。

## 本地執行環境設定

在本地執行 CLI 前請先使用虛擬環境。Co-op Translator 支援 Python 3.10 到 3.12。

一般使用 CLI 時，請在虛擬環境內安裝已發佈的套件：

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

For repository development, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

當 CLI 可用後，請在 `.env` 中配置一個語言模型供應者。

## 供應者選擇

工具會按以下順序自動偵測供應者：

1. Azure OpenAI
2. OpenAI

如果未設定任何供應者，`translate`、`evaluate`、`migrate-links` 和 `run_translation` 在設定檢查時會失敗。`co-op-review` 和 `run_review` 則是決定性的維護檢查，無需供應者憑證。

## Azure OpenAI

當您的模型部署於 Azure AI Foundry 或 Azure OpenAI Service 時，請使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

在開始翻譯前，連線檢查會使用 endpoint、API key、API version 和 deployment name。

## OpenAI

直接呼叫 OpenAI API 時請使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # 可選
OPENAI_BASE_URL="..."        # 可選
```

`OPENAI_CHAT_MODEL_ID` 是必需的，因為翻譯工具在 API 呼叫時需要指定明確的 chat 模型。

## Azure AI Vision

圖片翻譯需要 Azure AI Vision，以便工具在翻譯前從影像中擷取文字。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果使用 `-img`、`images=True`，或沒有內容類型過濾而選擇圖片翻譯，工具會在翻譯開始前驗證 Vision 的設定。

## 多組憑證

設定層支持多組憑證，方法是對變數加上相同的索引後綴：

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

每組憑證必須完整。健康檢查會在翻譯繼續前選擇一組可用的憑證。

## 指令需求

| Command 或 API | 需要 LLM | 需要 Vision | 備註 |
| --- | --- | --- | --- |
| `translate -md` | 是 | 否 | 只翻譯 Markdown。 |
| `translate -nb` | 是 | 否 | 只翻譯 筆記本。 |
| `translate -img` | 是 | 是 | 只翻譯圖片。 |
| `translate` with no type flags | 是 | 是 | 預設模式包含 Markdown、筆記本和圖片。 |
| `evaluate` | 是 | 否 | 使用 LLM 評估，除非選擇了 `--fast`。 |
| `migrate-links` | Yes | No | 執行連結遷移，但仍會執行共用的設定檢查。 |
| `co-op-review` | No | No | 執行決定性的翻譯結構、新鮮度、Markdown、筆記本及本地連結檢查。 |
| `run_translation(markdown=True)` | 是 | 否 | 程式化的 Markdown 翻譯。 |
| `run_translation(images=True)` | 是 | 是 | 程式化的圖片翻譯。 |
| `run_review(...)` | 否 | 否 | 程式化的決定性檢查。 |

## 輸出目錄

預設文字翻譯輸出：

```text
translations/<language-code>/<source-relative-path>
```

預設翻譯後圖片輸出：

```text
translated_images/<language-code>/<source-relative-path>
```

Python API 可以使用 `translations_dir` 和 `image_dir` 覆蓋這些目錄。