<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:39:52+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "hi"
}
-->
# "अन्य पाठ्यक्रम" अनुभाग अपडेट करें (Microsoft Beginners रिपॉजिटरी)

यह गाइड बताता है कि कैसे "अन्य पाठ्यक्रम" अनुभाग को Co-op Translator का उपयोग करके ऑटो-सिंक्रनाइज़ किया जाए, और सभी रिपॉजिटरी के लिए वैश्विक टेम्पलेट को कैसे अपडेट किया जाए।

- लागू होता है: केवल Microsoft Beginners रिपॉजिटरीज़ पर
- काम करता है: Co-op Translator CLI और GitHub Actions के साथ
- टेम्पलेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## त्वरित शुरुआत: अपने रिपॉजिटरी में ऑटो-सिंक सक्षम करें

अपने README में "अन्य पाठ्यक्रम" अनुभाग के चारों ओर निम्नलिखित मार्कर जोड़ें। Co-op Translator हर रन पर इन मार्करों के बीच की सारी सामग्री को बदल देगा।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

हर बार जब Co-op Translator चलता है—CLI के माध्यम से (जैसे, `translate -l "<language codes>"`) या GitHub Actions के जरिए—यह स्वचालित रूप से इन मार्करों से घिरे "अन्य पाठ्यक्रम" अनुभाग को अपडेट कर देता है।

> [!NOTE]
> यदि आपके पास पहले से कोई सूची है, तो बस उसे उन्हीं मार्करों के साथ घेर दें। अगली बार रन होने पर इसे नवीनतम मानकीकृत सामग्री से बदल दिया जाएगा।

---

## वैश्विक सामग्री कैसे बदलें

यदि आप सभी Beginners रिपॉजिटरीज़ में दिखने वाली मानकीकृत सामग्री को अपडेट करना चाहते हैं:

1. टेम्पलेट संपादित करें: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. अपने परिवर्तनों के साथ Co-op Translator रिपॉजिटरी में एक पुल रिक्वेस्ट खोलें
3. PR मर्ज होने के बाद, Co-op Translator का संस्करण अपडेट हो जाएगा
4. अगली बार जब Co-op Translator (CLI या GitHub Action) लक्षित रिपॉजिटरी में चलेगा, तो यह अपडेटेड अनुभाग को स्वचालित रूप से सिंक कर देगा

इससे सभी Beginners रिपॉजिटरीज़ में "अन्य पाठ्यक्रम" सामग्री के लिए एकल सत्य स्रोत सुनिश्चित होता है।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->