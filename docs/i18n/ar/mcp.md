# خادم MCP

يتضمن Co-op Translator خادماً لبروتوكول سياق النموذج للعوامل والمحرّرين والعملاء المتوافقين مع MCP.

في الإعداد المحلي الافتراضي، لا يحتفظ المستخدمون بخادم منفصل يعمل يدوياً. يقومون بتكوين عميل MCP الخاص بهم، ويقوم العميل بتشغيل `co-op-translator-mcp` تلقائياً عبر `stdio` عندما يحتاج إلى أدوات Co-op Translator.

إذا كنت تقرر بين CLI وPython API وMCP، ابدأ بـ [اختر سير العمل](workflows.md).

استخدم MCP عندما يجب على وكيل أو محرر استدعاء Co-op Translator مباشرةً:

| هدف المستخدم | أدوات MCP |
| --- | --- |
| ترجمة مستند Markdown واحد أو دفتر ملاحظات أو صورة | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ترجمة محتوى Markdown أو دفتر الملاحظات باستخدام نموذج الوكيل المضيف | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| إعادة كتابة روابط Markdown أو دفتر الملاحظات المترجمة بعد اختيار مسار الإخراج | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ترجمة مستودع كامل مثل CLI | `run_translation`, `translate_project` |
| مراجعة المخرجات المترجمة بدون بيانات اعتماد LLM | `run_review` |
| فحص القدرات وحالة البيئة | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

يغلف خادم MCP نفس واجهة برمجة بايثون العامة الموثقة في [Python API](api.md). تستخدم الأدوات المدعومة من المزود نفس المزودين المكوَّنين مثل CLI وواجهة Python. تُعد الأدوات المساعدة المعتمدة على الوكيل القطع للوكيل المضيف لترجمتها، ثم تستخدم Co-op Translator لإعادة بناء Markdown أو دفتر الملاحظات النهائي.

## الخطوة 1: تثبيت وتكوين Co-op Translator

ثبّت Co-op Translator في بيئة Python التي سيستخدمها عميل MCP الخاص بك:

```bash
pip install co-op-translator
```

للتطوير المحلي من هذا المستودع، ثبّت الحزمة في وضع قابل للتحرير:

```bash
pip install -e .
```

اختر وضع الترجمة الذي سيستخدمه عميل MCP الخاص بك:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | تستدعي Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, أو `run_translation`. | تتطلب الترجمة Azure OpenAI أو OpenAI أو Anthropic. تتطلب ترجمة الصور أيضًا Azure AI Vision. |
| Agent-assisted | يترجم الوكيل المضيف قطع المحتوى التي تم إرجاعها بواسطة `start_markdown_agent_translation` أو `start_notebook_agent_translation`. | لا تتطلب قطع Markdown أو دفتر الملاحظات بيانات اعتماد مزود LLM لـ Co-op Translator. لم يتم تغطية ترجمة الصور بعد بواسطة وضع المساعدة بالوكيل. |

إذا بدأت بترجمة Markdown أو دفاتر الملاحظات داخل وكيل مثل Codex أو Claude Code، فابدأ بوضع المساعدة بالوكيل. استخدم وضع المدعوم بالمزود عندما تريد أن يقوم Co-op Translator نفسه باستدعاء المزودين المكوَّنين لديك، أو عند ترجمة الصور، أو عند تشغيل ترجمة على مستوى المستودع مثل CLI.

قم بتكوين مزود واحد لعمليات سير العمل المدعومة بالمزود:

```bash
# أزور أوبن إيه آي
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# أو أوبن إيه آي
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# أو أنثروبيك
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

تتطلب ترجمة الصور المدعومة بالمزود إضافياً:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    يغطي وضع المساعدة بالوكيل حالياً Markdown وخلايا Markdown في دفاتر الملاحظات. لا تزال ترجمة الصور تستخدم خط معالجة الصور المدعوم بالمزود وتتطلب Azure AI Vision لأغراض OCR والتصيير المدرك للتخطيط.

## الخطوة 2: تكوين عميل MCP الخاص بك

للإعداد المحلي العادي عبر `stdio`، أضف Co-op Translator إلى تكوين عميل MCP الخاص بك. سيقوم العميل بتشغيل وإيقاف العملية تلقائياً.

تكوين الحزمة المثبتة:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

تكوين النسخة المصدرية على Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

تكوين النسخة المصدرية على macOS أو Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

بعد تغيير تكوين عميل MCP، أعد تشغيل العميل أو أعد تحميله ليتمكن من اكتشاف الخادم الجديد.

## الخطوة 3: التحقق من الخادم في العميل

اطلب من عميل MCP عرض الأدوات المتاحة، أو استدعِ أحد المساعدين للقراءة فقط أولاً:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

فحوصات أولية مفيدة:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | يؤكد أن الخادم يمكن الوصول إليه ويعرض سير العمل المتاحة. |
| `list_supported_languages` | يؤكد أن بيانات اللغة المجمعة يمكن تحميلها. |
| `get_configuration_status` | يؤكد توفر موفر LLM وموفر Vision دون كشف القيم السرية. |

## الخطوة 4: اختر سير العمل

### ترجمة ملفات أو مستندات فردية

استخدم أدوات المحتوى المدعومة بالمزود عندما يحتوي عميل MCP بالفعل على محتوى المستند أو مسار الصورة ويجب أن يستدعي Co-op Translator مزودي الترجمة المكوّنين.

بالنسبة لـ Markdown:

1. استدعِ `translate_markdown_content` مع `document` و`language_code` واختياريًا `source_path`.
2. إذا كان من المقرر كتابة النتيجة المترجمة ضمن تنسيق إخراج Co-op Translator، استدعِ `rewrite_markdown_paths`.
3. دع العميل يكتب أو يعيد الـ `content` النهائي.

بالنسبة لدفاتر الملاحظات:

1. استدعِ `translate_notebook_content` مع JSON الدفتر و`language_code`.
2. استدعِ `rewrite_notebook_paths` إذا كانت روابط الدفتر المترجمة بحاجة إلى تعديل لمسار الهدف.
3. اكتب أو أعد JSON الدفتر النهائي.

بالنسبة للصور:

1. استدعِ `translate_image_content` مع `image_path` و`language_code` و`root_dir` أو `fast_mode` الاختياري.
2. اقرأ الـ `data_base64` و`mime_type` المُرجعتين.
3. إذا تم توفير `output_path`، تُحفظ الصورة المترجمة أيضًا في ذلك المسار.

لا تقوم أدوات المحتوى باكتشاف المشروع أو تحديث البيانات الوصفية أو إضافة التنصلات أو إعادة كتابة المسارات تلقائياً. إذا أردت أن يترجم الوكيل المضيف قطع Markdown أو دفاتر الملاحظات دون بيانات اعتماد مزود LLM لـ Co-op Translator، فاستخدم سير العمل المساعدة بالوكيل أدناه.

### الترجمة باستخدام نموذج الوكيل المضيف

استخدم أدوات المساعدة بالوكيل عندما تريد من وكيل MCP المضيف، مثل مساعد الترميز، أن ينتج النص المترجم بدلاً من تكوين موفر LLM لـ Co-op Translator.

في عميل MCP القائم على الدردشة، عادةً لا تحتاج لكتابة JSON الأداة بنفسك. اطلب من الوكيل استخدام سير العمل المساعدة بالوكيل:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

بالنسبة لدفاتر الملاحظات، استخدم نفس النمط:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

إذا كان عميل MCP الخاص بك يدعم محاور الخادم، استخدم `agent_assisted_markdown_translation_prompt` ليقوم العميل بتحميل تعليمات سير العمل نفسها.

بالنسبة لـ Markdown:

1. استدعِ `start_markdown_agent_translation` مع `document` و`language_code` واختياريًا `source_path`.
2. ترجم كل قطعة (`chunk`) مُعادة في الوكيل المضيف باتباع الـ `prompt` الخاص بها.
3. استدعِ `finish_markdown_agent_translation` مع الـ `job` الأصلي والقطع المترجمة مستخدماً `chunk_id` و`translated_text`.
4. إذا كان من المقرر كتابة المحتوى إلى مسار هدف مترجم، استدعِ `rewrite_markdown_paths`.

بالنسبة لدفاتر الملاحظات:

1. استدعِ `start_notebook_agent_translation` مع JSON الدفتر و`language_code`.
2. ترجم كل قطعة مُعادة في الوكيل المضيف.
3. استدعِ `finish_notebook_agent_translation` مع الـ `job` الأصلي والقطع المترجمة.
4. استدعِ `rewrite_notebook_paths` إذا كانت روابط الدفتر المترجمة بحاجة إلى تعديل لمسار الهدف.

لا تستدعي أدوات المساعدة بالوكيل موفر LLM المكوّن من Co-op Translator. الوكيل المضيف مسؤول عن ترجمة القطع المُعادة. يتولى Co-op Translator تقسيم Markdown إلى قطع، والحفاظ على العناصر النائبة، وإعادة بناء frontmatter، واستبدال خلايا الدفتر، والتقويم بعد الترجمة.

### ترجمة مستودع كامل

استخدم `run_translation` عندما يريد المستخدم أن يتصرف Co-op Translator مثل أمر CLI `translate`.

افتراضيًا تكون ترجمة المستودع بـ `dry_run=true` حتى يتمكن الوكيل من فحص النطاق قبل تغييرات الملفات:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

تتضمن نتيجة `run_translation` مصفوفة `events` مع أحداث تقدم مؤرشفة بإصدار
`co-op.translation.event.v1`. ينبغي على عملاء MCP استخدام حقول مثل
`type`, `stage_key`, `completed`, `total`, و`current_path` بدلًا من
تحليل نص وحدة التحكم المُلتقَط. مرّر `json_events_path` لكتابة تلك الأحداث
أيضًا إلى ملف NDJSON.

للسماح بالكتابة، يجب على المستدعي تعيين كل من `dry_run=false` و`confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

يتم كشف `translate_project` كتسمية توافقية لـ `run_translation`.

### مراجعة المخرجات المترجمة

استخدم `run_review` للتحقق الحتمي الذي لا يتطلب بيانات اعتماد LLM أو Vision:

!!! note "نسخة تجريبية"
    يكشف MCP واجهة برمجة تطبيقات الإصدار التجريبي `run_review`. هي آمنة لعمليات المراجعة للقراءة فقط، لكن قد تتغير فحوصات المراجعة ومخططات القضايا.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

تتضمن النتيجة إخراج نصي مُلتقَط وملخص مراجعة منظم عندما يكون متاحًا.

## تشغيل الخادم يدوياً

عمليات التشغيل اليدوية مخصصة أساسًا للتصحيح أو للنواقل التي تتصرف كخوادم طويلة الأجل.

قم بتصحيح خادم stdio الافتراضي:

```bash
co-op-translator-mcp
```

التشغيل من نسخة المصدر:

```bash
python -m co_op_translator.mcp.server
```

تشغيل خادم HTTP أو SSE طويل العمر:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

للتكاملات المحلية مع المحرر والوكيل، افضّل تكوين `stdio` المدار من قبل العميل في الخطوة 2.

## الأدوات

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | ترجمة سلسلة Markdown. | لا |
| `translate_notebook_content` | ترجمة خلايا Markdown في JSON الدفتر. | لا |
| `translate_image_content` | ترجمة النص في صورة واحدة وإرجاع بيانات الصورة base64. | اختياري، فقط عندما يتم توفير `output_path` |
| `start_markdown_agent_translation` | إعداد قطع Markdown ليترجمها الوكيل المضيف دون بيانات اعتماد موفر Co-op Translator. | لا |
| `finish_markdown_agent_translation` | إعادة بناء Markdown من القطع المترجمة من الوكيل المضيف. | لا |
| `start_notebook_agent_translation` | إعداد قطع خلايا Markdown في الدفتر ليترجمها الوكيل المضيف. | لا |
| `finish_notebook_agent_translation` | إعادة بناء JSON الدفتر من القطع المترجمة من الوكيل المضيف. | لا |
| `rewrite_markdown_paths` | إعادة كتابة مسارات جسم Markdown وfrontmatter لمسار هدف مترجم. | لا |
| `rewrite_notebook_paths` | إعادة كتابة المسارات داخل خلايا Markdown في الدفتر. | لا |
| `run_translation` | تشغيل ترجمة مستوى المشروع مثل CLI. | نعم عندما `dry_run=false` و`confirm_write=true` |
| `translate_project` | تسمية توافقية لـ `run_translation`. | نعم عندما `dry_run=false` و`confirm_write=true` |
| `run_review` | تشغيل فحوصات مراجعة حتمية. | لا |
| `get_configuration_status` | الإبلاغ عن موفري LLM وVision المكوّنين دون كشف الأسرار. | لا |
| `list_supported_languages` | سرد رموز اللغات الهدف المدعومة. | لا |
| `get_api_overview` | وصف سير العمل والأدوات المتاحة. | لا |

## الموارد

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | نظرة JSON عامة على سير العمل والأدوات. |
| `co-op://supported-languages` | قائمة JSON برموز اللغات المدعومة. |
| `co-op://configuration` | ملخص توفر الموفرين بصيغة JSON دون أسرار. |

## مطالبات

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | إرشاد عميل MCP خلال ترجمة المحتوى بالإضافة إلى إعادة كتابة المسارات الاختيارية. |
| `agent_assisted_markdown_translation_prompt` | إرشاد عميل MCP خلال ترجمة Markdown بواسطة الوكيل المضيف دون بيانات اعتماد موفر Co-op Translator. |
| `translate_repository_prompt` | إرشاد عميل MCP خلال ترجمة المستودع التي تبدأ بمُعاينة (dry-run) أولاً. |

## أمثلة للنسخ واللصق

ترجمة محتوى Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

إعادة كتابة روابط Markdown المترجمة:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

ترجمة Markdown باستخدام نموذج الوكيل المضيف:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

بعد أن يترجم الوكيل المضيف كل قطعة مُرجعة، أنهِ المهمة باستخدام كائن الـ `job` الكامل المُعاد من `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

معاينة ترجمة المستودع:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## استكشاف الأخطاء وإصلاحها

| Problem | What to try |
| --- | --- |
| لا يستطيع عميل MCP العثور على `co-op-translator-mcp`. | استخدم مسار تنفيذ Python المطلق وتكوين النسخة المصدرية `["-m", "co_op_translator.mcp.server"]`. |
| يتم إدراج الخادم لكن الترجمة تفشل. | استدعِ `get_configuration_status` وتأكد من توفر مزود LLM. |
| تريد ترجمة Markdown أو دفتر الملاحظات بدون بيانات اعتماد المزود. | استخدم `start_markdown_agent_translation` / `finish_markdown_agent_translation` أو ما يعادله في الدفتر حتى يقوم الوكيل المضيف بترجمة القطع. |
| تفشل ترجمة الصورة. | تأكد من تعيين متغيرات Azure AI Vision واستدعِ `get_configuration_status`. |
| لا تكتب ترجمة المستودع ملفات. | عيّن `dry_run=false` و`confirm_write=true` فقط بعد موافقة صريحة من المستخدم. |
| لا تظهر تغييرات في تكوين العميل. | أعد تشغيل أو أعد تحميل عميل MCP. |

## ملاحظات السلامة

- استدعاءات أدوات MCP مُتحكم بها من النموذج من قبل التطبيق المضيف، لذا تكون ترجمة المستودع افتراضيًا في وضع المعاينة (dry-run).
- يمكن أن تؤدي الترجمة الكاملة للمستودع إلى إنشاء أو تحديث أو إزالة العديد من الملفات. اشترِط موافقة صريحة من المستخدم قبل تعيين `confirm_write=true`.
- أداة حالة التكوين لا تُرجع أبداً مفاتيح API أو نقاط النهاية أو قيمًا سرية أخرى.
- ترجع ترجمة الصور بيانات صورة بصيغة base64. يمكن أن تنتج الصور الكبيرة استجابات أدوات كبيرة.
- تُعيد أدوات المساعدة بالوكيل قطع المصدر والمطالبات إلى مضيف MCP. استخدمها فقط مع المحتوى الذي يوافق المستخدم على إرساله إلى نموذج الوكيل المضيف ذلك.