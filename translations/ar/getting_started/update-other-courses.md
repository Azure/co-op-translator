<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:36:20+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ar"
}
-->
# تحديث قسم "الدورات الأخرى" (مستودعات Microsoft Beginners)

يشرح هذا الدليل كيفية جعل قسم "الدورات الأخرى" يتزامن تلقائيًا باستخدام Co-op Translator، وكيفية تحديث القالب العام لجميع المستودعات.

- ينطبق على: مستودعات Microsoft Beginners فقط
- يعمل مع: أداة سطر الأوامر Co-op Translator و GitHub Actions
- مصدر القالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## بداية سريعة: تفعيل التزامن التلقائي في مستودعك

أضف العلامات التالية حول قسم "الدورات الأخرى" في ملف README الخاص بك. سيقوم Co-op Translator باستبدال كل ما بين هذه العلامات في كل مرة يتم تشغيله.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

في كل مرة يتم تشغيل Co-op Translator — سواء عبر سطر الأوامر (مثل `translate -l "<language codes>"`) أو GitHub Actions — يقوم تلقائيًا بتحديث قسم "الدورات الأخرى" المحاط بهذه العلامات.

> [!NOTE]
> إذا كان لديك قائمة موجودة مسبقًا، فقط قم بتغليفها بنفس العلامات. في التشغيل التالي سيتم استبدالها بالمحتوى الموحد الأحدث.

---

## كيفية تغيير المحتوى العام

إذا أردت تحديث المحتوى الموحد الذي يظهر في جميع مستودعات Beginners:

1. حرر القالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. افتح طلب سحب (Pull Request) إلى مستودع Co-op Translator مع التعديلات التي أجريتها
3. بعد دمج طلب السحب، سيتم تحديث نسخة Co-op Translator
4. في المرة التالية التي يتم فيها تشغيل Co-op Translator (سطر الأوامر أو GitHub Action) في مستودع مستهدف، سيتم مزامنة القسم المحدث تلقائيًا

هذا يضمن وجود مصدر واحد موثوق لمحتوى "الدورات الأخرى" عبر جميع مستودعات Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->