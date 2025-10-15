<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:24:52+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ne"
}
-->
## परियोजना अवलोकन

Co‑op Translator एक Python कमाण्ड‑लाइन उपकरण र GitHub Actions वर्कफ्लो हो जसले Markdown फाइलहरू, Jupyter नोटबुकहरू, र चित्रमा भएको पाठलाई धेरै भाषामा अनुवाद गर्छ। यसले नतिजाहरू भाषा‑अनुसारका फोल्डरहरूमा राख्छ र स्रोत सामग्रीसँग अनुवादहरू सँगै राख्छ। परियोजना Poetry‑द्वारा व्यवस्थापन गरिएको लाइब्रेरीको रूपमा संरचित छ, जसमा CLI प्रवेश बिन्दुहरू छन्।

### संरचना अवलोकन

- CLI प्रवेश बिन्दुहरू (`translate`, `migrate-links`, `evaluate`) ले एउटै CLI चलाउँछन्, जसले अनुवाद, लिंक माइग्रेशन, र मूल्याङ्कन प्रक्रिया सुरु गर्छ।
- कन्फिगरेसन लोडरले `.env` पढ्छ र LLM प्रदायक (Azure OpenAI वा OpenAI) स्वचालित रूपमा पत्ता लगाउँछ, र आवश्यक परेमा Vision प्रदायक (Azure AI Service) पनि छान्छ चित्रको पाठ निकाल्न।
- अनुवाद कोरले Markdown र नोटबुकहरू सम्हाल्छ; Vision पाइपलाइनले `-img` प्रयोग गर्दा चित्रबाट पाठ निकाल्छ।
- नतिजाहरू `translations/<lang>/` मा पाठका लागि र `translated_images/` मा चित्रका लागि राखिन्छ, मूल संरचना जोगाइन्छ।

### मुख्य प्रविधिहरू र फ्रेमवर्कहरू

- Python 3.10–3.12, प्याकेजिङका लागि Poetry
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP र डेटा: `httpx`, `pydantic`
- इमेजिङ: `pillow`, `opencv-python`, `matplotlib`
- टुलिङ: `pytest`, `black`, `ruff`

## सेटअप कमाण्डहरू

### आवश्यकताहरू

- Python 3.10–3.12
- Azure सदस्यता (वैकल्पिक, Azure AI सेवाहरूका लागि)
- LLM/Vision API हरूका लागि इन्टरनेट पहुँच (जस्तै Azure OpenAI/OpenAI, Azure AI Vision)

### विकल्प A: Poetry (सिफारिस गरिएको)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### विकल्प B: pip/venv

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

## अन्तिम प्रयोगकर्ता प्रयोग

### Docker (प्रकाशित इमेज)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

नोटहरू:
- डिफल्ट प्रवेश बिन्दु `translate` हो। लिंक माइग्रेशनका लागि `--entrypoint migrate-links` प्रयोग गर्नुहोस्।
- GHCR प्याकेज दृश्यता Public राख्नुहोस् ताकि अनामिक डाउनलोड सम्भव होस्।

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### वातावरण कन्फिगरेसन

रिपोजिटरीको मूलमा `.env` फाइल बनाउनुहोस् र रोजिएको भाषा मोडेल तथा (वैकल्पिक) Vision सेवाका लागि प्रमाणिकरण/एन्डप्वाइन्टहरू राख्नुहोस्। प्रदायक‑विशिष्ट सेटअपका लागि `getting_started/set-up-azure-ai.md` हेर्नुहोस्।

### आवश्यक वातावरण भेरिएबलहरू

कम्तीमा एउटा LLM प्रदायक कन्फिगर गर्नुपर्छ। चित्र अनुवादका लागि Azure AI Service पनि आवश्यक छ।

- Azure OpenAI (पाठ अनुवाद):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (पाठ अनुवाद वैकल्पिक):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (वैकल्पिक)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI प्रदायक प्रयोग गर्दा आवश्यक)
  - `OPENAI_BASE_URL` (वैकल्पिक; डिफल्ट `https://api.openai.com/v1`)

- चित्रको पाठ निकाल्न Azure AI Service (जब `-img` प्रयोग गरिन्छ):
  - `AZURE_AI_SERVICE_API_KEY` (प्राथमिक) वा पुरानो `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env` को उदाहरण:

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

नोटहरू:

- उपकरणले उपलब्ध LLM प्रदायक स्वचालित रूपमा पत्ता लगाउँछ; Azure OpenAI वा OpenAI मध्ये एक कन्फिगर गर्नुहोस्।
- चित्र अनुवादका लागि `AZURE_AI_SERVICE_API_KEY` र `AZURE_AI_SERVICE_ENDPOINT` दुवै आवश्यक छन्।
- आवश्यक भेरिएबलहरू नभएमा CLI ले स्पष्ट त्रुटि देखाउँछ।

## विकास कार्यप्रवाह

- स्रोत कोड `src/co_op_translator` मा राखिएको छ; परीक्षणहरू `tests/` मा छन्।
- मुख्य CLI हरू (entry points बाट इन्स्टल):

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

थप प्रयोगका लागि `getting_started/` मा डकुमेन्टेसन हेर्नुहोस्।

## परीक्षण निर्देशनहरू

रिपोजिटरीको मूलबाट परीक्षणहरू चलाउनुहोस्। केही परीक्षणहरूमा API प्रमाणिकरण आवश्यक हुन सक्छ; आवश्यक परे ती छोड्नुहोस्।

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

वैकल्पिक कभरेज (coverage आवश्यक):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## कोड शैली निर्देशिका

- Formatter: Black (`pyproject.toml` मा कन्फिगर, लाइन लम्बाइ 88)
- Linter: Ruff (`pyproject.toml` मा कन्फिगर, लाइन लम्बाइ 120)
- Type checks: mypy (कन्फिगरेसन छ; इन्स्टल भएमा सक्षम गर्नुहोस्)

कमाण्डहरू:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python स्रोतहरू `src/` मा, परीक्षणहरू `tests/` मा राख्नुहोस्, र प्याकेज नेमस्पेस (`co_op_translator.*`) भित्र स्पष्ट इम्पोर्टहरू प्रयोग गर्नुहोस्।

## निर्माण र डिप्लोयमेन्ट

निर्मित आर्टिफ्याक्टहरू `dist/` मा प्रकाशित हुन्छन्।

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions द्वारा स्वचालन समर्थित छ; हेर्नुहोस्:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### कन्टेनर इमेज (GHCR)

- आधिकारिक इमेज: `ghcr.io/azure/co-op-translator:<tag>`
- ट्यागहरू: `latest` (main मा), semantic ट्यागहरू जस्तै `vX.Y.Z`, र `sha` ट्याग
- Multi-arch: `linux/amd64, linux/arm64` Buildx द्वारा समर्थित
- Dockerfile ढाँचा: builder मा dependency wheel बनाउने (`build-essential` र `python3-dev` सहित) र runtime मा local wheelhouse बाट इन्स्टल गर्ने (`pip install --no-index --find-links=/wheels`)
- कार्यप्रवाह: `.github/workflows/docker-publish.yml` ले GHCR मा build र push गर्छ

## सुरक्षा विचारहरू

- API key र endpoint हरू `.env` वा CI secrets store मा राख्नुहोस्; कहिल्यै secrets commit नगर्नुहोस्।
- चित्र अनुवादका लागि Azure AI Vision key/endpoint आवश्यक छ; नभए `-img` प्रयोग नगर्नुहोस्।
- ठूलो अनुवाद ब्याच चलाउँदा प्रदायकको quota/rate limit जाँच गर्नुहोस्।

## पुल अनुरोध निर्देशिका

### पेश गर्नु अघि

1. **आफ्नो परिवर्तन परीक्षण गर्नुहोस्:**
   - प्रभावित नोटबुकहरू पूर्ण रूपमा चलाउनुहोस्
   - सबै सेलहरू त्रुटि बिना चल्ने सुनिश्चित गर्नुहोस्
   - नतिजा उपयुक्त छन् कि छैनन् जाँच गर्नुहोस्

2. **डकुमेन्टेसन अपडेटहरू:**
   - नयाँ अवधारणा थप्दा `README.md` अपडेट गर्नुहोस्
   - जटिल कोडका लागि नोटबुकमा टिप्पणी थप्नुहोस्
   - Markdown सेलहरूले उद्देश्य स्पष्ट पार्नुपर्छ

3. **फाइल परिवर्तनहरू:**
   - `.env` फाइल commit नगर्नुहोस् (`.env.example` प्रयोग गर्नुहोस्)
   - `venv/` वा `__pycache__/` डाइरेक्टरी commit नगर्नुहोस्
   - अवधारणा देखाउने नोटबुक आउटपुट राख्नुहोस्
   - अस्थायी फाइल र ब्याकअप नोटबुक (`*-backup.ipynb`) हटाउनुहोस्

4. **शैली र ढाँचा:**
   - शैली र ढाँका निर्देशिका पालना गर्नुहोस्
   - `poetry run black .` र `poetry run ruff check .` चलाएर शैली/ढाँका समस्या जाँच गर्नुहोस्

5. **परीक्षण र CLI सहायता थप/अपडेट गर्नुहोस्:**
   - व्यवहार परिवर्तन गर्दा परीक्षण थप/अपडेट गर्नुहोस्
   - CLI सहायता परिवर्तनसँग मिलाउनुहोस्


### Commit सन्देश र मर्ज रणनीति

हामी Squash and Merge डिफल्ट रूपमा प्रयोग गर्छौं। अन्तिम squash commit सन्देश यस ढाँचामा हुनुपर्छ:

```bash
<type>: <description> (#<PR number>)
```

स्वीकृत प्रकारहरू:
- `Docs` — डकुमेन्टेसन अपडेटहरू
- `Build` — build सिस्टम, dependencies, configuration/CI
- `Core` — मुख्य कार्यक्षमता र फिचरहरू (जस्तै `src/co_op_translator/core`)

उदाहरणहरू:
- `Docs: स्पष्टता लागि इन्स्टलेशन निर्देशन अपडेट (#50)`
- `Core: चित्र अनुवादको ह्यान्डलिंग सुधार (#60)`

नोटहरू:
- PR शीर्षकहरू प्रायः लेबलका आधारमा स्वतः prefix हुन्छन्; उत्पन्न भएको prefix सही छ कि छैन जाँच गर्नुहोस्।

### PR शीर्षक ढाँचा

स्पष्ट, संक्षिप्त शीर्षक प्रयोग गर्नुहोस्। अन्तिम squash commit जस्तै संरचना रोज्नुहोस्:
- `Docs: स्पष्टता लागि इन्स्टलेशन निर्देशन अपडेट`
- `Core: चित्र अनुवादको ह्यान्डलिंग सुधार`

## डिबगिङ र समस्या समाधान

- सामान्य समस्या र समाधान: `getting_started/troubleshooting.md`
- समर्थित भाषाहरू र नोटहरू (फन्ट/ज्ञात समस्या सहित): `getting_started/supported-languages.md`
- नोटबुकमा लिंक समस्या भएमा: `migrate-links -l "all" -y` पुन: चलाउनुहोस्

## एजेन्टहरूका लागि नोटहरू

- पुन: उत्पादक वातावरणका लागि Poetry प्राथमिकता दिनुहोस्; नभए `requirements.txt` प्रयोग गर्नुहोस्।
- CI मा CLI चलाउँदा आवश्यक secrets वातावरण भेरिएबल वा `.env` द्वारा उपलब्ध गराउनुहोस्।
- Monorepo प्रयोगकर्ताहरूका लागि, यो repo standalone प्याकेजको रूपमा काम गर्छ; कुनै sub‑package समन्वय आवश्यक छैन।

- Multi-arch निर्देशन: ARM प्रयोगकर्ता (Apple Silicon/ARM server) लक्षित भए `linux/arm64` राख्नुहोस्; नभए सरलताका लागि `linux/amd64` मात्र पर्याप्त छ।
- कन्टेनर प्रयोग गर्न चाहने प्रयोगकर्तालाई `README.md` मा Docker Quick Start देखाउनुहोस्; Bash र PowerShell दुवैका उदाहरण राख्नुहोस् किनभने quoting फरक हुन्छ।

---

**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेज़लाई नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।