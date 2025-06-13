<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:18+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "da"
}
-->
# Opret *.env*-filen i rodmappen

I denne vejledning vil vi guide dig gennem opsætningen af dine miljøvariabler til Azure-tjenester ved hjælp af en *.env*-fil. Miljøvariabler giver dig mulighed for sikkert at håndtere følsomme legitimationsoplysninger, som API-nøgler, uden at indkode dem direkte i din kode.

> [!IMPORTANT]
> - Kun én sprogmodeltjeneste (Azure OpenAI eller OpenAI) skal konfigureres. Udfyld miljøvariablerne for den tjeneste, du foretrækker. Hvis miljøvariabler for flere sprogmodeller er sat, vælger oversætteren en baseret på prioritet.
> - Hvis miljøvariabler for Computer Vision ikke er sat, skifter oversætteren automatisk til [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Denne guide fokuserer primært på Azure-tjenester, men du kan vælge en hvilken som helst understøttet sprogmodel fra [listen over understøttede modeller og tjenester](../README.md#-supported-models-and-services).

## Opret *.env*-filen

I rodmappen af dit projekt opretter du en fil med navnet *.env*. Denne fil vil gemme alle dine miljøvariabler i et enkelt format.

> [!WARNING]
> Undlad at committe din *.env*-fil til versionsstyringssystemer som Git. Tilføj *.env* til din .gitignore-fil for at undgå utilsigtede commits.

1. Naviger til rodmappen i dit projekt.

1. Opret en *.env*-fil i rodmappen af dit projekt.

1. Åbn *.env*-filen og indsæt følgende skabelon:

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
> Hvis du vil finde dine API-nøgler og endpoints, kan du se [set-up-azure-ai.md](../set-up-azure-ai.md).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.