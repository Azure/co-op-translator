<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:14:57+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "zh"
}
-->
# 设置 Azure OpenAI 进行语言翻译

## 在 Azure AI Foundry 中创建 Azure OpenAI 资源

要在 Azure AI Foundry 中设置 Azure OpenAI，请按照以下步骤操作：

### 创建 Hub

1. 登录 [Azure AI Foundry 门户](https://ai.azure.com)：确保你已使用 Azure 账号登录。

2. 进入管理中心：在首页，从左侧菜单选择“Management Center”。

3. 创建新 Hub：点击“+ New hub”，填写订阅、资源组和 Hub 名称等必要信息。建议将 Hub 部署在 East US 区域，因为该区域支持认知视觉和 GPT 模型。

4. 审核并创建：确认信息无误后，点击“Create”创建 Hub。

### 创建项目

1. 进入首页：如果不在首页，点击页面左上角的“Azure AI Foundry”返回首页。

2. 创建项目：点击“+ Create project”，输入项目名称。

3. 选择 Hub：如果有多个 Hub，选择你要使用的那个。如果需要新建 Hub，也可以在此步骤进行创建。

4. 配置项目：按照提示，根据需求配置项目。

5. 创建项目：点击“Create”完成设置。

### 部署 OpenAI 模型和端点

1. 登录 [Azure AI Foundry 门户](https://ai.azure.com)：确保你使用包含 Azure OpenAI 服务资源的 Azure 订阅登录。

2. 进入模型和端点：在 Azure AI Foundry 首页，找到相应模块并点击“Let's go.”，或者从左侧菜单选择“Model and Endpoints”。

3. 如果尚未部署 GPT 模型，选择“deploy model”：推荐选择 GPT-4o、GPT-4o-mini 或 o3-mini。

4. 访问资源：你会看到已有的 Azure OpenAI 服务资源。如果有多个资源，使用选择器选择你想操作的资源。

更多详细说明，请参考官方 Azure AI Foundry 文档。

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。