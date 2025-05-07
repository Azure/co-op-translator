<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:13:45+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ar"
}
-->
# إنشاء ملف *.env* في الدليل الرئيسي

في هذا الدرس، سنرشدك خلال إعداد متغيرات البيئة الخاصة بك لخدمات Azure باستخدام ملف *.env*. تتيح لك متغيرات البيئة إدارة بيانات الاعتماد الحساسة بأمان، مثل مفاتيح API، دون الحاجة إلى تضمينها مباشرة في قاعدة الكود الخاصة بك.

> [!IMPORTANT]
> - يلزم تكوين خدمة نموذج لغة واحدة فقط (Azure OpenAI أو OpenAI). املأ متغيرات البيئة للخدمة التي تفضلها. إذا تم تعيين متغيرات بيئة لعدة نماذج لغوية، سيختار المترجم التعاوني واحدة بناءً على الأولوية.
> - إذا لم يتم تعيين متغيرات بيئة Computer Vision، سينتقل المترجم تلقائيًا إلى [وضع Markdown فقط](./markdown-only-mode.md).

> [!NOTE]
> يركز هذا الدليل بشكل أساسي على خدمات Azure، لكن يمكنك اختيار أي نموذج لغة مدعوم من [قائمة النماذج والخدمات المدعومة](../README.md#-supported-models-and-services).

## إنشاء ملف *.env*

في الدليل الرئيسي لمشروعك، أنشئ ملفًا باسم *.env*. سيحتوي هذا الملف على جميع متغيرات البيئة الخاصة بك بتنسيق بسيط.

> [!WARNING]
> لا تقم بإضافة ملف *.env* إلى أنظمة التحكم في الإصدارات مثل Git. أضف *.env* إلى ملف .gitignore الخاص بك لتجنب الالتزام العرضي.

1. انتقل إلى الدليل الرئيسي لمشروعك.

1. أنشئ ملف *.env* في الدليل الرئيسي لمشروعك.

1. افتح ملف *.env* والصق النموذج التالي:

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
> إذا كنت ترغب في العثور على مفاتيح API ونقاط النهاية الخاصة بك، يمكنك الرجوع إلى [set-up-azure-ai.md](../set-up-azure-ai.md).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الحساسة، يُنصح بالاعتماد على الترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.