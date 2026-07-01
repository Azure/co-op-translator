# కన్ఫిగరేషన్

Co-op Translator కి ఒక భాషా మోడల్ ప్రొవైడర్ అవసరం. చిత్ర అనువాదానికి అదనంగా Azure AI Vision అవసరం.

కన్ఫిగరేషన్‌ను పరిసర వేరియబుల్స్ నుండి చదివుతుంది. స్థానిక ప్రాజెక్టుల కోసం, అవి ప్రాజెక్ట్ రూట్‌లో `.env` ఫైల్‌లో ఉంచండి.

Azure వనరుల సెటప్ కోసం చూడండి [Azure AI సెటప్](azure-ai-setup.md).

## స్థానిక రన్‌టైమ్ సెటప్

స్థానికంగా CLI ను 실행 చేసే ముందు వర్చువల్ ఎన్విరాన్‌మెంట్ ఉపయోగించండి. Co-op Translator Python 3.10 నుంచి 3.12 వరకు మద్దతు ఇస్తుంది.

సాధారణ CLI వాడుక కోసం, ప్రచురిత ప్యాకేజీని వర్చువల్ ఎన్విరాన్‌మెంట్ లో ఇన్‌స్టాల్ చేయండి:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

For repository development, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

CLI లభ్యమైతే, `.env` లో ఒక భాషా మోడల్ ప్రొవైడర్‌ను కాన్ఫిగర్ చేయండి.

## ప్రొవైడర్ ఎంపిక

టూల్ ఈ క్రమంలో ప్రొవైడర్లను ఆటో-డిటెక్ట్ చేస్తుంది:

1. Azure OpenAI
2. OpenAI

ఈ రెండింటిలో ఏ ప్రొవైడర్ కాన్ఫిగర్ చేయబడకపోతే, `translate`, `evaluate`, `migrate-links`, మరియు `run_translation` కాన్ఫిగరేషన్ తనిఖీల సమయంలో విఫలమవుతాయి. `co-op-review` మరియు `run_review` డిటర్మినిస్టిక్ నిర్వహణ తనిఖీలు కావడంతో ప్రొవైడర్ క్రెడెంసియల్స్ అవసరం ఉండదు.

## Azure OpenAI

మీ మోడల్ Azure AI Foundry లేదా Azure OpenAI Serviceలో డిప్లాయ్ చేయబడినపుడు Azure OpenAI ఉపయోగించండి.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

కనెక్టివిటీ తనిఖీ ట్రాన్స్లేషన్ ప్రారంభం కాకముందు endpoint, API key, API version మరియు deployment name ను పరీక్షిస్తుంది.

## OpenAI

OpenAI API ను నేరుగా పిలిచే సమయంలో OpenAI ఉపయోగించండి.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ఐచ్ఛిక
OPENAI_BASE_URL="..."        # ఐచ్ఛిక
```

`OPENAI_CHAT_MODEL_ID` అవసరం, ఎందుకంటే ట్రాన్స్‌లేటర్‌కు API కాల్స్ కోసం స్పష్టమైన చాట్ మోడల్ అవసరం.

## Azure AI Vision

చిత్ర అనువాదానికి Azure AI Vision అవసరం, ఎందుకంటే టూల్ అనువాదానికి ముందు చిత్రాల నుండి టెక్స్ట్‌ను ఎక్స్‌ట్రాక్ట్ చేయాలి.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

చిత్ర అనువాదం `-img`, `images=True` లేదా content-type ఫిల్టర్ లేనప్పుడు ఎంచుకోబడినట్లయితే, టూల్ అనువాదం మొదలయ్యే ముందు Vision కాన్ఫిగరేషన్‌ను ధృవీకরుస్తుంది.

## బహుళ క్రెడెన్షియల్ సెట్లు

కన్ఫిగరేషన్ లేయర్ ఒకే ఇండెక్స్‌తో వేరియబుల్స్‌కు సఫిక్స్ పెట్టి బహుళ క్రెడెన్షియల్ సెట్లను మద్దతు చేస్తుంది:

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

ప్రతి సెటు పూర్తి ఉండాలి. హెల్త్ చెక్ అనువాదం కొనసాగిపోవడానికి ముందు పనిచేసే సెట్ను ఎంపిక చేస్తుంది.

## ఆదేశాల అవసరాలు

| ఆదేశం లేదా API | LLM అవసరమా | Vision అవసరమా | గమనికలు |
| --- | --- | --- | --- |
| `translate -md` | అవును | కాదు | Markdown మాత్రమే అనువదిస్తుంది. |
| `translate -nb` | అవును | కాదు | నోట్బుక్స్ మాత్రమే అనువదిస్తుంది. |
| `translate -img` | అవును | అవును | చిత్రాలు మాత్రమే అనువదిస్తుంది. |
| `translate` with no type flags | అవును | అవును | డిఫాల్ట్ మోడ్‌లో Markdown, నోట్బుక్స్, మరియు చిత్రాలు ఉంటాయి. |
| `evaluate` | అవును | కాదు | `--fast` సెలెక్ట్ కాకపోతే LLM మూల్యాంకనాన్ని ఉపయోగిస్తుంది. |
| `migrate-links` | అవును | కాదు | లింక్ మైగ్రేషన్‌ను అమలు చేస్తుంది, కానీ ఇంకా పంచుకున్న కాన్ఫిగరేషన్ తనిఖీలు నడిపిస్తుంది. |
| `co-op-review` | కాదు | లేదు | డిటర్మినిస్టిక్ అనువాద నిర్మాణం, తాజత్వం, Markdown, నోట్బుక్, మరియు లోకల్ లింక్ తనిఖీలు నడిపిస్తుంది. |
| `run_translation(markdown=True)` | అవును | కాదు | ప్రోగ్రామాటిక్ Markdown అనువాదం. |
| `run_translation(images=True)` | అవును | అవును | ప్రోగ్రామాటిక్ చిత్ర అనువాదం. |
| `run_review(...)` | కాదు | కాదు | ప్రోగ్రామాటిక్ డిటర్మినిస్టిక్ సమీక్ష. |

## అవుట్‌పుట్ డైరెక్టరీలు

డిఫాల్ట్ టెక్స్ట్ అనువాద అవుట్‌పుట్:

```text
translations/<language-code>/<source-relative-path>
```

డిఫాల్ట్ అనువదించిన చిత్ర అవుట్‌పుట్:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API ఈ డైరెక్టరీలను `translations_dir` మరియు `image_dir`తో ఓవర్‌రైడ్ చేయవచ్చు.