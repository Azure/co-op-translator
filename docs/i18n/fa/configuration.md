# پیکربندی

Co-op Translator نیاز به یک ارائه‌دهنده مدل زبان دارد. ترجمه تصویر به‌علاوه به Azure AI Vision نیاز دارد.

پیکربندی از متغیرهای محیطی خوانده می‌شود. برای پروژه‌های محلی، آن‌ها را در فایل `.env` در ریشه پروژه قرار دهید.

برای راه‌اندازی منابع Azure، به [راهنمای راه‌اندازی Azure AI](azure-ai-setup.md) مراجعه کنید.

## تنظیم محیط اجرا به‌صورت محلی

قبل از اجرای CLI به‌صورت محلی از یک محیط مجازی استفاده کنید. Co-op Translator از Python 3.10 تا 3.12 پشتیبانی می‌کند.

برای استفاده معمولی از CLI، بسته منتشرشده را داخل یک محیط مجازی نصب کنید:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

برای توسعه مخزن، بجای آن وابستگی‌ها را از ریشه پروژه نصب کنید:

```bash
poetry install
poetry run translate --help
```

پس از در دسترس بودن CLI، یک ارائه‌دهنده مدل زبان را در `.env` پیکربندی کنید.

## انتخاب ارائه‌دهنده

ابزار ارائه‌دهنده‌ها را به‌صورت خودکار به این ترتیب تشخیص می‌دهد:

1. Azure OpenAI
2. OpenAI

اگر هیچ‌یک از ارائه‌دهنده‌ها پیکربندی نشده باشند، `translate`, `evaluate`, `migrate-links`، و `run_translation` در بررسی‌های پیکربندی شکست می‌خورند. `co-op-review` و `run_review` بررسی‌های نگهداری قطعی هستند و به اعتبارنامه ارائه‌دهنده نیاز ندارند.

## Azure OpenAI

از Azure OpenAI زمانی استفاده کنید که مدل شما در Azure AI Foundry یا Azure OpenAI Service مستقر شده باشد.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

بررسی اتصال از نقطه انتهایی، کلید API، نسخه API، و نام استقرار قبل از شروع ترجمه استفاده می‌کند.

## OpenAI

از OpenAI زمانی استفاده کنید که مستقیماً از API OpenAI فراخوانی می‌کنید.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # اختیاری
OPENAI_BASE_URL="..."        # اختیاری
```

`OPENAI_CHAT_MODEL_ID` لازم است زیرا مترجم برای فراخوانی‌های API به یک مدل چت صریح نیاز دارد.

## Azure AI Vision

ترجمه تصویر به Azure AI Vision احتیاج دارد تا ابزار بتواند قبل از ترجمه متن را از تصاویر استخراج کند.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

اگر ترجمه تصویر با `-img`، `images=True`، یا بدون فیلتر نوع محتوا انتخاب شده باشد، ابزار پیکربندی Vision را قبل از شروع ترجمه اعتبارسنجی می‌کند.

## چند مجموعه اعتبارنامه

لایه پیکربندی از چند مجموعه اعتبارنامه با افزودن پسوند به متغیرها با همان شاخص پشتیبانی می‌کند:

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

هر مجموعه باید کامل باشد. بررسی سلامت یک مجموعه کاری را قبل از ادامه ترجمه انتخاب می‌کند.

## نیازمندی‌های فرمان

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | بله | خیر | فقط Markdown را ترجمه می‌کند. |
| `translate -nb` | بله | خیر | فقط نوت‌بوک‌ها را ترجمه می‌کند. |
| `translate -img` | بله | بله | فقط تصاویر را ترجمه می‌کند. |
| `translate` with no type flags | بله | بله | حالت پیش‌فرض شامل Markdown، نوت‌بوک‌ها و تصاویر است. |
| `evaluate` | بله | خیر | از ارزیابی LLM استفاده می‌کند مگر این‌که `--fast` انتخاب شود. |
| `migrate-links` | بله | خیر | مهاجرت لینک را انجام می‌دهد، اما بررسی‌های پیکربندی مشترک را نیز اجرا می‌کند. |
| `co-op-review` | خیر | خیر | بررسی‌های قطعی ساختار ترجمه، تازه‌بودن، Markdown، نوت‌بوک و لینک‌های محلی را اجرا می‌کند. |
| `run_translation(markdown=True)` | بله | خیر | ترجمهٔ برنامه‌ای Markdown. |
| `run_translation(images=True)` | بله | بله | ترجمهٔ برنامه‌ای تصاویر. |
| `run_review(...)` | خیر | خیر | بازبینی قطعی برنامه‌ای. |

## دایرکتوری‌های خروجی

خروجی پیش‌فرض ترجمه متن:

```text
translations/<language-code>/<source-relative-path>
```

خروجی پیش‌فرض تصاویر ترجمه‌شده:

```text
translated_images/<language-code>/<source-relative-path>
```

API پایتون می‌تواند این دایرکتوری‌ها را با `translations_dir` و `image_dir` بازنویسی کند.