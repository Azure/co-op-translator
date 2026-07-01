# دليل الصيانة

تلخِّص هذه الصفحة كيفية ربط API وCLI وموقع التوثيق ببعضها.

## حدود واجهة برمجة التطبيقات العامة

يتم تصدير واجهة Python المستقرة من:

```python
co_op_translator.api
```

تنظّم واجهة API العامة إلى مساعدات ترجمة المحتوى، مساعدات إعادة كتابة المسارات، تنظيم المشروع، والمراجعة:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

عند إضافة واجهات API عامة جديدة، قم بتحديث:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- اختبارات API ذات الصلة الموجودة تحت `tests/co_op_translator/`، مثل `test_api.py` أو `test_review_api.py`

تجنّب توثيق وحدات `core` منخفضة المستوى كواجهة API مستقرة ما لم يكن المشروع يعتزم دعمها مباشرة.

## نقاط الدخول الخاصة بـ CLI

تعرّف الحزمة نصوص Poetry التالية:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

يقوم `src/co_op_translator/__main__.py` بتوجيه التنفيذ حسب اسم السكريبت:

- `translate` يستدعي `co_op_translator.cli.translate.translate_command`
- `evaluate` يستدعي `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` يستدعي `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` يستدعي `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` يتجاوز `__main__.py` ويستدعي `co_op_translator.mcp.server:main` مباشرة.

عند إضافة أو تغيير خيارات CLI، قم بتحديث:

- الأمر ذي الصلة في `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- اختبارات CLI ذات الصلة، إذا تغير السلوك

## خادم MCP

تم تنفيذ خادم MCP في:

```python
co_op_translator.mcp.server
```

يغلف الخادم عمدًا واجهة Python العامة بدلاً من استدعاء وحدات `core` منخفضة المستوى. حافظ على هذه الحدود كما هي حتى تشترك عملاء MCP ومنادي Python وCLI في نفس السلوك.

عند إضافة أو تغيير أدوات MCP، قم بتحديث:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` إذا تغير سطح واجهة API العامة

أدوات ترجمة المستودع قابلة للاستدعاء عبر النموذج من خلال MCP ويمكنها كتابة العديد من الملفات. اجعل `dry_run=True` افتراضيًا واطلب `confirm_write=True` قبل ترجمة مشروع ليس في وضع `dry_run`.

## تدفق الترجمة

التدفق العام لترجمة المشروع هو:

1. تحليل وسائط CLI أو معلمات API.
2. التحقق من تكوين LLM باستخدام `LLMConfig`.
3. التحقق من Azure AI Vision عند اختيار ترجمة الصور.
4. توحيد رموز اللغات.
5. اكتشاف أسماء مجلدات اللغات القديمة.
6. تقدير حجم الترجمة.
7. تحديث أقسام اللغة/الدورة في README عند الاقتضاء.
8. تفويض ترجمة المشروع إلى `ProjectTranslator`.
9. `ProjectTranslator` يفوض معالجة الملفات إلى `TranslationManager`.

`TranslationManager` يتكون من مزيجات متخصصة لأنواع الملفات:

- `ProjectMarkdownTranslationMixin` يتولى قراءة ملفات Markdown، ترجمة المحتوى، إعادة كتابة المسارات، البيانات الوصفية، إخلاءات المسؤولية، والكتابة.
- `ProjectNotebookTranslationMixin` يتولى قراءة ملفات الدفاتر، ترجمة خلايا Markdown، إعادة كتابة المسارات، البيانات الوصفية، إخلاءات المسؤولية، والكتابة.
- `ProjectImageTranslationMixin` يتولى اكتشاف الصور، استخراج/ترجمة النص، كتابة الصور المرسومة، والبيانات الوصفية.

تتجاوز واجهات المحتوى منخفضة المستوى سير عمل المشروع:

1. `translate_markdown_content` و`translate_notebook_content` تترجمان المحتوى المخزن في الذاكرة فقط.
2. `translate_image_content` يترجم النص في صورة واحدة ويُرجع كائن صورة مرسوم.
3. `rewrite_markdown_paths` و`rewrite_notebook_paths` هما مساعدان صريحان لما بعد المعالجة. لا يقومان بأي ترجمة ولا بكتابة على مستوى المشروع.

## تدفق المراجعة

التدفق الحتمي للمراجعة هو:

1. تحليل وسائط CLI أو معلمات API.
2. توحيد رموز اللغات المطلوبة.
3. بناء هدف مراجعة واحد أو أكثر من `root_dir` أو `root_dirs` أو `groups`.
4. اختياريًا، قصر ملفات المصدر باستخدام `--changed-from`.
5. تشغيل فحوصات حتمية للبنية، حداثة الترجمة، سلامة Markdown، ومسارات الروابط/الصور المحلية.
6. طباعة إخراج نصي أو Markdown بنكهة GitHub.
7. الخروج مع فشل عند العثور على أخطاء في المراجعة.

لا يتطلب تدفق المراجعة مفاتيح API ويجب أن يظل مناسبًا لتكامل CI لطلبات السحب. يسجل سير عمل طلب السحب ملخص فحص في كل تشغيل ولا ينشر تعليق PR إلا عندما يفشل `co-op-review`.

## موقع التوثيق

يتم تكوين موقع الوثائق بواسطة:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

دليل `docs/` هو المصدر الرسمي للوثائق. لا تضف أدلة للمستخدم النهائي خارج هذا الدليل ما لم يقدم المشروع عن قصد سطح توثيق منشور آخر.

بناء محليًا:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

المعاينة محليًا:

```bash
python -m mkdocs serve
```

يُكتب الموقع المُولَّد إلى `site/`، والذي يتجاهله git.

## سير عمل GitHub Pages

يقوم `.github/workflows/docs.yml` ببناء الموقع على طلبات السحب ونشره عند الدفع إلى `main`.

يقوم سير العمل بتثبيت:

```bash
pip install -r requirements-docs.txt
```

يثبت سير عمل الوثائق سلسلة أدوات التوثيق فقط. يشير `mkdocs.yml` إلى `mkdocstrings` على `src/` بحيث يمكن عرض صفحات API العامة من شجرة المصدر دون تثبيت مجموعة الاعتماديات الزمنية الكاملة. إذا تطلبت وثائق API المستقبلية استيراد موفري وقت تشغيل اختياريين أثناء البناء، قم بتحديث كل من `.github/workflows/docs.yml` وهذا الدليل معًا.

## معيار جودة الوثائق

قبل دمج تغييرات الوثائق، قم بتشغيل:

```bash
python -m mkdocs build --strict
git diff --check
```

استخدم بناءات صارمة بحيث تفشل الروابط المعطلة، إدخالات التنقل غير الصالحة، ومشاكل عرض API في وقت مبكر.