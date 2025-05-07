<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:53:49+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "zh"
}
-->
# 在根目录创建 *.env* 文件

在本教程中，我们将指导你如何使用 *.env* 文件设置 Azure 服务的环境变量。环境变量可以让你安全地管理敏感凭据，例如 API 密钥，而无需将它们硬编码在代码中。

> [!IMPORTANT]
> - 只需配置一个语言模型服务（Azure OpenAI 或 OpenAI）。填写你偏好的服务的环境变量。如果设置了多个语言模型的环境变量，协同翻译器将根据优先级选择其中一个。
> - 如果未设置计算机视觉的环境变量，翻译器将自动切换到[仅 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要针对 Azure 服务，但你也可以从[支持的模型和服务列表](../README.md#-supported-models-and-services)中选择任何支持的语言模型。

## 创建 *.env* 文件

在项目的根目录下，创建一个名为 *.env* 的文件。此文件将以简单的格式存储所有环境变量。

> [!WARNING]
> 不要将你的 *.env* 文件提交到版本控制系统（如 Git）。请将 *.env* 添加到你的 .gitignore 文件中，以防止意外提交。

1. 进入你的项目根目录。

1. 在项目根目录创建一个 *.env* 文件。

    ![创建 *.env* 文件](../../../../imgs/create-env.png)

1. 打开 *.env* 文件，粘贴以下模板：

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

## 收集你的 Azure 凭据

你需要准备以下 Azure 凭据来配置环境：

你可以在 [AI Foundry](https://ai.azure.com/build/overview) 的项目概览页面获取所有详细信息。

![Foundry-overview](../../../../imgs/foundry-overview.png)

### 对于 Azure AI 服务：

- Azure 订阅密钥：你的 Azure AI 服务 API 密钥，用于访问 Azure AI 服务。
- Azure AI 服务终结点：你特定 Azure AI 服务的终结点 URL。

### 对于 Azure OpenAI 服务：

- Azure OpenAI API 密钥：访问 Azure OpenAI 服务的 API 密钥。
- Azure OpenAI 终结点：你的 Azure OpenAI 服务的终结点 URL。

1. 将你的 AI 服务密钥和终结点复制粘贴到 *.env* 文件中。
2. 将你的 Azure OpenAI API 密钥和终结点复制粘贴到 *.env* 文件中。

### 模型详情

从左侧菜单选择模型和终结点

![FoundryModels](../../../../imgs/gpt-models.png)

接下来选择你想使用的模型以获取模型详情

![ModelDetails](../../../../imgs/model-deployment-name.png)

*.env* 文件中需要以下信息：

- Azure OpenAI 模型名称：你将使用的模型名称。
- Azure OpenAI 名称：你为 Azure OpenAI 模型部署所命名的名称。
- Azure OpenAI API 版本：你正在使用的 Azure OpenAI API 版本，位于 URL 字符串的末尾。

要获取这些信息，请选择模型部署

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### 添加 Azure 环境变量

3. 将你的 Azure OpenAI **名称** 和模型 **版本** 复制粘贴到 *.env* 文件中。
4. 保存 *.env* 文件。
5. 现在，你可以访问这些环境变量，以便使用 **Co-op Translator** 配合你的 Azure 服务。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始语言的文件应被视为权威版本。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。