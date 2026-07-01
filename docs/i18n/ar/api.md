# Python API

يتم تصدير واجهة برمجة تطبيقات Python العامة المستقرة من `co_op_translator.api`. تستخدم معظم التكاملات أحد سير العمل هذه:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | يقرأ تطبيقك المحتوى المصدر، يستدعي Co-op Translator للترجمة، ويقرر مكان حفظ النتيجة. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | سيقوم مضيف MCP أو نموذج التطبيق الخاص بك بترجمة القطع، بينما يتولى Co-op Translator تجزئة المحتوى وإعادة تجميعه. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | تريد أن يتصرف Python API مثل CLI ويتولى الاكتشاف، مسارات الإخراج، البيانات الوصفية، التنظيف، والكتابة. | `run_translation` |

تعد معظم الوحدات منخفضة المستوى تحت `core`, `config`, `review`, و `utils` تفاصيل تنفيذية تُستخدم بواسطة نقاط الدخول هذه في API.

يستخدم عملاء MCP نفس API العامة عبر [MCP Server](mcp.md). استخدم هذه الصفحة عند استدعاء Python مباشرة، ودليل MCP عند عرض Co-op Translator لوكيل أو محرر. إذا كنت تختار بين CLI أو Python API أو MCP، ابدأ بـ [Choose Your Workflow](workflows.md).

## First-Time API Flow

ابدأ هنا إذا كنت تستدعي Co-op Translator من كود Python:

1. قم بتكوين مُزوّد LLM كما هو موضح في [Configuration](configuration.md)، ما لم تكن تقوم فقط بتحضير قطع Markdown أو دفاتر الملاحظات للترجمة بواسطة مضيف-الوكيل.
2. قرر ما إذا كان تطبيقك يتولى عمليات القراءة/الكتابة للملفات.
3. استخدم واجهات برمجة المحتوى عندما يقرأ تطبيقك الملفات ويكتبها بشكل فردي.
4. استخدم `run_translation` عندما يجب على Co-op Translator معالجة مستودع كما في CLI.
5. استخدم `run_review` بعد الترجمة إذا كنت بحاجة إلى فحوصات حتمية في الأتمتة.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

استخدم هذا سير العمل عندما يكون لديك بالفعل ملف أو حافظة محرر أو حمولة دفتر ملاحظات أو طلب MCP أو مدخل خط أنابيب مخصص. تطبيقك يتولى عمليات القراءة/الكتابة للملفات:

1. اقرأ المحتوى المصدر.
2. استدعِ واجهة API لترجمة المحتوى.
3. اختياريًا استدعِ واجهة إعادة كتابة المسارات إذا كان المحتوى المترجم سيُكتب إلى مجلد ترجمة المشروع.
4. احفظ أو أعد النتيجة من تطبيقك.

واجهات ترجمة المحتوى لا تُجري اكتشاف المشروع، لا تكتب بيانات وصفية، لا تُلحق إخلاءات مسؤولية، ولا تعيد كتابة الروابط تلقائيًا.

### Markdown File

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

إذا لم يكن من المقرر أن يعيش Markdown المترجم في تخطيط مشروع Co-op Translator، فتخطَّ `rewrite_markdown_paths` واحفظ السلسلة المترجمة مباشرة.

### Notebook File

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

`translate_notebook_content` يترجم خلايا Markdown ويحافظ على الخلايا غير Markdown. تُطبَّق إعادة كتابة المسارات على خلايا Markdown فقط.

### Image File

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

`translate_image_content` يقرأ الصورة المصدر ويعيد `PIL.Image.Image` مرسومة. لا يكتب بيانات وصفية للصورة المترجمة.

## Scenario 2: Translate an Entire Repository

استخدم هذا سير العمل عندما تريد أن يتصرف Python API مثل أمر `translate` في CLI. يقوم `run_translation` باكتشاف الملفات المدعومة، يترجم أنواع المحتوى المحددة، يعيد كتابة المسارات، يكتب ملفات الإخراج، يحدث البيانات الوصفية، ويقوم بمهام صيانة الترجمة مثل التنظيف.

يعد `run_translation` نقطة الدخول المفضلة لتنظيم المشروع. يتم تصدير `translate_project` كاسم مستعار للتوافق بنفس السلوك.

ترجم ملفات Markdown في المستودع الحالي إلى الكورية واليابانية:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ترجم دفاتر الملاحظات فقط من جذر مشروع محدد:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

عاين حجم الترجمة بدون كتابة ملفات:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

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

استخدم عنصر نائب لكل لغة عندما يجب أن تحتوي كل لغة على دليل فرعي متداخل:

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

إذا لم يتم تعيين أي من `markdown`, `notebook`, أو `images`، يقوم API بترجمة جميع الأنواع المدعومة: Markdown، دفاتر الملاحظات، والصور.

## Review Translated Output

`run_review` يشغّل فحوصات ترجمة حتمية بدون بيانات اعتماد LLM أو Vision.

!!! note "نسخة تجريبية"
    `run_review` هو واجهة مراجعة حتمية في النسخة التجريبية. إنها لا تستدعي موفري النماذج ولا تكتب ملفات، لكن من الممكن أن تتطور مخططات الفحوصات والمشكلات.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

راجع الملفات التي تغيرت فقط مقابل مرجع أساسي واطبع مخرجًا بنمط GitHub:

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

## Copy-Paste API Examples

ترجم محتوى Markdown بدون كتابة ملفات:

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
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

واجهات ترجمة المحتوى مخصّصة للتكاملات التي لديها المحتوى بالفعل في الذاكرة، مثل امتداد محرر، أداة MCP، معالج دفاتر ملاحظات، أو خط أنابيب مخصص.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. يترجم محتوى Markdown فقط. لا يعيد كتابة الروابط، ولا يكتب بيانات وصفية، ولا يلحِق إخلاءات مسؤولية. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. يترجم خلايا Markdown ويحافظ على الخلايا غير Markdown. لا يعيد كتابة الروابط، ولا يكتب بيانات وصفية، ولا يلحِق إخلاءات مسؤولية. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. يستخرج ويترجم نص الصورة، ثم يعيد صورة مرسومة. لا يحفظ بيانات وصفية للصورة المترجمة. |

`translate_markdown_content` و `translate_notebook_content` تقبلان `source_path` اختياريًا عبر خياراتهما. يتم تمرير المسار كسياق إلى المترجم؛ يظل المتصلون مسؤولين عن أي إعادة كتابة مسارات خاصة بالمشروع بعد الترجمة.

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

## Agent-Assisted Translation APIs

واجهات الترجمة بمساعدة الوكيل لا تستدعي Azure OpenAI أو OpenAI من Co-op Translator. تقوم بتحضير قطع Markdown أو دفاتر الملاحظات ليترجمها مضيف-الوكيل، ثم تعيد تجميع المحتوى النهائي من القطع المترجمة.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | إرجاع مهمة Markdown مكتفية ذاتيًا تحتوي على قطع، مطالبات، وحالة إعادة التكوين. |
| `finish_markdown_agent_translation` | إعادة تجميع Markdown من مهمة وقطع مترجمة بواسطة مضيف-الوكيل. |
| `start_notebook_agent_translation` | إرجاع مهمة دفتر ملاحظات تحتوي على قطع خلايا Markdown لترجمة مضيف-الوكيل. |
| `finish_notebook_agent_translation` | إعادة تجميع JSON الدفتر مع الحفاظ على خلايا الكود والمخرجات والبيانات الوصفية. |

هذا سير العمل مخصص بشكل رئيسي لمضيفي MCP. إذا كنت بحاجة إلى ترجمة مستودع إنتاجية مع إدارة Co-op Translator لاستدعاءات المُزوّد، استخدم `translate_markdown_content`, `translate_notebook_content`, أو `run_translation`.

## Path Rewriting APIs

واجهات إعادة كتابة المسار لا تُجري أي ترجمة. تقوم بتحديث الروابط وحقول المسارات في الـ frontmatter بعد أن يعرف المستدعون المسار المصدر، مسار الهدف المترجم، وتخطيط المشروع.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | يعيد كتابة روابط Markdown وحقول المسارات المدعومة في الـ frontmatter لهدف مترجم. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | يطبّق إعادة كتابة مسارات Markdown على كل خلية Markdown ويترك الخلايا غير Markdown دون تغيير. |

قد يكون الوسيطة `policy` قاموسًا يحتوي هذه الحقول:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | رمز اللغة الهدف، مثل `"ko"` أو `"pt-BR"`. |
| `root_dir` | No | جذر مشروع المصدر. الافتراضي هو `"."`. |
| `translations_dir` | No | دليل إخراج ترجمة النص. الافتراضي هو `translations` تحت `root_dir`. |
| `translated_images_dir` | No | دليل إخراج الصور المترجمة. الافتراضي هو `translated_images` تحت `root_dir`. |
| `translation_types` | No | أنواع الترجمة الممكّنة. الافتراضي هو Markdown، دفاتر الملاحظات، والصور. |
| `lang_subdir` | No | دليل فرعي اختياري تحت كل مجلد لغة. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | رموز لغات الهدف مفصولة بمسافات، مثل `"ko ja fr"`، أو `"all"`. تُطَبَّع رموز الاسم المستعار إلى قيم BCP 47 المعيارية. |
| `root_dir` | `str` | `"."` | جذر المشروع لهدف ترجمة واحد. يتم تجاهله عند تزويد `root_dirs` أو `groups`. |
| `update` | `bool` | `False` | حذف وإعادة إنشاء الترجمات الموجودة للغات المحددة. |
| `images` | `bool` | `False` | تضمين ترجمة الصور. يتطلب تكوين Azure AI Vision. |
| `markdown` | `bool` | `False` | تضمين ترجمة Markdown. |
| `notebook` | `bool` | `False` | تضمين ترجمة دفاتر Jupyter. |
| `debug` | `bool` | `False` | تفعيل تسجيل التصحيح. |
| `save_logs` | `bool` | `False` | حفظ ملفات سجل بمستوى DEBUG تحت دليل `logs/` الجذري. |
| `yes` | `bool` | `True` | التأكيد التلقائي على المطالبات للاستخدام البرمجي وCI. |
| `add_disclaimer` | `bool` | `False` | إضافة إخلاءات مسؤولية الترجمة الآلية إلى Markdown والدفاتر المترجمة. |
| `translations_dir` | `str \| None` | `None` | دليل إخراج ترجمة نص مخصص. تُحل المسارات النسبية مقابل كل جذر. |
| `image_dir` | `str \| None` | `None` | دليل إخراج صور مترجمة مخصص. تُحل المسارات النسبية مقابل كل جذر. |
| `root_dirs` | `Iterable[str] \| None` | `None` | جذور متعددة تشترك في نفس إعدادات الإخراج. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | أزواج صريحة `(root_dir, translations_dir)`. لها الأسبقية على `root_dirs`. |
| `repo_url` | `str \| None` | `None` | عنوان URL للمستودع يُستخدم عند عرض دليل جدول اللغات في README. |
| `glossaries` | `Iterable[str] \| None` | `None` | مصطلحات مسرد يجب الحفاظ عليها أثناء الترجمة. يتم تطبيع التكرارات والمصطلحات الفارغة. |
| `dry_run` | `bool` | `False` | تقدير حجم الترجمة ومعاينة سلوك الهجرة دون كتابة ملفات. |

## Review Parameters

يُقصد من `run_review` أن يعكس توقيع `run_translation` حيثما أمكن حتى تتمكن الأتمتة من التبديل بين سير عمل الترجمة والمراجعة بأدنى قدر من التفرع.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | مجلدات اللغة الهدف للمراجعة. تُقبل سلسلات مفصولة بمسافات والمجموعات القابلة للتكرار. `"all"` تراجع كل لغات الترجمة المكتشفة. |
| `root_dir` | `str` | `"."` | جذر المشروع لهدف مراجعة واحد. يتم تجاهله عند تزويد `root_dirs` أو `groups`. |
| `markdown` | `bool` | `False` | تضمين ملفات المصدر Markdown وMDX. |
| `notebook` | `bool` | `False` | تضمين ملفات مصدر دفاتر Jupyter. |
| `images` | `bool` | `False` | محفوظ من أجل تعادل الخيارات مع الترجمة. تُفحص مراجع الروابط للصور من Markdown. |
| `translations_dir` | `str \| None` | `None` | دليل مخرجات الترجمة النصية المخصصة. تُحل المسارات النسبية بالنسبة لكل جذر. |
| `root_dirs` | `Iterable[str] \| None` | `None` | جذور متعددة تشترك في نفس إعدادات المخرجات. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | أزواج صريحة `(root_dir, translations_dir)`. لها أسبقية على `root_dirs`. |
| `changed_from` | `str \| None` | `None` | مرجع Git يُستخدم لتقليص المراجعة إلى ملفات المصدر المُعدلة. |
| `output_format` | `str` | `"text"` | تنسيق مخرجات المراجعة. القيم المدعومة هي `"text"` و `"github"`. |
| `fail_on_warnings` | `bool` | `False` | اعتبار التحذيرات كفشل بالإضافة إلى الأخطاء. |
| `debug` | `bool` | `False` | تمكين تسجيلات التصحيح. |
| `save_logs` | `bool` | `False` | حفظ ملفات السجل بمستوى DEBUG تحت دليل الجذر `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## متطلبات التكوين

تتطلب واجهات برمجة تطبيقات الترجمة المدعومة من مزود تهيئة المزود قبل الترجمة:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

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

المتغيرات المطلوبة لـ Azure AI Vision لترجمة الصور:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` حتمي ولا يتطلب تكوين Azure OpenAI أو OpenAI أو Azure AI Vision.

## ملاحظات السلوك

- تحافظ واجهات برمجة تطبيقات ترجمة المحتوى على فصل الترجمة عن إعادة كتابة مسارات المشروع. استدعِ `rewrite_markdown_paths` أو `rewrite_notebook_paths` صراحةً عندما تحتاج المحتويات المترجمة إلى تعديل الروابط النسبية للمشروع لموقع الهدف.
- تضيف واجهات برمجة تطبيقات تنظيم المشروع سلوك المشروع حول ترجمة المحتوى، بما في ذلك اكتشاف الملفات والكتابة وإعادة كتابة المسارات والبيانات الوصفية والتنظيف وإخلاءات المسؤولية الاختيارية.
- `run_translation` يعرض تقدم وملخصات التقدير عبر Click، مطابقة لتجربة مستخدم سطر الأوامر.
- `dry_run=True` يحسب التقديرات باستخدام تحديثات README افتراضية، لكنه لا يكتب README أو ملفات الترجمة.
- تُعالَج `groups` بالتتابع. يُطبع تقدير إجمالي واحد قبل بدء العمل.
- عند اختيار ترجمة الصور، يؤدي غياب تكوين Vision إلى رفع خطأ قبل بدء الترجمة.
- يتم اكتشاف مجلدات اللغة القديمة ذات الأسماء البديلة ويمكن ترحيلها إلى أسماء مجلدات لغوية معيارية كجزء من التشغيل.
- `run_review` يفشل عند وجود ملفات مترجمة مفقودة أو بيانات وصفية للترجمة مفقودة أو قديمة، ترويسات frontmatter أو حواجز كود Markdown تالفة، وJSON لدفتر مترجم غير صالح.
- `run_review` يبلغ عن أهداف روابط Markdown والصورة المحلية المفقودة كتحذيرات بشكل افتراضي.

## مسار الاستدعاء الداخلي

تفوض واجهة برمجة التطبيقات إلى نفس التنفيذ الأساسي المستخدم في سطر الأوامر:

الترجمة:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

المراجعة:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

الفئات التالية مفيدة للقائمين على الصيانة، لكنها غير مُصدّرة كواجهة برمجة تطبيقات ثابتة على مستوى الحزمة.

| الفئة | الوحدة | المسؤولية |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ينسق ترجمة مستوى المشروع، وإدارة الأدلة، وتطبيع البيانات الوصفية لكل لغة، والتفويض إلى مترجمي Markdown والدفاتر والصور. |
| `TranslationManager` | `co_op_translator.core.project.translation` | ينفّذ عمل معالجة الملفات غير المتزامنة لملفات Markdown والدفاتر والصور، وكشف الملفات القديمة، وتحديثات البيانات الوصفية للترجمة. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | ينسق قراءات ملفات Markdown، وترجمة المحتوى، وإعادة كتابة المسارات، والبيانات الوصفية، وإخلاءات المسؤولية، والكتابة. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ينسق قراءات ملفات الدفاتر، وترجمة خلايا Markdown، وإعادة كتابة المسارات، والبيانات الوصفية، وإخلاءات المسؤولية، والكتابة. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ينسق اكتشاف الصور المصدرية، ترجمة الصور، مسارات المخرجات، والبيانات الوصفية، والكتابة. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | يعثر على أزواج Markdown المترجمة، ويقيّم جودة الترجمة، ويقرأ البيانات الوصفية للثقة لعمليات إصلاح ذات ثقة منخفضة. |
| `ReviewRunner` | `co_op_translator.review.runner` | ينسق فحوصات المراجعة الحتمية عبر ملفات المصدر، اللغات الهدف، وجذور الترجمة المكوّنة. |
| `ReviewTarget` | `co_op_translator.review.targets` | يصف جذر المصدر ودليل مخرجات الترجمة الذي تُراجع لهذا الجذر. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | يكشف مجلدات اللغة القديمة ذات الأسماء البديلة ويُعد خطط ترحيل لأسماء المجلدات اللغوية المعيارية وفق BCP 47. |
| `Config` | `co_op_translator.config.base_config` | يحمّل ملفات `.env` ويفحص ما إذا كانت مزودات LLM المطلوبة وVision الاختيارية مُكوّنة. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | يكشف تلقائيًا Azure OpenAI أو OpenAI، يتحقق من صحة متغيرات البيئة المطلوبة، ويُجري فحوصات اتصال المزود. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | يكشف تكوين Azure AI Vision ويُجري فحوصات الاتصال لترجمة الصور. |