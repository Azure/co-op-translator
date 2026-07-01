# مستودعات Microsoft للمبتدئين

هذه الصفحة مخصصة للمسؤولين عن صيانة مستودعات Microsoft "For Beginners" التي تستخدم قسم README المشترك "Other Courses".

معظم مستخدمي Co-op Translator لا يحتاجون إلى هذه الصفحة.

## المزامنة التلقائية لقسم "Other Courses"

أضف هذه العلامات حول قسم "Other Courses" في README الخاص بك:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

في كل مرة يقوم فيها Co-op Translator بالتشغيل عبر CLI أو GitHub Actions، يستبدل المحتوى بين العلامات بالقالب المعبأ.

## تحديث القالب المشترك

مصدر القالب موجود في:

```text
src/co_op_translator/templates/other_courses.md
```

لتحديث المحتوى المشترك:

1. حرّر القالب.
2. افتح طلب سحب إلى Co-op Translator.
3. بعد صدور التغيير، شغّل Co-op Translator في المستودع الهدف.

## تنبيه حول السحب الجزئي (Sparse Checkout)

يمكن أن تصبح مستودعات الدورات الكبيرة مكلفة للاستنساخ عندما تتضمن العديد من المخرجات المترجمة. يمكنك إدراج هذا التنبيه في أقسام اللغة المولدة:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```