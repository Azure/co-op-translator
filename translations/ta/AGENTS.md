<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:36:45+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ta"
}
-->
## திட்டத்தின் மேலோட்டம்

Co‑op Translator என்பது Python கட்டளையீட்டு கருவி மற்றும் GitHub Actions workflow ஆகும். இது Markdown கோப்புகள், Jupyter நோட்புக்குகள் மற்றும் படங்களில் உள்ள உரைகளை பல மொழிகளுக்கு மொழிபெயர்க்கும். மொழி‑வகை கோப்புறைகளில் வெளியீடுகளை ஒழுங்குபடுத்தி, மூல உள்ளடக்கத்துடன் மொழிபெயர்ப்புகளை ஒத்திசைக்கிறது. இந்த திட்டம் Poetry மூலம் நிர்வகிக்கப்படும் நூலகமாகவும் CLI entry points உடன் அமைக்கப்பட்டுள்ளது.

### கட்டமைப்பு மேலோட்டம்

- CLI entry points (`translate`, `migrate-links`, `evaluate`) ஒன்றிணைந்த CLI-யை இயக்கும்; இது மொழிபெயர்ப்பு, இணைப்பு மாற்றம், மற்றும் மதிப்பீடு செயல்முறைகளுக்கு அனுப்புகிறது.
- அமைப்பு ஏற்றுபவர் `.env`-ஐ வாசித்து, LLM வழங்குநரை (Azure OpenAI அல்லது OpenAI) தானாக கண்டறிகிறது; தேவைப்பட்டால், பட உரை பிரித்தெடுக்க Azure AI Service vision வழங்குநரை பயன்படுத்துகிறது.
- மொழிபெயர்ப்பு மையம் Markdown மற்றும் நோட்புக்குகளை கையாளும்; `-img` பயன்படுத்தும்போது vision pipeline படங்களில் இருந்து உரையை பிரித்தெடுக்கிறது.
- வெளியீடுகள் `translations/<lang>/` (உரைக்கு) மற்றும் `translated_images/` (படங்களுக்கு) என ஒழுங்குபடுத்தப்படுகின்றன; மூல அமைப்பை பாதுகாக்கும்.

### முக்கிய தொழில்நுட்பங்கள் மற்றும் கட்டமைப்புகள்

- Python 3.10–3.12, Poetry (பேக்கேஜிங்)
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP மற்றும் தரவு: `httpx`, `pydantic`
- படங்கள்: `pillow`, `opencv-python`, `matplotlib`
- கருவிகள்: `pytest`, `black`, `ruff`

## அமைப்பு கட்டளைகள்

### முன்பதிவுகள்

- Python 3.10–3.12
- Azure subscription (விருப்பத்திற்காக, Azure AI சேவைகளுக்கு)
- LLM/Vision API-களுக்காக இணைய அணுகல் (Azure OpenAI/OpenAI, Azure AI Vision)

### விருப்பம் A: Poetry (பரிந்துரைக்கப்படுகிறது)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### விருப்பம் B: pip/venv

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

## இறுதி பயனர் பயன்பாடு

### Docker (பதிவிடப்பட்ட image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

குறிப்புகள்:
- இயல்பான entrypoint `translate` ஆகும். இணைப்பு மாற்றத்திற்கு `--entrypoint migrate-links` பயன்படுத்தவும்.
- GHCR package visibility-ஐ Public-ஆக அமைக்கவும், anonymous pulls-க்கு.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### சூழல் அமைப்பு

Repository-யின் root-இல் `.env` கோப்பை உருவாக்கி, நீங்கள் தேர்ந்தெடுத்த மொழி மாதிரி மற்றும் (விருப்பமாக) vision சேவைக்கு உரிய சான்றுகள்/முகவரிகளை வழங்கவும். வழங்குநர்‑சார்ந்த அமைப்புக்கு, `getting_started/set-up-azure-ai.md`-ஐ பார்க்கவும்.

### தேவையான சூழல் மாறிகள்

குறைந்தபட்சம் ஒரு LLM வழங்குநர் அமைக்கப்பட வேண்டும். பட மொழிபெயர்ப்புக்கு Azure AI Service-யும் தேவை.

- Azure OpenAI (உரை மொழிபெயர்ப்பு):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (மாற்று உரை மொழிபெயர்ப்பு):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (விருப்பம்)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI வழங்குநரை பயன்படுத்தும்போது தேவை)
  - `OPENAI_BASE_URL` (விருப்பம்; இயல்பாக `https://api.openai.com/v1`)

- பட உரை பிரித்தெடுக்க Azure AI Service (`-img` பயன்படுத்தும்போது தேவை):
  - `AZURE_AI_SERVICE_API_KEY` (முன்னுரிமை) அல்லது பழைய `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

உதாரண `.env` பகுதி:

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

குறிப்புகள்:

- கருவி கிடைக்கும் LLM வழங்குநரை தானாக கண்டறியும்; Azure OpenAI அல்லது OpenAI-ஐ அமைக்கவும்.
- பட மொழிபெயர்ப்புக்கு `AZURE_AI_SERVICE_API_KEY` மற்றும் `AZURE_AI_SERVICE_ENDPOINT` இரண்டும் தேவை.
- தேவையான மாறிகள் இல்லையெனில் CLI தெளிவான பிழை செய்தியை காட்டும்.

## மேம்பாட்டு பணிப்படிகள்

- மூல குறியீடு `src/co_op_translator`-இல்; சோதனைகள் `tests/`-இல்.
- முதன்மை CLI-கள் (entry points மூலம் நிறுவப்படும்):

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

மேலும் பயன்பாட்டு ஆவணங்கள் `getting_started/`-இல்.

## சோதனை வழிமுறைகள்

Repository-யின் root-இல் இருந்து சோதனைகளை இயக்கவும். சில சோதனைகளுக்கு API சான்றுகள் தேவை; அவற்றை தேவையெனில் தவிர்க்கவும்.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

விருப்பமான coverage (`coverage` தேவை):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## குறியீட்டு பாணி வழிகாட்டிகள்

- Formatter: Black (`pyproject.toml`-இல் அமைக்கப்பட்டுள்ளது, line length 88)
- Linter: Ruff (`pyproject.toml`-இல், line length 120)
- Type checks: mypy (அமைப்பு உள்ளது; நிறுவப்பட்டால் இயக்கவும்)

கட்டளைகள்:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python மூலங்களை `src/`-இல், சோதனைகளை `tests/`-இல் ஒழுங்குபடுத்தவும்; package namespace (`co_op_translator.*`)-இல் explicit imports-ஐ விரும்பவும்.

## கட்டமைப்பு மற்றும் வெளியீடு

Build செய்யப்பட்ட artifacts `dist/`-இல் வெளியிடப்படும்.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions மூலம் தானாக செயல்படுத்தலாம்; பார்க்க:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- அதிகாரப்பூர்வ image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (main-இல்), semantic tags (`vX.Y.Z`), மற்றும் `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` Buildx மூலம் ஆதரிக்கப்படுகிறது
- Dockerfile pattern: builder-இல் dependency wheels-ஐ உருவாக்கி (with `build-essential` மற்றும் `python3-dev`), runtime-இல் local wheelhouse-இல் இருந்து நிறுவவும் (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` GHCR-க்கு build செய்து push செய்யும்

## பாதுகாப்பு கவனிக்க வேண்டியவை

- API keys மற்றும் endpoints-ஐ `.env`-இல் அல்லது உங்கள் CI secrets store-இல் வைக்கவும்; ரகசியங்களை commit செய்ய வேண்டாம்.
- பட மொழிபெயர்ப்புக்கு Azure AI Vision keys/endpoints தேவை; இல்லையெனில் `-img` பயன்படுத்த வேண்டாம்.
- பெரிய மொழிபெயர்ப்பு தொகுதிகளை இயக்கும்போது வழங்குநர் quota/rate limits-ஐ சரிபார்க்கவும்.

## Pull Request வழிகாட்டிகள்

### சமர்ப்பிப்பதற்கு முன்

1. **உங்கள் மாற்றங்களை சோதிக்கவும்:**
   - பாதிக்கப்பட்ட நோட்புக்குகளை முழுமையாக இயக்கவும்
   - அனைத்து cell-களும் பிழையில்லாமல் இயங்குவதை உறுதி செய்யவும்
   - வெளியீடுகள் பொருத்தமானவை என்பதை சரிபார்க்கவும்

2. **ஆவண புதுப்பிப்புகள்:**
   - புதிய கருத்துகள் சேர்க்கும்போது `README.md`-ஐ புதுப்பிக்கவும்
   - சிக்கலான குறியீடுக்கு நோட்புக்குகளில் கருத்துகள் சேர்க்கவும்
   - markdown cell-கள் நோட்புக்கில் நோக்கம் விளக்க வேண்டும்

3. **கோப்பு மாற்றங்கள்:**
   - `.env` கோப்புகளை commit செய்ய வேண்டாம் (`.env.example` பயன்படுத்தவும்)
   - `venv/` அல்லது `__pycache__/` கோப்புறைகளை commit செய்ய வேண்டாம்
   - கருத்துகளை விளக்கும் போது நோட்புக் வெளியீடுகளை வைத்திருக்கவும்
   - தற்காலிக கோப்புகள் மற்றும் backup நோட்புக்குகளை (`*-backup.ipynb`) நீக்கவும்

4. **பாணி மற்றும் வடிவமைப்பு:**
   - பாணி மற்றும் வடிவமைப்பு வழிகாட்டிகளை பின்பற்றவும்
   - `poetry run black .` மற்றும் `poetry run ruff check .` மூலம் பாணி/வடிவமைப்பு பிழைகளை சரிபார்க்கவும்

5. **சோதனைகள் மற்றும் CLI உதவியை சேர்க்க/புதுப்பிக்கவும்:**
   - நடத்தை மாற்றும்போது சோதனைகளை சேர்க்க/புதுப்பிக்கவும்
   - CLI உதவி மாற்றங்களுக்கு ஏற்ப ஒத்திசைக்கவும்

### Commit செய்தி மற்றும் இணைப்பு உத்தி

நாம் Squash and Merge-ஐ இயல்பாக பயன்படுத்துகிறோம். இறுதி squash commit செய்தி கீழ்காணும் வடிவில் இருக்க வேண்டும்:

```bash
<type>: <description> (#<PR number>)
```

அனுமதிக்கப்பட்ட வகைகள்:
- `Docs` — ஆவண புதுப்பிப்புகள்
- `Build` — build அமைப்பு, dependencies, configuration/CI
- `Core` — முக்கிய செயல்பாடுகள் மற்றும் அம்சங்கள் (உதா: `src/co_op_translator/core`)

உதாரணங்கள்:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

குறிப்புகள்:
- PR titles பெரும்பாலும் labels-ஐ அடிப்படையாக auto-prefix செய்யப்படும்; உருவாக்கப்பட்ட prefix சரியானதா என்பதை உறுதி செய்யவும்.

### PR தலைப்பு வடிவம்

தெளிவான, சுருக்கமான தலைப்புகளை பயன்படுத்தவும். இறுதி squash commit போலவே அமைக்கவும்:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## பிழைநீக்கம் மற்றும் சிக்கல் தீர்வு

- பொதுவான சிக்கல்கள் மற்றும் தீர்வுகள்: `getting_started/troubleshooting.md`
- ஆதரிக்கப்படும் மொழிகள் மற்றும் குறிப்புகள் (font/பழக்கப்பட்ட சிக்கல்கள்): `getting_started/supported-languages.md`
- நோட்புக்குகளில் இணைப்பு சிக்கலுக்கு, மீண்டும் இயக்கவும்: `migrate-links -l "all" -y`

## முகவர்களுக்கு குறிப்புகள்

- மீண்டும் உருவாக்கக்கூடிய சூழலுக்கு Poetry-ஐ விரும்பவும்; இல்லையெனில் `requirements.txt` பயன்படுத்தவும்.
- CI-யில் CLI-களை இயக்கும்போது, தேவையான ரகசியங்களை சூழல் மாறிகள் அல்லது `.env` மூலம் வழங்கவும்.
- Monorepo-வில் பயன்படுத்துபவர்களுக்கு, இந்த repo தனிப்பட்ட package-ஆக செயல்படும்; sub‑package ஒத்திசைப்பு தேவையில்லை.

- Multi-arch வழிகாட்டி: ARM பயனர்கள் (Apple Silicon/ARM servers) இலக்கு என்றால் `linux/arm64`-ஐ வைத்திருக்கவும்; இல்லையெனில் எளிமைக்காக `linux/amd64` மட்டும் போதுமானது.
- Container பயன்பாட்டை விரும்புபவர்களுக்கு `README.md`-இல் Docker Quick Start-ஐ காட்டவும்; Bash மற்றும் PowerShell வகைகளையும் சேர்க்கவும், quote வேறுபாடுகளுக்காக.

---

**பொறுப்புத் தவிர்ப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்தாலும், தானாக மொழிபெயர்க்கப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை தயவுசெய்து கவனிக்கவும். மூல ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல் அல்லது தவறான விளக்கத்திற்கு நாங்கள் பொறுப்பல்ல.