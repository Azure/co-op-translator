<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:53:00+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ar"
}
-->
# كيفية استخدام واجهة سطر الأوامر الخاصة بـ Co-op Translator (CLI)

## المتطلبات الأساسية

- **Python 3.10 أو أعلى**: مطلوب لتشغيل Co-op Translator.
- **مصدر نموذج اللغة**:  
  - **Azure OpenAI** أو نماذج لغوية كبيرة أخرى. يمكن العثور على التفاصيل في [النماذج والخدمات المدعومة](../../../../README.md).
- **مصدر رؤية الحاسوب** (اختياري):  
  - لترجمة الصور. إذا لم يكن متوفرًا، يعمل المترجم في [وضع Markdown فقط](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### الإعداد الأولي

قبل البدء، تأكد من إعداد الموارد التالية:

- [إعداد Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [إعداد Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (اختياري)

## جدول المحتويات

1. [إنشاء ملف '.env' في الدليل الجذري](./create-env-file.md)  
   - تضمين المفاتيح اللازمة لخدمة نموذج اللغة المختارة.  
   - إذا تم حذف مفاتيح Azure Computer Vision أو تم تحديد `-md`، سيعمل المترجم في وضع Markdown فقط.  
3. [تثبيت حزمة Co-op translator](./install-package.md)  
4. [ترجمة مشروعك باستخدام Co-op Translator](./translator-your-project.md)

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. بالنسبة للمعلومات الهامة، يُنصح بالاعتماد على الترجمة الاحترافية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.