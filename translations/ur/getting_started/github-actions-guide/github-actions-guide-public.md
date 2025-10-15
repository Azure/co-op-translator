<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T02:25:43+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ur"
}
-->
# کو-آپ ٹرانسلیٹر گیٹ ہب ایکشن کا استعمال (پبلک سیٹ اپ)

**ہدف صارفین:** یہ رہنمائی زیادہ تر پبلک یا پرائیویٹ ریپوزیٹریز کے صارفین کے لیے ہے جہاں اسٹینڈرڈ GitHub Actions کی اجازتیں کافی ہیں۔ اس میں بلٹ ان `GITHUB_TOKEN` استعمال ہوتا ہے۔

اپنے ریپوزیٹری کی ڈاکیومنٹیشن کو خودکار طریقے سے ترجمہ کریں کو-آپ ٹرانسلیٹر گیٹ ہب ایکشن کے ذریعے۔ یہ رہنمائی آپ کو ایکشن سیٹ اپ کرنے کے مراحل بتاتی ہے تاکہ جب بھی آپ کے سورس مارک ڈاؤن فائلز یا امیجز میں تبدیلی ہو، خودکار طور پر ترجمہ شدہ اپڈیٹس کے ساتھ پل ریکویسٹ بن جائے۔

> [!IMPORTANT]
>
> **درست رہنمائی کا انتخاب:**
>
> یہ رہنمائی **آسان سیٹ اپ کو بیان کرتی ہے جو اسٹینڈرڈ `GITHUB_TOKEN` استعمال کرتا ہے**۔ زیادہ تر صارفین کے لیے یہی طریقہ تجویز کیا جاتا ہے کیونکہ اس میں حساس GitHub App پرائیویٹ کیز کو سنبھالنے کی ضرورت نہیں۔
>

## لازمی شرائط

GitHub Action کو ترتیب دینے سے پہلے، یہ یقینی بنائیں کہ آپ کے پاس مطلوبہ AI سروس کی اسناد موجود ہیں۔

**1. لازمی: AI لینگویج ماڈل کی اسناد**
آپ کو کم از کم ایک سپورٹڈ لینگویج ماڈل کے لیے اسناد درکار ہیں:

- **Azure OpenAI**: اینڈ پوائنٹ، API Key، ماڈل/ڈیپلائمنٹ نام، API ورژن درکار ہیں۔
- **OpenAI**: API Key درکار ہے، (اختیاری: Org ID، Base URL، Model ID)۔
- مزید تفصیل کے لیے دیکھیں [Supported Models and Services](../../../../README.md)۔

**2. اختیاری: AI ویژن کی اسناد (امیج ترجمہ کے لیے)**

- صرف اس صورت میں درکار ہیں جب آپ امیجز کے اندر موجود متن کا ترجمہ کرنا چاہتے ہیں۔
- **Azure AI Vision**: اینڈ پوائنٹ اور سبسکرپشن کی درکار ہیں۔
- اگر فراہم نہ کی جائیں تو ایکشن [صرف مارک ڈاؤن موڈ](../markdown-only-mode.md) پر چلتا ہے۔

## سیٹ اپ اور ترتیب

اسٹینڈرڈ `GITHUB_TOKEN` کے ساتھ اپنے ریپوزیٹری میں کو-آپ ٹرانسلیٹر گیٹ ہب ایکشن کو ترتیب دینے کے لیے یہ مراحل فالو کریں۔

### مرحلہ 1: تصدیق کو سمجھیں (`GITHUB_TOKEN` کا استعمال)

یہ ورک فلو GitHub Actions کی طرف سے فراہم کردہ بلٹ ان `GITHUB_TOKEN` استعمال کرتا ہے۔ یہ ٹوکن خودکار طور پر ورک فلو کو آپ کے ریپوزیٹری کے ساتھ تعامل کی اجازت دیتا ہے، جیسا کہ **مرحلہ 3** میں ترتیب دیا گیا ہے۔

### مرحلہ 2: ریپوزیٹری سیکرٹس کی ترتیب

آپ کو صرف اپنی **AI سروس کی اسناد** کو ریپوزیٹری سیٹنگز میں انکرپٹڈ سیکرٹس کے طور پر شامل کرنا ہے۔

1.  اپنے مطلوبہ GitHub ریپوزیٹری پر جائیں۔
2.  **Settings** > **Secrets and variables** > **Actions** پر جائیں۔
3.  **Repository secrets** کے تحت، ہر مطلوبہ AI سروس سیکرٹ کے لیے **New repository secret** پر کلک کریں۔

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ur.png" alt="سیکرٹس شامل کرنے کی جگہ" /> *(تصویری حوالہ: سیکرٹس کہاں شامل کرنے ہیں)*

**مطلوبہ AI سروس سیکرٹس (اپنی لازمی شرائط کے مطابق تمام شامل کریں):**

| سیکرٹ کا نام                         | وضاحت                               | ویلیو سورس                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) کے لیے کی  | آپ کا Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) کے لیے اینڈ پوائنٹ | آپ کا Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI سروس کے لیے کی              | آپ کا Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI سروس کے لیے اینڈ پوائنٹ         | آپ کا Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | آپ کا Azure OpenAI ماڈل نام              | آپ کا Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | آپ کا Azure OpenAI ڈیپلائمنٹ نام         | آپ کا Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI کے لیے API ورژن              | آپ کا Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAI کے لیے API Key                        | آپ کا OpenAI Platform              |
| `OPENAI_ORG_ID`                     | OpenAI آرگنائزیشن آئی ڈی (اختیاری)         | آپ کا OpenAI Platform              |
| `OPENAI_CHAT_MODEL_ID`              | مخصوص OpenAI ماڈل آئی ڈی (اختیاری)       | آپ کا OpenAI Platform              |
| `OPENAI_BASE_URL`                   | کسٹم OpenAI API Base URL (اختیاری)     | آپ کا OpenAI Platform              |

### مرحلہ 3: ورک فلو کی اجازتیں ترتیب دیں

GitHub Action کو `GITHUB_TOKEN` کے ذریعے کوڈ چیک آؤٹ کرنے اور پل ریکویسٹ بنانے کی اجازت درکار ہے۔

1.  اپنے ریپوزیٹری میں **Settings** > **Actions** > **General** پر جائیں۔
2.  **Workflow permissions** سیکشن تک نیچے جائیں۔
3.  **Read and write permissions** منتخب کریں۔ اس سے `GITHUB_TOKEN` کو اس ورک فلو کے لیے `contents: write` اور `pull-requests: write` کی اجازت مل جائے گی۔
4.  **Allow GitHub Actions to create and approve pull requests** کے چیک باکس کو **چیک** کریں۔
5.  **Save** منتخب کریں۔

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.ur.png" alt="اجازتوں کی ترتیب" />

### مرحلہ 4: ورک فلو فائل بنائیں

آخر میں، YAML فائل بنائیں جو `GITHUB_TOKEN` کے ساتھ خودکار ورک فلو کو بیان کرتی ہے۔

1.  اپنے ریپوزیٹری کی روٹ ڈائریکٹری میں `.github/workflows/` ڈائریکٹری بنائیں اگر موجود نہیں۔
2.  `.github/workflows/` کے اندر `co-op-translator.yml` نامی فائل بنائیں۔
3.  درج ذیل مواد `co-op-translator.yml` میں پیسٹ کریں۔

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
4.  **ورک فلو کو اپنی مرضی کے مطابق بنائیں:**
  - **[!IMPORTANT] ہدف زبانیں:** `Run Co-op Translator` مرحلے میں، آپ کو لازمی طور پر `translate -l "..." -y` کمانڈ میں زبانوں کے کوڈز کی فہرست کو اپنے پروجیکٹ کی ضروریات کے مطابق دیکھنا اور تبدیل کرنا ہے۔ دی گئی مثال (`ar de es...`) کو تبدیل یا ایڈجسٹ کرنا ضروری ہے۔
  - **ٹرگر (`on:`):** موجودہ ٹرگر ہر بار `main` پر پش ہونے پر ورک فلو چلاتا ہے۔ بڑے ریپوزیٹریز کے لیے، `paths:` فلٹر شامل کرنے پر غور کریں (YAML میں تبصرہ شدہ مثال دیکھیں) تاکہ ورک فلو صرف متعلقہ فائلوں (مثلاً سورس ڈاکیومنٹیشن) میں تبدیلی پر چلے، اور رنر منٹس بچیں۔
  - **PR تفصیلات:** `Create Pull Request` مرحلے میں `commit-message`, `title`, `body`, `branch` نام، اور `labels` کو اپنی ضرورت کے مطابق تبدیل کریں۔

## ورک فلو چلانا

> [!WARNING]  
> **GitHub-hosted رنر وقت کی حد:**  
> GitHub-hosted رنرز جیسے `ubuntu-latest` کی **زیادہ سے زیادہ عمل درآمد کی حد 6 گھنٹے** ہے۔  
> اگر بڑے ڈاکیومنٹیشن ریپوزیٹریز میں ترجمہ کا عمل 6 گھنٹے سے زیادہ ہو جائے تو ورک فلو خودکار طور پر ختم ہو جائے گا۔  
> اس سے بچنے کے لیے:  
> - **سیلف-ہوسٹڈ رنر** استعمال کریں (کوئی وقت کی حد نہیں)  
> - ہر رن میں ہدف زبانوں کی تعداد کم کریں

جب `co-op-translator.yml` فائل آپ کی مین برانچ (یا `on:` ٹرگر میں دی گئی برانچ) میں مرج ہو جائے گی، ورک فلو خودکار طور پر ہر بار چلے گا جب اس برانچ میں تبدیلی پش کی جائے گی (اور اگر `paths` فلٹر ترتیب دیا گیا ہو تو اس کے مطابق)۔

---

**اعلانِ دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی مقامی زبان میں مستند ذریعہ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ہم ذمہ دار نہیں ہیں۔