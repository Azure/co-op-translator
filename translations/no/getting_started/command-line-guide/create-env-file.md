<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:28+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "no"
}
-->
# Opprett *.env*-filen i rotmappen

I denne veiledningen vil vi hjelpe deg med å sette opp miljøvariablene dine for Azure-tjenester ved bruk av en *.env*-fil. Miljøvariabler lar deg håndtere sensitive legitimasjoner, som API-nøkler, på en sikker måte uten å hardkode dem i koden din.

> [!IMPORTANT]
> - Bare én språkmodell-tjeneste (Azure OpenAI eller OpenAI) trenger å konfigureres. Fyll inn miljøvariablene for den tjenesten du foretrekker. Hvis miljøvariabler for flere språkmodeller er satt, vil co-op-oversetteren velge én basert på prioritet.
> - Hvis miljøvariabler for Computer Vision ikke er satt, vil oversetteren automatisk bytte til [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Denne veiledningen fokuserer hovedsakelig på Azure-tjenester, men du kan velge hvilken som helst støttet språkmodell fra [listen over støttede modeller og tjenester](../README.md#-supported-models-and-services).

## Opprett *.env*-filen

I rotmappen til prosjektet ditt, opprett en fil som heter *.env*. Denne filen vil lagre alle miljøvariablene dine i et enkelt format.

> [!WARNING]
> Ikke legg *.env*-filen inn i versjonskontrollsystemer som Git. Legg til *.env* i .gitignore-filen din for å unngå utilsiktede innlegginger.

1. Gå til rotmappen i prosjektet ditt.

1. Opprett en *.env*-fil i rotmappen til prosjektet ditt.

1. Åpne *.env*-filen og lim inn følgende mal:

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
> Hvis du vil finne API-nøklene og endepunktene dine, kan du se [set-up-azure-ai.md](../set-up-azure-ai.md).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.