# اختر سير عملك

يمكن استخدام Co-op Translator بثلاث طرق: CLI، Python API، وخادم MCP. تشترك هذه الطرق في نفس قدرات الترجمة، لكن كل واحدة تناسب سير عمل مختلف.

استخدم هذه الصفحة عندما تقرر من أين تبدأ.

**إذا كنت تعدل الترجمات يدويًا:** تقوم طرق العمل الافتراضية لـ CLI وActions بإعادة ترجمة ملفات المصدر التي تم تغييرها بالكامل، لذا قد تُستبدَل صياغتك في تلك الملفات. راجع الفروقات قبل قبول التحديث. للحفاظ على مستوى كتل Markdown للتعديلات المقبولة، استخدم المزود الاختياري [مزود حالة ترجمة Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## قرار سريع

| إذا أردت... | استخدم | ابدأ من هنا |
| --- | --- | --- |
| ترجمة أو مراجعة مستودع من الطرفية | CLI | [مرجع CLI](cli.md) |
| أضف الترجمة إلى سكربت Python أو خدمة أو دفتر ملاحظات أو مهمة CI | Python API | [Python API](api.md) |
| دَع وكيلاً أو محررًا أو عميلًا متوافقًا مع MCP يترجم المحتوى نيابةً عنك | MCP Server | [MCP Server](mcp.md) |
| ترجمة مستند Markdown واحد أو دفتر ملاحظات أو صورة قام تطبيقك بتحميلها بالفعل | Python API أو MCP Server | [Python API](api.md) أو [MCP Server](mcp.md) |
| ترجمة مستودع كامل مع مجلدات إخراج وبيانات وصفية قياسية | CLI أو `run_translation` | [مرجع CLI](cli.md) أو [Python API](api.md) |

## استخدم CLI عندما

اختر CLI عندما يقوم شخص أو مهمة CI بتشغيل ترجمة المستودع من الطرفية.

CLI هو المسار الأكثر مباشرة عندما تريد من Co-op Translator اكتشاف ملفات المشروع، إنشاء مخرجات مترجمة، الحفاظ على بنية المشروع، تحديث البيانات الوصفية، وتشغيل أوامر المراجعة.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

هذا المثال يترجم Markdown ودفاتر الملاحظات. أضف `-img` فقط بعد تهيئة [Azure AI Vision](configuration.md#azure-ai-vision). بالنسبة لتشغيل أول يقتصر على Markdown فقط، اتبع [ترجمتك الأولى](first-translation.md).

مناسب في الحالات التالية:

- أنت تترجم مستودعًا من الطرفية.
- تريد أمرًا قابلاً لإعادة التشغيل لعمليات CI أو سير عمل الإصدارات.
- تريد اكتشاف المشروع المدمج، مسارات الإخراج، البيانات الوصفية، التنظيف، والمراجعة.
- تفضل واجهة الأوامر بدلاً من كتابة كود Python.

## استخدم Python API عندما

اختر Python API عندما يجب أن يتحكم كودك في سير العمل.

تكون الواجهة مفيدة للتطبيقات، سكربتات الأتمتة، دفاتر الملاحظات، الخدمات، وخطوط الأنابيب المخصصة. تتيح لك استدعاء واجهات ترجمة المحتوى منخفضة المستوى لملفات فردية، أو تشغيل نفس تنظيم سير العمل على مستوى المستودع المستخدم بواسطة CLI.

ترجم مستند Markdown واحد وقرّر مكان حفظه:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

شغّل ترجمة مستودع من Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

مناسب في الحالات التالية:

- تطبيقك يقرأ بالفعل ملفات أو بافرات أو دفاتر ملاحظات أو بايتات صور.
- تحتاج إلى تحقق مخصص، تخزين، تسجيل، عمليات إعادة المحاولة، أو سير عمل للموافقة.
- تريد ترجمة مستند واحد أو دفتر ملاحظات أو صورة دون معالجة مستودع كامل.
- تريد ترجمة المستودع، لكن من أتمتة Python بدلاً من أمر shell.

## استخدم خادم MCP عندما

اختر خادم MCP عندما يجب على وكيل أو محرر أو عميل متوافق مع MCP استدعاء أدوات Co-op Translator.

في الإعداد المحلي العادي، لا يقوم المستخدم بإبقاء الخادم قيد التشغيل يدويًا. يقوم عميل MCP بتشغيل `co-op-translator-mcp` عبر `stdio` عندما يحتاج الأدوات.

أمثلة على طلبات المستخدم التي يمكن للوكيل التعامل معها:

- "ترجم ملف Markdown هذا إلى الكورية واحتفظ بالروابط صحيحة."
- "ترجم ملف Markdown هذا إلى الكورية باستخدام سير عمل MCP بمساعدة الوكيل، مستخدمًا نموذجك الخاص للأجزاء المترجمة."
- "ترجم دفتر الملاحظات هذا إلى الكورية، احتفظ بخلايا الكود، واستخدم Co-op Translator MCP لإعادة بناء دفتر الملاحظات."
- "ترجم النص في هذه الصورة إلى اليابانية واحفظ النتيجة."
- "قم بمحاكاة ترجمة مستودع إلى الإسبانية وأخبرني بما سيتغير."
- "راجع ما إذا كانت مخرجات الترجمة الكورية محدّثة."

بالنسبة لـ Markdown ودفاتر الملاحظات، يمكن لـ MCP العمل في وضعين:

| الوضع | استخدم عندما | الأدوات الرئيسية |
| --- | --- | --- |
| بمساعدة الوكيل | يجب على وكيل مضيف MCP ترجمة الأجزاء باستخدام نموذجه الخاص، دون بيانات اعتماد مزود LLM الخاصة بـ Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| مدعوم بواسطة مزود | يجب على Co-op Translator استدعاء Azure OpenAI أو OpenAI أو Anthropic مباشرةً. | `translate_markdown_content`, `translate_notebook_content` |

شكل استدعاء أداة Markdown المدعومة بواسطة المزود في MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

شكل استدعاء أداة الصور في MCP:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

تكون ترجمة المستودع عبر MCP افتراضيًا في وضع المحاكاة:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

مناسب في الحالات التالية:

- تريد سير عمل للترجمة بلغة طبيعية داخل وكيل أو محرر.
- تريد ترجمة Markdown أو دفاتر ملاحظات حيث يترجم نموذج وكيل المضيف الأجزاء المُعدة.
- تريد أن يترجم الوكيل المحتوى المحدد بدلاً من المستودع بأكمله.
- تريد خطوة موافقة قبل عمليات الكتابة على مستوى المستودع.
- تريد واجهة واحدة تعرض أدوات Markdown ودفاتر الملاحظات والصور والمراجعة وإعادة كتابة المسارات.

## كيف تتكامل معًا

CLI هو الخيار الافتراضي الأفضل للبشر الذين يترجمون المستودعات. Python API هو الأفضل عندما يتولى كودك سير العمل. خادم MCP هو الأفضل عندما يتولى وكيل أو محرر سير العمل.

جميع المسارات الثلاثة تستخدم نفس واجهة Co-op Translator العامة، لذا يمكنك البدء بـ CLI، ثم الأتمتة باستخدام Python لاحقًا، وكشف نفس القدرات لعملاء MCP عندما تحتاج إلى سير عمل يقوده الوكيل.