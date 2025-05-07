<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:54:00+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "tw"
}
-->
# 在根目錄建立 *.env* 檔案

在本教學中，我們將指導你如何使用 *.env* 檔案設定 Azure 服務的環境變數。環境變數讓你能夠安全地管理敏感的憑證，例如 API 金鑰，而不需要將它們硬編碼在程式碼中。

> [!IMPORTANT]
> - 只需設定一個語言模型服務（Azure OpenAI 或 OpenAI）。請填寫你偏好的服務的環境變數。如果同時設定多個語言模型的環境變數，協同翻譯器將會根據優先順序選擇其中一個。
> - 若未設定 Computer Vision 的環境變數，翻譯器會自動切換到[僅 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要聚焦於 Azure 服務，但你也可以從[支援的模型與服務清單](../README.md#-supported-models-and-services)中選擇任何支援的語言模型。

## 建立 *.env* 檔案

在專案的根目錄下，建立一個名為 *.env* 的檔案。此檔案將以簡單的格式儲存所有環境變數。

> [!WARNING]
> 請勿將 *.env* 檔案提交至版本控制系統（例如 Git）。請將 *.env* 加入你的 .gitignore 檔案，以避免不小心提交。

1. 移動到專案的根目錄。

1. 在專案根目錄建立一個 *.env* 檔案。

    ![建立 *.env* 檔案。](../../../../imgs/create-env.png)

1. 開啟 *.env* 檔案並貼上以下範本：

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

## 準備你的 Azure 憑證

你需要準備以下 Azure 憑證來設定環境：

你可以在 [AI Foundry](https://ai.azure.com/build/overview) 的專案總覽頁面取得所有相關資訊。

![Foundry-overview](../../../../imgs/foundry-overview.png)

### Azure AI 服務：

    - Azure Subscription Key：你的 Azure AI 服務 API 金鑰，用來存取 Azure AI 服務。
    - Azure AI Service Endpoint：你所使用的 Azure AI 服務端點 URL。

### Azure OpenAI 服務：

    - Azure OpenAI API Key：用來存取 Azure OpenAI 服務的 API 金鑰。
    - Azure OpenAI Endpoint：你的 Azure OpenAI 服務端點 URL。

1. 將你的 AI 服務金鑰與端點複製並貼到 *.env* 檔案中。
2. 將你的 Azure OpenAI API 金鑰與端點複製並貼到 *.env* 檔案中。

### 模型詳細資訊

從左側選單選擇 Model 和 Endpoints

![FoundryModels](../../../../imgs/gpt-models.png)

接著選擇你想使用的模型，以取得模型詳細資訊

![ModelDetails](../../../../imgs/model-deployment-name.png)

在 .env 檔案中需要以下資訊：

    - Azure OpenAI Model Name：你將互動的模型名稱。
    - Azure OpenAI Name：你為 Azure OpenAI 模型部署所設定的名稱。
    - Azure OpenAI API Version：你使用的 Azure OpenAI API 版本，可從 URL 字串末端找到。

取得這些資訊，請選擇模型部署

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### 新增 Azure 環境變數

3. 將你的 Azure OpenAI **Name** 與模型 **Version** 複製並貼到 *.env* 檔案中。
4. 儲存 *.env* 檔案。
5. 現在，你可以存取這些環境變數，並使用 **Co-op Translator** 搭配你的 Azure 服務。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。