<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:13:40+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ar"
}
-->
# كيفية استخدام واجهة سطر الأوامر (CLI) الخاصة بـ Co-op Translator

## المتطلبات الأساسية

- **Python 3.10 أو أحدث**: مطلوب لتشغيل Co-op Translator.
- **مصدر نموذج اللغة**:  
  - **Azure OpenAI** أو نماذج LLM أخرى. يمكن العثور على التفاصيل في [النماذج والخدمات المدعومة](../../../../README.md).
- **مصدر رؤية الحاسوب** (اختياري):  
  - لترجمة الصور. إذا لم يكن متوفرًا، يعمل المترجم في [وضع Markdown فقط](../markdown-only-mode.md).  
  - **Azure Computer Vision**

## جدول المحتويات

1. [إنشاء ملف '.env' في الدليل الجذري](./create-env-file.md)  
   - تضمين المفاتيح اللازمة لخدمة نموذج اللغة المختارة.  
   - إذا تم حذف مفاتيح Azure Computer Vision أو تم تحديد `-md`، سيعمل المترجم في وضع Markdown فقط.  
1. [تثبيت حزمة Co-op Translator](./install-package.md)  
1. [ترجمة مشروعك باستخدام Co-op Translator](./translator-your-project.md)

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالاعتماد على الترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.