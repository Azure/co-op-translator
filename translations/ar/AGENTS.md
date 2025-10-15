<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:20:18+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ar"
}
-->
## نظرة عامة على المشروع

Co‑op Translator هو أداة سطر أوامر بايثون وتدفق عمل GitHub Actions لترجمة ملفات Markdown، دفاتر Jupyter، ونصوص الصور إلى عدة لغات. ينظم المخرجات ضمن مجلدات خاصة بكل لغة ويحافظ على تزامن الترجمات مع المحتوى الأصلي. المشروع منظم كمكتبة تُدار عبر Poetry مع نقاط دخول CLI.

### نظرة عامة على البنية

- نقاط دخول CLI (`translate`, `migrate-links`, `evaluate`) تستدعي CLI موحد يوجه إلى تدفقات الترجمة، ترحيل الروابط، والتقييم.
- محمل الإعدادات يقرأ ملف `.env` ويكتشف تلقائياً مزود LLM (Azure OpenAI أو OpenAI) وإذا طُلب، مزود الرؤية (Azure AI Service) لاستخراج نص الصور.
- نواة الترجمة تتعامل مع Markdown ودفاتر Jupyter؛ خط أنابيب الرؤية يستخرج النص من الصور عند استخدام `-img`.
- يتم تنظيم المخرجات في `translations/<lang>/` للنصوص و`translated_images/` للصور، مع الحفاظ على البنية الأصلية.

### التقنيات والأطر الأساسية

- بايثون 3.10–3.12، Poetry للإدارة والتغليف
- CLI: مكتبة `click`
- حزم LLM/AI: Azure OpenAI، OpenAI
- الرؤية: Azure AI Service (Computer Vision)
- HTTP والبيانات: `httpx`, `pydantic`
- معالجة الصور: `pillow`, `opencv-python`, `matplotlib`
- الأدوات: `pytest`, `black`, `ruff`

## أوامر الإعداد

### المتطلبات الأساسية

- بايثون 3.10–3.12
- اشتراك Azure (اختياري، لخدمات Azure AI)
- اتصال بالإنترنت للوصول إلى واجهات LLM/Vision (مثل Azure OpenAI/OpenAI، Azure AI Vision)

### الخيار أ: Poetry (موصى به)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### الخيار ب: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## استخدام المستخدم النهائي

### Docker (صورة منشورة)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

ملاحظات:
- نقطة الدخول الافتراضية هي `translate`. يمكن تجاوزها بـ `--entrypoint migrate-links` لترحيل الروابط.
- تأكد من أن حزمة GHCR مرئية للعامة للسحب المجهول.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### إعداد البيئة

أنشئ ملف `.env` في جذر المستودع ووفّر بيانات الاعتماد/نقاط النهاية لنموذج اللغة الذي اخترته و(اختياريًا) خدمة الرؤية. لإعداد مزود معين، راجع `getting_started/set-up-azure-ai.md`.

### متغيرات البيئة المطلوبة

يجب تكوين مزود LLM واحد على الأقل. لترجمة الصور، يجب أيضًا تكوين Azure AI Service.

- Azure OpenAI (ترجمة نصية):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (بديل للترجمة النصية):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (اختياري)
  - `OPENAI_CHAT_MODEL_ID` (مطلوب عند استخدام مزود OpenAI)
  - `OPENAI_BASE_URL` (اختياري؛ الافتراضي `https://api.openai.com/v1`)

- Azure AI Service لاستخراج نص الصور (مطلوب عند استخدام `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (مفضل) أو `AZURE_SUBSCRIPTION_KEY` القديمة
  - `AZURE_AI_SERVICE_ENDPOINT`

مثال على جزء من ملف `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

ملاحظات:

- الأداة تكتشف تلقائياً مزود LLM المتاح؛ قم بتكوين Azure OpenAI أو OpenAI.
- ترجمة الصور تتطلب كل من `AZURE_AI_SERVICE_API_KEY` و`AZURE_AI_SERVICE_ENDPOINT`.
- سيظهر خطأ واضح في CLI إذا كانت المتغيرات المطلوبة مفقودة.

## سير عمل التطوير

- الشيفرة المصدرية موجودة تحت `src/co_op_translator`؛ الاختبارات تحت `tests/`.
- CLIs الأساسية (مثبتة عبر نقاط الدخول):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

راجع مستندات الاستخدام الإضافية في `getting_started/`.

## تعليمات الاختبار

شغّل الاختبارات من جذر المستودع. بعض الاختبارات قد تتطلب بيانات اعتماد API؛ تخطها عند الحاجة.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

تغطية اختيارية (تتطلب `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## إرشادات أسلوب الشيفرة

- المنسق: Black (مضبوط في `pyproject.toml`، طول السطر 88)
- المدقق: Ruff (مضبوط في `pyproject.toml`، طول السطر 120)
- فحوصات النوع: mypy (الإعداد موجود؛ فعّل إذا كان مثبتاً)

الأوامر:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

نظم مصادر بايثون تحت `src/`، والاختبارات تحت `tests/`، ويفضل الاستيراد الصريح ضمن مساحة الحزمة (`co_op_translator.*`).

## البناء والنشر

يتم نشر نواتج البناء إلى `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

يتم دعم الأتمتة عبر GitHub Actions؛ راجع:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### صورة الحاوية (GHCR)

- الصورة الرسمية: `ghcr.io/azure/co-op-translator:<tag>`
- العلامات: `latest` (على main)، علامات دلالية مثل `vX.Y.Z`، وعلامة `sha`
- تعدد المعماريات: `linux/amd64, linux/arm64` مدعومة عبر Buildx
- نمط Dockerfile: بناء عجلات الاعتماديات في مرحلة البناء (مع `build-essential` و`python3-dev`) وتثبيتها من wheelhouse المحلي في وقت التشغيل (`pip install --no-index --find-links=/wheels`)
- سير العمل: `.github/workflows/docker-publish.yml` يبني ويدفع إلى GHCR

## اعتبارات الأمان

- احتفظ بمفاتيح API ونقاط النهاية في `.env` أو في مخزن أسرار CI الخاص بك؛ لا تقم أبداً برفع الأسرار.
- لترجمة الصور، مفاتيح/نقاط نهاية Azure AI Vision مطلوبة؛ وإلا تجاهل `-img`.
- تحقق من حصص المزود/حدود المعدل عند تشغيل دفعات ترجمة كبيرة.

## إرشادات طلبات السحب

### قبل الإرسال

1. **اختبر تغييراتك:**
   - شغّل الدفاتر المتأثرة بالكامل
   - تحقق من تنفيذ جميع الخلايا بدون أخطاء
   - تأكد من أن المخرجات مناسبة

2. **تحديثات التوثيق:**
   - حدّث `README.md` إذا أضفت مفاهيم جديدة
   - أضف تعليقات في الدفاتر للشيفرة المعقدة
   - تأكد من أن خلايا markdown تشرح الغرض

3. **تغييرات الملفات:**
   - تجنب رفع ملفات `.env` (استخدم `.env.example`)
   - لا ترفع مجلدات `venv/` أو `__pycache__/`
   - احتفظ بمخرجات الدفاتر عندما توضح مفاهيم
   - احذف الملفات المؤقتة ودفاتر النسخ الاحتياطي (`*-backup.ipynb`)

4. **الأسلوب والتنسيق:**
   - اتبع إرشادات الأسلوب والتنسيق
   - شغّل `poetry run black .` و`poetry run ruff check .` للتحقق من مشاكل الأسلوب والتنسيق

5. **إضافة/تحديث الاختبارات ومساعدة CLI:**
   - أضف أو حدّث الاختبارات عند تغيير السلوك
   - حافظ على مساعدة CLI متسقة مع التغييرات


### رسالة الالتزام واستراتيجية الدمج

نستخدم Squash and Merge كإعداد افتراضي. يجب أن تتبع رسالة الالتزام النهائية بعد الدمج النمط التالي:

```bash
<type>: <description> (#<PR number>)
```

الأنواع المسموحة:
- `Docs` — تحديثات التوثيق
- `Build` — نظام البناء، الاعتماديات، الإعدادات/CI
- `Core` — الوظائف الأساسية والميزات (مثلاً: `src/co_op_translator/core`)

أمثلة:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

ملاحظات:
- غالباً ما يتم إضافة بادئة تلقائياً لعناوين PR بناءً على التصنيفات؛ تحقق من صحة البادئة المولدة.

### تنسيق عنوان PR

استخدم عناوين واضحة وموجزة. ويفضل نفس بنية رسالة الالتزام النهائية:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## تصحيح الأخطاء واستكشاف المشاكل

- المشاكل الشائعة وحلولها: `getting_started/troubleshooting.md`
- اللغات المدعومة والملاحظات (بما في ذلك الخطوط/المشاكل المعروفة): `getting_started/supported-languages.md`
- لمشاكل الروابط في الدفاتر، أعد التشغيل: `migrate-links -l "all" -y`

## ملاحظات للوكلاء

- يفضل استخدام Poetry لبيئات قابلة لإعادة الإنتاج؛ وإلا استخدم `requirements.txt`.
- عند استدعاء CLIs في CI، وفّر الأسرار المطلوبة عبر متغيرات البيئة أو حقن `.env`.
- لمستهلكي monorepo، هذا المستودع يعمل كحزمة مستقلة؛ لا حاجة لتنسيق الحزم الفرعية.

- إرشادات تعدد المعماريات: احتفظ بـ `linux/arm64` عندما يكون مستخدمو ARM (Apple Silicon/خوادم ARM) هدفاً؛ وإلا فإن `linux/amd64` فقط مقبول للبساطة.
- وجّه المستخدمين إلى دليل البدء السريع لـ Docker في `README.md` إذا فضلوا استخدام الحاويات؛ أدرج نسخ Bash وPowerShell بسبب اختلاف علامات الاقتباس.

---

**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي والمعتمد. بالنسبة للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.