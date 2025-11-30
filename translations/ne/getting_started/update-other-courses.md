<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:41:12+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ne"
}
-->
# "अन्य कोर्सहरू" सेक्सन अपडेट गर्नुहोस् (Microsoft Beginners रिपोजिटोरीहरू)

यो मार्गदर्शनले "अन्य कोर्सहरू" सेक्सनलाई Co‑op Translator प्रयोग गरी कसरी स्वचालित रूपमा समक्रमण गर्ने र सबै रिपोजिटोरीहरूको लागि ग्लोबल टेम्प्लेट कसरी अपडेट गर्ने भनेर बताउँछ।

- लागू हुने: Microsoft Beginners रिपोजिटोरीहरूमा मात्र
- काम गर्ने: Co‑op Translator CLI र GitHub Actions सँग
- टेम्प्लेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## छिटो सुरु: तपाईंको रिपोमा स्वचालित समक्रमण सक्षम पार्नुहोस्

तपाईंको README मा "अन्य कोर्सहरू" सेक्सन वरिपरि तलका मार्करहरू थप्नुहोस्। Co‑op Translator ले हरेक रनमा यी मार्करहरू बीचको सबै कुरा प्रतिस्थापन गर्नेछ।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator हरेक पटक चल्दा—CLI मार्फत (जस्तै, `translate -l "<language codes>"`) वा GitHub Actions मार्फत—स्वचालित रूपमा यी मार्करहरूले घेरिएको "अन्य कोर्सहरू" सेक्सन अपडेट गर्छ।

> [!NOTE]
> यदि तपाईंको पहिले नै सूची छ भने, त्यसलाई पनि उही मार्करहरूले घेरिदिनुहोस्। अर्को रनले यसलाई सबैभन्दा नयाँ मानकीकृत सामग्रीले प्रतिस्थापन गर्नेछ।

---

## ग्लोबल सामग्री कसरी परिवर्तन गर्ने

यदि तपाईं सबै Beginners रिपोजिटोरीहरूमा देखिने मानकीकृत सामग्री अपडेट गर्न चाहनुहुन्छ भने:

1. टेम्प्लेट सम्पादन गर्नुहोस्: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. तपाईंका परिवर्तनहरू सहित Co-op Translator रिपोमा पुल रिक्वेस्ट खोल्नुहोस्
3. PR मर्ज भएपछि, Co‑op Translator को संस्करण अपडेट हुनेछ
4. अर्को पटक Co‑op Translator (CLI वा GitHub Action) लक्षित रिपोमा चल्दा, यो अपडेट गरिएको सेक्सन स्वचालित रूपमा समक्रमण गर्नेछ

यसले सबै Beginners रिपोजिटोरीहरूमा "अन्य कोर्सहरू" सामग्रीको लागि एकल सत्य स्रोत सुनिश्चित गर्दछ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->