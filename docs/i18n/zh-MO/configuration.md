# 設定

Co-op Translator 需要一個語言模型提供者。圖像翻譯另外需要 Azure AI Vision。

設定會從環境變數讀取。對於本地專案，請將它們放在專案根目錄的 `.env` 檔案中。

如需 Azure 資源設定，請參閱 [Azure AI 設定](azure-ai-setup.md)。

## 本地執行環境設定

在本地執行 CLI 之前，請先使用虛擬環境。Co-op Translator 支援 Python 3.10 到 3.12。

若為一般 CLI 使用，請在虛擬環境內安裝已發佈的套件：

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

在 CLI 可用之後，請在 `.env` 中設定一個語言模型提供者。

## Provider selection

工具會以以下順序自動偵測提供者：

1. Azure OpenAI
2. OpenAI

如果兩者皆未設定，`translate`、`evaluate`、`migrate-links` 與 `run_translation` 將在設定檢查期間失敗。`co-op-review` 與 `run_review` 為確定性維護檢查，不需要提供者憑證。

## Azure OpenAI

當您的模型部署在 Azure AI Foundry 或 Azure OpenAI Service 時，請使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

連線性檢查會在翻譯開始前使用端點、API 金鑰、API 版本與部署名稱進行驗證。

## OpenAI

當直接呼叫 OpenAI API 時，請使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # 可選的
OPENAI_BASE_URL="..."        # 可選的
```

`OPENAI_CHAT_MODEL_ID` 為必要欄位，因為翻譯器需要一個明確的 chat model 來進行 API 呼叫。

## Azure AI Vision

圖像翻譯需要 Azure AI Vision，工具才能在翻譯前從圖像中擷取文字。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果使用 `-img`、`images=True` 或未指定內容類型過濾器而選擇圖像翻譯，工具會在翻譯開始前驗證 Vision 的設定。

## Multiple credential sets

設定層支援透過在變數後加上相同索引來使用多組憑證：

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

每一組必須完整。健康檢查會在翻譯繼續之前選擇一組可用的憑證。

## Command requirements

| 命令或 API | 是否需要 LLM | 是否需要 Vision | 備註 |
| --- | --- | --- | --- |
| `translate -md` | 是 | 否 | 僅翻譯 Markdown。 |
| `translate -nb` | 是 | 否 | 僅翻譯筆記本。 |
| `translate -img` | 是 | 是 | 僅翻譯圖片。 |
| `translate` with no type flags | 是 | 是 | 預設模式包含 Markdown、筆記本與圖片。 |
| `evaluate` | 是 | 否 | 使用 LLM 評估，除非選取 `--fast`。 |
| `migrate-links` | 是 | 否 | 執行連結遷移，但仍會執行共用的設定檢查。 |
| `co-op-review` | 否 | 否 | 執行確定性的翻譯結構、時效性、Markdown、筆記本與本地連結檢查。 |
| `run_translation(markdown=True)` | 是 | 否 | 以程式方式進行 Markdown 翻譯。 |
| `run_translation(images=True)` | 是 | 是 | 以程式方式進行圖片翻譯。 |
| `run_review(...)` | 否 | 否 | 以程式方式執行確定性檢查。 |

## Output directories

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

The Python API can override these directories with `translations_dir` and `image_dir`.