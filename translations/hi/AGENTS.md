<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:23:39+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hi"
}
-->
## परियोजना का अवलोकन

Co‑op Translator एक Python कमांड‑लाइन टूल और GitHub Actions वर्कफ़्लो है जो Markdown फाइलें, Jupyter नोटबुक्स, और इमेज टेक्स्ट को कई भाषाओं में अनुवाद करता है। यह आउटपुट्स को भाषा‑विशिष्ट फोल्डरों में व्यवस्थित करता है और स्रोत सामग्री के साथ अनुवादों को सिंक्रनाइज़ रखता है। यह प्रोजेक्ट Poetry‑प्रबंधित लाइब्रेरी के रूप में संरचित है जिसमें CLI एंट्री पॉइंट्स हैं।

### आर्किटेक्चर का अवलोकन

- CLI एंट्री पॉइंट्स (`translate`, `migrate-links`, `evaluate`) एकीकृत CLI को कॉल करते हैं जो अनुवाद, लिंक माइग्रेशन, और मूल्यांकन फ्लो को डिस्पैच करता है।
- कॉन्फ़िगरेशन लोडर `.env` पढ़ता है और LLM प्रदाता (Azure OpenAI या OpenAI) को ऑटो‑डिटेक्ट करता है, और यदि अनुरोध किया गया हो तो इमेज टेक्स्ट एक्सट्रैक्शन के लिए विज़न प्रदाता (Azure AI Service) को भी।
- ट्रांसलेशन कोर Markdown और नोटबुक्स को संभालता है; विज़न पाइपलाइन इमेज से टेक्स्ट निकालती है जब `-img` उपयोग किया जाता है।
- आउटपुट्स को `translations/<lang>/` में टेक्स्ट के लिए और `translated_images/` में इमेज के लिए व्यवस्थित किया जाता है, मूल संरचना को बनाए रखते हुए।

### प्रमुख तकनीकें और फ्रेमवर्क्स

- Python 3.10–3.12, पैकेजिंग के लिए Poetry
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- विज़न: Azure AI Service (Computer Vision)
- HTTP और डेटा: `httpx`, `pydantic`
- इमेजिंग: `pillow`, `opencv-python`, `matplotlib`
- टूलिंग: `pytest`, `black`, `ruff`

## सेटअप कमांड्स

### आवश्यकताएँ

- Python 3.10–3.12
- Azure सब्सक्रिप्शन (वैकल्पिक, Azure AI सेवाओं के लिए)
- LLM/Vision APIs के लिए इंटरनेट एक्सेस (जैसे Azure OpenAI/OpenAI, Azure AI Vision)

### विकल्प A: Poetry (अनुशंसित)

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

## एंड यूज़र उपयोग

### Docker (प्रकाशित इमेज)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

नोट्स:
- डिफ़ॉल्ट एंट्रीपॉइंट `translate` है। लिंक माइग्रेशन के लिए `--entrypoint migrate-links` से ओवरराइड करें।
- गुमनाम pulls के लिए GHCR पैकेज विजिबिलिटी Public रखें।

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### पर्यावरण कॉन्फ़िगरेशन

रिपॉजिटरी रूट पर `.env` फाइल बनाएं और अपनी चुनी हुई भाषा मॉडल और (वैकल्पिक) विज़न सेवा के लिए क्रेडेंशियल्स/एंडपॉइंट्स प्रदान करें। प्रदाता‑विशिष्ट सेटअप के लिए देखें `getting_started/set-up-azure-ai.md`।

### आवश्यक पर्यावरण वेरिएबल्स

कम से कम एक LLM प्रदाता कॉन्फ़िगर होना चाहिए। इमेज अनुवाद के लिए Azure AI Service भी कॉन्फ़िगर होनी चाहिए।

- Azure OpenAI (टेक्स्ट अनुवाद):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (टेक्स्ट अनुवाद विकल्प):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (वैकल्पिक)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI प्रदाता उपयोग करते समय आवश्यक)
  - `OPENAI_BASE_URL` (वैकल्पिक; डिफ़ॉल्ट `https://api.openai.com/v1`)

- इमेज टेक्स्ट एक्सट्रैक्शन के लिए Azure AI Service (`-img` उपयोग करते समय आवश्यक):
  - `AZURE_AI_SERVICE_API_KEY` (प्राथमिकता) या पुराना `AZURE_SUBSCRIPTION_KEY`
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

नोट्स:

- टूल उपलब्ध LLM प्रदाता को ऑटो‑डिटेक्ट करता है; Azure OpenAI या OpenAI में से किसी एक को कॉन्फ़िगर करें।
- इमेज अनुवाद के लिए दोनों `AZURE_AI_SERVICE_API_KEY` और `AZURE_AI_SERVICE_ENDPOINT` आवश्यक हैं।
- यदि आवश्यक वेरिएबल्स गायब हैं तो CLI स्पष्ट त्रुटि देगा।

## डेवलपमेंट वर्कफ़्लो

- सोर्स कोड `src/co_op_translator` के अंतर्गत रहता है; टेस्ट्स `tests/` में।
- मुख्य CLIs (एंट्री पॉइंट्स के माध्यम से इंस्टॉल):

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

अधिक उपयोग दस्तावेज़ के लिए देखें `getting_started/`।

## टेस्टिंग निर्देश

रिपॉजिटरी रूट से टेस्ट्स चलाएँ। कुछ टेस्ट्स के लिए API क्रेडेंशियल्स आवश्यक हो सकते हैं; आवश्यकता अनुसार उन्हें स्किप करें।

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

वैकल्पिक कवरेज (`coverage` आवश्यक):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## कोड स्टाइल दिशानिर्देश

- फॉर्मेटर: Black (`pyproject.toml` में कॉन्फ़िगर, लाइन लंबाई 88)
- लिंटर: Ruff (`pyproject.toml` में कॉन्फ़िगर, लाइन लंबाई 120)
- टाइप चेक्स: mypy (कॉन्फ़िगरेशन मौजूद; इंस्टॉल होने पर सक्षम करें)

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

Python स्रोतों को `src/` में, टेस्ट्स को `tests/` में व्यवस्थित करें, और पैकेज नेमस्पेस (`co_op_translator.*`) के भीतर स्पष्ट इम्पोर्ट्स को प्राथमिकता दें।

## बिल्ड और डिप्लॉयमेंट

बिल्ड आर्टिफैक्ट्स `dist/` में प्रकाशित होते हैं।

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions के माध्यम से ऑटोमेशन समर्थित है; देखें:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### कंटेनर इमेज (GHCR)

- आधिकारिक इमेज: `ghcr.io/azure/co-op-translator:<tag>`
- टैग्स: `latest` (main पर), semantic टैग्स जैसे `vX.Y.Z`, और एक `sha` टैग
- मल्टी‑आर्क: `linux/amd64, linux/arm64` Buildx के माध्यम से समर्थित
- Dockerfile पैटर्न: बिल्ड डिपेंडेंसी व्हील्स को बिल्डर में बनाएं (`build-essential` और `python3-dev` के साथ) और रनटाइम में लोकल व्हीलहाउस से इंस्टॉल करें (`pip install --no-index --find-links=/wheels`)
- वर्कफ़्लो: `.github/workflows/docker-publish.yml` GHCR पर बिल्ड और पुश करता है

## सुरक्षा विचार

- API कीज़ और एंडपॉइंट्स को `.env` या अपने CI सीक्रेट्स स्टोर में रखें; कभी भी सीक्रेट्स कमिट न करें।
- इमेज अनुवाद के लिए Azure AI Vision कीज़/एंडपॉइंट्स आवश्यक हैं; अन्यथा `-img` छोड़ दें।
- बड़े अनुवाद बैच चलाते समय प्रदाता कोटा/रेट लिमिट्स को सत्यापित करें।

## पुल रिक्वेस्ट दिशानिर्देश

### सबमिट करने से पहले

1. **अपनी परिवर्तनों का परीक्षण करें:**
   - प्रभावित नोटबुक्स को पूरी तरह चलाएँ
   - सुनिश्चित करें कि सभी सेल्स बिना त्रुटि के निष्पादित हों
   - आउटपुट उपयुक्त हैं यह जांचें

2. **डॉक्युमेंटेशन अपडेट्स:**
   - यदि नए कॉन्सेप्ट जोड़ रहे हैं तो `README.md` अपडेट करें
   - जटिल कोड के लिए नोटबुक्स में कमेंट्स जोड़ें
   - सुनिश्चित करें कि मार्कडाउन सेल्स उद्देश्य स्पष्ट करें

3. **फाइल परिवर्तन:**
   - `.env` फाइलें कमिट करने से बचें (`.env.example` का उपयोग करें)
   - `venv/` या `__pycache__/` डायरेक्टरीज़ कमिट न करें
   - जब वे कॉन्सेप्ट दर्शाते हैं तो नोटबुक आउटपुट्स रखें
   - अस्थायी फाइलें और बैकअप नोटबुक्स (`*-backup.ipynb`) हटा दें

4. **स्टाइल और फॉर्मेटिंग:**
   - स्टाइल और फॉर्मेटिंग दिशानिर्देशों का पालन करें
   - स्टाइल और फॉर्मेटिंग समस्याओं के लिए `poetry run black .` और `poetry run ruff check .` चलाएँ

5. **टेस्ट्स और CLI हेल्प जोड़ें/अपडेट करें:**
   - व्यवहार बदलते समय टेस्ट्स जोड़ें या अपडेट करें
   - CLI हेल्प को परिवर्तनों के अनुरूप रखें


### कमिट संदेश और मर्ज रणनीति

हम Squash and Merge को डिफ़ॉल्ट के रूप में उपयोग करते हैं। अंतिम squash कमिट संदेश इस प्रकार होना चाहिए:

```bash
<type>: <description> (#<PR number>)
```

अनुमत प्रकार:
- `Docs` — डॉक्युमेंटेशन अपडेट्स
- `Build` — बिल्ड सिस्टम, डिपेंडेंसीज़, कॉन्फ़िगरेशन/CI
- `Core` — मुख्य कार्यक्षमता और फीचर्स (जैसे `src/co_op_translator/core`)

उदाहरण:
- `Docs: स्पष्टता के लिए इंस्टॉलेशन निर्देश अपडेट करें (#50)`
- `Core: इमेज अनुवाद की हैंडलिंग सुधारें (#60)`

नोट्स:
- PR टाइटल्स अक्सर लेबल्स के आधार पर ऑटो‑प्रिफिक्स होते हैं; सुनिश्चित करें कि जनरेटेड प्रिफिक्स सही है।

### PR शीर्षक प्रारूप

स्पष्ट, संक्षिप्त शीर्षक का उपयोग करें। अंतिम squash कमिट के समान संरचना को प्राथमिकता दें:
- `Docs: स्पष्टता के लिए इंस्टॉलेशन निर्देश अपडेट करें`
- `Core: इमेज अनुवाद की हैंडलिंग सुधारें`

## डिबगिंग और समस्या निवारण

- सामान्य समस्याएँ और समाधान: `getting_started/troubleshooting.md`
- समर्थित भाषाएँ और नोट्स (फॉन्ट्स/ज्ञात समस्याएँ सहित): `getting_started/supported-languages.md`
- नोटबुक्स में लिंक समस्याओं के लिए पुनः चलाएँ: `migrate-links -l "all" -y`

## एजेंट्स के लिए नोट्स

- पुनरुत्पादित वातावरण के लिए Poetry को प्राथमिकता दें; अन्यथा `requirements.txt` का उपयोग करें।
- CI में CLIs को कॉल करते समय आवश्यक सीक्रेट्स पर्यावरण वेरिएबल्स या `.env` इंजेक्शन के माध्यम से प्रदान करें।
- मोनोरिपो उपभोक्ताओं के लिए, यह रिपो एक स्टैंडअलोन पैकेज के रूप में कार्य करता है; कोई सब‑पैकेज समन्वय आवश्यक नहीं है।

- मल्टी‑आर्क गाइडेंस: जब ARM उपयोगकर्ता (Apple Silicon/ARM सर्वर) लक्ष्य हों तो `linux/arm64` रखें; अन्यथा केवल `linux/amd64` सरलता के लिए स्वीकार्य है।
- जब उपयोगकर्ता कंटेनर उपयोग पसंद करते हैं तो उन्हें `README.md` में Docker Quick Start की ओर इंगित करें; Bash और PowerShell वेरिएंट शामिल करें क्योंकि कोटिंग में अंतर होता है।

---

**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।