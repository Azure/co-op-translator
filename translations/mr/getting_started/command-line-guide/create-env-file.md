<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:41:04+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "mr"
}
-->
# मूळ डिरेक्टरीत *.env* फाइल तयार करा

या ट्यूटोरियलमध्ये, आम्ही तुम्हाला Azure सेवांसाठी तुमचे पर्यावरणीय चल सेट करण्यासाठी *.env* फाइल तयार करण्याचा मार्गदर्शन करू. पर्यावरणीय चल तुम्हाला संवेदनशील क्रेडेन्शियल्स जसे की API की सुरक्षितपणे व्यवस्थापित करण्याची परवानगी देतात, ज्यामुळे तुम्हाला ते कोडमध्ये हार्ड-कोड करण्याची गरज नाही.

> [!IMPORTANT]
> - फक्त एका भाषा मॉडेल सेवा (Azure OpenAI किंवा OpenAI) साठी कॉन्फिगर करणे आवश्यक आहे. तुमच्या पसंतीच्या सेवेसाठी पर्यावरणीय चल भरा. जर एकापेक्षा जास्त भाषा मॉडेलसाठी पर्यावरणीय चल सेट केले गेले, तर सहकार्य अनुवादक प्राधान्यक्रमानुसार एक निवडेल.
> - जर Computer Vision साठी पर्यावरणीय चल सेट केलेले नसतील, तर अनुवादक आपोआप [Markdown-only mode](./markdown-only-mode.md) मध्ये स्विच होईल.

> [!NOTE]
> हा मार्गदर्शक मुख्यत्वे Azure सेवांवर लक्ष केंद्रित करतो, पण तुम्ही [supported models and services list](../README.md#-supported-models-and-services) मधील कोणतेही समर्थित भाषा मॉडेल निवडू शकता.

## *.env* फाइल तयार करा

तुमच्या प्रोजेक्टच्या मूळ डिरेक्टरीत, *.env* नावाची एक फाइल तयार करा. ही फाइल सर्व पर्यावरणीय चल सोप्या स्वरूपात साठवेल.

> [!WARNING]
> तुमची *.env* फाइल Git सारख्या आवृत्ती नियंत्रण प्रणालीमध्ये कमिट करू नका. चुकीने कमिट होण्यापासून प्रतिबंध करण्यासाठी *.env* ला तुमच्या .gitignore फाइलमध्ये जोडा.

1. तुमच्या प्रोजेक्टच्या मूळ डिरेक्टरीकडे जा.

1. प्रोजेक्टच्या मूळ डिरेक्टरीत *.env* फाइल तयार करा.

1. *.env* फाइल उघडा आणि खालील टेम्पलेट पेस्ट करा:

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
> जर तुम्हाला तुमच्या API की आणि endpoints शोधायच्या असतील, तर तुम्ही [set-up-azure-ai.md](../set-up-azure-ai.md) कडे पाहू शकता.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत फरक असू शकतो. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती साठी व्यावसायिक मानवी अनुवाद शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.