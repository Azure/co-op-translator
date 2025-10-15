<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:44:18+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "tl"
}
-->
# Paggamit ng Co-op Translator GitHub Action (Pampublikong Setup)

**Para Kanino:** Ang gabay na ito ay para sa mga gumagamit ng karamihan sa mga pampubliko o pribadong repository kung saan sapat na ang karaniwang GitHub Actions permissions. Ginagamit nito ang built-in na `GITHUB_TOKEN`.

I-automate ang pagsasalin ng dokumentasyon ng iyong repository nang madali gamit ang Co-op Translator GitHub Action. Tuturuan ka ng gabay na ito kung paano i-setup ang action para awtomatikong gumawa ng pull request na may updated na mga salin tuwing may pagbabago sa iyong source Markdown files o mga larawan.

> [!IMPORTANT]
>
> **Pagpili ng Tamang Gabay:**
>
> Detalyado sa gabay na ito ang **mas simpleng setup gamit ang karaniwang `GITHUB_TOKEN`**. Ito ang inirerekomendang paraan para sa karamihan ng mga user dahil hindi na kailangan pang mag-manage ng sensitibong GitHub App Private Keys.
>

## Mga Kailangan Bago Magsimula

Bago i-configure ang GitHub Action, siguraduhing handa na ang iyong AI service credentials.

**1. Kailangan: AI Language Model Credentials**
Kailangan mo ng credentials para sa kahit isang suportadong Language Model:

- **Azure OpenAI**: Kailangan ng Endpoint, API Key, Model/Deployment Names, API Version.
- **OpenAI**: Kailangan ng API Key, (Opsyonal: Org ID, Base URL, Model ID).
- Tingnan ang [Supported Models and Services](../../../../README.md) para sa detalye.

**2. Opsyonal: AI Vision Credentials (para sa Pagsasalin ng Larawan)**

- Kailangan lang kung gusto mong isalin ang teksto sa loob ng mga larawan.
- **Azure AI Vision**: Kailangan ng Endpoint at Subscription Key.
- Kung hindi ibinigay, ang action ay magde-default sa [Markdown-only mode](../markdown-only-mode.md).

## Setup at Configuration

Sundin ang mga hakbang na ito para i-configure ang Co-op Translator GitHub Action sa iyong repository gamit ang karaniwang `GITHUB_TOKEN`.

### Hakbang 1: Unawain ang Authentication (Gamit ang `GITHUB_TOKEN`)

Gamit ng workflow na ito ang built-in na `GITHUB_TOKEN` na ibinibigay ng GitHub Actions. Awtomatikong binibigyan ng token na ito ng pahintulot ang workflow na makipag-interact sa iyong repository base sa settings na iaayos sa **Hakbang 3**.

### Hakbang 2: I-configure ang Repository Secrets

Kailangan mo lang idagdag ang iyong **AI service credentials** bilang encrypted secrets sa settings ng iyong repository.

1.  Pumunta sa iyong target na GitHub repository.
2.  Pumunta sa **Settings** > **Secrets and variables** > **Actions**.
3.  Sa ilalim ng **Repository secrets**, i-click ang **New repository secret** para sa bawat kinakailangang AI service secret na nakalista sa ibaba.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.tl.png) *(Reference ng Larawan: Ipinapakita kung saan magdagdag ng secrets)*

**Mga Kailangan na AI Service Secrets (Idagdag LAHAT ng naaangkop base sa iyong Mga Kailangan):**

| Secret Name                         | Deskripsyon                               | Pinagmulan ng Value                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Key para sa Azure AI Service (Computer Vision)  | Iyong Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint para sa Azure AI Service (Computer Vision) | Iyong Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Key para sa Azure OpenAI service              | Iyong Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint para sa Azure OpenAI service         | Iyong Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Iyong Azure OpenAI Model Name              | Iyong Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Iyong Azure OpenAI Deployment Name         | Iyong Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | API Version para sa Azure OpenAI              | Iyong Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key para sa OpenAI                        | Iyong OpenAI Platform              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Opsyonal)         | Iyong OpenAI Platform              |
| `OPENAI_CHAT_MODEL_ID`              | Specific OpenAI model ID (Opsyonal)       | Iyong OpenAI Platform              |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL (Opsyonal)     | Iyong OpenAI Platform              |

### Hakbang 3: I-configure ang Workflow Permissions

Kailangan ng GitHub Action ng pahintulot mula sa `GITHUB_TOKEN` para mag-check out ng code at gumawa ng pull requests.

1.  Sa iyong repository, pumunta sa **Settings** > **Actions** > **General**.
2.  Mag-scroll pababa sa seksyong **Workflow permissions**.
3.  Piliin ang **Read and write permissions**. Bibigyan nito ang `GITHUB_TOKEN` ng kinakailangang `contents: write` at `pull-requests: write` permissions para sa workflow na ito.
4.  Siguraduhing naka-check ang checkbox para sa **Allow GitHub Actions to create and approve pull requests**.
5.  Piliin ang **Save**.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.tl.png)

### Hakbang 4: Gumawa ng Workflow File

Sa huli, gumawa ng YAML file na magde-define ng automated workflow gamit ang `GITHUB_TOKEN`.

1.  Sa root directory ng iyong repository, gumawa ng `.github/workflows/` directory kung wala pa ito.
2.  Sa loob ng `.github/workflows/`, gumawa ng file na pinangalanang `co-op-translator.yml`.
3.  I-paste ang sumusunod na content sa `co-op-translator.yml`.

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
4.  **I-customize ang Workflow:**
  - **[!IMPORTANT] Target Languages:** Sa step na `Run Co-op Translator`, **KAILANGAN mong i-review at baguhin ang listahan ng language codes** sa loob ng `translate -l "..." -y` command para tumugma sa requirements ng iyong proyekto. Ang example list (`ar de es...`) ay kailangang palitan o i-adjust.
  - **Trigger (`on:`):** Ang kasalukuyang trigger ay tumatakbo sa bawat push sa `main`. Para sa malalaking repository, maaaring magdagdag ng `paths:` filter (tingnan ang naka-comment na example sa YAML) para tumakbo lang ang workflow kapag may pagbabago sa mga relevant na files (hal. source documentation), para makatipid sa runner minutes.
  - **PR Details:** I-customize ang `commit-message`, `title`, `body`, `branch` name, at `labels` sa step na `Create Pull Request` kung kinakailangan.

## Pagpapatakbo ng Workflow

> [!WARNING]  
> **Limitasyon sa Oras ng GitHub-hosted Runner:**  
> Ang mga GitHub-hosted runner tulad ng `ubuntu-latest` ay may **maximum execution time limit na 6 na oras**.  
> Para sa malalaking documentation repository, kung lalampas sa 6 na oras ang translation process, awtomatikong ititigil ang workflow.  
> Para maiwasan ito, maaaring:  
> - Gumamit ng **self-hosted runner** (walang time limit)  
> - Bawasan ang bilang ng target languages kada run

Kapag na-merge na ang `co-op-translator.yml` file sa iyong main branch (o sa branch na nakasaad sa `on:` trigger), awtomatikong tatakbo ang workflow tuwing may changes na ipu-push sa branch na iyon (at tumutugma sa `paths` filter, kung naka-configure).

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.