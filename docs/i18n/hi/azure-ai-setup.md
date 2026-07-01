# Azure AI सेटअप

यह मार्गदर्शिका तब उपयोग करें जब आप टेक्स्ट अनुवाद के लिए Azure OpenAI और छवि में टेक्स्ट निकालने के लिए Azure AI Vision कॉन्फ़िगर करना चाहें।

## पूर्वापेक्षाएँ

- एक Azure सदस्यता।
- Azure AI संसाधन और मॉडल डिप्लॉयमेंट बनाने या उपयोग करने की अनुमति।
- Azure AI Foundry में एक प्रोजेक्ट या Azure OpenAI और Azure AI Vision संसाधनों तक समकक्ष पहुँच।

## एक Azure AI प्रोजेक्ट बनाएं

1. [Azure AI Foundry](https://ai.azure.com) खोलें।
2. एक प्रोजेक्ट बनाएं या चुनें।
3. प्रोजेक्ट के लिए एक AI हब बनाएं या चुनें।
4. निर्माण के बाद प्रोजेक्ट का अवलोकन खोलें।

## एक Azure OpenAI मॉडल तैनात करें

1. प्रोजेक्ट में **मॉडल + एंडपॉइंट्स** खोलें।
2. **मॉडल तैनात करें** चुनें।
3. `gpt-4o` जैसे GPT मॉडल चुनें।
4. मॉडल तैनात करें।
5. एंडपॉइंट, डिप्लॉयमेंट नाम, मॉडल नाम, API कुंजी, और API संस्करण रिकॉर्ड करें।

!!! note
    Azure AI Foundry में दिखाए गए मॉडल वर्शन से Azure OpenAI API संस्करण अलग है। अपनी तैनाती के लिए एक समर्थित API संस्करण चुनें।

## Azure AI Vision कॉन्फ़िगर करें

इमेज अनुवाद में स्रोत छवियों से टेक्स्ट निकालने के लिए Azure AI Vision का उपयोग किया जाता है, उसके बाद टेक्स्ट का अनुवाद किया जाता है।

अपने Azure AI प्रोजेक्ट में, Azure AI सर्विसेज कुंजी और एंडपॉइंट ढूंढें।

![Azure AI सेवा जानकारी खोजें](../../assets/find-azure-ai-info.png)

Record:

- Azure AI सेवा एंडपॉइंट
- Azure AI सेवा API कुंजी

## पर्यावरण वेरिएबल

प्रमाण-पत्र अपनी `.env` फ़ाइल या CI secrets में जोड़ें।

```bash
# Azure AI Vision, छवि अनुवाद के लिए आवश्यक
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, पाठ अनुवाद के लिए आवश्यक
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator वैकल्पिक फॉलबैक क्रेडेंशियल सेट्स का भी समर्थन करता है। एक पूर्ण प्रदाता सेट को `_1` या `_2` जैसे उपसर्गों के साथ डुप्लिकेट करें; फॉलबैक सेट में सभी वेरिएबल्स का वही उपसर्ग होना चाहिए।

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## अगले कदम

- [कॉन्फ़िगरेशन](configuration.md) पर लौटें ताकि स्थानीय या CI पर्यावरण वेरिएबल सेट कर सकें।
- अनुवाद कमांड्स के लिए [CLI संदर्भ](cli.md) का उपयोग करें।
- अनुवाद पुल रिक्वेस्ट्स को स्वचालित करने के लिए [GitHub Actions](github-actions.md) का उपयोग करें।