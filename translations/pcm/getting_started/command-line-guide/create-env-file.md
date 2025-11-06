<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-11-06T17:31:41+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "pcm"
}
-->
# Create di *.env* file for di root directory

For dis tutorial, we go show you how you fit take set up your environment variables for Azure services using *.env* file. Environment variables dey help you manage sensitive credentials like API keys well, so you no go need to put dem directly for your code.

> [!IMPORTANT]
> - Na only one language model service (Azure OpenAI or OpenAI) you need configure. Put di environment variables for di service wey you like pass. If you set environment variables for more than one language model, di co-op translator go choose one based on priority.
> - If you no set Computer Vision environment variables, di translator go automatically switch to [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Dis guide na mainly for Azure services, but you fit still choose any language model wey dey di [supported models and services list](../README.md#-supported-models-and-services).

## Create di *.env* file

For di root directory of your project, create one file wey you go name *.env*. Dis file go hold all your environment variables for simple format.

> [!WARNING]
> No put your *.env* file for version control systems like Git. Add *.env* to your .gitignore file so you no go mistakenly commit am.

1. Go di root directory of your project.

1. Create one *.env* file for di root directory of your project.

1. Open di *.env* file and paste di template wey dey below:

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
> If you wan find your API keys and endpoints, you fit check [set-up-azure-ai.md](../set-up-azure-ai.md).

---

**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say transleshion wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.