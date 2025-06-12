<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:03:27+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "ur"
}
-->
# سپورٹ شدہ زبانیں

نیچے دی گئی جدول میں وہ زبانیں درج ہیں جو اس وقت **Co-op Translator** کی طرف سے سپورٹ کی جا رہی ہیں۔ اس میں زبان کے کوڈز، زبان کے نام، اور ہر زبان سے متعلقہ معروف مسائل شامل ہیں۔ اگر آپ کسی نئی زبان کے لیے سپورٹ شامل کرنا چاہتے ہیں تو براہ کرم متعلقہ زبان کا کوڈ، نام، اور مناسب فونٹ `font_language_mappings.yml` فائل میں شامل کریں جو `src/co_op_translator/fonts/` پر واقع ہے، اور ٹیسٹنگ کے بعد ایک پل ریکوئسٹ جمع کروائیں۔

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | No          | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | No          | No           |
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
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | No          | No           |
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
| uk            | Ukrainian            | NotoSans-Medium.ttf               | No          | No           |
| my            | Burmese (Myanmar)    | NotoSans-Medium.ttf               | No          | No           |

## نئی زبان شامل کرنا

کسی نئی زبان کے لیے سپورٹ شامل کرنے کے لیے:

1. [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml) پر جائیں۔
2. زبان کا کوڈ، نام، اور مناسب فونٹ فائل کا نام شامل کریں۔ اگر زبان دائیں سے بائیں ہے تو `rtl` خصوصیت شامل کرنا نہ بھولیں۔
3. اگر آپ کو نیا فونٹ استعمال کرنا ہے تو اس بات کو یقینی بنائیں کہ وہ فونٹ اوپن سورس پروجیکٹس میں مفت استعمال کے لیے دستیاب ہو، اس کی لائسنسنگ اور حقوق کا جائزہ لے کر۔ تصدیق کے بعد فونٹ فائل کو `src/co_op_translator/fonts/` ڈائریکٹری میں شامل کریں۔
4. اپنی تبدیلیاں مقامی طور پر ٹیسٹ کریں تاکہ یہ یقینی بنایا جا سکے کہ نئی زبان صحیح طریقے سے سپورٹ ہو رہی ہے۔
5. اپنی تبدیلیوں کے ساتھ ایک پل ریکوئسٹ جمع کروائیں اور PR کی تفصیل میں نئی زبان کے اضافے کی نشاندہی کریں۔

مثال:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**دستخطی دستبرد**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔