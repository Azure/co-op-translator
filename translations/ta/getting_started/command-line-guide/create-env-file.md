<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-10-15T04:59:30+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ta"
}
-->
# உங்கள் மூல அடைவில் *.env* கோப்பை உருவாக்குங்கள்

இந்த பயிற்சியில், Azure சேவைகளுக்கான உங்கள் சூழல் மாறிகளை *.env* கோப்பைப் பயன்படுத்தி அமைப்பது எப்படி என்பதை வழிகாட்டுகிறோம். சூழல் மாறிகள் மூலம், API விசைகள் போன்ற முக்கியமான தகவல்களை உங்கள் குறியீட்டில் நேரடியாக எழுதாமல் பாதுகாப்பாக நிர்வகிக்க முடியும்.

> [!IMPORTANT]
> - ஒரே ஒரு மொழி மாதிரி சேவையை (Azure OpenAI அல்லது OpenAI) மட்டுமே அமைக்க வேண்டும். உங்களுக்கு விருப்பமான சேவைக்கான சூழல் மாறிகளை நிரப்புங்கள். பல மொழி மாதிரிகளுக்கான சூழல் மாறிகள் அமைக்கப்பட்டிருந்தால், co-op translator முன்னுரிமை அடிப்படையில் ஒன்றை தேர்வு செய்யும்.
> - Computer Vision சூழல் மாறிகள் அமைக்கப்படவில்லை என்றால், translator தானாகவே [Markdown-only mode](./markdown-only-mode.md)க்கு மாறும்.

> [!NOTE]
> இந்த வழிகாட்டி Azure சேவைகளில் அதிக கவனம் செலுத்துகிறது, ஆனால் நீங்கள் விரும்பும் எந்த ஆதரவு language model-ஐயும் [supported models and services list](../README.md#-supported-models-and-services)இல் இருந்து தேர்வு செய்யலாம்.

## *.env* கோப்பை உருவாக்குங்கள்

உங்கள் திட்டத்தின் மூல அடைவில் *.env* என்ற பெயரில் ஒரு கோப்பை உருவாக்குங்கள். இந்த கோப்பில் உங்கள் சூழல் மாறிகள் எளிய வடிவில் சேமிக்கப்படும்.

> [!WARNING]
> உங்கள் *.env* கோப்பை Git போன்ற version control systems-க்கு commit செய்ய வேண்டாம். *.env*ஐ .gitignore கோப்பில் சேர்த்து தவறுதலாக commit ஆகாமல் பாதுகாக்கவும்.

1. உங்கள் திட்டத்தின் மூல அடைவிற்கு செல்லுங்கள்.

1. அந்த அடைவில் *.env* கோப்பை உருவாக்குங்கள்.

1. *.env* கோப்பை திறந்து, கீழே உள்ள வார்ப்புருவை ஒட்டுங்கள்:

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
> உங்கள் API விசைகள் மற்றும் endpoint-ஐ கண்டுபிடிக்க விரும்பினால், [set-up-azure-ai.md](../set-up-azure-ai.md)ஐ பார்க்கலாம்.

---

**பொறுப்புத் தவிர்ப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்தாலும், தானாக மொழிபெயர்க்கப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை தயவுசெய்து கவனிக்கவும். மூல ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல் அல்லது தவறான விளக்கத்திற்கு நாங்கள் பொறுப்பல்ல.