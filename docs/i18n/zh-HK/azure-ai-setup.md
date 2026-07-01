# Azure AI 設定

當您想要設定 Azure OpenAI 以進行文字翻譯，以及使用 Azure AI Vision 以擷取圖片文字時，請使用本指南。

## 先決條件

- 一個 Azure 訂閱。
- 具備建立或使用 Azure AI 資源與模型部署的權限。
- 在 Azure AI Foundry 中的一個專案或等同的 Azure OpenAI 與 Azure AI Vision 存取權。

## 建立 Azure AI 專案

1. 開啟 [Azure AI Foundry](https://ai.azure.com).
2. 建立或選擇一個專案。
3. 為該專案建立或選擇一個 AI 中心。
4. 建立後開啟專案概覽。

## 部署 Azure OpenAI 模型

1. 在專案中，開啟 **Models + endpoints**。
2. 選取 **Deploy model**。
3. 選擇一個 GPT 模型，例如 `gpt-4o`。
4. 部署該模型。
5. 記錄端點、部署名稱、模型名稱、API 金鑰與 API 版本。

!!! note
    Azure OpenAI API 版本與 Azure AI Foundry 中顯示的模型版本是分開的。請為您的部署選擇受支援的 API 版本。

## 設定 Azure AI Vision

圖片翻譯會先使用 Azure AI Vision 從原始圖片擷取文字，然後再翻譯該文字。

在您的 Azure AI 專案中，找到 Azure AI Services 的金鑰與端點。

![尋找 Azure AI 服務資訊](../../assets/find-azure-ai-info.png)

記錄：

- Azure AI 服務端點
- Azure AI 服務 API 金鑰

## 環境變數

將認證加入到您的 `.env` 檔案或 CI 機密。

```bash
# 需要 Azure AI Vision 才能進行圖像翻譯
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# 需要 Azure OpenAI 才能進行文字翻譯
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator also supports optional fallback credential sets. Duplicate a complete provider set with suffixes such as `_1` or `_2`; all variables in a fallback set must share the same suffix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## 下一步

- 返回 [設定](configuration.md) 以設定本地或 CI 的環境變數。
- 使用 [CLI 參考](cli.md) 取得翻譯指令。
- 使用 [GitHub Actions](github-actions.md) 自動化翻譯的拉取請求。