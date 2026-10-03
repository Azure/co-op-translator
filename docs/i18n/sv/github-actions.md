# GitHub Actions

Använd GitHub Actions när du vill att ett repository ska översätta ändrad dokumentation automatiskt och öppna en pull request med de genererade resultaten.

Börja med den standardmässiga `GITHUB_TOKEN`-inställningen, även för organisationsrepositories där policyn tillåter det. Se [Inställning av GitHub App](#github-app-setup) när din organisation kräver en App-identitet eller när du behöver automatiska nedströmskörningar av workflows.

**Manuella redigeringar:** dessa arbetsflöden översätter om ändrade källfiler i sin helhet och kan skriva över formuleringar som redigerats i deras översättningar. Granska varje PR innan sammanslagning. För att bevara Markdown på blocknivå för accepterade ändringar krävs en anpassad integration med [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Din första README-översättnings-PR

Börja med en rot-`README.md` och ett målspråk. Detta arbetsflöde översätter endast Markdown, så Azure AI Vision krävs inte.

1. Kopiera [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([visa mallen på GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) till `.github/workflows/translate-readme.yml` i det repository du vill översätta, och commit:a det till det repositoryts standardbranch. Mallen använder root Action i `Azure/co-op-translator@main`, som installerar CLI från samma källref. Pinna ett granskat commit för reproducerbara körningar.
2. Öppna **Actions > Translate README > Run workflow**, välj ett språk, och låt **Preview only** vara ikryssat. Granska tokenuppskattningen i förhandsgranskningssteget. Förhandsgranskning anropar inte modellleverantörer, skriver inte översättningar eller skapar en PR.
3. Lägg till hemligheterna för en [textleverantör](#prerequisites), och aktivera **Tillåt GitHub Actions att skapa och godkänna pull requests** under **Inställningar > Actions > Allmänt**. Mallen begär `contents: write` och `pull-requests: write` för sitt jobb; du behöver inte ändra standardbehörigheterna för varje workflow. Om organisationspolicyn blockerar dessa behörigheter eller denna inställning, fråga en administratör om en godkänd [GitHub-app](#github-app-setup).
4. Kör arbetsflödet igen med **Preview only** avmarkerat. Det förhandsgranskar, översätter, kör `co-op-review --readme-only`, och skapar eller uppdaterar en översättnings-PR endast efter att översättning och granskning lyckats. Arbetsflödesöversikten länkar till PR:en.
5. Granska formuleringar och filändringar i PR:en, och slå sedan ihop när du är redo. Arbetsflödet slår inte ihop automatiskt.

PR:en innehåller endast `translations/<language>/README.md` och dess språkmetadatafil. Käll-README:n förblir oförändrad, och länkar till andra dokument fortsätter att peka på källdokumenten. PR-body:n listar ändrade filer och resultat från den strukturella granskningen. Om översättning eller granskning misslyckas, inspektera arbetsflödesöversikten och loggar för misslyckade steg; ingen PR skapas. Om det inte finns några ändringar behövs ingen ny PR.

**Organisation och CI-anteckning:** En GitHub App är valfri och inte ett krav för organisationsägande. Med `GITHUB_TOKEN` kräver pull-request-arbetsflöden för att öppna, uppdatera eller återöppna en PR att en användare med skrivbehörighet väljer **Approve workflows to run**. Push-arbetsflöden triggas inte av denna token. För obevakad nedströms CI, se [Inställning av GitHub App](#github-app-setup) och GitHubs [regler för att trigga workflows](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Förutsättningar

Innan du skapar arbetsflödet, konfigurera de AI-tjänsthemligheter som din översättningskörning behöver.

Textöversättning kräver en språkmodellleverantör:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, samt valfritt `OPENAI_ORG_ID` och `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, samt valfritt `ANTHROPIC_BASE_URL`

För bildöversättning krävs dessutom Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Se [Konfiguration](configuration.md) och [Azure AI-inställning](azure-ai-setup.md) för lokala konfigurationsdetaljer.

## Standardinställning

Efter att ha testat README-arbetsflödet, använd denna setup för att översätta ett repositories Markdown-filer till flera språk. Den kör en Markdown-granskning innan en PR öppnas och kräver inte Azure AI Vision.

### Steg 1: Lägg till repository-hemligheter

I ditt målrepository, öppna **Settings** > **Secrets and variables** > **Actions**, lägg sedan till leverantörshemligheterna som ditt arbetsflöde kommer att använda.

![Välj Actions-hemligheter](../../assets/github-actions/select-setting-action.png)

### Steg 2: Aktivera arbetsflödesbehörigheter

Open **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. Aktivera **Tillåt GitHub Actions att skapa och godkänna pull requests**.
2. Spara inställningen.

Jobben nedan begär uttryckligen `contents: write` och `pull-requests: write`. Låt repositoryts standardinställningar för workflow-behörigheter vara oförändrade. Om organisationspolicyn blockerar skapande av PR, fråga en administratör om en godkänd [GitHub App](#github-app-setup).

### Steg 3: Lägg till arbetsflödet

Skapa `.github/workflows/co-op-translator.yml`:

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

Ändra `TARGET_LANGUAGES` till de språk ditt projekt behöver. Granskningen använder Python API:t för att kontrollera endast Markdown, vilket matchar översättningssteget. Ett översättnings- eller granskningsfel stoppar jobbet innan en PR skapas. Arbetsflödet slår inte ihop PR:en automatiskt. För stora repositories, lägg till ett `paths:`-filter under `on.push` så att arbetsflödet endast körs när dokumentationen ändras.

### Valfritt: notebooks och bilder

För notebooks, lägg till `-nb` i översättningskommandot och sätt `notebook=True` i granskningssteget. För bildtext, konfigurera de två [Azure AI Vision-hemligheterna](#prerequisites), skicka dem i översättningsstegets `env`, lägg till `-img` i kommandot, och lägg till `translated_images/` i PR-stegets `add-paths`. Granska översatta bilder visuellt; den deterministiska granskningen intygar inte bildtext eller språklig noggrannhet.

## Inställning av GitHub App

Använd en godkänd GitHub App när din organisation kräver en App-identitet, eller när den genererade PR:en behöver trigga nedströms CI utan `GITHUB_TOKEN`-godkännandesteg. En App kringgår inte organisationspolicyn; administratörer kontrollerar fortfarande dess installation och behörigheter.

### Steg 1: Skapa eller installera en GitHub App

Använd en befintlig App som tillhandahålls av organisationen när den finns, eller skapa en med läs-/skrivåtkomst till **Contents** och **Pull requests**. Installera den i målrepositoryt med eventuell nödvändig organisationsgodkännande.

Anteckna:

- App-ID
- Privat nyckelinnehåll

Spara dem som repository-hemligheter:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Steg 2: Generera en App-token

Lägg till detta steg omedelbart före det befintliga pull request-steget. För README-mallen, använd samma framgångsvillkor så att förhandsvisningar och misslyckade översättningar inte begär en App-token:

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

Ändra sedan endast det befintliga pull request-stegets `token`-input till `${{ steps.generate_token.outputs.token }}`. Behåll dess framgångsvillkor, branch, PR-body och `add-paths` oförändrade. Tokenet är avgränsat till det aktuella repositoryt som standard. När du anpassar standardinställningen istället för README-mallen, utelämna `if` ovan: det arbetsflödet använder standard framgångsvillkor, så token-skapande och PR-skapande körs endast efter att översättning och granskning lyckats.

Se den officiella [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) för installation och tokenbehörigheter.

## Runnerbegränsningar

GitHub-hostade runners har en maximal jobbtid. Stora repositories eller många målspråk kan överskrida den gränsen.

För stora översättningsarbetsbelastningar:

- Översätt färre språk per körning.
- Använd innehållsflaggor såsom `-md`, `-nb` eller `-img`.
- Använd en självhostad runner när repositorystorlek eller modellatens gör hostade runners opålitliga.

## Granskning i CI

Använd `co-op-review` när en pull request ska validera genererade översättningar utan att anropa LLM- eller Vision-leverantörer.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` är ett deterministiskt granskningskommando i beta. Dess kontroller och utskriftschema kan utvecklas, men det är utformat för att vara säkert för CI eftersom det inte skriver filer eller anropar modellleverantörer.