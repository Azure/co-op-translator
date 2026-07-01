# التكوين

يتطلب Co-op Translator مزود نموذج لغة واحد. تتطلب ترجمة الصور أيضاً Azure AI Vision.

يُقرأ التكوين من متغيرات البيئة. لمشاريع محلية، ضعها في ملف `.env` في جذر المشروع.

لمعرفة إعداد موارد Azure، راجع [إعداد Azure AI](azure-ai-setup.md).

## إعداد التشغيل المحلي

استخدم بيئة افتراضية قبل تشغيل واجهة الأوامر محلياً. يدعم Co-op Translator بايثون 3.10 حتى 3.12.

لاستخدام واجهة الأوامر العادي، ثبّت الحزمة المنشورة داخل بيئة افتراضية:

=== "ويندوز"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / لينكس"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

لتطوير المستودع، ثبّت التبعيات من جذر المشروع بدلاً من ذلك:

```bash
poetry install
poetry run translate --help
```

بعد توافر واجهة الأوامر، قم بتكوين مزود نموذج لغة واحد في `.env`.

## اختيار المزود

تكتشف الأداة المزودين تلقائياً بالترتيب التالي:

1. Azure OpenAI
2. OpenAI

إذا لم يتم تكوين أي من المزودين، فإن `translate`, `evaluate`, `migrate-links`, و`run_translation` ستفشل أثناء فحوصات التكوين. `co-op-review` و`run_review` عبارة عن فحوصات صيانة حتمية ولا تتطلب بيانات اعتماد المزود.

## Azure OpenAI

استخدم Azure OpenAI عندما يتم نشر نموذجك في Azure AI Foundry أو خدمة Azure OpenAI.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

يفحص اختبار الاتصال نقطة النهاية ومفتاح الـ API وإصدار الـ API واسم النشر قبل بدء الترجمة.

## OpenAI

استخدم OpenAI عند استدعاء OpenAI API مباشرةً.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # اختياري
OPENAI_BASE_URL="..."        # اختياري
```

مطلوب `OPENAI_CHAT_MODEL_ID` لأن المترجم يحتاج نموذج دردشة صريح لاستدعاءات الـ API.

## Azure AI Vision

تتطلب ترجمة الصور Azure AI Vision حتى تتمكن الأداة من استخراج النص من الصور قبل ترجمته.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

إذا تم اختيار ترجمة الصور باستخدام `-img`, `images=True`, أو عدم وجود فلتر لنوع المحتوى، فإن الأداة تتحقق من تكوين Vision قبل بدء الترجمة.

## مجموعات بيانات الاعتماد المتعددة

تدعم طبقة التكوين مجموعات متعددة من بيانات الاعتماد عن طريق إضافة لاحقة ذات الفهرس نفسه إلى المتغيرات:

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

يجب أن تكون كل مجموعة مكتملة. يختار فحص الصحة مجموعة عاملة قبل متابعة الترجمة.

## متطلبات الأوامر

| الأمر أو API | يتطلب LLM | يتطلب Vision | ملاحظات |
| --- | --- | --- | --- |
| `translate -md` | نعم | لا | يترجم ملفات Markdown فقط. |
| `translate -nb` | نعم | لا | يترجم دفاتر الملاحظات فقط. |
| `translate -img` | نعم | نعم | يترجم الصور فقط. |
| `translate` مع عدم وجود أعلام نوع | نعم | نعم | الوضع الافتراضي يتضمن Markdown ودفاتر الملاحظات والصور. |
| `evaluate` | نعم | لا | يستخدم تقييم LLM ما لم يتم اختيار `--fast`. |
| `migrate-links` | نعم | لا | ينفّذ ترحيل الروابط، لكنه لا يزال يشغل فحوصات التكوين المشتركة. |
| `co-op-review` | لا | لا | يجري فحوصات حتمية لبنية الترجمة، والحداثة، وملفات Markdown، ودفاتر الملاحظات، والروابط المحلية. |
| `run_translation(markdown=True)` | نعم | لا | ترجمة Markdown برمجياً. |
| `run_translation(images=True)` | نعم | نعم | ترجمة الصور برمجياً. |
| `run_review(...)` | لا | لا | مراجعة حتمية برمجياً. |

## مجلدات الإخراج

إخراج الترجمة النصية الافتراضي:

```text
translations/<language-code>/<source-relative-path>
```

إخراج الصور المترجمة الافتراضي:

```text
translated_images/<language-code>/<source-relative-path>
```

يمكن لواجهة برمجة بايثون (Python API) تجاوز هذه المجلدات باستخدام `translations_dir` و`image_dir`.