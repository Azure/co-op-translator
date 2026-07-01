# Azure AI 设置

当您想为文本翻译配置 Azure OpenAI 并为图像文字提取配置 Azure AI Vision 时，请使用本指南。

## 前提条件

- Azure 订阅。
- 创建或使用 Azure AI 资源和模型部署的权限。
- Azure AI Foundry 中的项目或对 Azure OpenAI 和 Azure AI Vision 资源的等效访问权限。

## 创建 Azure AI 项目

1. 打开 [Azure AI Foundry](https://ai.azure.com)。
2. 创建或选择一个项目。
3. 为该项目创建或选择 AI 中心。
4. 创建后打开项目概览。

## 部署 Azure OpenAI 模型

1. 在项目中，打开 **Models + endpoints**。
2. 选择 **Deploy model**。
3. 选择 GPT 模型，例如 `gpt-4o`。
4. 部署模型。
5. 记录端点、部署名称、模型名称、API 密钥和 API 版本。

!!! note
    Azure OpenAI 的 API 版本与 Azure AI Foundry 中显示的模型版本是分开的。为您的部署选择受支持的 API 版本。

## 配置 Azure AI Vision

图像翻译在翻译文本之前使用 Azure AI Vision 从源图像中提取文本。

在您的 Azure AI 项目中，查找 Azure AI Services 密钥和端点。

![查找 Azure AI 服务信息](../../assets/find-azure-ai-info.png)

记录：

- Azure AI Service 端点
- Azure AI Service API 密钥

## 环境变量

将凭据添加到您的 `.env` 文件或 CI 密钥中。

```bash
# Azure AI Vision，图像翻译所必需
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI，文本翻译所必需
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator 还支持可选的回退凭证集。复制完整的提供程序集并添加后缀，例如 `_1` 或 `_2`；回退集中的所有变量必须共享相同的后缀。

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## 下一步

- 返回 [Configuration](configuration.md) 以设置本地或 CI 环境变量。
- 使用 [CLI Reference](cli.md) 了解翻译命令。
- 使用 [GitHub Actions](github-actions.md) 自动化翻译拉取请求。