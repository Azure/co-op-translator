<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba33aa8d5da0d3dd14322b77fcb63deb",
  "translation_date": "2025-05-06T17:48:49+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "ar"
}
-->
# اللغات المدعومة

تدرج الجدول أدناه اللغات المدعومة حالياً بواسطة **Co-op Translator**. يتضمن رموز اللغات، أسماء اللغات، وأي مشكلات معروفة مرتبطة بكل لغة. إذا كنت ترغب في إضافة دعم للغة جديدة، يرجى إضافة رمز اللغة المقابل، الاسم، والخط المناسب في ملف `font_language_mappings.yml` الموجود في `src/co_op_translator/fonts/` ثم تقديم طلب سحب بعد الاختبار.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| mo            | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc    | No          | No           |
| hk            | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc| No          | No           |
| tw            | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc   | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt            | Portuguese (Portugal)| NotoSans-Medium.ttf               | No          | No           |
| br            | Portuguese (Brazil)  | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |

## إضافة لغة جديدة

لإضافة دعم للغة جديدة:

1. انتقل إلى [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. أضف رمز اللغة، الاسم، واسم ملف الخط المناسب. تأكد من تضمين السمة `rtl` إذا كانت اللغة تكتب من اليمين إلى اليسار.
3. إذا كنت بحاجة لاستخدام خط جديد، تأكد من أن الخط مجاني للاستخدام في المشاريع مفتوحة المصدر من خلال التحقق من ترخيصه وشروط حقوق النشر. بعد التأكد، أضف ملف الخط إلى مجلد `src/co_op_translator/fonts/`.
4. اختبر التغييرات محلياً للتأكد من دعم اللغة الجديدة بشكل صحيح.
5. قدم طلب سحب مع تغييراتك واذكر إضافة اللغة الجديدة في وصف الطلب.

مثال:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد والموثوق. بالنسبة للمعلومات الهامة، يُنصح بالترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.