# Create a `.env` file

Co-op Translator reads credentials from environment variables. For local use, place them in a `.env` file at your project root.

> [!IMPORTANT]
> Configure either Azure OpenAI or OpenAI. You do not need both. Azure AI Vision is required only for image translation.

> [!WARNING]
> Do not commit `.env` files. Store real keys in your local environment or CI secret store.

## Minimal template

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment-name>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID=""        # optional
OPENAI_BASE_URL=""      # optional

# Azure AI Vision, required for `translate -img`
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-resource>.cognitiveservices.azure.com/"
```

## Multiple credential sets

You can add fallback sets by giving every variable in a set the same suffix:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

Each set must be complete. The translator validates connectivity and selects a working set before translation starts.

For the full provider matrix and command requirements, see [Configuration](../../docs/configuration.md). For Azure portal steps, see [Set up Azure AI](../set-up-azure-ai.md).
