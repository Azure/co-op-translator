<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-11-22T05:59:29+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "te"
}
-->
# రూట్ డైరెక్టరీలో *.env* ఫైల్‌ను సృష్టించండి

ఈ ట్యుటోరియల్‌లో, మీ Azure సేవల కోసం మీ ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను సెటప్ చేయడం గురించి మేము మీకు మార్గనిర్దేశం చేస్తాము, *.env* ఫైల్‌ను ఉపయోగించి. ఎన్విరాన్‌మెంట్ వేరియబుల్స్ API కీలు వంటి సున్నితమైన క్రెడెన్షియల్స్‌ను మీ కోడ్‌బేస్‌లో హార్డ్-కోడ్ చేయకుండా సురక్షితంగా నిర్వహించడానికి అనుమతిస్తాయి.

> [!IMPORTANT]
> - ఒకే ఒక భాషా మోడల్ సేవ (Azure OpenAI లేదా OpenAI) మాత్రమే కాన్ఫిగర్ చేయాలి. మీకు ఇష్టమైన సేవ కోసం ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను పూరించండి. ఒకటి కంటే ఎక్కువ భాషా మోడల్స్ కోసం ఎన్విరాన్‌మెంట్ వేరియబుల్స్ సెట్ చేయబడితే, కో-ఆప్ ట్రాన్స్‌లేటర్ ప్రాధాన్యత ఆధారంగా ఒకదాన్ని ఎంచుకుంటుంది.
> - కంప్యూటర్ విజన్ ఎన్విరాన్‌మెంట్ వేరియబుల్స్ సెట్ చేయబడని పక్షంలో, ట్రాన్స్‌లేటర్ ఆటోమేటిక్‌గా [Markdown-only mode](./markdown-only-mode.md)కి మారుతుంది.

> [!NOTE]
> ఈ గైడ్ ప్రధానంగా Azure సేవలపై దృష్టి సారిస్తుంది, కానీ మీరు [supported models and services list](../README.md#-supported-models-and-services) నుండి ఏదైనా మద్దతు ఉన్న భాషా మోడల్‌ను ఎంచుకోవచ్చు.

## *.env* ఫైల్‌ను సృష్టించండి

మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీలో, *.env* అనే ఫైల్‌ను సృష్టించండి. ఈ ఫైల్ మీ ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను సులభమైన ఫార్మాట్‌లో నిల్వ చేస్తుంది.

> [!WARNING]
> మీ *.env* ఫైల్‌ను Git వంటి వెర్షన్ కంట్రోల్ సిస్టమ్స్‌కు కమిట్ చేయవద్దు. అనుకోకుండా కమిట్స్‌ను నివారించడానికి *.env* ను మీ .gitignore ఫైల్‌లో చేర్చండి.

1. మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీకి వెళ్లండి.

1. మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీలో *.env* ఫైల్‌ను సృష్టించండి.

1. *.env* ఫైల్‌ను ఓపెన్ చేసి, ఈ టెంప్లేట్‌ను పేస్ట్ చేయండి:

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
> మీ API కీలు మరియు ఎండ్‌పాయింట్స్‌ను కనుగొనాలనుకుంటే, [set-up-azure-ai.md](../set-up-azure-ai.md) ను చూడవచ్చు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వస్థల భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదం సిఫారసు చేయబడుతుంది. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->