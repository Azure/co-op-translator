# Configurazione di Azure AI

Usa questa guida quando desideri configurare Azure OpenAI per la traduzione di testo e Azure AI Vision per l'estrazione del testo dalle immagini.

## Prerequisiti

- Una sottoscrizione Azure.
- Autorizzazione a creare o utilizzare risorse Azure AI e distribuzioni dei modelli.
- Un progetto in Azure AI Foundry o accesso equivalente alle risorse Azure OpenAI e Azure AI Vision.

## Creare un progetto Azure AI

1. Apri [Azure AI Foundry](https://ai.azure.com).
2. Crea o seleziona un progetto.
3. Crea o seleziona un AI hub per il progetto.
4. Apri la panoramica del progetto dopo la creazione.

## Distribuire un modello Azure OpenAI

1. Nel progetto, apri **Modelli + endpoint**.
2. Seleziona **Distribuisci modello**.
3. Scegli un modello GPT come `gpt-4o`.
4. Distribuisci il modello.
5. Annota l'endpoint, il nome del deployment, il nome del modello, la chiave API e la versione dell'API.

!!! note
    La versione dell'API Azure OpenAI è separata dalla versione del modello mostrata in Azure AI Foundry. Scegli una versione dell'API supportata per il tuo deployment.

## Configurare Azure AI Vision

La traduzione delle immagini utilizza Azure AI Vision per estrarre il testo dalle immagini sorgente prima che il testo venga tradotto.

Nel tuo progetto Azure AI, trova la chiave e l'endpoint di Azure AI Services.

![Trova le informazioni sul servizio Azure AI](../../assets/find-azure-ai-info.png)

Annota:

- Endpoint del servizio Azure AI
- Chiave API del servizio Azure AI

## Variabili d'ambiente

Aggiungi le credenziali al tuo file `.env` o ai segreti del CI.

```bash
# Azure AI Vision, necessario per la traduzione delle immagini
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, necessario per la traduzione del testo
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator supporta inoltre set di credenziali di fallback opzionali. Duplica un insieme completo di provider con suffissi come `_1` o `_2`; tutte le variabili in un set di fallback devono condividere lo stesso suffisso.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Prossimi passi

- Torna a [Configuration](configuration.md) per configurare le variabili d'ambiente locali o del CI.
- Usa [Riferimento CLI](cli.md) per i comandi di traduzione.
- Usa [GitHub Actions](github-actions.md) per automatizzare le pull request di traduzione.