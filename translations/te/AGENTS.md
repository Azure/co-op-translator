<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-11-22T05:53:45+00:00",
  "source_file": "AGENTS.md",
  "language_code": "te"
}
-->
# AGENTS.md

## ప్రాజెక్ట్ అవలోకనం

Co‑op Translator అనేది పైథాన్ కమాండ్‑లైన్ టూల్ మరియు GitHub Actions వర్క్‌ఫ్లో, ఇది Markdown ఫైళ్లను, Jupyter నోట్‌బుక్‌లను మరియు చిత్రాల టెక్స్ట్‌ను అనేక భాషలలోకి అనువదిస్తుంది. ఇది అవుట్‌పుట్‌లను భాష-స్పెసిఫిక్ ఫోల్డర్‌లలో ఆర్గనైజ్ చేస్తుంది మరియు మూల కంటెంట్‌తో అనువాదాలను సమకాలీకరంగా ఉంచుతుంది. ఈ ప్రాజెక్ట్‌ను Poetry‑తో నిర్వహించే లైబ్రరీగా నిర్మించారు, CLI ఎంట్రీ పాయింట్‌లతో.

### ఆర్కిటెక్చర్ అవలోకనం

- CLI ఎంట్రీ పాయింట్‌లు (`translate`, `migrate-links`, `evaluate`) ఒక ఏకీకృత CLIని ఆహ్వానిస్తాయి, ఇది అనువాదం, లింక్ మైగ్రేషన్ మరియు మూల్యాంకన ఫ్లోలకు పంపుతుంది.
- కాన్ఫిగరేషన్ లోడర్ `.env`ని చదివి, LLM ప్రొవైడర్ (Azure OpenAI లేదా OpenAI) మరియు అవసరమైతే, విజన్ ప్రొవైడర్ (Azure AI Service)ని చిత్ర టెక్స్ట్ ఎక్స్ట్రాక్షన్ కోసం ఆటో‑డిటెక్ట్ చేస్తుంది.
- అనువాదం కోర్ Markdown మరియు నోట్‌బుక్‌లను నిర్వహిస్తుంది; విజన్ పైప్‌లైన్ `-img` ఉపయోగించినప్పుడు చిత్రాల నుండి టెక్స్ట్‌ను ఎక్స్ట్రాక్ట్ చేస్తుంది.
- అవుట్‌పుట్‌లు `translations/<lang>/` లో టెక్స్ట్ కోసం మరియు `translated_images/` లో చిత్రాల కోసం ఆర్గనైజ్ చేయబడతాయి, అసలు నిర్మాణాన్ని కాపాడుతూ.

### ముఖ్యమైన టెక్నాలజీలు మరియు ఫ్రేమ్‌వర్క్‌లు

- Python 3.10–3.12, Poetry ప్యాకేజింగ్ కోసం
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- విజన్: Azure AI Service (Computer Vision)
- HTTP మరియు డేటా: `httpx`, `pydantic`
- ఇమేజింగ్: `pillow`, `opencv-python`, `matplotlib`
- టూలింగ్: `pytest`, `black`, `ruff`

## సెటప్ కమాండ్లు

### అవసరమైనవి

- Python 3.10–3.12
- Azure సబ్‌స్క్రిప్షన్ (ఐచ్ఛికం, Azure AI సేవల కోసం)
- LLM/Vision APIs (ఉదా., Azure OpenAI/OpenAI, Azure AI Vision) కోసం ఇంటర్నెట్ యాక్సెస్

### ఆప్షన్ A: Poetry (సిఫార్సు చేయబడింది)

```bash
# రిపోజిటరీ రూట్ నుండి
pip install poetry
poetry install

# పోయెట్రీ ద్వారా ఏదైనా ఆదేశాన్ని అమలు చేయండి
poetry run translate --help
```

### ఆప్షన్ B: pip/venv

```bash
# వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి & యాక్టివేట్ చేయండి
python -m venv .venv
# విండోస్
.venv\\Scripts\\activate
# లినక్స్/మాక్‌ఓఎస్
# source .venv/bin/activate

# డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి
pip install -r requirements.txt

# (ఐచ్ఛికం) స్థానిక అభివృద్ధి కోసం ఎడిటబుల్ ఇన్‌స్టాల్
pip install -e .
```

## ఎండ్ యూజర్ వినియోగం

### Docker (ప్రచురించిన ఇమేజ్)

```bash
# GHCR నుండి పబ్లిక్ ఇమేజ్‌ను తీసుకోండి
docker pull ghcr.io/azure/co-op-translator:latest

# ప్రస్తుత ఫోల్డర్ మౌంట్ చేయబడిన మరియు .env అందించబడిన (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# పవర్‌షెల్
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

గమనికలు:
- డిఫాల్ట్ ఎంట్రీపాయింట్ `translate`. లింక్ మైగ్రేషన్ కోసం `--entrypoint migrate-links` తో ఓవర్‌రైడ్ చేయండి.
- అనామిక పుల్‌ల కోసం GHCR ప్యాకేజీ విజిబిలిటీ పబ్లిక్‌గా ఉండేలా చూసుకోండి.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### ఎన్విరాన్‌మెంట్ కాన్ఫిగరేషన్

రిపోజిటరీ రూట్‌లో `.env` ఫైల్‌ను సృష్టించి, మీ ఎంపిక చేసిన భాషా మోడల్ మరియు (ఐచ్ఛికంగా) విజన్ సేవ కోసం క్రెడెన్షియల్స్/ఎండ్‌పాయింట్‌లను అందించండి. ప్రొవైడర్‑స్పెసిఫిక్ సెటప్ కోసం, `getting_started/set-up-azure-ai.md` చూడండి.

### అవసరమైన ఎన్విరాన్‌మెంట్ వేరియబుల్స్

కనీసం ఒక LLM ప్రొవైడర్ కాన్ఫిగర్ చేయాలి. చిత్ర అనువాదం కోసం, Azure AI Service కూడా కాన్ఫిగర్ చేయాలి.

- Azure OpenAI (టెక్స్ట్ అనువాదం):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (టెక్స్ట్ అనువాదం ప్రత్యామ్నాయం):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ఐచ్ఛికం)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI ప్రొవైడర్ ఉపయోగించినప్పుడు అవసరం)
  - `OPENAI_BASE_URL` (ఐచ్ఛికం; డిఫాల్ట్‌గా `https://api.openai.com/v1`)

- Azure AI Service చిత్ర టెక్స్ట్ ఎక్స్ట్రాక్షన్ కోసం (`-img` ఉపయోగించినప్పుడు అవసరం):
  - `AZURE_AI_SERVICE_API_KEY` (ప్రాధాన్యత) లేదా లెగసీ `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

ఉదాహరణ `.env` స్నిపెట్:

```bash
# ఆజూర్ AI సేవ (చిత్ర అనువాదం కోసం)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# ఆజూర్ ఓపెన్AI (ప్రధాన ఎంపిక)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ఓపెన్AI (ప్రత్యామ్నాయ ఎంపిక)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # ఐచ్ఛికం
OPENAI_CHAT_MODEL_ID="gpt-4o"   # ఓపెన్AI ఉపయోగిస్తున్నప్పుడు అవసరం
OPENAI_BASE_URL="https://api.openai.com/v1" # ఐచ్ఛికం
```

గమనికలు:

- టూల్ అందుబాటులో ఉన్న LLM ప్రొవైడర్‌ను ఆటో‑డిటెక్ట్ చేస్తుంది; Azure OpenAI లేదా OpenAIని కాన్ఫిగర్ చేయండి.
- చిత్ర అనువాదం కోసం `AZURE_AI_SERVICE_API_KEY` మరియు `AZURE_AI_SERVICE_ENDPOINT` రెండూ అవసరం.
- అవసరమైన వేరియబుల్స్ లేకపోతే CLI స్పష్టమైన ఎర్రర్‌ను చూపుతుంది.

## డెవలప్‌మెంట్ వర్క్‌ఫ్లో

- సోర్స్ కోడ్ `src/co_op_translator` లో ఉంటుంది; టెస్టులు `tests/` లో ఉంటాయి.
- ప్రాథమిక CLIలు (ఎంట్రీ పాయింట్‌ల ద్వారా ఇన్‌స్టాల్ చేయబడతాయి):

```bash
# కంటెంట్‌ను ఒకటి లేదా ఎక్కువ భాషలకు అనువదించండి (స్పేస్-సెపరేటెడ్ కోడ్స్)
translate -l "fr es de"

# కంటెంట్ రకాన్ని పరిమితం చేయండి
translate -l "ja" -md            # కేవలం Markdown
translate -l "ko" -nb            # కేవలం నోట్‌బుక్స్
translate -l "zh" -md -img       # Markdown + చిత్రాలు

# గతంలో అనువదించిన నోట్‌బుక్స్/Markdownలో లింకులను నవీకరించండి
migrate-links -l "all" -y
```

మరింత వినియోగ డాక్స్ కోసం `getting_started/` చూడండి.

## టెస్టింగ్ సూచనలు

రిపోజిటరీ రూట్ నుండి టెస్టులను రన్ చేయండి. కొన్ని టెస్టులకు API క్రెడెన్షియల్స్ అవసరం కావచ్చు; అవసరమైతే వాటిని స్కిప్ చేయండి.

```bash
# పూర్తి పరీక్ష సూట్ నడపండి
pytest

# ప్రత్యక్ష API కీలు అవసరం ఉన్న పరీక్షలను దాటవేయండి
pytest -m "not api_key_required"

# ఒక ఉపసెట్ నడపండి
pytest tests/co_op_translator -k "name_substring"
```

ఐచ్ఛిక కవరేజ్ (కవరేజ్ అవసరం):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # ./htmlcov కు అవుట్‌పుట్‌లు
```

## కోడ్ స్టైల్ మార్గదర్శకాలు

- ఫార్మాటర్: Black (`pyproject.toml` లో కాన్ఫిగర్ చేయబడింది, లైన్ పొడవు 88)
- లింటర్: Ruff (`pyproject.toml` లో కాన్ఫిగర్ చేయబడింది, లైన్ పొడవు 120)
- టైప్ చెక్స్: mypy (కాన్ఫిగరేషన్ ఉంది; ఇన్‌స్టాల్ చేసినప్పుడు ఎనేబుల్ చేయండి)

కమాండ్లు:

```bash
# పోయెట్రీ ద్వారా
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # సురక్షితమైన ఆటో‑ఫిక్సులు

# లేదా గ్లోబల్ టూల్స్‌తో
black .
ruff check .
```

Python సోర్స్‌లను `src/` లో, టెస్టులను `tests/` లో ఆర్గనైజ్ చేయండి మరియు ప్యాకేజీ నేమ్‌స్పేస్ (`co_op_translator.*`) లో స్పష్టమైన ఇంపోర్ట్‌లను ప్రాధాన్యత ఇవ్వండి.

## బిల్డ్ మరియు డిప్లాయ్‌మెంట్

బిల్డ్ ఆర్టిఫాక్ట్‌లు `dist/` లో ప్రచురించబడతాయి.

```bash
# నిర్మాణం (కవిత్వం)
poetry build

# నిర్మించిన వీల్ యొక్క స్థానిక ఇన్‌స్టాల్
pip install dist/*.whl
```

GitHub Actions ద్వారా ఆటోమేషన్ మద్దతు ఉంది; చూడండి:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### కంటైనర్ ఇమేజ్ (GHCR)

- అధికారిక ఇమేజ్: `ghcr.io/azure/co-op-translator:<tag>`
- ట్యాగ్‌లు: `latest` (main లో), సెమాంటిక్ ట్యాగ్‌లు `vX.Y.Z`, మరియు `sha` ట్యాగ్
- మల్టీ-ఆర్చ్: `linux/amd64, linux/arm64` Buildx ద్వారా మద్దతు
- Dockerfile ప్యాటర్న్: బిల్డ్ డిపెండెన్సీ వీల్స్‌ను బిల్డర్‌లో (తో `build-essential` మరియు `python3-dev`) నిర్మించి, రన్‌టైమ్‌లో లోకల్ వీల్‌హౌస్ నుండి ఇన్‌స్టాల్ చేయండి (`pip install --no-index --find-links=/wheels`)
- వర్క్‌ఫ్లో: `.github/workflows/docker-publish.yml` GHCRకి బిల్డ్ చేసి పుష్ చేస్తుంది

## భద్రతా అంశాలు

- API కీలు మరియు ఎండ్‌పాయింట్‌లను `.env` లేదా మీ CI సీక్రెట్స్ స్టోర్‌లో ఉంచండి; సీక్రెట్స్‌ను ఎప్పుడూ కమిట్ చేయవద్దు.
- చిత్ర అనువాదం కోసం, Azure AI Vision కీలు/ఎండ్‌పాయింట్‌లు అవసరం; లేకపోతే `-img` వదిలివేయండి.
- పెద్ద అనువాద బ్యాచ్‌లను రన్ చేయేటప్పుడు ప్రొవైడర్ కోటాలు/రేట్ లిమిట్స్‌ను ధృవీకరించండి.

## పుల్ రిక్వెస్ట్ మార్గదర్శకాలు

### సమర్పించే ముందు

1. **మీ మార్పులను టెస్ట్ చేయండి:**
   - ప్రభావిత నోట్‌బుక్‌లను పూర్తిగా రన్ చేయండి
   - అన్ని సెల్‌లు ఎర్రర్‌లతో లేకుండా ఎగ్జిక్యూట్ అవుతున్నాయో ధృవీకరించండి
   - అవుట్‌పుట్‌లు సరైనవా అని తనిఖీ చేయండి

2. **డాక్యుమెంటేషన్ అప్‌డేట్‌లు:**
   - కొత్త కాన్సెప్ట్‌లను జోడించినప్పుడు `README.md` అప్‌డేట్ చేయండి
   - క్లిష్టమైన కోడ్ కోసం నోట్‌బుక్‌లలో కామెంట్లు జోడించండి
   - Markdown సెల్‌లు ఉద్దేశాన్ని వివరించేలా చూసుకోండి

3. **ఫైల్ మార్పులు:**
   - `.env` ఫైల్‌లను కమిట్ చేయవద్దు (`.env.example` ఉపయోగించండి)
   - `venv/` లేదా `__pycache__/` డైరెక్టరీలను కమిట్ చేయవద్దు
   - కాన్సెప్ట్‌లను డెమో చేసే నోట్‌బుక్ అవుట్‌పుట్‌లను ఉంచండి
   - తాత్కాలిక ఫైల్‌లు మరియు బ్యాకప్ నోట్‌బుక్‌లను (`*-backup.ipynb`) తొలగించండి

4. **స్టైల్ మరియు ఫార్మాటింగ్:**
   - స్టైల్ మరియు ఫార్మాటింగ్ మార్గదర్శకాలను అనుసరించండి
   - `poetry run black .` మరియు `poetry run ruff check .` రన్ చేసి స్టైల్ మరియు ఫార్మాటింగ్ సమస్యలను తనిఖీ చేయండి

5. **టెస్టులు మరియు CLI సహాయం జోడించండి/అప్‌డేట్ చేయండి:**
   - ప్రవర్తనను మార్చినప్పుడు టెస్టులను జోడించండి లేదా అప్‌డేట్ చేయండి
   - మార్పులతో CLI సహాయాన్ని అనుగుణంగా ఉంచండి

### కమిట్ మెసేజ్ మరియు మర్జ్ స్ట్రాటజీ

మేము డిఫాల్ట్‌గా Squash మరియు Merge ఉపయోగిస్తాము. ఫైనల్ స్క్వాష్ కమిట్ మెసేజ్ ఈ విధంగా ఉండాలి:

```bash
<type>: <description> (#<PR సంఖ్య>)
```

అనుమతించిన రకాల:
- `Docs` — డాక్యుమెంటేషన్ అప్‌డేట్‌లు
- `Build` — బిల్డ్ సిస్టమ్, డిపెండెన్సీలు, కాన్ఫిగరేషన్/CI
- `Core` — కోర్ ఫంక్షనాలిటీ మరియు ఫీచర్లు (ఉదా., `src/co_op_translator/core`)

ఉదాహరణలు:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

గమనికలు:
- PR టైటిల్స్ తరచుగా లేబుల్‌ల ఆధారంగా ఆటో-ప్రిఫిక్స్ చేయబడతాయి; జనరేట్ చేసిన ప్రిఫిక్స్ సరైనదా అని ధృవీకరించండి.

### PR టైటిల్ ఫార్మాట్

స్పష్టమైన, సంక్షిప్తమైన టైటిల్స్ ఉపయోగించండి. ఫైనల్ స్క్వాష్ కమిట్ నిర్మాణం వంటి నిర్మాణాన్ని ప్రాధాన్యత ఇవ్వండి:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## డీబగ్గింగ్ మరియు ట్రబుల్‌షూటింగ్

- సాధారణ సమస్యలు మరియు పరిష్కారాలు: `getting_started/troubleshooting.md`
- మద్దతు ఉన్న భాషలు మరియు గమనికలు (ఫాంట్‌లు/తెలిసిన సమస్యలు): `getting_started/supported-languages.md`
- నోట్‌బుక్‌లలో లింక్ సమస్యల కోసం, మళ్లీ రన్ చేయండి: `migrate-links -l "all" -y`

## ఏజెంట్ల కోసం గమనికలు

- పునరుత్పాదక ఎన్విరాన్‌మెంట్‌ల కోసం Poetryని ప్రాధాన్యత ఇవ్వండి; లేకపోతే `requirements.txt` ఉపయోగించండి.
- CIలో CLIలను ఆహ్వానించినప్పుడు, అవసరమైన సీక్రెట్స్‌ను ఎన్విరాన్‌మెంట్ వేరియబుల్స్ లేదా `.env` ఇంజెక్షన్ ద్వారా అందించండి.
- మోనోరిపో వినియోగదారుల కోసం, ఈ రిపో స్టాండలోన్ ప్యాకేజీగా పనిచేస్తుంది; ఉప‑ప్యాకేజీ సమన్వయం అవసరం లేదు.

- మల్టీ-ఆర్చ్ మార్గదర్శకాలు: ARM వినియోగదారులు (Apple Silicon/ARM సర్వర్లు) లక్ష్యంగా ఉన్నప్పుడు `linux/arm64` ఉంచండి; లేకపోతే సరళత కోసం `linux/amd64` మాత్రమే సరిపోతుంది.
- కంటైనర్ వినియోగానికి ప్రాధాన్యత ఇచ్చే వినియోగదారులకు `README.md` లో Docker Quick Startని సూచించండి; కోటింగ్ వ్యత్యాసాల కారణంగా Bash మరియు PowerShell వేరియంట్‌లను చేర్చండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->