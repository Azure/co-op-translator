<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:41:16+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ne"
}
-->
# रुट डाइरेक्टरीमा *.env* फाइल बनाउनुहोस्

यस ट्युटोरियलमा, हामी तपाईंलाई Azure सेवाहरूको लागि वातावरण भेरिएबलहरू सेटअप गर्ने तरिका देखाउनेछौं जसमा *.env* फाइल प्रयोग गरिन्छ। वातावरण भेरिएबलहरूले तपाईंलाई संवेदनशील प्रमाणपत्रहरू, जस्तै API कुञ्जीहरू, सुरक्षित रूपमा व्यवस्थापन गर्न अनुमति दिन्छन्, जसलाई तपाईंले कोडमा सिधै लेख्नु पर्दैन।

> [!IMPORTANT]
> - केवल एउटा भाषा मोडेल सेवा (Azure OpenAI वा OpenAI) कन्फिगर गर्न आवश्यक छ। तपाईंले आफ्नो रोजेको सेवाको वातावरण भेरिएबलहरू भर्नुहोस्। यदि धेरै भाषा मोडेलका वातावरण भेरिएबलहरू सेट गरिएको छ भने, सह-अनुवादक प्राथमिकताका आधारमा एउटा चयन गर्नेछ।
> - यदि Computer Vision का वातावरण भेरिएबलहरू सेट गरिएको छैन भने, अनुवादकले स्वतः [Markdown-only मोड](./markdown-only-mode.md) मा स्विच गर्नेछ।

> [!NOTE]
> यो मार्गदर्शन मुख्य रूपमा Azure सेवाहरूमा केन्द्रित छ, तर तपाईं [supported models and services list](../README.md#-supported-models-and-services) बाट कुनै पनि समर्थित भाषा मोडेल चयन गर्न सक्नुहुन्छ।

## *.env* फाइल बनाउनुहोस्

तपाईंको प्रोजेक्टको रुट डाइरेक्टरीमा *.env* नामक फाइल बनाउनुहोस्। यस फाइलमा तपाईंका सबै वातावरण भेरिएबलहरू सरल ढाँचामा राखिनेछन्।

> [!WARNING]
> *.env* फाइललाई Git जस्ता भर्सन कन्ट्रोल प्रणालीमा कमिट नगर्नुहोस्। गल्तीले कमिट हुन नदिन *.env* लाई .gitignore फाइलमा थप्नुहोस्।

1. तपाईंको प्रोजेक्टको रुट डाइरेक्टरीमा जानुहोस्।

1. प्रोजेक्टको रुट डाइरेक्टरीमा *.env* फाइल बनाउनुहोस्।

1. *.env* फाइल खोल्नुहोस् र तलको टेम्प्लेट पेस्ट गर्नुहोस्:

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
> यदि तपाईं आफ्नो API कुञ्जीहरू र एन्डपोइन्टहरू खोज्न चाहनुहुन्छ भने, [set-up-azure-ai.md](../set-up-azure-ai.md) मा हेर्न सक्नुहुन्छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असङ्गतिहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनेछ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।