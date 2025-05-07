<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:18:21+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "zh"
}
-->
# 设置 Azure AI 用于合作翻译器（Azure OpenAI 和 Azure AI Vision）

本指南将带你完成在 Azure AI Foundry 中设置 Azure OpenAI 用于语言翻译，以及 Azure 计算机视觉用于图像内容分析（进而实现基于图像的翻译）的步骤。

**先决条件：**
- 拥有一个带有有效订阅的 Azure 账号。
- 具备在 Azure 订阅中创建资源和部署的权限。

## 创建 Azure AI 项目

首先创建一个 Azure AI 项目，作为管理 AI 资源的中心。

1. 访问 [https://ai.azure.com](https://ai.azure.com) 并使用你的 Azure 账号登录。

1. 选择 **+Create** 创建一个新项目。

1. 执行以下操作：
   - 输入 **项目名称**（例如 `CoopTranslator-Project`）。
   - 选择 **AI 中心**（例如 `CoopTranslator-Hub`）（如有需要，可新建一个）。

1. 点击“**Review and Create**”完成项目设置。你将进入项目概览页面。

## 设置 Azure OpenAI 用于语言翻译

在项目内，部署一个 Azure OpenAI 模型，作为文本翻译的后端。

### 进入你的项目

如果还没进入，打开你刚创建的项目（例如 `CoopTranslator-Project`）在 Azure AI Foundry 中。

### 部署 OpenAI 模型

1. 在项目左侧菜单中，“My assets”下选择“**Models + endpoints**”。

1. 选择 **+ Deploy model**。

1. 选择 **Deploy Base Model**。

1. 系统会展示可用模型列表。筛选或搜索合适的 GPT 模型。推荐使用 `gpt-4o`。

1. 选择你想要的模型，点击 **Confirm**。

1. 点击 **Deploy**。

### Azure OpenAI 配置

部署完成后，你可以在“**Models + endpoints**”页面选择该部署，查看其 **REST endpoint URL**、**Key**、**Deployment name**、**Model name** 和 **API version**。这些信息将用于将翻译模型集成到你的应用中。

## 设置 Azure 计算机视觉用于图像翻译

要实现图像中文字的翻译，需要获取 Azure AI 服务的 API Key 和 Endpoint。

1. 进入你的 Azure AI 项目（例如 `CoopTranslator-Project`），确保在项目概览页面。

### Azure AI 服务配置

从 Azure AI 服务中获取 API Key 和 Endpoint。

1. 进入你的 Azure AI 项目（例如 `CoopTranslator-Project`），确保在项目概览页面。

1. 在 Azure AI 服务标签页找到 **API Key** 和 **Endpoint**。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

此连接将链接的 Azure AI 服务资源（包括图像分析）功能引入你的 AI Foundry 项目。你可以在笔记本或应用中使用此连接提取图像中的文本，然后将其发送到 Azure OpenAI 模型进行翻译。

## 整理你的凭据

到目前为止，你应该已经收集了以下信息：

**针对 Azure OpenAI（文本翻译）：**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI 模型名称（例如 `gpt-4o`）
- Azure OpenAI 部署名称（例如 `cooptranslator-gpt4o`）
- Azure OpenAI API 版本

**针对 Azure AI 服务（通过视觉进行图像文字提取）：**
- Azure AI 服务 Endpoint
- Azure AI 服务 API Key

### 示例：环境变量配置（预览）

稍后构建应用时，通常会使用这些凭据进行配置。例如，可以将它们设置为环境变量，如下所示：

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

### 相关阅读

- [如何在 Azure AI Foundry 创建项目](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [如何创建 Azure AI 资源](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [如何在 Azure AI Foundry 部署 OpenAI 模型](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或曲解承担责任。