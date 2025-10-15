<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:31:11+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "nl"
}
-->
# De Co-op Translator GitHub Action gebruiken (Openbare Setup)

**Doelgroep:** Deze handleiding is bedoeld voor gebruikers in de meeste openbare of privé-repositories waar standaard GitHub Actions-machtigingen voldoende zijn. Er wordt gebruikgemaakt van de ingebouwde `GITHUB_TOKEN`.

Automatiseer eenvoudig de vertaling van de documentatie in je repository met de Co-op Translator GitHub Action. Deze handleiding legt uit hoe je de actie instelt zodat er automatisch pull requests worden aangemaakt met bijgewerkte vertalingen telkens wanneer je bron-Markdownbestanden of afbeeldingen wijzigen.

> [!IMPORTANT]
>
> **De juiste handleiding kiezen:**
>
> Deze handleiding beschrijft de **eenvoudigere setup met de standaard `GITHUB_TOKEN`**. Dit is de aanbevolen methode voor de meeste gebruikers, omdat je dan geen gevoelige GitHub App Private Keys hoeft te beheren.
>

## Vereisten

Zorg ervoor dat je de benodigde AI-servicegegevens bij de hand hebt voordat je de GitHub Action configureert.

**1. Vereist: AI Language Model-gegevens**
Je hebt gegevens nodig voor ten minste één ondersteund Language Model:

- **Azure OpenAI**: Vereist Endpoint, API Key, Model/Deployment-namen, API-versie.
- **OpenAI**: Vereist API Key, (Optioneel: Org ID, Base URL, Model ID).
- Zie [Ondersteunde modellen en services](../../../../README.md) voor details.

**2. Optioneel: AI Vision-gegevens (voor beeldvertaling)**

- Alleen nodig als je tekst in afbeeldingen wilt vertalen.
- **Azure AI Vision**: Vereist Endpoint en Subscription Key.
- Als je deze niet opgeeft, werkt de actie standaard in de [Markdown-only modus](../markdown-only-mode.md).

## Installatie en Configuratie

Volg deze stappen om de Co-op Translator GitHub Action in je repository te configureren met de standaard `GITHUB_TOKEN`.

### Stap 1: Begrijp Authenticatie (Gebruik van `GITHUB_TOKEN`)

Deze workflow gebruikt de ingebouwde `GITHUB_TOKEN` die door GitHub Actions wordt geleverd. Deze token geeft de workflow automatisch de juiste rechten om met je repository te werken, afhankelijk van de instellingen die je in **Stap 3** configureert.

### Stap 2: Repository Secrets instellen

Je hoeft alleen je **AI-servicegegevens** toe te voegen als versleutelde secrets in de repository-instellingen.

1.  Ga naar je doel-GitHub-repository.
2.  Ga naar **Settings** > **Secrets and variables** > **Actions**.
3.  Onder **Repository secrets** klik je voor elk benodigde AI-service secret hieronder op **New repository secret**.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.nl.png" alt="Select setting action"> *(Afbeeldingsreferentie: toont waar je secrets toevoegt)*

**Benodigde AI Service Secrets (voeg ALLES toe wat van toepassing is op basis van je vereisten):**

| Secret Name                         | Beschrijving                               | Waarde bron                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Sleutel voor Azure AI Service (Computer Vision)  | Je Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint voor Azure AI Service (Computer Vision) | Je Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Sleutel voor Azure OpenAI service              | Je Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint voor Azure OpenAI service         | Je Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Je Azure OpenAI Modelnaam                  | Je Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Je Azure OpenAI Deploymentnaam             | Je Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | API-versie voor Azure OpenAI               | Je Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key voor OpenAI                        | Je OpenAI Platform                |
| `OPENAI_ORG_ID`                     | OpenAI Organisatie-ID (optioneel)          | Je OpenAI Platform                |
| `OPENAI_CHAT_MODEL_ID`              | Specifieke OpenAI model-ID (optioneel)     | Je OpenAI Platform                |
| `OPENAI_BASE_URL`                   | Aangepaste OpenAI API Base URL (optioneel) | Je OpenAI Platform                |

### Stap 3: Workflow-machtigingen instellen

De GitHub Action heeft rechten nodig via de `GITHUB_TOKEN` om code te kunnen ophalen en pull requests aan te maken.

1.  Ga in je repository naar **Settings** > **Actions** > **General**.
2.  Scroll naar het gedeelte **Workflow permissions**.
3.  Selecteer **Read and write permissions**. Hiermee krijgt de `GITHUB_TOKEN` de benodigde `contents: write` en `pull-requests: write` rechten voor deze workflow.
4.  Zorg dat het selectievakje bij **Allow GitHub Actions to create and approve pull requests** is **aangevinkt**.
5.  Klik op **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.nl.png" alt="Permission setting">

### Stap 4: Maak het Workflow-bestand aan

Maak tot slot het YAML-bestand aan dat de geautomatiseerde workflow definieert met `GITHUB_TOKEN`.

1.  Maak in de hoofdmap van je repository de map `.github/workflows/` aan als deze nog niet bestaat.
2.  Maak in `.github/workflows/` een bestand aan met de naam `co-op-translator.yml`.
3.  Plak de volgende inhoud in `co-op-translator.yml`.

```yaml
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
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
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

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
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
4.  **Pas de Workflow aan:**
  - **[!IMPORTANT] Doeltalen:** In de stap `Run Co-op Translator` moet je **de lijst met taalcodes in het commando** `translate -l "..." -y` **controleren en aanpassen** aan de behoeften van jouw project. De voorbeeldlijst (`ar de es...`) moet worden vervangen of aangepast.
  - **Trigger (`on:`):** De huidige trigger draait bij elke push naar `main`. Voor grote repositories kun je overwegen een `paths:` filter toe te voegen (zie het uit-gecommentarieerde voorbeeld in de YAML) zodat de workflow alleen draait als relevante bestanden (zoals bron-documentatie) wijzigen, om runner-minuten te besparen.
  - **PR-details:** Pas indien nodig het `commit-message`, de `title`, `body`, `branch`-naam en `labels` aan in de stap `Create Pull Request`.

## De Workflow uitvoeren

> [!WARNING]  
> **Tijdslimiet voor GitHub-hosted Runner:**  
> GitHub-hosted runners zoals `ubuntu-latest` hebben een **maximale uitvoeringstijd van 6 uur**.  
> Voor grote documentatierepositories geldt dat als het vertaalproces langer dan 6 uur duurt, de workflow automatisch wordt gestopt.  
> Om dit te voorkomen kun je:  
> - Een **self-hosted runner** gebruiken (geen tijdslimiet)  
> - Het aantal doeltalen per run verminderen

Zodra het bestand `co-op-translator.yml` is samengevoegd in je hoofdbranch (of de branch die is opgegeven in de `on:` trigger), wordt de workflow automatisch uitgevoerd telkens wanneer er wijzigingen naar die branch worden gepusht (en overeenkomen met het `paths` filter, indien ingesteld).

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.