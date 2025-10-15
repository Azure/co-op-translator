<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:25:22+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "no"
}
-->
# Bruke Co-op Translator GitHub Action (Organisasjonsveiledning)

**Målgruppe:** Denne veiledningen er for **interne Microsoft-brukere** eller **team som har tilgang til nødvendige legitimasjoner for den forhåndsbygde Co-op Translator GitHub-appen** eller kan opprette sin egen tilpassede GitHub-app.

Automatiser oversettelsen av dokumentasjonen i ditt repository enkelt med Co-op Translator GitHub Action. Denne veiledningen viser deg hvordan du setter opp actionen slik at den automatisk oppretter pull requests med oppdaterte oversettelser hver gang kilde-Markdown-filer eller bilder endres.

> [!IMPORTANT]
> 
> **Velg riktig veiledning:**
>
> Denne veiledningen beskriver oppsett med **GitHub App ID og en privat nøkkel**. Du trenger vanligvis denne "Organisasjonsveiledningen" hvis: **`GITHUB_TOKEN`-tillatelsene er begrenset:** Organisasjonen eller repository-innstillingene dine begrenser standardtillatelsene som gis til `GITHUB_TOKEN`. Spesielt hvis `GITHUB_TOKEN` ikke har nødvendige `write`-tillatelser (som `contents: write` eller `pull-requests: write`), vil workflowen i [Offentlig oppsettveiledning](./github-actions-guide-public.md) feile på grunn av manglende tillatelser. Ved å bruke en dedikert GitHub-app med eksplisitte tillatelser unngår du denne begrensningen.
>
> **Hvis dette ikke gjelder deg:**
>
> Hvis standard `GITHUB_TOKEN` har tilstrekkelige tillatelser i ditt repository (dvs. du ikke er blokkert av organisasjonsbegrensninger), bruk **[Offentlig oppsettveiledning med GITHUB_TOKEN](./github-actions-guide-public.md)**. Den offentlige veiledningen krever ikke at du skaffer eller håndterer App ID-er eller private nøkler, og bruker kun standard `GITHUB_TOKEN` og repository-tillatelser.

## Forutsetninger

Før du konfigurerer GitHub Action, må du sørge for at du har nødvendige AI-tjenestelegitimasjoner klare.

**1. Påkrevd: AI Language Model-legitimasjon**
Du trenger legitimasjon for minst én støttet språkmodell:

- **Azure OpenAI**: Krever Endpoint, API-nøkkel, modell-/deploymentsnavn, API-versjon.
- **OpenAI**: Krever API-nøkkel, (valgfritt: Org ID, Base URL, Modell-ID).
- Se [Støttede modeller og tjenester](../../../../README.md) for detaljer.
- Oppsettveiledning: [Sett opp Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Valgfritt: Computer Vision-legitimasjon (for bildeoversettelse)**

- Kun nødvendig hvis du skal oversette tekst i bilder.
- **Azure Computer Vision**: Krever Endpoint og Subscription Key.
- Hvis ikke oppgitt, kjører actionen i [kun Markdown-modus](../markdown-only-mode.md).
- Oppsettveiledning: [Sett opp Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Oppsett og konfigurasjon

Følg disse stegene for å konfigurere Co-op Translator GitHub Action i ditt repository:

### Steg 1: Installer og konfigurer GitHub App-autentisering

Workflowen bruker GitHub App-autentisering for å samhandle sikkert med repositoryet ditt (f.eks. opprette pull requests) på dine vegne. Velg ett alternativ:

#### **Alternativ A: Installer forhåndsbygd Co-op Translator GitHub App (for intern Microsoft-bruk)**

1. Gå til [Co-op Translator GitHub App](https://github.com/apps/co-op-translator)-siden.

1. Velg **Install** og velg kontoen eller organisasjonen der repositoryet ditt ligger.

    ![Installer app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.no.png)

1. Velg **Only select repositories** og velg repositoryet ditt (f.eks. `PhiCookBook`). Klikk **Install**. Du kan bli bedt om å autentisere.

    ![Installer autorisasjon](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.no.png)

1. **Skaff app-legitimasjon (intern prosess kreves):** For at workflowen skal kunne autentisere som appen, trenger du to opplysninger fra Co-op Translator-teamet:
  - **App ID:** Den unike identifikatoren for Co-op Translator-appen. App ID er: `1164076`.
  - **Privat nøkkel:** Du må skaffe **hele innholdet** i `.pem`-filen med privat nøkkel fra kontaktpersonen for vedlikehold. **Behandle denne nøkkelen som et passord og hold den sikker.**

1. Gå videre til Steg 2.

#### **Alternativ B: Bruk din egen tilpassede GitHub App**

- Hvis du ønsker det, kan du opprette og konfigurere din egen GitHub App. Sørg for at den har lese- og skrivetilgang til Contents og Pull requests. Du trenger App ID og en generert privat nøkkel.

### Steg 2: Konfigurer repository-secrets

Du må legge til GitHub App-legitimasjon og AI-tjenestelegitimasjon som krypterte secrets i repository-innstillingene.

1. Gå til repositoryet ditt (f.eks. `PhiCookBook`).

1. Gå til **Settings** > **Secrets and variables** > **Actions**.

1. Under **Repository secrets**, klikk **New repository secret** for hver secret som er listet opp nedenfor.

   ![Velg innstilling action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.no.png)

**Påkrevde secrets (for GitHub App-autentisering):**

| Secret Name          | Beskrivelse                                      | Kilde til verdi                                     |
| :------------------- | :----------------------------------------------- | :-------------------------------------------------- |
| `GH_APP_ID`          | App ID for GitHub App (fra Steg 1).              | GitHub App-innstillinger                            |
| `GH_APP_PRIVATE_KEY` | **Hele innholdet** i den nedlastede `.pem`-filen. | `.pem`-fil (fra Steg 1)                             |

**AI-tjeneste-secrets (legg til ALLE som gjelder ut fra forutsetningene dine):**

| Secret Name                         | Beskrivelse                               | Kilde til verdi                  |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Nøkkel for Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint for Azure AI Service (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Nøkkel for Azure OpenAI-tjeneste              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint for Azure OpenAI-tjeneste         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Ditt Azure OpenAI-modellnavn              | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Ditt Azure OpenAI deployment-navn         | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | API-versjon for Azure OpenAI              | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API-nøkkel for OpenAI                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI-organisasjons-ID                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | Spesifikk OpenAI-modell-ID                  | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | Tilpasset OpenAI API Base URL                | OpenAI Platform                    |

![Skriv inn miljøvariabelnavn](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.no.png)

### Steg 3: Opprett workflow-filen

Til slutt, opprett YAML-filen som definerer den automatiserte workflowen.

1. I rotmappen til repositoryet ditt, opprett `.github/workflows/`-mappen hvis den ikke finnes.

1. Inne i `.github/workflows/`, opprett en fil som heter `co-op-translator.yml`.

1. Lim inn følgende innhold i co-op-translator.yml.

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

4.  **Tilpass workflowen:**
  - **[!IMPORTANT] Mål-språk:** I steget `Run Co-op Translator` må du **gå gjennom og endre listen over språk-koder** i `translate -l "..." -y`-kommandoen slik at den passer til prosjektets behov. Eksempellisten (`ar de es...`) må byttes ut eller tilpasses.
  - **Trigger (`on:`):** Nåværende trigger kjører på hver push til `main`. For store repositories, vurder å legge til en `paths:`-filter (se kommentert eksempel i YAML) for å kun kjøre workflowen når relevante filer (f.eks. kilde-dokumentasjon) endres, for å spare runner-minutter.
  - **PR-detaljer:** Tilpass `commit-message`, `title`, `body`, `branch`-navn og `labels` i steget `Create Pull Request` om nødvendig.

## Håndtering og fornyelse av legitimasjon

- **Sikkerhet:** Oppbevar alltid sensitive legitimasjoner (API-nøkler, private nøkler) som GitHub Actions-secrets. Aldri eksponer dem i workflow-filen eller repository-koden.
- **[!IMPORTANT] Nøkkelfornyelse (interne Microsoft-brukere):** Vær oppmerksom på at Azure OpenAI-nøkkelen brukt internt i Microsoft kan ha obligatorisk fornyelsespolicy (f.eks. hver 5. måned). Sørg for å oppdatere de tilhørende GitHub-secrets (`AZURE_OPENAI_...`-nøkler) **før de utløper** for å unngå feil i workflowen.

## Kjøre workflowen

> [!WARNING]  
> **Tidsbegrensning for GitHub-hosted runner:**  
> GitHub-hostede runnere som `ubuntu-latest` har en **maksimal kjøretid på 6 timer**.  
> For store dokumentasjons-repositories, hvis oversettelsesprosessen tar mer enn 6 timer, vil workflowen automatisk bli avbrutt.  
> For å unngå dette, vurder:  
> - Å bruke en **self-hosted runner** (ingen tidsbegrensning)  
> - Å redusere antall mål-språk per kjøring

Når `co-op-translator.yml`-filen er merget inn i hovedgrenen (eller grenen spesifisert i `on:`-triggeren), vil workflowen automatisk kjøres hver gang det pushes endringer til den grenen (og matcher `paths`-filteret, hvis konfigurert).

Hvis det genereres eller oppdateres oversettelser, vil actionen automatisk opprette en Pull Request med endringene, klar for gjennomgang og merging.

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.