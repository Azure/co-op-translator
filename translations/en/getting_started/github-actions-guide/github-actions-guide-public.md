<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T02:06:56+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "en"
}
-->
# Using the Co-op Translator GitHub Action (Public Setup)

**Target Audience:** This guide is for users in most public or private repositories where standard GitHub Actions permissions are enough. It uses the built-in `GITHUB_TOKEN`.

Easily automate the translation of your repository’s documentation with the Co-op Translator GitHub Action. This guide shows you how to set up the action so it automatically creates pull requests with updated translations whenever your source Markdown files or images change.

> [!IMPORTANT]
>
> **Choosing the Right Guide:**
>
> This guide explains the **simpler setup using the standard `GITHUB_TOKEN`**. This is recommended for most users since you don’t need to manage sensitive GitHub App Private Keys.
>

## Prerequisites

Before you set up the GitHub Action, make sure you have the necessary AI service credentials.

**1. Required: AI Language Model Credentials**
You’ll need credentials for at least one supported Language Model:

- **Azure OpenAI**: Needs Endpoint, API Key, Model/Deployment Names, API Version.
- **OpenAI**: Needs API Key, (Optional: Org ID, Base URL, Model ID).
- See [Supported Models and Services](../../../../README.md) for more info.

**2. Optional: AI Vision Credentials (for Image Translation)**

- Only needed if you want to translate text inside images.
- **Azure AI Vision**: Needs Endpoint and Subscription Key.
- If you don’t provide these, the action defaults to [Markdown-only mode](../markdown-only-mode.md).

## Setup and Configuration

Follow these steps to set up the Co-op Translator GitHub Action in your repository using the standard `GITHUB_TOKEN`.

### Step 1: Understand Authentication (Using `GITHUB_TOKEN`)

This workflow uses the built-in `GITHUB_TOKEN` that GitHub Actions provides. This token automatically gives the workflow permission to interact with your repository, based on the settings you configure in **Step 3**.

### Step 2: Configure Repository Secrets

You only need to add your **AI service credentials** as encrypted secrets in your repository settings.

1.  Go to your target GitHub repository.
2.  Navigate to **Settings** > **Secrets and variables** > **Actions**.
3.  Under **Repository secrets**, click **New repository secret** for each required AI service secret listed below.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.en.png) *(Image Reference: Shows where to add secrets)*

**Required AI Service Secrets (Add ALL that apply based on your Prerequisites):**

| Secret Name                         | Description                               | Value Source                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Key for Azure AI Service (Computer Vision)  | Your Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint for Azure AI Service (Computer Vision) | Your Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Key for Azure OpenAI service              | Your Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint for Azure OpenAI service         | Your Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Your Azure OpenAI Model Name              | Your Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Your Azure OpenAI Deployment Name         | Your Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | API Version for Azure OpenAI              | Your Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key for OpenAI                        | Your OpenAI Platform              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Optional)         | Your OpenAI Platform              |
| `OPENAI_CHAT_MODEL_ID`              | Specific OpenAI model ID (Optional)       | Your OpenAI Platform              |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL (Optional)     | Your OpenAI Platform              |

### Step 3: Configure Workflow Permissions

The GitHub Action needs permissions via the `GITHUB_TOKEN` to check out code and create pull requests.

1.  In your repository, go to **Settings** > **Actions** > **General**.
2.  Scroll down to the **Workflow permissions** section.
3.  Select **Read and write permissions**. This gives the `GITHUB_TOKEN` the needed `contents: write` and `pull-requests: write` permissions for this workflow.
4.  Make sure the checkbox for **Allow GitHub Actions to create and approve pull requests** is **checked**.
5.  Click **Save**.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.en.png)

### Step 4: Create the Workflow File

Finally, create the YAML file that defines the automated workflow using `GITHUB_TOKEN`.

1.  In the root directory of your repository, create the `.github/workflows/` directory if it doesn’t exist.
2.  Inside `.github/workflows/`, create a file named `co-op-translator.yml`.
3.  Paste the following content into `co-op-translator.yml`.

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
4.  **Customize the Workflow:**
  - **[!IMPORTANT] Target Languages:** In the `Run Co-op Translator` step, you **MUST review and change the list of language codes** in the `translate -l "..." -y` command to fit your project’s needs. The example list (`ar de es...`) should be replaced or updated.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see the commented example in the YAML) so the workflow only runs when relevant files (like source documentation) change, saving runner minutes.
  - **PR Details:** You can customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` step if you want.

## Running the Workflow

> [!WARNING]  
> **GitHub-hosted Runner Time Limit:**  
> GitHub-hosted runners like `ubuntu-latest` have a **maximum execution time limit of 6 hours**.  
> For large documentation repositories, if the translation process takes longer than 6 hours, the workflow will be stopped automatically.  
> To avoid this, consider:  
> - Using a **self-hosted runner** (no time limit)  
> - Reducing the number of target languages per run

Once the `co-op-translator.yml` file is merged into your main branch (or the branch specified in the `on:` trigger), the workflow will automatically run whenever changes are pushed to that branch (and match the `paths` filter, if you set one).

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.