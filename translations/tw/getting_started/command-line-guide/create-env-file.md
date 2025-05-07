<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:02:26+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "tw"
}
-->
# 在根目錄建立 *.env* 檔案

在本教學中，我們將引導你如何使用 *.env* 檔案設定 Azure 服務的環境變數。環境變數讓你能安全地管理敏感憑證，例如 API 金鑰，而不需要將它們硬編碼在程式碼中。

> [!IMPORTANT]
> - 只需設定一個語言模型服務（Azure OpenAI 或 OpenAI）。請填寫你偏好的服務的環境變數。如果設定了多個語言模型的環境變數，co-op translator 將依優先順序選擇其中一個。
> - 如果未設定 Computer Vision 的環境變數，翻譯器會自動切換到 [僅 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要聚焦於 Azure 服務，但你也可以從 [supported models and services list](../README.md#-supported-models-and-services) 選擇任何支援的語言模型。

## 建立 *.env* 檔案

在專案的根目錄中，建立一個名為 *.env* 的檔案。此檔案將以簡單格式儲存所有環境變數。

> [!WARNING]
> 請勿將 *.env* 檔案提交到版本控制系統（如 Git）。請將 *.env* 加入你的 .gitignore 檔案，以避免不小心提交。

1. 進入專案的根目錄。

1. 在根目錄建立一個 *.env* 檔案。

1. 開啟 *.env* 檔案，並貼上以下範本：

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
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

> [!NOTE]
> 如果想查找你的 API 金鑰和端點，可以參考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤釋負責。