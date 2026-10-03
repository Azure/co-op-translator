# GitHub Actions

استخدم GitHub Actions عندما تريد أن يقوم المستودع بترجمة الوثائق المتغيرة تلقائيًا وفتح طلب سحب مع المخرجات المولَّدة.

ابدأ بإعداد `GITHUB_TOKEN` القياسي، بما في ذلك لمستودعات المؤسسة حيث تسمح السياسة بذلك. انظر [إعداد تطبيق GitHub](#github-app-setup) عندما تتطلب مؤسستك هوية تطبيق أو تحتاج إلى تشغيلات سير عمل تالية تلقائية.

**تحريرات بشرية:** تعيد هذه سلاسل العمل ترجمة ملفات المصدر المتغيرة بالكامل وقد تُعيد كتابة الصياغة المحررة في ترجماتها. راجع كل طلب سحب قبل الدمج. تتطلب المحافظة على كتل Markdown لمقتبَسات التعديلات المقبولة تكاملًا مخصصًا مع [موفر حالة الترجمة لواجهة برمجة تطبيقات Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## أول طلب سحب لترجمة README

ابدأ بملف `README.md` جذر واحد ولغة هدف واحدة. يترجم هذا السريان ملفات Markdown فقط، لذا فـ Azure AI Vision ليست مطلوبة.

1. انسخ [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([عرض القالب على GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) إلى `.github/workflows/translate-readme.yml` في المستودع الذي تريد ترجمته، وقم بارتكابه إلى الفرع الافتراضي لذلك المستودع. يستخدم القالب الـ Action الجذري في `Azure/co-op-translator@main`، الذي يثبّت CLI من نفس مرجع المصدر. قفل ارتكاب مُراجَع للحصول على عمليات قابلة لإعادة الإنتاج.
2. افتح **Actions > Translate README > Run workflow**، اختر لغة، واترك **Preview only** محددة. راجع تقدير الرموز في خطوة المعاينة. المعاينة لا تستدعي موفري النماذج، ولا تكتب الترجمات، ولا تنشئ طلب سحب.
3. أضف الأسرار لموفِّر واحد [مزود النص](#prerequisites)، وقم بتمكين **السماح لـ GitHub Actions بإنشاء طلبات سحب والموافقة عليها** تحت **الإعدادات > الإجراءات > عام**. يطلب القالب `contents: write` و `pull-requests: write` لعمله؛ لا تحتاج إلى تغيير أذونات السريان الافتراضية لكل سير عمل. إذا كانت سياسة المؤسسة تمنع هذه الأذونات أو هذا الإعداد، اسأل المسؤول عن [تطبيق GitHub معتمد](#github-app-setup).
4. شغّل سريان العمل مرة أخرى مع إلغاء تحديد **Preview only**. يقوم بالمعاينة، والترجمة، وتشغيل `co-op-review --readme-only`، وينشئ أو يحدّث طلب ترجمة فقط بعد نجاح الترجمة والمراجعة. يربط ملخص السريان إلى طلب السحب.
5. راجع الصياغة وتغييرات الملفات في طلب السحب، ثم ادمجه عند الاستعداد. لا يقوم سريان العمل بالدمج تلقائيًا.

يحتوي طلب السحب على `translations/<language>/README.md` فقط وملف بيانات تعريف اللغة الخاص به. يظل README المصدر دون تغيير، وتستمر الروابط إلى المستندات الأخرى في الإشارة إلى المستندات المصدر. يسرد جسم طلب السحب الملفات المتغيرة ونتائج المراجعة الهيكلية. إذا فشلت الترجمة أو المراجعة، فافحص ملخص السريان وسجلات الخطوة الفاشلة؛ لا يتم إنشاء طلب سحب. إذا لم تكن هناك تغييرات، فلا حاجة إلى طلب سحب جديد.

**ملاحظة خاصة بالمؤسسة وCI:** تطبيق GitHub اختياري، وليس مطلبًا لملكية المؤسسة. باستخدام `GITHUB_TOKEN`، تتطلب سلاسل عمل طلب السحب لفتح أو تحديث أو إعادة فتح طلب سحب وجود مستخدم لديه صلاحية الكتابة لتحديد **Approve workflows to run**. لا تُشغّل سلاسل العمل عند الدفع بواسطة هذا الرمز. لمهام CI التالية غير المراقَبة، انظر [إعداد تطبيق GitHub](#github-app-setup) وقواعد [تشغيل سلاسل العمل](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) الخاصة بـ GitHub.

## المتطلبات المسبقة

قبل إنشاء سريان العمل، قم بتكوين أسرار خدمة AI التي تحتاجها عملية الترجمة الخاصة بك.

تتطلب ترجمة النص مزود نموذج لغوي واحد:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

تتطلب ترجمة الصور أيضًا Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

انظر [التكوين](configuration.md) و[إعداد Azure AI](azure-ai-setup.md) لتفاصيل التكوين المحلي.

## الإعداد القياسي

بعد تجربة سريان README، استخدم هذا الإعداد لترجمة ملفات Markdown في مستودع إلى عدة لغات. يجري مراجعة Markdown قبل فتح طلب السحب ولا يتطلب Azure AI Vision.

### الخطوة 1: إضافة أسرار المستودع

في المستودع الهدف، افتح **Settings** > **Secrets and variables** > **Actions**، ثم أضف أسرار الموفر التي سيستخدمها سريان العمل.

![حدد أسرار الإجراءات](../../assets/github-actions/select-setting-action.png)

### الخطوة 2: تمكين أذونات سير العمل

افتح **Settings** > **Actions** > **General**.

تحت **Workflow permissions**:

1. فعّل **السماح لـ GitHub Actions بإنشاء طلبات سحب والموافقة عليها**.
2. احفظ الإعداد.

يطلب العمل أدناه صراحةً `contents: write` و `pull-requests: write`. اترك أذونات سلاسل العمل الافتراضية للمستودع دون تغيير. إذا منعت سياسة المؤسسة إنشاء طلبات السحب، اسأل المسؤول عن [تطبيق GitHub معتمد](#github-app-setup).

### الخطوة 3: إضافة سير العمل

أنشئ `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

غيّر `TARGET_LANGUAGES` إلى اللغات التي يحتاجها مشروعك. تستخدم المراجعة واجهة برمجة تطبيقات Python للتحقق من Markdown فقط، مما يطابق خطوة الترجمة. توقف الخطأ في الترجمة أو المراجعة عن تنفيذ المهمة قبل إنشاء طلب السحب. لا يقوم سير العمل بدمج طلب السحب تلقائيًا. بالنسبة للمستودعات الكبيرة، أضف مرشحًا `paths:` تحت `on.push` حتى يعمل السريان فقط عند تغيّر الوثائق.

### اختياري: دفاتر الملاحظات والصور

بالنسبة لدفاتر الملاحظات، أضف `-nb` إلى أمر الترجمة واضبط `notebook=True` في خطوة المراجعة. بالنسبة لنص الصورة، قم بتكوين الأسرار الاثنين لـ [Azure AI Vision](#prerequisites)، ومرّرها في `env` لخطوة الترجمة، وأضف `-img` إلى الأمر، وأضف `translated_images/` إلى `add-paths` لخطوة طلب السحب. راجع الصور المترجمة بصريًا؛ لا تكفل المراجعة الحتمية دقة نص الصورة أو الدقة اللغوية.

## إعداد تطبيق GitHub

استخدم تطبيق GitHub معتمدًا عندما تتطلب مؤسستك هوية تطبيق، أو عندما يحتاج طلب السحب المولَّد إلى تشغيل CI التالي بدون خطوة موافقة `GITHUB_TOKEN`. لا يتجاوز التطبيق سياسة المؤسسة؛ يظل المسؤولون متحكمين في تثبيته وأذوناته.

### الخطوة 1: إنشاء أو تثبيت تطبيق GitHub

استخدم تطبيقًا موجودًا مقدمًا من المؤسسة عند توفره، أو أنشئ واحدًا بصلاحيات قراءة/كتابة على **Contents** و **Pull requests**. ثبّته على المستودع الهدف مع أي موافقة مطلوبة من المؤسسة.

سجّل:

- معرّف التطبيق
- محتويات المفتاح الخاص

خزّنها كأسرار في المستودع:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### الخطوة 2: إنشاء رمز تطبيق

أضف هذه الخطوة مباشرة قبل خطوة طلب السحب الموجودة. بالنسبة لقالب README، استخدم نفس شرط النجاح حتى لا تطلب المعاينات والترجمات الفاشلة رمز تطبيق:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

ثم غيّر إدخال `token` لخطوة طلب السحب الموجودة فقط إلى `${{ steps.generate_token.outputs.token }}`. اترك شرط النجاح، والفرع، ومضمون طلب السحب، و`add-paths` دون تغيير. يتم تقييد الرمز إلى المستودع الحالي افتراضيًا. عند تكييف الإعداد القياسي بدلًا من قالب README، احذف الـ `if` أعلاه: يستخدم ذلك السريان شرط النجاح الافتراضي، لذا تعمل عملية إنشاء الرمز وإنشاء طلب السحب فقط بعد نجاح الترجمة والمراجعة.

راجع [الإجراء create-github-app-token الرسمي](https://github.com/actions/create-github-app-token/tree/v2) للتثبيت وأذونات الرمز.

## حدود المشغل

لدى المشغلات المستضافة من GitHub مدة قصوى للمهام. قد تتجاوز المستودعات الكبيرة أو العديد من لغات الهدف هذا الحد.

بالنسبة لأحمال عمل الترجمة الكبيرة:

- ترجمة عدد أقل من اللغات في كل تشغيل.
- استخدم أعلام المحتوى مثل `-md`، `-nb`، أو `-img`.
- استخدم مشغّلًا مستضافًا ذاتيًا عندما يجعل حجم المستودع أو زمن استجابة النموذج المشغّلات المستضافة غير موثوقة.

## المراجعة في CI

استخدم `co-op-review` عندما يجب أن يتحقق طلب السحب من الترجمات المولّدة دون استدعاء موفري LLM أو Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` هو أمر مراجعة حتمي في الإصدار التجريبي. قد تتطور فحوصاته ومخطط مخرجاته، لكنه مصمم ليكون آمنًا لـ CI لأنه لا يكتب ملفات أو يستدعي موفري النماذج.