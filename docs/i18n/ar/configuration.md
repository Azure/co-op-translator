# التكوين

يتطلب Co-op Translator مزود نموذج لغوي واحد. تتطلب ترجمة الصور أيضًا Azure AI Vision.

يُقرأ التكوين من متغيرات البيئة. بالنسبة للمشاريع المحلية، ضعها في ملف `.env` في جذر المشروع.

لإعداد موارد Azure، راجع [إعداد Azure AI](azure-ai-setup.md).

## إعداد وقت التشغيل المحلي

استخدم بيئة افتراضية قبل تشغيل واجهة الأوامر محليًا. يدعم Co-op Translator Python 3.11 إلى 3.14.

لاستخدام واجهة الأوامر العادي، ثبّت الحزمة المنشورة داخل بيئة افتراضية:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### تطوير المستودع

لتطوير المستودع، ثبّت التبعيات من جذر المشروع بدلًا من ذلك:

```bash
poetry install
poetry run translate --help
```

بعد أن تصبح واجهة الأوامر متاحة، قم بتكوين مزود نموذج لغوي واحد في ملف `.env`.

## اختيار المزود

تكتشف الأداة المزودين تلقائيًا بالترتيب التالي:

1. Azure OpenAI
2. OpenAI
3. Anthropic

تتطلب الترجمة بيانات اعتماد المزود، باستثناء المعاينات مثل `translate -l "ko" -md --dry-run`. تُعد `migrate-links` و `co-op-review` و `run_review` عمليات صيانة حتمية ولا تحتاج إلى بيانات اعتماد المزود.

## الواجهة الخلفية لعميل النموذج

بدءًا من Co-op Translator 0.22.0، تستخدم Azure OpenAI وOpenAI وAnthropic إطار عمل Microsoft Agent افتراضيًا. لا يلزم إعداد واجهة خلفية للاستخدام الاعتيادي.

يبقى Semantic Kernel متاحًا مؤقتًا من أجل التوافق. لاختياره صراحةً، اضبط:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

يُصدر استخدام Semantic Kernel تحذير إلغاء الدعم. من المخطط أن تنقل الحزمة Semantic Kernel إلى تبعية اختيارية في الإصدار 0.23.0 وتزيل التكامل في 0.24.0، وذلك رهناً بنتائج التوافق وردود فعل المستخدمين. تتطلب Anthropic `agent-framework`; اختيار `semantic-kernel` صراحةً مع Anthropic يفشل بخطأ في التكوين. القيم غير الصالحة تفشل أثناء تهيئة المترجم المعتمد على المزود بدلاً من الرجوع الصامت إلى قيمة أخرى. تابع عملية النشر وابلِغ عن العوائق في [المشكلة على GitHub رقم 543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

استخدم Azure OpenAI عندما يكون نموذجك منشورًا في Azure AI Foundry أو خدمة Azure OpenAI.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

يستخدم فحص الاتصال نقطة النهاية ومفتاح API وإصدار API واسم النشر قبل بدء الترجمة.

## OpenAI

استخدم OpenAI عند استدعاء OpenAI API مباشرةً.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` مطلوب لأن المترجم يحتاج نموذج محادثة صريح لاستدعاءات API.

اترك `OPENAI_ORG_ID` و `OPENAI_BASE_URL` غير مضبوطتين للإعداد الافتراضي. أضف معرف منظمة فقط إذا كان حسابك بحاجة إليه، أو `OPENAI_BASE_URL` فقط عند استخدام نقطة نهاية مخصصة. لا تنسخ القيم النائبة للإعدادات الاختيارية.

## Anthropic Claude

استخدم Anthropic عند استدعاء Claude API مباشرةً. أنشئ [مفتاح API لـ Anthropic](https://platform.claude.com/docs/en/get-started) واختر [معرّف نموذج Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) المدعوم.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` و `ANTHROPIC_MODEL` مطلوبان. لا تحتاج إلى ضبط `CO_OP_TRANSLATOR_MODEL_CLIENT`; إطار عمل Agent هو الواجهة الخلفية الافتراضية.

اترك `ANTHROPIC_BASE_URL` غير مضبوط لواجهة Anthropic API. اضبطه فقط عند استخدام نقطة نهاية مخصصة.

`ANTHROPIC_MAX_TOKENS` الافتراضي هو `8192`، مما يترك مجالًا للنصوص الكثيفة بالرموز مثل Meitei Mayek. خفّضه إذا كان نموذجك أو نقطة نهاية متوافقة مع Anthropic تحدّ الإخراج دون ذلك.

## Azure AI Vision

تتطلب ترجمة الصور Azure AI Vision حتى تتمكن الأداة من استخراج النصوص من الصور قبل أن يترجمها نموذج اللغة المُكوّن. يمكن لـ Anthropic ترجمة النص المستخرج بنفس طريقة Azure OpenAI أو OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

إذا تم اختيار ترجمة الصور باستخدام `-img` أو `images=True` أو بدون عامل تصفية لنوع المحتوى، فإن الأداة تتحقق من صحة تكوين Vision قبل بدء الترجمة.

## مجموعات بيانات اعتماد متعددة

تدعم طبقة التكوين مجموعات بيانات اعتماد متعددة عن طريق إضافة لاحقات إلى المتغيرات بنفس الفهرس:

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

يجب أن تكون كل مجموعة كاملة. يختار فحص الصحة مجموعة عاملة قبل المضي قدمًا في الترجمة.

تدعم OpenAI وAnthropic نفس اتفاقية اللاحقات. احتفظ بكل متغير في مجموعة بيانات الاعتماد على نفس اللاحقة، بما في ذلك القيم الاختيارية مثل `OPENAI_BASE_URL_1` أو `ANTHROPIC_BASE_URL_1`.

## متطلبات الأوامر

| الأمر أو API | يتطلب LLM | يتطلب Vision | ملاحظات |
| --- | --- | --- | --- |
| `translate -md` | نعم | لا | يترجم Markdown فقط. |
| `translate -nb` | نعم | لا | يترجم دفاتر الملاحظات فقط. |
| `translate -img` | نعم | نعم | يترجم الصور فقط. |
| `translate` بدون علامات نوع | نعم | نعم | الوضع الافتراضي يتضمن Markdown ودفاتر الملاحظات والصور. |
| `evaluate` | نعم | لا | يستخدم تقييم LLM ما لم يُحدد `--fast`. |
| `migrate-links` | لا | لا | يقوم بترحيل الروابط محليًا دون استدعاءات للمزود. |
| `co-op-review` | لا | لا | يشغّل اختبارات بنية الترجمة الحتمية، حداثة المحتوى، Markdown، دفاتر الملاحظات، وفحوصات الروابط المحلية. |
| `run_translation(markdown=True)` | نعم | لا | ترجمة Markdown برمجياً. |
| `run_translation(images=True)` | نعم | نعم | ترجمة الصور برمجياً. |
| `run_review(...)` | لا | لا | مراجعة حتمية برمجية. |

## مجلدات الإخراج

مخرجات الترجمة النصية الافتراضية:

```text
translations/<language-code>/<source-relative-path>
```

مخرجات الصور المترجمة الافتراضية:

```text
translated_images/<language-code>/<source-relative-path>
```

يمكن لواجهة برمجة Python تجاوز هذه المجلدات باستخدام `translations_dir` و `image_dir`.