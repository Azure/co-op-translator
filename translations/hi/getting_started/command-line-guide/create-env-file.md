<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:09:38+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "hi"
}
-->
# रूट डायरेक्टरी में *.env* फाइल बनाएं

इस ट्यूटोरियल में, हम आपको Azure सेवाओं के लिए अपने पर्यावरण चर सेटअप करने के लिए *.env* फाइल का उपयोग करना सिखाएंगे। पर्यावरण चर आपको संवेदनशील क्रेडेंशियल्स, जैसे API कीज़, को सुरक्षित रूप से प्रबंधित करने की सुविधा देते हैं, बिना उन्हें सीधे कोडबेस में हार्ड-कोड किए।

> [!IMPORTANT]
> - केवल एक भाषा मॉडल सेवा (Azure OpenAI या OpenAI) को कॉन्फ़िगर करना आवश्यक है। अपनी पसंदीदा सेवा के लिए पर्यावरण चर भरें। यदि कई भाषा मॉडलों के पर्यावरण चर सेट किए गए हैं, तो सहायक अनुवादक प्राथमिकता के आधार पर एक का चयन करेगा।
> - यदि Computer Vision के पर्यावरण चर सेट नहीं हैं, तो अनुवादक स्वचालित रूप से [Markdown-only mode](./markdown-only-mode.md) में स्विच हो जाएगा।

> [!NOTE]
> यह गाइड मुख्य रूप से Azure सेवाओं पर केंद्रित है, लेकिन आप [supported models and services list](../README.md#-supported-models-and-services) में से कोई भी समर्थित भाषा मॉडल चुन सकते हैं।

## *.env* फाइल बनाएं

अपने प्रोजेक्ट की रूट डायरेक्टरी में, *.env* नाम की एक फाइल बनाएं। यह फाइल आपके सभी पर्यावरण चर एक सरल प्रारूप में स्टोर करेगी।

> [!WARNING]
> अपनी *.env* फाइल को Git जैसे वर्शन कंट्रोल सिस्टम में कमिट न करें। आकस्मिक कमिट से बचने के लिए *.env* को अपनी .gitignore फाइल में जोड़ें।

1. अपने प्रोजेक्ट की रूट डायरेक्टरी पर जाएं।

1. प्रोजेक्ट की रूट डायरेक्टरी में *.env* फाइल बनाएं।

1. *.env* फाइल खोलें और निम्न टेम्प्लेट पेस्ट करें:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> यदि आप अपनी API कीज़ और एंडपॉइंट्स ढूंढना चाहते हैं, तो आप [set-up-azure-ai.md](../set-up-azure-ai.md) देख सकते हैं।

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।