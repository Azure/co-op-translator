# Microsoft Beginners रिपॉज़िटरीज़

यह पृष्ठ उन Microsoft "For Beginners" रिपॉज़िटरीज़ के रखरखावकर्ताओं के लिए है जो साझा "Other Courses" README सेक्शन का उपयोग करते हैं।

Most Co-op Translator users do not need this page.

## Other Courses सेक्शन को ऑटो-सिंक करें

अपने README में "Other Courses" सेक्शन के चारों ओर ये मार्कर्स जोड़ें:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

हर बार जब Co-op Translator CLI या GitHub Actions के माध्यम से चलाया जाता है, यह मार्कर्स के बीच की सामग्री को पैकेज्ड टेम्पलेट से बदल देता है।

## साझा टेम्पलेट को अपडेट करें

टेम्पलेट स्रोत इस स्थान पर स्थित है:

```text
src/co_op_translator/templates/other_courses.md
```

साझा सामग्री को अपडेट करने के लिए:

1. टेम्पलेट को संपादित करें।
2. Co-op Translator के लिए एक पुल रिक्वेस्ट खोलें।
3. परिवर्तन जारी किए जाने के बाद, लक्षित रिपॉज़िटरी में Co-op Translator चलाएँ।

## Sparse Checkout सलाह

जब बड़े कोर्स रिपॉज़िटरी में कई अनुवादित आउटपुट शामिल होते हैं, तो क्लोन करना महँगा पड़ सकता है। आप इस सलाह को उत्पन्न भाषा अनुभागों में शामिल कर सकते हैं:

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