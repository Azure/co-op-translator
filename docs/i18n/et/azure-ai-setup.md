# Azure AI seadistamine

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Eeltingimused

- Azure'i tellimus.
- Luba Azure AI ressursside ja mudeli juurutuste loomiseks või kasutamiseks.
- Projekt Azure AI Foundry'is või samaväärne juurdepääs Azure OpenAI ja Azure AI Vision ressurssidele.

## Azure AI projekti loomine

1. Avage [Azure AI Foundry](https://ai.azure.com).
2. Loo või vali projekt.
3. Loo või vali projekti jaoks AI-hub.
4. Avage pärast loomist projekti ülevaade.

## Azure OpenAI mudeli juurutamine

1. Projektis avage **Models + endpoints**.
2. Valige **Deploy model**.
3. Valige GPT-mudel, näiteks `gpt-4o`.
4. Juurutage mudel.
5. Salvestage lõpp-punkt, juurutuse nimi, mudeli nimi, API-võti ja API-versioon.

!!! note
    Azure OpenAI API versioon on eraldi Azure AI Foundry'is kuvatavast mudeli versioonist. Valige oma juurutuse jaoks toetatud API-versioon.

## Azure AI Visioni seadistamine

Piltide tõlkimine kasutab Azure AI Visioni selleks, et eraldada tekst lähtepiltidelt enne teksti tõlkimist.

In your Azure AI project, find the Azure AI Services key and endpoint.

![Leia Azure AI teenuse teave](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service lõpp-punkt
- Azure AI Service API-võti

## Keskkonnamuutujad

Lisage autentimisandmed oma `.env` faili või CI saladustesse.

```bash
# Azure AI Vision, vajalik piltide tõlkimiseks
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, vajalik teksti tõlkimiseks
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator toetab ka valikulisi varu autentimisandmete komplekte. Duplikeerige täielik pakkuja komplekt sufiksiga nagu `_1` või `_2`; kõigil muutujatel varu komplektis peab olema sama sufiks.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Järgmised sammud

- Minge tagasi [Konfiguratsioon](configuration.md), et seadistada lokaalseid või CI keskkonnamuutujaid.
- Kasutage [CLI viidet](cli.md) tõlkimiskäskude jaoks.
- Kasutage [GitHub Actions](github-actions.md) tõlke pull requestide automatiseerimiseks.