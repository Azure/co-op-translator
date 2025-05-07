<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:09:37+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "en"
}
-->
# Using the Co-op Translator GitHub Action (Public Setup)

**Target Audience:** This guide is designed for users of most public or private repositories where standard GitHub Actions permissions suffice. It uses the built-in `GITHUB_TOKEN`.

Easily automate the translation of your repository’s documentation with the Co-op Translator GitHub Action. This guide explains how to set up the action to automatically open pull requests with updated translations whenever your source Markdown files or images change.

> [!IMPORTANT]
>
> **Choosing the Right Guide:**
>
> This guide covers the **simpler setup using the standard `GITHUB_TOKEN`**. This is the recommended approach for most users since it doesn’t require managing sensitive GitHub App Private Keys.
>

## Prerequisites

Before setting up the GitHub Action, make sure you have the necessary AI service credentials ready.

**1. Required: AI Language Model Credentials**  
You need credentials for at least one supported Language Model:

- **Azure OpenAI**: Requires Endpoint, API Key, Model/Deployment Names, API Version.  
- **OpenAI**: Requires API Key, (Optional: Org ID, Base URL, Model ID).  
- See [Supported Models and Services](../../../../README.md) for details.  
- Setup Guide: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Optional: Computer Vision Credentials (for Image Translation)**

- Only needed if you want to translate text inside images.  
- **Azure Computer Vision**: Requires Endpoint and Subscription Key.  
- If not provided, the action will run in [Markdown-only mode](../markdown-only-mode.md).  
- Setup Guide: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Setup and Configuration

Follow these steps to configure the Co-op Translator GitHub Action in your repository using the standard `GITHUB_TOKEN`.

### Step 1: Understand Authentication (Using `GITHUB_TOKEN`)

This workflow uses the built-in `GITHUB_TOKEN` provided by GitHub Actions. This token automatically grants the workflow permissions to interact with your repository according to the settings you configure in **Step 3**.

### Step 2: Configure Repository Secrets

You only need to add your **AI service credentials** as encrypted secrets in your repository settings.

1.  Go to your target GitHub repository.  
2.  Navigate to **Settings** > **Secrets and variables** > **Actions**.  
3.  Under **Repository secrets**, click **New repository secret** for each required AI service secret listed below.

    ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(Image Reference: Shows where to add secrets)*

**Required AI Service Secrets (Add ALL that apply based on your Prerequisites):**

| Secret Name                         | Description                               | Value Source                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Key for Azure AI Service (Computer Vision)  | Your Azure AI Foundry               |
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

The GitHub Action requires permissions granted via the `GITHUB_TOKEN` to check out code and create pull requests.

1.  In your repository, go to **Settings** > **Actions** > **General**.  
2.  Scroll to the **Workflow permissions** section.  
3.  Select **Read and write permissions**. This grants the `GITHUB_TOKEN` the necessary `contents: write` and `pull-requests: write` permissions for this workflow.  
4.  Make sure the checkbox for **Allow GitHub Actions to create and approve pull requests** is **checked**.  
5.  Click **Save**.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### Step 4: Create the Workflow File

Finally, create the YAML file that defines the automated workflow using `GITHUB_TOKEN`.

1.  In your repository’s root directory, create the `.github/workflows/` folder if it doesn’t already exist.  
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
4.  **Customize the Workflow:**  
  - **[!IMPORTANT] Target Languages:** In the `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` step, update the target languages as needed.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.