<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T02:25:08+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "ur"
}
-->
# کو-آپ ٹرانسلیٹر گِٹ ہب ایکشن کا استعمال (ادارے کے لیے رہنمائی)

**ہدف سامعین:** یہ رہنمائی **مائیکروسافٹ کے اندرونی صارفین** یا **ان ٹیموں** کے لیے ہے جن کے پاس پہلے سے بنے ہوئے کو-آپ ٹرانسلیٹر گِٹ ہب ایپ کے لیے ضروری اسناد تک رسائی ہے یا وہ اپنی مرضی کی گِٹ ہب ایپ بنا سکتے ہیں۔

اپنے ریپوزٹری کی ڈاکیومنٹیشن کا ترجمہ خودکار طریقے سے کروائیں کو-آپ ٹرانسلیٹر گِٹ ہب ایکشن کے ذریعے۔ یہ رہنمائی آپ کو ایکشن سیٹ اپ کرنے کے مراحل بتاتی ہے تاکہ جب بھی آپ کے سورس مارک ڈاؤن فائلز یا امیجز میں تبدیلی ہو، خودکار طور پر ترجمہ شدہ اپڈیٹس کے ساتھ پل ریکویسٹ بن جائے۔

> [!IMPORTANT]
> 
> **صحیح رہنمائی کا انتخاب:**
>
> اس رہنمائی میں **گِٹ ہب ایپ آئی ڈی اور پرائیویٹ کی** کے ذریعے سیٹ اپ کی تفصیل ہے۔ آپ کو عموماً یہ "ادارے کی رہنمائی" تب چاہیے جب: **`GITHUB_TOKEN` کی اجازتیں محدود ہوں:** آپ کی تنظیم یا ریپوزٹری کی سیٹنگز ڈیفالٹ `GITHUB_TOKEN` کو دی جانے والی اجازتوں کو محدود کرتی ہیں۔ خاص طور پر اگر `GITHUB_TOKEN` کو ضروری `write` اجازتیں (جیسے `contents: write` یا `pull-requests: write`) نہیں ملتیں، تو [پبلک سیٹ اپ گائیڈ](./github-actions-guide-public.md) میں دیا گیا ورک فلو ناکام ہو جائے گا۔ ایک مخصوص گِٹ ہب ایپ کے ذریعے واضح اجازتوں کے ساتھ یہ مسئلہ حل ہو جاتا ہے۔
>
> **اگر اوپر والی شرط آپ پر لاگو نہیں ہوتی:**
>
> اگر آپ کے ریپوزٹری میں ڈیفالٹ `GITHUB_TOKEN` کے پاس کافی اجازتیں ہیں (یعنی آپ کو ادارے کی طرف سے کوئی رکاوٹ نہیں)، تو براہ کرم **[پبلک سیٹ اپ گائیڈ (GITHUB_TOKEN کے ساتھ)](./github-actions-guide-public.md)** استعمال کریں۔ اس میں ایپ آئی ڈی یا پرائیویٹ کی کی ضرورت نہیں، صرف `GITHUB_TOKEN` اور ریپوزٹری کی اجازتیں کافی ہیں۔

## پیشگی شرائط

گِٹ ہب ایکشن کنفیگر کرنے سے پہلے، یہ یقینی بنائیں کہ آپ کے پاس ضروری AI سروس کی اسناد موجود ہیں۔

**1. لازمی: AI لینگویج ماڈل کی اسناد**
آپ کو کم از کم ایک سپورٹڈ لینگویج ماڈل کے لیے اسناد درکار ہیں:

- **Azure OpenAI**: اینڈ پوائنٹ، API کی، ماڈل/ڈیپلائمنٹ نیمز، API ورژن درکار ہیں۔
- **OpenAI**: API کی، (اختیاری: آرگ آئی ڈی، بیس یو آر ایل، ماڈل آئی ڈی) درکار ہیں۔
- مزید تفصیل کے لیے دیکھیں [سپورٹڈ ماڈلز اور سروسز](../../../../README.md)۔
- سیٹ اپ گائیڈ: [Azure OpenAI سیٹ اپ کریں](../set-up-resources/set-up-azure-openai.md)۔

**2. اختیاری: کمپیوٹر وژن کی اسناد (امیج ترجمہ کے لیے)**

- صرف تب درکار ہیں جب آپ کو امیجز میں موجود ٹیکسٹ کا ترجمہ کرنا ہو۔
- **Azure Computer Vision**: اینڈ پوائنٹ اور سبسکرپشن کی درکار ہے۔
- اگر فراہم نہ کی جائیں تو ایکشن [صرف مارک ڈاؤن موڈ](../markdown-only-mode.md) پر چلا جائے گا۔
- سیٹ اپ گائیڈ: [Azure Computer Vision سیٹ اپ کریں](../set-up-resources/set-up-azure-computer-vision.md)۔

## سیٹ اپ اور کنفیگریشن

اپنے ریپوزٹری میں کو-آپ ٹرانسلیٹر گِٹ ہب ایکشن کنفیگر کرنے کے لیے یہ مراحل فالو کریں:

### مرحلہ 1: گِٹ ہب ایپ آتھنٹیکیشن انسٹال اور کنفیگر کریں

ورک فلو آپ کی طرف سے ریپوزٹری کے ساتھ محفوظ طریقے سے انٹریکٹ کرنے کے لیے گِٹ ہب ایپ آتھنٹیکیشن استعمال کرتا ہے (مثلاً پل ریکویسٹ بنانا)۔ ایک آپشن منتخب کریں:

#### **آپشن A: پہلے سے بنی ہوئی کو-آپ ٹرانسلیٹر گِٹ ہب ایپ انسٹال کریں (صرف مائیکروسافٹ کے اندرونی استعمال کے لیے)**

1. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) پیج پر جائیں۔

1. **Install** منتخب کریں اور وہ اکاؤنٹ یا آرگنائزیشن منتخب کریں جہاں آپ کی مطلوبہ ریپوزٹری ہے۔

    ![ایپ انسٹال کریں](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ur.png)

1. **Only select repositories** منتخب کریں اور اپنی مطلوبہ ریپوزٹری (مثلاً `PhiCookBook`) منتخب کریں۔ **Install** پر کلک کریں۔ آپ سے آتھنٹیکیشن مانگی جا سکتی ہے۔

    ![انسٹال آتھرائز کریں](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ur.png)

1. **ایپ کی اسناد حاصل کریں (اندرونی پراسیس درکار):** ورک فلو کو ایپ کے طور پر آتھنٹیکیٹ کرنے کے لیے آپ کو کو-آپ ٹرانسلیٹر ٹیم سے دو چیزیں درکار ہوں گی:
  - **App ID:** کو-آپ ٹرانسلیٹر ایپ کا منفرد شناختی نمبر۔ App ID ہے: `1164076`۔
  - **Private Key:** آپ کو `.pem` پرائیویٹ کی فائل کا **پورا مواد** مینٹینر سے حاصل کرنا ہوگا۔ **اس کی کو پاس ورڈ کی طرح حفاظت کریں۔**

1. مرحلہ 2 پر جائیں۔

#### **آپشن B: اپنی مرضی کی گِٹ ہب ایپ استعمال کریں**

- اگر آپ چاہیں تو اپنی مرضی کی گِٹ ہب ایپ بنا اور کنفیگر کر سکتے ہیں۔ اس کو Contents اور Pull requests پر Read & write ایکسیس ہونی چاہیے۔ آپ کو اس کی App ID اور پرائیویٹ کی درکار ہوگی۔

### مرحلہ 2: ریپوزٹری سیکرٹس کنفیگر کریں

آپ کو گِٹ ہب ایپ کی اسناد اور AI سروس کی اسناد کو اپنی ریپوزٹری سیٹنگز میں انکرپٹڈ سیکرٹس کے طور پر شامل کرنا ہوگا۔

1. اپنی مطلوبہ گِٹ ہب ریپوزٹری (مثلاً `PhiCookBook`) پر جائیں۔

1. **Settings** > **Secrets and variables** > **Actions** پر جائیں۔

1. **Repository secrets** کے تحت، نیچے دیے گئے ہر سیکرٹ کے لیے **New repository secret** پر کلک کریں۔

   ![سیٹنگ ایکشن منتخب کریں](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ur.png)

**لازمی سیکرٹس (گِٹ ہب ایپ آتھنٹیکیشن کے لیے):**

| سیکرٹ کا نام         | وضاحت                                         | ویلیو سورس                                      |
| :------------------- | :-------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | گِٹ ہب ایپ کا App ID (مرحلہ 1 سے)              | GitHub App Settings                             |
| `GH_APP_PRIVATE_KEY` | ڈاؤن لوڈ کی گئی `.pem` فائل کا **پورا مواد**   | `.pem` فائل (مرحلہ 1 سے)                        |

**AI سروس سیکرٹس (اپنی پیشگی شرائط کے مطابق جتنے بھی لاگو ہوں شامل کریں):**

| سیکرٹ کا نام                        | وضاحت                                    | ویلیو سورس                      |
| :---------------------------------- | :---------------------------------------- | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) کی کی   | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) کا اینڈ پوائنٹ | Azure AI Foundry           |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI سروس کی کی                   | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI سروس کا اینڈ پوائنٹ          | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`           | آپ کے Azure OpenAI ماڈل کا نام            | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | آپ کے Azure OpenAI ڈیپلائمنٹ کا نام       | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI کے لیے API ورژن              | Azure AI Foundry                |
| `OPENAI_API_KEY`                    | OpenAI کے لیے API کی                      | OpenAI Platform                 |
| `OPENAI_ORG_ID`                     | OpenAI آرگنائزیشن آئی ڈی                  | OpenAI Platform                 |
| `OPENAI_CHAT_MODEL_ID`              | مخصوص OpenAI ماڈل آئی ڈی                  | OpenAI Platform                 |
| `OPENAI_BASE_URL`                   | کسٹم OpenAI API بیس یو آر ایل              | OpenAI Platform                 |

![انوائرمنٹ ویری ایبل کا نام درج کریں](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ur.png)

### مرحلہ 3: ورک فلو فائل بنائیں

آخر میں، YAML فائل بنائیں جو خودکار ورک فلو کو ڈیفائن کرے۔

1. اپنی ریپوزٹری کے روٹ فولڈر میں `.github/workflows/` ڈائریکٹری بنائیں (اگر پہلے سے موجود نہیں)۔

1. `.github/workflows/` کے اندر `co-op-translator.yml` نامی فائل بنائیں۔

1. نیچے دیا گیا مواد co-op-translator.yml میں پیسٹ کریں۔

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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
  - **[!IMPORTANT] ہدف زبانیں:** `Run Co-op Translator` مرحلے میں، آپ کو لازمی طور پر `translate -l "..." -y` کمانڈ میں زبانوں کے کوڈز کی فہرست اپنی پروجیکٹ کی ضرورت کے مطابق دیکھنا اور تبدیل کرنا ہوگا۔ دی گئی مثال (`ar de es...`) کو اپنی ضرورت کے مطابق بدلیں۔
  - **ٹرگر (`on:`):** موجودہ ٹرگر ہر بار `main` پر پش ہونے پر ورک فلو چلاتا ہے۔ بڑے ریپوزٹریز کے لیے، `paths:` فلٹر (YAML میں کمنٹیڈ مثال دیکھیں) شامل کریں تاکہ ورک فلو صرف متعلقہ فائلز میں تبدیلی پر چلے اور رنر منٹس بچیں۔
  - **PR کی تفصیل:** اگر ضرورت ہو تو `commit-message`, `title`, `body`, `branch` نام اور `labels` کو `Create Pull Request` مرحلے میں اپنی مرضی کے مطابق بنائیں۔

## اسناد کا انتظام اور تجدید

- **سیکیورٹی:** حساس اسناد (API کیز، پرائیویٹ کیز) ہمیشہ گِٹ ہب ایکشنز سیکرٹس میں رکھیں۔ انہیں کبھی بھی ورک فلو فائل یا ریپوزٹری کوڈ میں ظاہر نہ کریں۔
- **[!IMPORTANT] کی کی تجدید (مائیکروسافٹ کے اندرونی صارفین):** یاد رکھیں کہ Azure OpenAI کی جو مائیکروسافٹ کے اندر استعمال ہوتی ہے اس کی تجدید پالیسی ہو سکتی ہے (مثلاً ہر 5 ماہ بعد)۔ اس لیے متعلقہ گِٹ ہب سیکرٹس (`AZURE_OPENAI_...` کیز) **ان کے ختم ہونے سے پہلے** اپڈیٹ کریں تاکہ ورک فلو ناکام نہ ہو۔

## ورک فلو چلانا

> [!WARNING]  
> **گِٹ ہب ہوسٹڈ رنر کا وقت محدود:**  
> گِٹ ہب ہوسٹڈ رنرز جیسے `ubuntu-latest` کی **زیادہ سے زیادہ ایکزیکیوشن ٹائم لمٹ 6 گھنٹے** ہے۔  
> اگر بڑے ڈاکیومنٹیشن ریپوزٹریز میں ترجمہ 6 گھنٹے سے زیادہ ہو جائے تو ورک فلو خودکار طور پر بند ہو جائے گا۔  
> اس سے بچنے کے لیے:  
> - **سیلف ہوسٹڈ رنر** استعمال کریں (کوئی وقت کی حد نہیں)  
> - ہر رن میں ہدف زبانوں کی تعداد کم کریں

جب `co-op-translator.yml` فائل آپ کی مین برانچ (یا `on:` ٹرگر میں دی گئی برانچ) میں مرج ہو جائے گی، ورک فلو خودکار طور پر ہر بار اس برانچ میں تبدیلی آنے پر (اور اگر `paths` فلٹر لگا ہو تو اس کے مطابق) چل جائے گا۔

اگر ترجمے بنیں یا اپڈیٹ ہوں تو ایکشن خودکار طور پر تبدیلیوں کے ساتھ پل ریکویسٹ بنا دے گا، جو آپ کے جائزے اور مرج کے لیے تیار ہو گا۔

---

**اعلانِ دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی بھرپور کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔