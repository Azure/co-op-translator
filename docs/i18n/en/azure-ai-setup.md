# Azure AI Setup

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Prerequisites

- An Azure subscription.
- Permission to create or use Azure AI resources and model deployments.
- A project in Azure AI Foundry or equivalent access to Azure OpenAI and Azure AI Vision resources.

## Create an Azure AI Project

1. Open [Azure AI Foundry](https://ai.azure.com).
2. Create or select a project.
3. Create or select an AI hub for the project.
4. Open the project overview after creation.

## Deploy an Azure OpenAI Model

1. In the project, open **Models + endpoints**.
2. Select **Deploy model**.
3. Choose a GPT model such as `gpt-4o`.
4. Deploy the model.
5. Record the endpoint, deployment name, model name, API key, and API version.

!!! note
    The Azure OpenAI API version is separate from the model version shown in Azure AI Foundry. Choose a supported API version for your deployment.

## Configure Azure AI Vision

Image translation uses Azure AI Vision to extract text from source images before the text is translated.

In your Azure AI project, find the Azure AI Services key and endpoint.

![Find Azure AI service information](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service endpoint
- Azure AI Service API key

## Environment Variables

Add the credentials to your `.env` file or CI secrets.

```bash
# Azure AI Vision, required for image translation
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, required for text translation
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator also supports optional fallback credential sets. Duplicate a complete provider set with suffixes such as `_1` or `_2`; all variables in a fallback set must share the same suffix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Next Steps

- Return to [Configuration](configuration.md) to set up local or CI environment variables.
- Use [CLI Reference](cli.md) for translation commands.
- Use [GitHub Actions](github-actions.md) to automate translation pull requests.