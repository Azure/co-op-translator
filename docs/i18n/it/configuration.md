# Configurazione

Co-op Translator richiede un provider di modelli linguistici. La traduzione delle immagini richiede inoltre Azure AI Vision.

La configurazione viene letta dalle variabili d'ambiente. Per i progetti locali, inseriscile in un file `.env` nella radice del progetto.

Per la configurazione delle risorse Azure, vedere [Configurazione di Azure AI](azure-ai-setup.md).

## Configurazione dell'ambiente di esecuzione locale

Usa un ambiente virtuale prima di eseguire la CLI localmente. Co-op Translator supporta Python da 3.11 a 3.14.

Per l'utilizzo normale della CLI, installa il pacchetto pubblicato all'interno di un ambiente virtuale:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Sviluppo del repository

Per lo sviluppo del repository, installa le dipendenze dalla radice del progetto invece:

```bash
poetry install
poetry run translate --help
```

Dopo che la CLI è disponibile, configura un provider di modelli linguistici in `.env`.

## Selezione del provider

Lo strumento rileva automaticamente i provider in questo ordine:

1. Azure OpenAI
2. OpenAI
3. Anthropic

La traduzione richiede le credenziali del provider, ad eccezione delle anteprime come `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` e `run_review` sono operazioni di manutenzione deterministiche e non richiedono credenziali del provider.

## Backend del client del modello

A partire da Co-op Translator 0.22.0, Azure OpenAI, OpenAI e Anthropic utilizzano Microsoft Agent Framework per impostazione predefinita. Non è necessario configurare il backend per l'uso normale.

Semantic Kernel rimane temporaneamente disponibile per compatibilità. Per selezionarlo esplicitamente, impostare:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

L'uso di Semantic Kernel genera un avviso di deprecazione. È previsto che il pacchetto sposti Semantic Kernel in una dipendenza opzionale nella versione 0.23.0 e rimuova l'integrazione in 0.24.0, subordinatamente ai risultati di compatibilità e al feedback degli utenti. Anthropic richiede `agent-framework`; la selezione esplicita di `semantic-kernel` con Anthropic fallisce con un errore di configurazione. Valori non validi causano un errore durante l'inizializzazione del traduttore supportato dal provider invece di ricadere silenziosamente su impostazioni alternative. Segui il rollout e segnala i blocchi in [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Usa Azure OpenAI quando il tuo modello è distribuito in Azure AI Foundry o Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Il controllo di connettività utilizza endpoint, chiave API, versione dell'API e nome della distribuzione prima dell'avvio della traduzione.

## OpenAI

Usa OpenAI quando chiami direttamente l'API di OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` è richiesto perché il traduttore necessita di un modello chat esplicito per le chiamate API.

Lascia `OPENAI_ORG_ID` e `OPENAI_BASE_URL` non impostati per la configurazione predefinita. Aggiungi un ID organizzazione solo se il tuo account ne ha bisogno, o un base URL solo quando usi un endpoint personalizzato. Non copiare valori segnaposto per le impostazioni opzionali.

## Anthropic Claude

Usa Anthropic quando chiami direttamente l'API Claude. Crea una [Chiave API Anthropic](https://platform.claude.com/docs/en/get-started) e scegli un [ID modello Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) supportato.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` e `ANTHROPIC_MODEL` sono richiesti. Non è necessario impostare `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework è il backend predefinito.

Lascia `ANTHROPIC_BASE_URL` non impostato per l'API Anthropic. Impostalo solo quando usi un endpoint personalizzato.

`ANTHROPIC_MAX_TOKENS` è impostato di default su `8192`, il che lascia spazio per script con alta densità di token come Meitei Mayek. Abbassalo se il tuo modello o un endpoint compatibile con Anthropic limita l'output a un valore inferiore.

## Azure AI Vision

La traduzione delle immagini richiede Azure AI Vision in modo che lo strumento possa estrarre il testo dalle immagini prima che il modello linguistico configurato lo traduca. Anthropic può tradurre il testo estratto proprio come Azure OpenAI o OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Se la traduzione delle immagini è selezionata con `-img`, `images=True` o senza filtro di tipo di contenuto, lo strumento valida la configurazione di Vision prima dell'inizio della traduzione.

## Più set di credenziali

Il livello di configurazione supporta più set di credenziali aggiungendo un suffisso con lo stesso indice alle variabili:

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

Ogni set deve essere completo. Il controllo di integrità seleziona un set funzionante prima che la traduzione proceda.

OpenAI e Anthropic supportano la stessa convenzione di suffisso. Mantieni ogni variabile in un set di credenziali con lo stesso suffisso, comprese i valori opzionali come `OPENAI_BASE_URL_1` o `ANTHROPIC_BASE_URL_1`.

## Requisiti dei comandi

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Sì | No | Traduce solo Markdown. |
| `translate -nb` | Sì | No | Traduce solo notebook. |
| `translate -img` | Sì | Sì | Traduce solo immagini. |
| `translate` with no type flags | Sì | Sì | La modalità predefinita include Markdown, notebook e immagini. |
| `evaluate` | Sì | No | Utilizza la valutazione LLM a meno che non sia selezionato `--fast`. |
| `migrate-links` | No | No | Esegue la migrazione locale dei link senza chiamate al provider. |
| `co-op-review` | No | No | Esegue controlli deterministici sulla struttura di traduzione, sulla freschezza, su Markdown, su notebook e sui link locali. |
| `run_translation(markdown=True)` | Sì | No | Traduzione Markdown programmatica. |
| `run_translation(images=True)` | Sì | Sì | Traduzione di immagini programmatica. |
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