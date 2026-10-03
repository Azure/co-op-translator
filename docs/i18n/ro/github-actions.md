# GitHub Actions

Folosiți GitHub Actions când doriți ca un depozit să traducă automat documentația modificată și să deschidă un pull request cu rezultatele generate.

Începeți cu configurarea standard `GITHUB_TOKEN`, inclusiv pentru depozitele organizației atunci când politica permite. Consultați [Configurare GitHub App](#github-app-setup) când organizația dumneavoastră necesită o identitate App sau aveți nevoie de execuții automate ale fluxului de lucru downstream.

**Human edits:** aceste fluxuri de lucru retraduce integral fișierele sursă modificate și pot suprascrie formulările editate în traducerile lor. Revizuiți fiecare PR înainte de a-l fuziona. Păstrarea la nivel de bloc Markdown a editărilor acceptate necesită o integrare personalizată cu [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Primul PR de traducere pentru README

Începeți cu un singur `README.md` rădăcină și o singură limbă țintă. Acest flux de lucru traduce doar Markdown, deci Azure AI Vision nu este necesar.

1. Copiați [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) în `.github/workflows/translate-readme.yml` în depozitul pe care doriți să îl traduceți și comiteți-l în ramura implicită a acelui depozit. Șablonul folosește Action-ul root din `Azure/co-op-translator@main`, care instalează CLI din aceeași referință sursă. Blocați un commit revizuit pentru rulări reproductibile.
2. Deschideți **Actions > Translate README > Run workflow**, alegeți o limbă și lăsați bifat **Preview only**. Revizuiți estimarea de token în pasul de previzualizare. Previzualizarea nu apelează furnizori de modele, nu scrie traduceri și nu creează un PR.
3. Adăugați secretele pentru un [furnizor de text](#prerequisites) și activați **Permiteți GitHub Actions să creeze și să aprobe pull request-uri** în **Setări > Acțiuni > General**. Șablonul solicită `contents: write` și `pull-requests: write` pentru jobul său; nu trebuie să modificați permisiunile implicite pentru fiecare flux de lucru. Dacă politica organizației blochează aceste permisiuni sau această setare, întrebați un administrator despre o [aplicație GitHub](#github-app-setup) aprobată.
4. Rulați din nou fluxul de lucru cu **Preview only** debifat. Acesta previzualizează, traduce, rulează `co-op-review --readme-only` și creează sau actualizează un PR de traducere doar după ce traducerea și revizuirea reușesc. Rezumatul fluxului de lucru conține un link către PR.
5. Revizuiți formularea și modificările fișierelor din PR, apoi fuzionați când sunteți gata. Fluxul de lucru nu fuzionează automat.

PR-ul conține doar `translations/<language>/README.md` și fișierul său de metadate pentru limbă. README-ul sursă rămâne neschimbat, iar linkurile către alte documente continuă să indice documentele sursă. Corpul PR-ului listează fișierele modificate și rezultatele revizuirii structurale. Dacă traducerea sau revizuirea eșuează, inspectați rezumatul fluxului de lucru și jurnalele pasului eșuat; nu se creează niciun PR. Dacă nu există modificări, nu este necesar niciun PR nou.

**Organization and CI note:** O GitHub App este opțională, nu o cerință legată de proprietatea organizației. Cu `GITHUB_TOKEN`, fluxurile de lucru pentru pull-request care deschid, actualizează sau redeschid un PR necesită un utilizator cu acces de scriere pentru a selecta **Approve workflows to run**. Fluxurile push nu sunt declanșate de acest token. Pentru CI downstream neasistat, vedeți [Configurare GitHub App](#github-app-setup) și regulile GitHub despre [declanșarea fluxurilor de lucru](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Cerințe prealabile

Înainte de a crea fluxul de lucru, configurați secretele serviciilor AI de care are nevoie rularea traducerii.

Traducerea textului necesită un furnizor de modele de limbaj:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, și, opțional, `OPENAI_ORG_ID` și `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, și, opțional, `ANTHROPIC_BASE_URL`

Traducerea imaginilor necesită, în plus, Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Consultați [Configuration](configuration.md) și [Azure AI Setup](azure-ai-setup.md) pentru detalii despre configurarea locală.

## Configurare standard

După ce testați fluxul de lucru pentru README, folosiți această configurație pentru a traduce fișierele Markdown ale unui depozit în mai multe limbi. Rulează o revizuire Markdown înainte de a deschide un PR și nu necesită Azure AI Vision.

### Pasul 1: Adăugați secretele depozitului

În depozitul țintă, deschideți **Settings** > **Secrets and variables** > **Actions**, apoi adăugați secretele furnizorului pe care fluxul de lucru le va folosi.

![Selectați secretele Actions](../../assets/github-actions/select-setting-action.png)

### Pasul 2: Activați permisiunile pentru fluxul de lucru

Deschideți **Settings** > **Actions** > **General**.

În secțiunea **Workflow permissions**:

1. Activați **Permiteți GitHub Actions să creeze și să aprobe pull request-uri**.
2. Salvați setarea.

Jobul de mai jos solicită explicit `contents: write` și `pull-requests: write`. Păstrați permisiunile implicite ale fluxului de lucru ale depozitului neschimbate. Dacă politica organizației blochează crearea PR-urilor, întrebați un administrator despre o [GitHub App](#github-app-setup) aprobată.

### Pasul 3: Adăugați fluxul de lucru

Creați `.github/workflows/co-op-translator.yml`:

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

Schimbați `TARGET_LANGUAGES` la limbile de care are nevoie proiectul dumneavoastră. Revizuirea folosește Python API pentru a verifica doar Markdown, potrivindu-se cu pasul de traducere. O eroare de traducere sau revizuire oprește jobul înainte de crearea PR-ului. Fluxul de lucru nu fuzionează PR-ul automat. Pentru depozite mari, adăugați un filtru `paths:` sub `on.push` astfel încât fluxul de lucru să ruleze doar când se schimbă documentația.

### Opțional: notebook-uri și imagini

Pentru notebook-uri, adăugați `-nb` la comanda de traducere și setați `notebook=True` în pasul de revizuire. Pentru textul din imagini, configurați cele două [secrete Azure AI Vision](#prerequisites), transmiteți-le în `env` al pasului de traducere, adăugați `-img` la comandă și includeți `translated_images/` în `add-paths` al pasului PR. Revizuiți imaginile traduse vizual; revizuirea deterministă nu certifică acuratețea textului din imagini sau a acurateței lingvistice.

## Configurare GitHub App

Folosiți o GitHub App aprobată atunci când organizația dumneavoastră cere o identitate App sau când PR-ul generat trebuie să declanșeze CI downstream fără pasul de aprobare `GITHUB_TOKEN`. O App nu ocolește politica organizației; administratorii controlează în continuare instalarea și permisiunile acesteia.

### Pasul 1: Creați sau instalați o GitHub App

Folosiți o App existentă furnizată de organizație când este disponibilă sau creați una cu acces de citire/scriere la **Contents** și **Pull requests**. Instalați-o pe depozitul țintă cu orice aprobare necesară din partea organizației.

Înregistrați:

- ID-ul aplicației
- Conținutul cheii private

Stocați-le ca secrete ale depozitului:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Pasul 2: Generați un token pentru App

Adăugați acest pas imediat înainte de pasul existent de pull request. Pentru șablonul README, utilizați aceeași condiție de succes astfel încât previzualizările și traducerile eșuate să nu ceară un token App:

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

Apoi schimbați doar inputul `token` al pasului existent de pull request la `${{ steps.generate_token.outputs.token }}`. Păstrați condiția sa de succes, ramura, corpul PR-ului și `add-paths` neschimbate. Tokenul este limitat implicit la depozitul curent. Când adaptați configurația standard în locul șablonului README, omiteți `if` de mai sus: acel flux de lucru folosește condiția de succes implicită, astfel încât crearea tokenului și crearea PR-ului rulează doar după ce traducerea și revizuirea reușesc.

Consultați acțiunea oficială [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) pentru instalare și permisiunile tokenului.

## Limitări ale runner-ului

Runner-ii găzduiți de GitHub au o durată maximă a jobului. Depozitele mari sau multe limbi țintă pot depăși acel limită.

Pentru volume mari de traducere:

- Traduceți un număr mai mic de limbi per execuție.
- Utilizați flag-uri de conținut, cum ar fi `-md`, `-nb` sau `-img`.
- Folosiți un runner self-hosted când dimensiunea depozitului sau latența modelului face ca runner-ii găzduiți să fie nesiguri.

## Revizuire în CI

Folosiți `co-op-review` când un pull request ar trebui să valideze traducerile generate fără a apela furnizori LLM sau Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` este o comandă de revizuire deterministă beta. Verificările și schema de ieșire se pot modifica, dar este proiectată să fie sigură pentru CI deoarece nu scrie fișiere și nu apelează furnizori de modele.