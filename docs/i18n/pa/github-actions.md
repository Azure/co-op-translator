# GitHub Actions

ਜੇ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ ਕੋਈ ਰਿਪੋਜ਼ਟਰੀ ਬਦਲੇ ਹੋਏ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਅਨੁਵਾਦ ਕਰੇ ਅਤੇ ਬਣਾਏ ਗਏ ਨਤੀਜਿਆਂ ਨਾਲ ਇੱਕ ਪੁਲ ਰਿਕਵੇਸਟ ਖੋਲ੍ਹੇ ਤਾਂ GitHub Actions ਵਰਤੋ।

ਮਿਆਰੀ `GITHUB_TOKEN` ਸੈਟਅਪ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ, ਜਿਸ ਵਿੱਚ ਉਹ ਆਰਗਨਾਈਜ਼ੇਸ਼ਨ ਰਿਪੋਜ਼ਿਟਰੀਆਂ ਵੀ ਸ਼ਾਮਲ ਹਨ ਜਿੱਥੇ ਨੀਤੀ ਇਸਨੂੰ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। [GitHub ਐਪ ਸੈਟਅਪ](#github-app-setup) ਵੇਖੋ ਜਦੋਂ ਤੁਹਾਡੀ ਸੰਗਠਨ ਨੂੰ ਐਪ ਪਛਾਣ ਦੀ ਲੋੜ ਹੋਵੇ ਜਾਂ ਤੁਹਾਨੂੰ ਆਟੋਮੈਟਿਕ ਡਾਊਨਸਟ੍ਰੀਮ ਵਰਕਫਲੋ ਰਨਸ ਦੀ ਲੋੜ ਹੋਵੇ।

**ਮਾਨਵੀ ਸੋਧਾਂ:** ਇਹ ਵਰਕਫਲੋ ਬਦਲੇ ਹੋਏ ਸਰੋਤ ਫਾਈਲਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਦੁਬਾਰਾ ਅਨੁਵਾਦ ਕਰਦੇ ਹਨ ਅਤੇ ਉਹਨਾਂ ਦੀਆਂ ਅਨੁਵਾਦਿਤ ਫਾਇਲਾਂ ਵਿੱਚ ਸੋਧੀਆਂ ਗਈਆਂ ਲਫ਼ਜ਼ਬੰਦੀ ਨੂੰ ਓਵਰਰਾਈਟ ਕਰ ਸਕਦੇ ਹਨ। ਹਰ PR ਨੂੰ ਮਰਜ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸਮੀਖਿਆ ਕਰੋ। ਸਵੀਕਾਰ ਕੀਤੀਆਂ ਸੋਧਾਂ ਦੀ Markdown ਬਲਾਕ-ਲੈਵਲ ਸੰਰੱਖਣਤਾ ਲਈ ਇੱਕ ਕਸਟਮ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)।

## ਤੁਹਾਡਾ ਪਹਿਲਾ README ਅਨੁਵਾਦ PR

`README.md` ਦੇ ਇੱਕ ਮੂਲ ਫਾਇਲ ਅਤੇ ਇੱਕ ਨਿਸ਼ਾਨਾ ਭਾਸ਼ਾ ਦੇ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ। ਇਹ ਵਰਕਫਲੋ ਸਿਰਫ Markdown ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਇਸ ਲਈ Azure AI Vision ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ।

1. ਆਪਣੇ ਅਨੁਵਾਦ ਕਰਨ ਵਾਲੇ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([GitHub 'ਤੇ ਟੈਮਪਲੇਟ ਵੇਖੋ](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ਨੂੰ `.github/workflows/translate-readme.yml` 'ਤੇ ਕਾਪੀ ਕਰੋ, ਅਤੇ ਇਸਨੂੰ ਉਸ ਰਿਪੋਜ਼ਿਟਰੀ ਦੀ ਡਿਫੌਲਟ ਬ੍ਰਾਂਚ 'ਤੇ ਕਮਿਟ ਕਰੋ। ਟੈਮਪਲੇਟ `Azure/co-op-translator@main` ਵਿੱਚ ਮੂਲ Action ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ, ਜੋ ਉਹੀ CLI ਉਸੇ ਸੋਸ ਰੈਫ ਤੋਂ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ। ਦੁਹਰਾਏ ਜਾਣ ਯੋਗ ਰਨ ਲਈ ਇੱਕ ਸਮੀਖਿਆ ਕੀਤਾ ਹੋਇਆ ਕਮਿਟ ਪਿਨ ਕਰੋ।
2. Open **Actions > Translate README > Run workflow**, ਇੱਕ ਭਾਸ਼ਾ ਚੁਣੋ, ਅਤੇ **Preview only** ਨੂੰ ਚੈੱਕ ਕੀਤਾ ਰਹਿਣ ਦਿਓ। ਪ੍ਰੀਵਿਊ ਸਟੈਪ ਵਿੱਚ ਟੋਕਨ ਅਨੁਮਾਨ ਦੀ ਸਮੀਖਿਆ ਕਰੋ। ਪ੍ਰੀਵਿਊ ਮਾਡਲ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦਾ, ਅਨੁਵਾਦ ਨਹੀਂ ਲਿਖਦਾ, ਅਤੇ PR ਨਹੀਂ ਬਣਾਉਂਦਾ।
3. ਇੱਕ [ਟੈਕਸਟ ਪ੍ਰਦਾਤਾ](#prerequisites) ਲਈ ਸੀਕ੍ਰੇਟ ਜੋੜੋ, ਅਤੇ **ਸੈਟਿੰਗਜ਼ > ਐਕਸ਼ਨ > ਜਨਰਲ** ਹੇਠਾਂ **GitHub Actions ਨੂੰ ਪੁਲ ਰਿਕਵੇਸਟ ਬਣਾਉਣ ਅਤੇ ਮਨਜ਼ੂਰ ਕਰਨ ਦੀ ਆਗਿਆ** ਨੂੰ ਯੋਗ ਕਰੋ। ਟੈਮਪਲੇਟ ਆਪਣੇ ਜੌਬ ਲਈ `contents: write` ਅਤੇ `pull-requests: write` ਦੀ ਮੰਗ ਕਰਦਾ ਹੈ; ਤੁਹਾਨੂੰ ਹਰ ਵਰਕਫਲੋ ਲਈ ਡਿਫੌਲਟ ਅਨੁਮਤੀਆਂ ਬਦਲਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ। ਜੇ ਸੰਗਠਨ ਨੀਤੀ ਇਹ ਅਨੁਮਤੀਆਂ ਜਾਂ ਇਸ ਸੈਟਿੰਗ ਨੂੰ ਰੋਕਦੀ ਹੈ, ਤਾਂ ਪ੍ਰਸ਼ਾਸਕ ਤੋਂ ਮਨਜ਼ੂਰਸ਼ੁਦਾ [GitHub ਐਪ](#github-app-setup) ਬਾਰੇ ਪੁੱਛੋ।
4. **Preview only** ਨੂੰ ਅਨਚੈਕ ਕੀਤਾ ਹੋਇਆ ਰੱਖ ਕੇ ਵਰਕਫਲੋ ਨੂੰ ਮੁੜ ਚਲਾਓ। ਇਹ ਪ੍ਰੀਵਿਊ ਕਰਦਾ ਹੈ, ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, `co-op-review --readme-only` ਚਲਾਉਂਦਾ ਹੈ, ਅਤੇ ਸਿਰਫ਼ ਅਨੁਵਾਦ ਅਤੇ ਸਮੀਖਿਆ ਸਫਲ ਹੋਣ ਤੋਂ ਬਾਅਦ ਹੀ ਇਕ ਅਨੁਵਾਦ PR ਬਣਾਉਂਦਾ ਜਾਂ ਅਪਡੇਟ ਕਰਦਾ ਹੈ। ਵਰਕਫਲੋ ਸਾਰਾਂਸ਼ PR ਨਾਲ ਲਿੰਕ ਕਰਦਾ ਹੈ।
5. PR ਵਿੱਚ ਵਰਤਿਆ ਗਿਆ ਭਾਸ਼ਾ ਅਤੇ ਫਾਇਲਾਂ ਵਿੱਚ ਕੀਤੇ ਗਏ ਬਦਲਾਵਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ, ਫਿਰ ਤਿਆਰ ਹੋਣ 'ਤੇ ਮਰਜ ਕਰੋ। ਵਰਕਫਲੋ ਆਪਣੇ ਆਪ ਮਰਜ ਨਹੀਂ ਕਰਦਾ।

PR ਵਿੱਚ ਸਿਰਫ਼ `translations/<language>/README.md` ਅਤੇ ਇਸ ਦੀ ਭਾਸ਼ਾ ਮੈਟਾਡੇਟਾ ਫਾਇਲ ਹੁੰਦੀ ਹੈ। ਸੋਰਸ README ਬਦਲਦਾ ਨਹੀਂ ਹੈ, ਅਤੇ ਹੋਰ ਦਸਤਾਵੇਜ਼ਾਂ ਵੱਲ ਦੇ ਲਿੰਕ ਉਸੇ ਸੋਰਸ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਹੀ ਸੰਕੇਤ ਕਰਦੇ ਰਹਿੰਦੇ ਹਨ। PR ਦੇ ਬਾਡੀ ਵਿੱਚ ਬਦਲੇ ਗਏ ਫਾਇਲਾਂ ਅਤੇ ਸੰਰਚਨਾਤਮਕ ਸਮੀਖਿਆ ਨਤੀਜੇ ਲਿਖੇ ਹੁੰਦੇ ਹਨ। ਜੇ ਅਨੁਵਾਦ ਜਾਂ ਸਮੀਖਿਆ ਫੇਲ ਹੋ ਜਾਵੇ, ਤਾਂ ਵਰਕਫਲੋ ਸਾਰਾਂਸ਼ ਅਤੇ ਅਸਫਲ ਕਦਮਾਂ ਦੇ ਲੌਗਾਂ ਦੀ ਜਾਂਚ ਕਰੋ; ਕੋਈ PR ਬਣਾਈ ਨਹੀਂ ਜਾਂਦੀ। ਜੇ ਕੋਈ ਤਬਦੀਲੀ ਨਹੀਂ ਹੈ, ਤਾਂ ਕੋਈ ਨਵਾਂ PR ਲੋੜੀਂਦਾ ਨਹੀਂ।

**ਸੰਸਥਾ ਅਤੇ CI ਨੋਟ:** GitHub ਐਪ ਵਿਕਲਪਿਕ ਹੈ, ਸੰਸਥਾ ਦੀ ਮਲਕੀਅਤ ਲਈ ਲਾਜ਼ਮੀ ਨਹੀਂ। `GITHUB_TOKEN` ਨਾਲ, PR ਖੋਲ੍ਹਣ, ਅਪਡੇਟ ਕਰਨ ਜਾਂ ਮੁੜ-ਖੋਲ੍ਹਣ ਵਾਲੇ ਪੁਲ-ਰਿਕਵੇਸਟ ਵਰਕਫਲੋਜ਼ ਲਈ ਲਿਖਣ ਦੀ ਪਹੁੰਚ ਵਾਲੇ ਯੂਜ਼ਰ ਨੂੰ **Approve workflows to run** ਚੁਣਨਾ ਲਾਜ਼ਮੀ ਹੁੰਦਾ ਹੈ। Push ਵਰਕਫਲੋਜ਼ ਇਸ ਟੋਕਨ ਨਾਲ ਟ੍ਰਿਗਰ ਨਹੀਂ ਹੁੰਦੇ। ਬਿਨਾਂ ਨਿਗਰਾਨੀ ਡਾਊਨਸਟ੍ਰੀਮ CI ਲਈ, [GitHub App Setup](#github-app-setup) ਅਤੇ GitHub ਦੇ [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) ਵੇਖੋ।

## Prerequisites

ਵਰਕਫਲੋ ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਉਹ AI ਸੇਵਾ secrets ਸੰਰਚਿਤ ਕਰੋ ਜੋ ਤੁਹਾਡੇ ਅਨੁਵਾਦ ਰਨ ਨੂੰ ਲੋੜੀਂਦੇ ਹਨ।

ਟੈਕਸਟ ਅਨੁਵਾਦ ਲਈ ਇੱਕ ਭਾਸ਼ਾ ਮਾਡਲ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਵਾਧੂ ਤੌਰ 'ਤੇ Azure AI Vision ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

See [Configuration](configuration.md) and [Azure AI Setup](azure-ai-setup.md) for local configuration details.

## ਮਿਆਰੀ ਸੈਟਅਪ

README ਵਰਕਫਲੋ آزਮائڻ ਤੋਂ ਬਾਅਦ, ਇਸ ਸੈਟਅਪ ਨੂੰ ਵਰਤੋ ਤਾਂ ਜੋ ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਦੀਆਂ Markdown ਫਾਇਲਾਂ ਨੂੰ ਕਈ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹ PR ਖੋਲ੍ਹਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ Markdown ਸਮੀਖਿਆ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ Azure AI Vision ਦੀ ਲੋੜ ਨਹੀਂ ਹੋਂਦੀ।

### ਕਦਮ 1: ਰਿਪੋਜ਼ਿਟਰੀ ਸੀਕ੍ਰਿਟ ਜੋੜੋ

ਆਪਣੇ ਲਕਸ਼ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ, **Settings** > **Secrets and variables** > **Actions** ਖੋਲ੍ਹੋ, ਫਿਰ ਉਹ ਪ੍ਰੋਵਾਈਡਰ ਸੀਕ੍ਰੇਟ ਜੋੜੋ ਜੋ ਤੁਹਾਡੇ ਵਰਕਫਲੋ ਵਰਤੇਗਾ।

![Actions ਸਿਕਰੇਟਸ ਚੁਣੋ](../../assets/github-actions/select-setting-action.png)

### ਕਦਮ 2: ਵਰਕਫਲੋ ਦੀਆਂ ਅਨੁਮਤੀਆਂ ਚਾਲੂ ਕਰੋ

Open **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. **GitHub Actions ਨੂੰ ਪੁਲ ਰਿਕਵੇਸਟ ਬਣਾਉਣ ਅਤੇ ਮਨਜ਼ੂਰ ਕਰਨ ਦੀ ਆਗਿਆ** ਨੂੰ ਚਾਲੂ ਕਰੋ।
2. ਸੈਟਿੰਗ ਸੇਵ ਕਰੋ।

ਥੱਲੇ ਦਿੱਤਾ ਜੌਬ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ `contents: write` ਅਤੇ `pull-requests: write` ਦੀ ਮੰਗ ਕਰਦਾ ਹੈ। ਰਿਪੋਜ਼ਿਟਰੀ ਦੀ ਡਿਫੌਲਟ ਵਰਕਫਲੋ ਅਨੁਮਤੀਆਂ ਬਦਲੀਆਂ ਨਾ ਕਰੋ। ਜੇ ਸੰਗਠਨ ਨੀਤੀ PR ਬਣਾਉਣ ਨੂੰ ਰੋਕਦੀ ਹੈ, ਤਾਂ ਪ੍ਰਸ਼ਾਸਕ ਤੋਂ ਮਨਜ਼ੂਰ ਕੀਤੀ ਹੋਈ [GitHub ਐਪ](#github-app-setup) ਬਾਰੇ ਪੁੱਛੋ।

### ਕਦਮ 3: ਵਰਕਫਲੋ ਸ਼ਾਮਿਲ ਕਰੋ

Create `.github/workflows/co-op-translator.yml`:

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

ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਲੋੜੀਂਦੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ `TARGET_LANGUAGES` ਨੂੰ ਬਦਲੋ। ਸਮੀਖਿਆ ਸਿਰਫ Markdown ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ Python API ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ, ਜੋ ਅਨੁਵਾਦ ਕਦਮ ਨਾਲ ਮਿਲਦੀ ਹੈ। ਕਿਸੇ ਵੀ ਅਨੁਵਾਦ ਜਾਂ ਸਮੀਖਿਆ ਦੀ ਗਲਤੀ PR ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਹੀ ਜੌਬ ਨੂੰ ਰੋਕ ਦੇਵੇਗੀ। ਵਰਕਫਲੋ PR ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਮੇਰਜ ਨਹੀਂ ਕਰਦਾ। ਵੱਡੇ ਰਿਪੋਜ਼ਿਟਰੀਆਂ ਲਈ, `on.push` ਦੇ ਹੇਠਾਂ ਇੱਕ `paths:` ਫਿਲਟਰ ਜੋੜੋ ਤਾਂ ਕਿ ਵਰਕਫਲੋ ਸਿਰਫ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਤਬਦੀਲੀ ਹੋਣ 'ਤੇ ਹੀ ਚਲੇ।

### ਵਿਕਲਪਿਕ: notebooks and images

ਨੋਟਬੁੱਕਾਂ ਲਈ, ਅਨੁਵਾਦ ਕਮਾਂਡ ਵਿੱਚ `-nb` ਜੋੜੋ ਅਤੇ ਸਮੀਖਿਆ ਕਦਮ ਵਿੱਚ `notebook=True` ਸੈੱਟ ਕਰੋ। ਚਿੱਤਰਾਂ ਦੇ ਟੈਕਸਟ ਲਈ, ਦੋਹਾਂ [Azure AI Vision secrets](#prerequisites) ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ, ਉਨ੍ਹਾਂ ਨੂੰ ਅਨੁਵਾਦ ਕਦਮ ਦੇ `env` ਵਿੱਚ ਪਾਸ ਕਰੋ, ਕਮਾਂਡ ਵਿੱਚ `-img` ਜੋੜੋ, ਅਤੇ PR ਕਦਮ ਦੇ `add-paths` ਵਿੱਚ `translated_images/` ਜੋੜੋ। ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਚਿੱਤਰਾਂ ਦੀ ਵਿਜ਼ੂਅਲ ਰੂਪ ਵਿੱਚ ਸਮੀਖਿਆ ਕਰੋ; ਨਿਰਧਾਰਿਤ ਸਮੀਖਿਆ ਚਿੱਤਰ ਟੈਕਸਟ ਜਾਂ ਭਾਸ਼ਾਈ ਦਰੁਸਤਤਾ ਦੀ ਪ੍ਰਮਾਣਿਕਤਾ ਨਹੀਂ ਦਿੰਦੀਆਂ।

## GitHub ਐਪ ਸੈਟਅਪ

ਜਦੋਂ ਤੁਹਾਡੀ ਸੰਗਠਨ ਨੂੰ ਐਪ ਪਛਾਣ ਦੀ ਲੋੜ ਹੋਵੇ ਜਾਂ ਜਦੋਂ ਬਣਾਇਆ ਗਿਆ PR `GITHUB_TOKEN` ਮਨਜ਼ੂਰੀ ਕਦਮ ਦੇ ਬਿਨਾਂ ਹੇਠਲੇ CI ਨੂੰ ਟਰigger ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ ਮਨਜ਼ੂਰਸ਼ੁਦਾ GitHub ਐਪ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇੱਕ ਐਪ ਸੰਗਠਨ ਨੀਤੀ ਨੂੰ ਬਾਈਪਾਸ ਨਹੀਂ ਕਰਦਾ; ਪ੍ਰਸ਼ਾਸਕ ਫਿਰ ਵੀ ਇਸ ਦੀ ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਅਨੁਮਤੀਆਂ ਨੂੰ ਕੰਟਰੋਲ ਕਰਦੇ ਹਨ।

### ਕਦਮ 1: ਇੱਕ GitHub App ਬਣਾਓ ਜਾਂ ਇੰਸਟਾਲ ਕਰੋ

ਉਪਲਬਧ ਹੋਣ 'ਤੇ ਮੌਜੂਦਾ ਸੰਸਥਾ-ਪ੍ਰਦਾਤ App ਦੀ ਵਰਤੋਂ ਕਰੋ, ਜਾਂ **Contents** ਅਤੇ **Pull requests** ਲਈ ਪੜ੍ਹਨ/ਲਿਖਣ ਦੀ ਪਹੁੰਚ ਦੇ ਨਾਲ ਇੱਕ ਨਵਾਂ ਬਣਾਓ। ਕਿਸੇ ਵੀ ਲੋੜੀਂਦੀ ਸੰਸਥਾ ਮਨਜ਼ੂਰੀ ਨਾਲ ਇਸਨੂੰ ਲਕ਼ਸ਼ ਰਿਪੋਜ਼ਿਟਰੀ 'ਤੇ ਇੰਸਟਾਲ ਕਰੋ।

Record:

- App ID
- Private key contents

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### ਕਦਮ 2: ਇੱਕ App ਟੋਕਨ ਜਨਰੇਟ ਕਰੋ

ਇਸ ਕਦਮ ਨੂੰ ਮੌਜੂਦਾ ਪੁਲ ਰਿਕਵੇਸਟ ਸਟੈਪ ਤੋਂ ਠੀਕ ਪਹਿਲਾਂ ਸ਼ਾਮِل ਕਰੋ। README ਟੈਮਪਲੇਟ ਲਈ, ਉਹੀ ਸਫਲਤਾ ਦੀ ਸ਼ਰਤ ਵਰਤੋ ਤਾਂ ਜੋ ਪ੍ਰੀਵਿਊ ਅਤੇ ਨਾਕਾਮ ਹੋਏ ਅਨੁਵਾਦ App ਟੋਕਨ ਦੀ ਬੇਨਤੀ ਨਾ ਕਰਨ।

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

ਫਿਰ ਮੌਜੂਦਾ ਪੁਲ ਰਿਕਵੇਸਟ ਸਟੈਪ ਦੇ ਕੇਵਲ `token` ਇਨਪੁੱਟ ਨੂੰ `${{ steps.generate_token.outputs.token }}` ਵਿੱਚ ਬਦਲੋ। ਇਸ ਦੀ ਸਫਲਤਾ ਦੀ ਸ਼ਰਤ, ਬਰਾਂਚ, PR ਬਾਡੀ ਅਤੇ `add-paths` ਨੂੰ ਅਨਬਦਲ ਰੱਖੋ। ਟੋਕਨ ਮੂਲ ਤੌਰ 'ਤੇ ਮੌਜੂਦਾ ਰਿਪੋਜ਼ਿਟਰੀ ਤੱਕ ਸੀਮਿਤ ਹੁੰਦਾ ਹੈ। README ਟੈਮਪਲੇਟ ਦੇ ਬਦਲੇ ਸਟੈਂਡਰਡ ਸੈਟਅੱਪ ਨੂੰ ਅਨੁਕੂਲ ਕਰਨ ਸਮੇਂ, ਉਪਰੋਕਤ `if` ਨੂੰ ਛੱਡ ਦਿਓ: ਉਹ ਵਰਕਫਲੋ ਡਿਫੌਲਟ ਸਫਲਤਾ ਦੀ ਸ਼ਰਤ ਵਰਤਦਾ ਹੈ, ਇਸ ਲਈ ਟੋਕਨ ਬਣਾਉਣ ਅਤੇ PR ਬਣਾਉਣ ਸਿਰਫ਼ ਅਨੁਵਾਦ ਅਤੇ ਸਮੀਖਿਆ ਸਫਲ ਹੋਣ ਤੋਂ ਬਾਅਦ ਹੀ ਚਲਦੇ ਹਨ।

See the official [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) for installation and token permissions.

## ਰਨਰ ਸੀਮਾਵਾਂ

GitHub-hosted runners ਦੀਆਂ ਜ਼ਿਆਦਾ ਤੋਂ ਜ਼ਿਆਦਾ ਜੌਬ ਮਿਆਦਾਂ ਹੁੰਦੀਆਂ ਹਨ। ਵੱਡੇ ਰਿਪੋਜ਼ਿਟਰੀ ਜਾਂ ਕਈ ਲਕੜੇ ਟਾਰਗਟ ਭਾਸ਼ਾਵਾਂ ਇਸ ਹੱਦ ਨੂੰ ਪਾਰ ਕਰ ਸਕਦੀਆਂ ਹਨ।

For large translation workloads:

- Translate fewer languages per run.
- Use content flags such as `-md`, `-nb`, or `-img`.
- ਜਦੋਂ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਆਕਾਰ ਜਾਂ ਮਾਡਲ ਦੀ ਲੇਟੈਂਸੀ ਹੋਸਟਡ ਰਨਰਾਂ ਨੂੰ ਗੈਰ-ਭਰੋਸੇਯੋਗ ਬਣਾਉਂਦੀ ਹੋਵੇ, ਤਾਂ ਸਵੈ-ਹੋਸਟਡ ਰਨਰ ਦੀ ਵਰਤੋਂ ਕਰੋ।

## CI ਵਿੱਚ ਸਮੀਖਿਆ

ਜਦੋਂ ਇੱਕ ਪુલ ਰਿਕਵੈਸਟ ਨੂੰ ਜਨਰੇਟ ਕੀਤੀਆਂ ਅਨੁਵਾਦਾਂ ਨੂੰ LLM ਜਾਂ Vision ਪ੍ਰੋਵਾਇਡਰਾਂ ਨੂੰ ਕਾਲ ਕੀਤੇ ਬਿਨਾਂ ਵੈਰੀਫਾਈ ਕਰਨਾ ਹੋਵੇ ਤਾਂ `co-op-review` ਦੀ ਵਰਤੋਂ ਕਰੋ।

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ਇੱਕ ਬੀਟਾ ਨਿਰਧਾਰਤ ਸਮੀਖਿਆ ਕਮਾਂਡ ਹੈ। ਇਸ ਦੀਆਂ ਜਾਂਚਾਂ ਅਤੇ ਆਉਟਪੁਟ ਸਕੀਮਾ ਵਿਕਸਤ ਹੋ ਸਕਦੇ ਹਨ, ਪਰ ਇਹ CI ਲਈ ਸੁਰੱਖਿਅਤ ਬਣਾਈ ਗਈ ਹੈ ਕਿਉਂਕਿ ਇਹ ਫਾਇਲਾਂ ਨਹੀਂ ਲਿਖਦੀ ਅਤੇ ਨਾਹ ਹੀ ਮਾਡਲ ਪ੍ਰੋਵਾਇਡਰਾਂ ਨੂੰ ਕਾਲ ਕਰਦੀ ਹੈ।
