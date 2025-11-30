<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:40:42+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "mr"
}
-->
# "इतर कोर्सेस" विभाग अद्यतनित करा (Microsoft Beginners रेपॉजिटरीज)

हा मार्गदर्शक "इतर कोर्सेस" विभाग कसा स्वयंचलितपणे समक्रमित करायचा हे Co-op Translator वापरून स्पष्ट करतो, आणि सर्व रेपॉजिटरीजसाठी जागतिक टेम्पलेट कसे अद्यतनित करायचे ते सांगतो.

- लागू: फक्त Microsoft Beginners रेपॉजिटरीजसाठी
- काम करते: Co-op Translator CLI आणि GitHub Actions सह
- टेम्पलेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## जलद प्रारंभ: तुमच्या रेपॉमध्ये ऑटो-सिंक सक्षम करा

तुमच्या README मध्ये "इतर कोर्सेस" विभागाभोवती खालील मार्कर्स जोडा. Co-op Translator प्रत्येक वेळी चालवताना या मार्कर्समधील सर्व काही बदलेल.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

प्रत्येक वेळी Co-op Translator चालवला जातो—CLI द्वारे (उदा., `translate -l "<language codes>"`) किंवा GitHub Actions द्वारे—तो या मार्कर्सने वेढलेल्या "इतर कोर्सेस" विभागाला स्वयंचलितपणे अद्यतनित करतो.

> [!NOTE]
> जर तुमच्याकडे आधीच यादी असेल, तर ती फक्त त्याच मार्कर्सने वेढा. पुढील वेळी चालवताना ती नवीनतम प्रमाणित सामग्रीने बदलली जाईल.

---

## जागतिक सामग्री कशी बदलायची

जर तुम्हाला सर्व Beginners रेपॉजिटरीजमध्ये दिसणारी प्रमाणित सामग्री अद्यतनित करायची असेल:

1. टेम्पलेट संपादित करा: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. तुमच्या बदलांसह Co-op Translator रेपॉमध्ये पुल रिक्वेस्ट उघडा
3. PR मर्ज झाल्यानंतर, Co-op Translator ची आवृत्ती अद्यतनित होईल
4. पुढच्या वेळी Co-op Translator (CLI किंवा GitHub Action) लक्ष्य रेपॉमध्ये चालवला गेला, तेव्हा तो अद्यतनित विभाग स्वयंचलितपणे समक्रमित करेल

हे सर्व Beginners रेपॉजिटरीजमध्ये "इतर कोर्सेस" सामग्रीसाठी एकच सत्य स्रोत सुनिश्चित करते.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->