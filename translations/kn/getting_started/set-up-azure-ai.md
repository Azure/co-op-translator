<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b58d7c3cb4210697a073d20eb3064945",
  "translation_date": "2025-11-24T06:37:25+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "kn"
}
-->
# Azure AI ಅನ್ನು Co-op Translator (Azure OpenAI & Azure AI Vision) ಗೆ ಸೆಟ್ ಅಪ್ ಮಾಡುವುದು

ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮ್ಮನ್ನು ಭಾಷಾ ಅನುವಾದಕ್ಕಾಗಿ Azure OpenAI ಮತ್ತು ಚಿತ್ರ ಆಧಾರಿತ ಅನುವಾದಕ್ಕಾಗಿ ಚಿತ್ರ ವಿಷಯ ವಿಶ್ಲೇಷಣೆಗೆ Azure Computer Vision ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುವ ಪ್ರಕ್ರಿಯೆ ಮೂಲಕ Azure AI Foundry ನಲ್ಲಿ ನಡೆಸುತ್ತದೆ.

**ಪೂರ್ವಶರತ್ತುಗಳು:**
- ಸಕ್ರಿಯ ಚಂದಾದಾರಿಕೆಯನ್ನು ಹೊಂದಿರುವ Azure ಖಾತೆ.
- ನಿಮ್ಮ Azure ಚಂದಾದಾರಿಕೆಯಲ್ಲಿ ಸಂಪತ್ತುಗಳನ್ನು ಮತ್ತು ನಿಯೋಜನೆಗಳನ್ನು ರಚಿಸಲು ಸಾಕಷ್ಟು ಅನುಮತಿಗಳು.

## Azure AI ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಿ

ನೀವು ನಿಮ್ಮ AI ಸಂಪತ್ತುಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಕೇಂದ್ರ ಸ್ಥಳವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ Azure AI ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು ರಚಿಸುವ ಮೂಲಕ ಪ್ರಾರಂಭಿಸುತ್ತೀರಿ.

1. [https://ai.azure.com](https://ai.azure.com) ಗೆ ಹೋಗಿ ಮತ್ತು ನಿಮ್ಮ Azure ಖಾತೆ ಬಳಸಿ ಲಾಗಿನ್ ಮಾಡಿ.

1. **+Create** ಆಯ್ಕೆ ಮಾಡಿ ಹೊಸ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು ರಚಿಸಲು.

1. ಈ ಕೆಳಗಿನ ಕಾರ್ಯಗಳನ್ನು ಮಾಡಿ:
   - **Project name** ನಮೂದಿಸಿ (ಉದಾ., `CoopTranslator-Project`).
   - **AI hub** ಆಯ್ಕೆಮಾಡಿ (ಉದಾ., `CoopTranslator-Hub`) (ಅವಶ್ಯಕತೆ ಇದ್ದರೆ ಹೊಸದನ್ನು ರಚಿಸಿ).

1. "**Review and Create**" ಕ್ಲಿಕ್ ಮಾಡಿ ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಲು. ನೀವು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಅವಲೋಕನ ಪುಟಕ್ಕೆ ಕರೆದೊಯ್ಯಲ್ಪಡುತ್ತೀರಿ.

## ಭಾಷಾ ಅನುವಾದಕ್ಕಾಗಿ Azure OpenAI ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುವುದು

ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನಲ್ಲಿ, ನೀವು ಪಠ್ಯ ಅನುವಾದಕ್ಕಾಗಿ ಬ್ಯಾಕೆಂಡ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಲು Azure OpenAI ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸುತ್ತೀರಿ.

### ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ

ನೀವು ಈಗಾಗಲೇ ಅಲ್ಲದಿದ್ದರೆ, ನಿಮ್ಮ ಹೊಸದಾಗಿ ರಚಿಸಿದ ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾ., `CoopTranslator-Project`) ಅನ್ನು Azure AI Foundry ನಲ್ಲಿ ತೆರೆಯಿರಿ.

### OpenAI ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡಗಡೆಯ ಮೆನುದಿಂದ, "My assets" ಅಡಿಯಲ್ಲಿ, "**Models + endpoints**" ಆಯ್ಕೆಮಾಡಿ.

1. **+ Deploy model** ಆಯ್ಕೆಮಾಡಿ.

1. **Deploy Base Model** ಆಯ್ಕೆಮಾಡಿ.

1. ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳ ಪಟ್ಟಿ ನಿಮಗೆ ತೋರಿಸಲಾಗುತ್ತದೆ. ಸೂಕ್ತ GPT ಮಾದರಿಯನ್ನು ಫಿಲ್ಟರ್ ಅಥವಾ ಹುಡುಕಿ. ನಾವು `gpt-4o` ಅನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ.

1. ನಿಮ್ಮ ಇಚ್ಛಿತ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ಮತ್ತು **Confirm** ಕ್ಲಿಕ್ ಮಾಡಿ.

1. **Deploy** ಆಯ್ಕೆಮಾಡಿ.

### Azure OpenAI ಸಂರಚನೆ

ನಿಯೋಜನೆ ಮಾಡಿದ ನಂತರ, ನೀವು "**Models + endpoints**" ಪುಟದಿಂದ ನಿಯೋಜನೆ ಆಯ್ಕೆಮಾಡಬಹುದು ಮತ್ತು ಅದರ **REST endpoint URL**, **Key**, **Deployment name**, **Model name** ಮತ್ತು **API version** ಅನ್ನು ಕಂಡುಹಿಡಿಯಬಹುದು. ಇವು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಅನುವಾದ ಮಾದರಿಯನ್ನು ಸಂಯೋಜಿಸಲು ಅಗತ್ಯವಿರುತ್ತದೆ.

> [!NOTE]
> ನೀವು ನಿಮ್ಮ ಅಗತ್ಯಗಳ ಆಧಾರದ ಮೇಲೆ [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) ಪುಟದಿಂದ API ಆವೃತ್ತಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಬಹುದು. **API version** ಅನ್ನು **Models + endpoints** ಪುಟದಲ್ಲಿ ತೋರಿಸಲಾಗುವ **Model version** ಗೆ ಭಿನ್ನವಾಗಿದೆ ಎಂಬುದನ್ನು ಗಮನಿಸಿ.

## ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ Azure Computer Vision ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುವುದು

ಚಿತ್ರಗಳಲ್ಲಿ ಪಠ್ಯದ ಅನುವಾದವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಲು, ನೀವು Azure AI Service API Key ಮತ್ತು Endpoint ಅನ್ನು ಕಂಡುಹಿಡಿಯಬೇಕು.

1. ನಿಮ್ಮ Azure AI ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾ., `CoopTranslator-Project`) ಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ. ನೀವು ಪ್ರಾಜೆಕ್ಟ್ ಅವಲೋಕನ ಪುಟದಲ್ಲಿ ಇದ್ದೀರಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

### Azure AI Service ಸಂರಚನೆ

Azure AI Service ನಿಂದ API Key ಮತ್ತು Endpoint ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.

1. ನಿಮ್ಮ Azure AI ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾ., `CoopTranslator-Project`) ಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ. ನೀವು ಪ್ರಾಜೆಕ್ಟ್ ಅವಲೋಕನ ಪುಟದಲ್ಲಿ ಇದ್ದೀರಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

1. Azure AI Service ಟ್ಯಾಬ್‌ನಿಂದ **API Key** ಮತ್ತು **Endpoint** ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.

    ![API Key ಮತ್ತು Endpoint ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ](../../../getting_started/imgs/find-azure-ai-info.png)

ಈ ಸಂಪರ್ಕವು ಲಿಂಕ್ ಮಾಡಲಾದ Azure AI Services ಸಂಪತ್ತಿನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು (ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಒಳಗೊಂಡಂತೆ) ನಿಮ್ಮ AI Foundry ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ಲಭ್ಯವಾಗುವಂತೆ ಮಾಡುತ್ತದೆ. ನಂತರ ನೀವು ಈ ಸಂಪರ್ಕವನ್ನು ನಿಮ್ಮ ನೋಟ್ಬುಕ್‌ಗಳು ಅಥವಾ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಚಿತ್ರಗಳಿಂದ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆದು, ಅದನ್ನು ಅನುವಾದಕ್ಕಾಗಿ Azure OpenAI ಮಾದರಿಗೆ ಕಳುಹಿಸಲು ಬಳಸಬಹುದು.

## ನಿಮ್ಮ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳನ್ನು ಒಗ್ಗೂಡಿಸುವುದು

ಈಗಾಗಲೇ, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಸಂಗ್ರಹಿಸಿರಬೇಕು:

**Azure OpenAI (ಪಠ್ಯ ಅನುವಾದಕ್ಕಾಗಿ):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ಉದಾ., `gpt-4o`)
- Azure OpenAI Deployment Name (ಉದಾ., `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (Vision ಮೂಲಕ ಚಿತ್ರ ಪಠ್ಯ ಹೊರತೆಗೆಯುವುದು):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ಉದಾಹರಣೆ: ಪರಿಸರ ವ್ಯತ್ಯಯ ಸಂರಚನೆ (ಪೂರ್ವವೀಕ್ಷಣೆ)

ನಂತರ, ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಿರ್ಮಿಸುವಾಗ, ನೀವು ಈ ಸಂಗ್ರಹಿಸಿದ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಅದನ್ನು ಸಂರಚಿಸುವ ಸಾಧ್ಯತೆ ಇದೆ. ಉದಾಹರಣೆಗೆ, ನೀವು ಅವುಗಳನ್ನು ಪರಿಸರ ವ್ಯತ್ಯಯಗಳಾಗಿ ಈ ರೀತಿಯಾಗಿ ಸೆಟ್ ಮಾಡಬಹುದು:

```bash
# ಆಜೂರ್ AI ಸೇವಾ ಪ್ರಮಾಣಪತ್ರಗಳು (ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಅಗತ್ಯವಿದೆ)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ಉದಾ., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ಆಜೂರ್ OpenAI ಪ್ರಮಾಣಪತ್ರಗಳು (ಪಠ್ಯ ಅನುವಾದಕ್ಕಾಗಿ ಅಗತ್ಯವಿದೆ)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ಉದಾ., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ಉದಾ., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ಉದಾ., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ಉದಾ., 2024-12-01-preview
```

---

### ಹೆಚ್ಚಿನ ಓದು

- [Azure AI Foundry ನಲ್ಲಿ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸುವ ವಿಧಾನ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI ಸಂಪತ್ತುಗಳನ್ನು ರಚಿಸುವ ವಿಧಾನ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry ನಲ್ಲಿ OpenAI ಮಾದರಿಗಳನ್ನು ನಿಯೋಜಿಸುವ ವಿಧಾನ](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸಮಾಕ್ಷಿಕೆ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸಮಾಕ್ಷಿತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->