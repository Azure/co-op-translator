# Create an '.env' file in the root directory

In this tutorial, we will guide you through setting up your environment variables for Azure services using an `.env` file. Environment variables allow you to securely manage sensitive credentials, such as API keys, without hard-coding them into your codebase.

### Gather Your Azure Credentials

Before you create the .env file, make sure you have the following Azure credentials on hand:

#### For Azure AI Service:

- Azure Subscription Key: Your Azure subscription key, which allows you to access the Azure AI services.
- Azure AI Service Endpoint: The endpoint URL for your specific Azure AI service.

#### For Azure OpenAI Service:

- Azure OpenAI API Key: The API key for accessing Azure OpenAI services.
- Azure OpenAI Endpoint: The endpoint URL for your Azure OpenAI service.
- Azure OpenAI Model Name: The name of the model you will be interacting with.
- Azure OpenAI Deployment Name: The name of your deployment for Azure OpenAI models.
- Azure OpenAI API Version: The version of the Azure OpenAI API you are using.

### Create the `.env` File

In the root directory of your project, create a file named .env. This file will store all your environment variables in a simple format.

> [!WARNING]
> Do not commit your .env file to version control systems like Git. Add .env to your .gitignore file to prevent accidental commits.

1. Navigate to the root directory of your project.

1. Create an `.env` file in the root directory of your project by copying the provided .env.template file. Fill in the environment variables in the `.env` file as a guide.

1. Open the .env file and copy the following template:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_subscription_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"
    
    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"
    ```

1. Replace the placeholder values (e.g., your_azure_subscription_key) with your actual credentials.

1. Save the `.env` file.

1. Now, you can access these environment variables to use Co Op Translator with your Azure services.
