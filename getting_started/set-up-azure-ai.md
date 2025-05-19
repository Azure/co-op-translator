# Set Up Azure AI for Co-op Translator (Azure OpneAI & Azure AI Vision)

This guide walks you through setting up Azure OpenAI for language translation and Azure Computer Vision for image content analysis (which can then be used for image-based translation) within Azure AI Foundry.

**Prerequisites:**
- An Azure account with an active subscription.
- Sufficient permissions to create resources and deployments in your Azure subscription.

## Create an Azure AI Project

You'll start by creating an Azure AI Project, which acts as a central place for managing your AI resources.

1. Navigate to [https://ai.azure.com](https://ai.azure.com) and sign in with your Azure account.

1. Select **+Create** to create a new project.

1. Perform the following tasks:
   - Enter a **Project name** (e.g., `CoopTranslator-Project`).
   - Select the **AI hub**  (e.g., `CoopTranslator-Hub`) (Create a new one if needed).

1. Click "**Review and Create**" to set up your project. You will be taken to your project's overview page.

## Set up Azure OpenAI for Language Translation

Within your project, you will deploy an Azure OpenAI model to serve as the backend for text translation.

### Navigate to Your Project

If not already there, open your newly created project (e.g., `CoopTranslator-Project`) in Azure AI Foundry.

### Deploy an OpenAI Model

1. From your project's left-hand menu, under "My assets", select "**Models + endpoints**".

1. Select **+ Deploy model**.

1. Select **Deploy Base Model**.

1. You will be presented with a list of available models. Filter or search for a suitable GPT model. We recommend `gpt-4o`.

1. Select your desired model and click **Confirm**.

1. Select **Deploy**.

### Azure OpenAI configuration

Once deployed, you can select the deployment from the "**Models + endpoints**" page to find its **REST endpoint URL**, **Key**, **Deployment name**, **Model name** and **API version**. These will be needed to integrate the translation model into your application.

> [!NOTE]
> You can select API versions from the [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) page based on your requirements. Be aware that the **API version** is different from the **Model version** shown on the **Models + endpoints** page in Azure AI Foundry.

## Set up Azure Computer Vision for Image Translation

To enable translation of text within images, you need to find the Azure AI Service API Key and Endpoint.

1. Navigate to your Azure AI Project (e.g., `CoopTranslator-Project`). Ensure you are in the project overview page.

### Azure AI Service configuration

Find the API Key and Endpoint from the Azure AI Service.

1. Navigate to your Azure AI Project (e.g., `CoopTranslator-Project`). Ensure you are in the project overview page.

1. Find the **API Key** and **Endpoint** from the Azure AI Service tab.

    ![Find API Key and Endpoint](./imgs/find-azure-ai-info.png)

This connection makes the capabilities of the linked Azure AI Services resource (including image analysis) available to your AI Foundry project. You can then use this connection in your notebooks or applications to extract text from images, which can subsequently be sent to the Azure OpenAI model for translation.

## Consolidating Your Credentials

By now, you should have collected the following:

**For Azure OpenAI (Text Translation):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (e.g., `gpt-4o`)
- Azure OpenAI Deployment Name (e.g., `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**For Azure AI Services (Image Text Extraction via Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Example: Environment Variable Configuration (Preview)

Later, when building your application, you'll likely configure it using these collected credentials. For instance, you might set them as environment variables like so:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### Further Reading

- [How to Create a project in Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [How to Create Azure AI resources](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [How to Deploy OpenAI models in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)
