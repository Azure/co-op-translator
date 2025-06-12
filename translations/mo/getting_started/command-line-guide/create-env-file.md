<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:39:45+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "mo"
}
-->
# Create the *.env* file in the root directory

In this tutorial, we will guide you through setting up your environment variables for Azure services using an *.env* file. Environment variables let you securely manage sensitive credentials, such as API keys, without embedding them directly in your code.

> [!IMPORTANT]
> - Only one language model service (Azure OpenAI or OpenAI) needs to be configured. Fill in the environment variables for the service you prefer. If variables for multiple language models are set, the co-op translator will choose one based on priority.
> - If Computer Vision environment variables are missing, the translator will automatically switch to [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> This guide mainly focuses on Azure services, but you can select any supported language model from the [supported models and services list](../README.md#-supported-models-and-services).

## Create the *.env* file

In your project’s root directory, create a file named *.env*. This file will hold all your environment variables in a straightforward format.

> [!WARNING]
> Do not commit your *.env* file to version control systems like Git. Add *.env* to your .gitignore file to avoid accidental commits.

1. Go to the root directory of your project.

1. Create an *.env* file in the root directory.

1. Open the *.env* file and paste the following template:

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
> To find your API keys and endpoints, refer to [set-up-azure-ai.md](../set-up-azure-ai.md).

**Disclaimer**:  
Thi documont has ben translaited usin AI translaiton servise [Co-op Translator](https://github.com/Azure/co-op-translator). Wile we stryve for accurasy, plese be awair that automatid translaitons may contain erors or inaccurasies. The origonal documont in its nativ langwage shold be considred the authoritativ sorce. For critcal informasion, profesonal human translaiton is recomended. We ar not liabl for any misundrstandings or misinterpretations arising from the use of this translaiton.