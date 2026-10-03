# واجهة برمجة تطبيقات Python

يتم تصدير واجهة Python العامة المستقرة من `co_op_translator.api`. تستخدم معظم التكاملات إحدى سير العمل التالية:

| السيناريو | استخدم هذا عندما | واجهات برمجة التطبيقات الرئيسية |
| --- | --- | --- |
| ترجمة ملفات أو مستندات فردية | يقرأ تطبيقك المحتوى المصدر، يستدعي Co-op Translator للترجمة، ويحدد مكان حفظ النتيجة. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| تحضير المحتوى لترجمة وكيل المضيف | سيقوم مضيف MCP أو نموذج التطبيق الخاص بك بترجمة الأجزاء، بينما يتولى Co-op Translator تقسيم الأجزاء وإعادة تجميعها. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ترجمة مستودع كامل | تريد أن تتصرف واجهة Python مثل CLI وتتعامل مع الاكتشاف، ومسارات الإخراج، والبيانات الوصفية، والتنظيف، والكتابات. | `run_translation` |

معظم الوحدات منخفضة المستوى تحت `core`, `config`, `review`, و`utils` هي تفاصيل تنفيذ تُستخدم بواسطة نقاط الدخول هذه في الواجهة البرمجية.

يستخدم عملاء MCP نفس الواجهة العامة عبر [خادم MCP](mcp.md). استخدم هذه الصفحة عند استدعاء Python مباشرة، واستخدم دليل MCP عند تعريض Co-op Translator لوكيل أو محرر. إذا كنت تقرر بين CLI وواجهة Python وMCP، ابدأ بـ [اختر سير العمل الخاص بك](workflows.md).

## تدفق الواجهة البرمجية للمرة الأولى

ابدأ من هنا إذا كنت تستدعي Co-op Translator من كود Python:

1. قم بتكوين مزود LLM كما هو موضح في [Configuration](configuration.md)، ما لم تكن تقوم فقط بتحضير أجزاء Markdown أو الدفاتر (notebook) لترجمة وكيل المضيف.
2. قرر ما إذا كان تطبيقك يتولى إدخال/إخراج الملفات.
3. استخدم واجهات المحتوى عندما يقرأ تطبيقك ويكتب ملفات فردية.
4. استخدم `run_translation` عندما يجب أن يعالج Co-op Translator مستودعًا مثل الـ CLI.
5. استخدم `run_review` بعد الترجمة إذا احتجت إلى فحوصات حتمية في الأتمتة.

| الهدف | واجهة برمجة التطبيقات للبدء بها |
| --- | --- |
| ترجمة سلسلة Markdown أو ملف واحد | `translate_markdown_content` |
| ترجمة حمولة دفتر واحد | `translate_notebook_content` |
| ترجمة صورة واحدة | `translate_image_content` |
| السماح لوكيل المضيف بترجمة أجزاء Markdown أو الدفتر | `start_markdown_agent_translation` أو `start_notebook_agent_translation` |
| إعادة كتابة الروابط المترجمة بعد اختيار مسار الإخراج | `rewrite_markdown_paths` أو `rewrite_notebook_paths` |
| ترجمة مستودع كامل | `run_translation` |
| مراجعة المخرجات المترجمة | `run_review` |

## السيناريو 1: ترجمة ملفات أو مستندات فردية

استخدم هذا التدفق عندما يكون لديك بالفعل ملف أو مخزن مؤقت للمحرر أو حمولة دفتر أو طلب MCP أو إدخال خط أنابيب مخصص. تطبيقك يتولى إدخال/إخراج الملفات:

1. اقرأ المحتوى المصدر.
2. استدعِ واجهة ترجمة المحتوى.
3. اختياريًا استدعِ واجهة إعادة كتابة المسارات إذا كان المحتوى المترجم سيُكتب في مجلد ترجمة المشروع.
4. احفظ أو أعد النتيجة من تطبيقك.

لا تقوم واجهات ترجمة المحتوى بتشغيل اكتشاف المشروع، ولا تكتب بيانات وصفية، ولا تُلحق إخلاءات مسؤولية، ولا تعيد كتابة الروابط تلقائيًا.

### ملف Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

إذا لم يَكن Markdown المترجم سيعيش في تخطيط مشروع Co-op Translator، فتخطَّ `rewrite_markdown_paths` واحفظ السلسلة المترجمة مباشرة.

### ملف الدفتر

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

يترجم `translate_notebook_content` خلايا Markdown ويحافظ على الخلايا غير‑Markdown. يتم تطبيق إعادة كتابة المسارات فقط على خلايا Markdown.

### ملف الصورة

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

يقرأ `translate_image_content` صورة المصدر ويعيد `PIL.Image.Image` مرسومًا. لا يكتب بيانات وصفية للصورة المترجمة.

## السيناريو 2: ترجمة مستودع كامل

استخدم هذا التدفق عندما تريد أن تتصرف واجهة Python مثل أمر `translate` في CLI. يقوم `run_translation` باكتشاف الملفات المدعومة، يترجم أنواع المحتوى المحددة، يعيد كتابة المسارات، يكتب ملفات الإخراج، يحدث البيانات الوصفية، ويؤدي مهام صيانة الترجمة مثل التنظيف.

`run_translation` هو نقطة الدخول المفضلة لتنظيم المشاريع. يتم تصدير `translate_project` كاسم مرادف متوافق بنفس السلوك.

ترجم ملفات Markdown في المستودع الحالي إلى الكورية واليابانية:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ترجم دفاتر (notebooks) فقط من جذر مشروع محدد:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

معاينة حجم الترجمة دون كتابة ملفات:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

سجِّل أحداث تقدم منظمة لتكامل:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # قم بتخزين الحمولة في جدول أحداث الوظيفة أو قم ببثها إلى واجهة المستخدم لديك.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

تستخدم الأحداث المخطط ذو الإصدار `co-op.translation.event.v1`. يجب أن تعتمد التكاملات على الحقول الثابتة مثل `type` و`stage_key`، لا على نص وحدة التحكم الموجه للمستخدم أو `stage_label`.



ترجم عدة جذور محتوى في استدعاء واحد:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

اكتب الترجمات في مجموعات إخراج صريحة:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

استخدم عنصرًا نائبًا لكل لغة عندما يجب أن يحتوي كل مجلد لغة على دليل فرعي متداخل:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

إذا لم يتم تعيين أي من `markdown` أو `notebook` أو `images`، تقوم الواجهة بترجمة كل الأنواع المدعومة: Markdown والدفاتر والصور.

### الحفاظ على التعديلات البشرية المقبولة بواسطة مزود حالة الترجمة

بشكل افتراضي، يحافظ Co-op Translator على سلوكه الحالي على مستوى الملف: عندما
يصبح مصدر Markdown قديمًا، يتم إعادة توليد الملف المترجم بالكامل. يمكن للتكاملات المستضافة
أن تمرر اختياريًا `TranslationStateProvider` للحفاظ على التعديلات البشرية
في كتل المصدر التي لم تتغير.

يوفر المزود زوج المصدر/الهدف المقبول الأخير ويسجل كل
مرشح جديد. تظل عملية القبول مسؤولية التكامل — على سبيل المثال،
بعد دمج طلب سحب الترجمة:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

بالنسبة لملفات Markdown التي لديها خط أساس مقبول صالح، يقوم Co-op Translator بمحاذاة
الكتل العلوية في Markdown. تعيد كتل المصدر غير المتغيرة استخدام الكتل المترجمة الحالية،
بما في ذلك التعديلات التي أجرها الأشخاص؛ تُرسل كتل المصدر التي تغيرت أو أضيفت
للترجمة؛ تُزال كتل المصدر المحذوفة. إذا كانت المحاذاة غير واضحة،
تغيرت بنية الهدف، كانت ترجمة كتلة غير صالحة، أو لا يوجد خط أساس
متاح، يتراجع Co-op Translator بأمان إلى مسار الترجمة الكامل الموجود.


تخزن هذه الواجهة حالة ترجمة المستند، وليس ذاكرة ترجمة عبارات أو
مقاطع عبر المستندات. ينطبق ذلك حاليًا على ترجمة مشاريع Markdown.
سلوك الدفاتر والصور لم يتغير. تمرير `update=True`
لا يزال يطلب إعادة توليد كاملة.

إذا تعذر ترجمة ملف واحد أو أكثر، فإن `run_translation` يطرح
`RuntimeError` بعد انتهاء سير عمل المشروع بدلاً من الإبلاغ عن
تشغيل ناجح مع مخرجات مفقودة. يجب أن تعامل التكاملات هذا على أنه مهمة فاشلة
وتحتفظ بحالة الترجمة المقبولة السابقة.

## مراجعة المخرجات المترجمة

`run_review` يجري فحوصات ترجمة حتمية دون الاعتماد على أوراق اعتماد LLM أو Vision.

!!! note "Beta"
    `run_review` هي واجهة مراجعة حتمية في طور البيتا. لا تستدعي مزودي النماذج أو تكتب ملفات، لكن قد تتطور مخططات الفحوصات والقضايا.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

بعد ترجمة تقتصر على README فقط، استخدم نفس النطاق للمراجعة:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

يراجع `readme_only=True` ملف `README.md` فقط تحت كل جذر مصدر مُكوَّن،
بما في ذلك `groups` المخصصة ودلائل الإخراج. تُستثنى المستندات الأخرى وملفات
README المتداخلة. يؤدي فقدان README المصدر إلى إثارة `ValueError`; فحوصات
الترجمة الفاشلة تثير `RuntimeError`.

راجع الملفات التي تغيرت فقط مقابل مرجع أساسي واطبع مخرجات على طراز GitHub:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## أمثلة للنسخ واللصق للواجهة البرمجية

ترجم محتوى Markdown دون كتابة ملفات:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

ترجم وأعد كتابة روابط Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

ترجم مستودعًا من Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

ترجم عدة جذور:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

حافظ على مصطلحات المسرد:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## نقاط الدخول العامة

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## واجهات ترجمة المحتوى

تُعد واجهات ترجمة المحتوى مخصصة للتكاملات التي لديها المحتوى بالفعل في الذاكرة، مثل امتداد محرر، أداة MCP، معالج دفاتر، أو خط أنابيب مخصص.

| الدالة | الإدخال | المخرجات | إدخال/إخراج الملفات | ملاحظات |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | لا | غير متزامن. يترجم محتوى Markdown فقط. لا يعيد كتابة الروابط، ولا يكتب بيانات وصفية، ولا يُلحق إخلاءات مسؤولية. |
| `translate_notebook_content` | JSON دفتر `str` أو `dict` | JSON دفتر `str` | لا | غير متزامن. يترجم خلايا Markdown ويحافظ على الخلايا غير‑Markdown. لا يعيد كتابة الروابط، ولا يكتب بيانات وصفية، ولا يُلحق إخلاءات مسؤولية. |
| `translate_image_content` | مسار الصورة | `PIL.Image.Image` | يقرأ صورة المصدر فقط | متزامن. يستخرج ويترجم نص الصورة، ثم يعيد صورة مرسومة. لا يحفظ بيانات وصفية للصورة المترجمة. |

تقبل `translate_markdown_content` و`translate_notebook_content` خيارًا اختياريًا `source_path` عبر خياراتهما. يمرر المسار كسياق إلى المترجم؛ يظل المتصلون مسؤولين عن أي إعادة كتابة مسار محددة بالمشروع بعد الترجمة.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

يمكن تمرير نفس الخيارات كقواميس:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## واجهات الترجمة بمساعدة الوكيل

لا تستدعي واجهات الترجمة بمساعدة الوكيل مزود LLM المكوَّن من Co-op Translator. إنها تُعِد أجزاء Markdown أو الدفاتر لكي يترجمها وكيل المضيف، ثم تعيد تجميع المحتوى النهائي من الأجزاء المترجمة.

| الدالة | الغرض |
| --- | --- |
| `start_markdown_agent_translation` | إرجاع مهمة Markdown مكتفية ذاتيًا تحتوي على أجزاء، ومطالب، وحالة إعادة التجميع. |
| `finish_markdown_agent_translation` | إعادة تجميع Markdown من مهمة والأجزاء المترجمة بواسطة وكيل المضيف. |
| `start_notebook_agent_translation` | إرجاع مهمة دفتر تحتوي على أجزاء خلايا Markdown لترجمة وكيل المضيف. |
| `finish_notebook_agent_translation` | إعادة تجميع JSON الدفتر مع الحفاظ على خلايا الكود والمخرجات والبيانات الوصفية. |

يُقصد بهذا التدفق بشكل أساسي لمضيفي MCP. إذا كنت بحاجة إلى ترجمة مستودعات إنتاجية مع قيام Co-op Translator بإدارة استدعاءات المزود، فاستخدم `translate_markdown_content` أو `translate_notebook_content` أو `run_translation`.

## واجهات إعادة كتابة المسارات

لا تؤدي واجهات إعادة كتابة المسارات أي ترجمة. إنها تُحدِّث الروابط وحقول المسار في frontmatter بعد أن يعرف المتصلون مسار المصدر ومسار الهدف المترجم وتخطيط المشروع.

| الدالة | النطاق | ملاحظات |
| --- | --- | --- |
| `rewrite_markdown_paths` | جسم Markdown وfrontmatter | تعيد كتابة روابط Markdown وحقول المسار المدعومة في frontmatter لهدف مترجم. |
| `rewrite_notebook_paths` | خلايا Markdown في JSON الدفتر | تطبق إعادة كتابة مسارات Markdown على كل خلية Markdown وتترك الخلايا غير‑Markdown دون تغيير. |

قد يكون الوسيط `policy` قاموسًا يحتوي الحقول التالية:

| الحقل | مطلوب | الغرض |
| --- | --- | --- |
| `language_code` | نعم | رمز اللغة الهدف، مثل `"ko"` أو `"pt-BR"`. |
| `root_dir` | لا | جذر مشروع المصدر. الافتراضي هو `"."`. |
| `translations_dir` | لا | دليل إخراج ترجمة النص. الافتراضي هو `translations` تحت `root_dir`. |
| `translated_images_dir` | لا | دليل إخراج الصور المترجمة. الافتراضي هو `translated_images` تحت `root_dir`. |
| `translation_types` | لا | أنواع الترجمة الممكنة. الافتراضي هو Markdown والدفاتر والصور. |
| `lang_subdir` | لا | دليل فرعي اختياري تحت كل مجلد لغة. |

## معلمات ترجمة المشروع

| المعامل | النوع | الافتراضي | الغرض |
| --- | --- | --- | --- |
| `language_codes` | `str` | مطلوب | رموز لغات الهدف مفصولة بمسافات، مثل `"ko ja fr"`، أو `"all"`. تُطَبَّع رموز المرادفات إلى قيم BCP 47 القياسية. |
| `root_dir` | `str` | `"."` | جذر المشروع لهدف ترجمة واحد. يُتجاهل عندما يتم توفير `root_dirs` أو `groups`. |
| `update` | `bool` | `False` | حذف وإعادة إنشاء الترجمات الموجودة للغات المحددة. |
| `images` | `bool` | `False` | تضمين ترجمة الصور. يتطلب تكوين Azure AI Vision. |
| `markdown` | `bool` | `False` | تضمين ترجمة Markdown. |
| `notebook` | `bool` | `False` | تضمين ترجمة دفاتر Jupyter. |
| `debug` | `bool` | `False` | تفعيل تسجيل التصحيح. |
| `save_logs` | `bool` | `False` | احفظ ملفات السجل بمستوى DEBUG تحت دليل الجذر `logs/`. |
| `yes` | `bool` | `True` | تأكيد المطالبات تلقائيًا للاستخدام البرنامجي وفي بيئات CI. |
| `add_disclaimer` | `bool` | `False` | إضافة إخلاءات مسؤولية للترجمة الآلية إلى ملفات Markdown والمفكرات المترجمة. |
| `translations_dir` | `str \| None` | `None` | دليل مخرجات مخصص لترجمة النص. تُحل المسارات النسبية بالنسبة لكل جذر. |
| `image_dir` | `str \| None` | `None` | دليل مخرجات مخصص للصور المترجمة. تُحل المسارات النسبية بالنسبة لكل جذر. |
| `root_dirs` | `Iterable[str] \| None` | `None` | عدة جذور تشترك في نفس إعدادات المخرجات. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | أزواج صريحة (root_dir, translations_dir). تأخذ الأسبقية على `root_dirs`. |
| `repo_url` | `str \| None` | `None` | عنوان URL للمستودع يُستخدم عند عرض إرشادات جدول اللغات في README. |
| `glossaries` | `Iterable[str] \| None` | `None` | مصطلحات المعجم التي تُحفظ أثناء الترجمة. يتم تطبيع المصطلحات المكررة والفارغة. |
| `dry_run` | `bool` | `False` | تقدير حجم الترجمة ومعاينة سلوك الترحيل دون كتابة ملفات. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | محول اختياري للاحتفاظ بالخط الأساسي المقبول والمرشح لتحديثات Markdown التدريجية. حذفُه يحافظ على سلوك الملفات الكاملة الحالي. |

## معلمات المراجعة

`run_review` يحاكي عمدًا توقيع `run_translation` حيثما أمكن، حتى تتمكن الأتمتة من التبديل بين تدفقات العمل الخاصة بالترجمة والمراجعة مع أقل قدر من التشعب.

| المعامل | النوع | الافتراضي | الغرض |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | مجلدات اللغات الهدف للمراجعة. يمكن قبول سلاسل مفصولة بمسافات ومجاميع قابلة للتكرار. `"all"` تراجع كل لغة ترجمة تم اكتشافها. |
| `root_dir` | `str` | `"."` | جذر المشروع لهدف مراجعة واحد. يتم تجاهله عندما يتم توفير `root_dirs` أو `groups`. |
| `markdown` | `bool` | `False` | تضمين ملفات مصدر Markdown وMDX. |
| `notebook` | `bool` | `False` | تضمين ملفات مصدر دفاتر Jupyter. |
| `images` | `bool` | `False` | محجوز للتكافؤ مع خيارات الترجمة. يتم التحقق من مراجع الروابط للصور من Markdown. |
| `translations_dir` | `str \| None` | `None` | دليل مخرجات مخصص لترجمة النص. تُحل المسارات النسبية بالنسبة لكل جذر. |
| `root_dirs` | `Iterable[str] \| None` | `None` | عدة جذور تشترك في نفس إعدادات المخرجات. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | أزواج صريحة (root_dir, translations_dir). تأخذ الأسبقية على `root_dirs`. |
| `changed_from` | `str \| None` | `None` | مرجع Git يُستخدم لتقييد المراجعة بالملفات المصدرية المتغيرة. |
| `readme_only` | `bool` | `False` | مراجعة فقط `README.md` تحت كل جذر مصدر. يؤدي غياب README المصدر إلى إثارة `ValueError`. |
| `output_format` | `str` | `"text"` | تنسيق مخرجات المراجعة. القيم المدعومة هي `"text"` و`"github"`. |
| `fail_on_warnings` | `bool` | `False` | اعتبر التحذيرات فشلًا بالإضافة إلى الأخطاء. |
| `debug` | `bool` | `False` | تمكين تسجيلات التصحيح. |
| `save_logs` | `bool` | `False` | حفظ ملفات السجل بمستوى DEBUG تحت دليل الجذر `logs/`. |

إذا لم يتم تعيين أي من `markdown` أو `notebook` أو `images`، تقوم واجهة البرمجة بمراجعة مستندات Markdown والدفاتر وروابط الصور حيثما ينطبق ذلك. لا تستدعي المراجعة مزوِّد LLM ولا تتطلب مفاتيح API.

## متطلبات التكوين

تتطلب واجهات برمجة التطبيقات للترجمة المدعومة من مزود تكوين المزود قبل الترجمة:

- تتطلب ترجمة Markdown والدفاتر مزود LLM. قم بتكوين Azure OpenAI أو OpenAI أو Anthropic.
- تتطلب ترجمة الصور Azure AI Vision بالإضافة إلى مزود LLM.
- `run_translation` ينفذ فحوصات اتصال خفيفة قبل بدء ترجمة المشروع.
- واجهات برمجة التطبيقات المدعومة بالوكيل `start_*_agent_translation` و `finish_*_agent_translation` لا تستدعي مزوِّدي LLM الخاص بـ Co-op Translator. يقوم تطبيق المضيف أو وكيل MCP بترجمة الأجزاء المحضرة.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, و`run_review` تكون نتائجها حتمية ولا تتطلب بيانات اعتماد الموفر.

المتغيرات المطلوبة لـ Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

المتغيرات المطلوبة لـ OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

المتغيرات المطلوبة لـ Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` و `ANTHROPIC_MAX_TOKENS` اختياريان. Microsoft Agent Framework هو عميل النموذج الافتراضي لجميع الموفرين بدءًا من Co-op Translator 0.22.0. لا يزال بالإمكان اختيار Semantic Kernel مؤقتًا باستخدام `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, لكن القيام بذلك يصدر تحذيرًا بالإهمال؛ انظر [التكوين](configuration.md#model-client-backend) لخطة الإزالة المرحلية.

المتغيرات المطلوبة لـ Azure AI Vision لترجمة الصور:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` حتمية ولا تتطلب تكوين LLM أو Azure AI Vision.

## ملاحظات السلوك

- تحافظ واجهات برمجة تطبيقات ترجمة المحتوى على فصل الترجمة عن إعادة كتابة مسارات المشروع. استدعِ `rewrite_markdown_paths` أو `rewrite_notebook_paths` صراحةً عندما تحتاج المحتويات المترجمة إلى تعديل روابطها النسبية للمشروع لموقع الهدف.
- تضيف واجهات برمجة تطبيقات تنظيم المشروع سلوكيات المشروع حول ترجمة المحتوى، بما في ذلك اكتشاف الملفات، والكتابة، وإعادة كتابة المسارات، والبيانات الوصفية، والتنظيف، وإخلاءات المسؤولية الاختيارية.
- يقوم `run_translation` بطباعة ملخصات التقدم والتقديرات عبر نفس المُبلغ المدعوم من Rich المستخدم في CLI. يُرجع الإخراج غير التفاعلي إلى نص عادي.
- يقوم `dry_run=True` بحساب التقديرات باستخدام تحديثات README الافتراضية، لكنه لا يكتب README أو ملفات الترجمة.
- تتم معالجة `groups` تسلسليًا. يتم طباعة تقدير إجمالي واحد قبل بدء العمل.
- عندما يتم اختيار ترجمة الصور، يؤدي غياب تكوين Vision إلى إثارة خطأ قبل بدء الترجمة.
- يتم اكتشاف مجلدات اللغة الموجودة القائمة على الأسماء المستعارة ويمكن ترحيلها إلى أسماء مجلدات اللغة القياسية كجزء من التشغيل.
- يفشل `run_review` عند وجود ملفات مترجمة مفقودة، أو بيانات وصفية للترجمة مفقودة أو قديمة، أو ترويسات Markdown/سياجات الكود المشوهة، أو JSON لدفتر مترجم غير صالح.
- يقوم `run_review` بالإبلاغ عن أهداف روابط Markdown والصور المحلية المفقودة كتحذيرات بشكل افتراضي.

## مسار الاستدعاء الداخلي

تفوض API إلى نفس التنفيذ الأساسي المستخدم بواسطة CLI:

الترجمة:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. مزيجات ترجمة المشاريع المركزة لـ Markdown والدفاتر والصور.
8. المترجمون الخاصون بـ Markdown ودفتر الملاحظات والنص والصورة ضمن `co_op_translator.core`.

المراجعة:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

الفئات التالية مفيدة للمشرفين على الصيانة، لكنها غير مُصدّرة كواجهة API مستقرة على مستوى الحزمة.

| الفئة | الوحدة | المسؤولية |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ينسق ترجمة مستوى المشروع، وإدارة الدليل، وتطبيع البيانات الوصفية لكل لغة، والتفويض إلى مترجمي Markdown والدفاتر والصور. |
| `TranslationManager` | `co_op_translator.core.project.translation` | ينفذ العمل غير المتزامن لمعالجة الملفات لـ Markdown والدفاتر والصور، واكتشاف البُلى، وتحديثات البيانات الوصفية للترجمة. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | ينسق قراءات ملفات Markdown، وترجمة المحتوى، وإعادة كتابة المسارات، والبيانات الوصفية، وإخلاءات المسؤولية، والكتابة. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ينسق قراءات ملفات الدفاتر، وترجمة خلايا Markdown، وإعادة كتابة المسارات، والبيانات الوصفية، وإخلاءات المسؤولية، والكتابة. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ينسق اكتشاف صور المصدر، وترجمة الصور، ومسارات المخرجات، والبيانات الوصفية، والكتابة. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | يعثر على أزواج Markdown المترجمة، ويقيّم جودة الترجمة، ويقرأ البيانات الوصفية للثقة لعمليات إصلاح ذات ثقة منخفضة. |
| `ReviewRunner` | `co_op_translator.review.runner` | ينسق فحوص المراجعة الحتمية عبر ملفات المصدر واللغات الهدف وجذور الترجمة المكوّنة. |
| `ReviewTarget` | `co_op_translator.review.targets` | يصف جذر المصدر ودليل مخرجات الترجمة الذي تتم مراجعته لذلك الجذر. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | يكتشف مجلدات اللغات القديمة المستندة إلى الأسماء المستعارة ويُعد خطط ترحيل لمجلدات معيارية وفق BCP 47. |
| `Config` | `co_op_translator.config.base_config` | يحمل ملفات `.env` ويتحقق ما إذا كانت مزودات LLM المطلوبة ومزودات Vision الاختيارية مُكوّنة. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | يكتشف تلقائيًا Azure OpenAI أو OpenAI أو Anthropic، ويتحقق من صحة المتغيرات البيئية المطلوبة، ويُجري فحوصات اتصال المزود. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | يكتشف تكوين Azure AI Vision ويُجري فحوصات اتصال لترجمة الصور. |