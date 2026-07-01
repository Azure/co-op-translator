# راه‌اندازی Azure AI

از این راهنما زمانی استفاده کنید که می‌خواهید Azure OpenAI را برای ترجمهٔ متن و Azure AI Vision را برای استخراج متن از تصاویر پیکربندی کنید.

## پیش‌نیازها

- یک اشتراک Azure.
- دسترسی برای ایجاد یا استفاده از منابع Azure AI و استقرار مدل‌ها.
- یک پروژه در Azure AI Foundry یا دسترسی معادل به منابع Azure OpenAI و Azure AI Vision.

## ایجاد یک پروژه Azure AI

1. [Azure AI Foundry](https://ai.azure.com) را باز کنید.
2. یک پروژه ایجاد کنید یا یکی را انتخاب کنید.
3. یک هاب AI برای پروژه ایجاد کنید یا انتخاب کنید.
4. پس از ایجاد، نمای کلی پروژه را باز کنید.

## استقرار یک مدل Azure OpenAI

1. در پروژه، **Models + endpoints** را باز کنید.
2. گزینه **Deploy model** را انتخاب کنید.
3. یک مدل GPT مانند `gpt-4o` را انتخاب کنید.
4. مدل را مستقر کنید.
5. نقطه پایانی، نام استقرار، نام مدل، کلید API و نسخه API را ثبت کنید.

!!! note
    نسخه API Azure OpenAI جدا از نسخهٔ مدل نمایش‌داده‌شده در Azure AI Foundry است. برای استقرار خود یک نسخهٔ API پشتیبانی‌شده را انتخاب کنید.

## پیکربندی Azure AI Vision

ترجمهٔ تصویر از Azure AI Vision برای استخراج متن از تصاویر منبع قبل از ترجمهٔ متن استفاده می‌کند.

در پروژه Azure AI خود، کلید و نقطه پایانی Azure AI Services را پیدا کنید.

![یافتن اطلاعات سرویس Azure AI](../../assets/find-azure-ai-info.png)

Record:

- نقطه پایانی سرویس Azure AI
- کلید API سرویس Azure AI

## متغیرهای محیطی

اعتبارنامه‌ها را به فایل `.env` یا اسرار CI خود اضافه کنید.

```bash
# Azure AI Vision، برای ترجمهٔ تصاویر لازم است
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI، برای ترجمهٔ متن لازم است
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator همچنین از مجموعه‌های اعتبارنامهٔ پشتیبان اختیاری پشتیبانی می‌کند. یک مجموعهٔ کامل ارائه‌دهنده را با پسوندهایی مانند `_1` یا `_2` تکثیر کنید؛ تمام متغیرها در یک مجموعهٔ پشتیبان باید همان پسوند را داشته باشند.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## مراحل بعدی

- برای تنظیم متغیرهای محیطی محلی یا CI، به [Configuration](configuration.md) بازگردید.
- از [CLI Reference](cli.md) برای دستورات ترجمه استفاده کنید.
- از [GitHub Actions](github-actions.md) برای خودکارسازی pull requestهای ترجمه استفاده کنید.