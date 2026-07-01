# 設定

Co-op Translator 需要一個語言模型提供者。圖像翻譯另外需要 Azure AI Vision。

設定從環境變數讀取。對於本機專案，將它們放在專案根目錄的 `.env` 檔案中。

有關 Azure 資源設定，請參閱 [Azure AI 設定](azure-ai-setup.md)。

## 本地執行環境設定

在本地執行 CLI 之前請使用虛擬環境。Co-op Translator 支援 Python 3.10 至 3.12。

一般 CLI 使用情況下，請在虛擬環境中安裝已發佈的套件：

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

若為原始碼庫開發，請改從專案根目錄安裝相依套件：

```bash
poetry install
poetry run translate --help
```

在 CLI 可用之後，於 `.env` 中配置一個語言模型提供者。

## 提供者選擇

工具會依下列順序自動偵測提供者：

1. Azure OpenAI
2. OpenAI

如果兩者皆未設定，`translate`、`evaluate`、`migrate-links` 與 `run_translation` 會在設定檢查階段失敗。`co-op-review` 與 `run_review` 是決定性維護檢查，且不需要提供者憑證。

## Azure OpenAI

當您的模型部署在 Azure AI Foundry 或 Azure OpenAI Service 時，請使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

連線檢查會在翻譯開始前使用 endpoint、API key、API version 與 deployment name。

## OpenAI

當直接呼叫 OpenAI API 時，請使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # 可選
OPENAI_BASE_URL="..."        # 可選
```

`OPENAI_CHAT_MODEL_ID` 是必需的，因為翻譯器需要明確的聊天模型來進行 API 呼叫。

## Azure AI Vision

圖像翻譯需要 Azure AI Vision，這樣工具才能在翻譯前從圖像中擷取文字。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果使用 `-img`、`images=True` 選擇圖像翻譯，或沒有內容類型篩選，工具會在翻譯開始前驗證 Vision 的設定。

## 多組認證

設定層支援多組認證，方法是為變數加上相同的索引後綴：

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

每組必須完整。健康檢查會在翻譯進行前選擇一組可用的認證。

## 指令需求

| 指令或 API | 是否需要 LLM | 是否需要 Vision | 備註 |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | 僅翻譯 Markdown。 |
| `translate -nb` | Yes | No | 僅翻譯筆記本。 |
| `translate -img` | Yes | Yes | 僅翻譯圖像。 |
| `translate` with no type flags | Yes | Yes | 預設模式包含 Markdown、筆記本與圖像。 |
| `evaluate` | Yes | No | 使用 LLM 評估，除非選取 `--fast`。 |
| `migrate-links` | Yes | No | 執行連結遷移，但仍會執行共用的設定檢查。 |
| `co-op-review` | No | No | 執行決定性的翻譯結構、新鮮度、Markdown、筆記本與本機連結檢查。 |
| `run_translation(markdown=True)` | Yes | No | 以程式方式執行的 Markdown 翻譯。 |
| `run_translation(images=True)` | Yes | Yes | 以程式方式執行的圖像翻譯。 |
| `run_review(...)` | No | No | 以程式方式執行的決定性審查。 |

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