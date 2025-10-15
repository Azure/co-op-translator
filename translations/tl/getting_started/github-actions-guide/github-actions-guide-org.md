<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:44:00+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "tl"
}
-->
# Paggamit ng Co-op Translator GitHub Action (Gabay para sa Organisasyon)

**Sino ang para dito:** Ang gabay na ito ay para sa **mga Microsoft internal na user** o **mga team na may access sa kinakailangang credentials para sa pre-built Co-op Translator GitHub App** o kaya ay makakagawa ng sarili nilang custom GitHub App.

Automatiko mong maisasalin ang dokumentasyon ng iyong repository gamit ang Co-op Translator GitHub Action. Sa gabay na ito, matututunan mo kung paano i-set up ang action para awtomatikong gumawa ng pull request na may updated na salin tuwing may pagbabago sa iyong source Markdown files o mga larawan.

> [!IMPORTANT]
> 
> **Pagpili ng Tamang Gabay:**
>
> Ang gabay na ito ay para sa setup gamit ang **GitHub App ID at Private Key**. Kadalasan, kailangan mo ang "Organization Guide" na paraan kung: **`GITHUB_TOKEN` Permissions ay Limitado:** Ang iyong organisasyon o repository settings ay naglilimita sa default na permissions ng standard `GITHUB_TOKEN`. Halimbawa, kung ang `GITHUB_TOKEN` ay hindi pinapayagan ang kinakailangang `write` permissions (tulad ng `contents: write` o `pull-requests: write`), hindi gagana ang workflow sa [Public Setup Guide](./github-actions-guide-public.md) dahil kulang ang permissions. Ang paggamit ng dedikadong GitHub App na may malinaw na permissions ay nakakaiwas sa limitasyong ito.
>
> **Kung hindi ka apektado ng nasa itaas:**
>
> Kung sapat ang permissions ng standard `GITHUB_TOKEN` sa iyong repository (ibig sabihin, hindi ka na-block ng organizational restrictions), gamitin ang **[Public Setup Guide gamit ang GITHUB_TOKEN](./github-actions-guide-public.md)**. Ang public guide ay hindi nangangailangan ng App IDs o Private Keys at umaasa lang sa standard `GITHUB_TOKEN` at repository permissions.

## Mga Kailangan Bago Magsimula

Bago i-configure ang GitHub Action, siguraduhing handa na ang iyong AI service credentials.

**1. Kailangan: AI Language Model Credentials**
Kailangan mo ng credentials para sa kahit isang suportadong Language Model:

- **Azure OpenAI**: Kailangan ng Endpoint, API Key, Model/Deployment Names, API Version.
- **OpenAI**: Kailangan ng API Key, (Opsyonal: Org ID, Base URL, Model ID).
- Tingnan ang [Supported Models and Services](../../../../README.md) para sa detalye.
- Gabay sa Setup: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Opsyonal: Computer Vision Credentials (para sa Pagsasalin ng Larawan)**

- Kailangan lang kung gusto mong isalin ang text sa loob ng mga larawan.
- **Azure Computer Vision**: Kailangan ng Endpoint at Subscription Key.
- Kung hindi ibinigay, ang action ay magde-default sa [Markdown-only mode](../markdown-only-mode.md).
- Gabay sa Setup: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Setup at Configuration

Sundin ang mga hakbang na ito para i-configure ang Co-op Translator GitHub Action sa iyong repository:

### Hakbang 1: I-install at I-configure ang GitHub App Authentication

Gumagamit ang workflow ng GitHub App authentication para ligtas na makipag-interact sa iyong repository (hal. gumawa ng pull request) para sa iyo. Pumili ng isang opsyon:

#### **Opsyon A: I-install ang Pre-built Co-op Translator GitHub App (para sa Microsoft Internal Use)**

1. Pumunta sa [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) page.

1. Piliin ang **Install** at piliin ang account o organisasyon kung saan naroon ang iyong target repository.

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.tl.png)

1. Piliin ang **Only select repositories** at piliin ang iyong target repository (hal. `PhiCookBook`). I-click ang **Install**. Maaaring hingin ang iyong authentication.

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.tl.png)

1. **Kunin ang App Credentials (Internal Process Required):** Para makapag-authenticate ang workflow bilang app, kailangan mo ng dalawang impormasyon mula sa Co-op Translator team:
  - **App ID:** Ang unique identifier para sa Co-op Translator app. Ang App ID ay: `1164076`.
  - **Private Key:** Kailangan mong kunin ang **buong laman** ng `.pem` private key file mula sa maintainer contact. **Ituring ang key na ito na parang password at panatilihing ligtas.**

1. Magpatuloy sa Hakbang 2.

#### **Opsyon B: Gumamit ng Sarili Mong Custom GitHub App**

- Kung gusto mo, maaari kang gumawa at mag-configure ng sarili mong GitHub App. Siguraduhing may Read & write access ito sa Contents at Pull requests. Kailangan mo ang App ID at generated Private Key nito.

### Hakbang 2: I-configure ang Repository Secrets

Kailangan mong idagdag ang GitHub App credentials at AI service credentials bilang encrypted secrets sa iyong repository settings.

1. Pumunta sa iyong target GitHub repository (hal. `PhiCookBook`).

1. Pumunta sa **Settings** > **Secrets and variables** > **Actions**.

1. Sa ilalim ng **Repository secrets**, i-click ang **New repository secret** para sa bawat secret na nakalista sa ibaba.

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.tl.png)

**Mga Kailangan na Secret (para sa GitHub App Authentication):**

| Secret Name          | Description                                      | Value Source                                     |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | App ID ng GitHub App (mula Hakbang 1).           | GitHub App Settings                              |
| `GH_APP_PRIVATE_KEY` | **Buong laman** ng na-download na `.pem` file.   | `.pem` file (mula Hakbang 1)                     |

**AI Service Secrets (Idagdag LAHAT ng naaangkop base sa iyong Prerequisites):**

| Secret Name                         | Description                               | Value Source                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Key para sa Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint para sa Azure AI Service (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Key para sa Azure OpenAI service              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint para sa Azure OpenAI service         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI Model Name mo                   | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI Deployment Name mo              | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | API Version para sa Azure OpenAI              | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API Key para sa OpenAI                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                        | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | Specific OpenAI model ID                      | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL                    | OpenAI Platform                    |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.tl.png)

### Hakbang 3: Gumawa ng Workflow File

Sa huli, gumawa ng YAML file na magde-define ng automated workflow.

1. Sa root directory ng iyong repository, gumawa ng `.github/workflows/` directory kung wala pa ito.

1. Sa loob ng `.github/workflows/`, gumawa ng file na ang pangalan ay `co-op-translator.yml`.

1. I-paste ang sumusunod na content sa co-op-translator.yml.

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

4.  **I-customize ang Workflow:**
  - **[!IMPORTANT] Target Languages:** Sa `Run Co-op Translator` step, **KAILANGAN mong i-review at baguhin ang listahan ng language codes** sa loob ng `translate -l "..." -y` command para tumugma sa requirements ng iyong proyekto. Palitan o i-adjust ang example list (`ar de es...`) ayon sa kailangan.
  - **Trigger (`on:`):** Ang kasalukuyang trigger ay tumatakbo sa bawat push sa `main`. Para sa malalaking repository, magdagdag ng `paths:` filter (tingnan ang naka-comment na example sa YAML) para tumakbo lang ang workflow kapag may pagbabago sa relevant files (hal. source documentation), para makatipid sa runner minutes.
  - **PR Details:** I-customize ang `commit-message`, `title`, `body`, `branch` name, at `labels` sa `Create Pull Request` step kung kinakailangan.

## Pamamahala at Pag-renew ng Credentials

- **Seguridad:** Laging itago ang sensitibong credentials (API keys, private keys) bilang GitHub Actions secrets. Huwag kailanman ilantad ang mga ito sa workflow file o repository code.
- **[!IMPORTANT] Key Renewal (Microsoft Internal Users):** Tandaan na ang Azure OpenAI key na ginagamit sa loob ng Microsoft ay maaaring may mandatory renewal policy (hal. bawat 5 buwan). Siguraduhing i-update ang kaukulang GitHub secrets (`AZURE_OPENAI_...` keys) **bago mag-expire** para maiwasan ang workflow failures.

## Pagpapatakbo ng Workflow

> [!WARNING]  
> **GitHub-hosted Runner Time Limit:**  
> Ang mga GitHub-hosted runner tulad ng `ubuntu-latest` ay may **maximum execution time limit na 6 na oras**.  
> Para sa malalaking documentation repositories, kung lalampas sa 6 na oras ang translation process, awtomatikong ititigil ang workflow.  
> Para maiwasan ito, maaaring:  
> - Gumamit ng **self-hosted runner** (walang time limit)  
> - Bawasan ang bilang ng target languages kada run

Kapag na-merge na ang `co-op-translator.yml` file sa iyong main branch (o sa branch na nakasaad sa `on:` trigger), awtomatikong tatakbo ang workflow tuwing may changes na ipu-push sa branch na iyon (at tumutugma sa `paths` filter, kung naka-configure).

Kung may mga bagong salin o na-update, awtomatikong gagawa ng Pull Request ang action na naglalaman ng mga pagbabago, handa na para sa iyong review at pag-merge.

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.