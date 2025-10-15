<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T04:15:08+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "my"
}
-->
# Co-op Translator GitHub Action ကို အသုံးပြုခြင်း (Public Setup)

**အသုံးပြုသူအတွက်:** ဒီလမ်းညွှန်ကို GitHub Actions ရဲ့ ပုံမှန်ခွင့်ပြုချက်နဲ့ အလုပ်လုပ်နိုင်တဲ့ public သို့မဟုတ် private repository များအတွက် ရည်ရွယ်ထားပါတယ်။ ဒီမှာ built-in `GITHUB_TOKEN` ကို အသုံးပြုပါတယ်။

သင့် repository ရဲ့ documentation ကို Co-op Translator GitHub Action နဲ့ အလိုအလျောက် ဘာသာပြန်ပေးနိုင်အောင် automate လုပ်ပါ။ ဒီလမ်းညွှန်မှာ source Markdown ဖိုင်များ သို့မဟုတ် image များ ပြောင်းလဲသွားတိုင်း updated translation တွေပါဝင်တဲ့ pull request ကို အလိုအလျောက် ဖန်တီးပေးအောင် action ကို စနစ်တကျ တပ်ဆင်နည်းကို လမ်းညွှန်ပေးထားပါတယ်။

> [!IMPORTANT]
>
> **မှန်ကန်တဲ့ လမ်းညွှန် ရွေးချယ်ခြင်း:**
>
> ဒီလမ်းညွှန်မှာ **ပုံမှန် `GITHUB_TOKEN` ကို အသုံးပြုတဲ့ setup** ကို အသေးစိတ် ရှင်းပြထားပါတယ်။ GitHub App Private Key တွေကို စီမံခန့်ခွဲဖို့ မလိုအပ်တဲ့အတွက် အသုံးပြုသူအများစုအတွက် အကြံပြုတဲ့ နည်းလမ်းပါ။
>

## လိုအပ်ချက်များ

GitHub Action ကို တပ်ဆင်မယ်ဆိုရင် AI service credentials တွေကို ကြိုတင်ပြင်ဆင်ထားဖို့ လိုအပ်ပါတယ်။

**၁။ မဖြစ်မနေလိုအပ်သော - AI Language Model Credentials**
Support လုပ်ထားတဲ့ Language Model တစ်ခုခုအတွက် credentials လိုအပ်ပါတယ် -

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Name, API Version လိုအပ်ပါတယ်။
- **OpenAI**: API Key လိုအပ်ပါတယ်။ (Optional: Org ID, Base URL, Model ID)
- အသေးစိတ်ကို [Supported Models and Services](../../../../README.md) မှာ ကြည့်နိုင်ပါတယ်။

**၂။ Optional - AI Vision Credentials (Image Translation အတွက်)**

- Image ထဲကစာသားကို ဘာသာပြန်ချင်ရင်သာ လိုအပ်ပါတယ်။
- **Azure AI Vision**: Endpoint နဲ့ Subscription Key လိုအပ်ပါတယ်။
- မထည့်ပေးရင် [Markdown-only mode](../markdown-only-mode.md) ကို default အနေနဲ့ အသုံးပြုပါလိမ့်မယ်။

## တပ်ဆင်ခြင်းနှင့် ပြင်ဆင်ခြင်း

ပုံမှန် `GITHUB_TOKEN` ကို အသုံးပြုပြီး Co-op Translator GitHub Action ကို repository မှာ configure လုပ်နည်းအဆင့်ဆင့် လုပ်ဆောင်ပါ။

### အဆင့် ၁ - Authentication ကို နားလည်ပါ (`GITHUB_TOKEN` အသုံးပြုခြင်း)

ဒီ workflow မှာ GitHub Actions မှာ built-in အနေနဲ့ ပါဝင်တဲ့ `GITHUB_TOKEN` ကို အသုံးပြုပါတယ်။ ဒီ token က **အဆင့် ၃** မှာ ပြင်ဆင်ထားတဲ့ settings အပေါ် မူတည်ပြီး repository နဲ့ ဆက်သွယ်ခွင့်ကို အလိုအလျောက် ပေးပါတယ်။

### အဆင့် ၂ - Repository Secrets ကို ပြင်ဆင်ပါ

သင့် **AI service credentials** တွေကို repository settings မှာ encrypted secrets အနေနဲ့ ထည့်ပေးရုံပါပဲ။

၁။  သွားပါ - သင့် GitHub repository ကို။
၂။  **Settings** > **Secrets and variables** > **Actions** ကို သွားပါ။
၃။  **Repository secrets** အောက်မှာ လိုအပ်တဲ့ AI service secret တစ်ခုစီအတွက် **New repository secret** ကို နှိပ်ပါ။

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.my.png) *(Image Reference: Secrets ထည့်ရာနေရာ)*

**လိုအပ်တဲ့ AI Service Secrets (သင့်လိုအပ်ချက်အပေါ် မူတည်ပြီး အားလုံးထည့်ပါ):**

| Secret Name                         | Description                               | Value Source                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) အတွက် Key  | သင့် Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) အတွက် Endpoint | သင့် Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI service အတွက် Key              | သင့် Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI service အတွက် Endpoint         | သင့် Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI Model Name                    | သင့် Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI Deployment Name               | သင့် Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI အတွက် API Version              | သင့် Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAI အတွက် API Key                        | သင့် OpenAI Platform              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Optional)         | သင့် OpenAI Platform              |
| `OPENAI_CHAT_MODEL_ID`              | OpenAI model ID (Optional)                | သင့် OpenAI Platform              |
| `OPENAI_BASE_URL`                   | OpenAI API Base URL (Optional)            | သင့် OpenAI Platform              |

### အဆင့် ၃ - Workflow Permissions ကို ပြင်ဆင်ပါ

GitHub Action မှာ `GITHUB_TOKEN` နဲ့ code ကို checkout လုပ်ခြင်း၊ pull request ဖန်တီးခြင်းတို့အတွက် ခွင့်ပြုချက်လိုအပ်ပါတယ်။

၁။  Repository မှာ **Settings** > **Actions** > **General** ကို သွားပါ။
၂။  **Workflow permissions** အပိုင်းကို အောက်သို့ scroll လုပ်ပါ။
၃။  **Read and write permissions** ကို ရွေးပါ။ ဒီအတွက် `GITHUB_TOKEN` မှာ `contents: write` နဲ့ `pull-requests: write` ခွင့်ပြုချက်တွေ ရရှိပါလိမ့်မယ်။
၄။  **Allow GitHub Actions to create and approve pull requests** ဆိုတဲ့ checkbox ကို **အမှန်ခြစ်ထားပါ**။
၅။  **Save** ကို နှိပ်ပါ။

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.my.png)

### အဆင့် ၄ - Workflow File ကို ဖန်တီးပါ

နောက်ဆုံးအနေနဲ့ `GITHUB_TOKEN` ကို အသုံးပြုတဲ့ automated workflow ကို YAML ဖိုင်အနေနဲ့ ဖန်တီးပါ။

၁။  Repository ရဲ့ root directory မှာ `.github/workflows/` directory မရှိသေးရင် ဖန်တီးပါ။
၂။  `.github/workflows/` ထဲမှာ `co-op-translator.yml` ဆိုတဲ့ ဖိုင်တစ်ခု ဖန်တီးပါ။
၃။  အောက်ပါအကြောင်းအရာကို `co-op-translator.yml` ထဲမှာ paste လုပ်ပါ။

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
၄။  **Workflow ကို Customize လုပ်ပါ:**
  - **[!IMPORTANT] Target Languages:** `Run Co-op Translator` အဆင့်မှာ `translate -l "..." -y` command ထဲက language code list ကို သင့် project အတွက် သင့်တော်အောင် ပြင်ဆင်ဖို့ **သေချာစစ်ဆေးပြီး ပြင်ပါ**။ ဥပမာ list (`ar de es...`) ကို သင့်လိုအပ်ချက်အတိုင်း ပြောင်းပါ။
  - **Trigger (`on:`):** အခု trigger က `main` branch ကို push လုပ်တိုင်း run ဖြစ်ပါတယ်။ Repository ကြီးများအတွက် `paths:` filter (YAML မှာ comment ထည့်ထားတဲ့ ဥပမာ) ကို အသုံးပြုပြီး source documentation ပြောင်းလဲတဲ့အခါသာ workflow run ဖြစ်အောင် ပြင်နိုင်ပါတယ်။ ဒါက runner minutes ကို သက်သာစေပါတယ်။
  - **PR Details:** `Create Pull Request` အဆင့်မှာ `commit-message`, `title`, `body`, `branch` name, `labels` စတာတွေကို လိုအပ်ရင် ပြင်နိုင်ပါတယ်။

## Workflow ကို အသုံးပြုခြင်း

> [!WARNING]  
> **GitHub-hosted Runner Time Limit:**  
> GitHub-hosted runner တွေ (`ubuntu-latest` စတဲ့) မှာ **အများဆုံး ၆ နာရီ** အလုပ်လုပ်ခွင့်ရှိပါတယ်။  
> Documentation repository ကြီးများအတွက် ဘာသာပြန်လုပ်ငန်း ၆ နာရီကျော်သွားရင် workflow ကို အလိုအလျောက် ရပ်တန့်သွားပါလိမ့်မယ်။  
> ဒီပြဿနာကို ရှောင်ရှားဖို့ -  
> - **self-hosted runner** ကို အသုံးပြုပါ (အချိန်ကန့်သတ်မရှိ)  
> - တစ်ခါ run တစ်ခါ target language အရေအတွက်ကို လျှော့ပါ

`co-op-translator.yml` ဖိုင်ကို main branch (သို့မဟုတ် `on:` trigger မှာ သတ်မှတ်ထားတဲ့ branch) ထဲ merge လုပ်ပြီးသွားရင်၊ အဲဒီ branch ကို changes push လုပ်တိုင်း (နဲ့ `paths` filter ကို configure လုပ်ထားရင် အဲဒီ filter ကို ကိုက်ညီတဲ့ changes ဖြစ်ရင်) workflow က အလိုအလျောက် run ဖြစ်သွားပါလိမ့်မယ်။

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသော ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။