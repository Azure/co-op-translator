<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:25:32+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ar"
}
-->
# المساهمة في Co-op Translator

يرحب هذا المشروع بالمساهمات والاقتراحات. تتطلب معظم المساهمات موافقتك على اتفاقية ترخيص المساهمين (CLA) التي تُعلن فيها بأن لديك الحق في منحنا حقوق استخدام مساهمتك، وأنك فعلًا تمنحنا هذه الحقوق. لمزيد من التفاصيل، زر https://cla.opensource.microsoft.com.

عند تقديم طلب سحب، سيقوم بوت CLA تلقائيًا بتحديد ما إذا كنت بحاجة لتوفير CLA وتزيين طلب السحب بشكل مناسب (مثل فحص الحالة، تعليق). ما عليك سوى اتباع التعليمات التي يقدمها البوت. ستحتاج إلى القيام بذلك مرة واحدة فقط عبر جميع المستودعات التي تستخدم اتفاقيتنا.

## إعداد بيئة التطوير

لإعداد بيئة التطوير لهذا المشروع، نوصي باستخدام Poetry لإدارة التبعيات. نستخدم `pyproject.toml` لإدارة تبعيات المشروع، وبالتالي لتثبيت التبعيات، يجب عليك استخدام Poetry.

### إنشاء بيئة افتراضية

#### باستخدام pip

```bash
python -m venv .venv
```

#### باستخدام Poetry

```bash
poetry init
```

### تفعيل البيئة الافتراضية

#### لكل من pip و Poetry

- ويندوز:

    ```bash
    .venv\Scripts\activate.bat
    ```

- ماك/لينكس:

    ```bash
    source .venv/bin/activate
    ```

#### باستخدام Poetry

```bash
poetry shell
```

### تثبيت الحزمة والحزم المطلوبة

#### باستخدام Poetry (من pyproject.toml)

```bash
poetry install
```

### الاختبار اليدوي

قبل تقديم طلب السحب، من المهم اختبار وظيفة الترجمة باستخدام وثائق حقيقية:

1. أنشئ مجلد اختبار في المجلد الجذر:
    ```bash
    mkdir test_docs
    ```

2. انسخ بعض وثائق الماركدوان والصور التي تريد ترجمتها إلى مجلد الاختبار. على سبيل المثال:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. ثبت الحزمة محليًا:
    ```bash
    pip install -e .
    ```

4. شغّل Co-op Translator على مستندات الاختبار الخاصة بك:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. تحقق من الملفات المترجمة في ملف `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. املأ متغيرات البيئة كما هو موضح.

> [!TIP]
>
> ### خيارات إضافية لبيئة التطوير
>
> بالإضافة إلى تشغيل المشروع محليًا، يمكنك أيضًا استخدام GitHub Codespaces أو VS Code Dev Containers كخيارات بديلة لإعداد بيئة التطوير.
>
> #### GitHub Codespaces
>
> يمكنك تشغيل هذه العينات افتراضيًا باستخدام GitHub Codespaces ولا تحتاج إلى أي إعدادات إضافية.
>
> سيفتح الزر مثيل VS Code قائم على الويب في متصفحك:
>
> 1. افتح القالب (قد يستغرق عدة دقائق):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### التشغيل محليًا باستخدام VS Code Dev Containers
>
> ⚠️ هذا الخيار سيعمل فقط إذا كان Docker Desktop مخصصًا له على الأقل 16 جيجابايت من الذاكرة العشوائية. إذا كانت الذاكرة أقل من 16 جيجابايت، يمكنك تجربة خيار [GitHub Codespaces](../..) أو [إعداده محليًا](../..).
>
> خيار ذو صلة هو VS Code Dev Containers، الذي سيفتح المشروع في VS Code المحلي باستخدام [امتداد Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. شغّل Docker Desktop (وثبته إذا لم يكن مثبتًا)
> 2. افتح المشروع:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### نمط كتابة الكود

نستخدم [Black](https://github.com/psf/black) كمنسق كود بايثون للحفاظ على نمط كود موحد عبر المشروع. Black هو منسق كود صارم يعيد تنسيق كود بايثون تلقائيًا ليتوافق مع نمط Black.

#### التهيئة

يتم تحديد تهيئة Black في `pyproject.toml` الخاص بنا:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### تثبيت Black

يمكنك تثبيت Black باستخدام Poetry (موصى به) أو pip:

##### باستخدام Poetry

يتم تثبيت Black تلقائيًا عند إعداد بيئة التطوير:
```bash
poetry install
```

##### باستخدام pip

إذا كنت تستخدم pip، يمكنك تثبيت Black مباشرة:
```bash
pip install black
```

#### استخدام Black

##### مع Poetry

1. نسق جميع ملفات بايثون في المشروع:
    ```bash
    poetry run black .
    ```

2. نسق ملف أو مجلد محدد:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### مع pip

1. نسق جميع ملفات بايثون في المشروع:
    ```bash
    black .
    ```

2. نسق ملف أو مجلد محدد:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> نوصي بضبط محررك ليقوم تلقائيًا بتنسيق الكود باستخدام Black عند الحفظ. معظم المحررات الحديثة تدعم ذلك عبر الإضافات أو البلجنات.

## تشغيل Co-op Translator

لتشغيل Co-op Translator باستخدام Poetry في بيئتك، اتبع الخطوات التالية:

1. انتقل إلى المجلد حيث تريد إجراء اختبارات الترجمة أو أنشئ مجلدًا مؤقتًا لأغراض الاختبار.

2. نفذ الأمر التالي. يشير العلم `-l ko` with the language code you wish to translate into. The `-d` إلى وضع التصحيح.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> تأكد من تفعيل بيئة Poetry (poetry shell) قبل تشغيل الأمر.

## المسؤولون عن الصيانة

### رسالة الالتزام واستراتيجية الدمج

لضمان الاتساق والوضوح في سجل الالتزام الخاص بمشروعنا، نتبع تنسيقًا محددًا لرسائل الالتزام **لرسالة الالتزام النهائية** عند استخدام استراتيجية **Squash and Merge**.

عند دمج طلب سحب، يتم دمج الالتزامات الفردية في التزام واحد. يجب أن تتبع رسالة الالتزام النهائية التنسيق أدناه للحفاظ على سجل نظيف ومتسق.

#### تنسيق رسالة الالتزام (لـ squash and merge)

نستخدم التنسيق التالي لرسائل الالتزام:

```bash
<type>: <description> (#<PR number>)
```

- **type**: يحدد فئة الالتزام. نستخدم الأنواع التالية:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.