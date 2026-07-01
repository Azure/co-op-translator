# Azure AI సెటప్

టෙක්스트్ అనువాదానికి Azure OpenAI మరియు ఇమేజ్ టెక్స్ట్ ఎక్స్‌ట్రాక్షన్ కోసం Azure AI Vision‌ను కాన్ఫిగర్ చేయాలనుకునేటప్పుడు ఈ గైడ్‌ను ఉపయోగించండి.

## ముందస్తు అవసరాలు

- ఒక Azure సబ్‌స్క్రిప్షన్.
- Azure AI వనరులు మరియు మోడల్ డిప్లాయ్మెంట్లను సృష్టించటానికి లేదా ఉపయోగించటానికి అనుమతి.
- Azure AI Foundryలో ఒక ప్రాజెక్టు లేదా Azure OpenAI మరియు Azure AI Vision వనరులకు సమానమైన యాక్సెస్.

## Azure AI ప్రాజెక్టును సృష్టించండి

1. [Azure AI Foundry](https://ai.azure.com) ను తెరవండి.
2. ఒక ప్రాజెక్టును సృష్టించండి లేదా ఎన్నుకోండి.
3. ప్రాజెక్టుకు ఒక AI హబ్‌ను సృష్టించండి లేదా ఎన్నుకోండి.
4. సృష్టించిన తర్వాత ప్రాజెక్ట్ అవలోకనాన్ని తెరవండి.

## Azure OpenAI మోడల్‌ను అమర్చండి

1. ప్రాజెక్టులో, **మోడల్స్ + ఎండ్‌పాయింట్లు** ను తెరవండి.
2. **మోడల్‌ను అమర్చండి**ని ఎంచుకోండి.
3. `gpt-4o` వంటి GPT మోడల్‌ను ఎంచుకోండి.
4. మోడల్‌ను అమర్చండి.
5. ఎండ్పాయింట్, డిప్లాయ్‌మెంట్ పేరు, మోడల్ పేరు, API కీ మరియు API వెర్షన్‌ను నమోదు చేసుకోండి.

!!! note
    Azure OpenAI API వెర్షన్ Azure AI Foundryలో చూపబడుతున్న మోడల్ వెర్షన్ నుండి వేరైనది. మీ డిప్లాయ్‌మెంట్‌కు మద్దతు ఉన్న API వెర్షన్‌ని ఎంచుకోండి.

## Azure AI Vision‌ని కాన్ఫిగర్ చేయండి

ఇమేజ్ అనువాదం కోసం, టెక్స్ట్ అనువదించబడటానికి ముందు మూల చిత్రాల నుంచి టెక్స్ట్‌ను తీయడానికి Azure AI Vision ఉపయోగిస్తారు.

మీ Azure AI ప్రాజెక్టులో, Azure AI సేవల కీ మరియు ఎండ్‌పాయింట్‌ను కనుగొనండి.

![Azure AI సేవ సమాచారం కనుగొనండి](../../assets/find-azure-ai-info.png)

గమనించండి:

- Azure AI సేవ ఎండ్‌పాయింట్
- Azure AI సేవ API కీ

## పర్యావరణ వేరియబుల్స్

మీ క్రెడెన్షియల్స్‌ను మీ `.env` ఫైల్ లేదా CI సీక్రెట్స్‌లో జత చేయండి.

```bash
# చిత్రం అనువాదం కోసం అవసరమైన Azure AI Vision
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# పాఠ్య అనువాదం కోసం అవసరమైన Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator కూడా ఐచ్ఛిక fallback క్రెడెన్షియల్ సెట్‌లను మద్దతు ఇస్తుంది. `_1` లేదా `_2` వంటి సఫిక్స్‌లతో పూర్తి ప్రొవైడర్ సెట్‌ను నకలు చేయండి; fallback సెట్‌లోని అన్ని వేరియబుల్స్ ఒకే సఫిక్స్‌ను పంచుకోవాలి.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## తదుపరి దశలు

- [కాన్ఫిగరేషన్](configuration.md)కు తిరిగి వెళ్లి స్థానిక లేదా CI పర్యావరణ వేరియబుల్స్‌ను సెటప్ చేయండి.
- అనువాద ఆదేశాల కోసం [CLI రిఫరెన్స్](cli.md)ను ఉపయోగించండి.
- అనువాద పుల్ రిక్వెస్టులను ఆటోమేట్ చేయడానికి [GitHub Actions](github-actions.md) ను ఉపయోగించండి.