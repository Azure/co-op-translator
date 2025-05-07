<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-05-07T14:08:36+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "br"
}
-->
# Oberer ar Co-op Translator GitHub Action (Setu Public)

**Kiberoù Cible:** Ar roll-mañ zo bet graet evit implijerien er meur a repositorioù publik pe prevez ma vez mat an aotreadennoù standard GitHub Actions. E implij ar token en-dro `GITHUB_TOKEN`.

Automatize an treuzskrivadur eus ho restradur er repo dreist-holl gant ar Co-op Translator GitHub Action. Ar roll-mañ a zispleg penaos lakaat ar workflow da grouiñ pull requests gant treuzskrivadurioù hizivaet pa vez kemmoù er restroù Markdown pe skeudennoù.

> [!IMPORTANT]
>
> **Dibab ar Roll Sevel Mat:**
>
> Ar roll-mañ a zispleg ar **stumm aes gant ar token en-dro `GITHUB_TOKEN`**. Se eo ar mod en em vodañ evit ar muiañ a implijerien abalamour ma n’eo ket ret merañ klemmioù prevez GitHub App.
>

## Palioù Goude

A-raok krouiñ ar GitHub Action, gwiriit ez eus an titouroù rekis evit ar servij AI prest.

**1. Rekis: Titouroù kredadoù Model Yezh AI**  
Ret eo bezañ kredadoù evit un nebeud modeloù yezh a zo bet degemeret:

- **Azure OpenAI**: Ret eo Endpoint, API Key, anvioù Model/Deployment, hag API Version.
- **OpenAI**: Ret eo API Key, (Dibarzh: Org ID, Base URL, Model ID).
- Gwiriañ [Supported Models and Services](../../../../README.md) evit muioc’h a ditouroù.

**2. Dibab: Kredadoù AI Vision (evit Treuzskrivadur Skeudennoù)**

- Ret eo nemet ma fell deoc’h treuzskrivañ destenn e skeudennoù.
- **Azure AI Vision**: Ret eo Endpoint hag Subscription Key.
- Ma n’int ket kinniget, e vo implijet ar [Markdown-only mode](../markdown-only-mode.md).

## Sevel ha Krouiñ

Heuliañ an hentenn-mañ evit krouiñ ar Co-op Translator GitHub Action er repo gant ar token en-dro `GITHUB_TOKEN`.

### Pleg 1: Kompren an Aozañ (Implij ar `GITHUB_TOKEN`)

Ar workflow-mañ a implij ar token en-dro `GITHUB_TOKEN` savet gant GitHub Actions. Ar token-mañ a ro aotreetoù d’ar workflow da labourat war ho repo hervez ar mouezhioù aozet er **Pleg 3**.

### Pleg 2: Krouiñ ar Sekredoù Repository

Ret eo ouzhpennañ ho **titouroù kredadoù servij AI** evel sekredoù krouet en aozadurioù ho repo.

1. Mont d’an repo GitHub a fell deoc’h implijout.
2. Mont da **Settings** > **Secrets and variables** > **Actions**.
3. E-barzh **Repository secrets**, klikit war **New repository secret** evit pep sekred AI rekis anezhañ.

![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(Skeudenn evit diskouez pelec’h ouzhpennañ sekredoù)*

**Sekredoù AI Rekis (Ouzhpennit AN HOLL hervez ho Palioù Goude):**

| Secret Name                         | Deskrivadur                             | Mamenn ar Valuer                |
| :---------------------------------- | :------------------------------------- | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Klenn Azure AI Service (Computer Vision) | Ho Azure AI Foundry             |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint Azure AI Service (Computer Vision) | Ho Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`              | Klenn servij Azure OpenAI              | Ho Azure AI Foundry             |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint servij Azure OpenAI           | Ho Azure AI Foundry             |
| `AZURE_OPENAI_MODEL_NAME`           | Anv Model Azure OpenAI                  | Ho Azure AI Foundry             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Anv Deployment Azure OpenAI             | Ho Azure AI Foundry             |
| `AZURE_OPENAI_API_VERSION`          | API Version Azure OpenAI                | Ho Azure AI Foundry             |
| `OPENAI_API_KEY`                    | API Key OpenAI                         | Ho OpenAI Platform             |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Dibarzh)       | Ho OpenAI Platform             |
| `OPENAI_CHAT_MODEL_ID`              | Model ID resis OpenAI (Dibarzh)         | Ho OpenAI Platform             |
| `OPENAI_BASE_URL`                   | URL Diazez API OpenAI kevrinus (Dibarzh) | Ho OpenAI Platform             |

### Pleg 3: Krouiñ Aotreoù Workflow

Ret eo reiñ aotreoù d’ar GitHub Action dre ar token en-dro `GITHUB_TOKEN` evit gallout tapout an kod ha krouiñ pull requests.

1. Er repo, mont da **Settings** > **Actions** > **General**.
2. Skrola da benn da **Workflow permissions**.
3. Dibabit **Read and write permissions**. Se a ro d’ar token en-dro `GITHUB_TOKEN` an aotreoù rekis evit `contents: write` ha `pull-requests: write` evit ar workflow-mañ.
4. Gwiriit e vez lakaet ar marc’henn war **Allow GitHub Actions to create and approve pull requests**.
5. Klikit **Save**.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### Pleg 4: Krouiñ ar Restr Workflow

En diwezhañ, krouit ar restr YAML a zispleg ar workflow awtomatek gant ar token en-dro `GITHUB_TOKEN`.

1. Er rouedad micherel eus ho repo, krouit an dir `.github/workflows/` ma ne vo ket bet savet c’hoazh.
2. E-barzh `.github/workflows/`, krouit un restr anvet `co-op-translator.yml`.
3. Lakait ar mennozhioù da-heul e-barzh `co-op-translator.yml`.

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
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
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
4. **Personalisit ar Workflow:**  
  - **[!IMPORTANT] Yezhoù Cible:** Er pal `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` ma vez ezhomm.

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.