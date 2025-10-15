<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:06:23+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "it"
}
-->
# Utilizzo della GitHub Action Co-op Translator (Configurazione Pubblica)

**Destinatari:** Questa guida è pensata per utenti nella maggior parte dei repository pubblici o privati dove le autorizzazioni standard di GitHub Actions sono sufficienti. Utilizza il `GITHUB_TOKEN` integrato.

Automatizza la traduzione della documentazione del tuo repository in modo semplice con la GitHub Action Co-op Translator. Questa guida ti accompagna nella configurazione dell’action per creare automaticamente pull request con traduzioni aggiornate ogni volta che i tuoi file Markdown sorgente o le immagini vengono modificati.

> [!IMPORTANT]
>
> **Scegliere la guida giusta:**
>
> Questa guida spiega la **configurazione più semplice usando il `GITHUB_TOKEN` standard**. È il metodo consigliato per la maggior parte degli utenti perché non richiede la gestione di chiavi private sensibili di GitHub App.
>

## Prerequisiti

Prima di configurare la GitHub Action, assicurati di avere pronti le credenziali del servizio AI necessario.

**1. Obbligatorio: Credenziali del Modello Linguistico AI**
Hai bisogno delle credenziali per almeno uno dei modelli linguistici supportati:

- **Azure OpenAI**: Richiede Endpoint, API Key, Nomi di Modello/Deployment, Versione API.
- **OpenAI**: Richiede API Key, (Opzionale: Org ID, Base URL, Model ID).
- Consulta [Modelli e Servizi Supportati](../../../../README.md) per i dettagli.

**2. Opzionale: Credenziali AI Vision (per la traduzione delle immagini)**

- Necessarie solo se vuoi tradurre il testo all’interno delle immagini.
- **Azure AI Vision**: Richiede Endpoint e Subscription Key.
- Se non fornite, l’action funzionerà in [modalità solo Markdown](../markdown-only-mode.md).

## Configurazione

Segui questi passaggi per configurare la GitHub Action Co-op Translator nel tuo repository usando il `GITHUB_TOKEN` standard.

### Passo 1: Comprendere l’Autenticazione (Uso di `GITHUB_TOKEN`)

Questo workflow utilizza il `GITHUB_TOKEN` integrato fornito da GitHub Actions. Questo token concede automaticamente i permessi necessari al workflow per interagire con il tuo repository in base alle impostazioni configurate nel **Passo 3**.

### Passo 2: Configurare i Segreti del Repository

Devi solo aggiungere le **credenziali del servizio AI** come segreti criptati nelle impostazioni del tuo repository.

1.  Vai al repository GitHub di destinazione.
2.  Vai su **Settings** > **Secrets and variables** > **Actions**.
3.  Sotto **Repository secrets**, clicca su **New repository secret** per ogni segreto richiesto elencato qui sotto.

    ![Seleziona impostazione action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.it.png) *(Riferimento immagine: mostra dove aggiungere i segreti)*

**Segreti richiesti per i servizi AI (Aggiungi TUTTI quelli che servono in base ai tuoi Prerequisiti):**

| Nome Segreto                         | Descrizione                               | Fonte Valore                     |
| :----------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`           | Chiave per Azure AI Service (Computer Vision)  | Il tuo Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`          | Endpoint per Azure AI Service (Computer Vision) | Il tuo Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`               | Chiave per Azure OpenAI service              | Il tuo Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint per Azure OpenAI service         | Il tuo Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`            | Nome del tuo modello Azure OpenAI         | Il tuo Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Nome del deployment Azure OpenAI          | Il tuo Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`           | Versione API per Azure OpenAI             | Il tuo Azure AI Foundry               |
| `OPENAI_API_KEY`                     | API Key per OpenAI                        | La tua piattaforma OpenAI             |
| `OPENAI_ORG_ID`                      | ID Organizzazione OpenAI (Opzionale)      | La tua piattaforma OpenAI             |
| `OPENAI_CHAT_MODEL_ID`               | ID modello OpenAI specifico (Opzionale)   | La tua piattaforma OpenAI             |
| `OPENAI_BASE_URL`                    | Base URL API OpenAI personalizzata (Opzionale) | La tua piattaforma OpenAI             |

### Passo 3: Configurare i Permessi del Workflow

La GitHub Action necessita dei permessi concessi tramite il `GITHUB_TOKEN` per effettuare il checkout del codice e creare pull request.

1.  Nel tuo repository, vai su **Settings** > **Actions** > **General**.
2.  Scorri fino alla sezione **Workflow permissions**.
3.  Seleziona **Read and write permissions**. Questo concede al `GITHUB_TOKEN` i permessi necessari `contents: write` e `pull-requests: write` per questo workflow.
4.  Assicurati che la casella **Allow GitHub Actions to create and approve pull requests** sia **selezionata**.
5.  Clicca su **Save**.

![Impostazione permessi](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.it.png)

### Passo 4: Crea il File del Workflow

Infine, crea il file YAML che definisce il workflow automatizzato usando `GITHUB_TOKEN`.

1.  Nella directory principale del tuo repository, crea la cartella `.github/workflows/` se non esiste già.
2.  All’interno di `.github/workflows/`, crea un file chiamato `co-op-translator.yml`.
3.  Incolla il seguente contenuto in `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Personalizza il Workflow:**
  - **[!IMPORTANT] Lingue di destinazione:** Nel passaggio `Run Co-op Translator`, **DEVI controllare e modificare la lista dei codici lingua** all’interno del comando `translate -l "..." -y` per adattarla alle esigenze del tuo progetto. La lista di esempio (`ar de es...`) va sostituita o aggiornata.
  - **Trigger (`on:`):** Il trigger attuale si attiva ad ogni push su `main`. Per repository grandi, valuta di aggiungere un filtro `paths:` (vedi esempio commentato nello YAML) per eseguire il workflow solo quando cambiano i file rilevanti (es. documentazione sorgente), risparmiando minuti di esecuzione.
  - **Dettagli PR:** Personalizza il `commit-message`, `title`, `body`, nome del `branch` e le `labels` nel passaggio `Create Pull Request` se necessario.

## Esecuzione del Workflow

> [!WARNING]  
> **Limite di tempo dei runner GitHub-hosted:**  
> I runner GitHub-hosted come `ubuntu-latest` hanno un **limite massimo di esecuzione di 6 ore**.  
> Per repository di documentazione molto grandi, se il processo di traduzione supera le 6 ore, il workflow verrà terminato automaticamente.  
> Per evitarlo, valuta:  
> - L’uso di un **runner self-hosted** (senza limiti di tempo)  
> - La riduzione del numero di lingue di destinazione per ogni esecuzione

Una volta che il file `co-op-translator.yml` è stato inserito nel tuo branch principale (o nel branch specificato nel trigger `on:`), il workflow verrà eseguito automaticamente ogni volta che vengono apportate modifiche a quel branch (e corrispondono al filtro `paths`, se configurato).

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.