# Azure AI 設定

當您想要設定 Azure OpenAI 以進行文字翻譯，以及使用 Azure AI Vision 從圖像擷取文字時，請使用本指南。

## 先決條件

- 一個 Azure 訂閱。
- 可建立或使用 Azure AI 資源與模型部署的權限。
- Azure AI Foundry 的專案，或等同的對 Azure OpenAI 與 Azure AI Vision 資源的存取權。

## 建立 Azure AI 專案

1. 開啟 [Azure AI Foundry](https://ai.azure.com)。
2. 建立或選擇一個專案。
3. 為專案建立或選擇一個 AI 中心。
4. 建立後開啟專案概覽。

## 部署 Azure OpenAI 模型

1. 在專案中，開啟 **Models + endpoints**。
2. 選擇 **Deploy model**。
3. 選擇 GPT 模型，例如 `gpt-4o`。
4. 部署該模型。
5. 記下端點、部署名稱、模型名稱、API 金鑰與 API 版本。

!!! note
    Azure OpenAI 的 API 版本與 Azure AI Foundry 顯示的模型版本是分開的。請為您的部署選擇受支援的 API 版本。

## 設定 Azure AI Vision

圖像翻譯會先使用 Azure AI Vision 從來源影像中擷取文字，然後再翻譯該文字。

在您的 Azure AI 專案中，查找 Azure AI Services 的金鑰與端點。

![尋找 Azure AI 服務資訊](../../assets/find-azure-ai-info.png)

記錄：

- Azure AI 服務端點
- Azure AI 服務 API 金鑰

## 環境變數

將憑證新增到您的 `.env` 檔案或 CI secrets。

```bash
# Azure AI Vision，為影像翻譯所需
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI，為文字翻譯所需
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator 也支援可選的後備憑證組。複製完整的提供者組並加入後綴，例如 `_1` 或 `_2`；後備組中的所有變數必須使用相同的後綴。

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## 下一步

- 返回 [設定](configuration.md) 以設定本機或 CI 的環境變數。
- 使用 [CLI 參考](cli.md) 來執行翻譯指令。
- 使用 [GitHub Actions](github-actions.md) 自動化翻譯的拉取請求。