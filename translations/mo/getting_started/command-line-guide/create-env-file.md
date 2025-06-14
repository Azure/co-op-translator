<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-14T12:50:19+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "mo"
}
-->
# 在根目錄創建 *.env* 文件

在本教程中，我們將指導您使用 *.env* 文件為 Azure 服務設置環境變量。環境變量允許您安全地管理敏感憑證，例如 API 密鑰，而不必將它們硬編碼到您的代碼庫中。

> [!IMPORTANT]
> - 只需配置一個語言模型服務（Azure OpenAI 或 OpenAI）。填寫您首選服務的環境變量。如果設置了多個語言模型的環境變量，合作翻譯器將根據優先級選擇一個。
> - 如果未設置計算機視覺環境變量，翻譯器將自動切換到[僅 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要關注 Azure 服務，但您可以從[支持的模型和服務列表](../README.md#-supported-models-and-services)中選擇任何支持的語言模型。

## 創建 *.env* 文件

在您的項目的根目錄中，創建一個名為 *.env* 的文件。此文件將以簡單的格式存儲所有環境變量。

> [!WARNING]
> 不要將您的 *.env* 文件提交到像 Git 這樣的版本控制系統。將 *.env* 添加到您的 .gitignore 文件中以防止意外提交。

1. 導航到您的項目的根目錄。

1. 在項目的根目錄中創建 *.env* 文件。

1. 打開 *.env* 文件並粘貼以下模板：

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
> 如果您想查找您的 API 密鑰和端點，可以參考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

**免責聲明**：  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議使用專業的人力翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。