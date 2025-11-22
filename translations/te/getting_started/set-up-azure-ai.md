<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b58d7c3cb4210697a073d20eb3064945",
  "translation_date": "2025-11-22T05:57:33+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "te"
}
-->
# కో-ఆప్ ట్రాన్స్‌లేటర్ కోసం Azure AI సెటప్ చేయడం (Azure OpenAI & Azure AI Vision)

ఈ గైడ్, Azure AI Foundryలో భాషా అనువాదం కోసం Azure OpenAI మరియు చిత్ర కంటెంట్ విశ్లేషణ (దీని ద్వారా చిత్ర ఆధారిత అనువాదం చేయవచ్చు) కోసం Azure Computer Vision సెటప్ చేయడంలో మీకు సహాయపడుతుంది.

**ముందస్తు అవసరాలు:**
- చురుకైన సబ్‌స్క్రిప్షన్‌తో Azure ఖాతా.
- మీ Azure సబ్‌స్క్రిప్షన్‌లో వనరులు మరియు డిప్లాయ్‌మెంట్లను సృష్టించడానికి తగిన అనుమతులు.

## Azure AI ప్రాజెక్ట్ సృష్టించండి

మీరు Azure AI ప్రాజెక్ట్‌ను సృష్టించడం ప్రారంభిస్తారు, ఇది మీ AI వనరులను నిర్వహించడానికి కేంద్ర ప్రదేశంగా పనిచేస్తుంది.

1. [https://ai.azure.com](https://ai.azure.com)కి వెళ్లి మీ Azure ఖాతాతో సైన్ ఇన్ చేయండి.

1. **+Create** ఎంచుకుని కొత్త ప్రాజెక్ట్‌ను సృష్టించండి.

1. ఈ క్రింది పనులను చేయండి:
   - **Project name** (ఉదా., `CoopTranslator-Project`) నమోదు చేయండి.
   - **AI hub** (ఉదా., `CoopTranslator-Hub`) ఎంచుకోండి (అవసరమైతే కొత్తదాన్ని సృష్టించండి).

1. "**Review and Create**" క్లిక్ చేసి మీ ప్రాజెక్ట్‌ను సెటప్ చేయండి. మీరు మీ ప్రాజెక్ట్ యొక్క అవలోకన పేజీకి తీసుకెళ్లబడతారు.

## భాషా అనువాదం కోసం Azure OpenAI సెటప్ చేయండి

మీ ప్రాజెక్ట్‌లో, మీరు టెక్స్ట్ అనువాదం కోసం బ్యాక్‌ఎండ్‌గా పనిచేసే Azure OpenAI మోడల్‌ను డిప్లాయ్ చేస్తారు.

### మీ ప్రాజెక్ట్‌కు వెళ్లండి

మీరు ఇప్పటికే అక్కడ లేకపోతే, Azure AI Foundryలో మీ కొత్తగా సృష్టించిన ప్రాజెక్ట్ (ఉదా., `CoopTranslator-Project`)ను తెరవండి.

### OpenAI మోడల్‌ను డిప్లాయ్ చేయండి

1. మీ ప్రాజెక్ట్ యొక్క ఎడమ వైపు మెనులో, "My assets" కింద, "**Models + endpoints**" ఎంచుకోండి.

1. **+ Deploy model** ఎంచుకోండి.

1. **Deploy Base Model** ఎంచుకోండి.

1. అందుబాటులో ఉన్న మోడల్స్ జాబితా మీకు చూపబడుతుంది. సరైన GPT మోడల్ కోసం ఫిల్టర్ చేయండి లేదా శోధించండి. మేము `gpt-4o`ని సిఫారసు చేస్తాము.

1. మీకు కావలసిన మోడల్‌ను ఎంచుకుని **Confirm** క్లిక్ చేయండి.

1. **Deploy** ఎంచుకోండి.

### Azure OpenAI కాన్ఫిగరేషన్

ఒకసారి డిప్లాయ్ చేసిన తర్వాత, మీరు "**Models + endpoints**" పేజీ నుండి డిప్లాయ్‌మెంట్‌ను ఎంచుకుని దాని **REST endpoint URL**, **Key**, **Deployment name**, **Model name** మరియు **API version** కనుగొనవచ్చు. ఇవి మీ అనువాద మోడల్‌ను మీ అప్లికేషన్‌లో సమగ్రపరచడానికి అవసరం.

> [!NOTE]
> మీ అవసరాల ఆధారంగా [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) పేజీ నుండి API వెర్షన్‌లను ఎంచుకోవచ్చు. **API version** అనేది Azure AI Foundryలో **Models + endpoints** పేజీలో చూపబడే **Model version** కంటే భిన్నమైనది.

## చిత్ర అనువాదం కోసం Azure Computer Vision సెటప్ చేయండి

చిత్రాలలోని టెక్స్ట్‌ను అనువదించడానికి, మీరు Azure AI Service API Key మరియు Endpoint కనుగొనాలి.

1. మీ Azure AI ప్రాజెక్ట్ (ఉదా., `CoopTranslator-Project`)కి వెళ్లండి. మీరు ప్రాజెక్ట్ అవలోకన పేజీలో ఉన్నారని నిర్ధారించుకోండి.

### Azure AI Service కాన్ఫిగరేషన్

Azure AI Service నుండి API Key మరియు Endpoint కనుగొనండి.

1. మీ Azure AI ప్రాజెక్ట్ (ఉదా., `CoopTranslator-Project`)కి వెళ్లండి. మీరు ప్రాజెక్ట్ అవలోకన పేజీలో ఉన్నారని నిర్ధారించుకోండి.

1. Azure AI Service ట్యాబ్ నుండి **API Key** మరియు **Endpoint** కనుగొనండి.

    ![API Key మరియు Endpoint కనుగొనండి](../../../getting_started/imgs/find-azure-ai-info.png)

ఈ కనెక్షన్, లింక్ చేయబడిన Azure AI Services వనరుల సామర్థ్యాలను (చిత్ర విశ్లేషణ సహా) మీ AI Foundry ప్రాజెక్ట్‌కు అందుబాటులోకి తీసుకువస్తుంది. మీరు ఈ కనెక్షన్‌ను మీ నోట్‌బుక్స్ లేదా అప్లికేషన్లలో ఉపయోగించి చిత్రాల నుండి టెక్స్ట్‌ను తీసి, దానిని Azure OpenAI మోడల్‌కు అనువాదం కోసం పంపవచ్చు.

## మీ క్రెడెన్షియల్స్‌ను సమీకరించడం

ఇప్పటికి, మీరు ఈ క్రింది వివరాలను సేకరించి ఉండాలి:

**Azure OpenAI (టెక్స్ట్ అనువాదం కోసం):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ఉదా., `gpt-4o`)
- Azure OpenAI Deployment Name (ఉదా., `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (చిత్ర టెక్స్ట్ ఎక్స్ట్రాక్షన్ కోసం Vision ద్వారా):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ఉదాహరణ: ఎన్విరాన్‌మెంట్ వేరియబుల్ కాన్ఫిగరేషన్ (ప్రివ్యూ)

తరువాత, మీ అప్లికేషన్‌ను నిర్మించేటప్పుడు, మీరు ఈ సేకరించిన క్రెడెన్షియల్స్‌ను ఉపయోగించి దానిని కాన్ఫిగర్ చేస్తారు. ఉదాహరణకు, మీరు వాటిని ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌గా ఈ విధంగా సెట్ చేయవచ్చు:

```bash
# ఆజూర్ AI సేవ క్రెడెన్షియల్స్ (చిత్ర అనువాదానికి అవసరం)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ఉదా., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ఆజూర్ OpenAI క్రెడెన్షియల్స్ (పాఠ్య అనువాదానికి అవసరం)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ఉదా., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ఉదా., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ఉదా., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ఉదా., 2024-12-01-preview
```

---

### మరింత చదవండి

- [Azure AI Foundryలో ప్రాజెక్ట్‌ను ఎలా సృష్టించాలి](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI వనరులను ఎలా సృష్టించాలి](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundryలో OpenAI మోడల్స్‌ను ఎలా డిప్లాయ్ చేయాలి](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->