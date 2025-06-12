<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b58d7c3cb4210697a073d20eb3064945",
  "translation_date": "2025-06-12T11:59:53+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "my"
}
-->
# Set Up Azure AI for Co-op Translator (Azure OpneAI & Azure AI Vision)

این راهنما شما را در تنظیم Azure OpenAI برای ترجمه زبان و Azure Computer Vision برای تحلیل محتوای تصویر (که سپس می‌تواند برای ترجمه مبتنی بر تصویر استفاده شود) در Azure AI Foundry راهنمایی می‌کند.

**پیش‌نیازها:**
- یک حساب Azure با اشتراک فعال.
- دسترسی کافی برای ایجاد منابع و استقرارها در اشتراک Azure خود.

## ایجاد یک پروژه Azure AI

ابتدا یک پروژه Azure AI ایجاد می‌کنید که به عنوان مرکزی برای مدیریت منابع AI شما عمل می‌کند.

1. به [https://ai.azure.com](https://ai.azure.com) بروید و با حساب Azure خود وارد شوید.

1. گزینه **+Create** را برای ایجاد پروژه جدید انتخاب کنید.

1. کارهای زیر را انجام دهید:
   - یک **Project name** وارد کنید (مثلاً `CoopTranslator-Project`).
   - **AI hub** را انتخاب کنید (مثلاً `CoopTranslator-Hub`) (در صورت نیاز، یک مورد جدید ایجاد کنید).

1. روی "**Review and Create**" کلیک کنید تا پروژه شما راه‌اندازی شود. به صفحه نمای کلی پروژه خود هدایت خواهید شد.

## راه‌اندازی Azure OpenAI برای ترجمه زبان

درون پروژه خود، یک مدل Azure OpenAI را مستقر خواهید کرد تا به عنوان بک‌اند برای ترجمه متن عمل کند.

### رفتن به پروژه شما

اگر هنوز در آنجا نیستید، پروژه تازه ایجاد شده خود (مثلاً `CoopTranslator-Project`) را در Azure AI Foundry باز کنید.

### استقرار مدل OpenAI

1. از منوی سمت چپ پروژه، زیر "My assets"، گزینه "**Models + endpoints**" را انتخاب کنید.

1. روی **+ Deploy model** کلیک کنید.

1. گزینه **Deploy Base Model** را انتخاب کنید.

1. لیستی از مدل‌های موجود به شما نمایش داده می‌شود. مدل GPT مناسب را فیلتر یا جستجو کنید. ما مدل `gpt-4o` را توصیه می‌کنیم.

1. مدل مورد نظر خود را انتخاب کرده و روی **Confirm** کلیک کنید.

1. روی **Deploy** کلیک کنید.

### پیکربندی Azure OpenAI

پس از استقرار، می‌توانید استقرار را از صفحه "**Models + endpoints**" انتخاب کنید تا **REST endpoint URL**، **Key**، **Deployment name**، **Model name** و **API version** آن را ببینید. این موارد برای یکپارچه‌سازی مدل ترجمه در برنامه شما لازم است.

> [!NOTE]
> می‌توانید نسخه‌های API را از صفحه [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) بر اساس نیاز خود انتخاب کنید. توجه داشته باشید که **API version** با **Model version** که در صفحه **Models + endpoints** در Azure AI Foundry نمایش داده می‌شود متفاوت است.

## راه‌اندازی Azure Computer Vision برای ترجمه تصویر

برای فعال کردن ترجمه متن داخل تصاویر، باید کلید API و Endpoint سرویس Azure AI را پیدا کنید.

1. به پروژه Azure AI خود بروید (مثلاً `CoopTranslator-Project`). مطمئن شوید در صفحه نمای کلی پروژه هستید.

### پیکربندی سرویس Azure AI

کلید API و Endpoint را از سرویس Azure AI پیدا کنید.

1. به پروژه Azure AI خود بروید (مثلاً `CoopTranslator-Project`). مطمئن شوید در صفحه نمای کلی پروژه هستید.

1. کلید **API Key** و **Endpoint** را از تب Azure AI Service پیدا کنید.

    ![Find API Key and Endpoint](../../../translated_images/find-azure-ai-info.60f8299be786dd67e61e2c79b4b9ea1f7694e6c0923f17a90bc6abf9d5f1dbd7.my.png)

این اتصال قابلیت‌های منبع سرویس Azure AI مرتبط (از جمله تحلیل تصویر) را برای پروژه AI Foundry شما در دسترس قرار می‌دهد. سپس می‌توانید از این اتصال در نوت‌بوک‌ها یا برنامه‌های خود برای استخراج متن از تصاویر استفاده کنید که پس از آن می‌تواند برای ترجمه به مدل Azure OpenAI ارسال شود.

## جمع‌آوری اطلاعات اعتبارسنجی شما

تا اینجا باید موارد زیر را جمع‌آوری کرده باشید:

**برای Azure OpenAI (ترجمه متن):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (مثلاً `gpt-4o`)
- Azure OpenAI Deployment Name (مثلاً `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**برای Azure AI Services (استخراج متن تصویر از طریق Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### مثال: پیکربندی متغیر محیطی (پیش‌نمایش)

بعداً، هنگام ساخت برنامه خود، احتمالاً آن را با استفاده از این اطلاعات اعتبارسنجی پیکربندی خواهید کرد. برای مثال، ممکن است آنها را به صورت متغیرهای محیطی به شکل زیر تنظیم کنید:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-12-01-preview
```

---

### مطالعه بیشتر

- [چگونه یک پروژه در Azure AI Foundry ایجاد کنیم](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [چگونه منابع Azure AI را ایجاد کنیم](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [چگونه مدل‌های OpenAI را در Azure AI Foundry مستقر کنیم](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

Sure! Could you please specify which language "my" refers to? For example, is it Burmese (Myanmar), Malay, or another language?