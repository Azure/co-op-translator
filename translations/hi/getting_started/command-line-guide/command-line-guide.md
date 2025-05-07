<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:52:40+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "hi"
}
-->
# Co-op Translator कमांड लाइन इंटरफेस (CLI) का उपयोग कैसे करें

## आवश्यकताएँ

- **Python 3.10 या उससे ऊपर**: Co-op Translator चलाने के लिए आवश्यक।
- **Language Model Resource**:  
  - **Azure OpenAI** या अन्य LLMs। विवरण [supported models and services](../../../../README.md) में उपलब्ध हैं।  
- **Computer Vision Resource** (वैकल्पिक):  
  - इमेज अनुवाद के लिए। यदि उपलब्ध नहीं है, तो translator [Markdown-only mode](../markdown-only-mode.md) में काम करेगा।  
  - **Azure Computer Vision**

### प्रारंभिक सेटअप

शुरू करने से पहले, निम्नलिखित संसाधनों को सेटअप करना सुनिश्चित करें:

- [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (वैकल्पिक)

## विषय सूची

1. [रूट डायरेक्टरी में '.env' फ़ाइल बनाएं](./create-env-file.md)  
   - चुने गए language model सेवा के लिए आवश्यक keys शामिल करें।  
   - यदि Azure Computer Vision keys छोड़ दिए गए हैं या `-md` निर्दिष्ट है, तो translator Markdown-only mode में काम करेगा।  
3. [Co-op translator पैकेज इंस्टॉल करें](./install-package.md)  
4. [Co-op Translator का उपयोग करके अपने प्रोजेक्ट का अनुवाद करें](./translator-your-project.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।