<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:20:39+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fa"
}
-->
## نمای کلی پروژه

Co‑op Translator یک ابزار خط فرمان پایتون و یک گردش کار GitHub Actions است که فایل‌های Markdown، دفترچه‌های Jupyter و متن تصاویر را به چندین زبان ترجمه می‌کند. خروجی‌ها را در پوشه‌های مخصوص هر زبان سازماندهی می‌کند و ترجمه‌ها را با محتوای منبع همگام نگه می‌دارد. این پروژه به صورت یک کتابخانه مدیریت‌شده با Poetry با نقاط ورود CLI ساختاربندی شده است.

### نمای معماری

- نقاط ورود CLI (`translate`، `migrate-links`، `evaluate`) یک CLI یکپارچه را فراخوانی می‌کنند که به جریان‌های ترجمه، مهاجرت لینک و ارزیابی هدایت می‌شود.
- بارگذار پیکربندی، فایل `.env` را می‌خواند و ارائه‌دهنده LLM (Azure OpenAI یا OpenAI) و در صورت نیاز، ارائه‌دهنده بینایی (Azure AI Service) را برای استخراج متن تصویر به طور خودکار شناسایی می‌کند.
- هسته ترجمه، Markdown و دفترچه‌ها را مدیریت می‌کند؛ خط لوله بینایی هنگام استفاده از `-img` متن را از تصاویر استخراج می‌کند.
- خروجی‌ها در `translations/<lang>/` برای متن و `translated_images/` برای تصاویر سازماندهی می‌شوند و ساختار اصلی را حفظ می‌کنند.

### فناوری‌ها و چارچوب‌های کلیدی

- پایتون 3.10 تا 3.12، Poetry برای بسته‌بندی
- CLI: `click`
- SDKهای LLM/AI: Azure OpenAI، OpenAI
- بینایی: Azure AI Service (Computer Vision)
- HTTP و داده: `httpx`، `pydantic`
- پردازش تصویر: `pillow`، `opencv-python`، `matplotlib`
- ابزارها: `pytest`، `black`، `ruff`

## دستورات راه‌اندازی

### پیش‌نیازها

- پایتون 3.10 تا 3.12
- اشتراک Azure (اختیاری، برای سرویس‌های Azure AI)
- دسترسی اینترنت برای APIهای LLM/بینایی (مانند Azure OpenAI/OpenAI، Azure AI Vision)

### گزینه A: Poetry (توصیه‌شده)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### گزینه B: pip/venv

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

## نحوه استفاده برای کاربر نهایی

### داکر (تصویر منتشرشده)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

نکات:
- نقطه ورود پیش‌فرض `translate` است. برای مهاجرت لینک با `--entrypoint migrate-links` جایگزین کنید.
- مطمئن شوید که دید پکیج GHCR روی Public باشد تا کشیدن ناشناس ممکن باشد.

### CLI (نصب با pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### پیکربندی محیط

یک فایل `.env` در ریشه مخزن بسازید و اعتبارنامه‌ها/آدرس‌های سرویس مدل زبانی و (در صورت نیاز) سرویس بینایی را وارد کنید. برای راه‌اندازی مخصوص هر ارائه‌دهنده، به `getting_started/set-up-azure-ai.md` مراجعه کنید.

### متغیرهای محیطی مورد نیاز

حداقل باید یک ارائه‌دهنده LLM پیکربندی شود. برای ترجمه تصویر، باید Azure AI Service نیز پیکربندی شود.

- Azure OpenAI (ترجمه متنی):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (جایگزین ترجمه متنی):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (اختیاری)
  - `OPENAI_CHAT_MODEL_ID` (الزامی هنگام استفاده از ارائه‌دهنده OpenAI)
  - `OPENAI_BASE_URL` (اختیاری؛ پیش‌فرض `https://api.openai.com/v1`)

- Azure AI Service برای استخراج متن تصویر (الزامی هنگام استفاده از `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (ترجیح داده می‌شود) یا `AZURE_SUBSCRIPTION_KEY` قدیمی
  - `AZURE_AI_SERVICE_ENDPOINT`

نمونه‌ای از بخش `.env`:

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

نکات:

- ابزار به طور خودکار ارائه‌دهنده LLM موجود را شناسایی می‌کند؛ یکی از Azure OpenAI یا OpenAI را پیکربندی کنید.
- ترجمه تصویر به هر دو `AZURE_AI_SERVICE_API_KEY` و `AZURE_AI_SERVICE_ENDPOINT` نیاز دارد.
- اگر متغیرهای مورد نیاز وجود نداشته باشند، CLI خطای واضحی نمایش می‌دهد.

## جریان کاری توسعه

- کد منبع در `src/co_op_translator` قرار دارد؛ تست‌ها در `tests/`.
- CLIهای اصلی (نصب‌شده از طریق entry point):

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

مستندات استفاده بیشتر در `getting_started/` موجود است.

## دستورالعمل‌های تست

تست‌ها را از ریشه مخزن اجرا کنید. برخی تست‌ها ممکن است به اعتبارنامه API نیاز داشته باشند؛ در صورت نیاز آن‌ها را رد کنید.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

پوشش اختیاری (نیازمند `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## راهنمای سبک کد

- قالب‌بندی: Black (پیکربندی در `pyproject.toml`، طول خط 88)
- لینتر: Ruff (پیکربندی در `pyproject.toml`، طول خط 120)
- بررسی نوع: mypy (پیکربندی موجود؛ در صورت نصب فعال کنید)

دستورات:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

کدهای پایتون را زیر `src/`، تست‌ها را زیر `tests/` قرار دهید و واردات را در فضای نام پکیج (`co_op_translator.*`) به صورت صریح انجام دهید.

## ساخت و انتشار

خروجی‌های ساخت در `dist/` منتشر می‌شوند.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

اتوماسیون از طریق GitHub Actions پشتیبانی می‌شود؛ ببینید:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### تصویر کانتینر (GHCR)

- تصویر رسمی: `ghcr.io/azure/co-op-translator:<tag>`
- تگ‌ها: `latest` (روی main)، تگ‌های معنایی مانند `vX.Y.Z` و یک تگ `sha`
- چند معماری: `linux/amd64, linux/arm64` با Buildx پشتیبانی می‌شود
- الگوی Dockerfile: ساخت چرخ‌های وابستگی در بیلدر (با `build-essential` و `python3-dev`) و نصب از wheelhouse محلی در زمان اجرا (`pip install --no-index --find-links=/wheels`)
- جریان کار: `.github/workflows/docker-publish.yml` می‌سازد و به GHCR پوش می‌کند

## ملاحظات امنیتی

- کلیدهای API و آدرس‌ها را در `.env` یا مخزن اسرار CI خود نگه دارید؛ هرگز اسرار را کامیت نکنید.
- برای ترجمه تصویر، کلیدها/آدرس‌های Azure AI Vision لازم است؛ در غیر این صورت `-img` را حذف کنید.
- هنگام اجرای دسته‌های بزرگ ترجمه، سهمیه‌ها/محدودیت‌های ارائه‌دهنده را بررسی کنید.

## راهنمای درخواست Pull

### پیش از ارسال

1. **تست تغییرات:**
   - دفترچه‌های تحت تأثیر را کامل اجرا کنید
   - مطمئن شوید همه سلول‌ها بدون خطا اجرا می‌شوند
   - بررسی کنید خروجی‌ها مناسب باشند

2. **به‌روزرسانی مستندات:**
   - اگر مفهوم جدیدی اضافه می‌کنید، `README.md` را به‌روزرسانی کنید
   - برای کدهای پیچیده در دفترچه‌ها کامنت بگذارید
   - مطمئن شوید سلول‌های markdown هدف را توضیح می‌دهند

3. **تغییرات فایل:**
   - از کامیت کردن فایل‌های `.env` خودداری کنید (از `.env.example` استفاده کنید)
   - دایرکتوری‌های `venv/` یا `__pycache__/` را کامیت نکنید
   - خروجی دفترچه‌ها را زمانی که مفهومی را نشان می‌دهند نگه دارید
   - فایل‌های موقت و دفترچه‌های پشتیبان (`*-backup.ipynb`) را حذف کنید

4. **سبک و قالب‌بندی:**
   - از راهنمای سبک و قالب‌بندی پیروی کنید
   - `poetry run black .` و `poetry run ruff check .` را برای بررسی سبک و قالب‌بندی اجرا کنید

5. **افزودن/به‌روزرسانی تست‌ها و راهنمای CLI:**
   - هنگام تغییر رفتار، تست‌ها را اضافه یا به‌روزرسانی کنید
   - راهنمای CLI را با تغییرات هماهنگ نگه دارید


### قالب پیام کامیت و استراتژی ادغام

ما به طور پیش‌فرض از Squash and Merge استفاده می‌کنیم. پیام کامیت نهایی squash باید به صورت زیر باشد:

```bash
<type>: <description> (#<PR number>)
```

انواع مجاز:
- `Docs` — به‌روزرسانی مستندات
- `Build` — سیستم ساخت، وابستگی‌ها، پیکربندی/CI
- `Core` — قابلیت‌ها و ویژگی‌های اصلی (مثلاً `src/co_op_translator/core`)

نمونه‌ها:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

نکات:
- عناوین PR اغلب بر اساس برچسب‌ها به طور خودکار پیشوند می‌گیرند؛ صحت پیشوند تولیدشده را بررسی کنید.

### قالب عنوان PR

از عناوین واضح و مختصر استفاده کنید. ساختار مشابه پیام squash نهایی را ترجیح دهید:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## اشکال‌زدایی و رفع مشکل

- مشکلات رایج و راه‌حل‌ها: `getting_started/troubleshooting.md`
- زبان‌های پشتیبانی‌شده و نکات (شامل فونت‌ها/مشکلات شناخته‌شده): `getting_started/supported-languages.md`
- برای مشکلات لینک در دفترچه‌ها، دوباره اجرا کنید: `migrate-links -l "all" -y`

## نکات برای ایجنت‌ها

- برای محیط‌های قابل بازتولید Poetry را ترجیح دهید؛ در غیر این صورت از `requirements.txt` استفاده کنید.
- هنگام فراخوانی CLIها در CI، اسرار مورد نیاز را از طریق متغیرهای محیطی یا تزریق `.env` فراهم کنید.
- برای مصرف‌کنندگان monorepo، این مخزن به عنوان یک پکیج مستقل عمل می‌کند؛ هماهنگی زیرپکیج لازم نیست.

- راهنمای چند معماری: اگر کاربران ARM (Apple Silicon/سرورهای ARM) هدف هستند، `linux/arm64` را نگه دارید؛ در غیر این صورت فقط `linux/amd64` برای سادگی کافی است.
- اگر کاربران ترجیح می‌دهند از کانتینر استفاده کنند، آن‌ها را به راهنمای سریع Docker در `README.md` ارجاع دهید؛ نسخه‌های Bash و PowerShell را به دلیل تفاوت در کوتیشن‌ها لحاظ کنید.

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً آگاه باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادقتی باشند. نسخه اصلی سند به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.