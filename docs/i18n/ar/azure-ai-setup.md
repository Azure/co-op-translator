# إعداد Azure AI

استخدم هذا الدليل عندما تريد تكوين Azure OpenAI لترجمة النصوص وAzure AI Vision لاستخراج نص الصورة.

## المتطلبات الأساسية

- اشتراك في Azure.
- إذن لإنشاء أو استخدام موارد Azure AI ونشر النماذج.
- مشروع في Azure AI Foundry أو وصول مكافئ إلى موارد Azure OpenAI وAzure AI Vision.

## إنشاء مشروع Azure AI

1. افتح [Azure AI Foundry](https://ai.azure.com).
2. أنشئ مشروعًا أو اختر مشروعًا موجودًا.
3. أنشئ أو اختر AI hub للمشروع.
4. افتح نظرة عامة على المشروع بعد الإنشاء.

## نشر نموذج Azure OpenAI

1. داخل المشروع، افتح **Models + endpoints**.
2. حدد **Deploy model**.
3. اختر نموذج GPT مثل `gpt-4o`.
4. انشر النموذج.
5. سجّل نقطة النهاية واسم النشر واسم النموذج ومفتاح API وإصدار API.

!!! note
    إصدار واجهة برمجة تطبيقات Azure OpenAI منفصل عن إصدار النموذج المعروض في Azure AI Foundry. اختر إصدار واجهة برمجة تطبيقات مدعومًا لنشرك.

## تكوين Azure AI Vision

تستخدم ترجمة الصور Azure AI Vision لاستخراج النص من الصور المصدر قبل ترجمة النص.

في مشروع Azure AI الخاص بك، ابحث عن مفتاح خدمة Azure AI ونقطة النهاية.

![Find Azure AI service information](../../assets/find-azure-ai-info.png)

سجّل:

- نقطة نهاية خدمة Azure AI
- مفتاح API لخدمة Azure AI

## متغيرات البيئة

أضف بيانات الاعتماد إلى ملف `.env` الخاص بك أو أسرار CI.

```bash
# Azure AI Vision، مطلوب لترجمة الصور
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI، مطلوب لترجمة النصوص
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

يدعم Co-op Translator أيضًا مجموعات بيانات اعتماد بديلة اختيارية. انسخ مجموعة مزود كاملة مع لاحقات مثل `_1` أو `_2`; يجب أن تشترك جميع المتغيرات في مجموعة بديلة في نفس اللاحقة.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## الخطوات التالية

- ارجع إلى [التكوين](configuration.md) لإعداد متغيرات بيئة محلية أو في CI.
- استخدم [مرجع CLI](cli.md) لأوامر الترجمة.
- استخدم [GitHub Actions](github-actions.md) لأتمتة طلبات السحب للترجمة.