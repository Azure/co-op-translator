<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:21:01+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ur"
}
-->
## پروجیکٹ کا جائزہ

کو-آپ ٹرانسلیٹر ایک پائتھون کمانڈ لائن ٹول اور GitHub Actions ورک فلو ہے جو مارک ڈاؤن فائلز، جیوپیٹر نوٹ بکس اور امیج ٹیکسٹ کو کئی زبانوں میں ترجمہ کرتا ہے۔ یہ آؤٹ پٹس کو زبان کے لحاظ سے الگ فولڈرز میں منظم کرتا ہے اور ترجمہ جات کو اصل مواد کے ساتھ ہم آہنگ رکھتا ہے۔ یہ پروجیکٹ ایک Poetry-مینجڈ لائبریری کے طور پر ترتیب دیا گیا ہے جس میں CLI انٹری پوائنٹس ہیں۔

### آرکیٹیکچر کا جائزہ

- CLI انٹری پوائنٹس (`translate`, `migrate-links`, `evaluate`) ایک متحد CLI کو کال کرتے ہیں جو ترجمہ، لنک مائیگریشن اور ایویلیوایشن کے فلو کو چلاتا ہے۔
- کنفیگریشن لوڈر `.env` کو پڑھتا ہے اور LLM پرووائیڈر (Azure OpenAI یا OpenAI) کو خودکار طور پر شناخت کرتا ہے، اور اگر ضرورت ہو تو امیج ٹیکسٹ نکالنے کے لیے ویژن پرووائیڈر (Azure AI Service) کو بھی۔
- ترجمہ کور مارک ڈاؤن اور نوٹ بکس کو ہینڈل کرتا ہے؛ ویژن پائپ لائن امیجز سے ٹیکسٹ نکالتی ہے جب `-img` استعمال ہو۔
- آؤٹ پٹس `translations/<lang>/` میں ٹیکسٹ کے لیے اور `translated_images/` میں امیجز کے لیے منظم ہوتے ہیں، اصل ساخت برقرار رہتی ہے۔

### اہم ٹیکنالوجیز اور فریم ورک

- پائتھون 3.10–3.12، پیکیجنگ کے لیے Poetry
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI، OpenAI
- ویژن: Azure AI Service (Computer Vision)
- HTTP اور ڈیٹا: `httpx`, `pydantic`
- امیجنگ: `pillow`, `opencv-python`, `matplotlib`
- ٹولنگ: `pytest`, `black`, `ruff`

## سیٹ اپ کمانڈز

### ضروریات

- پائتھون 3.10–3.12
- Azure سبسکرپشن (اختیاری، Azure AI سروسز کے لیے)
- LLM/Vision APIs کے لیے انٹرنیٹ رسائی (جیسے Azure OpenAI/OpenAI، Azure AI Vision)

### آپشن A: Poetry (تجویز کردہ)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### آپشن B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## اینڈ یوزر استعمال

### ڈاکر (شائع شدہ امیج)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

نوٹس:
- ڈیفالٹ انٹری پوائنٹ `translate` ہے۔ لنک مائیگریشن کے لیے `--entrypoint migrate-links` سے اووررائیڈ کریں۔
- گمنام پل کے لیے GHCR پیکیج کی ویزیبلٹی Public ہونی چاہیے۔

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### ماحول کی کنفیگریشن

ریپوزٹری روٹ پر `.env` فائل بنائیں اور اپنی منتخب کردہ لینگویج ماڈل اور (اختیاری) ویژن سروس کے لیے کریڈینشلز/اینڈ پوائنٹس فراہم کریں۔ پرووائیڈر کے لحاظ سے سیٹ اپ کے لیے `getting_started/set-up-azure-ai.md` دیکھیں۔

### ضروری ماحول کی ویریبلز

کم از کم ایک LLM پرووائیڈر کنفیگر ہونا چاہیے۔ امیج ترجمہ کے لیے Azure AI Service بھی کنفیگر ہونی چاہیے۔

- Azure OpenAI (ٹیکسٹ ترجمہ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (ٹیکسٹ ترجمہ متبادل):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (اختیاری)
  - `OPENAI_CHAT_MODEL_ID` (ضروری جب OpenAI پرووائیڈر استعمال ہو)
  - `OPENAI_BASE_URL` (اختیاری؛ ڈیفالٹ `https://api.openai.com/v1`)

- امیج ٹیکسٹ نکالنے کے لیے Azure AI Service (ضروری جب `-img` استعمال ہو):
  - `AZURE_AI_SERVICE_API_KEY` (ترجیحی) یا پرانا `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

مثال `.env` اسنیپٹ:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

نوٹس:

- ٹول دستیاب LLM پرووائیڈر کو خودکار طور پر شناخت کرتا ہے؛ Azure OpenAI یا OpenAI میں سے کسی ایک کو کنفیگر کریں۔
- امیج ترجمہ کے لیے دونوں `AZURE_AI_SERVICE_API_KEY` اور `AZURE_AI_SERVICE_ENDPOINT` ضروری ہیں۔
- اگر ضروری ویریبلز غائب ہوں تو CLI واضح ایرر دے گا۔

## ڈیولپمنٹ ورک فلو

- سورس کوڈ `src/co_op_translator` میں ہے؛ ٹیسٹس `tests/` میں۔
- بنیادی CLIs (انٹری پوائنٹس کے ذریعے انسٹال):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

مزید استعمال کی دستاویزات `getting_started/` میں دیکھیں۔

## ٹیسٹنگ ہدایات

ریپوزٹری روٹ سے ٹیسٹس چلائیں۔ کچھ ٹیسٹس کے لیے API کریڈینشلز درکار ہو سکتے ہیں؛ ضرورت پڑنے پر انہیں چھوڑ دیں۔

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

اختیاری کوریج (اس کے لیے `coverage` چاہیے):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## کوڈ اسٹائل گائیڈ لائنز

- فارمیٹر: Black (`pyproject.toml` میں کنفیگر، لائن لمبائی 88)
- لنٹر: Ruff (`pyproject.toml` میں کنفیگر، لائن لمبائی 120)
- ٹائپ چیکس: mypy (کنفیگریشن موجود؛ انسٹال ہو تو فعال کریں)

کمانڈز:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

پائتھون سورسز کو `src/` میں، ٹیسٹس کو `tests/` میں رکھیں، اور پیکیج نیم اسپیس (`co_op_translator.*`) کے اندر واضح امپورٹس کو ترجیح دیں۔

## بلڈ اور ڈپلائمنٹ

بلڈ آرٹیفیکٹس `dist/` میں شائع ہوتے ہیں۔

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions کے ذریعے آٹومیشن سپورٹڈ ہے؛ دیکھیں:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### کنٹینر امیج (GHCR)

- آفیشل امیج: `ghcr.io/azure/co-op-translator:<tag>`
- ٹیگز: `latest` (مین پر)، سیمینٹک ٹیگز جیسے `vX.Y.Z`، اور `sha` ٹیگ
- ملٹی-آرچ: `linux/amd64, linux/arm64` Buildx کے ذریعے سپورٹڈ
- ڈاکرفائل پیٹرن: بلڈر میں ڈیپینڈنسی وہیلز بنائیں (`build-essential` اور `python3-dev` کے ساتھ) اور رن ٹائم میں لوکل وہیل ہاؤس سے انسٹال کریں (`pip install --no-index --find-links=/wheels`)
- ورک فلو: `.github/workflows/docker-publish.yml` GHCR پر بلڈ اور پش کرتا ہے

## سیکیورٹی کے پہلو

- API کیز اور اینڈ پوائنٹس کو `.env` یا اپنے CI سیکرٹس اسٹور میں رکھیں؛ سیکرٹس کبھی کمیٹ نہ کریں۔
- امیج ترجمہ کے لیے Azure AI Vision کیز/اینڈ پوائنٹس ضروری ہیں؛ بصورت دیگر `-img` چھوڑ دیں۔
- بڑے ترجمہ بیچز چلاتے وقت پرووائیڈر کوٹا/ریٹ لمٹس کی تصدیق کریں۔

## پل ریکویسٹ گائیڈ لائنز

### جمع کرانے سے پہلے

1. **اپنی تبدیلیاں ٹیسٹ کریں:**
   - متاثرہ نوٹ بکس مکمل طور پر چلائیں
   - تمام سیلز بغیر ایرر کے چلیں
   - آؤٹ پٹس مناسب ہوں

2. **دستاویزات کی اپڈیٹس:**
   - نئے تصورات شامل کرنے پر `README.md` اپڈیٹ کریں
   - پیچیدہ کوڈ کے لیے نوٹ بکس میں کمنٹس شامل کریں
   - مارک ڈاؤن سیلز میں مقصد واضح کریں

3. **فائل تبدیلیاں:**
   - `.env` فائلز کمیٹ نہ کریں (استعمال کریں `.env.example`)
   - `venv/` یا `__pycache__/` ڈائریکٹریز کمیٹ نہ کریں
   - نوٹ بکس آؤٹ پٹس رکھیں جب وہ تصورات واضح کریں
   - عارضی فائلز اور بیک اپ نوٹ بکس (`*-backup.ipynb`) ہٹا دیں

4. **اسٹائل اور فارمیٹنگ:**
   - اسٹائل اور فارمیٹنگ گائیڈ لائنز پر عمل کریں
   - اسٹائل اور فارمیٹنگ ایشوز کے لیے `poetry run black .` اور `poetry run ruff check .` چلائیں

5. **ٹیسٹس اور CLI ہیلپ شامل/اپڈیٹ کریں:**
   - رویے میں تبدیلی پر ٹیسٹس شامل یا اپڈیٹ کریں
   - CLI ہیلپ کو تبدیلیوں کے مطابق رکھیں


### کمیٹ میسج اور مرج اسٹریٹیجی

ہم Squash and Merge کو ڈیفالٹ کے طور پر استعمال کرتے ہیں۔ فائنل squash کمیٹ میسج اس فارمیٹ میں ہونا چاہیے:

```bash
<type>: <description> (#<PR number>)
```

اجازت یافتہ اقسام:
- `Docs` — دستاویزات کی اپڈیٹس
- `Build` — بلڈ سسٹم، ڈیپینڈنسیز، کنفیگریشن/CI
- `Core` — بنیادی فنکشنلٹی اور فیچرز (جیسے `src/co_op_translator/core`)

مثالیں:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

نوٹس:
- PR ٹائٹلز اکثر لیبلز کی بنیاد پر خودکار طور پر پری فکس ہو جاتے ہیں؛ بنے ہوئے پری فکس کی تصدیق کریں۔

### PR ٹائٹل فارمیٹ

واضح، مختصر ٹائٹلز استعمال کریں۔ فائنل squash کمیٹ کی طرح ہی ساخت کو ترجیح دیں:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## ڈیبگنگ اور ٹربل شوٹنگ

- عام مسائل اور حل: `getting_started/troubleshooting.md`
- سپورٹڈ زبانیں اور نوٹس (فونٹس/معروف مسائل سمیت): `getting_started/supported-languages.md`
- نوٹ بکس میں لنک مسائل کے لیے دوبارہ چلائیں: `migrate-links -l "all" -y`

## ایجنٹس کے لیے نوٹس

- دوبارہ قابل استعمال ماحول کے لیے Poetry کو ترجیح دیں؛ بصورت دیگر `requirements.txt` استعمال کریں۔
- CI میں CLIs چلاتے وقت ضروری سیکرٹس ماحول کی ویریبلز یا `.env` انجیکشن کے ذریعے فراہم کریں۔
- مونو ریپو کنزیومرز کے لیے یہ ریپو اسٹینڈ الون پیکیج کے طور پر کام کرتا ہے؛ کسی سب-پیکیج کوآرڈینیشن کی ضرورت نہیں۔

- ملٹی-آرچ گائیڈنس: اگر ARM یوزرز (Apple Silicon/ARM سرورز) ہدف ہیں تو `linux/arm64` رکھیں؛ بصورت دیگر سادگی کے لیے صرف `linux/amd64` کافی ہے۔
- اگر یوزرز کنٹینر استعمال کرنا چاہتے ہیں تو انہیں `README.md` میں ڈاکر کوئیک اسٹارٹ کی طرف رہنمائی کریں؛ Bash اور PowerShell دونوں ورژنز شامل کریں کیونکہ کوٹنگ میں فرق آتا ہے۔

---

**اعلانِ دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی صورت میں ہم ذمہ دار نہیں ہیں۔