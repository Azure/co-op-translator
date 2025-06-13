<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:39:57+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "hk"
}
-->
# 喺根目錄建立 *.env* 檔案

喺呢個教學入面，我哋會教你點樣用 *.env* 檔案設定 Azure 服務嘅環境變數。環境變數可以幫你安全管理敏感嘅憑證，例如 API 金鑰，避免直接寫喺程式碼入面。

> [!IMPORTANT]
> - 只需要設定一個語言模型服務（Azure OpenAI 或 OpenAI）嘅環境變數。填寫你偏好嘅服務嘅環境變數。如果設定咗多個語言模型嘅環境變數，協同翻譯器會根據優先次序揀一個使用。
> - 如果冇設定 Computer Vision 嘅環境變數，翻譯器會自動切換去[只限 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 呢個指南主要係講 Azure 服務，但你都可以揀用[支援模型同服務清單](../README.md#-supported-models-and-services)入面嘅任何支援語言模型。

## 建立 *.env* 檔案

喺你嘅專案根目錄建立一個 *.env* 檔案。呢個檔案會用簡單嘅格式儲存你所有嘅環境變數。

> [!WARNING]
> 唔好將 *.env* 檔案提交到 Git 等版本控制系統。記得喺 .gitignore 入面加入 *.env*，防止誤提交。

1. 去到你專案嘅根目錄。

1. 喺根目錄建立一個 *.env* 檔案。

1. 開啟 *.env* 檔案，貼上以下範本：

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
> 如果想搵 API 金鑰同端點，可以參考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件以其母語版本為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司對因使用此翻譯而引起嘅任何誤解或誤釋概不負責。