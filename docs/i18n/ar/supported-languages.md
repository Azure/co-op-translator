# اللغات المدعومة

يدعم Co-op Translator رموز اللغات التالية لترجمات النصوص والدفاتر والصور.

إذا رغبت في إضافة لغة جديدة، قم بتحديث مطابَقات اللغة والخط تحت `src/co_op_translator/fonts/` واختبر اللغة قبل فتح طلب سحب.

| رمز اللغة | اسم اللغة | الخط | دعم RTL | مشاكل معروفة |
| --- | --- | --- | --- | --- |
| en | الإنجليزية | NotoSans-Medium.ttf | لا | لا |
| fr | الفرنسية | NotoSans-Medium.ttf | لا | لا |
| es | الإسبانية | NotoSans-Medium.ttf | لا | لا |
| de | الألمانية | NotoSans-Medium.ttf | لا | لا |
| ru | الروسية | NotoSans-Medium.ttf | لا | لا |
| ar | العربية | NotoSansArabic-Medium.ttf | نعم | لا |
| fa | الفارسية (فارسي) | NotoSansArabic-Medium.ttf | نعم | لا |
| ur | الأردية | NotoSansArabic-Medium.ttf | نعم | لا |
| zh-CN | الصينية (المبسطة) | NotoSansCJK-Medium.ttc | لا | لا |
| zh-MO | الصينية (التقليدية، ماكاو) | NotoSansCJK-Medium.ttc | لا | لا |
| zh-HK | الصينية (التقليدية، هونغ كونغ) | NotoSansCJK-Medium.ttc | لا | لا |
| zh-TW | الصينية (التقليدية، تايوان) | NotoSansCJK-Medium.ttc | لا | لا |
| ja | اليابانية | NotoSansCJK-Medium.ttc | لا | لا |
| ko | الكورية | NotoSansCJK-Medium.ttc | لا | لا |
| hi | الهندية | NotoSansDevanagari-Medium.ttf | لا | لا |
| bn | البنغالية | NotoSansBengali-Medium.ttf | لا | لا |
| mr | الماراثية | NotoSansDevanagari-Medium.ttf | لا | لا |
| ne | النيبالية | NotoSansDevanagari-Medium.ttf | لا | لا |
| pa | البنجابية (غورموخي) | NotoSansGurmukhi-Medium.ttf | لا | لا |
| pt-PT | البرتغالية (البرتغال) | NotoSans-Medium.ttf | لا | لا |
| pt-BR | البرتغالية (البرازيل) | NotoSans-Medium.ttf | لا | لا |
| it | الإيطالية | NotoSans-Medium.ttf | لا | لا |
| lt | اللتوانية | NotoSans-Medium.ttf | لا | لا |
| pl | البولندية | NotoSans-Medium.ttf | لا | لا |
| tr | التركية | NotoSans-Medium.ttf | لا | لا |
| el | اليونانية | NotoSans-Medium.ttf | لا | لا |
| th | التايلاندية | NotoSansThai-Medium.ttf | لا | لا |
| sv | السويدية | NotoSans-Medium.ttf | لا | لا |
| da | الدانمركية | NotoSans-Medium.ttf | لا | لا |
| no | النرويجية | NotoSans-Medium.ttf | لا | لا |
| fi | الفنلندية | NotoSans-Medium.ttf | لا | لا |
| nl | الهولندية | NotoSans-Medium.ttf | لا | لا |
| he | العبرية | NotoSansHebrew-Medium.ttf | نعم | لا |
| vi | الفيتنامية | NotoSans-Medium.ttf | لا | لا |
| id | الإندونيسية | NotoSans-Medium.ttf | لا | لا |
| ms | الملايوية | NotoSans-Medium.ttf | لا | لا |
| tl | التاغالوغية (الفلبينية) | NotoSans-Medium.ttf | لا | لا |
| sw | السواحلية | NotoSans-Medium.ttf | لا | لا |
| hu | الهنغارية | NotoSans-Medium.ttf | لا | لا |
| cs | التشيكية | NotoSans-Medium.ttf | لا | لا |
| sk | السلوفاكية | NotoSans-Medium.ttf | لا | لا |
| ro | الرومانية | NotoSans-Medium.ttf | لا | لا |
| bg | البلغارية | NotoSans-Medium.ttf | لا | لا |
| sr | الصربية (السيريلية) | NotoSans-Medium.ttf | لا | لا |
| hr | الكرواتية | NotoSans-Medium.ttf | لا | لا |
| sl | السلوفينية | NotoSans-Medium.ttf | لا | لا |
| uk | الأوكرانية | NotoSans-Medium.ttf | لا | لا |
| my | البورمية (ميانمار) | NotoSansMyanmar-Medium.ttf | لا | لا |
| ta | التاميلية | NotoSansTamil-Medium.ttf | لا | لا |
| et | الإستونية | NotoSans-Medium.ttf | لا | لا |
| pcm | البيجن النيجيري | NotoSans-Medium.ttf | لا | لا |
| te | التيلجو | NotoSans-Medium.ttf | لا | لا |
| ml | المالايالامية | NotoSans-Medium.ttf | لا | لا |
| kn | الكانادية | NotoSans-Medium.ttf | لا | لا |
| km | الخميرية | NotoSansKhmer-Medium.ttf | لا | لا |

## إضافة لغة

To add support for a new language:

1. أضف رمز اللغة واسم العرض إلى أدوات اللغة.
2. أضف خطًا أو اربطه في `src/co_op_translator/fonts/font_language_mappings.yml`.
3. اختبر مخرجات ترجمة Markdown والصور.
4. افتح طلب سحب يتضمن الخرائط وملاحظات التحقق.