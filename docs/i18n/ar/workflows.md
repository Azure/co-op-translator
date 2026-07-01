# اختر سير عملك

Co-op Translator يمكن استخدامه بثلاث طرق: CLI، وPython API، وخادم MCP. تشترك كلها في نفس قدرات الترجمة، لكن كل منها يناسب سير عمل مختلف.

استخدم هذه الصفحة عندما تقرر من أين تبدأ.

## قرار سريع

| إذا أردت... | استخدم | ابدأ هنا |
| --- | --- | --- |
| ترجمة أو مراجعة مستودع من الطرفية | CLI | [مرجع CLI](cli.md) |
| إضافة الترجمة إلى سكربت Python، أو خدمة، أو دفتر ملاحظات، أو مهمة CI | Python API | [Python API](api.md) |
| دع وكيلاً أو محرراً أو عميلًا متوافقًا مع MCP يترجم المحتوى نيابة عنك | MCP Server | [خادم MCP](mcp.md) |
| ترجم مستند Markdown واحد أو دفتر ملاحظات أو صورة قام تطبيقك بتحميلها بالفعل | Python API أو خادم MCP | [Python API](api.md) أو [خادم MCP](mcp.md) |
| ترجم مستودعًا كاملاً مع مجلدات إخراج قياسية والبيانات الوصفية | CLI أو `run_translation` | [مرجع CLI](cli.md) أو [Python API](api.md) |

## استخدم CLI عندما

اختر CLI عندما يقوم شخص أو مهمة CI بترجمة المستودع من الطرفية.

CLI هو الطريق الأكثر مباشرة عندما تريد من Co-op Translator اكتشاف ملفات المشروع، وإنشاء مخرجات مترجمة، والحفاظ على تخطيط المشروع، وتحديث البيانات الوصفية، وتشغيل أوامر المراجعة.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

ملائم في الحالات التالية:

- أنت تترجم مستودعًا من الطرفية.
- تريد أمرًا قابلًا للتكرار لعمليات CI أو سير عمل النشر.
- تريد اكتشاف المشروع المدمج، ومسارات الإخراج، والبيانات الوصفية، والتنظيف، والمراجعة.
- تفضل واجهة أوامر بدلاً من كتابة كود Python.

## استخدم Python API عندما

اختر Python API عندما يجب أن يتحكم كودك بسير العمل.

تكون الواجهة مفيدة للتطبيقات، سكربتات الأتمتة، دفاتر الملاحظات، الخدمات، وخطوط الأنابيب المخصصة. تتيح لك استدعاء واجهات ترجمة المحتوى منخفضة المستوى للملفات الفردية، أو تشغيل نفس تنسيق التنسيق على مستوى المستودع المستخدم من قبل CLI.

ترجم مستند Markdown واحد وقرر أين تحفظه:

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

ملائم في الحالات التالية:

- تطبيقك يقرأ بالفعل ملفات أو بافرات أو دفاتر ملاحظات أو بايتات صور.
- تحتاج إلى تحقق مخصص، أو تخزين، أو تسجيل، أو محاولات إعادة، أو مسارات موافقة.
- تريد ترجمة مستند واحد أو دفتر ملاحظات أو صورة دون معالجة مستودع كامل.
- تريد ترجمة المستودع، لكن من أتمتة Python بدلًا من أمر صدفي.

## استخدم خادم MCP عندما

اختر خادم MCP عندما يجب أن يستدعي وكيل أو محرر أو عميل متوافق مع MCP أدوات Co-op Translator.

في الإعداد المحلي العادي، لا يقوم المستخدم بتشغيل خادم يدويًا. يبدأ عميل MCP `co-op-translator-mcp` عبر `stdio` عندما يحتاج إلى الأدوات.

أمثلة لطلبات المستخدم التي يمكن أن يتعامل معها وكيل:

- "ترجم هذا الملف Markdown إلى الكورية وحافظ على صحة الروابط."
- "ترجم هذا الملف Markdown إلى الكورية عبر سير عمل MCP بمساعدة الوكيل، باستخدام نموذجك الخاص للأجزاء المترجمة."
- "ترجم هذا دفتر الملاحظات إلى الكورية، واحفظ خلايا الكود، واستخدم Co-op Translator MCP لإعادة بناء دفتر الملاحظات."
- "ترجم النص في هذه الصورة إلى اليابانية واحفظ النتيجة."
- "قم بتشغيل ترجمة مستودع كتشغيل تجريبي إلى الإسبانية وأخبرني بما سيتغير."
- "راجع ما إذا كان مخرج الترجمة إلى الكورية محدثًا."

بالنسبة إلى Markdown ودفاتر الملاحظات، يمكن لـ MCP العمل في وضعين:

| الوضع | متى تستخدم | الأدوات الرئيسية |
| --- | --- | --- |
| بمساعدة الوكيل | يجب أن يترجم وكيل المضيف في MCP الأجزاء باستخدام نموذجه الخاص، دون بيانات اعتماد موفر LLM الخاصة بـ Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| مدعوم من المزود | يجب على Co-op Translator استدعاء Azure OpenAI أو OpenAI مباشرة. | `translate_markdown_content`, `translate_notebook_content` |

شكل استدعاء أداة Markdown المدعومة بالمزود في MCP:

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

شكل استدعاء أداة الصورة في MCP:

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

ترجمة المستودع تتم كتجربة جافة افتراضيًا عبر MCP:

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

ملائم في الحالات التالية:

- تريد سير عمل ترجمة باللغة الطبيعية داخل وكيل أو محرر.
- تريد ترجمة Markdown أو دفاتر الملاحظات حيث يترجم نموذج وكيل المضيف الأجزاء المحضرة.
- تريد أن يترجم الوكيل محتوى محددًا بدلاً من مستودع كامل.
- تريد خطوة موافقة قبل الكتابات على مستوى المستودع.
- تريد واجهة واحدة تكشف عن أدوات Markdown، ودفاتر الملاحظات، والصور، والمراجعة، وإعادة كتابة المسارات.

## كيف تتناسب معًا

CLI هو الخيار الافضل بشكل افتراضي للبشر الذين يترجمون المستودعات. Python API هو الأفضل عندما يملك كودك سير العمل. خادم MCP هو الأفضل عندما يملك وكيل أو محرر سير العمل.

تستخدم المسارات الثلاثة نفس واجهة Co-op Translator العامة، لذا يمكنك البدء بـ CLI، وأتمتة العملية باستخدام Python لاحقًا، وكشف نفس القدرات لعملاء MCP عندما تحتاج إلى سير عمل يقوده الوكيل.