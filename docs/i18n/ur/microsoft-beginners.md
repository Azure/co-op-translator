# مائیکروسافٹ ابتدائی ریپوزیٹریز

یہ صفحہ اُن لوگوں کے لیے ہے جو مائیکروسافٹ "For Beginners" ریپوزیٹریز کو برقرار رکھتے ہیں جو مشترکہ "Other Courses" README سیکشن استعمال کرتی ہیں۔

زیادہ تر Co-op Translator صارفین کو اس صفحے کی ضرورت نہیں ہے۔

## دیگر کورسز سیکشن کی خودکار ہم آہنگی

اپنے README میں "Other Courses" سیکشن کے اطراف یہ مارکرز شامل کریں:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

جب بھی Co-op Translator CLI یا GitHub Actions کے ذریعے چلتا ہے، یہ مارکرز کے درمیان موجود مواد کو پیک شدہ ٹیمپلیٹ سے بدل دیتا ہے۔

## مشترکہ ٹیمپلیٹ کو اپ ڈیٹ کریں

ٹیمپلیٹ کا ماخذ یہ ہے:

```text
src/co_op_translator/templates/other_courses.md
```

مشترکہ مواد کو اپڈیٹ کرنے کے لیے:

1. ٹیمپلیٹ میں ترمیم کریں۔
2. Co-op Translator کے لیے پل ریکویسٹ کھولیں۔
3. تبدیلی جاری ہونے کے بعد، ہدف ریپوزیٹری میں Co-op Translator چلائیں۔

## Sparse Checkout مشورہ

جب بڑے کورس ریپوزیٹریز میں بہت سے ترجمہ شدہ آؤٹ پٹس شامل ہوں تو کلون کرنا مہنگا پڑ سکتا ہے۔ آپ اس ہدایت کو پیدا کردہ زبان کے سیکشنز میں شامل کر سکتے ہیں:

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