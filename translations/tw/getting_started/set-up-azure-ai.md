<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:18:31+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "tw"
}
-->
# 設定 Azure AI 以支援合作翻譯器 (Azure OpenAI 與 Azure AI Vision)

本指南將帶你完成在 Azure AI Foundry 中設定 Azure OpenAI 進行語言翻譯，以及 Azure Computer Vision 用於影像內容分析（進而用於影像翻譯）。

**前置條件：**
- 擁有有效訂閱的 Azure 帳號。
- 有足夠權限在 Azure 訂閱中建立資源與部署。

## 建立 Azure AI 專案

你將從建立一個 Azure AI 專案開始，這是管理 AI 資源的集中平台。

1. 前往 [https://ai.azure.com](https://ai.azure.com) 並使用你的 Azure 帳號登入。

1. 選擇 **+Create** 來建立新專案。

1. 執行以下操作：
   - 輸入 **Project name**（例如 `CoopTranslator-Project`）。
   - 選擇 **AI hub**（例如 `CoopTranslator-Hub`）（如有需要可建立新的）。

1. 點選「**Review and Create**」以建立專案，系統會帶你到專案總覽頁面。

## 設定 Azure OpenAI 用於語言翻譯

在專案中，你將部署一個 Azure OpenAI 模型，作為文字翻譯的後端。

### 前往你的專案

若尚未進入，請打開你剛建立的專案（例如 `CoopTranslator-Project`）於 Azure AI Foundry。

### 部署 OpenAI 模型

1. 在專案左側選單「My assets」底下，選擇「**Models + endpoints**」。

1. 點選 **+ Deploy model**。

1. 選擇 **Deploy Base Model**。

1. 系統會顯示可用模型清單，篩選或搜尋合適的 GPT 模型，我們推薦 `gpt-4o`。

1. 選擇你想要的模型後，點選 **Confirm**。

1. 點選 **Deploy**。

### Azure OpenAI 設定

部署完成後，你可以在「**Models + endpoints**」頁面選擇該部署，查看其 **REST endpoint URL**、**Key**、**Deployment name**、**Model name** 及 **API version**。這些資訊將用於整合翻譯模型到你的應用程式。

## 設定 Azure Computer Vision 用於影像翻譯

要啟用影像中文字的翻譯，你需要取得 Azure AI Service 的 API Key 與 Endpoint。

1. 前往你的 Azure AI 專案（例如 `CoopTranslator-Project`），確認你在專案總覽頁面。

### Azure AI Service 設定

從 Azure AI Service 中找到 API Key 與 Endpoint。

1. 前往你的 Azure AI 專案（例如 `CoopTranslator-Project`），確認你在專案總覽頁面。

1. 從 Azure AI Service 分頁找到 **API Key** 與 **Endpoint**。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

此連結讓你連結的 Azure AI Services 資源（包含影像分析）功能可用於你的 AI Foundry 專案，之後你可以在筆記本或應用程式中使用這個連結來擷取影像中文字，再送至 Azure OpenAI 模型進行翻譯。

## 整合你的認證資訊

到目前為止，你應該已收集到以下資訊：

**Azure OpenAI（文字翻譯）:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name（例如 `gpt-4o`）
- Azure OpenAI Deployment Name（例如 `cooptranslator-gpt4o`）
- Azure OpenAI API Version

**Azure AI Services（透過 Vision 擷取影像文字）:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### 範例：環境變數設定（預覽）

之後在建置應用程式時，通常會使用這些認證資訊設定環境變數，例如：

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### 延伸閱讀

- [如何在 Azure AI Foundry 建立專案](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [如何建立 Azure AI 資源](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [如何在 Azure AI Foundry 部署 OpenAI 模型](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤譯負責。