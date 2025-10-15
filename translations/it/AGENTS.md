<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:26:24+00:00",
  "source_file": "AGENTS.md",
  "language_code": "it"
}
-->
## Panoramica del progetto

Co‑op Translator è uno strumento da riga di comando Python e un workflow GitHub Actions che traduce file Markdown, notebook Jupyter e testo contenuto nelle immagini in più lingue. Organizza gli output in cartelle specifiche per lingua e mantiene le traduzioni sincronizzate con il contenuto originale. Il progetto è strutturato come una libreria gestita con Poetry con punti di ingresso CLI.

### Panoramica dell’architettura

- I punti di ingresso CLI (`translate`, `migrate-links`, `evaluate`) richiamano una CLI unificata che gestisce i flussi di traduzione, migrazione dei link e valutazione.
- Il loader di configurazione legge il file `.env` e rileva automaticamente il provider LLM (Azure OpenAI o OpenAI) e, se richiesto, il provider vision (Azure AI Service) per l’estrazione del testo dalle immagini.
- Il core di traduzione gestisce Markdown e notebook; la pipeline vision estrae testo dalle immagini quando si usa l’opzione `-img`.
- Gli output vengono organizzati in `translations/<lang>/` per il testo e `translated_images/` per le immagini, mantenendo la struttura originale.

### Tecnologie e framework principali

- Python 3.10–3.12, Poetry per il packaging
- CLI: `click`
- SDK LLM/AI: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP e dati: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Strumenti: `pytest`, `black`, `ruff`

## Comandi di configurazione

### Prerequisiti

- Python 3.10–3.12
- Abbonamento Azure (opzionale, per servizi Azure AI)
- Connessione Internet per le API LLM/Vision (es. Azure OpenAI/OpenAI, Azure AI Vision)

### Opzione A: Poetry (consigliata)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opzione B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Utilizzo per l’utente finale

### Docker (immagine pubblicata)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Note:
- Il punto di ingresso predefinito è `translate`. Sovrascrivi con `--entrypoint migrate-links` per la migrazione dei link.
- Assicurati che la visibilità del pacchetto GHCR sia Pubblica per i pull anonimi.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Configurazione dell’ambiente

Crea un file `.env` nella radice del repository e inserisci le credenziali/endpoint per il modello linguistico scelto e (opzionalmente) per il servizio vision. Per la configurazione specifica del provider, consulta `getting_started/set-up-azure-ai.md`.

### Variabili d’ambiente richieste

Almeno un provider LLM deve essere configurato. Per la traduzione delle immagini, è necessario configurare anche Azure AI Service.

- Azure OpenAI (traduzione testo):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa per traduzione testo):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opzionale)
  - `OPENAI_CHAT_MODEL_ID` (richiesto se si usa il provider OpenAI)
  - `OPENAI_BASE_URL` (opzionale; default `https://api.openai.com/v1`)

- Azure AI Service per estrazione testo da immagini (richiesto con `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferito) o il vecchio `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Esempio di snippet `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Note:

- Lo strumento rileva automaticamente il provider LLM disponibile; configura Azure OpenAI o OpenAI.
- La traduzione delle immagini richiede sia `AZURE_AI_SERVICE_API_KEY` che `AZURE_AI_SERVICE_ENDPOINT`.
- La CLI segnalerà chiaramente se mancano variabili richieste.

## Workflow di sviluppo

- Il codice sorgente si trova in `src/co_op_translator`; i test in `tests/`.
- CLI principali (installate tramite entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Consulta la documentazione aggiuntiva in `getting_started/`.

## Istruzioni per i test

Esegui i test dalla radice del repository. Alcuni test potrebbero richiedere credenziali API; salta quelli se necessario.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Copertura opzionale (richiede `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Linee guida per lo stile del codice

- Formatter: Black (configurato in `pyproject.toml`, lunghezza linea 88)
- Linter: Ruff (configurato in `pyproject.toml`, lunghezza linea 120)
- Controlli di tipo: mypy (configurazione presente; attiva se installato)

Comandi:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizza i sorgenti Python sotto `src/`, i test sotto `tests/`, e preferisci import espliciti all’interno dello spazio dei nomi del pacchetto (`co_op_translator.*`).

## Build e distribuzione

Gli artefatti di build vengono pubblicati in `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

L’automazione tramite GitHub Actions è supportata; vedi:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Immagine container (GHCR)

- Immagine ufficiale: `ghcr.io/azure/co-op-translator:<tag>`
- Tag: `latest` (su main), tag semantici come `vX.Y.Z`, e un tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` supportati tramite Buildx
- Pattern Dockerfile: costruisci le dipendenze wheel nel builder (con `build-essential` e `python3-dev`) e installa dalla wheelhouse locale nel runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` costruisce e pubblica su GHCR

## Considerazioni sulla sicurezza

- Conserva le chiavi API e gli endpoint nel file `.env` o nello store dei segreti del CI; non committare mai segreti.
- Per la traduzione delle immagini, sono richiesti chiavi/endpoint Azure AI Vision; altrimenti ometti `-img`.
- Verifica le quote/limiti del provider quando esegui batch di traduzione di grandi dimensioni.

## Linee guida per le Pull Request

### Prima di inviare

1. **Testa le tue modifiche:**
   - Esegui completamente i notebook interessati
   - Verifica che tutte le celle vengano eseguite senza errori
   - Controlla che gli output siano corretti

2. **Aggiornamenti alla documentazione:**
   - Aggiorna `README.md` se aggiungi nuovi concetti
   - Aggiungi commenti nei notebook per codice complesso
   - Assicurati che le celle markdown spieghino lo scopo

3. **Modifiche ai file:**
   - Evita di committare file `.env` (usa `.env.example`)
   - Non committare le directory `venv/` o `__pycache__/`
   - Mantieni gli output dei notebook quando dimostrano concetti
   - Rimuovi file temporanei e notebook di backup (`*-backup.ipynb`)

4. **Stile e formattazione:**
   - Segui le linee guida di stile e formattazione
   - Esegui `poetry run black .` e `poetry run ruff check .` per verificare problemi di stile e formattazione

5. **Aggiungi/aggiorna test e help CLI:**
   - Aggiungi o aggiorna i test quando cambi il comportamento
   - Mantieni l’help della CLI coerente con le modifiche


### Messaggio di commit e strategia di merge

Usiamo Squash and Merge come default. Il messaggio finale del commit squash deve seguire:

```bash
<type>: <description> (#<PR number>)
```

Tipi consentiti:
- `Docs` — aggiornamenti alla documentazione
- `Build` — sistema di build, dipendenze, configurazione/CI
- `Core` — funzionalità e caratteristiche principali (es. `src/co_op_translator/core`)

Esempi:
- `Docs: Aggiorna istruzioni di installazione per chiarezza (#50)`
- `Core: Migliora la gestione della traduzione immagini (#60)`

Note:
- I titoli delle PR sono spesso auto-prefissati in base alle etichette; verifica che il prefisso generato sia corretto.

### Formato del titolo PR

Usa titoli chiari e concisi. Preferisci la stessa struttura del messaggio finale del commit squash:
- `Docs: Aggiorna istruzioni di installazione per chiarezza`
- `Core: Migliora la gestione della traduzione immagini`

## Debug e risoluzione dei problemi

- Problemi comuni e soluzioni: `getting_started/troubleshooting.md`
- Lingue supportate e note (inclusi font/problemi noti): `getting_started/supported-languages.md`
- Per problemi di link nei notebook, riesegui: `migrate-links -l "all" -y`

## Note per gli agenti

- Preferisci Poetry per ambienti riproducibili; altrimenti usa `requirements.txt`.
- Quando richiami le CLI nel CI, fornisci i segreti richiesti tramite variabili d’ambiente o iniezione `.env`.
- Per chi usa monorepo, questo repository funziona come pacchetto standalone; non è richiesta coordinazione tra sottopacchetti.

- Guida multi-arch: mantieni `linux/arm64` se ci sono utenti ARM (Apple Silicon/server ARM); altrimenti solo `linux/amd64` va bene per semplicità.
- Indirizza gli utenti alla sezione Docker Quick Start in `README.md` se preferiscono l’uso del container; includi varianti Bash e PowerShell per le differenze di quoting.

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.