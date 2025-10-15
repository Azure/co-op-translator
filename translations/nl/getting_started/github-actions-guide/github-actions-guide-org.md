<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:30:47+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "nl"
}
-->
# De Co-op Translator GitHub Action gebruiken (Organisatiehandleiding)

**Doelgroep:** Deze handleiding is bedoeld voor **interne Microsoft-gebruikers** of **teams die toegang hebben tot de benodigde inloggegevens voor de vooraf gebouwde Co-op Translator GitHub App** of hun eigen aangepaste GitHub App kunnen aanmaken.

Automatiseer eenvoudig de vertaling van de documentatie in je repository met de Co-op Translator GitHub Action. Deze handleiding legt uit hoe je de actie instelt zodat er automatisch pull requests worden aangemaakt met bijgewerkte vertalingen zodra je bron-Markdownbestanden of afbeeldingen wijzigen.

> [!IMPORTANT]
> 
> **De juiste handleiding kiezen:**
>
> Deze handleiding beschrijft de installatie met een **GitHub App ID en een Private Key**. Je hebt deze "Organisatiehandleiding" meestal nodig als: **`GITHUB_TOKEN`-machtigingen zijn beperkt:** De instellingen van je organisatie of repository beperken de standaardmachtigingen van de `GITHUB_TOKEN`. Als de `GITHUB_TOKEN` niet de benodigde `write`-machtigingen heeft (zoals `contents: write` of `pull-requests: write`), zal de workflow in de [Openbare Installatiehandleiding](./github-actions-guide-public.md) mislukken vanwege onvoldoende rechten. Door een speciale GitHub App te gebruiken met expliciet toegekende rechten, omzeil je deze beperking.
>
> **Als bovenstaande niet op jou van toepassing is:**
>
> Als de standaard `GITHUB_TOKEN` voldoende rechten heeft in je repository (dus je wordt niet geblokkeerd door organisatiebeperkingen), gebruik dan de **[Openbare Installatiehandleiding met GITHUB_TOKEN](./github-actions-guide-public.md)**. De openbare handleiding vereist geen App ID's of Private Keys en gebruikt alleen de standaard `GITHUB_TOKEN` en repositoryrechten.

## Vereisten

Zorg dat je de benodigde AI-service-inloggegevens hebt voordat je de GitHub Action configureert.

**1. Vereist: AI Language Model-inloggegevens**
Je hebt inloggegevens nodig voor ten minste één ondersteund Language Model:

- **Azure OpenAI**: Vereist Endpoint, API Key, Model/Deployment-namen, API-versie.
- **OpenAI**: Vereist API Key, (optioneel: Org ID, Base URL, Model ID).
- Zie [Ondersteunde modellen en services](../../../../README.md) voor details.
- Installatiehandleiding: [Azure OpenAI instellen](../set-up-resources/set-up-azure-openai.md).

**2. Optioneel: Computer Vision-inloggegevens (voor beeldvertaling)**

- Alleen nodig als je tekst in afbeeldingen wilt vertalen.
- **Azure Computer Vision**: Vereist Endpoint en Subscription Key.
- Als je deze niet opgeeft, werkt de actie standaard in de [alleen-Markdown-modus](../markdown-only-mode.md).
- Installatiehandleiding: [Azure Computer Vision instellen](../set-up-resources/set-up-azure-computer-vision.md).

## Installatie en Configuratie

Volg deze stappen om de Co-op Translator GitHub Action in je repository te configureren:

### Stap 1: Installeer en configureer GitHub App-authenticatie

De workflow gebruikt GitHub App-authenticatie om veilig namens jou met je repository te werken (zoals pull requests aanmaken). Kies een van de volgende opties:

#### **Optie A: Installeer de vooraf gebouwde Co-op Translator GitHub App (voor intern Microsoft-gebruik)**

1. Ga naar de pagina van de [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Klik op **Installeren** en selecteer het account of de organisatie waar je doelrepository zich bevindt.

    ![App installeren](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.nl.png)

1. Kies **Alleen geselecteerde repositories** en selecteer je doelrepository (bijvoorbeeld `PhiCookBook`). Klik op **Installeren**. Je moet mogelijk inloggen.

    ![Installatie autoriseren](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.nl.png)

1. **Verkrijg App-inloggegevens (intern proces vereist):** Om de workflow als de app te laten authenticeren, heb je twee gegevens nodig van het Co-op Translator-team:
  - **App ID:** De unieke identificatie van de Co-op Translator app. De App ID is: `1164076`.
  - **Private Key:** Je moet de **volledige inhoud** van het `.pem`-private key-bestand verkrijgen van de beheerder. **Behandel deze sleutel als een wachtwoord en houd hem veilig.**

1. Ga verder met Stap 2.

#### **Optie B: Gebruik je eigen aangepaste GitHub App**

- Je kunt ook je eigen GitHub App aanmaken en configureren. Zorg dat deze Lezen & schrijven-toegang heeft tot Inhoud en Pull requests. Je hebt de App ID en een gegenereerde Private Key nodig.

### Stap 2: Repository Secrets configureren

Je moet de GitHub App-inloggegevens en je AI-service-inloggegevens toevoegen als versleutelde secrets in de repository-instellingen.

1. Ga naar je doelrepository op GitHub (bijvoorbeeld `PhiCookBook`).

1. Ga naar **Instellingen** > **Secrets en variabelen** > **Actions**.

1. Klik onder **Repository secrets** op **Nieuw repository secret** voor elk secret hieronder.

   ![Selecteer setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.nl.png)

**Vereiste secrets (voor GitHub App-authenticatie):**

| Secretnaam           | Beschrijving                                      | Herkomst waarde                                   |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | De App ID van de GitHub App (van Stap 1).        | GitHub App-instellingen                          |
| `GH_APP_PRIVATE_KEY` | De **volledige inhoud** van het gedownloade `.pem`-bestand. | `.pem`-bestand (van Stap 1)                  |

**AI-service secrets (voeg ALLES toe wat van toepassing is op basis van je vereisten):**

| Secretnaam                          | Beschrijving                                 | Herkomst waarde                 |
| :---------------------------------- | :------------------------------------------- | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Sleutel voor Azure AI Service (Computer Vision)  | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint voor Azure AI Service (Computer Vision) | Azure AI Foundry                |
| `AZURE_OPENAI_API_KEY`              | Sleutel voor Azure OpenAI-service            | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint voor Azure OpenAI-service           | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`           | Jouw Azure OpenAI Modelnaam                  | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Jouw Azure OpenAI Deploymentnaam             | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`          | API-versie voor Azure OpenAI                 | Azure AI Foundry                |
| `OPENAI_API_KEY`                    | API Key voor OpenAI                          | OpenAI Platform                 |
| `OPENAI_ORG_ID`                     | OpenAI Organisatie-ID                        | OpenAI Platform                 |
| `OPENAI_CHAT_MODEL_ID`              | Specifieke OpenAI model-ID                   | OpenAI Platform                 |
| `OPENAI_BASE_URL`                   | Aangepaste OpenAI API Base URL               | OpenAI Platform                 |

![Voer omgevingsvariabelenaam in](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.nl.png)

### Stap 3: Maak het workflowbestand aan

Maak tot slot het YAML-bestand dat de geautomatiseerde workflow definieert.

1. Maak in de hoofdmap van je repository de map `.github/workflows/` aan als deze nog niet bestaat.

1. Maak in `.github/workflows/` een bestand aan met de naam `co-op-translator.yml`.

1. Plak de volgende inhoud in co-op-translator.yml.

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

4.  **Pas de workflow aan:**
  - **[!IMPORTANT] Doeltalen:** In de stap `Run Co-op Translator` moet je **de lijst met taalcodes in het commando `translate -l "..." -y` controleren en aanpassen** aan de behoeften van je project. De voorbeeldlijst (`ar de es...`) moet je vervangen of aanpassen.
  - **Trigger (`on:`):** De huidige trigger draait bij elke push naar `main`. Voor grote repositories kun je een `paths:`-filter toevoegen (zie het uit-gecommentarieerde voorbeeld in de YAML) zodat de workflow alleen draait als relevante bestanden (zoals bron-documentatie) wijzigen, om runner-minuten te besparen.
  - **PR-details:** Pas indien nodig het `commit-message`, `title`, `body`, de `branch`-naam en `labels` aan in de stap `Create Pull Request`.

## Beheer en vernieuwing van inloggegevens

- **Beveiliging:** Sla gevoelige inloggegevens (API-sleutels, private keys) altijd op als GitHub Actions-secrets. Zet ze nooit in je workflowbestand of code.
- **[!IMPORTANT] Sleutelvernieuwing (interne Microsoft-gebruikers):** Houd er rekening mee dat de Azure OpenAI-sleutel binnen Microsoft mogelijk een verplichte vernieuwing heeft (bijvoorbeeld elke 5 maanden). Werk de bijbehorende GitHub-secrets (`AZURE_OPENAI_...`-sleutels) **op tijd bij** om workflowfouten te voorkomen.

## De workflow uitvoeren

> [!WARNING]  
> **Tijdslimiet voor GitHub-hosted runner:**  
> GitHub-hosted runners zoals `ubuntu-latest` hebben een **maximale uitvoeringstijd van 6 uur**.  
> Voor grote documentatierepositories wordt het vertaalproces automatisch gestopt als het langer dan 6 uur duurt.  
> Om dit te voorkomen kun je:  
> - Een **self-hosted runner** gebruiken (geen tijdslimiet)  
> - Het aantal doeltalen per run verminderen

Zodra het bestand `co-op-translator.yml` is samengevoegd in je hoofdbranch (of de branch die is opgegeven in de `on:`-trigger), wordt de workflow automatisch uitgevoerd wanneer er wijzigingen naar die branch worden gepusht (en overeenkomen met het `paths`-filter, als dat is ingesteld).

Als er vertalingen worden aangemaakt of bijgewerkt, maakt de actie automatisch een Pull Request aan met de wijzigingen, klaar voor jouw review en samenvoeging.

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.