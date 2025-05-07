<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba33aa8d5da0d3dd14322b77fcb63deb",
  "translation_date": "2025-05-06T17:48:10+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "hi"
}
-->
# समर्थित भाषाएँ

नीचे दी गई तालिका में **Co-op Translator** द्वारा वर्तमान में समर्थित भाषाओं की सूची है। इसमें भाषा कोड, भाषा के नाम, और प्रत्येक भाषा से जुड़ी ज्ञात समस्याएँ शामिल हैं। यदि आप किसी नई भाषा के लिए समर्थन जोड़ना चाहते हैं, तो कृपया संबंधित भाषा कोड, नाम, और उपयुक्त फ़ॉन्ट को `font_language_mappings.yml` फ़ाइल में `src/co_op_translator/fonts/` पर जोड़ें और परीक्षण के बाद पुल रिक्वेस्ट सबमिट करें।

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | No           |
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
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
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

## नई भाषा जोड़ना

नई भाषा के लिए समर्थन जोड़ने के लिए:

1. [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml) पर जाएँ।
2. भाषा कोड, नाम, और उपयुक्त फ़ॉन्ट फ़ाइल नाम जोड़ें। यदि भाषा दाएँ से बाएँ है, तो `rtl` विशेषता शामिल करना न भूलें।
3. यदि आपको नया फ़ॉन्ट उपयोग करना है, तो सुनिश्चित करें कि वह ओपन-सोर्स प्रोजेक्ट्स में मुफ्त उपयोग के लिए लाइसेंस और कॉपीराइट नियमों के अनुसार हो। सत्यापन के बाद, फ़ॉन्ट फ़ाइल को `src/co_op_translator/fonts/` निर्देशिका में जोड़ें।
4. अपने परिवर्तनों का स्थानीय रूप से परीक्षण करें ताकि नई भाषा ठीक से समर्थित हो।
5. अपने परिवर्तनों के साथ पुल रिक्वेस्ट सबमिट करें और PR विवरण में नई भाषा के जोड़ने का उल्लेख करें।

उदाहरण:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।