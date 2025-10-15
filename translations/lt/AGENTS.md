<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:36:23+00:00",
  "source_file": "AGENTS.md",
  "language_code": "lt"
}
-->
# AGENTS.md

## Projekto apžvalga

Co‑op Translator – tai Python komandinės eilutės įrankis ir GitHub Actions darbo eiga, skirtas Markdown failų, Jupyter užrašų knygų ir paveikslėlių teksto vertimui į kelias kalbas. Vertimai išdėstomi kalbų aplankuose ir sinchronizuojami su pirminiu turiniu. Projektas struktūruotas kaip Poetry valdoma biblioteka su CLI įėjimo taškais.

### Architektūros apžvalga

- CLI įėjimo taškai (`translate`, `migrate-links`, `evaluate`) kviečia vieningą CLI, kuris paskirsto vertimo, nuorodų migravimo ir vertinimo srautus.
- Konfigūracijos įkėlėjas skaito `.env` ir automatiškai aptinka LLM tiekėją (Azure OpenAI arba OpenAI) ir, jei reikia, vaizdo tiekėją (Azure AI Service) paveikslėlių teksto išgavimui.
- Vertimo branduolys apdoroja Markdown ir užrašų knygas; vaizdo pipeline išgauna tekstą iš paveikslėlių, kai naudojamas `-img`.
- Rezultatai išdėstomi `translations/<lang>/` tekstui ir `translated_images/` paveikslėliams, išlaikant pradinę struktūrą.

### Pagrindinės technologijos ir karkasai

- Python 3.10–3.12, Poetry paketavimui
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vaizdas: Azure AI Service (Computer Vision)
- HTTP ir duomenys: `httpx`, `pydantic`
- Vaizdų apdorojimas: `pillow`, `opencv-python`, `matplotlib`
- Įrankiai: `pytest`, `black`, `ruff`

## Diegimo komandos

### Būtinos sąlygos

- Python 3.10–3.12
- Azure prenumerata (neprivaloma, Azure AI paslaugoms)
- Interneto prieiga LLM/Vision API (pvz., Azure OpenAI/OpenAI, Azure AI Vision)

### Variant A: Poetry (rekomenduojama)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Variant B: pip/venv

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

## Naudojimas galutiniam vartotojui

### Docker (publikuotas atvaizdas)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Pastabos:
- Numatytoji įėjimo taškas yra `translate`. Norėdami migruoti nuorodas, naudokite `--entrypoint migrate-links`.
- Įsitikinkite, kad GHCR paketo matomumas yra Public, kad būtų galima anonimiškai atsisiųsti.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Aplinkos konfigūracija

Sukurkite `.env` failą repozitorijos šaknyje ir nurodykite kredencialus/endpointus pasirinktam kalbos modeliui ir (neprivalomai) vaizdo paslaugai. Tiekėjo specifinei konfigūracijai žiūrėkite `getting_started/set-up-azure-ai.md`.

### Būtini aplinkos kintamieji

Bent vienas LLM tiekėjas turi būti sukonfigūruotas. Norint versti paveikslėlius, reikia sukonfigūruoti Azure AI Service.

- Azure OpenAI (teksto vertimas):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatyva teksto vertimui):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (neprivaloma)
  - `OPENAI_CHAT_MODEL_ID` (privaloma naudojant OpenAI tiekėją)
  - `OPENAI_BASE_URL` (neprivaloma; numatyta `https://api.openai.com/v1`)

- Azure AI Service paveikslėlių teksto išgavimui (privaloma naudojant `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (pageidautina) arba senas `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Pavyzdinis `.env` fragmentas:

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

Pastabos:

- Įrankis automatiškai aptinka galimą LLM tiekėją; sukonfigūruokite Azure OpenAI arba OpenAI.
- Paveikslėlių vertimui reikia ir `AZURE_AI_SERVICE_API_KEY`, ir `AZURE_AI_SERVICE_ENDPOINT`.
- CLI aiškiai praneš apie trūkstamus būtinus kintamuosius.

## Programavimo eiga

- Pirminis kodas yra `src/co_op_translator`; testai – `tests/`.
- Pagrindiniai CLI (įdiegiami per entry points):

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

Papildomą naudojimo dokumentaciją rasite `getting_started/`.

## Testavimo instrukcijos

Testus paleiskite iš repozitorijos šaknies. Kai kuriems testams gali reikėti API kredencialų; praleiskite juos, jei reikia.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Papildoma aprėptis (reikia `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Kodo stiliaus gairės

- Formatuotojas: Black (`pyproject.toml`, eilutės ilgis 88)
- Linteris: Ruff (`pyproject.toml`, eilutės ilgis 120)
- Tipų tikrinimas: mypy (konfigūracija yra; įjunkite jei įdiegta)

Komandos:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python kodą laikykite `src/`, testus – `tests/`, ir naudokite aiškius importus paketo vardų erdvėje (`co_op_translator.*`).

## Kompiliavimas ir diegimas

Kompiliavimo artefaktai publikuojami į `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatizavimas per GitHub Actions palaikomas; žiūrėkite:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Konteinerio atvaizdas (GHCR)

- Oficialus atvaizdas: `ghcr.io/azure/co-op-translator:<tag>`
- Žymos: `latest` (pagrindinėje šakoje), semantinės žymos kaip `vX.Y.Z`, ir `sha` žyma
- Multi-arch: `linux/amd64, linux/arm64` palaikoma per Buildx
- Dockerfile modelis: priklausomybių wheel'ų kūrimas builder'yje (su `build-essential` ir `python3-dev`) ir diegimas iš vietinio wheelhouse runtime'e (`pip install --no-index --find-links=/wheels`)
- Darbo eiga: `.github/workflows/docker-publish.yml` kuria ir siunčia į GHCR

## Saugumo aspektai

- API raktus ir endpointus laikykite `.env` arba CI slaptažodžių saugykloje; niekada neįtraukite slaptažodžių į commit'us.
- Paveikslėlių vertimui reikia Azure AI Vision raktų/endpointų; kitu atveju nenaudokite `-img`.
- Patikrinkite tiekėjo kvotas/greičio ribas, kai verčiate didelius kiekius.

## Pull Request gairės

### Prieš pateikiant

1. **Ištestuokite pakeitimus:**
   - Pilnai paleiskite paveiktas užrašų knygas
   - Patikrinkite, kad visos ląstelės vykdomos be klaidų
   - Įsitikinkite, kad rezultatai tinkami

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinkite `README.md`, jei pridedate naujų temų
   - Pridėkite komentarus užrašų knygose sudėtingam kodui
   - Užtikrinkite, kad Markdown ląstelės paaiškina paskirtį

3. **Failų pakeitimai:**
   - Venkite commit'inti `.env` failus (naudokite `.env.example`)
   - Neįtraukite `venv/` ar `__pycache__/` katalogų
   - Palikite užrašų knygų rezultatus, jei jie demonstruoja koncepcijas
   - Pašalinkite laikinus failus ir atsargines užrašų knygas (`*-backup.ipynb`)

4. **Stilius ir formatavimas:**
   - Laikykitės stiliaus ir formatavimo gairių
   - Paleiskite `poetry run black .` ir `poetry run ruff check .`, kad patikrintumėte stilių ir formatavimą

5. **Pridėkite/atnaujinkite testus ir CLI pagalbą:**
   - Pridėkite arba atnaujinkite testus, jei keičiate elgseną
   - CLI pagalbą palaikykite nuoseklią su pakeitimais


### Commit žinutė ir sujungimo strategija

Naudojame Squash and Merge kaip numatytąjį. Galutinė squash commit žinutė turi būti tokia:

```bash
<type>: <description> (#<PR number>)
```

Leistini tipai:
- `Docs` — dokumentacijos atnaujinimai
- `Build` — build sistema, priklausomybės, konfigūracija/CI
- `Core` — pagrindinė funkcionalumas ir ypatybės (pvz., `src/co_op_translator/core`)

Pavyzdžiai:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Pastabos:
- PR pavadinimai dažnai automatiškai pažymimi pagal etiketes; patikrinkite, ar sugeneruotas prefiksas teisingas.

### PR pavadinimo formatas

Naudokite aiškius, glaustus pavadinimus. Rekomenduojama ta pati struktūra kaip galutinėje squash commit žinutėje:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Derinimas ir trikčių šalinimas

- Dažniausios problemos ir sprendimai: `getting_started/troubleshooting.md`
- Palaikomos kalbos ir pastabos (įskaitant šriftus/žinomas problemas): `getting_started/supported-languages.md`
- Dėl nuorodų problemų užrašų knygose paleiskite: `migrate-links -l "all" -y`

## Pastabos agentams

- Rekomenduojama naudoti Poetry dėl atkartojamų aplinkų; kitu atveju naudokite `requirements.txt`.
- Kai CLI kviečiami CI, būtinus slaptažodžius pateikite per aplinkos kintamuosius arba `.env` injekciją.
- Monorepo vartotojams šis repo veikia kaip atskiras paketas; nereikia koordinuoti sub-paketų.

- Multi-arch rekomendacija: laikykite `linux/arm64`, jei taikote ARM vartotojams (Apple Silicon/ARM serveriai); kitu atveju paprastumui pakanka tik `linux/amd64`.
- Vartotojams, pageidaujantiems konteinerio naudojimo, nukreipkite į Docker Quick Start `README.md`; pateikite Bash ir PowerShell variantus dėl skirtumų kabutėse.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.