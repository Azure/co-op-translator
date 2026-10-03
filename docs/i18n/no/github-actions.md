# GitHub Actions

Bruk GitHub Actions når du vil at et repository automatisk skal oversette endret dokumentasjon og åpne en pull request med de genererte resultatene.

Start med det standard `GITHUB_TOKEN`-oppsettet, også for organisasjons-repositories der policy tillater det. Se [GitHub App Setup](#github-app-setup) når organisasjonen din krever en App-identitet eller du trenger automatiske downstream workflow-kjøringer.

**Manuelle endringer:** disse arbeidsflytene oversetter endrede kildefiler på nytt i sin helhet og kan overskrive formuleringer som er redigert i oversettelsene deres. Gå gjennom hver PR før sammenslåing. Bevaring av godkjente endringer på blokknivå i Markdown krever en tilpasset integrasjon med [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Din første README-oversettelses-PR

Begynn med én rot-`README.md` og ett målspråk. Denne arbeidsflyten oversetter kun Markdown, så Azure AI Vision er ikke nødvendig.

1. Kopier [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([se malen på GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) til `.github/workflows/translate-readme.yml` i repositoryet du vil oversette, og commit den til repositoryets standardbranch. Malen bruker root Action i `Azure/co-op-translator@main`, som installerer CLI-en fra samme source ref. Fest en gjennomgått commit for gjenskapbare kjøringer.
2. Åpne **Actions > Translate README > Run workflow**, velg et språk, og la **Preview only** stå avkrysset. Gå gjennom token-estimatet i forhåndsvisningssteget. Forhåndsvisning ringer ikke modellleverandører, skriver ikke oversettelser, eller oppretter en PR.
3. Legg til hemmelighetene for én [tekstleverandør](#prerequisites), og aktiver **Tillat GitHub Actions å opprette og godkjenne pull requests** under **Innstillinger > Actions > Generelt**. Malen ber om `contents: write` og `pull-requests: write` for jobben; du trenger ikke å endre standardtillatelsene for alle arbeidsflyter. Hvis organisasjonspolicy blokkerer disse tillatelsene eller denne innstillingen, spør en administrator om en godkjent [GitHub-app](#github-app-setup).
4. Kjør arbeidsflyten igjen med **Preview only** avkrysset fra. Den forhåndsviser, oversetter, kjører `co-op-review --readme-only`, og oppretter eller oppdaterer en oversettelses-PR først etter at oversettelse og gjennomgang lykkes. Arbeidsflytsammendraget lenker til PR-en.
5. Gå gjennom formuleringene og filendringene i PR-en, og merge når du er klar. Arbeidsflyten merger ikke automatisk.

PR-en inneholder bare `translations/<language>/README.md` og dens språkmeldingsfil. Kilde-README-en forblir uendret, og lenker til andre dokumenter fortsetter å peke på kilde­dokumentene. PR-bodyen viser endrede filer og resultater fra strukturgjennomgangen. Hvis oversettelse eller gjennomgang feiler, undersøk arbeidsflytsammendraget og loggene for feilede steg; ingen PR opprettes. Hvis det ikke er noen endringer, trengs ingen ny PR.

**Organisasjons- og CI-notat:** En GitHub App er valgfri, ikke et krav ved organisasjons-eierskap. Med `GITHUB_TOKEN` krever pull-request-arbeidsflyter for åpning, oppdatering eller gjenåpning av en PR at en bruker med skrivettigheter velger **Approve workflows to run**. Push-arbeidsflyter trigges ikke av denne tokenen. For ubemannet downstream CI, se [GitHub App Setup](#github-app-setup) og GitHubs [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Forutsetninger

Før du oppretter arbeidsflyten, konfigurer AI-tjenestens hemmeligheter som oversettelseskjøringen trenger.

Tekstoversettelse krever én språkmodellleverandør:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Bildeoversettelse krever i tillegg Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Se [Configuration](configuration.md) og [Azure AI Setup](azure-ai-setup.md) for lokale konfigurasjonsdetaljer.

## Standardoppsett

Etter å ha prøvd README-arbeidsflyten, bruk dette oppsettet for å oversette et repositorys Markdown-filer til flere språk. Den kjører en Markdown-gjennomgang før den åpner en PR og krever ikke Azure AI Vision.

### Trinn 1: Legg til repository-hemmeligheter

I mål-repositoryet ditt, åpne **Settings** > **Secrets and variables** > **Actions**, og legg til leverandørhemmelighetene arbeidsflyten din vil bruke.

![Velg Actions-hemmeligheter](../../assets/github-actions/select-setting-action.png)

### Trinn 2: Aktiver arbeidsflyttillatelser

Åpne **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. Aktiver **Tillat GitHub Actions å opprette og godkjenne pull requests**.
2. Lagre innstillingen.

Jobben nedenfor ber eksplisitt om `contents: write` og `pull-requests: write`. La repositoryets standard workflow-tillateler være uendret. Hvis organisasjonspolicy blokkerer PR-oppretting, spør en administrator om en godkjent [GitHub App](#github-app-setup).

### Trinn 3: Legg til arbeidsflyten

Opprett `.github/workflows/co-op-translator.yml`:

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

Endre `TARGET_LANGUAGES` til språkene prosjektet ditt trenger. Gjennomgangen bruker Python API-en for å sjekke kun Markdown, i samsvar med oversettelsestrinnet. En oversettelses- eller gjennomgangsfeil stopper jobben før PR-oppretting. Arbeidsflyten merger ikke PR-en automatisk. For store repositories, legg til et `paths:`-filter under `on.push` slik at arbeidsflyten kun kjører når dokumentasjonen endres.

### Valgfritt: notatbøker og bilder

For notatbøker, legg til `-nb` i oversettelseskommandoen og sett `notebook=True` i gjennomgangssteget. For bildetekst, konfigurer de to [Azure AI Vision secrets](#prerequisites), send dem i translation-stegets `env`, legg til `-img` i kommandoen, og legg til `translated_images/` i PR-stegets `add-paths`. Gjennomgå oversatte bilder visuelt; den deterministiske gjennomgangen sertifiserer ikke bilde­tekst eller lingvistisk nøyaktighet.

## Oppsett av GitHub-app

Bruk en godkjent GitHub App når organisasjonen din krever en App-identitet, eller når den genererte PR-en må trigge downstream CI uten `GITHUB_TOKEN`-godkjenningssteget. En App omgår ikke organisasjonspolicy; administratorer kontrollerer fortsatt installasjon og tillatelser.

### Trinn 1: Opprett eller installer en GitHub-app

Bruk en eksisterende organisasjons‑tilbydd App når tilgjengelig, eller opprett en med lese-/skrive-tilgang til **Contents** og **Pull requests**. Installer den på mål-repositoryet med eventuell nødvendig organisasjonsgodkjenning.

Noter:

- App ID
- Private key contents

Lagre dem som repository-hemmeligheter:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Trinn 2: Generer et App-token

Legg til dette steget umiddelbart før det eksisterende pull request-steget. For README-malen, bruk samme suksessbetingelse slik at forhåndsvisninger og mislykkede oversettelser ikke ber om et App-token:

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

Endre deretter kun det eksisterende pull request-stegets `token`-input til `${{ steps.generate_token.outputs.token }}`. Behold suksessbetingelsen, branch, PR-body og `add-paths` uendret. Tokenet er som standard scoped til det gjeldende repositoryet. Når du tilpasser standardoppsettet i stedet for README-malen, utelat `if`-betingelsen over: den arbeidsflyten bruker standard suksessbetingelse, så token-oppretting og PR-oppretting kjører bare etter at oversettelse og gjennomgang lykkes.

Se den offisielle [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installasjon og token-tillatelser.

## Begrensninger for runnere

GitHub-hostede runnere har en maksimal jobblengde. Store repositories eller mange målspråk kan overskride den grensen.

For store oversettelsesarbeidsmengder:

- Oversett færre språk per kjøring.
- Bruk innholdssignaler som `-md`, `-nb`, eller `-img`.
- Bruk en selvhostet runner når repository-størrelse eller modell-latens gjør hostede runnere upålitelige.

## Gjennomgang i CI

Bruk `co-op-review` når en pull request skal validere genererte oversettelser uten å kalle LLM- eller Vision-leverandører.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` er en beta deterministisk gjennomgangskommando. Dens sjekker og output‑skjema kan utvikle seg, men den er designet for å være trygg for CI fordi den ikke skriver filer eller kaller modellleverandører.