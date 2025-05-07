<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:20:04+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "ar"
}
-->
# إعداد Azure AI لمترجم التعاون (Azure OpenAI و Azure AI Vision)

يرشدك هذا الدليل خلال إعداد Azure OpenAI لترجمة اللغات وAzure Computer Vision لتحليل محتوى الصور (الذي يمكن استخدامه لاحقًا للترجمة المعتمدة على الصور) ضمن Azure AI Foundry.

**المتطلبات الأساسية:**
- حساب Azure مع اشتراك نشط.
- أذونات كافية لإنشاء الموارد والنشر ضمن اشتراك Azure الخاص بك.

## إنشاء مشروع Azure AI

ستبدأ بإنشاء مشروع Azure AI، الذي يعمل كمكان مركزي لإدارة موارد الذكاء الاصطناعي الخاصة بك.

1. انتقل إلى [https://ai.azure.com](https://ai.azure.com) وسجل الدخول باستخدام حساب Azure الخاص بك.

1. اختر **+Create** لإنشاء مشروع جديد.

1. قم بالمهام التالية:
   - أدخل **اسم المشروع** (مثل `CoopTranslator-Project`).
   - اختر **مركز الذكاء الاصطناعي** (مثل `CoopTranslator-Hub`) (أنشئ واحدًا جديدًا إذا لزم الأمر).

1. اضغط على "**Review and Create**" لإعداد مشروعك. سيتم توجيهك إلى صفحة نظرة عامة على المشروع.

## إعداد Azure OpenAI لترجمة اللغات

داخل مشروعك، ستقوم بنشر نموذج Azure OpenAI ليكون بمثابة الخلفية لترجمة النصوص.

### انتقل إلى مشروعك

إذا لم تكن هناك بالفعل، افتح مشروعك الجديد (مثل `CoopTranslator-Project`) في Azure AI Foundry.

### نشر نموذج OpenAI

1. من قائمة مشروعك الجانبية، تحت "My assets"، اختر "**Models + endpoints**".

1. اختر **+ Deploy model**.

1. اختر **Deploy Base Model**.

1. ستظهر لك قائمة بالنماذج المتاحة. قم بتصفية أو البحث عن نموذج GPT مناسب. نوصي بـ `gpt-4o`.

1. اختر النموذج الذي تريده واضغط على **Confirm**.

1. اختر **Deploy**.

### تكوين Azure OpenAI

بعد النشر، يمكنك اختيار النشر من صفحة "**Models + endpoints**" للعثور على **REST endpoint URL**، **Key**، **اسم النشر**، **اسم النموذج** و**إصدار API**. ستحتاج هذه المعلومات لدمج نموذج الترجمة في تطبيقك.

## إعداد Azure Computer Vision لترجمة الصور

لتمكين ترجمة النصوص داخل الصور، تحتاج إلى العثور على مفتاح API ونقطة النهاية لخدمة Azure AI.

1. انتقل إلى مشروع Azure AI الخاص بك (مثل `CoopTranslator-Project`). تأكد من أنك في صفحة نظرة عامة على المشروع.

### تكوين خدمة Azure AI

ابحث عن مفتاح API ونقطة النهاية من خدمة Azure AI.

1. انتقل إلى مشروع Azure AI الخاص بك (مثل `CoopTranslator-Project`). تأكد من أنك في صفحة نظرة عامة على المشروع.

1. ابحث عن **API Key** و **Endpoint** في علامة تبويب خدمة Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

هذا الاتصال يجعل قدرات مورد خدمات Azure AI المرتبط (بما في ذلك تحليل الصور) متاحة لمشروع AI Foundry الخاص بك. يمكنك بعد ذلك استخدام هذا الاتصال في دفاتر الملاحظات أو التطبيقات الخاصة بك لاستخراج النصوص من الصور، والتي يمكن إرسالها بعد ذلك إلى نموذج Azure OpenAI للترجمة.

## تجميع بيانات الاعتماد الخاصة بك

بحلول الآن، يجب أن تكون جمعت ما يلي:

**لـ Azure OpenAI (ترجمة النصوص):**
- نقطة نهاية Azure OpenAI
- مفتاح API الخاص بـ Azure OpenAI
- اسم نموذج Azure OpenAI (مثل `gpt-4o`)
- اسم نشر Azure OpenAI (مثل `cooptranslator-gpt4o`)
- إصدار API الخاص بـ Azure OpenAI

**لخدمات Azure AI (استخراج نص الصور عبر الرؤية):**
- نقطة نهاية خدمة Azure AI
- مفتاح API لخدمة Azure AI

### مثال: تكوين متغيرات البيئة (معاينة)

لاحقًا، عند بناء تطبيقك، من المحتمل أن تقوم بتكوينه باستخدام بيانات الاعتماد التي جمعتها. على سبيل المثال، قد تقوم بتعيينها كمتغيرات بيئة على النحو التالي:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### قراءة إضافية

- [كيفية إنشاء مشروع في Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [كيفية إنشاء موارد Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [كيفية نشر نماذج OpenAI في Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الهامة، يُنصح بالاستعانة بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.