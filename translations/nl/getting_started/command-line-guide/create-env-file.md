<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:46+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "nl"
}
-->
# Maak het *.env*-bestand aan in de hoofdmap

In deze handleiding begeleiden we je bij het instellen van je omgevingsvariabelen voor Azure-diensten met behulp van een *.env*-bestand. Omgevingsvariabelen stellen je in staat om gevoelige gegevens, zoals API-sleutels, veilig te beheren zonder ze hardcoded in je codebase op te nemen.

> [!IMPORTANT]
> - Er hoeft maar één taalmodelservice (Azure OpenAI of OpenAI) te worden geconfigureerd. Vul de omgevingsvariabelen in voor de service die je wilt gebruiken. Als er omgevingsvariabelen voor meerdere taalmodellen zijn ingesteld, kiest de co-op translator er één op basis van prioriteit.
> - Als de omgevingsvariabelen voor Computer Vision niet zijn ingesteld, schakelt de translator automatisch over naar de [Markdown-only modus](./markdown-only-mode.md).

> [!NOTE]
> Deze gids richt zich voornamelijk op Azure-diensten, maar je kunt elk ondersteund taalmodel kiezen uit de [lijst met ondersteunde modellen en diensten](../README.md#-supported-models-and-services).

## Maak het *.env*-bestand aan

Maak in de hoofdmap van je project een bestand met de naam *.env* aan. Dit bestand slaat al je omgevingsvariabelen op in een eenvoudig formaat.

> [!WARNING]
> Voeg je *.env*-bestand niet toe aan versiebeheersystemen zoals Git. Voeg *.env* toe aan je .gitignore-bestand om te voorkomen dat het per ongeluk wordt gecommit.

1. Navigeer naar de hoofdmap van je project.

1. Maak een *.env*-bestand aan in de hoofdmap van je project.

1. Open het *.env*-bestand en plak de volgende template:

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
> Als je je API-sleutels en endpoints wilt vinden, kun je terecht in [set-up-azure-ai.md](../set-up-azure-ai.md).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.