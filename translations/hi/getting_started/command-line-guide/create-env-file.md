<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:54:49+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "hi"
}
-->
# रूट डायरेक्टरी में *.env* फ़ाइल बनाएं

इस ट्यूटोरियल में, हम आपको Azure सेवाओं के लिए अपने पर्यावरण चर सेटअप करने में मार्गदर्शन करेंगे, जो कि *.env* फ़ाइल का उपयोग करके किया जाएगा। पर्यावरण चर आपको संवेदनशील क्रेडेंशियल्स, जैसे API कुंजियाँ, को सुरक्षित रूप से प्रबंधित करने की अनुमति देते हैं, बिना उन्हें अपने कोडबेस में हार्ड-कोड किए।

> [!IMPORTANT]
> - केवल एक भाषा मॉडल सेवा (Azure OpenAI या OpenAI) को कॉन्फ़िगर करना आवश्यक है। अपनी पसंदीदा सेवा के लिए पर्यावरण चर भरें। यदि कई भाषा मॉडलों के लिए पर्यावरण चर सेट हैं, तो को-ऑप ट्रांसलेटर प्राथमिकता के आधार पर एक का चयन करेगा।
> - यदि कंप्यूटर विज़न के पर्यावरण चर सेट नहीं हैं, तो ट्रांसलेटर स्वचालित रूप से [Markdown-only मोड](./markdown-only-mode.md) पर स्विच हो जाएगा।

> [!NOTE]
> यह गाइड मुख्य रूप से Azure सेवाओं पर केंद्रित है, लेकिन आप [समर्थित मॉडल और सेवाओं की सूची](../README.md#-supported-models-and-services) से कोई भी समर्थित भाषा मॉडल चुन सकते हैं।

## *.env* फ़ाइल बनाएं

अपने प्रोजेक्ट की रूट डायरेक्टरी में, *.env* नाम की एक फ़ाइल बनाएं। यह फ़ाइल आपके सभी पर्यावरण चर एक सरल फॉर्मेट में स्टोर करेगी।

> [!WARNING]
> अपनी *.env* फ़ाइल को Git जैसे वर्शन कंट्रोल सिस्टम में कमिट न करें। गलती से कमिट से बचने के लिए *.env* को अपनी .gitignore फ़ाइल में जोड़ें।

1. अपने प्रोजेक्ट की रूट डायरेक्टरी पर जाएं।

1. रूट डायरेक्टरी में *.env* फ़ाइल बनाएं।

    ![Create *.env* file.](../../../../imgs/create-env.png)

1. *.env* फ़ाइल खोलें और निम्न टेम्पलेट पेस्ट करें:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
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

## अपने Azure क्रेडेंशियल्स इकट्ठा करें

पर्यावरण सेटअप के लिए आपको निम्न Azure क्रेडेंशियल्स की आवश्यकता होगी:

आप सभी विवरण [AI Foundry](https://ai.azure.com/build/overview) के प्रोजेक्ट ओवरव्यू पेज से प्राप्त कर सकते हैं।

![Foundry-overview](../../../../imgs/foundry-overview.png)


### Azure AI सेवा के लिए:

    - Azure Subscription Key: आपकी Azure AI सेवाओं की API कुंजी, जो आपको Azure AI सेवाओं तक पहुंच प्रदान करती है।
    - Azure AI Service Endpoint: आपके विशिष्ट Azure AI सेवा का एंडपॉइंट URL।

### Azure OpenAI सेवा के लिए:

    - Azure OpenAI API Key: Azure OpenAI सेवाओं तक पहुंचने के लिए API कुंजी।
    - Azure OpenAI Endpoint: आपके Azure OpenAI सेवा का एंडपॉइंट URL।


1. अपनी AI सेवाओं की कुंजी और एंडपॉइंट को *.env* फ़ाइल में कॉपी और पेस्ट करें।
2. अपनी Azure OpenAI API कुंजी और एंडपॉइंट को *.env* फ़ाइल में कॉपी और पेस्ट करें।

### मॉडल विवरण

बाएं मेनू से मॉडल और एंडपॉइंट चुनें

![FoundryModels](../../../../imgs/gpt-models.png)

अब आपको उस मॉडल का चयन करना होगा जिसे आप उपयोग करना चाहते हैं ताकि मॉडल विवरण प्राप्त किया जा सके।

![ModelDetails](../../../../imgs/model-deployment-name.png)

.env फ़ाइल के लिए हमें निम्न विवरण चाहिए:

    - Azure OpenAI Model Name: वह मॉडल नाम जिससे आप इंटरैक्ट करेंगे।
    - Azure OpenAI Name: Azure OpenAI मॉडलों के लिए आपकी डिप्लॉयमेंट का नाम।
    - Azure OpenAI API Version: Azure OpenAI API का वह संस्करण जो URL स्ट्रिंग के अंत में पाया जाता है।

इन विवरणों को प्राप्त करने के लिए मॉडल डिप्लॉयमेंट चुनें।

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### Azure पर्यावरण चर जोड़ें

3. अपनी Azure OpenAI **Name** और मॉडल **Version** को *.env* फ़ाइल में कॉपी और पेस्ट करें।
4. *.env* फ़ाइल को सेव करें।
5. अब, आप इन पर्यावरण चर का उपयोग करके **Co-op Translator** को अपनी Azure सेवाओं के साथ एक्सेस कर सकते हैं।

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। हम सटीकता के लिए प्रयासरत हैं, लेकिन कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।