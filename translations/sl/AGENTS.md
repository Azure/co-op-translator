<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:35:06+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sl"
}
-->
## Pregled projekta

Co‑op Translator je orodje za prevajanje v ukazni vrstici Python in GitHub Actions potek, ki prevaja Markdown datoteke, Jupyter zvezke in besedilo na slikah v več jezikov. Izhode organizira v jezikovno specifične mape in ohranja prevode usklajene z izvirno vsebino. Projekt je strukturiran kot knjižnica, upravljana s Poetry, z vstopnimi točkami CLI.

### Pregled arhitekture

- Vstopne točke CLI (`translate`, `migrate-links`, `evaluate`) kličejo enoten CLI, ki usmerja v prevajalske, migracijske in evalvacijske tokove.
- Nalagalnik konfiguracije prebere `.env` in samodejno zazna ponudnika LLM (Azure OpenAI ali OpenAI) ter, če je zahtevano, ponudnika za vizijo (Azure AI Service) za ekstrakcijo besedila s slik.
- Jedro za prevajanje obravnava Markdown in zvezke; vizualna cevovodna veriga izlušči besedilo s slik, ko je uporabljen `-img`.
- Izhodi so organizirani v `translations/<lang>/` za besedilo in `translated_images/` za slike, pri čemer se ohrani izvirna struktura.

### Ključne tehnologije in ogrodja

- Python 3.10–3.12, Poetry za pakiranje
- CLI: `click`
- LLM/AI SDK-ji: Azure OpenAI, OpenAI
- Vizija: Azure AI Service (Computer Vision)
- HTTP in podatki: `httpx`, `pydantic`
- Obdelava slik: `pillow`, `opencv-python`, `matplotlib`
- Orodja: `pytest`, `black`, `ruff`

## Namestitveni ukazi

### Predpogoji

- Python 3.10–3.12
- Azure naročnina (neobvezno, za Azure AI storitve)
- Dostop do interneta za LLM/Vision API-je (npr. Azure OpenAI/OpenAI, Azure AI Vision)

### Možnost A: Poetry (priporočeno)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Možnost B: pip/venv

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

## Uporaba za končne uporabnike

### Docker (objavljena slika)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Opombe:
- Privzeta vstopna točka je `translate`. Prepišite z `--entrypoint migrate-links` za migracijo povezav.
- Prepričajte se, da je vidnost GHCR paketa nastavljena na Public za anonimne prenose.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfiguracija okolja

Ustvarite datoteko `.env` v korenu repozitorija in vnesite poverilnice/končne točke za izbran jezikovni model in (po želji) storitev za vizijo. Za nastavitev po ponudniku glejte `getting_started/set-up-azure-ai.md`.

### Zahtevane okoljske spremenljivke

Vsaj en ponudnik LLM mora biti konfiguriran. Za prevajanje slik mora biti konfigurirana tudi Azure AI Service.

- Azure OpenAI (prevajanje besedila):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa za prevajanje besedila):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (neobvezno)
  - `OPENAI_CHAT_MODEL_ID` (obvezno pri uporabi OpenAI ponudnika)
  - `OPENAI_BASE_URL` (neobvezno; privzeto `https://api.openai.com/v1`)

- Azure AI Service za ekstrakcijo besedila s slik (obvezno pri uporabi `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (priporočeno) ali zastareli `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Primer izseka `.env`:

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

Opombe:

- Orodje samodejno zazna razpoložljivega ponudnika LLM; konfigurirajte bodisi Azure OpenAI ali OpenAI.
- Prevajanje slik zahteva tako `AZURE_AI_SERVICE_API_KEY` kot `AZURE_AI_SERVICE_ENDPOINT`.
- CLI bo izpisal jasno napako, če manjkajo zahtevane spremenljivke.

## Razvojni potek dela

- Izvorna koda je v `src/co_op_translator`; testi v `tests/`.
- Glavne CLI (nameščene prek vstopnih točk):

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

Dodatna navodila za uporabo so v `getting_started/`.

## Navodila za testiranje

Testiranje zaženite iz korena repozitorija. Nekateri testi zahtevajo API poverilnice; te preskočite po potrebi.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Neobvezno poročilo o pokritosti (zahteva `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Smernice za slog kode

- Oblikovalnik: Black (nastavljen v `pyproject.toml`, dolžina vrstice 88)
- Linter: Ruff (nastavljen v `pyproject.toml`, dolžina vrstice 120)
- Preverjanje tipov: mypy (konfiguracija prisotna; omogočite, če je nameščen)

Ukazi:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizirajte Python izvorno kodo pod `src/`, teste pod `tests/`, in dajte prednost eksplicitnim uvozom znotraj imenskega prostora paketa (`co_op_translator.*`).

## Gradnja in objava

Gradbeni artefakti so objavljeni v `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Avtomatizacija prek GitHub Actions je podprta; glejte:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Kontejnerska slika (GHCR)

- Uradna slika: `ghcr.io/azure/co-op-translator:<tag>`
- Oznake: `latest` (na main), semantične oznake kot `vX.Y.Z` in oznaka `sha`
- Multi-arch: `linux/amd64, linux/arm64` podprto prek Buildx
- Vzorec Dockerfile: gradnja odvisnostnih wheelov v builderju (z `build-essential` in `python3-dev`) in namestitev iz lokalnega wheelhouse v runtime (`pip install --no-index --find-links=/wheels`)
- Potek: `.github/workflows/docker-publish.yml` gradi in potiska v GHCR

## Varnostni vidiki

- API ključe in končne točke hranite v `.env` ali v shrambi skrivnosti CI; nikoli ne objavljajte skrivnosti.
- Za prevajanje slik so potrebni Azure AI Vision ključi/končne točke; sicer izpustite `-img`.
- Preverite kvote/omejitve ponudnika pri večjih serijah prevodov.

## Smernice za Pull Requeste

### Pred oddajo

1. **Preizkusite spremembe:**
   - Popolnoma zaženite spremenjene zvezke
   - Preverite, da se vse celice izvedejo brez napak
   - Preverite, da so izhodi ustrezni

2. **Posodobitve dokumentacije:**
   - Posodobite `README.md`, če dodajate nove koncepte
   - Dodajte komentarje v zvezke za kompleksno kodo
   - Poskrbite, da markdown celice pojasnjujejo namen

3. **Spremembe datotek:**
   - Izogibajte se objavi `.env` datotek (uporabite `.env.example`)
   - Ne objavljajte map `venv/` ali `__pycache__/`
   - Ohranite izhode v zvezkih, če prikazujejo koncepte
   - Odstranite začasne datoteke in varnostne kopije zvezkov (`*-backup.ipynb`)

4. **Slog in oblikovanje:**
   - Upoštevajte smernice za slog in oblikovanje
   - Zaženite `poetry run black .` in `poetry run ruff check .` za preverjanje sloga in oblikovanja

5. **Dodajte/posodobite teste in pomoč CLI:**
   - Dodajte ali posodobite teste ob spremembi vedenja
   - Ohranjajte CLI pomoč usklajeno s spremembami


### Sporočilo commita in strategija združevanja

Uporabljamo Squash and Merge kot privzeto. Končno squash sporočilo commita naj sledi:

```bash
<type>: <description> (#<PR number>)
```

Dovoljene vrste:
- `Docs` — posodobitve dokumentacije
- `Build` — gradbeni sistem, odvisnosti, konfiguracija/CI
- `Core` — osnovna funkcionalnost in funkcije (npr. `src/co_op_translator/core`)

Primeri:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Opombe:
- Naslovi PR-jev so pogosto samodejno predznačeni glede na oznake; preverite, da je generirana predpona pravilna.

### Oblika naslova PR

Uporabljajte jasne, jedrnate naslove. Prednost dajte isti strukturi kot končno squash sporočilo:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Odpravljanje napak in težav

- Pogoste težave in rešitve: `getting_started/troubleshooting.md`
- Podprti jeziki in opombe (vključno s pisavami/znanimi težavami): `getting_started/supported-languages.md`
- Za težave s povezavami v zvezkih ponovno zaženite: `migrate-links -l "all" -y`

## Opombe za agente

- Prednost dajte Poetry za ponovljive okolja; sicer uporabite `requirements.txt`.
- Pri klicanju CLI v CI zagotovite zahtevane skrivnosti prek okoljskih spremenljivk ali injiciranja `.env`.
- Za uporabnike monorepo ta repozitorij deluje kot samostojen paket; ni potrebna koordinacija s podpaketi.

- Smernice za multi-arch: ohranite `linux/arm64`, če ciljate na ARM uporabnike (Apple Silicon/ARM strežniki); sicer je za enostavnost dovolj le `linux/amd64`.
- Uporabnike usmerite na Docker Quick Start v `README.md`, če želijo uporabljati kontejner; vključite Bash in PowerShell različice zaradi razlik v narekovajih.

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.