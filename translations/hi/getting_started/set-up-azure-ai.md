<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:19:28+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "hi"
}
-->
# Azure AI को-ऑप ट्रांसलेटर (Azure OpenAI & Azure AI Vision) के लिए सेटअप करें

यह गाइड आपको Azure AI Foundry में भाषा अनुवाद के लिए Azure OpenAI और छवि सामग्री विश्लेषण (जिसका उपयोग बाद में छवि-आधारित अनुवाद के लिए किया जा सकता है) के लिए Azure Computer Vision सेटअप करने के बारे में बताएगा।

**पूर्व आवश्यकताएँ:**
- एक सक्रिय सब्सक्रिप्शन वाला Azure खाता।
- आपके Azure सब्सक्रिप्शन में संसाधन और डिप्लॉयमेंट बनाने की पर्याप्त अनुमति।

## Azure AI प्रोजेक्ट बनाएं

आप Azure AI प्रोजेक्ट बनाकर शुरू करेंगे, जो आपके AI संसाधनों को प्रबंधित करने के लिए एक केंद्रीय स्थान के रूप में कार्य करता है।

1. [https://ai.azure.com](https://ai.azure.com) पर जाएं और अपने Azure खाते से साइन इन करें।

1. नया प्रोजेक्ट बनाने के लिए **+Create** चुनें।

1. निम्नलिखित कार्य करें:
   - एक **Project name** दर्ज करें (जैसे, `CoopTranslator-Project`)।
   - **AI hub** चुनें (जैसे, `CoopTranslator-Hub`) (यदि आवश्यक हो तो नया बनाएं)।

1. अपना प्रोजेक्ट सेटअप करने के लिए "**Review and Create**" पर क्लिक करें। आप अपने प्रोजेक्ट के ओवरव्यू पेज पर पहुंच जाएंगे।

## भाषा अनुवाद के लिए Azure OpenAI सेटअप करें

अपने प्रोजेक्ट के भीतर, आप टेक्स्ट अनुवाद के बैकएंड के रूप में एक Azure OpenAI मॉडल डिप्लॉय करेंगे।

### अपने प्रोजेक्ट पर जाएं

यदि आप पहले से वहाँ नहीं हैं, तो Azure AI Foundry में अपना नया बनाया गया प्रोजेक्ट (जैसे, `CoopTranslator-Project`) खोलें।

### OpenAI मॉडल डिप्लॉय करें

1. अपने प्रोजेक्ट के बाएँ मेनू में, "My assets" के अंतर्गत "**Models + endpoints**" चुनें।

1. **+ Deploy model** चुनें।

1. **Deploy Base Model** चुनें।

1. उपलब्ध मॉडलों की सूची दिखाई देगी। उपयुक्त GPT मॉडल खोजें या फ़िल्टर करें। हम `gpt-4o` की सलाह देते हैं।

1. अपनी पसंद का मॉडल चुनें और **Confirm** पर क्लिक करें।

1. **Deploy** चुनें।

### Azure OpenAI कॉन्फ़िगरेशन

डिप्लॉयमेंट के बाद, आप "**Models + endpoints**" पेज से डिप्लॉयमेंट चुनकर उसका **REST endpoint URL**, **Key**, **Deployment name**, **Model name** और **API version** देख सकते हैं। ये आपके एप्लिकेशन में अनुवाद मॉडल को इंटीग्रेट करने के लिए आवश्यक होंगे।

## छवि अनुवाद के लिए Azure Computer Vision सेटअप करें

छवियों के भीतर टेक्स्ट का अनुवाद सक्षम करने के लिए, आपको Azure AI Service API Key और Endpoint प्राप्त करने होंगे।

1. अपने Azure AI प्रोजेक्ट (जैसे, `CoopTranslator-Project`) पर जाएं। सुनिश्चित करें कि आप प्रोजेक्ट के ओवरव्यू पेज पर हैं।

### Azure AI Service कॉन्फ़िगरेशन

Azure AI Service से API Key और Endpoint खोजें।

1. अपने Azure AI प्रोजेक्ट (जैसे, `CoopTranslator-Project`) पर जाएं। सुनिश्चित करें कि आप प्रोजेक्ट के ओवरव्यू पेज पर हैं।

1. Azure AI Service टैब से **API Key** और **Endpoint** खोजें।

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

यह कनेक्शन लिंक्ड Azure AI Services संसाधन की क्षमताओं (जिसमें छवि विश्लेषण शामिल है) को आपके AI Foundry प्रोजेक्ट के लिए उपलब्ध कराता है। आप इस कनेक्शन का उपयोग अपने नोटबुक या एप्लिकेशन में छवियों से टेक्स्ट निकालने के लिए कर सकते हैं, जिसे बाद में अनुवाद के लिए Azure OpenAI मॉडल को भेजा जा सकता है।

## अपनी प्रमाण-पत्रों को एकत्रित करना

अब तक, आपको निम्नलिखित प्राप्त हो जाना चाहिए:

**Azure OpenAI (टेक्स्ट अनुवाद) के लिए:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (जैसे, `gpt-4o`)
- Azure OpenAI Deployment Name (जैसे, `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (दृष्टि के माध्यम से छवि टेक्स्ट निष्कर्षण) के लिए:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### उदाहरण: पर्यावरण चर कॉन्फ़िगरेशन (पूर्वावलोकन)

बाद में, जब आप अपना एप्लिकेशन बनाएंगे, तो आप संभवतः इन्हीं प्रमाण-पत्रों का उपयोग पर्यावरण चर के रूप में करेंगे। उदाहरण के लिए, आप उन्हें इस प्रकार सेट कर सकते हैं:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### आगे पढ़ने के लिए

- [Azure AI Foundry में प्रोजेक्ट कैसे बनाएं](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI संसाधन कैसे बनाएं](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry में OpenAI मॉडल कैसे डिप्लॉय करें](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।