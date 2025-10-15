<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:06:04+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "it"
}
-->
# Utilizzo dell’azione GitHub Co-op Translator (Guida per l’organizzazione)

**Destinatari:** Questa guida è pensata per **utenti interni Microsoft** o **team che hanno accesso alle credenziali necessarie per l’app GitHub Co-op Translator preconfigurata** oppure che possono creare una propria app GitHub personalizzata.

Automatizza la traduzione della documentazione del tuo repository in modo semplice con l’azione GitHub Co-op Translator. Questa guida ti accompagna nella configurazione dell’azione per creare automaticamente pull request con le traduzioni aggiornate ogni volta che i tuoi file Markdown sorgente o le immagini vengono modificati.

> [!IMPORTANT]
> 
> **Scegliere la guida giusta:**
>
> Questa guida spiega la configurazione tramite **GitHub App ID e chiave privata**. Di solito serve questo metodo “Guida per l’organizzazione” se: **`GITHUB_TOKEN` con permessi limitati:** Le impostazioni della tua organizzazione o del repository limitano i permessi predefiniti concessi al `GITHUB_TOKEN` standard. In particolare, se il `GITHUB_TOKEN` non ha i permessi necessari di `write` (come `contents: write` o `pull-requests: write`), il workflow nella [Guida pubblica](./github-actions-guide-public.md) fallirà per mancanza di permessi. Usare una GitHub App dedicata con permessi espliciti supera questa limitazione.
>
> **Se quanto sopra non ti riguarda:**
>
> Se il `GITHUB_TOKEN` standard ha permessi sufficienti nel tuo repository (cioè non sei bloccato da restrizioni organizzative), usa la **[Guida pubblica con GITHUB_TOKEN](./github-actions-guide-public.md)**. La guida pubblica non richiede App ID o chiavi private e si basa solo sul `GITHUB_TOKEN` standard e sui permessi del repository.

## Prerequisiti

Prima di configurare l’azione GitHub, assicurati di avere pronte le credenziali del servizio AI necessario.

**1. Obbligatorio: Credenziali del modello linguistico AI**
Ti servono le credenziali per almeno uno dei modelli linguistici supportati:

- **Azure OpenAI**: Richiede Endpoint, API Key, nomi di modello/distribuzione, versione API.
- **OpenAI**: Richiede API Key, (Opzionale: Org ID, Base URL, Model ID).
- Consulta [Modelli e servizi supportati](../../../../README.md) per i dettagli.
- Guida alla configurazione: [Configura Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Opzionale: Credenziali Computer Vision (per traduzione immagini)**

- Necessarie solo se vuoi tradurre testo all’interno delle immagini.
- **Azure Computer Vision**: Richiede Endpoint e Subscription Key.
- Se non fornite, l’azione userà la [modalità solo Markdown](../markdown-only-mode.md).
- Guida alla configurazione: [Configura Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Configurazione

Segui questi passaggi per configurare l’azione GitHub Co-op Translator nel tuo repository:

### Passo 1: Installa e configura l’autenticazione tramite GitHub App

Il workflow usa l’autenticazione tramite GitHub App per interagire in modo sicuro con il tuo repository (ad esempio, per creare pull request) per tuo conto. Scegli una delle opzioni:

#### **Opzione A: Installa l’app GitHub Co-op Translator preconfigurata (solo per uso interno Microsoft)**

1. Vai alla pagina della [GitHub App Co-op Translator](https://github.com/apps/co-op-translator).

1. Seleziona **Install** e scegli l’account o l’organizzazione dove si trova il repository di destinazione.

    ![Installa app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.it.png)

1. Scegli **Only select repositories** e seleziona il repository di destinazione (es. `PhiCookBook`). Clicca su **Install**. Potresti dover autenticarti.

    ![Autorizza installazione](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.it.png)

1. **Ottieni le credenziali dell’app (processo interno):** Per permettere al workflow di autenticarsi come app, ti servono due informazioni fornite dal team Co-op Translator:
  - **App ID:** L’identificatore unico dell’app Co-op Translator. L’App ID è: `1164076`.
  - **Chiave privata:** Devi ottenere **l’intero contenuto** del file `.pem` della chiave privata dal referente. **Tratta questa chiave come una password e conservala in modo sicuro.**

1. Passa al Passo 2.

#### **Opzione B: Usa una tua GitHub App personalizzata**

- Se preferisci, puoi creare e configurare una tua GitHub App. Assicurati che abbia accesso in lettura e scrittura a Contents e Pull requests. Ti serviranno il suo App ID e una chiave privata generata.

### Passo 2: Configura i segreti del repository

Devi aggiungere le credenziali della GitHub App e del servizio AI come segreti criptati nelle impostazioni del repository.

1. Vai al repository GitHub di destinazione (es. `PhiCookBook`).

1. Vai su **Settings** > **Secrets and variables** > **Actions**.

1. Sotto **Repository secrets**, clicca su **New repository secret** per ciascun segreto elencato qui sotto.

   ![Seleziona impostazioni azioni](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.it.png)

**Segreti richiesti (per autenticazione GitHub App):**

| Nome segreto         | Descrizione                                      | Fonte valore                                     |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | L’App ID della GitHub App (dal Passo 1).         | Impostazioni GitHub App                          |
| `GH_APP_PRIVATE_KEY` | **Tutto il contenuto** del file `.pem` scaricato. | File `.pem` (dal Passo 1)                        |

**Segreti servizio AI (aggiungi TUTTI quelli necessari in base ai prerequisiti):**

| Nome segreto                         | Descrizione                               | Fonte valore                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Chiave per Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint per Azure AI Service (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Chiave per Azure OpenAI service           | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint per Azure OpenAI service         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Nome del tuo modello Azure OpenAI         | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Nome della distribuzione Azure OpenAI     | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Versione API per Azure OpenAI             | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API Key per OpenAI                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | ID organizzazione OpenAI                  | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | ID modello specifico OpenAI               | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | Base URL API personalizzata OpenAI        | OpenAI Platform                    |

![Inserisci nome variabile ambiente](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.it.png)

### Passo 3: Crea il file workflow

Infine, crea il file YAML che definisce il workflow automatico.

1. Nella directory principale del repository, crea la cartella `.github/workflows/` se non esiste.

1. All’interno di `.github/workflows/`, crea un file chiamato `co-op-translator.yml`.

1. Incolla il seguente contenuto in co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **Personalizza il workflow:**
  - **[!IMPORTANT] Lingue di destinazione:** Nel passaggio `Run Co-op Translator`, **DEVI controllare e modificare la lista dei codici lingua** nel comando `translate -l "..." -y` in base alle esigenze del tuo progetto. La lista di esempio (`ar de es...`) va sostituita o adattata.
  - **Trigger (`on:`):** Il trigger attuale avvia il workflow ad ogni push su `main`. Per repository grandi, valuta di aggiungere un filtro `paths:` (vedi esempio commentato nel YAML) per eseguire il workflow solo quando cambiano i file rilevanti (es. documentazione sorgente), risparmiando minuti di esecuzione.
  - **Dettagli PR:** Personalizza `commit-message`, `title`, `body`, nome del `branch` e `labels` nel passaggio `Create Pull Request` se necessario.

## Gestione e rinnovo delle credenziali

- **Sicurezza:** Conserva sempre le credenziali sensibili (API key, chiavi private) come segreti di GitHub Actions. Non esporle mai nel file workflow o nel codice del repository.
- **[!IMPORTANT] Rinnovo chiavi (utenti Microsoft interni):** Tieni presente che la chiave Azure OpenAI usata internamente in Microsoft potrebbe avere una politica di rinnovo obbligatorio (es. ogni 5 mesi). Assicurati di aggiornare i segreti GitHub corrispondenti (`AZURE_OPENAI_...`) **prima della scadenza** per evitare errori nel workflow.

## Esecuzione del workflow

> [!WARNING]  
> **Limite di tempo runner GitHub-hosted:**  
> I runner GitHub-hosted come `ubuntu-latest` hanno un **limite massimo di esecuzione di 6 ore**.  
> Per repository di documentazione molto grandi, se il processo di traduzione supera le 6 ore, il workflow verrà terminato automaticamente.  
> Per evitarlo, valuta:  
> - L’uso di un **runner self-hosted** (senza limiti di tempo)  
> - La riduzione del numero di lingue di destinazione per ogni esecuzione

Una volta che il file `co-op-translator.yml` è stato inserito nel tuo branch principale (o nel branch specificato nel trigger `on:`), il workflow si avvierà automaticamente ogni volta che vengono apportate modifiche a quel branch (e corrispondono al filtro `paths`, se configurato).

Se vengono generate o aggiornate traduzioni, l’azione creerà automaticamente una Pull Request con le modifiche, pronta per la revisione e la fusione.

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.