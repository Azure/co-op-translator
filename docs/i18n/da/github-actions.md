# GitHub Actions

Brug GitHub Actions, når du vil have et repository til automatisk at oversætte ændret dokumentation og åbne en pull request med de genererede resultater.

Start med den standardmæssige `GITHUB_TOKEN`-opsætning, også for organisationsrepositories hvor politikken tillader det. Se [GitHub App Setup](#github-app-setup), når din organisation kræver en App-identitet, eller du har brug for automatiske downstream-workflowkørsler.

**Manuelle redigeringer:** disse workflows genoversætter ændrede kildefiler fuldstændigt og kan overskrive formuleringer, der er redigeret i deres oversættelser. Gennemgå hver PR før sammenfletning. Bevarelse af Markdown på blokniveau for accepterede rettelser kræver en brugerdefineret integration med [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Din første README-oversættelses-PR

Start med én rod `README.md` og ét målsprog. Denne workflow oversætter kun Markdown, så Azure AI Vision er ikke påkrævet.

1. Kopiér [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([se skabelonen på GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) til `.github/workflows/translate-readme.yml` i det repository, du vil oversætte, og commit det til repositoryets standardbranch. Skabelonen bruger root Action i `Azure/co-op-translator@main`, som installerer CLI'en fra samme source ref. Pin et gennemgået commit for reproducerbare køringer.
2. Åbn **Actions > Translate README > Run workflow**, vælg et sprog, og lad **Preview only** stå afkrydset. Gennemgå tokenestimatet i preview-trinnet. Preview kalder ikke modeludbydere, skriver ikke oversættelser eller opretter en PR.
3. Tilføj hemmelighederne for én [tekstudbyder](#prerequisites), og aktiver **Tillad GitHub Actions at oprette og godkende pull requests** under **Indstillinger > Actions > Generelt**. Skabelonen anmoder om `contents: write` og `pull-requests: write` for sit job; du behøver ikke ændre standardtilladelserne for hver workflow. Hvis organisationspolitikken blokerer disse tilladelser eller denne indstilling, spørg en administrator om en godkendt [GitHub App](#github-app-setup).
4. Kør workflow'en igen med **Preview only** ukrydset. Den forhåndsviser, oversætter, kører `co-op-review --readme-only` og opretter eller opdaterer en oversættelses-PR først efter, at oversættelse og review er vellykkede. Workflow-sammendraget linker til PR'en.
5. Gennemgå formuleringerne og filændringerne i PR'en, og slå den sammen, når du er klar. Workflow'en fletter ikke automatisk.

PR'en indeholder kun `translations/<language>/README.md` og dens sprogmetadatafil. Kilde-README forbliver uændret, og links til andre dokumenter peger fortsat på kildedokumenterne. PR-beskeden oplister ændrede filer og resultater af strukturel gennemgang. Hvis oversættelse eller review fejler, undersøg workflow-sammendraget og logfiler for fejlede trin; der oprettes ingen PR. Hvis der ikke er ændringer, er der ikke behov for en ny PR.

**Organisation og CI-note:** En GitHub App er valgfri, ikke et krav ved organisations ejerskab. Med `GITHUB_TOKEN` kræver pull-request-workflows til åbning, opdatering eller genåbning af en PR en bruger med skriveadgang for at vælge **Godkend, at workflows må køre**. Push-workflows udløses ikke af dette token. For ubemandet downstream CI se [GitHub App Setup](#github-app-setup) og GitHubs [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Forudsætninger

Før du opretter workflow'en, konfigurer de AI-tjenestehemmeligheder, som din oversættelseskørsel har brug for.

Tekstoversættelse kræver én sprogmodeludbyder:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` og `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Billedoversættelse kræver desuden Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Se [Konfiguration](configuration.md) og [Azure AI-opsætning](azure-ai-setup.md) for lokale konfigurationsdetaljer.

## Standardopsætning

Efter at have prøvet README-workflow'en, brug denne opsætning til at oversætte repositoryets Markdown-filer til flere sprog. Den kører en Markdown-gennemgang før åbning af en PR og kræver ikke Azure AI Vision.

### Trin 1: Tilføj repository-hemmeligheder

I dit målrepository, åbn **Indstillinger** > **Hemmeligheder og variabler** > **Actions**, og tilføj derefter de udbyderhemmeligheder, som din workflow vil bruge.

![Vælg Actions-hemmeligheder](../../assets/github-actions/select-setting-action.png)

### Trin 2: Aktiver workflow-tilladelser

Åbn **Indstillinger** > **Actions** > **Generelt**.

Under **Workflow-tilladelser**:

1. Aktivér **Tillad GitHub Actions at oprette og godkende pull requests**.
2. Gem indstillingen.

Jobbet nedenfor anmoder eksplicit om `contents: write` og `pull-requests: write`. Lad repositoryets standardworkflowtilladelser være uændrede. Hvis organisationspolitikken blokerer PR-oprettelse, spørg en administrator om en godkendt [GitHub App](#github-app-setup).

### Trin 3: Tilføj workflow'en

Opret `.github/workflows/co-op-translator.yml`:

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

Skift `TARGET_LANGUAGES` til de sprog, dit projekt har brug for. Reviewet bruger Python API'en til kun at tjekke Markdown, hvilket svarer til oversættelsestrinnet. En oversættelses- eller reviewfejl stopper jobbet før PR-oprettelse. Workflow'en fletter ikke PR'en automatisk. For store repositories, tilføj et `paths:` filter under `on.push`, så workflow'en kun kører, når dokumentationen ændres.

### Valgfrit: notebooks og billeder

For notebooks, tilføj `-nb` til oversættelseskommandoen og sæt `notebook=True` i review-trinnet. For billedtekst, konfigurer de to [Azure AI Vision secrets](#prerequisites), angiv dem i oversættelsestrinnets `env`, tilføj `-img` til kommandoen, og tilføj `translated_images/` til PR-trinnets `add-paths`. Gennemse oversatte billeder visuelt; det deterministiske review garanterer ikke billedtekst eller sproglig nøjagtighed.

## GitHub App-opsætning

Brug en godkendt GitHub App, når din organisation kræver en App-identitet, eller når den genererede PR skal udløse downstream CI uden `GITHUB_TOKEN` godkendelsestrin. En App omgår ikke organisationspolitikken; administratorer kontrollerer stadig dens installation og tilladelser.

### Trin 1: Opret eller installer en GitHub App

Brug en eksisterende organisationsleveret App, hvis tilgængelig, eller opret en med læse-/skriveadgang til **Contents** og **Pull requests**. Installer den på målrepositoriet med eventuel krævet organisationsgodkendelse.

Registrer:

- App ID
- Indholdet af privat nøgle

Gem dem som repository-hemmeligheder:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Trin 2: Generér et App-token

Tilføj dette trin lige før det eksisterende pull request-trin. For README-skabelonen, brug samme succesbetingelse, så forhåndsvisninger og fejlede oversættelser ikke anmoder om et App-token:

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

Skift derefter kun det eksisterende pull request-trins `token`-input til `${{ steps.generate_token.outputs.token }}`. Bevar dets succesbetingelse, branch, PR-indhold og `add-paths` uændrede. Tokenet er som standard scoped til det aktuelle repository. Når du tilpasser standardopsætningen i stedet for README-skabelonen, udelad `if`-sætningen ovenfor: den workflow bruger standard succesbetingelse, så tokenoprettelse og PR-oprettelse kun kører efter at oversættelse og review er lykkedes.

Se den officielle [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installation og token-tilladelser.

## Runner-begrænsninger

GitHub-hostede runnere har en maksimal jobvarighed. Store repositories eller mange målsprog kan overskride denne grænse.

For store oversættelsesarbejdsmængder:

- Oversæt færre sprog per kørsel.
- Brug indholdsflag som `-md`, `-nb` eller `-img`.
- Brug en self-hosted runner, når repository-størrelse eller modellatens gør hostede runnere upålidelige.

## Gennemgang i CI

Brug `co-op-review`, når en pull request skal validere genererede oversættelser uden at kalde LLM- eller Vision-udbydere.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` er en beta deterministisk review-kommando. Dens kontroller og output-skema kan udvikle sig, men den er designet til at være sikker for CI, fordi den ikke skriver filer eller kalder modeludbydere.