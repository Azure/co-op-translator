<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:32:01+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sw"
}
-->
## Muhtasari wa Mradi

Co‑op Translator ni zana ya Python ya mstari wa amri na mtiririko wa GitHub Actions inayotafsiri faili za Markdown, daftari za Jupyter, na maandishi ya picha kwenda lugha mbalimbali. Inaweka matokeo chini ya folda maalum za lugha na inahakikisha tafsiri zinabaki sambamba na yaliyomo asili. Mradi umeundwa kama maktaba inayosimamiwa na Poetry yenye sehemu za kuingia za CLI.

### Muhtasari wa Muundo

- Sehemu za kuingia za CLI (`translate`, `migrate-links`, `evaluate`) zinatumia CLI moja inayosambaza kazi za kutafsiri, kuhama viungo, na kutathmini.
- Kipakiaji cha mipangilio husoma `.env` na hutambua kiotomatiki mtoa huduma wa LLM (Azure OpenAI au OpenAI) na, ikihitajika, mtoa huduma wa vision (Azure AI Service) kwa ajili ya kutoa maandishi kwenye picha.
- Kiini cha tafsiri hushughulikia Markdown na daftari; mtiririko wa vision hutoa maandishi kutoka kwenye picha pale `-img` inapotumika.
- Matokeo yanaandaliwa kwenye `translations/<lang>/` kwa maandishi na `translated_images/` kwa picha, yakihifadhi muundo wa asili.

### Teknolojia na Mifumo Muhimu

- Python 3.10–3.12, Poetry kwa ufungashaji
- CLI: `click`
- SDK za LLM/AI: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP na data: `httpx`, `pydantic`
- Picha: `pillow`, `opencv-python`, `matplotlib`
- Zana: `pytest`, `black`, `ruff`

## Amri za Usanidi

### Mahitaji ya Awali

- Python 3.10–3.12
- Usajili wa Azure (hiari, kwa huduma za Azure AI)
- Muunganisho wa intaneti kwa API za LLM/Vision (mfano Azure OpenAI/OpenAI, Azure AI Vision)

### Chaguo A: Poetry (inapendekezwa)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Chaguo B: pip/venv

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

## Matumizi kwa Mtumiaji wa Mwisho

### Docker (picha iliyochapishwa)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Maelezo:
- Sehemu ya kuingia chaguo-msingi ni `translate`. Badilisha kwa `--entrypoint migrate-links` kwa ajili ya kuhama viungo.
- Hakikisha kifurushi cha GHCR kinaonekana kwa Umma ili kuruhusu upakuaji bila jina.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Mipangilio ya Mazingira

Tengeneza faili `.env` kwenye mzizi wa hazina na uweke taarifa za kitambulisho/viunganishi kwa mfano wa lugha uliouchagua na (hiari) huduma ya vision. Kwa maelezo maalum ya mtoa huduma, angalia `getting_started/set-up-azure-ai.md`.

### Vigezo vya Mazingira Vinavyohitajika

Angalau mtoa huduma mmoja wa LLM lazima awe amesanidiwa. Kwa tafsiri ya picha, Azure AI Service pia inahitajika.

- Azure OpenAI (tafsiri ya maandishi):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (mbadala wa tafsiri ya maandishi):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (hiari)
  - `OPENAI_CHAT_MODEL_ID` (inahitajika ukitumia OpenAI)
  - `OPENAI_BASE_URL` (hiari; chaguo-msingi ni `https://api.openai.com/v1`)

- Azure AI Service kwa kutoa maandishi kwenye picha (inahitajika ukitumia `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (inapendekezwa) au `AZURE_SUBSCRIPTION_KEY` ya zamani
  - `AZURE_AI_SERVICE_ENDPOINT`

Mfano wa kipande cha `.env`:

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

Maelezo:

- Zana hutambua kiotomatiki mtoa huduma wa LLM anayepatikana; sanidi Azure OpenAI au OpenAI.
- Tafsiri ya picha inahitaji zote mbili `AZURE_AI_SERVICE_API_KEY` na `AZURE_AI_SERVICE_ENDPOINT`.
- CLI itatoa kosa wazi ikiwa vigezo vinavyohitajika havipo.

## Mtiririko wa Maendeleo

- Chanzo cha msimbo kipo chini ya `src/co_op_translator`; majaribio chini ya `tests/`.
- CLI kuu (zimesanidiwa kupitia entry points):

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

Angalia nyaraka za matumizi zaidi kwenye `getting_started/`.

## Maelekezo ya Majaribio

Endesha majaribio kutoka kwenye mzizi wa hazina. Baadhi ya majaribio yanahitaji kitambulisho cha API; ruka hayo inapobidi.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Ufunikaji wa hiari (inahitaji `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Miongozo ya Mtindo wa Msimbo

- Mpangaji: Black (imesanidiwa kwenye `pyproject.toml`, urefu wa mstari 88)
- Kichunguzi: Ruff (imesanidiwa kwenye `pyproject.toml`, urefu wa mstari 120)
- Ukaguzi wa aina: mypy (mpangilio upo; washa ikiwa imewekwa)

Amri:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Panga vyanzo vya Python chini ya `src/`, majaribio chini ya `tests/`, na pendelea uingizaji wa wazi ndani ya namespace ya kifurushi (`co_op_translator.*`).

## Ujenzi na Uchapishaji

Bidhaa za ujenzi zinachapishwa kwenye `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Uendeshaji kiotomatiki kupitia GitHub Actions unapatikana; angalia:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Picha ya Kontena (GHCR)

- Picha rasmi: `ghcr.io/azure/co-op-translator:<tag>`
- Tag: `latest` (kwenye main), tag za semantic kama `vX.Y.Z`, na tag ya `sha`
- Multi-arch: `linux/amd64, linux/arm64` zinasaidiwa kupitia Buildx
- Muundo wa Dockerfile: jenga magurudumu ya utegemezi kwenye builder (na `build-essential` na `python3-dev`) na usakinishe kutoka kwenye wheelhouse ya ndani kwenye runtime (`pip install --no-index --find-links=/wheels`)
- Mtiririko: `.github/workflows/docker-publish.yml` inajenga na kusukuma kwenye GHCR

## Mambo ya Usalama

- Weka API keys na endpoints kwenye `.env` au hifadhi ya siri ya CI yako; usiwahi kuweka siri kwenye commit.
- Kwa tafsiri ya picha, funguo/viunganishi vya Azure AI Vision vinahitajika; vinginevyo acha kutumia `-img`.
- Hakiki mipaka ya mtoa huduma/viwango vya matumizi unapofanya tafsiri nyingi kwa wakati mmoja.

## Miongozo ya Pull Request

### Kabla ya Kutuma

1. **Jaribu mabadiliko yako:**
   - Endesha daftari husika lote
   - Hakikisha seli zote zinafanya kazi bila makosa
   - Angalia matokeo yanafaa

2. **Mabadiliko ya nyaraka:**
   - Sasisha `README.md` ukiongeza dhana mpya
   - Ongeza maelezo kwenye daftari kwa msimbo mgumu
   - Hakikisha seli za markdown zinaeleza madhumuni

3. **Mabadiliko ya faili:**
   - Epuka kuweka faili za `.env` (tumia `.env.example`)
   - Usikomishe `venv/` au folda za `__pycache__/`
   - Weka matokeo ya daftari pale yanapoonyesha dhana
   - Ondoa faili za muda na daftari za backup (`*-backup.ipynb`)

4. **Mtindo na mpangilio:**
   - Fuata miongozo ya mtindo na mpangilio
   - Endesha `poetry run black .` na `poetry run ruff check .` kuangalia masuala ya mtindo na mpangilio

5. **Ongeza/sasisha majaribio na msaada wa CLI:**
   - Ongeza au sasisha majaribio unapobadilisha tabia
   - Hakikisha msaada wa CLI unalingana na mabadiliko


### Ujumbe wa commit na mkakati wa kuunganisha

Tunatumia Squash and Merge kama chaguo-msingi. Ujumbe wa mwisho wa squash commit unapaswa kufuata:

```bash
<type>: <description> (#<PR number>)
```

Aina zinazokubalika:
- `Docs` — masasisho ya nyaraka
- `Build` — mfumo wa ujenzi, utegemezi, mipangilio/CI
- `Core` — utendaji na vipengele vya msingi (mfano, `src/co_op_translator/core`)

Mifano:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Maelezo:
- Vichwa vya PR mara nyingi huwekwa kiotomatiki kulingana na lebo; hakiki kiambishi kilichotengenezwa ni sahihi.

### Muundo wa Kichwa cha PR

Tumia vichwa wazi na vifupi. Pendelea muundo sawa na wa squash commit ya mwisho:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Utatuzi na Urekebishaji wa Matatizo

- Masuala ya kawaida na suluhisho: `getting_started/troubleshooting.md`
- Lugha zinazosaidiwa na maelezo (pamoja na fonti/masuala yanayojulikana): `getting_started/supported-languages.md`
- Kwa masuala ya viungo kwenye daftari, endesha tena: `migrate-links -l "all" -y`

## Maelezo kwa Mawakala

- Pendelea Poetry kwa mazingira yanayorudiwa; vinginevyo tumia `requirements.txt`.
- Unapotumia CLI kwenye CI, toa siri zinazohitajika kupitia vigezo vya mazingira au `.env` injection.
- Kwa watumiaji wa monorepo, hazina hii inafanya kazi kama kifurushi pekee; hakuna uratibu wa sub-package unaohitajika.

- Mwongozo wa multi-arch: weka `linux/arm64` pale watumiaji wa ARM (Apple Silicon/ARM servers) ni lengo; vinginevyo `linux/amd64` pekee inatosha kwa urahisi.
- Elekeza watumiaji kwenye Docker Quick Start kwenye `README.md` pale wanapopendelea kutumia kontena; jumuisha matoleo ya Bash na PowerShell kutokana na tofauti za nukuu.

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo rasmi. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.