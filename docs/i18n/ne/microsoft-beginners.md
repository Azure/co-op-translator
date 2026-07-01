# Microsoft शुरुआतीहरूको रिपोजिटरीहरू

यो पृष्ठ Microsoft "For Beginners" रिपोजिटरीहरूको रखरखावकर्ताहरूका लागि हो जुन साझा "Other Courses" README खण्ड प्रयोग गर्दछन्।

धेरै Co-op Translator प्रयोगकर्ताहरूलाई यो पृष्ठ आवश्यक पर्दैन।

## Other Courses खण्ड स्वचालित रूपमा समकालिक गर्नुहोस्

तपाईंको README मा "Other Courses" खण्ड वरिपरि यी मार्करहरू थप्नुहोस्:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

प्रति पटक Co-op Translator CLI वा GitHub Actions मार्फत चलाउँदा, यो मार्करहरूबिचको सामग्रीलाई प्याक गरिएको टेम्पलेटले प्रतिस्थापन गर्छ।

## साझा टेम्पलेट अपडेट गर्नुहोस्

टेम्पलेट स्रोत अवस्थित छ:

```text
src/co_op_translator/templates/other_courses.md
```

साझा सामग्री अपडेट गर्न:

1. टेम्पलेट सम्पादन गर्नुहोस्।
2. Co-op Translator मा pull request खोल्नुहोस्।
3. परिवर्तन रिलिज भएपछि, लक्ष्य रिपोजिटरीमा Co-op Translator चलाउनुहोस्।

## Sparse Checkout सल्लाह

ठूला कोर्स रिपोजिटरीहरूमा धेरै अनुवादित आउटपुटहरू समावेश हुँदा क्लोन गर्न महँगो हुन सक्छ। तपाईं यो सल्लाह उत्पन्न गरिएका भाषा खण्डहरूमा समावेश गर्न सक्नुहुन्छ:

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