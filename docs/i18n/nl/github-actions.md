# GitHub Actions

Gebruik GitHub Actions wanneer je wilt dat een repository gewijzigde documentatie automatisch vertaalt en een pull request opent met de gegenereerde output.

Begin met de standaard `GITHUB_TOKEN` setup, ook voor organisatie-repositories waar het beleid dit toestaat. Zie [GitHub App-configuratie](#github-app-setup) wanneer je organisatie een App-identiteit vereist of je automatische downstream workflow-uitvoeringen nodig hebt.

**Handmatige bewerkingen:** Deze workflows vertalen gewijzigde bronbestanden volledig opnieuw en kunnen bewoordingen die in hun vertalingen zijn bewerkt overschrijven. Beoordeel elke PR voordat u deze samenvoegt. Het behoud van Markdown op blokniveau voor geaccepteerde bewerkingen vereist een aangepaste integratie met de [Python API-provider voor vertaalstatus](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Je eerste README-vertalings-PR

Begin met één root `README.md` en één doeltaal. Deze workflow vertaalt alleen Markdown, dus Azure AI Vision is niet vereist.

1. Kopieer [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([bekijk het sjabloon op GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) naar `.github/workflows/translate-readme.yml` in de repository die je wilt vertalen, en commit het naar die repository's standaardbranch. Het sjabloon gebruikt de root Action in `Azure/co-op-translator@main`, die de CLI van dezelfde source ref installeert. Wijs een beoordeelde commit toe voor reproduceerbare runs.
2. Open **Actions > Translate README > Run workflow**, kies een taal, en laat **Preview only** aangevinkt. Controleer de token-schatting in de previewstap. De preview roept geen modelproviders aan, schrijft geen vertalingen en maakt geen PR aan.
3. Voeg de secrets toe voor één [tekstprovider](#prerequisites), en schakel **Toestaan dat GitHub Actions pull requests aanmaakt en goedkeurt** in onder **Instellingen > Acties > Algemeen**. Het sjabloon vraagt `contents: write` en `pull-requests: write` voor zijn job; je hoeft de standaardpermissies voor elke workflow niet te wijzigen. Als het organisatiebeleid deze permissies of deze instelling blokkeert, vraag een beheerder naar een goedgekeurde [GitHub App](#github-app-setup).
4. Voer de workflow opnieuw uit met **Preview only** uitgevinkt. Hij toont een preview, vertaalt, voert `co-op-review --readme-only` uit en maakt of werkt een vertalings-PR alleen aan nadat vertaling en review geslaagd zijn. De workflow-samenvatting bevat een link naar de PR.
5. Controleer de bewoording en bestandswijzigingen in de PR en merge wanneer je klaar bent. De workflow voegt niet automatisch samen.

De PR bevat alleen `translations/<language>/README.md` en het bijbehorende taalmetadata-bestand. De bron-README blijft ongewijzigd en links naar andere documenten blijven naar de brondocumenten verwijzen. De PR-body vermeldt gewijzigde bestanden en de resultaten van de structurele review. Als vertaling of review faalt, controleer de workflow-samenvatting en de logs van de gefaalde stappen; er wordt geen PR aangemaakt. Als er geen wijzigingen zijn, is geen nieuwe PR nodig.

**Organization and CI note:** Een GitHub App is optioneel en geen vereiste bij organisatie-eigendom. Met `GITHUB_TOKEN` vereisen pull-requestworkflows voor het openen, bijwerken of opnieuw openen van een PR dat een gebruiker met schrijfpermissie **Approve workflows to run** selecteert. Push-workflows worden niet door dit token getriggerd. Voor onbeheerde downstream CI, zie [GitHub App-configuratie](#github-app-setup) en GitHub's [regels voor het triggeren van workflows](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Vereisten

Voordat je de workflow aanmaakt, configureer de AI-service-secrets die je vertaalrun nodig heeft.

Tekstvertaling vereist één taalmodelprovider:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` en `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Voor afbeeldingsvertaling is daarnaast Azure AI Vision vereist:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Zie [Configuratie](configuration.md) en [Azure AI-configuratie](azure-ai-setup.md) voor details over lokale configuratie.

## Standaardconfiguratie

Nadat je de README-workflow hebt geprobeerd, gebruik deze setup om de Markdown-bestanden van een repository in meerdere talen te vertalen. Het voert een Markdown-review uit voordat het een PR opent en vereist geen Azure AI Vision.

### Stap 1: Voeg repository-secrets toe

In je doelrepository, open **Settings** > **Secrets and variables** > **Actions**, en voeg vervolgens de provider-secrets toe die je workflow zal gebruiken.

![Selecteer Actions-secrets](../../assets/github-actions/select-setting-action.png)

### Stap 2: Schakel workflowpermissies in

Open **Settings** > **Actions** > **General**.

Onder **Workflow permissions**:

1. Schakel **Toestaan dat GitHub Actions pull requests aanmaakt en goedkeurt** in.
2. Sla de instelling op.

De onderstaande job vraagt expliciet `contents: write` en `pull-requests: write`. Laat de standaard workflowpermissies van de repository ongewijzigd. Als het organisatiebeleid het aanmaken van PR's blokkeert, vraag een beheerder naar een goedgekeurde [GitHub App](#github-app-setup).

### Stap 3: Voeg de workflow toe

Maak `.github/workflows/co-op-translator.yml` aan:

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

Wijzig `TARGET_LANGUAGES` naar de talen die je project nodig heeft. De review gebruikt de Python API om alleen Markdown te controleren, overeenkomstig de vertalingstap. Een vertaal- of reviewfout stopt de job voordat een PR wordt aangemaakt. De workflow voegt de PR niet automatisch samen. Voor grote repositories voeg een `paths:`-filter toe onder `on.push` zodat de workflow alleen draait wanneer documentatie wijzigt.

### Optioneel: notebooks en afbeeldingen

Voor notebooks voeg `-nb` toe aan het vertaalcommando en zet `notebook=True` in de reviewstap. Voor afbeeldingstekst configureer de twee [Azure AI Vision secrets](#prerequisites), geef ze door in de `env` van de vertaalstap, voeg `-img` toe aan het commando, en voeg `translated_images/` toe aan `add-paths` van de PR-stap. Controleer vertaalde afbeeldingen visueel; de deterministische review garandeert niet de juistheid van afbeeldingstekst of linguïstische nauwkeurigheid.

## GitHub App-configuratie

Gebruik een goedgekeurde GitHub App wanneer je organisatie een App-identiteit vereist, of wanneer de gegenereerde PR downstream CI moet triggeren zonder de `GITHUB_TOKEN` goedkeuringsstap. Een App omzeilt het organisatiebeleid niet; beheerders blijven de installatie en permissies beheren.

### Stap 1: Maak of installeer een GitHub App

Gebruik een bestaande door de organisatie geleverde App indien beschikbaar, of maak er een met read/write-toegang tot **Contents** en **Pull requests**. Installeer deze op de doelrepository met eventuele vereiste goedkeuring van de organisatie.

Noteer:

- App ID
- Inhoud van private key

Bewaar ze als repository-secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Stap 2: Genereer een App-token

Voeg deze stap direct voor de bestaande pull request-stap toe. Voor het README-sjabloon, gebruik dezelfde success-voorwaarde zodat previews en mislukte vertalingen geen App-token opvragen:

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

Wijzig daarna alleen de `token`-input van de bestaande pull request-stap naar `${{ steps.generate_token.outputs.token }}`. Laat de success-voorwaarde, branch, PR-body en `add-paths` ongewijzigd. Het token is standaard beperkt tot de huidige repository. Wanneer je de standaardsetup aanpast in plaats van het README-sjabloon, laat dan de bovenstaande `if` weg: die workflow gebruikt de standaard success-voorwaarde, dus tokencreatie en PR-creatie lopen alleen als vertaling en review geslaagd zijn.

Zie de officiële [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) voor installatie en tokenpermissies.

## Runner-limieten

GitHub-hosted runners hebben een maximale jobduur. Grote repositories of veel doeltalen kunnen die limiet overschrijden.

Voor grote vertaaltaken:

- Vertaal minder talen per uitvoering.
- Gebruik contentflags zoals `-md`, `-nb` of `-img`.
- Gebruik een zelfgehoste runner wanneer repositorygrootte of modellatentie hosted runners onbetrouwbaar maakt.

## Controleren in CI

Gebruik `co-op-review` wanneer een pull request gegenereerde vertalingen moet valideren zonder LLM- of Vision-providers aan te roepen.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` is een bètadeterministische reviewopdracht. De controles en het outputschema kunnen evolueren, maar het is ontworpen om veilig te zijn voor CI omdat het geen bestanden schrijft of modelproviders aanroept.