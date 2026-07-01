# Configuration

Co-op Translator کو ایک زبان ماڈل فراہم کنندہ درکار ہے۔ امیج ترجمہ کے لیے اضافی طور پر Azure AI Vision ضروری ہے۔

Configuration ماحول کے متغیرات سے پڑھی جاتی ہے۔ مقامی پروجیکٹس کے لیے، انہیں پروجیکٹ روٹ میں `.env` فائل میں رکھیں۔

Azure وسائل کی ترتیب کے لیے، ملاحظہ کریں [Azure AI Setup](azure-ai-setup.md).

## Local runtime setup

CLI کو مقامی طور پر چلانے سے پہلے ایک virtual environment استعمال کریں۔ Co-op Translator Python 3.10 سے 3.12 تک کی تائید کرتا ہے۔

عام CLI استعمال کے لیے، شائع شدہ پیکیج کو ویچوئل انوائرنمنٹ کے اندر انسٹال کریں:

=== "ونڈوز"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / لینکس"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Repository کی development کے لیے، اس کے بجائے پروجیکٹ روٹ سے dependencies انسٹال کریں:

```bash
poetry install
poetry run translate --help
```

CLI دستیاب ہونے کے بعد، `.env` میں ایک زبان ماڈل فراہم کنندہ ترتیب دیں۔

## Provider selection

یہ ٹول فراہم کنندگان کو اس ترتیب میں خود کار طریقے سے پتہ لگاتا ہے:

1. Azure OpenAI
2. OpenAI

اگر کوئی بھی فراہم کنندہ تشکیل شدہ نہیں ہے تو `translate`, `evaluate`, `migrate-links`, اور `run_translation` ترتیب چیک کے دوران ناکام ہو جائیں گے۔ `co-op-review` اور `run_review` ایک طے شدہ مینٹیننس چیک ہیں اور انہیں فراہم کنندہ کی اسناد کی ضرورت نہیں ہوتی۔

## Azure OpenAI

جب آپ کا ماڈل Azure AI Foundry یا Azure OpenAI Service میں تعینات ہو تو Azure OpenAI استعمال کریں۔

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

کنیکٹوٹی چیک ترجمہ شروع ہونے سے پہلے endpoint، API key، API version، اور deployment name استعمال کرتا ہے۔

## OpenAI

جب OpenAI API کو براہِ راست کال کیا جاتا ہے تو OpenAI استعمال کریں۔

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # اختیاری
OPENAI_BASE_URL="..."        # اختیاری
```

`OPENAI_CHAT_MODEL_ID` ضروری ہے کیونکہ translator کو API کالز کے لیے واضح chat ماڈل درکار ہوتا ہے۔

## Azure AI Vision

امیج ترجمہ کے لیے Azure AI Vision ضروری ہے تاکہ ٹول تصاویر سے متن نکال سکے اور پھر اس کا ترجمہ کرے۔

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

اگر امیج ترجمہ `-img`, `images=True`, یا کوئی content-type فلٹر نہ ہونے کے ساتھ منتخب کیا جائے تو ٹول ترجمہ شروع ہونے سے پہلے Vision کنفیگریشن کی توثیق کرتا ہے۔

## Multiple credential sets

کنفیگریشن لیئر ایک ہی انڈیکس کے ساتھ ویری ایبلز کو suffix کر کے متعدد کریڈینشل سیٹس کی حمایت کرتی ہے:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

ہر سیٹ مکمل ہونی چاہیے۔ ہیلتھ چیک ایک کام کرنے والا سیٹ منتخب کرتا ہے اس سے پہلے کہ ترجمہ آگے بڑھے۔

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | ہاں | نہیں | صرف Markdown کا ترجمہ کرتا ہے۔ |
| `translate -nb` | ہاں | نہیں | صرف notebooks کا ترجمہ کرتا ہے۔ |
| `translate -img` | ہاں | ہاں | صرف تصاویر کا ترجمہ کرتا ہے۔ |
| `translate` with no type flags | ہاں | ہاں | ڈیفالٹ موڈ میں Markdown، notebooks، اور تصاویر شامل ہیں۔ |
| `evaluate` | ہاں | نہیں | LLM evaluation استعمال کرتا ہے جب تک کہ `--fast` منتخب نہ ہو۔ |
| `migrate-links` | ہاں | نہیں | لنک مائگریشن کرتا ہے، مگر پھر بھی مشترکہ کنفیگریشن چیکس چلتا ہے۔ |
| `co-op-review` | نہیں | نہیں | deterministic translation structure، freshness، Markdown، notebook، اور local link چیکس چلتا ہے۔ |
| `run_translation(markdown=True)` | ہاں | نہیں | پروگراماتی Markdown ترجمہ۔ |
| `run_translation(images=True)` | ہاں | ہاں | پروگراماتی امیج ترجمہ۔ |
| `run_review(...)` | نہیں | نہیں | پروگراماتی deterministic ریویو۔ |

## Output directories

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ان ڈائریکٹریز کو `translations_dir` اور `image_dir` کے ساتھ اوور رائڈ کر سکتا ہے۔