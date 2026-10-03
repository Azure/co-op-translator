# مرجع CLI

يقوم Co-op Translator بتثبيت نقاط إدخال سطر الأوامر التالية:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

تقوم أوامر `translate`, `evaluate`, `migrate-links`، و `co-op-review` بالتوجيه عبر `co_op_translator.__main__`، الذي يختار تنفيذ الأمر استنادًا إلى اسم البرنامج المستدعى. يستخدم خادم MCP `co_op_translator.mcp.server` مباشرة.

إذا كنت تحاول الاختيار بين CLI أو Python API أو MCP، ابدأ بـ [اختر سير عملك](workflows.md).

## إخراج وحدة التحكم

تستخدم المحطات التفاعلية تنسيق Rich لعنوان الأمر، شريط التقدم، والملخصات. أما في CI والمخرجات غير التفاعلية فتعود تلقائيًا إلى نص عادي.

اضبط `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` لإجبار الإخراج العادي، أو `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` لإجبار إخراج Rich. اضبط `CO_OP_TRANSLATOR_NO_PROGRESS=1` للحفاظ على الملخصات مع قمع أشرطة التقدم الحية.

استخدم `translate --json-events progress.ndjson` عندما يحتاج نظام آخر إلى
تقدم قابل للقراءة آليًا. يواصل CLI عرض محتوى مخصص للبشر، بينما
يتلقى ملف NDJSON أحداثًا ذات إصدار `co-op.translation.event.v1` مع
حقول ثابتة مثل `type`، `stage_key`، `completed`، `total`، و
`current_path`.

## سير عمل CLI للمرة الأولى

ابدأ من هنا إذا كنت تستخدم Co-op Translator من الطرفية:

1. قم بتكوين مزود نماذج لغوية كبيرة كما هو موضح في [التكوين](configuration.md).
2. اختر نوع المحتوى الذي تريد ترجمته.
3. شغّل أمرًا محددًا أولًا، مثل الترجمة الخاصة بملفات Markdown فقط.
4. استخدم `--dry-run` قبل تغييرات كبيرة في المستودع.
5. استخدم `co-op-review` بعد الترجمة للتحقق من البنية وحداثة المحتوى.

| الهدف | الأمر للبدء |
| --- | --- |
| ترجمة مستندات Markdown | `translate -l "ko" -md` |
| ترجمة دفاتر الملاحظات | `translate -l "ko" -nb` |
| ترجمة نصوص الصور | `translate -l "ko" -img` |
| معاينة العمل دون كتابة ملفات | `translate -l "ko" -md --dry-run` |
| مراجعة الترجمات الموجودة | `co-op-review -l "ko"` |
| تحديث روابط الدفاتر وملفات Markdown | `migrate-links -l "ko" --dry-run` |
| إتاحة الأدوات لعميل MCP | قم بتكوين [خادم MCP](mcp.md) بدلًا من تشغيل أوامر CLI مباشرة. |

## translate

ترجم ملفات Markdown ودفاتر الملاحظات ونصوص الصور إلى لغة أو أكثر.

```bash
translate -l "ko ja fr"
```

### أمثلة شائعة

ترجم Markdown فقط:

```bash
translate -l "de" -md
```

ترجم الدفاتر فقط:

```bash
translate -l "zh-CN" -nb
```

ترجم Markdown والصور:

```bash
translate -l "pt-BR" -md -img
```

حدّث الترجمات الموجودة عن طريق حذفها وإعادة إنشائها:

```bash
translate -l "ko" -u
```

شغّل دون موجهات تفاعلية:

```bash
translate -l "ko ja" -md -y
```

حفظ السجلات:

```bash
translate -l "ko" -s
```

اكتب أحداث تقدم مُنظمة:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | رموز اللغات مفصولة بمسافة، مثل `"es fr de"`, أو `"all"`. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `-u`, `--update` | No | حذف الترجمات الموجودة للغات المحددة وإعادة إنشائها. |
| `-img`, `--images` | No | ترجم ملفات الصور فقط. |
| `-md`, `--markdown` | No | ترجم ملفات Markdown فقط. |
| `-nb`, `--notebook` | No | ترجم ملفات دفاتر Jupyter فقط. |
| `-d`, `--debug` | No | تمكين تسجيلات التصحيح في وحدة التحكم. |
| `-s`, `--save-logs` | No | حفظ سجلات مستوى DEBUG تحت `<root-dir>/logs/`. |
| `--json-events` | No | كتابة أحداث تقدم الترجمة بصيغة قابلة للقراءة آليًا كـ NDJSON. |
| `-x`, `--fix` | No | إعادة ترجمة ملفات Markdown ذات الثقة المنخفضة بناءً على نتائج التقييم السابقة. |
| `-c`, `--min-confidence` | No | عتبة الثقة لـ `--fix`. الافتراضي `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | إضافة أو كتم إخطارات إخلاء المسؤولية الخاصة بالترجمة الآلية. الافتراضي مُمكّن في CLI. |
| `-f`, `--fast` | No | وضع الصور السريع (مهجور). |
| `-y`, `--yes` | No | تأكيد الموجهات تلقائيًا، مفيد في CI. |
| `--repo-url` | No | عنوان URL للمستودع المستخدم في نصيحة sparse-checkout لجدول لغات README. |
| `--migrate-language-folders` | No | إعادة تسمية مجلدات الأسماء المستعارة القديمة، مثل `cn` أو `tw`, إلى مجلدات BCP 47 القياسية. |
| `--dry-run` | No | معاينة ترحيل مجلدات اللغات وتقديرات الترجمة دون كتابة ملفات. |

إذا لم يتم توفير علم نوع، يقوم `translate` بمعالجة ملفات Markdown ودفاتر الملاحظات والصور. تتطلب ترجمة الصور تكوين Azure AI Vision.

## evaluate

قيّم جودة ترجمات Markdown للغة واحدة.

!!! warning "Experimental"
    `evaluate` تجريبي. يمكنه استخدام فحوصات جودة قائمة على قواعد وفحوصات مبنية على LLM، ويكتب نتائج التقييم في بيانات تعريف الترجمة، وقد يتغير نموذج التقييم وسلوك البيانات الوصفية.

```bash
evaluate -l "ko"
```

### أمثلة شائعة

استخدم عتبة ثقة منخفضة أكثر صرامة:

```bash
evaluate -l "es" -c 0.8
```

شغّل الفحوصات القائمة على القواعد فقط:

```bash
evaluate -l "fr" -f
```

شغّل الفحوصات المبنية على LLM فقط:

```bash
evaluate -l "ja" -D
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | رمز لغة واحد للتقييم. يتم تطبيع رموز الأسماء المستعارة. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `-c`, `--min-confidence` | No | العتبة المستخدمة عند سرد الترجمات منخفضة الثقة. الافتراضي `0.7`. |
| `-d`, `--debug` | No | تمكين تسجيلات التصحيح. |
| `-s`, `--save-logs` | No | حفظ سجلات مستوى DEBUG تحت `<root-dir>/logs/`. |
| `-f`, `--fast` | No | التقييم القائم على القواعد فقط. |
| `-D`, `--deep` | No | التقييم المبني على LLM فقط. |

بشكل افتراضي، يستخدم `evaluate` كلًا من التقييم القائم على القواعد والتقييم المبني على LLM. تُكتب النتائج في بيانات تعريف الترجمة وتُلخّص في وحدة التحكم.

## co-op-review

شغّل فحوصات صيانة ترجمة حتمية دون الحاجة إلى بيانات اعتماد API.

!!! note "Beta"
    `co-op-review` هو أمر مراجعة بيتا حتمي. لا يستدعي موفري النماذج ولا يكتب ملفات، لكن فحوصاته ومخطط مخرجات المشكلات قد يتطوران.

```bash
co-op-review -l "ko"
```

### أمثلة شائعة

راجع الترجمات الكورية واليابانية من الدليل الحالي:

```bash
co-op-review -l "ko ja"
```

راجع جذر مشروع محدد:

```bash
co-op-review -l "fr" -r ./my-course
```

راجع ملف README فقط بعد ترجمة مقتصرة على README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` يتجاهل المستندات الأخرى وملفات README المتداخلة. يفشل إذا كان الجذر
`README.md` مفقودًا. عند الجمع مع `--changed-from`، يقوم بمراجعة README فقط
عندما يتغير ملف المصدر هذا. تترك ترجمة مقتصرة على README ملف README المصدر
دون تغيير، بما في ذلك أي علامات لأقسام مشتركة.

راجع ملفات المصدر التي تغيرت فقط مقابل مرجع أساسي:

```bash
co-op-review -l "ko" --changed-from origin/main
```

اطبع إخراج Markdown بنكهة GitHub لملخصات CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-code` | No | رمز لغة للمراجعة. يمكن تمريره عدة مرات أو كقيمة مفصولة بمسافات. الافتراضي هو كل لغات الترجمة المكتشفة. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `--changed-from` | No | مرجع Git المستخدم لتقييد المراجعة بالملفات المصدرية المتغيرة. |
| `--readme-only` | No | مراجعة ترجمة `README.md` الجذر فقط. |
| `--format` | No | تنسيق الإخراج: `text` أو `github`. الافتراضي `text`. |

`co-op-review` حاليًا يتحقق من الملفات المترجمة المفقودة، والبيانات الوصفية للترجمة المفقودة أو القديمة، وصحة frontmatter في Markdown وسلامة سياج الأكواد، وJSON غير الصالح للدفاتر المترجمة، والأهداف المحلية المفقودة لروابط Markdown أو الصور. الروابط المفقودة تُعتبر تحذيرات افتراضيًا؛ المشاكل البنيوية ومشاكل الحداثة تؤدي إلى فشل الأمر.

## co-op-translator-mcp

شغّل خادم MCP الخاص بـ Co-op Translator للوكلاء والمحررين والعملاء المتوافقين مع MCP.

```bash
co-op-translator-mcp
```

الناقل الافتراضي هو `stdio`. انظر دليل [خادم MCP](mcp.md) لتكوين العميل والأدوات والموارد وملاحظات الأمان.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

أعد معالجة ملفات Markdown المترجمة وقم بتحديث روابط الدفاتر بحيث تشير إلى الدفاتر المترجمة عند توفرها.

```bash
migrate-links -l "ko ja"
```

### أمثلة شائعة

معاينة تحديثات الروابط:

```bash
migrate-links -l "ko" --dry-run
```

عالج كل اللغات المدعومة دون تأكيد:

```bash
migrate-links -l "all" -y
```

أعد كتابة الروابط فقط عندما توجد دفاتر مترجمة:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | رموز اللغات مفصولة بمسافة، أو `"all"`. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `--image-dir` | No | مجلد الصور المترجمة بالنسبة للجذر. الافتراضي `translated_images`. |
| `--dry-run` | No | أظهر الملفات التي ستتغير دون كتابة تحديثات. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | استخدم روابط الدفاتر الأصلية عندما تكون الدفاتر المترجمة مفقودة. مُفعّل افتراضيًا. |
| `-d`, `--debug` | No | تمكين تسجيلات التصحيح. |
| `-s`, `--save-logs` | No | حفظ سجلات مستوى DEBUG تحت `<root-dir>/logs/`. |
| `-y`, `--yes` | No | تأكيد الموجهات تلقائيًا عند معالجة كل اللغات. |

## البيئة

عندما يتطلب أمر بيانات اعتماد مزود، قم بتكوين أحد مجموعات المزودين هذه. لا يتطلب `translate --dry-run` و `co-op-review` بيانات اعتماد المزود:

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

تتطلب ترجمة الصور أيضًا Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## تخطيط المخرجات

تُكتب الترجمات النصية تحت:

```text
translations/<language-code>/<original-path>
```

يُكتب إخراج الصور المترجمة تحت:

```text
translated_images/<language-code>/<original-path>
```

على سبيل المثال، ترجمة `README.md` و `docs/setup.md` إلى الكورية تنتج:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## أمثلة CLI للنسخ واللصق

ترجم Markdown إلى ثلاث لغات:

```bash
translate -l "ko ja fr" -md
```

ترجم الدفاتر فقط:

```bash
translate -l "zh-CN" -nb
```

ترجم الصور فقط:

```bash
translate -l "pt-BR" -img
```

عاين ترجمة Markdown دون كتابة ملفات:

```bash
translate -l "de es" -md --dry-run
```

إصلاح ترجمات Markdown منخفضة الثقة:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

شغّل ترجمة Markdown صديقة لـ CI:

```bash
translate -l "ko ja" -md -y -s
```

راجع الإخراج المترجم:

```bash
co-op-review -l "ko ja"
```

عاين ترحيل الروابط:

```bash
migrate-links -l "ko" --dry-run
```