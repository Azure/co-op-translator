<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:10+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "sv"
}
-->
# Skapa filen *.env* i rotmappen

I den här guiden visar vi hur du ställer in dina miljövariabler för Azure-tjänster med hjälp av en *.env*-fil. Miljövariabler gör det möjligt att hantera känsliga uppgifter, som API-nycklar, på ett säkert sätt utan att hårdkoda dem i din kodbas.

> [!IMPORTANT]
> - Endast en språkmodellstjänst (Azure OpenAI eller OpenAI) behöver konfigureras. Fyll i miljövariablerna för den tjänst du föredrar. Om miljövariabler för flera språkmodeller är satta kommer översättaren att välja en baserat på prioritet.
> - Om miljövariabler för Computer Vision inte är inställda, kommer översättaren automatiskt att växla till [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Den här guiden fokuserar främst på Azure-tjänster, men du kan välja vilken som helst av de språkmodeller som stöds från [listan över stödja modeller och tjänster](../README.md#-supported-models-and-services).

## Skapa filen *.env*

I rotmappen för ditt projekt, skapa en fil som heter *.env*. Den här filen kommer att lagra alla dina miljövariabler i ett enkelt format.

> [!WARNING]
> Lägg inte upp din *.env*-fil i versionshanteringssystem som Git. Lägg till *.env* i din .gitignore-fil för att undvika oavsiktliga commits.

1. Gå till rotmappen för ditt projekt.

1. Skapa en *.env*-fil i rotmappen för ditt projekt.

1. Öppna *.env*-filen och klistra in följande mall:

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
> Om du vill hitta dina API-nycklar och endpoints kan du se [set-up-azure-ai.md](../set-up-azure-ai.md).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.