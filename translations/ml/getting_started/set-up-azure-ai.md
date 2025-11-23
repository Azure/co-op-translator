<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b58d7c3cb4210697a073d20eb3064945",
  "translation_date": "2025-11-23T02:20:32+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "ml"
}
-->
# Azure AI Co-op Translator (Azure OpenAI & Azure AI Vision) സജ്ജമാക്കുക

ഈ മാർഗ്ഗനിർദ്ദേശം, Azure AI Foundry-യിൽ Azure OpenAI ഉപയോഗിച്ച് ഭാഷാ വിവർത്തനം നടത്താനും Azure Computer Vision ഉപയോഗിച്ച് ചിത്രത്തിന്റെ ഉള്ളടക്കം വിശകലനം ചെയ്യാനും (ചിത്രത്തെ അടിസ്ഥാനമാക്കിയുള്ള വിവർത്തനത്തിന് ഉപയോഗിക്കാവുന്നതാണ്) സഹായിക്കുന്നു.

**ആവശ്യകതകൾ:**
- സജീവ സബ്സ്ക്രിപ്ഷനുള്ള Azure അക്കൗണ്ട്.
- നിങ്ങളുടെ Azure സബ്സ്ക്രിപ്ഷനിൽ റിസോഴ്സുകളും ഡിപ്ലോയ്മെന്റുകളും സൃഷ്ടിക്കാൻ മതിയായ അനുമതികൾ.

## Azure AI പ്രോജക്റ്റ് സൃഷ്ടിക്കുക

നിങ്ങളുടെ AI റിസോഴ്സുകൾ കൈകാര്യം ചെയ്യുന്നതിനുള്ള കേന്ദ്രസ്ഥാനം ആയി പ്രവർത്തിക്കുന്ന Azure AI പ്രോജക്റ്റ് സൃഷ്ടിച്ച് തുടങ്ങുക.

1. [https://ai.azure.com](https://ai.azure.com) എന്നതിലേക്ക് പോകുക, Azure അക്കൗണ്ട് ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക.

1. **+Create** തിരഞ്ഞെടുക്കുക, പുതിയ പ്രോജക്റ്റ് സൃഷ്ടിക്കുക.

1. താഴെ പറയുന്ന കാര്യങ്ങൾ ചെയ്യുക:
   - **Project name** നൽകുക (ഉദാ., `CoopTranslator-Project`).
   - **AI hub** തിരഞ്ഞെടുക്കുക (ഉദാ., `CoopTranslator-Hub`) (ആവശ്യമെങ്കിൽ പുതിയത് സൃഷ്ടിക്കുക).

1. "**Review and Create**" ക്ലിക്ക് ചെയ്ത് നിങ്ങളുടെ പ്രോജക്റ്റ് സജ്ജമാക്കുക. നിങ്ങൾ പ്രോജക്റ്റിന്റെ ഓവർവ്യൂ പേജിലേക്ക് കൊണ്ടുപോകും.

## ഭാഷാ വിവർത്തനത്തിനായി Azure OpenAI സജ്ജമാക്കുക

നിങ്ങളുടെ പ്രോജക്റ്റിനുള്ളിൽ, ടെക്സ്റ്റ് വിവർത്തനത്തിന് ബാക്ക്‌എൻഡ് ആയി പ്രവർത്തിക്കുന്ന Azure OpenAI മോഡൽ ഡിപ്ലോയ് ചെയ്യുക.

### നിങ്ങളുടെ പ്രോജക്റ്റിലേക്ക് പോകുക

നിങ്ങളുടെ പുതിയ പ്രോജക്റ്റ് (ഉദാ., `CoopTranslator-Project`) Azure AI Foundry-ൽ തുറക്കുക.

### OpenAI മോഡൽ ഡിപ്ലോയ് ചെയ്യുക

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ ഇടത്-കൈ മെനുവിൽ, "My assets" കീഴിൽ **Models + endpoints** തിരഞ്ഞെടുക്കുക.

1. **+ Deploy model** തിരഞ്ഞെടുക്കുക.

1. **Deploy Base Model** തിരഞ്ഞെടുക്കുക.

1. ലഭ്യമായ മോഡലുകളുടെ പട്ടിക നിങ്ങൾക്ക് കാണിക്കും. അനുയോജ്യമായ GPT മോഡൽ ഫിൽട്ടർ ചെയ്യുക അല്ലെങ്കിൽ തിരയുക. `gpt-4o` ശുപാർശ ചെയ്യുന്നു.

1. നിങ്ങളുടെ മോഡൽ തിരഞ്ഞെടുക്കുക, **Confirm** ക്ലിക്ക് ചെയ്യുക.

1. **Deploy** തിരഞ്ഞെടുക്കുക.

### Azure OpenAI കോൺഫിഗറേഷൻ

ഡിപ്ലോയ് ചെയ്ത ശേഷം, "**Models + endpoints**" പേജിൽ നിന്ന് **REST endpoint URL**, **Key**, **Deployment name**, **Model name**, **API version** എന്നിവ കണ്ടെത്താൻ ഡിപ്ലോയ്‌മെന്റ് തിരഞ്ഞെടുക്കാം. ഈ വിവരങ്ങൾ നിങ്ങളുടെ ആപ്ലിക്കേഷനിൽ വിവർത്തന മോഡൽ സംയോജിപ്പിക്കാൻ ആവശ്യമാണ്.

> [!NOTE]
> നിങ്ങളുടെ ആവശ്യകതകൾ അനുസരിച്ച് [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) പേജിൽ നിന്ന് API പതിപ്പുകൾ തിരഞ്ഞെടുക്കാം. **API version** Azure AI Foundry-യിലെ **Models + endpoints** പേജിൽ കാണുന്ന **Model version**-നുമായി വ്യത്യസ്തമാണ്.

## ചിത്ര വിവർത്തനത്തിനായി Azure Computer Vision സജ്ജമാക്കുക

ചിത്രങ്ങളിലെ ടെക്സ്റ്റ് വിവർത്തനം സജ്ജമാക്കാൻ, Azure AI Service API Key, Endpoint കണ്ടെത്തുക.

1. നിങ്ങളുടെ Azure AI പ്രോജക്റ്റിലേക്ക് (ഉദാ., `CoopTranslator-Project`) പോകുക. നിങ്ങൾ പ്രോജക്റ്റ് ഓവർവ്യൂ പേജിൽ ഉണ്ടെന്ന് ഉറപ്പാക്കുക.

### Azure AI Service കോൺഫിഗറേഷൻ

Azure AI Service-ൽ നിന്ന് API Key, Endpoint കണ്ടെത്തുക.

1. നിങ്ങളുടെ Azure AI പ്രോജക്റ്റിലേക്ക് (ഉദാ., `CoopTranslator-Project`) പോകുക. നിങ്ങൾ പ്രോജക്റ്റ് ഓവർവ്യൂ പേജിൽ ഉണ്ടെന്ന് ഉറപ്പാക്കുക.

1. Azure AI Service ടാബിൽ നിന്ന് **API Key**, **Endpoint** കണ്ടെത്തുക.

    ![API Key, Endpoint കണ്ടെത്തുക](../../../getting_started/imgs/find-azure-ai-info.png)

ഈ കണക്ഷൻ, ബന്ധിപ്പിച്ച Azure AI Services റിസോഴ്സിന്റെ (ചിത്ര വിശകലനം ഉൾപ്പെടെ) കഴിവുകൾ നിങ്ങളുടെ AI Foundry പ്രോജക്റ്റിൽ ലഭ്യമാക്കുന്നു. ഈ കണക്ഷൻ നിങ്ങളുടെ നോട്ട്‌ബുക്കുകളിലും ആപ്ലിക്കേഷനുകളിലും ഉപയോഗിച്ച് ചിത്രങ്ങളിൽ നിന്ന് ടെക്സ്റ്റ് എക്സ്ട്രാക്റ്റ് ചെയ്യാം, പിന്നീട് Azure OpenAI മോഡലിലേക്ക് വിവർത്തനത്തിനായി അയക്കാം.

## നിങ്ങളുടെ ക്രെഡൻഷ്യലുകൾ ഏകീകരിക്കുക

ഇപ്പോൾ, നിങ്ങൾ താഴെ പറയുന്നവ ശേഖരിച്ചിരിക്കണം:

**Azure OpenAI (ടെക്സ്റ്റ് വിവർത്തനം) വേണ്ടി:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ഉദാ., `gpt-4o`)
- Azure OpenAI Deployment Name (ഉദാ., `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (ചിത്ര ടെക്സ്റ്റ് എക്സ്ട്രാക്ഷൻ Vision വഴി):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ഉദാഹരണം: പരിസ്ഥിതി വേരിയബിൾ കോൺഫിഗറേഷൻ (Preview)

പിന്നീട്, നിങ്ങളുടെ ആപ്ലിക്കേഷൻ നിർമ്മിക്കുമ്പോൾ, ഈ ശേഖരിച്ച ക്രെഡൻഷ്യലുകൾ ഉപയോഗിച്ച് ഇത് കോൺഫിഗർ ചെയ്യാൻ സാധ്യതയുണ്ട്. ഉദാഹരണത്തിന്, നിങ്ങൾ ഇത് പരിസ്ഥിതി വേരിയബിൾ ആയി സജ്ജമാക്കാം:

```bash
# Azure AI സേവന ക്രെഡൻഷ്യലുകൾ (ചിത്രം വിവർത്തനത്തിന് ആവശ്യമാണ്)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ഉദാ., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI ക്രെഡൻഷ്യലുകൾ (ടെക്സ്റ്റ് വിവർത്തനത്തിന് ആവശ്യമാണ്)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ഉദാ., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ഉദാ., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ഉദാ., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ഉദാ., 2024-12-01-preview
```

---

### കൂടുതൽ വായന

- [Azure AI Foundry-ൽ പ്രോജക്റ്റ് സൃഷ്ടിക്കുന്നതെങ്ങനെ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI റിസോഴ്സുകൾ സൃഷ്ടിക്കുന്നതെങ്ങനെ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry-ൽ OpenAI മോഡലുകൾ ഡിപ്ലോയ് ചെയ്യുന്നതെങ്ങനെ](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:  
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള മൗലിക രേഖയാണ് വിശ്വസനീയമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->