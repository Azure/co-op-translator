# GitHub Actions

Usa GitHub Actions quando vuoi che un repository traduca automaticamente la documentazione modificata e apra una pull request con i risultati generati.

Inizia con la configurazione standard `GITHUB_TOKEN`, anche per i repository dell'organizzazione quando la policy lo consente. Consulta [Configurazione dell'App GitHub](#github-app-setup) quando la tua organizzazione richiede un'identità App o hai bisogno di esecuzioni automatiche dei workflow a valle.

**Modifiche manuali:** questi workflow retradurranno completamente i file sorgente modificati e possono sovrascrivere la formulazione modificata nelle loro traduzioni. Revisiona ogni PR prima di eseguire il merge. La preservazione a livello di blocco Markdown delle modifiche accettate richiede un'integrazione personalizzata con il [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## La tua prima PR di traduzione del README

Inizia con un unico file root `README.md` e una lingua di destinazione. Questo workflow traduce solo Markdown, quindi Azure AI Vision non è necessario.

1. Copia [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([visualizza il template su GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) in `.github/workflows/translate-readme.yml` nel repository che vuoi tradurre e committalo nel branch predefinito di quel repository. Il template usa l'Action root in `Azure/co-op-translator@main`, che installa la CLI dallo stesso ref di origine. Esegui il pin di un commit revisionato per esecuzioni riproducibili.
2. Apri **Actions > Translate README > Run workflow**, scegli una lingua e lascia selezionata l'opzione **Preview only**. Controlla la stima dei token nel passaggio di anteprima. L'anteprima non chiama i provider di modelli, non scrive traduzioni né crea una PR.
3. Aggiungi i secret per un [provider di testo](#prerequisites), e abilita **Consenti a GitHub Actions di creare e approvare pull request** in **Impostazioni > Azioni > Generale**. Il template richiede `contents: write` e `pull-requests: write` per il suo job; non è necessario modificare le autorizzazioni predefinite per ogni workflow. Se la policy dell'organizzazione blocca queste autorizzazioni o questa impostazione, chiedi a un amministratore di un [GitHub App](#github-app-setup) approvato.
4. Esegui di nuovo il workflow con **Preview only** deselezionato. Esegue l'anteprima, traduce, esegue `co-op-review --readme-only` e crea o aggiorna una PR di traduzione solo dopo che traduzione e revisione sono andate a buon fine. Il riepilogo del workflow include un link alla PR.
5. Revisiona la formulazione e le modifiche ai file nella PR, quindi esegui il merge quando sei pronto. Il workflow non effettua il merge automaticamente.

La PR contiene solo `translations/<language>/README.md` e il suo file di metadati della lingua. Il README sorgente rimane invariato e i link ad altri documenti continuano a puntare ai documenti sorgente. Il body della PR elenca i file modificati e i risultati della revisione strutturale. Se la traduzione o la revisione falliscono, controlla il riepilogo del workflow e i log dei passaggi falliti; non viene creata alcuna PR. Se non ci sono modifiche, non è necessaria una nuova PR.

**Nota su organizzazione e CI:** Un GitHub App è opzionale, non un requisito della proprietà dell'organizzazione. Con `GITHUB_TOKEN`, i workflow sulle pull request per aprire, aggiornare o riaprire una PR richiedono che un utente con accesso in scrittura selezioni **Approve workflows to run**. I workflow di push non vengono attivati da questo token. Per CI a valle non presidiata, consulta [Configurazione dell'App GitHub](#github-app-setup) e le [regole di attivazione dei workflow](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) di GitHub.

## Prerequisiti

Prima di creare il workflow, configura i secret dei servizi AI necessari alla tua esecuzione di traduzione.

La traduzione di testo richiede un provider di modelli linguistici:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

La traduzione delle immagini richiede inoltre Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

See [Configuration](configuration.md) and [Azure AI Setup](azure-ai-setup.md) for local configuration details.

## Configurazione standard

Dopo aver provato il workflow per il README, usa questa configurazione per tradurre i file Markdown di un repository in più lingue. Esegue una revisione Markdown prima di aprire una PR e non richiede Azure AI Vision.

### Passaggio 1: Aggiungi i secret del repository

Nel repository di destinazione, apri **Settings** > **Secrets and variables** > **Actions**, quindi aggiungi i secret del provider che il tuo workflow utilizzerà.

![Seleziona i secret di Actions](../../assets/github-actions/select-setting-action.png)

### Passaggio 2: Abilita le autorizzazioni del workflow

Apri **Settings** > **Actions** > **General**.

Sotto **Workflow permissions**:

1. Abilita **Consenti a GitHub Actions di creare e approvare pull request**.
2. Salva l'impostazione.

Il job qui sotto richiede esplicitamente `contents: write` e `pull-requests: write`. Mantieni inalterate le autorizzazioni predefinite dei workflow del repository. Se la policy dell'organizzazione impedisce la creazione di PR, chiedi a un amministratore informazioni su un [GitHub App](#github-app-setup) approvato.

### Passaggio 3: Aggiungi il workflow

Crea `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Modifica `TARGET_LANGUAGES` con le lingue necessarie al tuo progetto. La revisione utilizza la Python API per verificare solo Markdown, in linea con il passaggio di traduzione. Un errore di traduzione o revisione ferma il job prima della creazione della PR. Il workflow non esegue il merge della PR automaticamente. Per repository di grandi dimensioni, aggiungi un filtro `paths:` sotto `on.push` in modo che il workflow venga eseguito solo quando cambiano i documenti.

### Opzionale: notebook e immagini

Per i notebook, aggiungi `-nb` al comando di traduzione e imposta `notebook=True` nel passaggio di revisione. Per il testo nelle immagini, configura i due [Azure AI Vision secrets](#prerequisites), passali nell'`env` del passaggio di traduzione, aggiungi `-img` al comando e aggiungi `translated_images/` all'`add-paths` del passaggio PR. Revisiona le immagini tradotte visivamente; la revisione deterministica non certifica il testo nell'immagine né l'accuratezza linguistica.

## Configurazione dell'App GitHub

Usa un GitHub App approvato quando la tua organizzazione richiede un'identità App, o quando la PR generata deve attivare CI a valle senza il passaggio di approvazione del `GITHUB_TOKEN`. Un'App non bypassa la policy dell'organizzazione; gli amministratori controllano comunque la sua installazione e le autorizzazioni.

### Passaggio 1: Crea o installa un GitHub App

Usa un'App fornita dall'organizzazione quando disponibile, oppure creane una con accesso in lettura/scrittura a **Contents** e **Pull requests**. Installala nel repository di destinazione con le eventuali approvazioni richieste dall'organizzazione.

Annota:

- App ID
- Contenuto della chiave privata

Conservali come secret del repository:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Passaggio 2: Genera un token dell'App

Aggiungi questo passaggio immediatamente prima del passaggio esistente della pull request. Per il template del README, usa la stessa condizione di successo in modo che anteprime e traduzioni fallite non richiedano un token dell'App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Poi modifica solo l'input `token` del passaggio esistente della pull request in `${{ steps.generate_token.outputs.token }}`. Mantieni invariati la sua condizione di successo, il branch, il body della PR e gli `add-paths`. Il token è limitato al repository corrente per impostazione predefinita. Quando adatti la configurazione standard invece del template README, ometti l'`if` sopra: quel workflow usa la condizione di successo predefinita, quindi la creazione del token e la creazione della PR vengono eseguite solo dopo che traduzione e revisione hanno avuto successo.

Consulta l'[Action create-github-app-token](https://github.com/actions/create-github-app-token/tree/v2) ufficiale per informazioni su installazione e permessi del token.

## Limiti dei runner

I runner ospitati da GitHub hanno una durata massima per job. Repository di grandi dimensioni o molte lingue di destinazione possono superare tale limite.

Per carichi di lavoro di traduzione elevati:

- Traduci meno lingue per esecuzione.
- Usa flag di contenuto come `-md`, `-nb` o `-img`.
- Usa un runner self-hosted quando la dimensione del repository o la latenza dei modelli rendono i runner ospitati poco affidabili.

## Revisione in CI

Usa `co-op-review` quando una pull request dovrebbe convalidare le traduzioni generate senza chiamare provider LLM o Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` è un comando di revisione deterministica in beta. I suoi controlli e lo schema di output possono evolvere, ma è progettato per essere sicuro per la CI perché non scrive file né chiama provider di modelli.