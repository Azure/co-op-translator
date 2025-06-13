<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:39:35+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "zh"
}
-->
# 在根目录创建 *.env* 文件

在本教程中，我们将指导你如何使用 *.env* 文件设置 Azure 服务的环境变量。环境变量可以帮助你安全地管理敏感凭据，如 API 密钥，而无需将它们硬编码到代码中。

> [!IMPORTANT]
> - 只需配置一个语言模型服务（Azure OpenAI 或 OpenAI）。填写你偏好的服务的环境变量。如果同时设置了多个语言模型的环境变量，协同翻译器将根据优先级选择一个。
> - 如果未设置计算机视觉的环境变量，翻译器将自动切换到[仅 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要针对 Azure 服务，但你也可以从[支持的模型和服务列表](../README.md#-supported-models-and-services)中选择任何支持的语言模型。

## 创建 *.env* 文件

在项目的根目录下，创建一个名为 *.env* 的文件。该文件将以简单的格式存储所有环境变量。

> [!WARNING]
> 请勿将 *.env* 文件提交到 Git 等版本控制系统。请将 *.env* 添加到你的 .gitignore 文件中，以防止意外提交。

1. 进入项目的根目录。

1. 在根目录下创建一个 *.env* 文件。

1. 打开 *.env* 文件，粘贴以下模板：

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
> 如果你想查找 API 密钥和端点，可以参考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。