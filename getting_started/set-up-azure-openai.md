# Set up Azure OpenAI for language translation

### Create an Azure OpenAI resource

1. Sign in to the [Azure Portal](https://portal.azure.com/).

1. Type *azure openai* in the **search bar** at the top of the portal page and select **Azure OpenAI** from the options that appear.

    ![Type Azure OpenAI.](../imgs/type-azure-openai.png)

1. Select **+ Create** from the navigation menu.

    ![Create Azure OpenAI.](../imgs/create-azure-openai.png)

1. Perform the following tasks:

    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (create a new one if needed).
    - Select the **Region** you'd like to use.
    - Enter **Name**. It must be a unique value.
    - Select the **Pricing tier** you'd like to use.

    ![Fill Azure OpenAI.](../imgs/fill-azureopenai.png)

1. Select **Next** to move to the **Network** page.

1. Select a network security **Type** you'd like to use.

    ![Select a network security Type.](../imgs/select-azureopenai-security-type.png)

1. Select **Next** to move to the **Tags** page.

1. Select **Next** to move to the **Review + submit** page.

1. Select **Create**.

    ![Select Create.](../imgs/create-azure-openai-complete.png)

### Deploy Azure OpenAI models

1. Navigate to the Azure OpenAI resource that you created.

1. Select **Go to Azure OpenAI Studio** from the navigation menu.

    ![Select Go to Azure OpenAI Studio from the navigation menu.](../imgs/go-to-azureopenai-studio.png)

1. Inside Azure OpenAI Studio, select **Deployments** from the left side tab.
1. Select **+ Deploy model** from the navigation menu.
1. Select **Deploy base model** from the navigation menu to create a new **gpt-4o** deployment.

    ![Select Deployments.](../imgs/deploy-aoai.png)

1. Perform the following tasks:

    - Inside **Select a model** page, select **gpt-4o**.
    - Select **Confirm** to navigate to the **Deploy model gpt-4o** page.
    - Inside **Deploy model gpt-4o** page, enter **Deployment name**. It must be a unique value. For example, **gpt-4o**.
    - Inside **Deploy model gpt-4o** page, select the **Deployment type** you'd like to use.

    ![Create model.](../imgs/create-4o.png)

1. Select **Deploy**.
