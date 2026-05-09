# Create the *.env* file in the root directory

In this tutorial, we will guide you through setting up your environment variables for Azure services using an *.env* file. Environment variables allow you to securely manage sensitive credentials, such as API keys, without hard-coding them into your codebase.

> [!IMPORTANT]
> - Configure either Azure OpenAI or OpenAI. You do not need both.
> - Azure AI Vision is required only for image translation. If Vision variables are not set, run text-only commands such as `translate -l "ko" -md` or `translate -l "ko" -nb`.

> [!NOTE]
> This guide focuses on the local `.env` file. For the current provider matrix and command requirements, see the [configuration reference](../../docs/configuration.md).

## Create the *.env* file

In the root directory of your project, create a file named *.env*. This file will store all your environment variables in a simple format.

> [!WARNING]
> Do not commit your *.env* file to version control systems like Git. Add *.env* to your .gitignore file to prevent accidental commits.

1. Navigate to the root directory of your project.

1. Create an *.env* file in the root directory of your project.

1. Open the *.env* file and paste the following template:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1" # Optional. Remove this line to use the default OpenAI base URL.

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> If you want to find your API keys and endpoints, you can refer to [set-up-azure-ai.md](../set-up-azure-ai.md).
