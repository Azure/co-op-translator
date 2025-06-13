<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c64ba65e091e5d87385490fa63a8f574",
  "translation_date": "2025-06-12T12:34:00+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "hi"
}
-->
# Co-op Translator कमांड लाइन इंटरफेस (CLI) का उपयोग कैसे करें

## आवश्यकताएँ

- **Python 3.10 या उससे ऊपर**: Co-op Translator चलाने के लिए आवश्यक।

## सामग्री सूची

1. [रूट डायरेक्टरी में '.env' फ़ाइल बनाएं](./create-env-file.md)
   - चुने गए भाषा मॉडल सेवा के लिए आवश्यक कुंजियाँ शामिल करें।
   - यदि Azure Computer Vision की कुंजियाँ छोड़ दी गई हैं या `-md` निर्दिष्ट है, तो translator केवल Markdown मोड में काम करेगा।
1. [Co-op translator पैकेज इंस्टॉल करें](./install-package.md)
1. [Co-op Translator का उपयोग करके अपने प्रोजेक्ट का अनुवाद करें](./translator-your-project.md)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवाद में त्रुटियाँ या असत्यताएँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।