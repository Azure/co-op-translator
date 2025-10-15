<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:24:29+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mr"
}
-->
## प्रकल्पाचा आढावा

Co‑op Translator हे एक Python कमांड‑लाइन टूल आणि GitHub Actions वर्कफ्लो आहे जे Markdown फाइल्स, Jupyter नोटबुक्स आणि इमेजमधील मजकूर अनेक भाषांमध्ये अनुवादित करते. हे आउटपुट्स भाषा‑निहाय फोल्डर्समध्ये ठेवते आणि मूळ कंटेंटशी अनुवाद सिंक्रोनाइझ ठेवते. प्रकल्प Poetry‑ने व्यवस्थापित केलेल्या लायब्ररीप्रमाणे रचलेला आहे, ज्यात CLI एंट्री पॉइंट्स आहेत.

### आर्किटेक्चरचा आढावा

- CLI एंट्री पॉइंट्स (`translate`, `migrate-links`, `evaluate`) एकत्रित CLI कॉल करतात, जे अनुवाद, लिंक माइग्रेशन आणि मूल्यांकन फ्लोमध्ये पाठवतात.
- कॉन्फिगरेशन लोडर `.env` वाचतो आणि LLM प्रोव्हायडर (Azure OpenAI किंवा OpenAI) आणि, गरज असल्यास, व्हिजन प्रोव्हायडर (Azure AI Service) ऑटो‑डिटेक्ट करतो, इमेजमधील मजकूर काढण्यासाठी.
- ट्रान्सलेशन कोर Markdown आणि नोटबुक्स हाताळतो; व्हिजन पाइपलाइन `-img` वापरल्यास इमेजमधून मजकूर काढते.
- आउटपुट्स `translations/<lang>/` मध्ये मजकूरासाठी आणि `translated_images/` मध्ये इमेजसाठी ठेवले जातात, मूळ संरचना जपली जाते.

### मुख्य तंत्रज्ञान आणि फ्रेमवर्क्स

- Python 3.10–3.12, पॅकेजिंगसाठी Poetry
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP आणि डेटा: `httpx`, `pydantic`
- इमेजिंग: `pillow`, `opencv-python`, `matplotlib`
- टूलिंग: `pytest`, `black`, `ruff`

## सेटअप कमांड्स

### पूर्वअटी

- Python 3.10–3.12
- Azure सबस्क्रिप्शन (पर्यायी, Azure AI सेवांसाठी)
- LLM/Vision APIs साठी इंटरनेट कनेक्शन (उदा. Azure OpenAI/OpenAI, Azure AI Vision)

### पर्याय A: Poetry (शिफारसीय)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### पर्याय B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## एंड यूजर वापर

### Docker (प्रकाशित इमेज)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

टीप:
- डीफॉल्ट एंट्रीपॉइंट `translate` आहे. लिंक माइग्रेशनसाठी `--entrypoint migrate-links` वापरून ओव्हरराइड करा.
- GHCR पॅकेज व्हिजिबिलिटी Public ठेवा, जेणेकरून अनॉनिमस pulls करता येतील.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### वातावरण कॉन्फिगरेशन

रिपॉझिटरीच्या रूटवर `.env` फाइल तयार करा आणि निवडलेल्या भाषा मॉडेलसाठी आणि (पर्यायी) व्हिजन सर्व्हिससाठी क्रेडेन्शियल्स/एंडपॉइंट्स द्या. प्रोव्हायडर‑निहाय सेटअपसाठी `getting_started/set-up-azure-ai.md` पहा.

### आवश्यक वातावरणीय व्हेरिएबल्स

किमान एक LLM प्रोव्हायडर कॉन्फिगर केला पाहिजे. इमेज ट्रान्सलेशनसाठी Azure AI Service देखील आवश्यक आहे.

- Azure OpenAI (मजकूर अनुवाद):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (मजकूर अनुवाद पर्याय):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (पर्यायी)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI प्रोव्हायडर वापरताना आवश्यक)
  - `OPENAI_BASE_URL` (पर्यायी; डीफॉल्ट `https://api.openai.com/v1`)

- इमेजमधील मजकूर काढण्यासाठी Azure AI Service (`-img` वापरताना आवश्यक):
  - `AZURE_AI_SERVICE_API_KEY` (प्राधान्य) किंवा जुना `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

उदाहरण `.env` स्निपेट:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

टीप:

- टूल उपलब्ध LLM प्रोव्हायडर ऑटो‑डिटेक्ट करते; Azure OpenAI किंवा OpenAI पैकी एक कॉन्फिगर करा.
- इमेज ट्रान्सलेशनसाठी `AZURE_AI_SERVICE_API_KEY` आणि `AZURE_AI_SERVICE_ENDPOINT` दोन्ही आवश्यक आहेत.
- आवश्यक व्हेरिएबल्स नसल्यास CLI स्पष्ट त्रुटी दाखवेल.

## विकास वर्कफ्लो

- सोर्स कोड `src/co_op_translator` मध्ये; टेस्ट्स `tests/` मध्ये.
- मुख्य CLI (एंट्री पॉइंट्सद्वारे इंस्टॉल):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

अधिक वापरासाठी `getting_started/` मधील डॉक्युमेंटेशन पहा.

## टेस्टिंग सूचना

रिपॉझिटरीच्या रूटवरून टेस्ट्स चालवा. काही टेस्ट्ससाठी API क्रेडेन्शियल्स लागतील; गरज असल्यास त्या स्किप करा.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

पर्यायी कव्हरेज (`coverage` आवश्यक):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## कोड स्टाइल मार्गदर्शक

- Formatter: Black (`pyproject.toml` मध्ये कॉन्फिगर, लाईन लांबी 88)
- Linter: Ruff (`pyproject.toml` मध्ये कॉन्फिगर, लाईन लांबी 120)
- Type checks: mypy (कॉन्फिगरेशन आहे; इंस्टॉल केल्यास सक्षम करा)

कमांड्स:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python सोर्सेस `src/` मध्ये, टेस्ट्स `tests/` मध्ये ठेवा, आणि पॅकेज namespace (`co_op_translator.*`) मध्ये explicit imports वापरा.

## बिल्ड आणि डिप्लॉयमेंट

बिल्ड आर्टिफॅक्ट्स `dist/` मध्ये प्रकाशित होतात.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions द्वारे ऑटोमेशन सपोर्ट आहे; पहा:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### कंटेनर इमेज (GHCR)

- अधिकृत इमेज: `ghcr.io/azure/co-op-translator:<tag>`
- टॅग्स: `latest` (main वर), semantic टॅग्स जसे `vX.Y.Z`, आणि `sha` टॅग
- मल्टी‑आर्क: `linux/amd64, linux/arm64` Buildx द्वारे सपोर्ट
- Dockerfile पॅटर्न: बिल्ड डिपेंडन्सी व्हील्स builder मध्ये (सह `build-essential` आणि `python3-dev`) आणि runtime मध्ये लोकल wheelhouse मधून इंस्टॉल (`pip install --no-index --find-links=/wheels`)
- वर्कफ्लो: `.github/workflows/docker-publish.yml` GHCR वर बिल्ड आणि पुश करते

## सुरक्षा विचार

- API कीज आणि एंडपॉइंट्स `.env` किंवा CI secrets store मध्ये ठेवा; कधीही secrets कमिट करू नका.
- इमेज ट्रान्सलेशनसाठी Azure AI Vision कीज/एंडपॉइंट्स आवश्यक; अन्यथा `-img` वापरू नका.
- मोठ्या ट्रान्सलेशन बॅचेस चालवताना प्रोव्हायडर कोटा/रेट लिमिट्स तपासा.

## पुल रिक्वेस्ट मार्गदर्शक

### सबमिट करण्यापूर्वी

1. **तुमचे बदल टेस्ट करा:**
   - संबंधित नोटबुक्स पूर्णपणे चालवा
   - सर्व सेल्स त्रुटीशिवाय चालतात याची खात्री करा
   - आउटपुट योग्य आहेत का तपासा

2. **डॉक्युमेंटेशन अपडेट्स:**
   - नवीन संकल्पना जोडल्यास `README.md` अपडेट करा
   - क्लिष्ट कोडसाठी नोटबुक्समध्ये कमेंट्स जोडा
   - Markdown सेल्समध्ये उद्देश स्पष्ट करा

3. **फाइल बदल:**
   - `.env` फाइल्स कमिट करू नका (`.env.example` वापरा)
   - `venv/` किंवा `__pycache__/` डिरेक्टरीज कमिट करू नका
   - संकल्पना दाखवणारे नोटबुक आउटपुट्स ठेवा
   - तात्पुरत्या फाइल्स आणि बॅकअप नोटबुक्स (`*-backup.ipynb`) काढा

4. **स्टाइल आणि फॉरमॅटिंग:**
   - स्टाइल आणि फॉरमॅटिंग मार्गदर्शक पाळा
   - `poetry run black .` आणि `poetry run ruff check .` चालवून स्टाइल आणि फॉरमॅटिंग तपासा

5. **टेस्ट्स आणि CLI हेल्प जोडा/अपडेट करा:**
   - वर्तन बदलल्यास टेस्ट्स जोडा किंवा अपडेट करा
   - CLI हेल्प बदलांसह सुसंगत ठेवा


### कमिट मेसेज आणि मर्ज स्ट्रॅटेजी

आम्ही Squash and Merge डीफॉल्ट वापरतो. अंतिम squash कमिट मेसेज खालीलप्रमाणे असावा:

```bash
<type>: <description> (#<PR number>)
```

मान्य प्रकार:
- `Docs` — डॉक्युमेंटेशन अपडेट्स
- `Build` — बिल्ड सिस्टम, डिपेंडन्सीज, कॉन्फिगरेशन/CI
- `Core` — मुख्य फंक्शनॅलिटी आणि फीचर्स (उदा. `src/co_op_translator/core`)

उदाहरणे:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

टीप:
- PR टायटल्स बहुतेक वेळा लेबल्सवरून ऑटो‑प्रिफिक्स होतात; तयार झालेला प्रिफिक्स योग्य आहे का तपासा.

### PR टायटल फॉरमॅट

स्पष्ट, संक्षिप्त टायटल्स वापरा. अंतिम squash कमिटसारखीच रचना ठेवा:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## डीबगिंग आणि ट्रबलशूटिंग

- सामान्य समस्या आणि उपाय: `getting_started/troubleshooting.md`
- सपोर्टेड भाषा आणि टीपा (फॉन्ट्स/ज्ञात समस्या): `getting_started/supported-languages.md`
- नोटबुक्समधील लिंक समस्या असल्यास पुन्हा चालवा: `migrate-links -l "all" -y`

## एजंटसाठी टीपा

- पुनरुत्पादक वातावरणासाठी Poetry वापरा; अन्यथा `requirements.txt` वापरा.
- CI मध्ये CLI कॉल करताना आवश्यक secrets environment variables किंवा `.env` injection द्वारे द्या.
- Monorepo वापरकर्त्यांसाठी, हे repo स्वतंत्र पॅकेजप्रमाणे काम करते; उप‑पॅकेज समन्वय आवश्यक नाही.

- मल्टी‑आर्क मार्गदर्शन: ARM वापरकर्ते (Apple Silicon/ARM सर्व्हर्स) टार्गेट असल्यास `linux/arm64` ठेवा; अन्यथा साधेपणासाठी `linux/amd64` पुरेसे.
- कंटेनर वापर प्राधान्य असल्यास वापरकर्त्यांना `README.md` मधील Docker Quick Start दाखवा; Bash आणि PowerShell व्हेरिएंट्स समाविष्ट करा, कारण कोटिंगमध्ये फरक असतो.

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.