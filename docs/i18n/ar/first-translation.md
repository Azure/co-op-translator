# ترجم وحرر وراجع مشروعًا صغيرًا

ابدأ بملفين قصيرين بصيغة Markdown ولغة هدف واحدة. سترى أين تُكتب الترجمات، ماذا يحدث عندما يتغير المصدر، وكيفية التحقق من النتيجة.

## النتائج المسجلة

تم تشغيل المثال في 19 سبتمبر 2026 باستخدام Co-op Translator 0.21.0 وAzure OpenAI (`gpt-5-mini`). تم استدعاء أوامر CLI غير المعدّلة عبر `CliRunner` من Click باستخدام الحزمة المبنية والتبعيات الحالية لبايثون.

| Step | Result |
| --- | --- |
| Preview | Exit 0; لم يُطلب ترجمة من النموذج |
| Initial translation | Exit 0; 27.36 ثانية |
| Initial review | Exit 0 |
| Edit README and review | Exit 1; تم اكتشاف ترجمة قديمة |
| Update translation | Exit 0; 22.17 ثانية |
| Review after update | Exit 0; لا أخطاء أو تحذيرات |
| Unchanged guide | بايتات متطابقة قبل وبعد تحديث README |
| Run again | Exit 0; هاشات متطابقة لجميع ملفات الترجمة |

هذه قياسات تشغيل فردية، وليست ضمانات أداء. يُستبعد وقت الإعداد؛ ولم تُقاس فواتير المزود. قد يقوم التشغيل غير المتغير أيضًا بإجراء فحص صحة للمزود.

تحقق من [الترجمة المبدئية](../../assets/demo/before.txt)، [الترجمة المحدثة](../../assets/demo/after.txt)، [فارق الترجمة الكامل](../../assets/demo/update.diff)، [المراجعة القديمة](../../assets/demo/review-stale.txt)، [المراجعة النهائية](../../assets/demo/review-after.txt)، و[تفاصيل التشغيل](../../assets/demo/results.json). قد تغيّر الترجمة الكاملة للملف صياغات أخرى، كما يُظهر الفارق الملتقط. تحافظ كلتا القطعتين النصيتين على إخلاء المسؤولية المُولَّد.

لا تزال المراجعة البشرية مهمة: التحديث الملتقط يستخدم `[사용 가이드](guide.md)을`; الحرف الكوري الصحيح يجب أن يكون `[사용 가이드](guide.md)를`. تحتفظ القطع النصية بهذا الإخراج كما هو بدلاً من عرض ترجمة محررة كناتج النموذج. تمر المراجعة الهيكلية رغم مشكلة الصياغة هذه.

## 1. جهز مجلدًا صغيرًا

استخدم Python 3.11–3.14 و[إعداد البيئة الافتراضية](configuration.md#local-runtime-setup). ثبّت الإصدار المستخدم في هذا المثال:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

حمّل [README.txt](../../assets/demo/README.txt) و[guide.txt](../../assets/demo/guide.txt) إلى هذا المجلد، واحفظهما باسمَي `README.md` و`guide.md`. هما مستندان صغيران لمشروع خيالي؛ لا حاجة لتثبيت أي تطبيق.

يحتوي README على كتلة شفرة ورابط إلى `guide.md`. جملته النهائية هي:

```text
Notes are saved locally.
```

احتفظ بهذين المستندين المصدرَين فقط في هذا المجلد. تُنفّذ جميع الأوامر التالية داخل `translation-demo` وتعمل في Bash وPowerShell.

## 2. معاينة بدون بيانات اعتماد

```bash
translate -l "ko" -md --dry-run
```

تُقدّر المعاينة عمل الترجمة دون استدعاء نموذج أو كتابة الترجمات. تقديرات التوكنات ليست عرضًا للفوترة. يجب أن يحدد التشغيل الأول كلا ملفَي Markdown كعمل جديد.

## 3. اختر مزوّدًا وقم بالترجمة

قم بتكوين مزود واحد باستخدام [دليل التكوين](configuration.md): Azure OpenAI أو OpenAI أو Anthropic. لا تتطلّب ترجمات النص من OpenAI وAnthropic حساب Azure. خدمات الصور غير مطلوبة لهذا المثال.

إذا استخدمت ملف `.env` محليًا، أضف `.env` إلى `.gitignore` الخاص بهذا المجلد. تستخدم استدعاءات الترجمة حساب مزودك وقد تتسبب في رسوم.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

افتح `translations/ko/README.md` و`translations/ko/guide.md`. تحقق من الصياغة الكورية وكتلة الشفرة والرابط من README المترجم إلى الدليل المترجم. تختلف صياغة المخرجات حسب النموذج.

يتحقق `co-op-review` من الحداثة والبنية والروابط المحلية. لا تُعد نتيجة النجاح شهادة على الدقة اللغوية. قم بحل أي أخطاء مُبلغ عنها قبل المتابعة.

سجّل الخط الأساس الناجح باستخدام Git (قم بتكوين هويتك في Git أولًا إذا لزم الأمر):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. غيّر المصدر

في `README.md`، استبدل `Notes are saved locally.` بـ:

```text
Notes are saved locally as Markdown files.
```

اترك `guide.md` دون تغيير. ثم نفّذ:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

يجب أن تُبلغ المراجعة أن ترجمة README قديمة وأن تنهي التنفيذ بفشل. هذه هي الحالة الوسيطة المتوقعة. يجب أن تحدد المعاينة عملًا لملف README الذي تغيّر.

## 5. حدّث وافحص الفرق

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

افحص الفرق الحقيقي: تقوم واجهة CLI الافتراضية بإعادة ترجمة الملف المُغيّر، لذلك يمكن للنموذج أيضًا تعديل صياغات أخرى في ذلك الملف. يجب ألا يحتوي الدليل غير المتغير على فرق. يجب ألا تعيد المراجعة الإبلاغ بأن ترجمة README قديمة؛ تحقق من أي نتائج أخرى بدلًا من تجاهلها.

يتطلب الحفاظ على مستوى الكتل لتعديلات Markdown البشرية وجود موفر حالة ترجمة اختياري في [Python API](api.md). هذا غير مفعل بواسطة أوامر CLI هذه.

## 6. نفّذ مرة أخرى بدون تغييرات

قم بعمل commit للمصدر والترجمة المحدثين:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

مع الترجمات الحالية والتكوين غير المتغير، يتخطى المترجم الملفات. يجب ألا ينتج أمر Git النهائي فرقًا وأن ينتهي بنجاح.

## الخطوات التالية

- [ترجم README فقط وافتح طلب سحب](github-actions.md#your-first-readme-translation-pr).
- [اختر CLI أو Python API أو MCP](workflows.md).
- [أبلغ عن مشكلة في الترجمة بدون ترميز](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).