<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-11-23T02:23:00+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ml"
}
-->
# റൂട്ട് ഡയറക്ടറിയിൽ *.env* ഫയൽ സൃഷ്ടിക്കുക

ഈ ട്യൂട്ടോറിയലിൽ, *.env* ഫയൽ ഉപയോഗിച്ച് Azure സേവനങ്ങൾക്കുള്ള പരിസ്ഥിതി വേരിയബിളുകൾ സജ്ജമാക്കുന്നതിന് നിങ്ങളെ നയിക്കും. പരിസ്ഥിതി വേരിയബിളുകൾ API കീകൾ പോലുള്ള ഗൂഢമായ ക്രെഡൻഷ്യലുകൾ നിങ്ങളുടെ കോഡ്‌ബേസിൽ ഹാർഡ്-കോഡിംഗ് ചെയ്യാതെ സുരക്ഷിതമായി കൈകാര്യം ചെയ്യാൻ സഹായിക്കുന്നു.

> [!IMPORTANT]
> - ഒരു ഭാഷാ മോഡൽ സേവനം (Azure OpenAI അല്ലെങ്കിൽ OpenAI) മാത്രമേ കോൺഫിഗർ ചെയ്യേണ്ടതുള്ളൂ. നിങ്ങളുടെ ഇഷ്ട സേവനത്തിനുള്ള പരിസ്ഥിതി വേരിയബിളുകൾ പൂരിപ്പിക്കുക. ഒന്നിലധികം ഭാഷാ മോഡലുകൾക്കുള്ള പരിസ്ഥിതി വേരിയബിളുകൾ സജ്ജമാക്കിയാൽ, കോ-ഓപ്പ് ട്രാൻസ്ലേറ്റർ മുൻഗണന അടിസ്ഥാനമാക്കി ഒന്നിനെ തിരഞ്ഞെടുക്കും.
> - കംപ്യൂട്ടർ വിഷൻ പരിസ്ഥിതി വേരിയബിളുകൾ സജ്ജമാക്കിയിട്ടില്ലെങ്കിൽ, ട്രാൻസ്ലേറ്റർ സ്വയം [Markdown-only mode](./markdown-only-mode.md) ലേക്ക് മാറും.

> [!NOTE]
> ഈ മാർഗ്ഗനിർദ്ദേശം പ്രധാനമായും Azure സേവനങ്ങൾക്കാണ് ശ്രദ്ധ കേന്ദ്രീകരിക്കുന്നത്, പക്ഷേ നിങ്ങൾക്ക് [supported models and services list](../README.md#-supported-models-and-services) ലിസ്റ്റിൽ നിന്ന് പിന്തുണയുള്ള ഏതെങ്കിലും ഭാഷാ മോഡൽ തിരഞ്ഞെടുക്കാം.

## *.env* ഫയൽ സൃഷ്ടിക്കുക

നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ റൂട്ട് ഡയറക്ടറിയിൽ *.env* എന്ന പേരിൽ ഒരു ഫയൽ സൃഷ്ടിക്കുക. ഈ ഫയൽ നിങ്ങളുടെ പരിസ്ഥിതി വേരിയബിളുകൾ ഒരു ലളിതമായ ഫോർമാറ്റിൽ സംഭരിക്കും.

> [!WARNING]
> നിങ്ങളുടെ *.env* ഫയൽ Git പോലുള്ള വേർഷൻ കൺട്രോൾ സിസ്റ്റങ്ങളിൽ കമ്മിറ്റ് ചെയ്യരുത്. *.env* ഫയൽ .gitignore ഫയലിൽ ചേർത്ത് അനാവശ്യ കമ്മിറ്റുകൾ ഒഴിവാക്കുക.

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ റൂട്ട് ഡയറക്ടറിയിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ റൂട്ട് ഡയറക്ടറിയിൽ *.env* ഫയൽ സൃഷ്ടിക്കുക.

1. *.env* ഫയൽ തുറന്ന് താഴെ കാണുന്ന ടെംപ്ലേറ്റ് പേസ്റ്റ് ചെയ്യുക:

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
> നിങ്ങളുടെ API കീകളും എൻഡ്പോയിന്റുകളും കണ്ടെത്താൻ, [set-up-azure-ai.md](../set-up-azure-ai.md) കാണുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള മൂല രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->