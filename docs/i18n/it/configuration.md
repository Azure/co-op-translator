# Configurazione

Co-op Translator richiede un provider di modelli linguistici. La traduzione delle immagini richiede inoltre Azure AI Vision.

La configurazione viene letta dalle variabili d'ambiente. Per progetti locali, inseriscile in un file `.env` nella root del progetto.

Per la configurazione delle risorse Azure, vedi [Configurazione di Azure AI](azure-ai-setup.md).

## Configurazione dell'ambiente locale

Usa un ambiente virtuale prima di eseguire la CLI in locale. Co-op Translator supporta Python dalla versione 3.10 alla 3.12.

Per l'uso normale della CLI, installa il pacchetto pubblicato all'interno di un ambiente virtuale:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Per lo sviluppo del repository, installa le dipendenze dalla root del progetto invece:

```bash
poetry install
poetry run translate --help
```

Dopo che la CLI è disponibile, configura un provider di modelli linguistici in `.env`.

## Selezione del provider

Lo strumento individua automaticamente i provider in questo ordine:

1. Azure OpenAI
2. OpenAI

Se nessuno dei provider è configurato, `translate`, `evaluate`, `migrate-links` e `run_translation` falliscono durante i controlli di configurazione. `co-op-review` e `run_review` sono controlli di manutenzione deterministici e non richiedono credenziali del provider.

## Azure OpenAI

Usa Azure OpenAI quando il tuo modello è distribuito in Azure AI Foundry o in Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Il controllo di connettività utilizza l'endpoint, la chiave API, la versione dell'API e il nome della distribuzione prima dell'inizio della traduzione.

## OpenAI

Usa OpenAI quando chiami direttamente l'API OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opzionale
OPENAI_BASE_URL="..."        # opzionale
```

`OPENAI_CHAT_MODEL_ID` è richiesto perché il traduttore necessita di un modello chat esplicito per le chiamate API.

## Azure AI Vision

La traduzione delle immagini richiede Azure AI Vision affinché lo strumento possa estrarre il testo dalle immagini prima di tradurlo.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Se la traduzione delle immagini è selezionata con `-img`, `images=True`, o senza filtro content-type, lo strumento convalida la configurazione di Vision prima dell'avvio della traduzione.

## Set multipli di credenziali

Il livello di configurazione supporta set multipli di credenziali aggiungendo un suffisso con lo stesso indice alle variabili:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Ogni set deve essere completo. Il controllo di integrità seleziona un set funzionante prima che la traduzione prosegua.

## Requisiti dei comandi

| Comando o API | LLM richiesto | Vision richiesta | Note |
| --- | --- | --- | --- |
| `translate -md` | Sì | No | Traduce solo Markdown. |
| `translate -nb` | Sì | No | Traduce solo i notebook. |
| `translate -img` | Sì | Sì | Traduce solo le immagini. |
| `translate` with no type flags | Sì | Sì | La modalità predefinita include Markdown, notebook e immagini. |
| `evaluate` | Sì | No | Utilizza la valutazione LLM a meno che non sia selezionato `--fast`. |
| `migrate-links` | Sì | No | Esegue la migrazione dei link, ma esegue comunque i controlli di configurazione condivisi. |
| `co-op-review` | No | No | Esegue controlli deterministici sulla struttura della traduzione, freschezza, Markdown, notebook e link locali. |
| `run_translation(markdown=True)` | Sì | No | Traduzione Markdown programmatica. |
| `run_translation(images=True)` | Sì | Sì | Traduzione immagini programmatica. |
| `run_review(...)` | No | No | Revisione deterministica programmatica. |

## Directory di output

Output predefinito per la traduzione di testo:

```text
translations/<language-code>/<source-relative-path>
```

Output predefinito per le immagini tradotte:

```text
translated_images/<language-code>/<source-relative-path>
```

L'API Python può sovrascrivere queste directory con `translations_dir` e `image_dir`.