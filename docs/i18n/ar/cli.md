# مرجع CLI

Co-op Translator يقوم بتثبيت نقاط الدخول التالية لسطر الأوامر:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

تقوم الأوامر `translate` و `evaluate` و `migrate-links` و `co-op-review` بالتوجيه عبر `co_op_translator.__main__`، الذي يختار تنفيذ الأمر بناءً على اسم السكربت المستدعى. يستخدم خادم MCP `co_op_translator.mcp.server` مباشرة.

إذا كنت تحتار بين CLI أو Python API أو MCP، ابدأ بـ [اختر سير عملك](workflows.md).

## سير عمل CLI لأول مرة

ابدأ من هنا إذا كنت تستخدم Co-op Translator من الطرفية:

1. قم بتكوين مزود LLM كما هو موصوف في [Configuration](configuration.md).
2. اختر نوع المحتوى الذي تريد ترجمته.
3. شغّل أمرًا مركزًا أولاً، مثل الترجمة الخاصة بـ Markdown فقط.
4. استخدم `--dry-run` قبل تغييرات واسعة على المستودع.
5. استخدم `co-op-review` بعد الترجمة للتحقق من البنية والحداثة.

| الهدف | الأمر للبدء به |
| --- | --- |
| ترجمة مستندات Markdown | `translate -l "ko" -md` |
| ترجمة دفاتر الملاحظات | `translate -l "ko" -nb` |
| ترجمة نص الصور | `translate -l "ko" -img` |
| معاينة العمل دون كتابة ملفات | `translate -l "ko" -md --dry-run` |
| مراجعة الترجمات الحالية | `co-op-review -l "ko"` |
| تحديث روابط الدفاتر والمستندات | `migrate-links -l "ko" --dry-run` |
| إتاحة الأدوات لعميل MCP | قم بتكوين [MCP Server](mcp.md) بدلاً من تشغيل أوامر CLI مباشرة. |

## translate

Translate قم بترجمة ملفات Markdown ودفاتر الملاحظات ونص الصور إلى لغة أو أكثر من لغات الهدف.

```bash
translate -l "ko ja fr"
```

### أمثلة شائعة

ترجم Markdown فقط:

```bash
translate -l "de" -md
```

ترجم دفاتر الملاحظات فقط:

```bash
translate -l "zh-CN" -nb
```

ترجم Markdown والصور:

```bash
translate -l "pt-BR" -md -img
```

حدّث الترجمات الحالية بحذفها وإعادة إنشائها:

```bash
translate -l "ko" -u
```

شغّل بدون مطالبات تفاعلية:

```bash
translate -l "ko ja" -md -y
```

حفظ السجلات:

```bash
translate -l "ko" -s
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | رموز لغات مفصولة بمسافة، مثل `"es fr de"`, أو `"all"`. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `-u`, `--update` | No | حذف الترجمات الموجودة للغات المحددة وإعادة إنشائها. |
| `-img`, `--images` | No | ترجمة ملفات الصور فقط. |
| `-md`, `--markdown` | No | ترجمة ملفات Markdown فقط. |
| `-nb`, `--notebook` | No | ترجمة ملفات دفاتر Jupyter فقط. |
| `-d`, `--debug` | No | تمكين تسجيل التصحيح في وحدة التحكم. |
| `-s`, `--save-logs` | No | حفظ سجلات بمستوى DEBUG تحت `<root-dir>/logs/`. |
| `-x`, `--fix` | No | إعادة ترجمة ملفات Markdown منخفضة الثقة استنادًا إلى نتائج التقييم السابقة. |
| `-c`, `--min-confidence` | No | عتبة الثقة لـ `--fix`. الافتراضي هو `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | إضافة أو كبت إخلاء مسؤولية الترجمة الآلية. مفعل افتراضيًا في CLI. |
| `-f`, `--fast` | No | وضع الصور السريع مهمل. |
| `-y`, `--yes` | No | تأكيد المطالبات تلقائيًا، مفيد في CI. |
| `--repo-url` | No | عنوان URL للمستودع يستخدم في نصيحة sparse-checkout لجدول لغات README. |
| `--migrate-language-folders` | No | إعادة تسمية مجلدات الأسماء المستعارة القديمة، مثل `cn` أو `tw`، إلى مجلدات BCP 47 الرسمية. |
| `--dry-run` | No | معاينة ترحيل مجلدات اللغة وتقديرات الترجمة دون كتابة ملفات. |

إذا لم يتم توفير أي علم نوع، يقوم `translate` بمعالجة Markdown ودفاتر الملاحظات والصور. تتطلب ترجمة الصور تكوين Azure AI Vision.

## evaluate

evaluate قيّم جودة ترجمة Markdown للغة واحدة.

!!! warning "تجريبي"
    `evaluate` هو أمر تجريبي. يمكنه استخدام فحوصات جودة قائمة على القواعد ومرتكزة على LLM، ويكتب نتائج التقييم في بيانات الترجمة الوصفية، وقد يتغير نموذج التسجيل وسلوك البيانات الوصفية.

```bash
evaluate -l "ko"
```

### أمثلة شائعة

استخدم عتبة أكثر صرامة للترجمات منخفضة الثقة:

```bash
evaluate -l "es" -c 0.8
```

شغّل فحوصات قائمة على القواعد فقط:

```bash
evaluate -l "fr" -f
```

شغّل فحوصات قائمة على LLM فقط:

```bash
evaluate -l "ja" -D
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | رمز لغة واحد للتقييم. يتم تطبيع رموز الاختصار. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `-c`, `--min-confidence` | No | العتبة المستخدمة عند سرد الترجمات منخفضة الثقة. الافتراضي هو `0.7`. |
| `-d`, `--debug` | No | تمكين تسجيل التصحيح. |
| `-s`, `--save-logs` | No | حفظ سجلات بمستوى DEBUG تحت `<root-dir>/logs/`. |
| `-f`, `--fast` | No | تقييم قائم على القواعد فقط. |
| `-D`, `--deep` | No | تقييم قائم على LLM فقط. |

افتراضيًا، يستخدم `evaluate` كلًا من التقييم القائم على القواعد والتقييم القائم على LLM. تُكتب النتائج في بيانات الترجمة الوصفية وتُلخّص في وحدة التحكم.

## co-op-review

شغّل فحوصات صيانة ترجمة حتمية دون بيانات اعتماد API.

!!! note "بيتا"
    `co-op-review` هو أمر مراجعة حتمي في مرحلة بيتا. لا يستدعي مزودي النماذج ولا يكتب ملفات، لكن فحوصاته ومخطط إخراج المشكلات قد يتطوران.

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

راجع فقط ملفات المصدر التي تغيرت بالنسبة لمرجع أساسي:

```bash
co-op-review -l "ko" --changed-from origin/main
```

اطبع مخرجات Markdown بنكهة GitHub لملخصات CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `-l`, `--language-code` | No | رمز اللغة للمراجعة. يمكن تمريره عدة مرات أو كقيمة مفصولة بمسافات. الافتراضي هو جميع لغات الترجمة المكتشفة. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `--changed-from` | No | مرجع Git يستخدم لتقييد المراجعة على ملفات المصدر المتغيرة. |
| `--format` | No | تنسيق الإخراج: `text` أو `github`. الافتراضي هو `text`. |

يقوم `co-op-review` حاليًا بالتحقق من الملفات المترجمة المفقودة، وبيانات الترجمة الوصفية المفقودة أو القديمة، وسلامة frontmatter واحتواء أقواس الشيفرة في Markdown، وصحة JSON لدفاتر الملاحظات المترجمة، وأهداف روابط Markdown أو صور محلية مفقودة. الروابط المفقودة هي تحذيرات افتراضيًا؛ المشاكل البنيوية ومشاكل الحداثة تفشل الأمر.

## co-op-translator-mcp

شغّل خادم MCP الخاص بـ Co-op Translator للوكلاء والمحررين والعملاء المتوافقين مع MCP.

```bash
co-op-translator-mcp
```

الناقل الافتراضي هو `stdio`. راجع دليل [MCP Server](mcp.md) لتكوين العميل، والأدوات، والموارد، وملاحظات الأمان.

### الخيارات

| الخيار | مطلوب | الوصف |
| --- | --- | --- |
| `--transport` | No | ناقل MCP: `stdio`, `streamable-http`, أو `sse`. الافتراضي هو `stdio`. |

## migrate-links

أعد معالجة ملفات Markdown المترجمة وحدّث روابط دفاتر الملاحظات بحيث تشير إلى الدفاتر المترجمة عندما تكون متاحة.

```bash
migrate-links -l "ko ja"
```

### أمثلة شائعة

معاينة تحديثات الروابط:

```bash
migrate-links -l "ko" --dry-run
```

عالج جميع اللغات المدعومة دون تأكيد:

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
| `-l`, `--language-codes` | Yes | رموز لغات مفصولة بمسافة، أو `"all"`. |
| `-r`, `--root-dir` | No | جذر المشروع. الافتراضي هو الدليل الحالي. |
| `--image-dir` | No | مجلد الصور المترجمة بالنسبة للجذر. الافتراضي هو `translated_images`. |
| `--dry-run` | No | عرض الملفات التي سيتغير محتواها دون كتابة تحديثات. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | استخدام روابط الدفاتر الأصلية عندما تكون الدفاتر المترجمة مفقودة. مُمكن افتراضيًا. |
| `-d`, `--debug` | No | تمكين تسجيل التصحيح. |
| `-s`, `--save-logs` | No | حفظ سجلات بمستوى DEBUG تحت `<root-dir>/logs/`. |
| `-y`, `--yes` | No | تأكيد المطالبات تلقائيًا عند معالجة جميع اللغات. |

## البيئة

تتطلب جميع الأوامر مزود LLM واحد مُكوّن:

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
```

تتطلب ترجمة الصور إضافةً إلى ذلك Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## تخطيط المخرجات

تُكتب الترجمات النصية تحت:

```text
translations/<language-code>/<original-path>
```

يُكتب مخرج الصور المترجمة تحت:

```text
translated_images/<language-code>/<original-path>
```

على سبيل المثال، ترجمة `README.md` و `docs/setup.md` إلى الكورية ينتج:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## أمثلة CLI للنسخ واللصق

ترجم Markdown إلى ثلاث لغات:

```bash
translate -l "ko ja fr" -md
```

ترجم دفاتر الملاحظات فقط:

```bash
translate -l "zh-CN" -nb
```

ترجم الصور فقط:

```bash
translate -l "pt-BR" -img
```

معاينة ترجمة Markdown دون كتابة ملفات:

```bash
translate -l "de es" -md --dry-run
```

إصلاح ترجمات Markdown منخفضة الثقة:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

تشغيل ترجمة Markdown صديقة لـ CI:

```bash
translate -l "ko ja" -md -y -s
```

مراجعة المخرجات المترجمة:

```bash
co-op-review -l "ko ja"
```

معاينة ترحيل الروابط:

```bash
migrate-links -l "ko" --dry-run
```