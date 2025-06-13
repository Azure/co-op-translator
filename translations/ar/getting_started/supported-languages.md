<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:02:32+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "ar"
}
-->
# اللغات المدعومة

تدرج الجدول أدناه اللغات المدعومة حالياً بواسطة **Co-op Translator**. يشمل ذلك رموز اللغات، أسماء اللغات، وأي مشاكل معروفة مرتبطة بكل لغة. إذا رغبت في إضافة دعم للغة جديدة، يرجى إضافة رمز اللغة، الاسم، والخط المناسب في ملف `font_language_mappings.yml` الموجود في `src/co_op_translator/fonts/` ثم تقديم طلب سحب بعد الاختبار.

| رمز اللغة | اسم اللغة           | الخط                              | دعم من اليمين إلى اليسار | المشاكل المعروفة |
|-----------|---------------------|----------------------------------|-------------------------|------------------|
| en        | English             | NotoSans-Medium.ttf              | لا                      | لا               |
| fr        | French              | NotoSans-Medium.ttf              | لا                      | لا               |
| es        | Spanish             | NotoSans-Medium.ttf              | لا                      | لا               |
| de        | German              | NotoSans-Medium.ttf              | لا                      | لا               |
| ru        | Russian             | NotoSans-Medium.ttf              | لا                      | لا               |
| ar        | Arabic              | NotoSansArabic-Medium.ttf        | نعم                     | لا               |
| fa        | Persian (Farsi)     | NotoSansArabic-Medium.ttf        | لا                      | لا               |
| ur        | Urdu                | NotoSansArabic-Medium.ttf        | لا                      | لا               |
| zh        | Chinese (Simplified)| NotoSansCJK-Medium.ttc           | لا                      | لا               |
| mo        | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc  | لا                      | لا               |
| hk        | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | لا                      | لا               |
| tw        | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc    | لا                      | لا               |
| ja        | Japanese            | NotoSansCJK-Medium.ttc           | لا                      | لا               |
| ko        | Korean              | NotoSansCJK-Medium.ttc           | لا                      | لا               |
| hi        | Hindi               | NotoSansDevanagari-Medium.ttf    | لا                      | لا               |
| bn        | Bengali             | NotoSansBengali-Medium.ttf       | لا                      | لا               |
| mr        | Marathi             | NotoSansDevanagari-Medium.ttf    | لا                      | لا               |
| ne        | Nepali              | NotoSansDevanagari-Medium.ttf    | لا                      | لا               |
| pa        | Punjabi (Gurmukhi)  | NotoSansGurmukhi-Medium.ttf      | لا                      | لا               |
| pt        | Portuguese (Portugal)| NotoSans-Medium.ttf              | لا                      | لا               |
| br        | Portuguese (Brazil) | NotoSans-Medium.ttf              | لا                      | لا               |
| it        | Italian             | NotoSans-Medium.ttf              | لا                      | لا               |
| pl        | Polish              | NotoSans-Medium.ttf              | لا                      | لا               |
| tr        | Turkish             | NotoSans-Medium.ttf              | لا                      | لا               |
| el        | Greek               | NotoSans-Medium.ttf              | لا                      | لا               |
| th        | Thai                | NotoSansThai-Medium.ttf          | لا                      | لا               |
| sv        | Swedish             | NotoSans-Medium.ttf              | لا                      | لا               |
| da        | Danish              | NotoSans-Medium.ttf              | لا                      | لا               |
| no        | Norwegian           | NotoSans-Medium.ttf              | لا                      | لا               |
| fi        | Finnish             | NotoSans-Medium.ttf              | لا                      | لا               |
| nl        | Dutch               | NotoSans-Medium.ttf              | لا                      | لا               |
| he        | Hebrew              | NotoSansHebrew-Medium.ttf        | لا                      | لا               |
| vi        | Vietnamese          | NotoSans-Medium.ttf              | لا                      | لا               |
| id        | Indonesian          | NotoSans-Medium.ttf              | لا                      | لا               |
| ms        | Malay               | NotoSans-Medium.ttf              | لا                      | لا               |
| tl        | Tagalog (Filipino)  | NotoSans-Medium.ttf              | لا                      | لا               |
| sw        | Swahili             | NotoSans-Medium.ttf              | لا                      | لا               |
| hu        | Hungarian           | NotoSans-Medium.ttf              | لا                      | لا               |
| cs        | Czech               | NotoSans-Medium.ttf              | لا                      | لا               |
| sk        | Slovak              | NotoSans-Medium.ttf              | لا                      | لا               |
| ro        | Romanian            | NotoSans-Medium.ttf              | لا                      | لا               |
| bg        | Bulgarian           | NotoSans-Medium.ttf              | لا                      | لا               |
| sr        | Serbian (Cyrillic)  | NotoSans-Medium.ttf              | لا                      | لا               |
| hr        | Croatian            | NotoSans-Medium.ttf              | لا                      | لا               |
| sl        | Slovenian           | NotoSans-Medium.ttf              | لا                      | لا               |
| uk        | Ukrainian           | NotoSans-Medium.ttf              | لا                      | لا               |
| my        | Burmese (Myanmar)   | NotoSans-Medium.ttf              | لا                      | لا               |

## إضافة لغة جديدة

لإضافة دعم للغة جديدة:

1. انتقل إلى [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. أضف رمز اللغة، الاسم، واسم ملف الخط المناسب. تأكد من تضمين الخاصية `rtl` إذا كانت اللغة تُكتب من اليمين إلى اليسار.
3. إذا كنت بحاجة لاستخدام خط جديد، تأكد من أن الخط مجاني للاستخدام في المشاريع مفتوحة المصدر من خلال مراجعة ترخيصه وشروط حقوق النشر. بعد التحقق، أضف ملف الخط إلى مجلد `src/co_op_translator/fonts/`.
4. اختبر تغييراتك محلياً للتأكد من دعم اللغة الجديدة بشكل صحيح.
5. قدم طلب سحب مع تغييراتك واذكر إضافة اللغة الجديدة في وصف طلب السحب.

مثال:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**تنبيه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الحساسة أو الهامة، يُنصح بالاعتماد على الترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.