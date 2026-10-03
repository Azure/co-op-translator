# GitHub Actions

மாற்றப்பட்ட ஆவணங்களை தானாக மொழிமாற்றம் செய்து உருவாக்கப்பட்ட வெளியீடுகளுடன் ஒரு pull request திற விரும்பினால் GitHub Actions ஐப் பயன்படுத்துங்கள்.

அமைப்புச் சீரமைப்பாக உள்ள `GITHUB_TOKEN` அமைப்புடன் தொடங்குங்கள், விதிகள் அனுமதிக்கும் அமைப்புத் தொகுதிகளுக்கும் இதேபோல. உங்கள் அமைப்பு ஒரு App அடையாளத்தைக் கோரினால் அல்லது தானாக இணைப்பட்ட downstream workflow ஓட வேண்டுமானால் [GitHub App Setup](#github-app-setup) ஐ காணவும்.

**மனிதர் திருத்தங்கள்:** இந்த வேலைகள் மாற்றப்பட்ட மூல கோப்புகளை முழுமையாக மீண்டும் மொழிபெயர்க்கின்றன மற்றும் அவற்றின் மொழிபெயர்ப்புகளில் செய்யப்பட்ட சொற்களை ஒதுக்கிக்கொள்ளலாம். ஒற்றை PR ஐ இணைப்பதற்கு முன் அவை அனைத்தையும் பரிசீலிக்கவும். ஏற்றுக்கொள்ளப்பட்ட திருத்தங்களின் Markdown தொகுதி மட்டமான பாதுகாப்பு [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) உடன் தனிப்பயன் ஒருங்கிணைப்பை தேவைப்படுத்தும்.

## உங்கள் முதல் README மொழிபெயர்ப்பு PR

ஒரு root `README.md` மற்றும் ஒரு இலக்கு மொழியுடன் தொடங்குங்கள். இந்த workflow Markdown மட்டும் மொழிபெயர்க்கும், ஆகவே Azure AI Vision தேவைப்படும் அளவு இல்லை.

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([GitHub இல் வடிவமைப்பை காண்க](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ஐ நீங்கள் மொழிபெயர்க்க விருக்கும் களஞ்சியத்தின் `.github/workflows/translate-readme.yml` ஆக நகலெடுத்து அதனை அதன் இயல்புநிலைக் கிளையில் commit செய்யவும். இந்த வடிவமைப்பு root Action ஐ `Azure/co-op-translator@main` இலிருந்து பயன்படுத்துகிறது, அதே source ref இலிருந்து CLI ஐ நிறுவும். மறுபடியும் இயக்கங்களுக்கு புனரூபக்கமான நடத்தை உறுதிப்படுத்த ஒரு ஆய்வு செய்யப்பட்ட commit ஐ pin செய்யவும்.
2. **Actions > Translate README > Run workflow** ஐ திறந்து ஒரு மொழியை தேர்ந்தெடுத்து **முன்னோட்டு மட்டுமே** (**Preview only**) தேர்வை செயல்படுத்தவிட்டு வைக்கவும். முன்னோட்ட படியில் token மதிப்பீட்டை பரிசீலிக்கவும். முன்னோட்டி மாதிரி प्रदाता மாடல்களை அழைப்பதில்லை, மொழிபெயர்ப்புகளை எழுதுவதில்லை அல்லது PR உருவாக்குவதில்லை.
3. ஒரு [text provider](#prerequisites) க்கான ரகசியங்களைச் சேர்க்கவும், மற்றும் **அமைப்புகள் > Actions > பொது** இல் **GitHub Actions-க்கு pull requests உருவாக்கவும் மற்றும் ஒப்புக்கொள்ள அனுமதிக்கவும்** ஐ இயக்கி அனுமதி அளிக்கவும். இந்த வடிவம் அதன் ஜாப் க்கு `contents: write` மற்றும் `pull-requests: write` என்பதை கோருகிறது; ஒவ்வொரு வொர்க்ஃப்ளோக்கும் இயல்புநிலை அனுமதிகளை மாற்ற தேவையில்லை. அமைப்பு கொள்கை இந்த அனுமதிகளை அல்லது இந்த அமைப்பை தடுக்கும் பட்சத்தில், அனுமதி பெற்ற [GitHub App](#github-app-setup) பற்றி நிர்வாகியிடம் கேட்கவும்.
4. **முன்னோட்டு மட்டுமே** ஐ நீக்கி workflow ஐ மீண்டும் இயக்கவும். அது முன்னோட்டம் காட்டும், மொழிபெயர்க்கும், `co-op-review --readme-only` ஐ இயக்கும், மற்றும் மொழிபெயர்ப்பும் பரிசீலனையும் வெற்றி பெற்ற பிறகு மட்டுமே மொழிபெயர்ப்பு PR ஐ உருவாக்கும் அல்லது புதுப்பிக்கும். workflow சுருக்கம் PR ஐ இணைக்கும் இணைப்பை வழங்கும்.
5. PR இல் சொற்களையும் கோப்பு மாற்றங்களையும் மதிப்பாய்வு செய்து தயார் என்றபின் merge செய்யுங்கள். workflow தானாக merge செய்யாது.

PR இல் `translations/<language>/README.md` மற்றும் அதற்கான மொழி metadata கோப்பு மட்டுமே உள்ளது. மூல README மாற்றமில்லை, மற்ற ஆவணங்களுக்கு உள்ள இணைப்புகள் எப்போதும் மூல ஆவணங்களைத் தானாக குறிக்கின்றன. PR உட்பொருள் மாற்றப்பட்ட கோப்புகள் மற்றும் அமைப்புச் சோதனை முடிவுகளை பட்டியலிடும். மொழிபெயர்ப்பு அல்லது பரிசீலனை தவறானால் workflow சுருக்கத்தையும் தோல்வி அடைந்த படி படிகள் உள்ள பதிவுகளையும் பரிசீலிக்கவும்; எந்த PR உருவாகாது. மாற்றங்கள் இல்லாவிட்டால் புதிய PR தேவைப்படாது.

**அமைப்பு மற்றும் CI குறிப்பு:** GitHub App என்பது விருப்பமானது; அமைப்புச் சொந்தத்திற்கான கட்டாயம் அல்ல. `GITHUB_TOKEN` உடன், ஒரு PR திறப்பு, புதுப்பிப்பு அல்லது மறுதிறப்பு போன்ற pull-request வேலைப்பாடுகள் "Approve workflows to run" ஐ தேர்ந்தெடுக்கும் எழுதும் அணுகல் கொண்ட பயனரை தேவைப்படுத்தும். Push வேலைப்பாடுகள் இந்த token மூலம் தொடங்கப்படமாட்டாது. தானாக இயக்கப்படும் downstream CI க்காக, [GitHub App Setup](#github-app-setup) மற்றும் GitHub இன் [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) பார்க்கவும்.

## Prerequisites

workflow ஐ உருவாக்குவதற்கு முன்பு, உங்கள் மொழிபெயர்ப்பு ஓட்டத்திற்கு தேவையான AI சேவை ரகசியங்களை பதிப்பமைக்கவும்.

உரை மொழிபெயர்ப்புக்காக ஒரு மொழி மாதிரி வழங்குநர் தேவை:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

படங்கள் மொழிபெயர்ப்புக்கு கூடுதல் விதமாக Azure AI Vision தேவைப்படும்:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

உள்ளக அளவீட்டிற்கு [Configuration](configuration.md) மற்றும் [Azure AI Setup](azure-ai-setup.md) ஐ காணவும்.

## சாதாரண அமைப்பு

README workflow ஐ முயற்சி செய்த பிறகு, களஞ்சியத்தின் Markdown கோப்புகளை பல மொழிகளாக மொழிபெயர்க்க இந்த அமைப்பை பயன்படுத்தவும். இது PR திறப்பதற்கு முன் Markdown மதிப்பாய்வை ஓட்டும் மற்றும் Azure AI Vision தேவைப்படாது.

### படி 1: களஞ்சிய ரகசியங்களைச் சேர்க்கவும்

இலக்கு களஞ்சியத்தில் **Settings** > **Secrets and variables** > **Actions** ஐ திறந்து, உங்கள் workflow பயன்படுத்தும் provider ரகசியங்களைச் சேர்க்கவும்.

![Actions ரகசியங்களைத் தேர்ந்தெடுக்கவும்](../../assets/github-actions/select-setting-action.png)

### படி 2: வேலைப்பிரவாக அனுமதிகளை இயக்கவும்

**Settings** > **Actions** > **General** ஐ திறக்கவும்.

**Workflow permissions** என்பதின் கீழ்:

1. **GitHub Actions-க்கு pull requests உருவாக்கவும் மற்றும் ஒப்புக்கொள்ள அனுமதிக்கவும்** ஐ இயக்கு.
2. அந்த அமைப்பைச் சேமிக்கவும்.

கீழே உள்ள job தெளிவாக `contents: write` மற்றும் `pull-requests: write` ஐ கோருகிறது. களஞ்சியத்தின் இயல்புநிலை workflow அனுமதிகளை மாற்ற வேண்டாம். அமைப்பு கொள்கை PR உருவாக்கத்தை தடுக்குமானால், அனுமதிக்கப்பட்ட [GitHub App](#github-app-setup) பற்றி நிர்வாகியிடம் கேளுங்கள்.

### படி 3: வொர்க்ஃப்ளோவைச் சேர்க்கவும்

`.github/workflows/co-op-translator.yml` ஆகிய கோப்பை உருவாக்கவும்:

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

`TARGET_LANGUAGES` ஐ உங்கள் திட்டத்திற்கு தேவையான மொழிகளுக்கு மாற்றவும். மதிப்பாய்வு Python API ஐ பயன்படுத்தி Markdown மட்டும் சரிபார்க்கும், இது மொழிபெயர்ப்பு படிக்கொடுக்கும் படிக்கு பொருந்தும். மொழிபெயர்ப்பு அல்லது மதிப்பாய்வு தவறு வரும் போதும் job PR உருவாக்கத்திற்கு முன் நிறுத்தப்படு. workflow PR ஐ தானாக merge செய்யாது. பெரிய களஞ்சியங்களுக்கு, documentation மாற்றப்பட்டால் மட்டும் workflow ஓட `on.push` கீழ் `paths:` வடிகட்டியைச் சேர்க்கவும்.

### விருப்பமானது: நோட்புக் மற்றும் படங்கள்

நோ้ட்புக்குகளுக்கு, மொழிபெயர்ப்பு கட்டளையில் `-nb` சேர்க்கவும் மற்றும் மதிப்பாய்வில் `notebook=True` என அமைக்கவும். படங்களில் உள்ள உரைக்கு, இரண்டு [Azure AI Vision secrets](#prerequisites) ஐ கட்டமைக்கவும், அவற்றை மொழிபெயர்ப்பு படியின் `env` இல் பரிமாறவும், கட்டளையில் `-img` ஐ சேர்க்கவும், மற்றும் PR படியின் `add-paths` இல் `translated_images/` ஐ சேர்க்கவும். மொழிபெயர்க்கப்பட்ட படங்களை கண் பார்வையால் மதிப்பாய்வு செய்யவும்; தீர்ணமான (deterministic) மதிப்பாய்வு பட உரை அல்லது மொழியியல் துல்லியத்தினை சான்றளிக்காது.

## GitHub செயலி அமைப்பு

உங்கள் அமைப்பு ஒரு App அடையாளத்தைத் தேவைப்படுத்தும் போது அல்லது உருவாக்கப்பட்ட PR `GITHUB_TOKEN` அங்கீகாரம் இல்லாமல் downstream CI ஐ trigger செய்ய வேண்டுமெனில் அனுமதிக்கப்பட்ட GitHub App ஐப் பயன்படுத்துங்கள். App அமைப்பு அமைப்பு கொள்கையை தவிர்க்காது; அதன் நிறுவல் மற்றும் அனுமதிகளை நிர்வாகிகள் இன்னும் கட்டுப்படுத்துவார்கள்.

### படி 1: ஒரு GitHub App உருவாக்கவும் அல்லது நிறுவவும்

கிடைத்தால் அமைப்பு வழங்கிய உள்ளமைவான App ஐ பயன்படுத்துங்கள், அல்லது **Contents** மற்றும் **Pull requests** க்கு படிக்க/எழுத அனுமதியுடன் ஒன்றை உருவாக்குங்கள். தேவையான அமைப்பு அனுமதியுடன் அதை இலக்கு களஞ்சியத்தில் நிறுவவும்.

Record:

- App ID
- Private key contents

அவற்றை களஞ்சிய ரகசியங்களாக சேமிக்கவும்:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### படி 2: ஒரு App டோக்கனை உருவாக்கவும்

உள்ளமைவான pull request படிக்கு 바로 இந்த படியைச் சேர்க்கவும். README வடிவமைப்புக்கு, முன்னோட்டங்கள் மற்றும் தோல்வியடைந்த மொழிபெயர்ப்புகள் App token ஐ கோராமையிருக்க இதே success நிபந்தனையைப் பயன்படுத்தவும்:

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

பின்னர் உள்ள pull request படியின் `token` உள்ளீட்டை மட்டும் `${{ steps.generate_token.outputs.token }}` ஆக மாற்றவும். அதன் success நிபந்தனை, branch, PR உட்பொருள் மற்றும் `add-paths` மாற்றமின்றி வைக்கவும். token இயல்பாக தற்போதைய களஞ்சியத்திற்கு மட்டுமே வரம்பிடப்பட்டுள்ளது. README வடிவமைப்புக்குப் பதிலாக தரநிலை அமைப்பை ஏற்றுக்கொள்ளும்போது மேலேயுள்ள `if` ஐ விட்டு வையுங்கள்: அந்த workflow இயல்புநிலை success நிபந்தனையைப் பயன்படுத்தும், ஆகவே token உருவாக்கமும் PR உருவாக்கமும் மொழிபெயர்ப்பு மற்றும் மதிப்பாய்வு வெற்றி பெற்றபின் மட்டும் ஓடும்.

நிறுவல் மற்றும் token அனுமதிகளுக்காக அதிகாரப்பூர்வ [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) ஐ காணவும்.

## ரன்னர் வரம்புகள்

GitHub-பாாணித்த runners க்கு ஒரு அதிகபட்ச job கால அவகாசம் உள்ளது. பெரிய களஞ்சியங்கள் அல்லது பல இலக்கு மொழிகள் அந்த வரம்பை மீறலாம்.

பெரிய மொழிபெயர்ப்பு வேலைப்பளукиங்களுக்கு:

- ஓட்டத்திற்கு குறைவான மொழிகளை மொழிபெயர்க்கவும்.
- `-md`, `-nb`, அல்லது `-img` போன்ற உள்ளடக்க கொடிகளை பயன்படுத்தவும்.
- কளஞ்சியத்தின் அளவு அல்லது மாதிரி தாமதம் இடையே hosted runners நம்பகமாக இல்லாவிட்டால் self-hosted runner ஐப் பயன்படுத்தவும்.

## CI இல் மதிப்பாய்வு

LLM அல்லது Vision வழங்குநர்களை அழைக்காமல் உருவாக்கப்பட்ட மொழிபெயர்ப்புகளை சரிபாரிக்க வேண்டும் என்றால் `co-op-review` ஐப் பயன்படுத்தவும்.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` என்பது பீட்டா திடமான (deterministic) மதிப்பாய்வு கட்டளை. அதன் சோதனைகள் மற்றும் output schema பரிணாமம் அடையலாம், ஆனாலும் அது கோப்புகளை எழுதாது அல்லது மாடல் வழங்குநர்களை அழைக்காது என்பதால் CI க்கு பாதுகாப்பானதாக வடிவமைக்கப்பட்டது.