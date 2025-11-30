<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:37:12+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ur"
}
-->
# "دیگر کورسز" سیکشن کو اپ ڈیٹ کریں (Microsoft Beginners ریپوز)

یہ گائیڈ بتاتی ہے کہ "دیگر کورسز" سیکشن کو Co-op Translator کے ذریعے خودکار ہم آہنگی کیسے بنائی جائے، اور تمام ریپوز کے لیے عالمی ٹیمپلیٹ کو کیسے اپ ڈیٹ کیا جائے۔

- لاگو ہوتا ہے: صرف Microsoft Beginners ریپوز پر
- کام کرتا ہے: Co-op Translator CLI اور GitHub Actions کے ساتھ
- ٹیمپلیٹ کا ماخذ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## فوری آغاز: اپنے ریپو میں خودکار ہم آہنگی فعال کریں

اپنے README میں "دیگر کورسز" سیکشن کے گرد درج ذیل مارکرز شامل کریں۔ Co-op Translator ہر بار چلنے پر ان مارکرز کے درمیان موجود تمام مواد کو تبدیل کر دے گا۔

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

جب بھی Co-op Translator چلتا ہے—CLI کے ذریعے (مثلاً `translate -l "<language codes>"`) یا GitHub Actions کے ذریعے—یہ خود بخود ان مارکرز کے اندر موجود "دیگر کورسز" سیکشن کو اپ ڈیٹ کر دیتا ہے۔

> [!NOTE]
> اگر آپ کے پاس پہلے سے کوئی فہرست موجود ہے، تو بس اسے انہی مارکرز کے ساتھ لپیٹ دیں۔ اگلی بار چلنے پر اسے تازہ ترین معیاری مواد سے بدل دیا جائے گا۔

---

## عالمی مواد کو کیسے تبدیل کریں

اگر آپ وہ معیاری مواد اپ ڈیٹ کرنا چاہتے ہیں جو تمام Beginners ریپوز میں ظاہر ہوتا ہے:

1. ٹیمپلیٹ کو ایڈٹ کریں: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. اپنی تبدیلیوں کے ساتھ Co-op Translator ریپو میں پل ریکویسٹ کھولیں
3. جب PR مرج ہو جائے، تو Co-op Translator کا ورژن اپ ڈیٹ ہو جائے گا
4. اگلی بار جب Co-op Translator چلایا جائے (CLI یا GitHub Action کے ذریعے) کسی ہدف ریپو میں، تو یہ خود بخود اپ ڈیٹ شدہ سیکشن کو ہم آہنگ کر دے گا

یہ تمام Beginners ریپوز میں "دیگر کورسز" کے مواد کے لیے ایک واحد ماخذِ حقائق کو یقینی بناتا ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->