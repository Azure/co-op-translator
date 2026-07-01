# MCP Server

يتضمن Co-op Translator خادم بروتوكول سياق النموذج (Model Context Protocol) للوكلاء والمحررات والعملاء المتوافقين مع MCP.

بالإعداد المحلي الافتراضي، لا يحتفظ المستخدمون بخادم منفصل يعمل يدويًا. يقومون بتكوين عميل MCP الخاص بهم، ويقوم العميل بتشغيل `co-op-translator-mcp` تلقائيًا عبر `stdio` عند حاجته إلى أدوات Co-op Translator.

إذا كنت تقرر بين واجهة سطر الأوامر، واجهة Python، وMCP، فابدأ بـ [اختر سير العمل الخاص بك](workflows.md).

استخدم MCP عندما يجب على وكيل أو محرر استدعاء Co-op Translator مباشرة:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

يغلف خادم MCP نفس واجهة برمجة تطبيقات Python العامة الموثقة في [Python API](api.md). تستخدم الأدوات التي تعتمد على المزودين نفس المزودين المُكوَّنين كما في CLI وواجهة Python. تقوم الأدوات بمساعدة الوكيل بتحضير الأجزاء ليترجمها وكيل المضيف لـ MCP، ثم تستخدم Co-op Translator لإعادة بناء Markdown أو المفكرة النهائية.

## Step 1: Install and Configure Co-op Translator

ثبت Co-op Translator في بيئة Python التي سيستخدمها عميل MCP الخاص بك:

```bash
pip install co-op-translator
```

للتطوير المحلي من هذا المستودع، قم بتثبيت الحزمة في وضع التحرير:

```bash
pip install -e .
```

اختر وضع الترجمة الذي سيستخدمه عميل MCP الخاص بك:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

إذا كنت تبدأ بترجمة Markdown أو مفكرة داخل وكيل مثل Codex أو Claude Code، فابدأ بوضع agent-assisted. استخدم وضع provider-backed عندما تريد أن يستدعي Co-op Translator المزودين المُكوَّنين بنفسه، أو عندما تترجم الصور، أو عندما تقوم بترجمة على مستوى المستودع مثل واجهة سطر الأوامر.

قم بتكوين بيانات اعتماد المزود فقط لمسارات العمل التي تعتمد على المزود:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

تتطلب ترجمة الصور التي تعتمد على المزود أيضًا:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    يغطي وضع agent-assisted حاليًا Markdown وخلايا Markdown في المفكرات. تظل ترجمة الصور تستخدم أنبوب الصور الذي يعتمد على المزود وتحتاج إلى Azure AI Vision لأجل OCR والتصيير الواعي بالتخطيط.

## Step 2: Configure Your MCP Client

لإعداد `stdio` المحلي العادي، أضف Co-op Translator إلى تكوين عميل MCP الخاص بك. سيقوم العميل بتشغيل العملية وإيقافها تلقائيًا.

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

تكوين نسخة المصدر على Windows:

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

تكوين نسخة المصدر على macOS أو Linux:

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

بعد تغيير تكوين عميل MCP، أعد تشغيل العميل أو أعد تحميله حتى يتمكن من اكتشاف الخادم الجديد.

## Step 3: Verify the Server in the Client

اطلب من عميل MCP سرد الأدوات المتاحة، أو استدعِ واحدة من أدوات المساعدة فقط للقراءة أولاً:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

فحوصات مفيدة أولية:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | يؤكد أن الخادم قابل للوصول ويعرض سير العمل المتاحة. |
| `list_supported_languages` | يؤكد أنه يمكن تحميل بيانات اللغة المعبأة. |
| `get_configuration_status` | يؤكد توفر مزود LLM وVision دون الكشف عن القيم السرية. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

استخدم أدوات المحتوى التي تعتمد على المزود عندما يمتلك عميل MCP بالفعل محتوى الوثيقة أو مسار الصورة ويجب أن يستدعي Co-op Translator مزودي الترجمة المُكوَّنين.

بالنسبة لـ Markdown:

1. استدعِ `translate_markdown_content` مع `document` و`language_code` و`source_path` اختياريًا.
2. إذا كان سيتم كتابة النتيجة المترجمة داخل تخطيط مخرجات Co-op Translator، استدعِ `rewrite_markdown_paths`.
3. دع العميل يكتب أو يُعيد `content` النهائي.

بالنسبة للمفكرات:

1. استدعِ `translate_notebook_content` مع JSON المفكرة و`language_code`.
2. استدعِ `rewrite_notebook_paths` إذا كانت روابط المفكرة المترجمة تحتاج ضبطًا لمسار الهدف.
3. اكتب أو أعد JSON المفكرة النهائي.

بالنسبة للصور:

1. استدعِ `translate_image_content` مع `image_path` و`language_code` و`root_dir` اختياري أو `fast_mode`.
2. اقرأ الحقل المعاد `data_base64` و`mime_type`.
3. إذا تم توفير `output_path`، فسيتم أيضًا حفظ الصورة المترجمة في ذلك المسار.

أدوات المحتوى لا تجري اكتشاف المشروع، أو تحديثات البيانات الوصفية، أو إخلاءات المسؤولية، أو إعادة كتابة المسارات تلقائيًا. إذا كنت تريد من وكيل المضيف ترجمة أجزاء Markdown أو المفكرة بدون بيانات اعتماد موفر LLM من Co-op Translator، فاستخدم سير العمل المدعوم بالوكيل أدناه.

### Translate with the Host Agent Model

استخدم الأدوات المدعومة بالوكيل عندما تريد من وكيل المضيف لـ MCP، مثل مساعد الترميز، إنتاج النص المترجم بدلًا من تكوين Azure OpenAI أو OpenAI لـ Co-op Translator.

في عميل MCP القائم على الدردشة، عادةً لا تحتاج إلى كتابة JSON للأداة بنفسك. اطلب من الوكيل استخدام سير العمل المدعوم بالوكيل:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

للمفكرات، استخدم نفس النمط:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

إذا كان عميل MCP يدعم مطالبات الخادم، استخدم `agent_assisted_markdown_translation_prompt` ليقوم العميل بتحميل نفس تعليمات سير العمل.

بالنسبة لـ Markdown:

1. استدعِ `start_markdown_agent_translation` مع `document` و`language_code` و`source_path` اختياريًا.
2. ترجم كل جزء معاد في وكيل المضيف باتباع `prompt` الخاص بالجزء.
3. استدعِ `finish_markdown_agent_translation` مع الـ `job` الأصلي والأجزاء المترجمة باستخدام `chunk_id` و`translated_text`.
4. إذا كان المحتوى سيُكتب إلى مسار هدف مترجم، استدعِ `rewrite_markdown_paths`.

بالنسبة للمفكرات:

1. استدعِ `start_notebook_agent_translation` مع JSON المفكرة و`language_code`.
2. ترجم كل جزء معاد في وكيل المضيف.
3. استدعِ `finish_notebook_agent_translation` مع الـ `job` الأصلي والأجزاء المترجمة.
4. استدعِ `rewrite_notebook_paths` إذا كانت روابط المفكرة المترجمة تحتاج ضبطًا لمسار الهدف.

أدوات المدعومة بالوكيل لا تستدعي Azure OpenAI أو OpenAI من Co-op Translator. وكيل المضيف مسؤول عن ترجمة الأجزاء المعادة. يتولى Co-op Translator تجزئة Markdown، والحفاظ على العناصر النائبة، وإعادة بناء frontmatter، واستبدال خلايا المفكرة، والتطبيع ما بعد الترجمة.

### Translate an Entire Repository

استخدم `run_translation` عندما يريد المستخدم أن يتصرف Co-op Translator مثل واجهة سطر الأوامر `translate`.

ترجمة المستودع افتراضيًا تكون بـ `dry_run=true` حتى يتمكن وكيل من فحص النطاق قبل تغييرات الملفات:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

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

يتم الكشف عن `translate_project` كاسم بديل للتوافق مع `run_translation`.

### Review Translated Output

استخدم `run_review` للفحوص الحتمية التي لا تتطلب بيانات اعتماد LLM أو Vision:

!!! note "بيتا"
    يكشف MCP عن واجهة برمجة تطبيقات beta `run_review`. هي آمنة لسير عمل المراجعة للقراءة فقط، لكن فحوص المراجعة ومخططات المشكلات قد تتطور.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

تتضمن النتيجة نصًا مُلتَقَطًا ومُلخص مراجعة مُهيكل عند التوفر.

## Manual Server Runs

تشغيلات الخادم اليدوية مخصصة أساسًا للتصحيح أو للناقلات التي تتصرف كخوادم طويلة العمر.

صَحِّح خادم stdio الافتراضي:

```bash
co-op-translator-mcp
```

شغّل من نسخة مصدر:

```bash
python -m co_op_translator.mcp.server
```

شغّل خادم HTTP أو SSE طويل الأمد:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

لتكاملات المحرر والوكيل المحلية، فضّل تكوين `stdio` المدار من قبل العميل في الخطوة 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | ترجمة سلسلة Markdown. | No |
| `translate_notebook_content` | ترجمة خلايا Markdown في JSON المفكرة. | No |
| `translate_image_content` | ترجمة النص في صورة واحدة وإرجاع بيانات الصورة base64. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | تحضير أجزاء Markdown لكي يترجمها وكيل المضيف بدون بيانات اعتماد LLM من Co-op Translator. | No |
| `finish_markdown_agent_translation` | إعادة بناء Markdown من الأجزاء المترجمة بواسطة وكيل المضيف. | No |
| `start_notebook_agent_translation` | تحضير أجزاء خلايا Markdown في المفكرة لكي يترجمها وكيل المضيف. | No |
| `finish_notebook_agent_translation` | إعادة بناء JSON المفكرة من الأجزاء المترجمة بواسطة وكيل المضيف. | No |
| `rewrite_markdown_paths` | إعادة كتابة مسارات جسم Markdown وfrontmatter لمسار هدف مترجم. | No |
| `rewrite_notebook_paths` | إعادة كتابة المسارات داخل خلايا Markdown بالمفكرة. | No |
| `run_translation` | تشغيل ترجمة على مستوى المشروع مثل واجهة سطر الأوامر. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | اسم بديل للتوافق مع `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | تشغيل فحوص مراجعة حتمية. | No |
| `get_configuration_status` | الإبلاغ عن موفري LLM وVision المُكوَّنين دون الكشف عن الأسرار. | No |
| `list_supported_languages` | سرد رموز اللغات المستهدفة المدعومة. | No |
| `get_api_overview` | وصف سير العمل وأدوات MCP المتاحة. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | إرشاد عميل MCP عبر ترجمة المحتوى بالإضافة إلى إعادة كتابة المسارات الاختيارية. |
| `agent_assisted_markdown_translation_prompt` | إرشاد عميل MCP عبر ترجمة Markdown بواسطة وكيل المضيف دون بيانات اعتماد مزود LLM من Co-op Translator. |
| `translate_repository_prompt` | إرشاد عميل MCP عبر ترجمة المستودع مع خيار التنفيذ التجريبي أولًا. |

## Copy-Paste Examples

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
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

ترجمة Markdown باستخدام نموذج وكيل المضيف:

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

بعد أن يترجم وكيل المضيف كل جزء معاد، أنهِ الوظيفة باستخدام كائن `job` الكامل المعاد من `start_markdown_agent_translation`:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- استدعاءات أدوات MCP يتم التحكم فيها بواسطة النموذج في التطبيق المضيف، لذا تكون ترجمة المستودع تجريبيًا افتراضيًا.
- يمكن أن تُنشئ ترجمة المستودع الكاملة أو تُحدّث أو تُزيل العديد من الملفات. اشترط موافقة صريحة من المستخدم قبل تعيين `confirm_write=true`.
- أداة حالة التكوين لا تُرجع أبدًا مفاتيح API أو نقاط النهاية أو قيمًا سرية أخرى.
- ترجمة الصور تُرجع بيانات صورة base64. قد تنتج الصور الكبيرة استجابات أدوات كبيرة.
- تعيد الأدوات المدعومة بالوكيل أجزاء المصدر والمطالبات إلى مضيف MCP. استخدمها فقط مع المحتوى الذي يشعر المستخدم بالراحة لإرساله إلى نموذج وكيل المضيف ذاك.