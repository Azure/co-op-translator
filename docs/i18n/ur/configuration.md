# ترتیبات

Co-op Translator کو ایک language model فراہم کنندہ درکار ہے۔ تصاویر کے ترجمے کے لیے اضافی طور پر Azure AI Vision درکار ہے۔

تشکیلات ماحولیاتی متغیّرات (environment variables) سے پڑھی جاتی ہیں۔ مقامی پروجیکٹس کے لیے، انہیں پروجیکٹ کے روٹ میں `.env` فائل میں رکھیں۔

Azure وسائل کی ترتیب کے لیے دیکھیں [Azure AI Setup](azure-ai-setup.md)۔

## مقامی رن ٹائم سیٹ اپ

CLI کو مقامی طور پر چلانے سے پہلے ایک virtual environment استعمال کریں۔ Co-op Translator Python 3.11 تا 3.14 کی حمایت کرتا ہے۔

عام CLI استعمال کے لیے، شائع شدہ پیکیج کو virtual environment کے اندر انسٹال کریں:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### ریپوزٹری ڈویلپمنٹ

ریپوزٹری ڈویلپمنٹ کے لیے، اس کے بجائے پروجیکٹ روٹ سے dependencies انسٹال کریں:

```bash
poetry install
poetry run translate --help
```

جب CLI دستیاب ہو جائے، تو `.env` میں ایک language model فراہم کنندہ ترتیب دیں۔

## فراہم کنندہ کا انتخاب

ٹول خود بخود درج ذیل ترتیب میں فراہم کنندگان کا پتہ لگاتا ہے:

1. Azure OpenAI
2. OpenAI
3. Anthropic

ترجمہ کے لیے فراہم کنندہ کے اسناد درکار ہیں، سوائے پری ویوز کے جیسے `translate -l "ko" -md --dry-run`۔ `migrate-links`، `co-op-review`، اور `run_review` قطعی (deterministic) مرمتی عملیات ہیں اور انہیں فراہم کنندہ کی اسناد درکار نہیں ہوتیں۔

## ماڈل کلائنٹ بیک اینڈ

Co-op Translator 0.22.0 سے شروع کرتے ہوئے، Azure OpenAI، OpenAI، اور Anthropic بذریعہ ڈیفالٹ Microsoft Agent Framework استعمال کرتے ہیں۔ عام استعمال کے لیے کسی بیک اینڈ سیٹنگ کی ضرورت نہیں ہے۔

مطابقت کے لیے Semantic Kernel عارضی طور پر دستیاب رہتا ہے۔ اسے واضح طور پر منتخب کرنے کے لیے، درج کریں:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel استعمال کرنے پر deprecation وارننگ ظاہر ہوتی ہے۔ منصوبہ ہے کہ پیکیج Semantic Kernel کو 0.23.0 میں ایک اختیاری انحصار (optional dependency) میں منتقل کرے اور 0.24.0 میں انضمام کو ہٹا دے، بشرطیکہ مطابقت کے نتائج اور صارفین کی رائے۔ Anthropic کو `agent-framework` درکار ہے؛ Anthropic کے ساتھ واضح طور پر `semantic-kernel` منتخب کرنے پر کنفیگریشن خرابی ہوتی ہے۔ نامناسب اقدار provider-backed translator کی initialization کے دوران ناکام ہو جاتی ہیں بجائے اس کے کہ خاموشی سے fallback کر لیا جائے۔ رول آؤٹ کی پیروی کریں اور رکاوٹیں [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) میں رپورٹ کریں۔

## Azure OpenAI

جب آپ کا ماڈل Azure AI Foundry یا Azure OpenAI Service میں ڈپلائے کیا گیا ہو تو Azure OpenAI استعمال کریں۔

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

کنیکٹوٹی چیک ترجمہ شروع ہونے سے پہلے endpoint، API key، API version، اور deployment name استعمال کرتا ہے۔

## OpenAI

جب OpenAI API کو براہِ راست کال کر رہے ہوں تو OpenAI استعمال کریں۔

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

چونکہ translator کو API کالز کے لیے ایک واضح chat ماڈل درکار ہوتا ہے، `OPENAI_CHAT_MODEL_ID` ضروری ہے۔

ڈیفالٹ سیٹ اپ کے لیے `OPENAI_ORG_ID` اور `OPENAI_BASE_URL` کو غیر مرتب (unset) چھوڑ دیں۔ صرف اسی صورت میں organization ID شامل کریں جب آپ کے اکاؤنٹ کو ضرورت ہو، یا base URL اسی صورت میں جب آپ custom endpoint استعمال کر رہے ہوں۔ اختیاری ترتیبات کے لیے placeholder قدروں کو نقل نہ کریں۔

## Anthropic Claude

جب Claude API کو براہِ راست کال کر رہے ہوں تو Anthropic استعمال کریں۔ ایک [Anthropic API key](https://platform.claude.com/docs/en/get-started) بنائیں اور ایک معاون [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) منتخب کریں۔

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` اور `ANTHROPIC_MODEL` ضروری ہیں۔ آپ کو `CO_OP_TRANSLATOR_MODEL_CLIENT` سیٹ کرنے کی ضرورت نہیں ہے؛ Agent Framework بطور ڈیفالٹ بیک اینڈ ہے۔

`ANTHROPIC_BASE_URL` کو Anthropic API کے لیے غیر مرتب رکھیں۔ صرف اسی صورت میں سیٹ کریں جب custom endpoint استعمال کر رہے ہوں۔

`ANTHROPIC_MAX_TOKENS` کی ڈیفالٹ قدر `8192` ہے، جو Meitei Mayek جیسے token-dense اسکرپٹس کے لیے جگہ چھوڑتی ہے۔ اگر آپ کا ماڈل یا Anthropic-compatible endpoint اس سے کم آؤٹ پٹ کی حد مقرر کرتا ہے تو اسے کم کریں۔

## Azure AI Vision

تصاویر کا ترجمہ Azure AI Vision کا تقاضا کرتا ہے تاکہ ٹول کنفیگر کیے گئے language model کے ترجمے سے پہلے تصاویر سے متن نکال سکے۔ Anthropic نکالا گیا متن Azure OpenAI یا OpenAI کی طرح ترجمہ کر سکتا ہے۔

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

اگر تصویر کے ترجمے کا انتخاب `-img`، `images=True`، یا content-type فلٹر نہ ہونے کی صورت میں کیا گیا ہو تو ٹول ترجمہ شروع ہونے سے پہلے Vision کنفیگریشن کی توثیق کرتا ہے۔

## متعدد اسناد سیٹس

configuration لیئر ایک ہی انڈیکس بطور suffix متغیّرات میں لگا کر متعدد اسناد سیٹس کو سپورٹ کرتی ہے:

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

ہر سیٹ مکمل ہونا ضروری ہے۔ ہیل्थ چیک ترجمہ شروع ہونے سے پہلے ایک کام کرنے والا سیٹ منتخب کرتا ہے۔

OpenAI اور Anthropic ایک ہی suffix کنونشن کی حمایت کرتے ہیں۔ ہر credential set میں ہر متغیّر کو ایک ہی suffix پر رکھیں، بشمول اختیاری قدروں کے جیسے `OPENAI_BASE_URL_1` یا `ANTHROPIC_BASE_URL_1`۔

## کمانڈ کی ضروریات

| کمانڈ یا API | LLM درکار | Vision درکار | نوٹس |
| --- | --- | --- | --- |
| `translate -md` | ہاں | نہیں | صرف Markdown کا ترجمہ کرتا ہے۔ |
| `translate -nb` | ہاں | نہیں | صرف notebooks کا ترجمہ کرتا ہے۔ |
| `translate -img` | ہاں | ہاں | صرف تصاویر کا ترجمہ کرتا ہے۔ |
| `translate` with no type flags | ہاں | ہاں | ڈیفالٹ موڈ میں Markdown، notebooks، اور تصاویر شامل ہیں۔ |
| `evaluate` | ہاں | نہیں | LLM evaluation استعمال کرتا ہے جب تک `--fast` منتخب نہ کیا جائے۔ |
| `migrate-links` | نہیں | نہیں | provider کالز کے بغیر مقامی لنک مائیگریشن انجام دیتا ہے۔ |
| `co-op-review` | نہیں | نہیں | قطعی (deterministic) translation structure، freshness، Markdown، notebook، اور مقامی لنک چیکس چلاتا ہے۔ |
| `run_translation(markdown=True)` | ہاں | نہیں | پروگراماتی (programmatic) Markdown ترجمہ۔ |
| `run_translation(images=True)` | ہاں | ہاں | پروگراماتی تصویر کا ترجمہ۔ |
| `run_review(...)` | نہیں | نہیں | پروگراماتی قطعی (deterministic) جائزہ۔ |

## آؤٹ پٹ ڈائریکٹریز

متن کے ترجمے کا ڈیفالٹ آؤٹ پٹ:

```text
translations/<language-code>/<source-relative-path>
```

ترجمہ شدہ تصاویر کا ڈیفالٹ آؤٹ پٹ:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ان ڈائریکٹریوں کو `translations_dir` اور `image_dir` کے ساتھ اوور رائڈ (override) کر سکتا ہے۔