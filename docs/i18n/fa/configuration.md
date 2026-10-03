# پیکربندی

Co-op Translator به یک ارائه‌دهنده مدل زبانی نیاز دارد. ترجمه تصویر علاوه بر آن به Azure AI Vision نیاز دارد.

پیکربندی از متغیرهای محیطی خوانده می‌شود. برای پروژه‌های محلی، آن‌ها را در یک `.env` فایل در ریشهٔ پروژه قرار دهید.

برای راه‌اندازی منابع Azure، به [راه‌اندازی Azure AI](azure-ai-setup.md) مراجعه کنید.

## تنظیم محیط اجرای محلی

قبل از اجرای CLI به‌صورت محلی از یک محیط مجازی استفاده کنید. Co-op Translator از Python 3.11 تا 3.14 پشتیبانی می‌کند.

برای استفاده عادی از CLI، بسته منتشرشده را داخل یک محیط مجازی نصب کنید:

### ویندوز (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / لینوکس

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### توسعه مخزن

برای توسعهٔ مخزن، به‌جای آن وابستگی‌ها را از ریشهٔ پروژه نصب کنید:

```bash
poetry install
poetry run translate --help
```

پس از در دسترس قرار گرفتن CLI، یک ارائه‌دهندهٔ مدل زبانی را در `.env` پیکربندی کنید.

## انتخاب ارائه‌دهنده

ابزار ارائه‌دهندگان را به‌صورت خودکار به این ترتیب شناسایی می‌کند:

1. Azure OpenAI
2. OpenAI
3. Anthropic

ترجمه به اعتبارنامهٔ ارائه‌دهنده نیاز دارد، مگر برای پیش‌نمایش‌هایی مانند `translate -l "ko" -md --dry-run`. `migrate-links`، `co-op-review` و `run_review` عملیات نگهداری قطعی هستند و به اعتبارنامهٔ ارائه‌دهنده نیاز ندارند.

## بک‌اند کلاینت مدل

از نسخهٔ Co-op Translator 0.22.0 به بعد، Azure OpenAI، OpenAI و Anthropic به‌صورت پیش‌فرض از Microsoft Agent Framework استفاده می‌کنند. برای استفادهٔ عادی نیازی به تنظیم بک‌اند نیست.

Semantic Kernel به‌صورت موقتی برای سازگاری در دسترس باقی مانده است. برای انتخاب صریح آن، تنظیم زیر را قرار دهید:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

از Semantic Kernel استفاده کردن یک هشدار منسوخ بودن صادر می‌کند. برنامه‌ریزی شده است که بسته در نسخهٔ 0.23.0 Semantic Kernel را به یک وابستگی اختیاری تبدیل کند و در 0.24.0 این یکپارچگی را حذف کند، که مشروط به نتایج سازگاری و بازخورد کاربران است. Anthropic نیازمند `agent-framework` است؛ انتخاب صریح `semantic-kernel` همراه با Anthropic با خطای پیکربندی مواجه می‌شود. مقادیر نامعتبر هنگام راه‌اندازی مترجم با پشتیبانی ارائه‌دهنده شکست می‌خورند به‌جای اینکه بی‌صدا به حالتی دیگر برگردند. روند انتشار را دنبال کنید و موانع را در [مسئلهٔ GitHub #543](https://github.com/Azure/co-op-translator/issues/543) گزارش دهید.

## Azure OpenAI

زمانی از Azure OpenAI استفاده کنید که مدل شما در Azure AI Foundry یا Azure OpenAI Service مستقر شده باشد.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

پیش از آغاز ترجمه، بررسی اتصال از endpoint، API key، API version و نام استقرار استفاده می‌کند.

## OpenAI

وقتی به‌طور مستقیم از API OpenAI فراخوانی می‌کنید از OpenAI استفاده کنید.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

متغیر `OPENAI_CHAT_MODEL_ID` لازم است زیرا مترجم برای فراخوانی‌های API به یک مدل چت صریح نیاز دارد.

برای تنظیم پیش‌فرض، `OPENAI_ORG_ID` و `OPENAI_BASE_URL` را خالی بگذارید. شناسهٔ سازمان را فقط در صورتی اضافه کنید که حساب شما به آن نیاز دارد، و آدرس پایه را فقط زمانی که از یک endpoint سفارشی استفاده می‌کنید. مقادیر جایگزین را برای تنظیمات اختیاری کپی نکنید.

## Anthropic Claude

هنگامی که مستقیماً از API Claude فراخوانی می‌کنید از Anthropic استفاده کنید. یک [کلید API Anthropic](https://platform.claude.com/docs/en/get-started) ایجاد کنید و یک [شناسهٔ مدل Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) پشتیبانی‌شده انتخاب کنید.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

متغیرهای `ANTHROPIC_API_KEY` و `ANTHROPIC_MODEL` لازم هستند. نیازی به تنظیم `CO_OP_TRANSLATOR_MODEL_CLIENT` ندارید؛ Agent Framework بک‌اند پیش‌فرض است.

برای API Anthropic، `ANTHROPIC_BASE_URL` را خالی بگذارید. تنها هنگامی که از یک endpoint سفارشی استفاده می‌کنید آن را تنظیم کنید.

مقدار پیش‌فرض `ANTHROPIC_MAX_TOKENS` برابر با `8192` است، که برای نگارش‌هایی با تراکم توکن بالا مانند Meitei Mayek جا را باز نگه می‌دارد. اگر مدل شما یا endpoint سازگار با Anthropic خروجی را کمتر از این حد محدود می‌کند، آن را پایین بیاورید.

## Azure AI Vision

ترجمهٔ تصویر به Azure AI Vision نیاز دارد تا ابزار بتواند قبل از اینکه مدل زبانی پیکربندی‌شده آن را ترجمه کند، متن را از تصاویر استخراج کند. Anthropic می‌تواند متن استخراج‌شده را همانند Azure OpenAI یا OpenAI ترجمه کند.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

اگر ترجمهٔ تصویر با `-img`، `images=True` یا بدون فیلتر نوع محتوا انتخاب شده باشد، ابزار پیکربندی Vision را قبل از شروع ترجمه بررسی می‌کند.

## مجموعه‌های چندگانهٔ اعتبارنامه

لایهٔ پیکربندی با افزودن پسوند شاخص یکسان به متغیرها از مجموعه‌های چندگانهٔ اعتبارنامه پشتیبانی می‌کند:

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

هر مجموعه باید کامل باشد. بررسی سلامت یک مجموعهٔ کاری را قبل از ادامهٔ ترجمه انتخاب می‌کند.

OpenAI و Anthropic از همان قرارداد پسوند پشتیبانی می‌کنند. هر متغیر در یک مجموعهٔ اعتبارنامه را با همان پسوند نگه دارید، از جمله مقادیر اختیاری مانند `OPENAI_BASE_URL_1` یا `ANTHROPIC_BASE_URL_1`.

## نیازمندی‌های فرمان‌ها

| فرمان یا API | نیاز به LLM | نیاز به Vision | توضیحات |
| --- | --- | --- | --- |
| `translate -md` | بله | خیر | فقط Markdown را ترجمه می‌کند. |
| `translate -nb` | بله | خیر | فقط نوت‌بوک‌ها را ترجمه می‌کند. |
| `translate -img` | بله | بله | فقط تصاویر را ترجمه می‌کند. |
| `translate` بدون فلگ نوع | بله | بله | حالت پیش‌فرض شامل Markdown، نوت‌بوک‌ها و تصاویر است. |
| `evaluate` | بله | خیر | از ارزیابی LLM استفاده می‌کند مگر اینکه `--fast` انتخاب شود. |
| `migrate-links` | خیر | خیر | مهاجرت لینک محلی را بدون فراخوانی ارائه‌دهنده انجام می‌دهد. |
| `co-op-review` | خیر | خیر | ساختار ترجمهٔ قطعی، تازگی، Markdown، نوت‌بوک و بررسی‌های لینک محلی را اجرا می‌کند. |
| `run_translation(markdown=True)` | بله | خیر | ترجمهٔ Markdown برنامه‌ای. |
| `run_translation(images=True)` | بله | بله | ترجمهٔ تصاویر برنامه‌ای. |
| `run_review(...)` | خیر | خیر | بازبینی قطعی برنامه‌ای. |

## دایرکتوری‌های خروجی

خروجی پیش‌فرض ترجمهٔ متن:

```text
translations/<language-code>/<source-relative-path>
```

خروجی پیش‌فرض تصاویر ترجمه‌شده:

```text
translated_images/<language-code>/<source-relative-path>
```

API پایتون می‌تواند این دایرکتوری‌ها را با `translations_dir` و `image_dir` بازنویسی کند.