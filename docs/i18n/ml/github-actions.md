# GitHub Actions

നിങ്ങൾ ഒരു റിപ്പോസിറ്ററിയിലെ മാറ്റപ്പെട്ട ഡോക്യുമെന്റേഷൻ സ്വയമേവ വിവർത്തനം ചെയ്യിച്ച് സൃഷ്ടിച്ച ഔട്ട്പുട്ടുകളോട് ചേർന്ന് ഒരു പുൾ റിക്വസ്റ്റ് തുറക്കണമെന്നാൽ GitHub Actions ഉപയോഗിക്കുക.

പ്രമാണത്തിന്റെ സാധാരണ `GITHUB_TOKEN` ക്രമീകരണത്തോട് കൂടി തുടങ്ങുക — ഓർഗനൈസേഷന്‍ റിപ്പോസിറ്ററികളിൽ നയം അനുവദിച്ചാൽ അത് ഉൾപ്പെടും. നിങ്ങളുടെ ഓർഗനൈസേഷനു ഒരു App ഐഡന്റിറ്റി ആവശ്യമുണ്ടെങ്കിൽ അല്ലെങ്കിൽ ഓട്ടോമാറ്റിക് डाउनസ്ട്രീം workflow റൺസുകൾ ആവശ്യമുള്ളപ്പോൾ [GitHub App Setup](#github-app-setup) നോക്കുക.

**Human edits:** ഈ പ്രവൃത്തിപദ്ധതികൾ മാറ്റംവരിച്ചത് ഉറവിട ഫയലുകൾ പൂര്‍ണമായും വീണ്ടും വിവർത്തനം ചെയ്ത് അവരുടെ വിവർത്തനങ്ങളിൽ മാറ്റങ്ങളായി ചെയ്ത വാചകങ്ങൾ ഒভারറൈറ്റുചെയ്യാം. മേഴ്ജ് ചെയ്യുന്നത്ആഗേക്ക് മുമ്പ് ഓരോ PR-വും അവലോകനം ചെയ്യുക. അംഗീകരിച്ച എഡിറ്റുകളുടെ മാർക്ക്ഡൗൺ ബ്ലോക്ക്-തല സംരക്ഷണം ഉറപ്പാക്കുന്നതിന് [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ന്റെ ഇന്റഗ്രേഷൻ വേണം.

## നിങ്ങളുടെ ആദ്യ README പരിഭാഷ PR

ഒരു റൂട്ട് `README.md` ഒന്ന് കൂടി ഒരു ലക്ഷ്യ ഭാഷ മാത്രം ഉപയോഗിച്ച് തുടങ്ങുക. ഈ workflow മാർക്ക്ഡൗൺ മാത്രമേ വിവർത്തനം ചെയ്യൂ; അതുകൊണ്ട് Azure AI Vision ആവശ്യപ്പെട്ടിട്ടില്ല.

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) നിങ്ങളുടെ വിവർത്തനം ചെയ്യാൻ ആഗ്രഹിക്കുന്ന റിപ്പോസിറ്ററിയിലെ `.github/workflows/translate-readme.yml` എന്ന സ്ഥാനത്ത് പകർത്തി ആ റിപ്പോസിറ്ററിയുടെ ഡീഫോൾട്ട് ബ്രാഞ്ചിലേക്ക് commit ചെയ്യുക. ടെംപ്ലേറ്റ് `Azure/co-op-translator@main` എന്ന റൂട്ട് Action ഉപയോഗിക്കുന്നു, അത് CLI-നെ അതേ സോഴ്‌സ് റെഫിൽ നിന്നാണ് ഇൻസ്റ്റാൾ ചെയ്യുന്നത്. പുനരാവൃത്തി നടത്താവുന്ന റൺസിനായി പരിശോധിച്ചിട്ടുള്ള commit ഒരു pinned റഫറൻസായി ഉപയോഗിക്കുക.
2. Open **Actions > Translate README > Run workflow**, ഒരു ഭാഷ തിരഞ്ഞെടുക്കുക, തുടർന്ന് **Preview only** തിരഞ്ഞെടുക്കപ്പെട്ടിരിക്കുന്ന നിലയിൽ വിടുക. പ്രിവ്യൂ ഘട്ടത്തിൽ ടോക്കൺ അവലോകനം നോക്കുക. പ്രിവ്യൂ മോഡിൽ മോഡൽ പ്രൊവൈഡറുകളോട് കോൾ ചെയ്യുകയോ വിവർത്തനങ്ങൾ എഴുതുകയോ PR സൃഷ്ടിക്കുകയോ ചെയ്യില്ല.
3. ഒരു [ടെക്സ്റ്റ് പ്രൊവൈഡർ](#prerequisites) ലുള്ള രഹസ്യങ്ങൾ ചേർക്കുക, കൂടാതെ **Settings > Actions > General** ൽ **GitHub Actions-നെ പുൾ റിക്വസ്റ്റ് സൃഷ്ടിക്കുകയും അംഗീകരിക്കുകയും ചെയ്യാൻ അനുവദിക്കുക** സജീവമാക്കുക. ടെംപ്ലേറ്റ് അതിന്റെ ജോബിന് `contents: write` മാറിയും `pull-requests: write` അഭ്യർത്ഥിക്കുന്നു; ഓരോ വർക്ക്ഫ്ലോക്കും ഡീഫോൾട്ട് അനുമതികൾ മാറ്റേണ്ടതില്ല. ഓർഗനൈസേഷൻ നയം ഈ അനുമതികൾ അല്ലെങ്കിൽ ഈ ക്രമീകരണം തടയിക്കുന്നുവെങ്കിൽ, അംഗീകൃത [GitHub ആപ്പ്](#github-app-setup) സംബന്ധിച്ച് അഡ്മിനിസ്ട്രേറ്ററുമായി സംസാരിക്കുക.
4. **Preview only** ഓഫ് ചെയ്ത് workflow വീണ്ടും റൺ ചെയ്യുക. ഇത് പ്രിവ്യൂ ചെയ്യും, വിവർത്തനം ചെയ്യും, `co-op-review --readme-only` റൺ ചെയ്യും, വിവർത്തനവും റിവ്യൂയും വിജയിച്ച ശേഷം മാത്രം ഒരു വിവർത്തന PR സൃഷ്ടിക്കുകയും അപ്ഡേറ്റ് ചെയ്യുകയും ചെയ്യും. workflow സംഗ്രഹം PR-ിലേക്കുള്ള ലിങ്കുകൾ നൽകുന്നു.
5. PR-യിലെ വാചകങ്ങളും ഫയൽ മാറ്റങ്ങളും അവലോകനം ചെയ്ത് തയ്യാറാവുമ്പോൾ merge ചെയ്യുക. workflow സ്വയം ഫയൽ മേഴ്ജ് ചെയ്‌തുകൊള്ളുന്നില്ല.

PR-ൽ ഉണ്ടാവുക വെറും `translations/<language>/README.md` மற்றும் അതിന്റെ ഭാഷാ മെറ്റാഡേറ്റ ഫയലാണ്. ഉറവിട README മാറ്റമില്ലാതെ തുടരും, മറ്റ് രേഖകളിലേക്ക് ഉള്ള ലിങ്കുകൾ ഉറവിട രേഖകളിലേക്കോട് തുടരെയിരിക്കും. PR ബോഡിയിൽ മാറ്റിയ ഫയലുകളും ഘടനാത്മക റിവ്യൂ ഫലങ്ങളും പട്ടികവായി കാണിക്കും. വിവർത്തനമോ റിവ്യൂയോ പരാജയപ്പെട്ടാൽ workflow സംഗ്രഹവും പരാജയപ്പെട്ട ഘട്ട് ലോഗുകളും പരിശോധിക്കുക; ഈ ഘട്ടത്തിൽ PR സൃഷ്ടിക്കപ്പെടാൻ പോകില്ല. മാറ്റങ്ങൾ ഇല്ലെങ്കിൽ, പുതിയ PR ആവശ്യമില്ല.

**Organization and CI note:** GitHub App ഒരു നിർബന്ധമല്ല, ഓർഗനൈസേഷൻ ഉടമസ്ഥതയുടെ ആവശ്യകതയല്ല. `GITHUB_TOKEN` ഉപയോഗിക്കുമ്പോൾ ഒരു PR തുറക്കുന്നത്, അപ്ഡേറ്റ് ചെയ്യുന്നത് അല്ലെങ്കിൽ വീണ്ടും തുറക്കുന്നത് എന്നിവയ്ക്ക് വേണ്ടുന്ന പുൾ-റിക്വസ്റ്റു വേർക്ക്ഫ്ലോകള്‍ **Approve workflows to run** തിരഞ്ഞെടുക്കാൻ write access ഉള്ള ഒരു യൂസറിന്റെ പ്രവർത്തനം ആവശ്യമാണ്. Push workflows ഈ ടോക്കൺ കൊണ്ട് ട്രിഗർ ചെയ്യുന്നില്ല. അനൈദ്ധികമായ (unattended) ഡൗൺസ്ട്രീം CI ആവശ്യമായാൽ [GitHub App Setup](#github-app-setup) നോക്കുക അതോടൊപ്പം GitHub ന്റെ [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Prerequisites

workflow ഉണ്ടാക്കുന്നതിന് മുൻപ്, നിങ്ങളുടെ വിവർത്തന റൺ ആവശ്യപ്പെടുന്ന AI സർവീസ് രഹസ്യങ്ങൾ ക്രമീകരിക്കുക.

ടെക്സ്റ്റ് തർജ്ജമയ്ക്ക് ഒരു ഭാഷ മോഡൽ പ്രൊവൈഡർ ആവശ്യമാണ്:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

ഇമേജ് തർജ്ജമയ്ക്ക് പുറമേ Azure AI Vision ആവശ്യമാണ്:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

ലോക്കൽ കോൺഫിഗറേഷനുള്ള വിശദാംശങ്ങൾക്കായി [Configuration](configuration.md) மற்றும் [Azure AI Setup](azure-ai-setup.md) കാണുക.

## സ്റ്റാൻഡാർഡ് സജ്ജീകരണം

README workflow പരീക്ഷിച്ചതിന് ശേഷം, ഒരു റിപ്പോസിറ്ററിയിലെ മാർക്ക്ഡൗൺ ഫയലുകൾ പല ഭാഷകളിലാക്കി വിവർത്തനം ചെയ്യാൻ ഈ ക്രമീകരണം ഉപയോഗിക്കുക. PR തുറക്കുന്നതിന് മുൻപ് ഇത് മാർക്ക്ഡൗൺ റിവ്യൂ നടത്തുകയും Azure AI Vision ആവശ്യപ്പെടുകയില്ല.

### പടി 1: റിപ്പോസിറ്ററി രഹസ്യങ്ങൾ ചേർക്കുക

നിങ്ങളുടെ ലക്ഷ്യ റിപ്പോസിറ്ററിയിൽ **Settings** > **Secrets and variables** > **Actions** തുറന്ന് നിങ്ങളുടെ workflow ഉപയോഗിക്കാനാവശ്യമായ പ്രൊവൈഡർ രഹസ്യങ്ങൾ ചേർക്കുക.

![Actions രഹസ്യങ്ങൾ തിരഞ്ഞെടുക്കുക](../../assets/github-actions/select-setting-action.png)

### പടി 2: വർക്ക്ഫ്ലോ അനുമതികൾ സജീവമാക്കുക

Open **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. **GitHub Actions-നെ പുൾ റിക്വസ്റ്റ് സൃഷ്ടിക്കുകയും അംഗീകരിക്കുകയും ചെയ്യാൻ അനുവദിക്കുക** സജീവമാക്കുക.
2. Save the setting.

താഴെക്കാണുന്ന ജോബ് വ്യക്തമായി `contents: write` এবং `pull-requests: write` അഭ്യർത്ഥിക്കുന്നു. റിപ്പോസിറ്ററിയുടെ ഡീഫോൾട്ട് workflow അനുമതികൾ മാറരുത്. ഓർഗനൈസേഷൻ നയം PR സൃഷ്ടി തടയുകയാണെങ്കിൽ അംഗീകൃത [GitHub App](#github-app-setup) സംബന്ധിച്ച് അഡ്മിനിസ്ട്രേറ്ററോട് ചോദിക്കുക.

### പടി 3: വർക്ക്ഫ്ലോ ചേർക്കുക

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

`TARGET_LANGUAGES` നിങ്ങളുടെ പ്രോജക്ട് ആവശ്യപ്പെടുന്ന ഭാഷകളായി മാറ്റുക. റിവ്യൂ മാർക്ക്ഡൗൺ മാത്രം പരിശോധിക്കാൻ Python API ഉപയോഗിക്കുന്നു, ഇത് വിവർത്തന ഘട്ടத்தോടൊപ്പം പൊരുത്തപ്പെടുന്ന വിധത്തിലാണ്. വിവർത്തനമോ റിവ്യൂയോ പിഴച്ചാൽ PR സൃഷ്ടിക്കപ്പെടുന്നതിന് മുൻപ്_job_ നിർത്തും. workflow PR സ്വയം മേഴ്ജ് ചെയ്യില്ല. വലിയ റിപ്പോസിറ്ററികൾക്കായി, ഡോക്യുമെന്റേഷൻ മാറ്റങ്ങൾ മാത്രമായിരിക്കും workflow റൺ ചെയ്യാനായി `on.push` ഇന്റെ കീഴിൽ `paths:` ഫിൽറ്റർ ചേർക്കുക.

### ഐച്ഛികം: നോട്ട്ബുക്കുകളും ചിത്രങ്ങളും

നോട്ട്‌ബുക്കുകൾക്കായി, വിവർത്തന കമാൻഡിൽ `-nb` ചേർക്കുക എന്നും റിവ്യൂ ഘട്ടത്തിൽ `notebook=True` സെറ്റ് ചെയ്യുക. ഇമേജ് ടെക്സ്റ്റിന്, രണ്ട് [Azure AI Vision secrets](#prerequisites) ക്രമീകരിച്ച് അവ വിവർത്തന ഘട്ടത്തിന്റെ `env` വഴിയായി പാസ് ചെയ്യുക, കമാൻഡിൽ `-img` ചേർക്കുക, և PR ഘട്ടത്തിലെ `add-paths` ലേക്ക് `translated_images/` ചേർക്കുക. വിവർത്തനചെയ്ത ചിത്രങ്ങൾ കണ്ണടക്കി പരിശോധിക്കുക; ഡിറ്റർമിനിസ്റ്റിക് റിവ്യൂ ഇമേജ് ടെക്സ്റ്റിന്റെയും ഭാഷാ ശരിയായിത്തിരിയ്ക്കലിന്റെയും സർട്ടിഫിക്കേഷൻ നൽകുന്നില്ല.

## GitHub ആപ്പ് സജ്ജീകരണം

നിങ്ങളുടെ ഓർഗനൈസേഷൻ ഒരു App ഐഡന്റിറ്റി ആവശ്യപ്പെടുന്നുവെങ്കിൽ അല്ലെങ്കിൽ സൃഷ്ടിച്ച PR ന് `GITHUB_TOKEN` അംഗീകാരം ഇല്ലാതെ डाउनസ്ട്രീം CI ട്രിഗ്ഗർ ചെയ്യേണ്ടതായി വന്നാൽ ഒരു അംഗീകൃത GitHub App ഉപയോഗിക്കുക. ഒരു App ഓർഗനൈസേഷൻ നയം മറികടക്കില്ല; അതിന്റെ ഇൻസ്റ്റാളേഷനും അനുമതികളും അഡ്മിനിസ്ട്രേറ്റർമാരാണ് നിയന്ത്രിക്കുക.

### പടി 1: GitHub ആപ്പ് സൃഷ്ടിക്കുക അല്ലെങ്കിൽ ഇൻസ്റ്റാൾ ചെയ്യുക

ലഭ്യമായാൽ നിലവിലുള്ള ഓർഗനൈസേഷൻ-സൌജന്യ App ഉപയോഗിക്കുക, അല്ലെങ്കിൽ **Contents** এবং **Pull requests** ന് വായന/എഴുത്ത് ആക്‌സസ് നൽകിയ ഒരു App ഉണ്ടാക്കുക. ആവശ്യമായ ഓർഗനൈസേഷൻ അംഗീകാരം എടുത്ത് അതിനെ ലക്ഷ്യ റിപ്പോസിറ്ററിയിൽ ഇൻസ്റ്റാൾ ചെയ്യുക.

Record:

- App ID
- Private key contents

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### പടി 2: ആപ്പ് ടോക്കൺ ജനറേറ്റ് ചെയ്യുക

നിലവിലുള്ള പുൾ റിക്വസ്റ്റ് ഘട്ടത്തിന് 바로 മുമ്പ് ഈ ഘട്ടം ചേർക്കുക. README ടെംപ്ലേറ്റിനായി, പ്രിവ്യൂകളും പരാജയപ്പെട്ട വിവർത്തനങ്ങളും App ടോക്കൺ അഭ്യർത്ഥിക്കത്തക്കില്ല എന്നതിനായി അതേ വിജയശരത്സ് istifadə ചെയ്യുക:

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

പിന്നീട് നിലവിലുള്ള പുൾ റിക്വസ്റ്റ് ഘട്ടത്തിന്റെ `token` ഇൻപുട്ടിനെ മാത്രം `${{ steps.generate_token.outputs.token }}` ആയി മാറ്റുക. അതിന്റെ വിജയശരത്സ്, ബ്രാഞ്ച്, PR ബോഡി, և `add-paths` എല്ലാം മാറ്റരുത്. ടോക്കൺ സാധാരണയായി നിലവിലെ റിപ്പോസിറ്ററിക്ക് സ്‌കോപ്പ് ചെയ്യപ്പെട്ടിരിക്കുന്നു. README ടെംപ്ലേറ്റ് പകരം സ്റ്റാൻഡേർഡ് ക്രമീകരണം ഉപയോഗിക്കുമ്പോൾ മുകളിലുള്ള `if` ഒഴിവാക്കുക: ആ workflow ഡീഫോൾട്ട് വിജയശരത്സ് ഉപയോഗിക്കുന്നതാണ്, അതുകൊണ്ട് ടോക്കൺ സൃഷ്ടിയും PR സൃഷ്ടിയും വിവർത്തനവും റിവ്യൂയും വിജയിച്ചതിനു ശേഷം മാത്രം നടക്കും.

ഇൻസ്റ്റലേഷൻക്കും ടോക്കൺ അനുമതികൾക്കും ഔദ്യോഗിക [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) കാണുക.

## റണ്ണർ പരിധികൾ

GitHub-ഓട് ഹോസ്റ്റുചെയ്യുന്ന റണ്ണറുകൾക്ക് പരമാവധി ജോബ് ദൈർഘ്യമുണ്ട്. വലിയ റിപ്പോസിറ്ററികളും നിരവധി ലക്ഷ്യഭാഷകളും ആ പരിധി കടക്കാൻ സാധ്യതയുണ്ട്.

വലിയ വിവർത്തന പ്രവൃത്തി ഭാരത്തിന്:

- ഒരു റൺയിൽ കുറയ്ന്ന ഭാഷകളെ വിവർത്തനം ചെയ്യുക.
- `-md`, `-nb`, അല്ലെങ്കിൽ `-img` പോലുള്ള കോൺടെന്റ് ഫ്ലാഗുകൾ ഉപയോഗിക്കുക.
- റിപ്പോസിറ്ററി വലുതായിരിക്കുകയോ മോഡൽ ലേറ്റൻസി ഹോസ്റ്റുചെയ്യുന്ന റണ്ണറുകളെ വിശ്വാസയോഗ്യമാക്കുന്നില്ലെങ്കിൽ self-hosted runner ഉപയോഗിക്കുക.

## CI-ൽ അവലോകനം

LLM അല്ലെങ്കിൽ Vision പ്രൊവൈഡറുകളേ വിളിക്കാതെ ജനറേറ്റുചെയ്‌ത വിവർത്തനങ്ങൾвалидേറ്റ് ചെയ്യേണ്ടത് ഒരു പുൾ റിക്വസ്റ്റ് ഉണ്ടെങ്കിലാണെങ്കിൽ `co-op-review` ഉപയോഗിക്കുക.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ഒരു ബീറ്റാ ഡിറ്റർമിനിസ്റ്റിക് റിവ്യൂ കമാൻഡാണ്. അതിന്റെ പരിശോധനകളും ഔട്ട്പുട്ട് സ്കീമയും മാറ്റംവരിക്കാം, പക്ഷേ ഇത് CI-ക്കു സുരക്ഷിതമാക്കാൻ രൂപകൽപ്പന ചെയ്തതാണ് കാരണം ഇത് ഫയലുകൾ എഴുതുകയോ മോഡൽ പ്രൊവൈഡറുകളെ വിളിക്കുകയോ ചെയ്യില്ല.