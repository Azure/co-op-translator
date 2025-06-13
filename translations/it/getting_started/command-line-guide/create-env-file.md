<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:26:23+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "it"
}
-->
# Crea il file *.env* nella directory principale

In questo tutorial ti guideremo nella configurazione delle variabili d'ambiente per i servizi Azure utilizzando un file *.env*. Le variabili d'ambiente ti permettono di gestire in modo sicuro le credenziali sensibili, come le chiavi API, senza inserirle direttamente nel codice.

> [!IMPORTANT]
> - È necessario configurare un solo servizio di modello linguistico (Azure OpenAI o OpenAI). Compila le variabili d'ambiente per il servizio che preferisci. Se sono impostate variabili d'ambiente per più modelli linguistici, il traduttore cooperativo ne selezionerà uno in base alla priorità.
> - Se le variabili d'ambiente per Computer Vision non sono impostate, il traduttore passerà automaticamente alla [modalità solo Markdown](./markdown-only-mode.md).

> [!NOTE]
> Questa guida si concentra principalmente sui servizi Azure, ma puoi scegliere qualsiasi modello linguistico supportato dalla [lista di modelli e servizi supportati](../README.md#-supported-models-and-services).

## Crea il file *.env*

Nella directory principale del tuo progetto, crea un file chiamato *.env*. Questo file conterrà tutte le variabili d'ambiente in un formato semplice.

> [!WARNING]
> Non inserire il file *.env* nei sistemi di controllo versione come Git. Aggiungi *.env* al file .gitignore per evitare commit accidentali.

1. Vai nella directory principale del tuo progetto.

1. Crea un file *.env* nella directory principale del tuo progetto.

1. Apri il file *.env* e incolla il seguente modello:

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
> Se vuoi trovare le tue chiavi API e gli endpoint, puoi fare riferimento a [set-up-azure-ai.md](../set-up-azure-ai.md).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un traduttore umano. Non ci assumiamo responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.