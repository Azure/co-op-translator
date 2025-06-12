<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:39:12+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "fa"
}
-->
# ایجاد فایل *.env* در دایرکتوری ریشه

در این آموزش، شما را در تنظیم متغیرهای محیطی برای سرویس‌های Azure با استفاده از فایل *.env* راهنمایی می‌کنیم. متغیرهای محیطی به شما امکان می‌دهند که اطلاعات حساس مانند کلیدهای API را به‌صورت امن مدیریت کنید، بدون اینکه آن‌ها را مستقیماً در کد خود وارد کنید.

> [!IMPORTANT]
> - فقط یکی از سرویس‌های مدل زبان (Azure OpenAI یا OpenAI) باید پیکربندی شود. متغیرهای محیطی مربوط به سرویس مورد نظر خود را پر کنید. اگر متغیرهای محیطی چند مدل زبان تنظیم شوند، مترجم مشترک یکی را بر اساس اولویت انتخاب می‌کند.
> - اگر متغیرهای محیطی Computer Vision تنظیم نشده باشند، مترجم به‌طور خودکار به [حالت فقط Markdown](./markdown-only-mode.md) تغییر می‌یابد.

> [!NOTE]
> این راهنما عمدتاً بر سرویس‌های Azure تمرکز دارد، اما می‌توانید هر مدل زبانی که پشتیبانی می‌شود را از [فهرست مدل‌ها و سرویس‌های پشتیبانی شده](../README.md#-supported-models-and-services) انتخاب کنید.

## ایجاد فایل *.env*

در دایرکتوری ریشه پروژه خود، فایلی با نام *.env* ایجاد کنید. این فایل تمام متغیرهای محیطی شما را در قالبی ساده ذخیره خواهد کرد.

> [!WARNING]
> فایل *.env* خود را در سیستم‌های کنترل نسخه مانند Git ثبت (commit) نکنید. برای جلوگیری از ثبت تصادفی، فایل *.env* را به .gitignore خود اضافه کنید.

1. به دایرکتوری ریشه پروژه خود بروید.

1. در دایرکتوری ریشه پروژه خود، یک فایل *.env* ایجاد کنید.

1. فایل *.env* را باز کرده و قالب زیر را در آن جای‌گذاری کنید:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> اگر می‌خواهید کلیدهای API و نقاط پایانی خود را پیدا کنید، می‌توانید به [set-up-azure-ai.md](../set-up-azure-ai.md) مراجعه کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوء تفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.