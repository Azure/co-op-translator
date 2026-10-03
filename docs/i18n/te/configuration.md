# కాన్ఫిగరేషన్

Co-op Translatorకి ఒక భాషా మోడల్ ప్రొవైడర్ అవసరం. చిత్ర అనువాదానికి అదనంగా Azure AI Vision అవసరం.

కాన్ఫిగరేషన్‌ను ఎన్విరాన్‌మెంట్ వేరియబుల్స్ నుంచి చదివి తీసుకుంటుంది. స్థానిక ప్రాజెక్టుల కోసం, వాటిని ప్రాజెక్ట్ రూట్‌లోని `.env` ఫైల్‌లో ఉంచండి.

Azure వనరులు సెటప్ కోసం, చూడండి [Azure AI సెటప్](azure-ai-setup.md).

## లోకల్ రన్‌టైమ్ సెటప్

CLI ను స్థానికంగా నడిపించే ముందు వర్చువల్ ఎన్విరాన్‌మెంట్‌ను ఉపయోగించండి. Co-op Translator Python 3.11 నుండి 3.14 వరకు మద్దతు ఇస్తుంది.

సాధారణ CLI ఉపయోగానికి, పబ్లిష్ చేసిన ప్యాకేజీని వర్చువల్ ఎన్విరాన్‌మెంట్ లో ఇన్‌స్టాల్ చేయండి:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### రిపోజిటరీ అభివృద్ధి

రిపోజిటరీ అభివృద్ధికి, బదులుగా ప్రాజెక్ట్ రూట్ నుండే డిపెండెన్సీలు ఇన్‌స్టాల్ చేయండి:

```bash
poetry install
poetry run translate --help
```

CLI అందుబాటులోకి వచ్చిన తర్వాత, `.env` లో ఒక భాషా మోడల్ ప్రొవైడర్‌ని కాన్ఫిగర్ చేయండి.

## ప్రొవైడర్ ఎంపిక

టూల్ ఈ క్రమంలో ప్రొవైడర్లను ఆటో-డిటెక్ట్ చేస్తుంది:

1. Azure OpenAI
2. OpenAI
3. Anthropic

అనువాదానికి ప్రొవైడర్ క్రెడెన్షియల్స్ అవసరం, కానీ `translate -l "ko" -md --dry-run` వంటి ప్రివ్యూలకు తప్పు. `migrate-links`, `co-op-review`, మరియు `run_review` నిర్ణీతమైన నిర్వహణ చర్యలు మరియు ప్రొవైడర్ క్రెడెన్షియల్స్ అవసరం ఉండవు.

## మోడల్ క్లయింట్ బ్యాక్‌ఎండ్

Co-op Translator 0.22.0 నుండి, Azure OpenAI, OpenAI మరియు Anthropic డిఫాల్ట్‌గా Microsoft Agent Framework ను ఉపయోగిస్తాయి. సాధారణ ఉపయోగానికి బ్యాక్‌ఎండ్ సెట్టింగ్ అవసరం లేదు.

Semantic Kernel అనుకూలత కోసం తాత్కాలికంగా అందుబాటులో ఉంటుంది. దీన్ని స్పష్టంగా ఎన్నుకోవాలంటే, సెట్ చేయండి:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel ను ఉపయోగిస్తే డిప్రికేషన్ హెచ్చరిక ఉత్పన్నమవుతుంది. ప్యాకేజ్ లో Semantic Kernel ను 0.23.0 లో ఐచ్ఛిక డిపెండెన్సీగా మార్చడానికి ప్లాన్ ఉంది మరియు 0.24.0 లో ఇంటిగ్రేషన్ తీసివేయడానికి ఉద్దేశంగా ఉంది, ఇది అనుకూలత ఫలితాలు మరియు వినియోగదారుల అభిప్రాయాలపై ఆధారపడి ఉంటుంది. Anthropic కు `agent-framework` అవసరం; Anthropic తో `semantic-kernel` ను ఖచ్చితంగా ఎంపిక చేయడం కాన్ఫిగరేషన్ లో లోపంతో విఫలమవుతుంది. తప్పు విలువలు సైలెంట్‌గా fallback లేకుండా provider-backed translator ప్రారంభించేటప్పుడు విఫలమవుతాయి. విడుదలను అనుసరించండి మరియు అడ్డంకులను నివేదించండి [GitHub ఇష్యూ #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

మీ మోడెల్ Azure AI Foundry లేదా Azure OpenAI Service లో డిప్లాయ్ చేయబడినప్పుడు Azure OpenAI ను ఉపయోగించండి.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

కనెక్టివిటీ తనిఖీ అనువాదం ప్రారంభించే ముందు endpoint, API key, API version మరియు deployment name ను ఉపయోగిస్తుంది.

## OpenAI

OpenAI API ను నేరుగా పిలవుతున్నప్పుడు OpenAI ను ఉపయోగించండి.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` అవసరం, ఎందుకంటే అనువాదకానికి API కాల్స్ కోసం స్పష్టమైన చాట్ మోడల్ అవసరం.

`OPENAI_ORG_ID` మరియు `OPENAI_BASE_URL` ను డిఫాల్ట్ సెటప్ కోసం unset గా ఉంచండి. మీ ఖాతాకు ఒక organization ID అవసరమైతే మాత్రమే అది జోడించండి, లేదా కస్టమ్ endpoint ఉపయోగిస్తున్నప్పుడు మాత్రమే base URL జోడించండి. ఐచ్ఛిక సెట్టింగ్స్ కోసం ప్లేస్‌హోల్డర్ విలువలను కాపీ చేయకండి.

## Anthropic Claude

Claude API ను నేరుగా పిలవుతున్నప్పుడు Anthropic ను ఉపయోగించండి. ఒక [Anthropic API కీ](https://platform.claude.com/docs/en/get-started) సృష్టించండి మరియు మద్దతు ఇచ్చే ఒక [Claude మోడల్ ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) ఎంచుకోండి.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` మరియు `ANTHROPIC_MODEL` అవసరం. `CO_OP_TRANSLATOR_MODEL_CLIENT` ను సెట్ చేయాల్సిన అవసరం లేదు; Agent Framework డిఫాల్ట్ బ్యాక్‌ఎండ్.

Anthropic API కోసం `ANTHROPIC_BASE_URL` ను unset గా ఉంచండి. కస్టమ్ endpoint ఉపయోగిస్తున్నప్పుడు మాత్రమే దీన్ని సెట్ చేయండి.

`ANTHROPIC_MAX_TOKENS` పూర్వనిర్ణీతంగా `8192` కు సెట్ ఉంటుంది, ఇది Meitei Mayek వంటి టోకెన్-సాంద్రత ఉన్న స్క్రిప్ట్‌లకు స్థలం ఉంచుతుంది. మీ మోడల్ లేదా Anthropic-అనుకూల endpoint అవుట్పుట్‌ను ఆ పరిమితికి కింద పెట్టినప్పుడు దీన్ని తగ్గించండి.

## Azure AI Vision

చిత్ర అనువాదానికి Azure AI Vision అవసరం, తద్వారా టూల్ చిత్రాల నుంచి టెక్స్ట్‌ను తీసి, కాన్ఫిగర్ చేయబడిన భాషా మోడల్ అనువదించే ముందు అది చేయగలదు. Anthropic కూడా తీసిన టెక్ట్స్‌ను Azure OpenAI లేదా OpenAI లాగానే అనువదించగలదు.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True`, లేదా content-type ఫిల్టర్ లేకపోతే చిత్ర అనువాదం ఎంచుకుంటే, టూల్ అనువాదం ప్రారంభం కాకముందే Vision కాన్ఫిగరేషన్‌ని నిర్ధారిస్తుంది.

## బహుళ క్రెడెన్షియల్ సెట్లు

కాన్ఫిగరేషన్ లేయర్ ఒకే సూచికతో వేరియబుల్స్‌కు సఫిక్స్ ఇవ్వడం ద్వారా బహుళ క్రెడెన్షియల్ సెట్లకు మద్దతు ఇస్తుంది:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

ప్రతి సెట్ పూర్తిగా ఉండాలి. అనువాదం ప్రారంభం కాకముందు హెల్త్ చెక్ పనిచేస్తున్న సెట్‌ను ఎంచుకుంటుంది.

OpenAI మరియు Anthropic అదే సఫిక్స్ కాన్వెన్షన్‌ను మద్దతు ఇస్తాయి. ప్రతి క్రెడెన్షియల్ సెట్‌లోని ప్రతి వేరియబిల్ అదే సఫిక్స్‌లో ఉంచండి, `OPENAI_BASE_URL_1` లేదా `ANTHROPIC_BASE_URL_1` వంటి ఐచ్ఛిక విలువలను కూడా.

## కమాండ్ అవసరాలు

| కమాండ్ లేదా API | LLM అవసరమా | Vision అవసరమా | గమనికలు |
| --- | --- | --- | --- |
| `translate -md` | అవును | లేదు | Markdown మాత్రమే అనువదిస్తుంది. |
| `translate -nb` | అవును | లేదు | నోట్బుక్స్ మాత్రమే అనువదిస్తుంది. |
| `translate -img` | అవును | అవును | చిత్రాలు మాత్రమే అనువదిస్తుంది. |
| `translate` with no type flags | అవును | అవును | డిఫాల్ట్ మోడ్‌లో Markdown, నోట్బుక్స్ మరియు చిత్రాలు ఉంటాయి. |
| `evaluate` | అవును | లేదు | `--fast` ఎంచుకోకపోతే LLM మూల్యాంకనం ఉపయోగిస్తుంది. |
| `migrate-links` | లేదు | లేదు | ప్రొవైడర్ కాల్స్ లేకుండా స్థానిక లింక్ మైగ్రేషన్‌ను నిర్వహిస్తుంది. |
| `co-op-review` | లేదు | లేదు | నిర్ధారిత అనువాద నిర్మాణం, తాజాదన, Markdown, నోట్బుక్ మరియు స్థానిక లింక్ తనిఖీలను నడుపుతుంది. |
| `run_translation(markdown=True)` | అవును | లేదు | ప్రోగ్రామాటిక్ Markdown అనువాదం. |
| `run_translation(images=True)` | అవును | అవును | ప్రోగ్రామాటిక్ చిత్రం అనువాదం. |
| `run_review(...)` | లేదు | లేదు | ప్రోగ్రామాటిక్ నిర్ణీత సమీక్ష. |

## అవుట్‌పుట్ డైరెక్టరీలు

డిఫాల్ట్ టెక్స్ట్ అనువాద అవుట్‌పుట్:

```text
translations/<language-code>/<source-relative-path>
```

డిఫాల్ట్ అనువదించిన చిత్రం అవుట్‌పుట్:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ఈ డైరెక్టరీలను `translations_dir` మరియు `image_dir` తో ఓవర్‌రైడ్ చేయగలదు.