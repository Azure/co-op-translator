# GitHub Actions

GitHub Actions ကို repository မှ ပြောင်းလဲထားသော စာတမ်းများကို အလိုအလျောက် ဘာသာပြန်ပြီး ထုတ်လွှင့်အထွက်များနှင့်အတူ pull request ဖွင့်လိုသောအခါ အသုံးပြုပါ။

ပုံမှန် `GITHUB_TOKEN` အပြင်အဆင်ဖြင့် စတင်ပါ၊ အဖွဲ့အစည်း repository များတွင် မူဝါဒက ခွင့်ပြုလျှင်လည်း ထိန်းသိမ်းထားပါ။ သင့်အဖွဲ့အစည်းက App အထောက်အထားလိုအပ်ပါက သို့မဟုတ် အောက်ဆက် workflow များကို အလိုအလျောက် လည်ပတ်အောင် လိုအပ်ပါက [GitHub App Setup](#github-app-setup) ကို ကြည့်ပါ။

**Human edits:** ဤ workflow များသည် ပြောင်းလဲသော မူရင်းဖိုင်များကို အပြည့်အစုံ ပြန်လည်ဘာသာပြန်ပြီး ၎င်းတို့၏ ဘာသာပြန်ချက်များတွင် လူ့ဖျော်ဖြေမှုဖြင့် ပြင်ဆင်ထားသော စကားများကို အစားထိုးနိုင်သည်။ ပေါင်းစည်းခြင်းမပြုမီ PR တစ်ခုချင်းစီကို ပြန်လည်စိစစ်ပါ။ လက်ခံထားသော ပြင်ဆင်ချက်များကို Markdown block-level အဖြစ် ထိန်းသိမ်းလိုပါက [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ဖြင့် သီးခြား အမြင်ပေါင်းစည်းမှု လိုအပ်ပါသည်။

## သင်၏ ပထမ README ဘာသာပြန် PR

တစ်ခုသော root `README.md` နှင့် တစ်ခုသော သတ်မှတ်ဘာသာစကားဖြင့် စတင်ပါ။ ဤ workflow သည် Markdown ပင်သာ ဘာသာပြန်သည်၊ ထို့ကြောင့် Azure AI Vision လိုအပ်မှုမရှိပါ။

1. သင်ဘာသာပြန်လိုသော repository အတွင်း `.github/workflows/translate-readme.yml` သို့ [translate-readme.yml](../../assets/workflows/translate-readme.yml) ကို ကူးထည့်ပြီး အဲဒီ repository ၏ default branch တွင် commit လုပ်ပါ၊ ([view the template on GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml))။ အဆိုပါ template သည် `Azure/co-op-translator@main` မှ root Action ကို အသုံးပြုကာ CLI ကို အဲဒီ source ref မှ တပ်ဆင်ပါသည်။ ပြန်လည်ထပ်မံ ချမှတ်နိုင်သော runs အတွက် စစ်ဆေးထားသော commit ကို pin လုပ်ပါ။
2. **Actions > Translate README > Run workflow** ကို ဖွင့်ပြီး ဘာသာစကားရွေးပါ၊ **Preview only** ကို ကျန်ထားအောင် သတ်မှတ်ပါ။ preview ခြေလှမ်းတွင် token ခန့်မှန်းမှုကို ပြန်လည်စစ်ဆေးပါ။ Preview သည် model providers မများကို ဖိတ်ခေါ်ခြင်း၊ ဘာသာပြန်ချက်များရေးခြင်း သို့မဟုတ် PR ဖန်တီးခြင်း မပြုလုပ်ပါ။
3. [စာသားပေးသူ](#prerequisites) တစ်ခုအတွက် secrets များကို ထည့်ပြီး **Settings > Actions > General** အောက်ရှိ **GitHub Actions ကို pull request များ ဖန်တီး၍ အတည်ပြုခွင့် ပေးရန်** ကို ဖွင့်ပါ။ template သည် ၎င်း၏ job အတွက် `contents: write` နှင့် `pull-requests: write` ကို တောင်းဆိုထားသည်; workflow တစ်ခုချင်းစီအတွက် default permissions မပြောင်းရပါ။ အဖွဲ့အစည်း မူဝါဒက ဤ permissions သို့မဟုတ် ဤ setting ကို ပိတ်ထားလျှင် အုပ်ချုပ်ရေးမှူးထံတွင် အတည်ပြုထားသည့် [GitHub App](#github-app-setup) အကြောင်း မေးမြန်းပါ။
4. **Preview only** ကို အမှတ်မထားဘဲ workflow ကို ထပ်မံ လည်ပတ်ပါ။ ၎င်းသည် preview ပြုလုပ်ကာ ဘာသာပြန်ပြီး `co-op-review --readme-only` ကို run လုပ်ပြီး ဘာသာပြန်မှုနှင့် စစ်ဆေးမှု အောင်မြင်ပြီးနောက်မှသာ ဘာသာပြန် PR ကို ဖန်တီး သို့မဟုတ် အပ်ဒိတ် ပြုလုပ်မည်ဖြစ်သည်။ workflow summary သည် PR သို့လင့်ခ်ပေးပါသည်။
5. PR အတွင်း စကားစုနှင့် ဖိုင်ပြောင်းလဲမှုများကို ပြန်လည်သုံးသပ်ပြီး အဆင်ပြေပါက merge လုပ်ပါ။ workflow သည် အလိုအလျောက် merge မလုပ်ပါ။

PR တွင် `translations/<language>/README.md` နှင့် ၎င်း၏ ဘာသာစကား metadata ဖိုင်သာ ပါရှိသည်။ မူရင်း README သည် မပြောင်းလဲပါနှင့် အခြားစာရွက်စာတမ်းများသို့ လင့်ခ်များသည် မူရင်းစာရွက်စာတမ်းများကို ဆက်လက်ညွှန်ပြနေပါသည်။ PR body တွင် ပြောင်းလဲထားသော ဖိုင်များနှင့် ဖွဲ့စည်းမှု စစ်ဆေးမှု ရလဒ်များကို တွဲဖော်ပြထားသည်။ ဘာသာပြန်ခြင်း သို့မဟုတ် စစ်ဆေးမှု မအောင်မြင်ပါက workflow summary နှင့် မအောင်မြင်သော ချက် logs များကို စစ်ဆေးပါ; PR တစ်ခုအား မဖန်တီးပါ။ ပြောင်းလဲမှု မရှိပါက PR အသစ် မလိုအပ်ပါ။

**Organization and CI note:** GitHub App သည် ရွေးချယ်စရာသာဖြစ်ပြီး အဖွဲ့အစည်းပိုင်ဆိုင်မှုအတွက် အလိုမရှိပါ။ `GITHUB_TOKEN` ဖြင့် PR ဖွင့်ခြင်း၊ အပ်ဒိတ်ခြင်း သို့မဟုတ် ပြန်ဖွင့်ခြင်းနှင့်ဆိုင်သော pull-request workflows များအတွက် **Approve workflows to run** ကို ရွေးချယ်နိုင်သည့် write access ရှိသူ တစ်ဦး လိုအပ်သည်။ Push workflows များကို ဤ token ဖြင့် မေဆောင်ရွက်ပါ။ unattended downstream CI အတွက် [GitHub App Setup](#github-app-setup) နှင့် GitHub ၏ [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) ကို ကြည့်ပါ။

## အလိုအပ်ချက်များ

workflow ဖန်တီးမီ သင်၏ ဘာသာပြန် run အတွက် လိုအပ်သည့် AI service secrets များကို ပြင်ဆင်ပါ။

စာသားဘာသာပြန်ရန် တစ်ခုသော ဘာသာစကားမော်ဒယ် ပံ့ပိုးသူ တစ်ဦး လိုအပ်သည်။

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`၊ ရွေးချယ်နိုင်သည့် `OPENAI_ORG_ID` နှင့် `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`၊ ရွေးချယ်နိုင်သည့် `ANTHROPIC_BASE_URL`

ပုံဘာသာပြန်ခြင်းအတွက် ထပ်ဆင့်လိုအပ်သည်မှာ Azure AI Vision ဖြစ်သည် -

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

ဒေသဆိုင်ရာ သတ်မှတ်ချက်များအတွက် [ဆက်တင်များ](configuration.md) နှင့် [Azure AI သတ်မှတ်ခြင်း](azure-ai-setup.md) ကို ကြည့်ပါ။

## စံအစီအစဉ်

README workflow ကို စမ်းသပ်ပြီးနောက် ဤ စနစ်ကို အသုံးပြု၍ repository ၏ Markdown ဖိုင်များကို ဘာသာစကားအနည်းငယ် သို့မဟုတ် အများပြားသို့ ဘာသာပြန်နိုင်သည်။ PR ဖွင့်မီ Markdown စစ်ဆေးမှုကို အရင်ဆုံး ပြုလုပ်ပြီး Azure AI Vision မလိုအပ်ပါ။

### အဆင့် 1: Repository Secrets ထည့်ရန်

သင်၏ ထိန်းချုပ်လိုသော repository တွင် **Settings** > **Secrets and variables** > **Actions** ကို ဖွင့်ပြီး သင်၏ workflow မှအသုံးပြုမည့် provider secrets များကို ထည့်ပါ။

![Actions secrets ရွေးချယ်ခြင်း](../../assets/github-actions/select-setting-action.png)

### အဆင့် 2: Workflow ခွင့်ပြုချက်များ ဖွင့်ရန်

**Settings** > **Actions** > **General** ကို ဖွင့်ပါ။

**Workflow permissions** အောက်တွင်:

1. **GitHub Actions ကို pull request များ ဖန်တီး၍ အတည်ပြုခွင့် ပေးရန်** ကို ဖွင့်ပါ။
2. သတ်မှတ်ချက်ကို သိမ်းဆည်းပါ။

အောက်ပါ job သည် `contents: write` နှင့် `pull-requests: write` ကို ထူးထူးခြားခြား တောင်းဆိုထားသည်။ repository ၏ default workflow permissions များကို မပြောင်းလဲပါနဲ့။ အဖွဲ့အစည်း မူဝါဒက PR ဖန်တီးမှုကို ပိတ်ထားလျှင် အုပ်ချုပ်ရေးမှူးထံမှ အတည်ပြုထားသည့် [GitHub App](#github-app-setup) အကြောင်း မေးမြန်းပါ။

### အဆင့် 3: Workflow ထည့်ရန်

`.github/workflows/co-op-translator.yml` ကို ဖန်တီးပါ:

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

`TARGET_LANGUAGES` ကို သင့် project အတွက် လိုအပ်သည့် ဘာသာစကားများထံ ပြောင်းပါ။ စစ်ဆေးမှုတွင် Python API ကို အသုံးပြုပြီး Markdown ပင်သာ စစ်ဆေးမည် ဖြစ်၍ ဘာသာပြန်ခြင်းအဆင့်နှင့် ကိုက်ညီပါသည်။ ဘာသာပြန်ခြင်း သို့မဟုတ် စစ်ဆေးမှု အမှားရှိပါက PR ဖန်တီးမီ job ကို ရပ်လိမ့်မည်။ workflow သည် PR ကို အလိုအလျောက် merge မလုပ်ပါ။ repository များကြီးမားသော အမျိုးအစားများတွင် documentation ပြောင်းလဲမှုများဖြစ်နေသည့် အချိန်တွင်သာ workflow ပြေးအောင် `on.push` အောက်တွင် `paths:` filter ကို ထည့်ပါ။

### ရွေးချယ်နိုင်: notebook များနှင့် ပုံများ

Notebook များအတွက် ဘာသာပြန် command တွင် `-nb` ကို ထည့်ပြီး review အဆင့်တွင် `notebook=True` သတ်မှတ်ပါ။ ပုံအကြောင်းအရာများအတွက်တော့ [Azure AI Vision secrets](#prerequisites) နှစ်ခုကို ပြင်ဆင်ကာ ၎င်းတို့ကို translation အဆင့်၏ `env` မှတဆင့် ပေးပို့ပြီး command တွင် `-img` ကို ထည့်သွင်းကာ PR အဆင့်၏ `add-paths` တွင် `translated_images/` ကို ထည့်ပါ။ ဘာသာပြန်ပြီးပုံများကို မျက်မြင်ဖြင့် ပြန်လည်စစ်ဆေးပါ; deterministic review သည် ပုံစာသား သို့မဟုတ် ဘာသာရပ်ဗေဒ များ၏ တိကျမှုကို အတည်ပြုမည် မဟုတ်ပါ။

## GitHub App သတ်မှတ်ချက်

အဖွဲ့အစည်းက App အထောက်အထားကို လိုအပ်သည့်အခါ သို့မဟုတ် ထုတ်လွှင့်သော PR သည် `GITHUB_TOKEN` အတည်ပြုခြင်း အဆင့် မလိုအပ်ဘဲ downstream CI ကို ထိန်းချုပ်ရန် လိုအပ်သောအခါ အတည်ပြုထားသော GitHub App ကို အသုံးပြုပါ။ App သည် အဖွဲ့အစည်း မူဝါဒကို ကျော်လွှားစေမည် မဟုတ်ပါ; အုပ်ချုပ်ရေးမှူးများက တပ်ဆင်ခြင်းနှင့် ခွင့်ပြုချက်များကို ထိန်းချုပ်နေဆဲဖြစ်သည်။

### အဆင့် 1: GitHub App တစ်ခု ဖန်တီးရန် သို့မဟုတ် တပ်ဆင်ရန်

ရရှိနိုင်ပါက အဖွဲ့အစည်းမှ ပေးအပ်ထားသော App ကို အသုံးပြုပါ၊ မရှိပါက **Contents** နှင့် **Pull requests** များအတွက် ဖတ်/ရေး ခွင့်ရှိသော App အသစ်တစ်ခု ဖန်တီးပါ။ လိုအပ်သည့် အဖွဲ့အစည်း အတည်ပြုပြီး target repository တွင် တပ်ဆင်ပါ။

မှတ်သားပါ:

- App ID
- Private key contents

၎င်းတို့ကို repository secrets အဖြစ် သိမ်းဆည်းပါ။

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### အဆင့် 2: App Token ထုတ်ယူရန်

ဤ အဆင့်ကို လက်ရှိ pull request အဆင့် မရောက်ခင် ချက်ချင်း ထည့်ပါ။ README template အတွက် preview များနှင့် မအောင်မြင်သော ဘာသာပြန်ချက်များသည် App token မတောင်းရရန် အောင်မြင်မှု အခြေအနေနှင့် တူညီစွာ သတ်မှတ်ပါ။

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

ထို့နောက် ရှိပြီးသား pull request အဆင့်၏ `token` input ကို မျှတစွာ `${{ steps.generate_token.outputs.token }}` သို့ ပြောင်းပါ။ ၎င်း၏ success condition၊ branch၊ PR body နှင့် `add-paths` များကို မပြောင်းလဲပါနဲ့။ token သည် default အနေဖြင့် လက်ရှိ repository ကိုသာ scope ပြုထားသည်။ README template အစား standard setup ကို ကိုက်ညီစေလိုလျှင် အထက်ပါ `if` ကို ဖျက်ပစ်ပါ။ ထို workflow သည် default success condition ကို အသုံးပြုကာ token ဖန်တီးခြင်းနှင့် PR ဖန်တီးခြင်းကို ဘာသာပြန်ခြင်းနှင့် စစ်ဆေးမှု အောင်မြင်လျှင်သာ သွင်းဆောင်သည်။

စက်တင်နှင့် token ခွင့်များအတွက် တရားဝင် [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) ကို ကြည့်ပါ။

## Runner ကန့်သတ်ချက်များ

GitHub-hosted runners များတွင် job အချိန်ကန့်သတ်မှုရှိပါသည်။ repository များကြီးမားခြင်း သို့မဟုတ် သတ်မှတ်ဘာသာစကား အများအပြားရှိခြင်းကြောင့် ထိုကန့်သတ်မှုကို ကျော်လွန်နိုင်သည်။

ဘာသာပြန် အလုပ်များ ကြီးမားသောအခါ:

- တစ် run အတွင်း ဘာသာစကားများအား အနည်းငယ်သာ ဘာသာပြန်ပါ။
- `-md`, `-nb`, သို့မဟုတ် `-img` ကဲ့သို့ content flag များကို အသုံးပြုပါ။
- repository အရွယ်အစား သို့မဟုတ် မော်ဒယ် latency ကြောင့် hosted runners မယုံကြည်နိုင်လျှင် self-hosted runner များကို အသုံးပြုပါ။

## CI ထဲတွင် ပြန်လည်စစ်ဆေးခြင်း

generated translations များကို LLM သို့ Vision provider မခေါ်ဘဲ စစ်ဆေးရန် လိုပါက `co-op-review` ကို အသုံးပြုပါ။

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` သည် beta အဆင့်ရှိ deterministic review command ဖြစ်သည်။ ၎င်း၏ စစ်ဆေးချက်များနှင့် output schema များသည် တိုးပွားနိုင်သော်လည်း ဖိုင်များ မရေးဆွဲခြင်း သို့မဟုတ် model providers မခေါ်ခြင်းကြောင့် CI အတွက် ဘေးကင်းလုံခြုံစိတ်ချရ하도록 ဒီဇိုင်းဆွဲထားသည်။