# Azure AI Setup

Use dis guide if you wan configure Azure OpenAI for text translation and Azure AI Vision to comot text from images.

## Wetin you need

- Azure subscription.
- Permission to create or use Azure AI resources and model deployments.
- Project for Azure AI Foundry or similar access to Azure OpenAI and Azure AI Vision resources.

## Create an Azure AI Project

1. Open [Azure AI Foundry](https://ai.azure.com).
2. Create or select one project.
3. Create or select an AI hub for the project.
4. Open the project overview after you don create am.

## Deploy an Azure OpenAI Model

1. For the project, open **Models + endpoints**.
2. Select **Deploy model**.
3. Choose one GPT model like `gpt-4o`.
4. Deploy the model.
5. Abeg record the endpoint, deployment name, model name, API key, and API version.

!!! note
    Di Azure OpenAI API version different from di model version wey dem dey show for Azure AI Foundry. Make you choose API version wey dem support for your deployment.

## Configure Azure AI Vision

Image translation dey use Azure AI Vision to comot text from source images before dem go translate am.

For your Azure AI project, find di Azure AI Services key and endpoint.

![Find Azure AI service information](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service endpoint
- Azure AI Service API key

## Environment Variables

Put di credentials for your `.env` file or CI secrets.

```bash
# Azure AI Vision, wey dem need for picture translation
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, wey dem need for text translation
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator still dey support optional fallback credential sets. Duplicate whole provider set and add suffix dem like `_1` or `_2`; all variables for one fallback set must get the same suffix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Next Steps

- Go back to [Configuration](configuration.md) to set up local or CI environment variables.
- Use [CLI Reference](cli.md) for translation commands.
- Use [GitHub Actions](github-actions.md) to automate translation pull requests.