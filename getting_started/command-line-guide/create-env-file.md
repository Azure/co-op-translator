# Create the *.env* file in the root directory

In this tutorial, we will guide you through setting up your environment variables for Azure services using an *.env* file. Environment variables allow you to securely manage sensitive credentials, such as API keys, without hard-coding them into your codebase.

> [!IMPORTANT]
> - Only one language model service (Azure OpenAI or OpenAI) needs to be configured. Fill in the environment variables for your preferred service. If environment variables for multiple language models are set, the co-op translator will select one based on priority.
> - If Computer Vision environment variables are not set, the translator will automatically switch to [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> This guide primarily focuses on Azure services, but you can choose any supported language model from the [supported models and services list](../README.md#-supported-models-and-services).

## Create the *.env* file

In the root directory of your project, create a file named *.env*. This file will store all your environment variables in a simple format.

> [!WARNING]
> Do not commit your *.env* file to version control systems like Git. Add *.env* to your .gitignore file to prevent accidental commits.

1. Navigate to the root directory of your project.

1. Create an *.env* file in the root directory of your project.

    ![Create *.env* file.](../../imgs/create-env.png)

1. Open the *.env* file and paste the following template:

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

## Gather your Azure credentials

You will need the following Azure credentials on hand to configure the environment:

You can get all the details from the project overview page within [AI Foundry](https://ai.azure.com/build/overview)

![Foundry-overview](../../imgs/foundry-overview.png)


### For Azure AI Service:

    - Azure Subscription Key: Your Azure AI Services API Key, which allows you to access the Azure AI services.
    - Azure AI Service Endpoint: The endpoint URL for your specific Azure AI service.

### For Azure OpenAI Service:

    - Azure OpenAI API Key: The API key for accessing Azure OpenAI services.
    - Azure OpenAI Endpoint: The endpoint URL for your Azure OpenAI service.


1. Copy and paste your AI Services key and Endpoint into the *.env* file.
2. Copy and paste your Azure OpenAI API Key and Endpoint into the *.env* file.

### Model Details 

Select Model and Endpoints from the left hand menu 

![FoundryModels](../../imgs/gpt-models.png)

You now need to select the model which you wish to utilise to get the model details 

![ModelDetails](../../imgs/model-deployment-name.png)

For the .env file we need the following details 

    - Azure OpenAI Model Name: The name of the model you will be interacting with.
    - Azure OpenAI Name: The name of your deployment for Azure OpenAI models.
    - Azure OpenAI API Version: The version of the Azure OpenAI API you are using found at the end of the url string.

To get these details select the model deployment 

![FoundryModelinfo](../../imgs/foundry-model-info.png)

### Add Azure environment variables

3. Copy and paste your Azure OpenAI **Name** and model **Version** into the *.env* file.
4. Save the *.env* file.
5. Now, you can access these environment variables to use **Co-op Translator** with your Azure services.
