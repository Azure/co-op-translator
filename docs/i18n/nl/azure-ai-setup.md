# Azure AI Setup

Use deze gids wanneer je Azure OpenAI wilt configureren voor tekstvertaling en Azure AI Vision voor het extraheren van tekst uit afbeeldingen.

## Prerequisites

- Een Azure-abonnement.
- Machtiging om Azure AI-resources en modelimplementaties te maken of te gebruiken.
- Een project in Azure AI Foundry of gelijkwaardige toegang tot Azure OpenAI- en Azure AI Vision-resources.

## Create an Azure AI Project

1. Open [Azure AI Foundry](https://ai.azure.com).
2. Maak of selecteer een project.
3. Maak of selecteer een AI-hub voor het project.
4. Open het projectoverzicht na aanmaak.

## Deploy an Azure OpenAI Model

1. In het project, open **Models + endpoints**.
2. Selecteer **Deploy model**.
3. Kies een GPT-model zoals `gpt-4o`.
4. Implementeer het model.
5. Noteer het endpoint, de deploymentnaam, modelnaam, API-sleutel en API-versie.

!!! note
    De Azure OpenAI API-versie is losstaand van de modelversie die wordt weergegeven in Azure AI Foundry. Kies een ondersteunde API-versie voor je implementatie.

## Configure Azure AI Vision

Beeldvertaling gebruikt Azure AI Vision om tekst uit bronafbeeldingen te extraheren voordat de tekst wordt vertaald.

In je Azure AI-project, zoek de Azure AI Services-sleutel en het endpoint.

![Vind informatie over Azure AI-service](../../assets/find-azure-ai-info.png)

Noteer:

- Azure AI Service-endpoint
- Azure AI Service API-sleutel

## Environment Variables

Voeg de referenties toe aan je `.env`-bestand of CI-secrets.

```bash
# Azure AI Vision, vereist voor afbeeldingsvertaling
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, vereist voor tekstvertaling
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator ondersteunt ook optionele fallback-referentiesets. Dupliceer een volledige provider set met achtervoegsels zoals `_1` of `_2`; alle variabelen in een fallback-set moeten hetzelfde achtervoegsel hebben.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Next Steps

- Ga terug naar [Configuratie](configuration.md) om lokale of CI-omgevingsvariabelen in te stellen.
- Gebruik de [CLI-referentie](cli.md) voor vertaalopdrachten.
- Gebruik [GitHub Actions](github-actions.md) om vertaal-pull requests te automatiseren.