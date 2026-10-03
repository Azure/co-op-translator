# GitHub Actions

ប្រើ GitHub Actions នៅពេលដែលអ្នកចង់ឲ្យ repository បកប្រែឯកសារដែលបានផ្លាស់ប្ដូរយ៉ាងស្វ័យប្រវត្តិ និងបើក pull request ជាមួយលទ្ធផលដែលបានបង្កើត។

ចាប់ផ្តើមជាមួយការកំណត់ស្តង់ដារ `GITHUB_TOKEN` រួមទាំងសម្រាប់ repos ក្នុងអង្គការដែលគោលនយោបាយអនុញ្ញាត។ មើល [ការកំណត់ GitHub App](#github-app-setup) នៅពេលអង្គការរបស់អ្នកទាមទារបណ្តាញអត្តសញ្ញាណ App ឬអ្នកត្រូវការការប្រតិបត្តិការ workflow ដោយស្វ័យប្រវត្តិសម្រាប់ downstream។

**Human edits:** វិធីសាស្ត្រទាំងនេះធ្វើការបកប្រែឡើងវិញឯកសូម៉ោងម៉ោងដើមដែលបានផ្លាស់ប្ដូរជាមួយ និងអាចលុបពាក្យដែលបានកែសម្រួលក្នុងការបកប្រែ។ សូមពិនិត្យមើល PR ណាដែលមុននឹងរួមបញ្ចូល។ ការអង្គរក្សកម្រិតប្លុក Markdown សម្រាប់កែសម្រួលដែលទទួលបានទាមទារ ឧបករណ៍បច្ចេកវិទ្យាផ្ទាល់ខ្លួនជាមួយ [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)។

## PR ការបកប្រែ README ជាលើកដំបូងរបស់អ្នក

ចាប់ផ្តើមជាមួយ README មូលដ្ឋានតែមួយ `README.md` និងភាសាគោលដៅមួយ។ វិធីសាស្ត្រនេះបកប្រែ Markdown តែប៉ុណ្ណោះ ដូច្នេះ មិនចាំបាច់មាន Azure AI Vision ទេ។

1. ចម្លង [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ទៅ `.github/workflows/translate-readme.yml` ក្នុង repository ដែលអ្នកចង់បកប្រែ ហើយ commit វាទៅ branch ដើម។ តំរូវប័ណ្ណប្រើ root Action នៅ `Azure/co-op-translator@main` ដែលតំឡើង CLI ពី source ref ដូចគ្នា។ បិទកំណត់​ជា commit ដែលបានពិនិត្យសម្រាប់ការប្រតិបត្តិអាចធ្វើឡើងម្តងទៀតបាន។
2. បើក **Actions > Translate README > Run workflow**, ជ្រើសភាសាមួយ ហើយទុក **Preview only** ឲ្យបានបានសម្គាល់។ ពិនិត្យក្រុមហ៊ុន token ហេលក្នុងដំណាក់កាល preview។ Preview មិនហៅអ្នកផ្ដល់ម៉ូដែល មិនសរសេរ​ការ​បកប្រែ ហើយមិនបង្កើត PR ទេ។
3. បន្ថែម secrets សម្រាប់មួយ [អ្នកផ្គត់ផ្គង់អត្ថបទ](#prerequisites) ហើយបើក **អនុញ្ញាតឲ្យ GitHub Actions បង្កើត និងអនុម័ត pull requests** នៅក្រោម **Settings > Actions > General**។ តំណការងារនៅក្នុង template ស្នើសុំ `contents: write` និង `pull-requests: write` សម្រាប់ job របស់វា; អ្នកមិនចាំបាច់ផ្លាស់ប្តូរសិទ្ធិលំនាំដើមសម្រាប់ workflow គ្រប់ផ្លូវទេ។ ប្រសិនបើគោលនយោបាយអង្គការកំព្រឹកសិទ្ធិទាំងនេះ ឬការកំណត់នេះ ត្រូវសួរអ្នកគ្រប់គ្រងអំពី [ការកំណត់ GitHub App](#github-app-setup) ដែលអនុញ្ញាត។
4. រត់ workflow ម្ដងទៀតដោយដោះសោ **Preview only**។ វា preview, បកប្រែ, ដំណើរការ `co-op-review --readme-only`, និងបង្កើត ឬបន្ទាន់សម័យ PR ប៉ុណ្ណោះបន្ទាប់ពីការបកប្រែ និងការវិភាគជោគជ័យ។ សេចក្តីសង្ខេប workflow ចែកចាយតំណភ្ជាប់ទៅ PR។
5. ពិនិត្យពាក្យ និងការផ្លាស់ប្តូរឯកសារ ក្នុង PR រួចរួមបញ្ចូលនៅពេលដែលរួមបញ្ចូល។ Workflow មិនរួមបញ្ចូលដោយស្វ័យប្រវត្តិទេ។

PR នោះមានតែ `translations/<language>/README.md` និងឯកសារមេតាភាសា។ README ដើមនៅស្ថានភាពដើម មិនផ្លាស់ប្ដូរ និងតំណទៅឯកសារផ្សេងទៀតនៅតែបង្ហាញឱ្យឃើញឯកសារដើម។ សាររបស់ PR បញ្ជីឯកសារដែលបានផ្លាស់ប្ដូរ និងលទ្ធផលពិនិត្យរចនាសម្ព័ន្ធ។ ប្រសិនបើការបកប្រែ ឬការពិនិត្យបរាជ័យ សូមពិនិត្យសេចក្តីសង្ខេប workflow និងបណ្ណាល័យជំហានដែលខូច; មិនមាន PR ត្រូវបានបង្កើត។ ប្រសិនបើមិនមានការផ្លាស់ប្តូរ មិនចាំបាច់មាន PR ថ្មីទេ។

**Organization and CI note:** GitHub App ជាជម្រើសមិនមែនជាការទាមទារ​សម្រាប់កម្មសិទ្ធិអង្គការ។ ជាមួយ `GITHUB_TOKEN`, workflow ដែលបង្កើត pull-request សម្រាប់បើក ទាន់សម័យ ឬបើកឡើងវិញ PR ត្រូវការអ្នកប្រើដែលមានសិទ្ធិ write ដើម្បីជ្រើស **Approve workflows to run**។ Push workflows មិនត្រូវបានចាប់ផ្តើមដោយ token នេះទេ។ សម្រាប់ CI downstream ដែលមិនត្រូវការអ្នកដឹកនាំ សូមមើល [ការកំណត់ GitHub App](#github-app-setup) និង [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) របស់ GitHub។

## លក្ខខ័ណ្ឌមុន

មុននឹងបង្កើត workflow សូមកំណត់ secrets សេវា AI ដែលការបកប្រែរបស់អ្នកត្រូវការប្រើ។

ការបកប្រែអត្ថបទត្រូវការអ្នកផ្ដល់ម៉ូដែលភាសា​មួយ៖

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

ការបកប្រែរូបភាពនិងទៀតទាមទារ Azure AI Vision៖

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

មើល [Configuration](configuration.md) និង [ការកំណត់ Azure AI](azure-ai-setup.md) សម្រាប់ព័ត៌មានលម្អិតអំពីការកំណត់ក្នុងកាស៊ីយ៉ា។

## ការកំណត់ស្តង់ដារ

បន្ទាប់ពីសាកល្បង workflow README ជាមួយ ដាក់ការកំណត់នេះដើម្បីបកប្រែឯកសារ Markdown ក្នុង repository ទៅជាច្រើនភាសា។ វារត់ការពិនិត្យ Markdown មុនពេលបើក PR និងមិនទាមទារ Azure AI Vision។

### ជំហានទី 1: បន្ថែម Repository Secrets

ក្នុង repository គោលដៅរបស់អ្នក បើក **Settings** > **Secrets and variables** > **Actions** បន្ទាប់មកបន្ថែម provider secrets ដែល workflow របស់អ្នកនឹងប្រើ។

![ជ្រើសរើស Actions secrets](../../assets/github-actions/select-setting-action.png)

### ជំហានទី 2: បើកសិទ្ធិ Workflow

បើក **Settings** > **Actions** > **General**។

នៅក្រោម **Workflow permissions**:

1. បើក **អនុញ្ញាតឲ្យ GitHub Actions បង្កើត និងអនុម័ត pull requests**។
2. រក្សាទុកការកំណត់។

តំណការងារខាងក្រោមស្នើសុំ `contents: write` និង `pull-requests: write` ឲ្យច្បាស់។ រក្សាសិទ្ធិលំនាំដើមរបស់ repository សម្រាប់ workflow មិនឲ្យផ្លាស់ប្តូរ។ ប្រសិនបើគោលនយោបាយអង្គការឆ្នេរការបង្កើត PR សូមពិគ្រោះជាមួយអ្នកគ្រប់គ្រងអំពី [ការកំណត់ GitHub App](#github-app-setup)។

### ជំហានទី 3: បន្ថែម Workflow

បង្កើត `.github/workflows/co-op-translator.yml`:

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

ប្រែ `TARGET_LANGUAGES` ទៅជាភាសាដែលគម្រោងរបស់អ្នកត្រូវការ។ ការពិនិត្យប្រើ Python API ដើម្បីពិនិត្យ Markdown តែប៉ុណ្ណោះ ដែលដំណើរការផ្គូរផ្គងនឹងជំហានបកប្រែ។ កំហុសបកប្រែ ឬការពិនិត្យនឹងឈប់ job មុនពេលបង្កើត PR។ Workflow មិនរួម PR ដោយស្វ័យប្រវត្តិ។ សម្រាប់ repository ធំៗ បន្ថែម filter `paths:` ក្រោម `on.push` ដើម្បីឲ្យ workflow រត់តែកាលណាឯកសារឯកសារការបណ្តុះបណ្តាលបិទ។

### ជម្រើស: notebooks និងរូបភាព

សម្រាប់ notebooks, បន្ថែម `-nb` ទៅពាក្យបញ្ជាបកប្រែ និងកំណត់ `notebook=True` ក្នុងជំហានពិនិត្យ។ សម្រាប់អត្ថបទក្នុងរូបភាព កំណត់ពីរ secrets [Azure AI Vision](#prerequisites), ផ្តល់ពួកវាក្នុង `env` របស់ជំហានបកប្រែ, បន្ថែម `-img` ទៅពាក្យបញ្ជា, និងបន្ថែម `translated_images/` ទៅ `add-paths` របស់ជំហាន PR។ ពិនិត្យរូបភាពដែលបានបកប្រែដោយភាពខ្មស; ការពិនិត្យដែលទាក់ស្ម័គ្រនេះមិនធានាសុពលភាពអត្ថបទរូបភាព ឬភាពត្រឹមត្រូវភាសាបានទេ។

## ការកំណត់ GitHub App

ប្រើ GitHub App ដែលបានអនុម័តនៅពេលអង្គការរបស់អ្នកទាមទារអត្តសញ្ញាណ App ឬនៅពេល PR ត្រូវការបញ្ចេញ downstream CI ដោយមិនខ្វះជំហានអនុម័ត `GITHUB_TOKEN`។ App មិនរំលោភគោលនយោបាយអង្គការទេ; អ្នកគ្រប់គ្រងនៅតែគ្រប់គ្រងការដំឡើង និងសិទ្ធិរបស់វា។

### ជំហានទី 1: បង្កើតឬដំឡើង GitHub App

ប្រើ App ដែលមានរួចដែលអង្គការ​ផ្ដល់ឲ្យ ប្រសិនបើមាន ឬបង្កើតមួយដែលមានសិទ្ធិអាន/សរសេរ ទៅ **Contents** និង **Pull requests**។ ដំឡើងវាទៅលើ repository គោលដៅជាមួយការអនុម័តដែលត្រូវការពីអង្គការ។

កត់ចំណាំ:

- App ID
- Private key contents

រក្សាទុកពួកវាជា repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### ជំហានទី 2: បង្កើត App Token

បន្ថែមជំហាននេះភ្លាមៗ មុនជំហាន pull request មានស្រាប់។ សម្រាប់ទំរង់ README ប្រើលក្ខខណ្ឌជោគជ័យដូចគ្នា ដើម្បីឲ្យ preview និងការបកប្រែបរាជ័យ មិនទាមទារការបង្កើត App token៖

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

បន្ទាប់មកផ្លាស់ប្តូរតែ input `token` របស់ជំហាន pull request មានស្រាប់ទៅ `${{ steps.generate_token.outputs.token }}`។ រក្សាលក្ខខណ្ឌជោគជ័យ សាខា សាររបស់ PR និង `add-paths` ដូចដើម។ Token ត្រូវបានកំណត់ប្រហែលទៅ repository បច្ចុប្បន្នដោយលំនាំដើម។ នៅពេលកែច្នៃការកំណត់ស្តង់ដា ជំនួសទម្រង់ README ទុកចោល `if` ខាងលើ: វិធីសាស្ត្រនោះប្រើលក្ខខណ្ឌជោគជ័យលំនាំដើម ដូច្នេះ ការបង្កើត token និងការបង្កើត PR ទៅដំណើរការ បន្ទាប់ពីការបកប្រែ និងការពិនិត្យជោគជ័យ។

មើល [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) ផ្លូវការសម្រាប់ការដំឡើង និងសិទ្ធិ token។

## កំណត់សមត្ថភាព Runner

GitHub-hosted runners មានធីមរយៈពេលធ្វើការឧប្បបរមា។ repository ធំៗ ឬភាសាគោលដៅច្រើនអាចលើសកំណត់នោះ។

សម្រាប់ការងារបកប្រែទំហំធំ:

- បកប្រែភាសារតិចជាងក្នុងមួយដំណើរការ។
- ប្រើ ទង់ខ្លួនខ្លះៗ ដូចជា `-md`, `-nb`, ឬ `-img`។
- ប្រើ self-hosted runner នៅពេលដែលទំហំ repository ឬពេលយឺតរបស់ម៉ូដែលធ្វើឲ្យ hosted runners មិនទាន់ទុកចិត្តបាន។

## ការពិនិត្យក្នុង CI

ប្រើ `co-op-review` នៅពេលដែល pull request គួរតែផ្ទៀងផ្ទាត់ការបកប្រែដែលបានផលិត ដោយមិនហៅអ្នកផ្ដល់ LLM ឬ Vision។

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` គឺជា ពាក្យបញ្ជា​ពិនិត្យប្រកបដោយកំណត់ beta។ ការត្រួតពិនិត្យ និង schema លទ្ធផលរបស់វាអាចអភិវឌ្ឍ ប៉ុន្តែវាត្រូវបានរចនាឡើងឲ្យមានសុវត្ថិភាពសម្រាប់ CI ព្រោះវាមិនសរសេ​ឯកសារ ឬហៅអ្នកផ្ដល់ម៉ូដែលទេ។