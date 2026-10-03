# GitHub Actions

ಬದಲಾದ ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನುವಾದಿಸಿ ತಯಾರಿಸಿದ ಔಟ್‌ಪುಟ್‌ಗಳೊಂದಿಗೆ ಒಂದು pull request ತೆರೆಯಲು ನೀವು ರೆಪೊ ಬಳಸಬೇಕಾದಾಗ GitHub Actions ಅನ್ನು ಬಳಸಿ.

ಸಾಮಾನ್ಯ `GITHUB_TOKEN` ಸೆಟ್‌ಅಪ್‌ನಿಂದ ಪ್ರಾರಂಭಿಸಿ, ಸಂಸ್ಥೆಯ ರೆಪೊಗಳು ಪಾಲಿಸಿಯು ಇದನ್ನು ಅನುಮತಿಸಿದಲ್ಲಿ ಸಹ. ನಿಮ್ಮ ಸಂಘಟನೆಗೆ App ಗುರುತು ಬೇಕಿದ್ದಾಗ ಅಥವಾ ಸ್ವಯಂಚಾಲಿತ ಡೌನ್‌ಸ್ಟ್ರೀಂ ವರ್ಕ್‌ಫ್ಲೋ ಚಾಲನೆಗಳು ಅಗತ್ಯವಾಗುವಾಗ [GitHub App Setup](#github-app-setup) ನೋಡಿ.

**ಮಾನವ ಸಂಪಾದನೆಗಳು:** ಈ ವರ್ಕ್ಫ್ಲೋಗಳು ಬದಲಾಗಿಸಿದ ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಮರುಅನುವಾದಿಸುತ್ತವೆ ಮತ್ತು ಅವರ ಅನುವಾದಗಳಲ್ಲಿ ಮಾಡಿದ ವರ್ಡಿಂಗ್ ಅನ್ನು ಓವರ್ರೈಟ್ ಮಾಡಬಹುದು. ಮರ್ಜ್ ಮಾಡುವ ಮೊದಲು ಪ್ರತಿ PR ಅನ್ನು ಪರಿಶೀಲಿಸಿ. ಸ್ವೀಕೃತ ಸಂಪಾದನೆಗಳ Markdown ಬ್ಲಾಕ್-ಮಟ್ಟದ ಸಂರಕ್ಷಣೆಗಾಗಿ [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ಜೊತೆಗೆ ಕಸ್ಟಮ್ ಇಂಟಿಗ್ರೇಶನ್ ಬೇಕಾಗುತ್ತದೆ.

## ನಿಮ್ಮ ಮೊದಲ README ಅನುವಾದ PR

ಒಂದು ರೂಟ್ `README.md` ಮತ್ತು ಒಂದು ಗುರಿ ಭಾಷೆಯಿಂದ ಪ್ರಾರಂಭಿಸಿ. ಈ ವರ್ಕ್ಫ್ಲೋ Markdown ಮಾತ್ರ ಅನುವಾದಿಸುತ್ತದೆ, ಆದ್ದರಿಂದ Azure AI Vision ಅಗತ್ಯವಿಲ್ಲ.

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ಅನ್ನು ನೀವು ಅನುವಾದಿಸಲು ಬಯಸುವ ರೆಪೊನ `.github/workflows/translate-readme.yml` ಗೆ ನಕಲಿಸಿ ಮತ್ತು ಅದನ್ನು ಆ ರೆಪೊನ ಡೀಫಾಲ್ಟ್ ಬ್ರಾಂಚ್‌ಗೆ ಕಮಿಟ್ ಮಾಡಿ. ಟೆಂಪ್ಲೆಟ್ ಮೂಲ Action ಅನ್ನು `Azure/co-op-translator@main` ನಲ್ಲಿ ಬಳಸುತ್ತದೆ, ಇದು CLI ಅನ್ನು ಅದೇ ಸ್ರೋತ ರೆಫರ್‌ನಿಂದ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುತ್ತದೆ. ಪುನರಾವೃತ್ತಿಯ ಚಲನೆಗಳಿಗೆ ಪರಿಶೀಲಿಸಿದ ಕಮಿಟ್ ಅನ್ನು ಪಿನ್ ಮಾಡಿ.
2. **Actions > Translate README > Run workflow** ತೆರೆಯಿರಿ, ಒಂದು ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ, ಮತ್ತು **Preview only** ಅನ್ನು ಟಿಕ್ ಮಾಡಿರುವಂತೆ ಇಡಿರಿ. ಪ್ರಿವ್ಯೂ ಹಂತದಲ್ಲಿ ಟೋಕನ್ ಅಂದಾಜನ್ನು ಪರಿಶೀಲಿಸಿ. ಪ್ರಿವ್ಯೂ ಮಾದರಿ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆಯುವುದಿಲ್ಲ, ಅನುವಾದಗಳನ್ನು ಬರೆಯುವುದಿಲ್ಲ, ಅಥವಾ PR ರಚಿಸುವುದಿಲ್ಲ.
3. ಒಂದು [ಟೆಕ್ಸ್ಟ್ ಪ್ರೊವೈಡರ್](#prerequisites)ಗಾಗಿ ರಹಸ್ಯಗಳನ್ನು ಸೇರಿಸಿ, ಮತ್ತು **ಸೆಟ್ಟಿಂಗ್ಸ್ > ಆಕ್ಷನ್ಸ್ > ಸಾಮಾನ್ಯ** ಅಡಿಯಲ್ಲಿ **GitHub Actions ಮೂಲಕ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ರಚನೆ ಮತ್ತು ಅನುಮೋದನೆ** ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ. ಟೆಂಪ್ಲೆಟ್ ತನ್ನ ജോಬ್‌ಗಾಗಿ `contents: write` ಮತ್ತು `pull-requests: write` ಅನ್ನು ವಿನಂತಿಸುತ್ತದೆ; ಪ್ರತಿಯೊಂದು ವರ್ಕ್ಫ್ಲೋವಿನಡಕೂ ನೀವು ಡೀಫಾಲ್ಟ್ ಪರವಾನಗಿಗಳನ್ನು ಬದಲಿಸಬೇಕಾಗಿಲ್ಲ. ಸಂಸ್ಥೆಯ ಪಾಲಿಸಿ ಈ ಪರವಾನಗಿಗಳು ಅಥವಾ ಸೆಟ್ಟಿಂಗ್ ಅನ್ನು ತಡೆಯುವಿದ್ದರೆ, ಅನುಮೋದಿತ [GitHub App](#github-app-setup) ಕುರಿತು ನಿರ್ವಾಹಕರನ್ನು ಕೇಳಿ.
4. **Preview only** ಅನ್ನು ಅನಚೆಕ್ ಮಾಡಿ ಮತ್ತು ವರ್ಕ್ಫ್ಲೋವನ್ನು ಮళ్లಿಸಿ. ಅದು ಪ್ರಿವ್ಯೂ ಮಾಡುತ್ತದೆ, ಅನುವಾದಿಸುತ್ತದೆ, `co-op-review --readme-only` 를 ರನ್ ಮಾಡುತ್ತದೆ, ಮತ್ತು ಅನುವಾದ ಮತ್ತು ಪರಿಶೀಲನೆ ಯಶಸ್ವಿಯಾಗಿದೆಯೇನೆಂದು ದೃಢವಾದ ನಂತರ ಮಾತ್ರ ಅನುವಾದ PR ಅನ್ನು ರಚಿಸುತ್ತದೆ ಅಥವಾ ಅಪ್‌ಡೇಟ್ ಮಾಡುತ್ತದೆ. ವರ್ಕ್‌ಫ್ಲೋ ಸಾರಾಂಶವು PR ಗೆ ಲಿಂಕ್ ಅನ್ನು ನೀಡುತ್ತದೆ.
5. PR ನಲ್ಲಿ ಪದಬಳಕೆ ಮತ್ತು ಫೈಲ್ ಬದಲಾವಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ, ಸಿದ್ಧವಾದಾಗ ಮರ್ಜ್ ಮಾಡಿ. ವರ್ಕ್ಫ್ಲೋ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮರ್ಜ್ ಮಾಡುವುದಿಲ್ಲ.

PRನಲ್ಲಿ ಕೇವಲ `translations/<language>/README.md` ಮತ್ತು ಅದರ ಭಾಷಾ ಮೆಟಾಡೇಟಾ ಫೈಲ್ ಮಾತ್ರವೂ ಸೇರಿರುತ್ತವೆ. ಮೂಲ README ಬದಲಾಗುವುದಿಲ್ಲ, ಮತ್ತು ಇತರ ದಾಖಲೆಗಳಿಗೆ ಇರುವ ಲಿಂಕ್‌ಗಳು ಮೂಲ ದಾಖಲೆಗಳನ್ನೇ ಸೂಚಿಸುತ್ತವೆ. PR ಬಾಡಿಯಲ್ಲಿ ಬದಲಾಗಿದೆ ಫೈಲ್‌ಗಳು ಮತ್ತು ರಚನಾತ್ಮಕ ಪರಿಶೀಲನೆ ಫಲಿತಾಂಶಗಳ ಪಟ್ಟಿ ಇರುತ್ತದೆ. ಅನುವಾದ ಅಥವಾ ಪರಿಶೀಲನೆ ವಿಫಲವಾದರೆ, ವರ್ಕ್ಫ್ಲೋ ಸಾರಾಂಶ ಮತ್ತು ವಿಫಲವಾದ ಸ್ಟೆಪ್ ಲಾಗ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ; ಯಾವುದೇ PR ರಚನೆ ಆಗುವುದಿಲ್ಲ. ಬದಲಾವಣೆಗಳಿಲ್ಲದಿದ್ದರೆ ಹೊಸ PR ಅಗತ್ಯವಿಲ್ಲ.

**Organization and CI note:** GitHub App ಐಚ್ಛಿಕವಾಗಿದೆ, ಸಂಸ್ಥೆಯ ಮಾಲೀಕತ್ವದ ಆವಶ್ಯಕತೆ ಅಲ್ಲ. `GITHUB_TOKEN` ಬಳಕೆದಾರರಿಂದ PR ತೆರೆಯುವುದು, ಅಪ್‌ಡೇಟ್ ಮಾಡುವದು ಅಥವಾ ಮರುತೆರೆದಂತೆ ಮಾಡುವದು ಎಂಬ ವರ್ಕ್ಫ್ಲೋಗಳು ಒಬ್ಬ ಬರೆಯ权限 ಇರುವ ಬಳಕೆದಾರನು **Approve workflows to run** ಅನ್ನು ಆಯ್ಕೆಮಾಡಬೇಕಾಗುತ್ತದೆ. Push ವರ್ಕ್ಫ್ಲೋಗಳು ಈ ಟೋಕನ್ ಮೂಲಕ ಪ್ರೇರೇಪಿತವಾಗುವುದಿಲ್ಲ. ನಿರೀಕ್ಷಿಸಲು ಇಲ್ಲದ ಡೌನ್‌ಸ್ಟ್ರೀಂ CI ಗಾಗಿ, [GitHub App Setup](#github-app-setup) ಮತ್ತು GitHub ನ [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) ನೋಡಿ.

## Prerequisites

ವರ್ಕ್ಫ್ಲೋ ಸೃಷ್ಟಿಸುವ ಮೊದಲು, ನಿಮ್ಮ ಅನುವಾದ ಚಾಲನೆಗೆ ಅಗತ್ಯವಾದ AI ಸೇವೆಯ ರಹಸ್ಯಗಳನ್ನು ಸಂರಚಿಸಿ.

ಟೆಕ್ಸ್ಟ್ ಅನುವಾದಕ್ಕೆ ಒಂದು ಭಾಷಾ ಮಾದರಿ ಪ್ರೊವೈಡರ್ ಅಗತ್ಯವಿರುತ್ತದೆ:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, ಮತ್ತು ಐಚ್ಛಿಕವಾಗಿ `OPENAI_ORG_ID` ಮತ್ತು `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, ಮತ್ತು ಐಚ್ಛಿಕವಾಗಿ `ANTHROPIC_BASE_URL`

ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ ಹೆಚ್ಚುವರಿವಾಗಿ Azure AI Vision ಬೇಕಾಗುತ್ತದೆ:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

ಸ್ಥಳೀಯ ಕಾನ್ಫಿಗರೇಶನ್ ವಿವರಗಳಿಗಾಗಿ [Configuration](configuration.md) ಮತ್ತು [Azure AI Setup](azure-ai-setup.md) ಅನ್ನು ನೋಡಿ.

## ಪ್ರಮಾಣಿತ ಸಂರಚನೆ

README ವರ್ಕ್ಫ್ಲೋ ಪ್ರಯೋಗಿಸಿದ ನಂತರ, ಈ ಸೆಟಪ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು ರೆಪೊನ Markdown ಫೈಲ್‌ಗಳನ್ನು ವಿವಿಧ ಭಾಷೆಗಳಿಗೆ ಅನುವಾದಿಸಿ. ಇದು PR ತೆರೆಯುವ ಮೊದಲು Markdown ಪರಿಶೀಲನೆಯನ್ನು ನಡೆಸುತ್ತದೆ ಮತ್ತು Azure AI Vision ಅಗತ್ಯವಿಲ್ಲ.

### ಹಂತ 1: ರೆಪೊಸಿಟರಿ ರಹಸ್ಯಗಳನ್ನು ಸೇರಿಸಿ

ನಿಮ್ಮ ಗುರಿ ರೆಪೊನಲ್ಲಿ **Settings** > **Secrets and variables** > **Actions** ತೆರೆಯಿರಿ, ನಂತರ ನಿಮ್ಮ ವರ್ಕ್ಫ್ಲೋ ಬಳಸುವ ಪ್ರೊವೈಡರ್ ರಹಸ್ಯಗಳನ್ನು ಸೇರಿಸಿ.

![ಕಾರ್ಯಗಳ ರಹಸ್ಯಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ](../../assets/github-actions/select-setting-action.png)

### ಹಂತ 2: ವರ್ಕ್‌ಫ್ಲೋ ಅನುಮತಿಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ

**Settings** > **Actions** > **General** ತೆರೆಯಿರಿ.

**Workflow permissions** ಅಡಿಯಲ್ಲಿ:

1. **GitHub Actions ಮೂಲಕ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ರಚನೆ ಮತ್ತು ಅನುಮೋದನೆ** ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ.
2. ಸೆಟ್ಟಿಂಗ್ ಅನ್ನು ಉಳಿಸಿ.

ಕೆಳಗಿನ ಕೆಲಸವು ಸ್ಪಷ್ಟವಾಗಿ `contents: write` ಮತ್ತು `pull-requests: write` ಅನ್ನು ವಿನಂತಿಸುತ್ತದೆ. ರೆಪೊನ ಡೀಫಾಲ್ಟ್ ವರ್ಕ್ಫ್ಲೋ ಪರವಾನಗಿಗಳನ್ನು ಅಗೋಚರವಾಗಿ ಇರಿಸಿ. ಸಂಸ್ಥೆಯ ಪಾಲಿಸಿ PR ರಚನೆ ತಡೆಯುವದಾದರೆ, ಅನುಮೋದಿತ [GitHub App](#github-app-setup) ಕುರಿತು ನಿರ್ವಾಹಕರನ್ನು ಕೇಳಿ.

### ಹಂತ 3: ಕಾರ್ಯಪ್ರವಾಹ ಸೇರಿಸಿ

`.github/workflows/co-op-translator.yml` ಸೃಷ್ಟಿಸಿ:

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

`TARGET_LANGUAGES` ಅನ್ನು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ಬೇಕಾದ ಭಾಷೆಗಳಿಗೆ ಬದಲಿಸಿ. ರಿವ್ಯೂ ವಾಕ್‌ಫ್ಲೋ ಮಾತ್ರ Markdown ಅನ್ನು ಪರಿಶೀಲಿಸಲು Python API ಬಳಕೆಗೊಳಿಸುತ್ತದೆ, ಇದು ಅನುವಾದ ಹಂತದೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ. ಅನುವಾದ ಅಥವಾ ಪರಿಶೀಲನೆ ದೋಷವು PR ರಚನೆಯ ಮೊದಲು ಕೆಲಸವನ್ನು ನಿಲ್ಲಿಸುತ್ತದೆ. ವರ್ಕ್ಫ್ಲೋ PR ಅನ್ನು ಸ್ವಯಂಮರ್ಜ್ ಮಾಡುವುದಿಲ್ಲ. ದೊಡ್ಡ ರೆಪೊಗಳಿಗಾಗಿ, ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಬದಲಾಗುವಾಗ ಮಾತ್ರ ವರ್ಕ್ಫ್ಲೋ ಓಡಿಸಲು `on.push` ಅಡಿಯಲ್ಲಿ `paths:` ಫಿಲ್ಟರ್ ಅನ್ನು ಸೇರಿಸಬಹುದು.

### ಐಚ್ಛಿಕ: ನೋಟ್‌ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರಗಳು

ನೋಟ್‌ಬುಕ್ಸ್‌ಗಳಿಗೆ, ಅನುವಾದ ಕಮಾಂಡ್‌ಗೆ `-nb` ಅನ್ನು ಸೇರಿಸಿ ಮತ್ತು ರಿವ್ಯೂ ಹಂತದಲ್ಲಿ `notebook=True` ಅನ್ನು ಸೆಟ್ ಮಾಡಿ. ಚಿತ್ರ ಪಠ್ಯಕ್ಕಾಗಿ, ಎರಡು [Azure AI Vision ರಹಸ್ಯಗಳನ್ನು](#prerequisites) ಸಂರಚಿಸಿ, ಅವುಗಳನ್ನು ಅನುವಾದ ಹಂತದ `env` ನಲ್ಲಿ ಪಾಸ್ ಮಾಡಿ, ಕಮಾಂಡ್‌ಗೆ `-img` ಅನ್ನು ಸೇರಿಸಿ, ಮತ್ತು PR ಹಂತದ `add-paths` ಗೆ `translated_images/` ಅನ್ನು ಸೇರಿಸಿ. ಅನುವಾದಿತ ಚಿತ್ರಗಳನ್ನು ದೃಷ್ಟಿ ಪಟುಕಾರಿಯಾಗಿ ಪರಿಶೀಲಿಸಿ; ನಿಖರವಾದ (deterministic) ರಿವ್ಯೂ ಚಿತ್ರ ಪಠ್ಯ ಅಥವಾ ಭಾಷಾ ನಿಖರತೆಯನ್ನು ಪ್ರಮಾಣೀಕರಿಸುವುದಿಲ್ಲ.

## GitHub ಆಪ್ ಸಂರಚನೆ

ನಿಮ್ಮ ಸಂಘಟನೆ App ಗುರುತು ಬೇಡಿಕೆ ಮಾಡಿದಾಗ ಅಥವಾ ಉತ್ಪನ್ನವಾದ PR ಗಾಗಿ `GITHUB_TOKEN` ಅನುಮೋದನೆ ಹಂತ ಇಲ್ಲದೆ ಡೌನ್‌ಸ್ಟ್ರೀಂ CI ಅನ್ನು ಪ್ರೇರೇಪಿಸಲು ಬೇಕಾಗುವಾಗ ಅನುಮೋದಿತ GitHub App ಅನ್ನು ಬಳಸಿ. App ಸಂಸ್ಥೆಯ ನೀತಿಯನ್ನೇ ಮೀರಿಸುವುದಿಲ್ಲ; ಅದರ ಇನ್‌ಸ್ಟಾಲೇಶನ್ ಮತ್ತು ಪರವಾನಗಿಗಳನ್ನು ನಿರ್ವಾಹಕರು ಇನ್ನೂ ನಿಯಂತ್ರಿಸುತ್ತಾರೆ.

### ಹಂತ 1: GitHub App ರಚಿಸಿ ಅಥವಾ ಸ್ಥಾಪಿಸಿ

ಲಭ್ಯವಿದ್ದಾಗ ಈಗಿರುವ ಸಂಸ್ಥೆ-ಒದಗಿಸಿದ App ಅನ್ನು ಬಳಸಿ, ಅಥವಾ **Contents** ಮತ್ತು **Pull requests** ಗೆ ಓದಿ/ಬರೆಯುವ ಪ್ರವೇಶವನ್ನು ಹೊಂದಿರುವ ಒಂದು App ರಚಿಸಿ. ಅತ್ಯವಶ್ಯಕ ಸಂಸ್ಥಾ ಅನುಮೋದನೆಯೊಂದಿಗೆ ಅದನ್ನು ಗುರಿ ರೆಪೊದಲ್ಲಿ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ.

ದಾಖಲಿಸಿ:

- App ID
- Private key contents

ಅವನ್ನು ರೆಪೊ ರಹಸ್ಯಗಳಾಗಿ ಸಂಗ್ರಹಿಸಿ:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### ಹಂತ 2: App Token ಉತ್ಪಾದಿಸಿ

ಈ ಹಂತವನ್ನು ಇದ್ದಕ್ಕಿದ್ದಂತೆ ಮಾರ್ಪಟ್ಟಿರುವ pull request ಹಂತಕ್ಕಿಂತ ಮುಂಚಿತವಾಗಿ ಸೇರಿಸಿ. README ಟೆಂಪ್ಲೇಟಿಗಾಗಿ, ಪ್ರಿವ್ಯೂಗಳು ಮತ್ತು ವಿಫಲವಾದ ಅನುವಾದಗಳು App ಟೋಕನ್ ವಿನಂತಿಯನ್ನು ಮಾಡದಿರಲು ಅದೇ ಯಶಸ್ಸಿನ ಶರತ್ತುಗಳನ್ನು ಬಳಸಿ:

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

ನಂತರ ಇರುವ pull request ಹಂತದ `token` ಇನ್ಪುಟ್ ಅನ್ನು ಮಾತ್ರ `${{ steps.generate_token.outputs.token }}` ಗೆ ಬದಲಿಸಿ. ಅದರ ಯಶಸ್ಸಿನ ಶರತ್ತು, ಶಾಖೆ, PR ದೇಹ ಮತ್ತು `add-paths` ಅನ್ನು ಬದಲಿಸದೆ ಇಡಿ. ಟೋಕನ್ ಡೀಫಾಲ್ಟ್ ಆಗಿ ಪ್ರಸ್ತುತ ರೆಪೊಗೆ ವ್ಯಾಪ್ತಿಯಾಗಿರುತ್ತದೆ. README ಟೆಂಪ್ಲೇಟಿನ ಬದಲು ಮಾನಕ ಸೆಟಪ್ ಅನ್ನು ಹೊಂದಿಸಲು ಬಳಸಿದಾಗ ಮೇಲಿನ `if` ಅನ್ನು ಬಿಟ್ಟುಕೊಡಿ: ಆ ವರ್ಕ್ಫ್ಲೋ ಡೀಫಾಲ್ಟ್ ಯಶಸ್ಸಿನ ಶರತ್ತರನ್ನು ಬಳಸುತ್ತದನ್ನು, ಆದ್ದರಿಂದ ಟೋಕನ್ ರಚನೆ ಮತ್ತು PR ರಚನೆಯು ಅನುವಾದ ಮತ್ತು ಪರಿಶೀಲನೆ ಯಶಸ್ವಿಯಾದ ನಂತರ ಮಾತ್ರ ನಡೆಯುತ್ತವೆ.

ಇನ್‌ಸ್ಟಾಲೇಶನ್ ಮತ್ತು ಟೋಕನ್ ಪರವಾನಗಿಗಳಿಗಾಗಿ ಅಧಿಕೃತ [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) ನೋಡಿ.

## ರನ್ನರ್ ಮಿತಿಗಳು

GitHub-ಹೋಸ್ಟ್ ಮಾಡಿದ ರನ್ನರ್‌ಗಳಿಗೆ ಗರಿಷ್ಠ ಜಾಬ್ ಅವಧಿ ಇರುತ್ತದೆ. ದೊಡ್ಡ ರೆಪೊಗಳು ಅಥವಾ ಅನೇಕ ಗುರಿ ಭಾಷೆಗಳು ಆ ಮಿತಿಯನ್ನು ಮೀರಿಸಬಹುದಾಗಿದೆ.

ದೊಡ್ಡ ಅನುವಾದ ಭಾರಗಳಿಗೆ:

- ಒಂದು ಚಲನೆಗೆ ಕಡಿಮೆ ಭಾಷೆಗಳನ್ನು ಅನುವದಿಸಿ.
- `-md`, `-nb`, ಅಥವಾ `-img` ಮುಂತಾದ ವಿಷಯ ಹೋರಣಿಗಳನ್ನು ಬಳಸಿ.
- ರೆಪೊ ಗಾತ್ರ ಅಥವಾ ಮಾದರಿ ವಿಳಂಬತೆಯು ಹೋಸ್ಟ್ ಮಾಡಿದ ರನ್ನರ್‌ಗಳನ್ನು ಅಪ್ರತಿಷ್ಠಿತ ಮಾಡುವಾಗ self-hosted ರನ್ನರ್ ಅನ್ನು ಬಳಸಿ.

## CI ನಲ್ಲಿ ಪರಿಶೀಲನೆ

LLM ಅಥವಾ Vision ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆಯದೆ ರಚಿಸಲಾದ ಅನುವಾದಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸಲು pull request ಒಂದು ಸತ್ಯಪಡೆಯಬೇಕಾದರೆ `co-op-review` ಅನ್ನು ಬಳಸಿ.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ಒಂದು ಬೀಟಾ ನಿರ್ಧಾರಾತ್ಮಕ (deterministic) ರಿವ್ಯೂ ಕಮಾಂಡ್. ಇದರ ತಪಾಸಣೆಗಳು ಮತ್ತು ಔಟ್‌ಪುಟ್ ಸ್ಕೀಮಾ ಬದಲಾಗಬಹುದು, ಆದರೆ ಇದು CI ಗೆ ಸುರಕ್ಷಿತವಾಗಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ ಏಕೆಂದರೆ ಇದು ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುವುದಿಲ್ಲ ಅಥವಾ ಮಾದರಿ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆದು ಸಾಧ್ಯ.