# دليل الصيانة

تلخّص هذه الصفحة كيفية ربط واجهة برمجة التطبيقات (API)، وسطر الأوامر (CLI)، وموقع التوثيق معًا.

## حدود واجهة برمجة التطبيقات العامة

يتم تصدير واجهة برمجة تطبيقات بايثون المستقرة من:

```python
co_op_translator.api
```

تنظم واجهة برمجة التطبيقات العامة إلى مساعدات ترجمة المحتوى، مساعدات إعادة كتابة المسارات، تنظيم المشاريع، والمراجعة:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` هو حد الاستمرارية للتكاملات المستضافة.
يجب أن يحافظ على فصل المرشحين المولدين عن القواعد المقبولة
حتى لا تصبح الترجمة غير المدمجة مصدر الحقيقة.

عند إضافة واجهات برمجة تطبيقات عامة جديدة، حدِّث ما يلي:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

تجنب توثيق وحدات `core` منخفضة المستوى كواجهة برمجة تطبيقات مستقرة ما لم يكن المشروع يعتزم دعمها مباشرة.

## نقاط دخول سطر الأوامر (CLI)

تعرّف الحزمة سكربتات Poetry التالية:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` يقوم بتوجيه حسب اسم السكربت:

- `translate` يستدعي `co_op_translator.cli.translate.translate_command`
- `evaluate` يستدعي `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` يستدعي `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` يستدعي `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` يتجاوز `__main__.py` ويستدعي `co_op_translator.mcp.server:main` مباشرة.

عند إضافة أو تغيير خيارات CLI، حدِّث:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- اختبارات متعلقة بـCLI، إذا تغير السلوك

## خادم MCP

تم تنفيذ خادم MCP في:

```python
co_op_translator.mcp.server
```

يعمل الخادم عن قصد كغلاف لواجهة برمجة التطبيقات العامة لبايثون بدلاً من استدعاء وحدات `core` منخفضة المستوى. حافظ على هذا الحد كما هو حتى يشترك عملاء MCP، ومستدعي بايثون، وسطر الأوامر في نفس السلوك.

عند إضافة أو تغيير أدوات MCP، حدِّث:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

أدوات ترجمة المستودع قابلة للاستدعاء عبر النموذج من خلال MCP ويمكنها كتابة العديد من الملفات. اجعل `dry_run=True` افتراضيًا واطلب `confirm_write=True` قبل ترجمة المشروع بدون التشغيل الجاف.

## سير الترجمة

سير ترجمة المشروع عالي المستوى هو:

1. تحليل وسيطات CLI أو معلمات API.
2. التحقق من تكوين LLM باستخدام `LLMConfig`.
3. التحقق من Azure AI Vision عند اختيار ترجمة الصور.
4. توحيد رموز اللغات.
5. كشف الأسماء المستعارة لمجلدات اللغات القديمة.
6. تقدير حجم الترجمة.
7. تحديث أقسام اللغة/الدورة في README عند الاقتضاء.
8. تفويض ترجمة المشروع إلى `ProjectTranslator`.
9. يقوم `ProjectTranslator` بتفويض معالجة الملفات إلى `TranslationManager`.

`TranslationManager` يتألف من مزيجات (mixins) مخصّصة لأنواع الملفات:

- `ProjectMarkdownTranslationMixin` يتعامل مع قراءة ملفات Markdown، ترجمة المحتوى، إعادة كتابة المسارات، البيانات الوصفية، إخلاءات المسؤولية، والكتابة.
- `ProjectNotebookTranslationMixin` يتعامل مع قراءة ملفات notebook، ترجمة خلايا Markdown، إعادة كتابة المسارات، البيانات الوصفية، إخلاءات المسؤولية، والكتابة.
- `ProjectImageTranslationMixin` يتعامل مع اكتشاف الصور، استخلاص/ترجمة النص، كتابة الصور المولَّدة، والبيانات الوصفية.

تتخطى واجهات API للمحتوى منخفضة المستوى سير عمل المشروع:

1. تقوم `translate_markdown_content` و`translate_notebook_content` بترجمة المحتوى المخزّن في الذاكرة فقط.
2. تقوم `translate_image_content` بترجمة النص في صورة واحدة وتعيد كائن صورة مولَّدة.
3. يعدّ `rewrite_markdown_paths` و`rewrite_notebook_paths` مساعدين للمعالجة اللاحقة الصريحة. لا يقومان بأي ترجمة ولا بكتابات في المشروع.

## سير المراجعة

سير المراجعة الحتمي هو:

1. تحليل وسيطات CLI أو معلمات API.
2. توحيد رموز اللغات المطلوبة.
3. بناء هدف مراجعة واحد أو أكثر من `root_dir`, `root_dirs`, أو `groups`.
4. اختيارياً تحديد ملفات المصدر باستخدام `--changed-from`.
5. تشغيل فحوص حتمية للهيكل، حداثة الترجمة، سلامة Markdown، ومسارات الروابط/الصور المحلية.
6. طباعة إخراج نصي أو GitHub-flavored Markdown.
7. الخروج كفشل عند العثور على أخطاء مراجعة.

لا يتطلب سير المراجعة مفاتيح API ويظل متاحًا لفحوص محلية أو CI اختياري للمستخدمين. لا يقوم هذا المستودع بتشغيل `co-op-review` تلقائيًا على كل طلب سحب.

## موقع التوثيق

يتم تكوين موقع التوثيق بواسطة:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

يعدُّ دليل `docs/` المصدر القانوني للتوثيق. لا تضف دلائل مستخدم جديدة خارج هذا الدليل ما لم يُدخِل المشروع عمدًا سطح توثيق منشور آخر.

بناء محلياً:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

معاينة محليًا:

```bash
python -m mkdocs serve
```

يتم كتابة الموقع المولد إلى `site/`، والذي يتجاهله git.

## سير عمل GitHub Pages

يقوم `.github/workflows/docs.yml` ببناء الموقع عند طلبات السحب ونشره عند الدفع إلى `main`.

يقوم سير العمل بتثبيت:

```bash
pip install -r requirements-docs.txt
```

يثبّت سير عمل التوثيق سلسلة أدوات التوثيق فقط. يشير `mkdocs.yml` إلى `mkdocstrings` على `src/` بحيث يمكن عرض صفحات واجهة برمجة التطبيقات العامة من شجرة المصدر دون تثبيت مجموعة الاعتماديات الكاملة لوقت التشغيل. إذا كانت توثيقات API المستقبلية تتطلب استيراد مزوّدي وقت تشغيل اختياريين أثناء البناء، فحدّث كلًا من `.github/workflows/docs.yml` وهذا الدليل معًا.

## معيار جودة التوثيق

قبل دمج تغييرات التوثيق، شغّل:

```bash
python -m mkdocs build --strict
git diff --check
```

استخدم عمليات بناء صارمة بحيث تفشل الروابط المكسورة، إدخالات التنقل غير الصالحة، ومشكلات عرض API مبكرًا.