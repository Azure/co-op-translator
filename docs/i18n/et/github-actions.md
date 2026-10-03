# GitHub Actions

Kasutage GitHub Actionsi, kui soovite, et hoidla tõlgiks muudetud dokumentatsiooni automaatselt ja avaks genereeritud väljundiga pull requesti.

Alustage tavalise `GITHUB_TOKEN` seadistusega, ka organisatsiooni hoidlate puhul, kui poliitika seda lubab. Vaadake [GitHub rakenduse seadistus](#github-app-setup), kui teie organisatsioon nõuab rakenduse identiteeti või vajate automaatseid alluvate töövoogude käivitusi.

**Inimese tehtud muudatused:** need töövood tõlgivad muudetud lähtefaile täielikult uuesti ja võivad kirjutada üle nende tõlgetes tehtud sõnastuse muutused. Kontrollige iga PR-i enne ühendamist. Heakskiidetud muudatuste Markdowni plokitaseme säilitamiseks on vajalik kohandatud integratsioon [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Teie esimene README tõlke-PR

Alustage ühest juurfailist `README.md` ja ühest sihtkeelest. See töövoog tõlgib ainult Markdownit, seega Azure AI Vision pole vajalik.

1. Kopeerige [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([vaadake malli GitHubis](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) faili `.github/workflows/translate-readme.yml` hoidlas, mida soovite tõlkida, ja committige see selle hoidla vaikesharusse. Mall kasutab põhitoimingu versiooni `Azure/co-op-translator@main`, mis installeerib CLI sama allikaviite alusel. Valige ülevaadatud commit korduvajooksude reprodutseeritavuse tagamiseks.
2. Avage **Actions > Translate README > Run workflow**, valige keel ja jätke **Preview only** märgitud. Vaadake eelvaate sammus tokenite hinnang üle. Eelvaade ei kutsu mudeli pakkujaid, ei kirjuta tõlkeid ega loo PR-i.
3. Lisage saladused ühe [tekstipakkuja](#prerequisites) jaoks ja lubage **GitHub Actionsil luua ja heaks kiita pull requeste** asukohas **Seaded > Actions > Üldine**. Mall palub oma töö jaoks `contents: write` ja `pull-requests: write`; te ei pea vaikimisi õigusi iga töövoo jaoks muutma. Kui organisatsiooni poliitika blokeerib need õigused või selle sätte, küsige administraatorilt heakskiidetud [GitHub rakenduse seadistus](#github-app-setup).
4. Käivitage töövoog uuesti, eemaldades märkeruudu **Preview only**. See teeb eelvaate, tõlgib, käivitab `co-op-review --readme-only` ja loob või uuendab tõlke-PR-i ainult pärast seda, kui tõlge ja ülevaatus õnnestuvad. Töövoo kokkuvõte linkib PR-ile.
5. Kontrollige PR-is sõnastust ja failimuudatusi ning ühendage (merge) siis, kui olete valmis. Töövoog ei ühenda automaatselt.

PR sisaldab ainult `translations/<language>/README.md` faili ja selle keele metaandmefaili. Lähte-README jääb muutmata ning lingid teistele dokumentidele osutavad jätkuvalt lähte­dokumentidele. PR-i kirjeldus loetleb muudetud failid ja strukturaalse ülevaatuse tulemused. Kui tõlkimine või ülevaatus ebaõnnestub, vaadake töövoo kokkuvõtet ja nurjunud sammu logisid; PR-i ei loo. Kui muudatusi ei ole, pole uut PR-i vaja.

**Organisatsiooni ja CI märkus:** GitHub App on valikuline, mitte organisatsiooni omandi nõue. Kui kasutatakse `GITHUB_TOKEN`i, siis pull-requestide avamise, uuendamise või uuesti avamise töövood nõuavad, et kirjutamisõigusega kasutaja valiks **Approve workflows to run**. Push-töövooge see token ei käivita. Automaatse alluva CI jaoks vaadake [GitHub rakenduse seadistus](#github-app-setup) ja GitHubi [töövoogude käivitamise reeglid](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Eeltingimused

Enne töövoo koostamist seadistage AI-teenuse saladused, mida teie tõlketöö jaoks vaja on.

Tekstitõlge nõuab ühte keelemudeli pakkujat:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Piltide tõlkimiseks on lisaks vajalik Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Vaadake kohaliku konfiguratsiooni üksikasjade jaoks [Konfiguratsioon](configuration.md) ja [Azure AI seadistus](azure-ai-setup.md).

## Standardne seadistus

Pärast README töövoo proovimist kasutage seda seadistust, et tõlkida hoidla Markdown-failid mitmesse keelde. See käivitab Markdown-ülevaatuse enne PR-i avamist ja ei vaja Azure AI Visionit.

### Samm 1: Lisa hoidla saladused

Sihthoidlas avage **Settings** > **Secrets and variables** > **Actions** ja lisage seejärel pakkuja saladused, mida teie töövoog kasutab.

![Vali Actions saladused](../../assets/github-actions/select-setting-action.png)

### Samm 2: Luba töövoo õigused

Avage **Settings** > **Actions** > **General**.

Jaotises **Workflow permissions**:

1. Luba **GitHub Actionsil luua ja heaks kiita pull requeste**.
2. Salvestage säte.

Alljärgnev töö nõuab otseselt `contents: write` ja `pull-requests: write`. Jätke hoidla vaike-töövooõigused muutmata. Kui organisatsiooni poliitika blokeerib PR-i loomise, küsige administraatorilt heakskiidetud [GitHub rakenduse seadistus](#github-app-setup).

### Samm 3: Lisa töövoog

Looge fail `.github/workflows/co-op-translator.yml`:

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

Muutke `TARGET_LANGUAGES` väärtuseks need keeled, mida teie projekt vajab. Ülevaatus kasutab Python API-d, et kontrollida ainult Markdownit, mis vastab tõlke sammule. Tõlke- või ülevaatusviga peatab töö enne PR-i loomist. Töövoog ei ühenda PR-i automaatselt. Suurte hoidlate puhul lisage `paths:` filter `on.push` alla, nii et töövoog jookseb ainult siis, kui dokumentatsioon muutub.

### Valikuline: notebookid ja pildid

Notebookide puhul lisage tõlkekäsule `-nb` ja määrake ülevaatussammus `notebook=True`. Pildi teksti puhul seadistage need kaks [Azure AI Visioni saladust](#prerequisites), edastage need tõlkesammu `env`-i, lisage käsule `-img` ja lisage PR-sammu `add-paths`-i `translated_images/`. Vaadake tõlgitud pilte visuaalselt üle; deterministlik ülevaatus ei kinnita pildi teksti ega keelelist täpsust.

## GitHub rakenduse seadistus

Kasutage heakskiidetud GitHub Appi, kui teie organisatsioon nõuab rakenduse identiteeti või kui genereeritud PR peab käivitama alluvat CI-d ilma `GITHUB_TOKEN` heakskiitmiseta. Rakendus ei möödu organisatsiooni poliitikast; administraatorid kontrollivad endiselt selle installimist ja õigusi.

### Samm 1: Loo või installi GitHub App

Kasutage olemasolevat organisatsiooni pakutud rakendust, kui see on saadaval, või looge rakendus, millel on lugemis-/kirjutamisõigused **Contents** ja **Pull requests** jaoks. Installige see sihthoidlasse koos vajaliku organisatsiooni heakskiiduga.

Record:

- App ID
- Private key contents

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Samm 2: Genereeri rakenduse token

Lisage see samm vahetult enne olemasolevat pull request sammu. README malli puhul kasutage sama edukuse tingimust, et eelvaated ja ebaõnnestunud tõlked ei küsiks App-tokenit:

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

Seejärel muutke ainult olemasoleva pull request sammude `token` sisendiks `${{ steps.generate_token.outputs.token }}`. Säilitage selle edukuse tingimus, haru, PR-i keha ja `add-paths` muutmata. Token on vaikimisi piiritletud praeguse hoidla jaoks. Kui kohandate standardset seadistust README-malli asemel, jätke ülaltoodud `if` ära: see töövoog kasutab vaike-edukuse tingimust, nii et tokeni loomine ja PR-i loomine jooksevad alles pärast tõlke ja ülevaatuse õnnestumist.

Vaadake ametlikku [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2), et saada installi- ja tokeniõiguste teavet.

## Runneri piirangud

GitHubi poolt hostitud runneritel on maksimaalne tööaja piirang. Suured hoidlad või palju sihtkeeli võivad selle piiri ületada.

Suuremate tõlketööde puhul:

- Tõlkige jooksu kohta vähem keeli.
- Kasutage sisumärke nagu `-md`, `-nb` või `-img`.
- Kasutage isehostitud runnerit, kui hoidla suurus või mudeli latentsus teeb hostitud runnerid ebausaldusväärseks.

## Ülevaatus CI-s

Kasutage `co-op-review`-i, kui pull request peaks valideerima genereeritud tõlkeid ilma LLM-ide või mudeli pakkujate kutsumiseta.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` on beetaversiooni deterministlik ülevaatuse käsk. Selle kontrollid ja väljundiskeem võivad muutuda, kuid see on mõeldud CI jaoks ohutuks, kuna see ei kirjuta faile ega kutsu mudeli pakkujaid.