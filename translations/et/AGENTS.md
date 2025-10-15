<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:37:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "et"
}
-->
## Projekti ülevaade

Co‑op Translator on Pythonil põhinev käsurea tööriist ja GitHub Actions töövoog, mis tõlgib Markdown-faile, Jupyteri märkmikke ja piltidel olevat teksti mitmesse keelde. Tõlked paigutatakse keelepõhistesse kaustadesse ning hoitakse sünkroonis algsisuga. Projekt on üles ehitatud Poetry abil hallatava teegina, millel on CLI sisendpunktid.

### Arhitektuuri ülevaade

- CLI sisendpunktid (`translate`, `migrate-links`, `evaluate`) kutsuvad välja ühtse CLI, mis suunab tõlke-, lingimigratsiooni- ja hindamisvoogudesse.
- Konfiguratsioonilaadur loeb `.env` faili ja tuvastab automaatselt LLM pakkuja (Azure OpenAI või OpenAI) ning vajadusel ka visiooniteenuse (Azure AI Service) piltidelt teksti eraldamiseks.
- Tõlke tuumik haldab Markdowni ja märkmikke; visioonitoru eraldab teksti piltidelt, kui kasutatakse `-img` lippu.
- Väljundid paigutatakse `translations/<lang>/` (tekst) ja `translated_images/` (pildid) kaustadesse, säilitades algse struktuuri.

### Olulised tehnoloogiad ja raamistikud

- Python 3.10–3.12, Poetry paketihaldus
- CLI: `click`
- LLM/AI SDK-d: Azure OpenAI, OpenAI
- Visioon: Azure AI Service (Computer Vision)
- HTTP ja andmed: `httpx`, `pydantic`
- Pilditöötlus: `pillow`, `opencv-python`, `matplotlib`
- Tööriistad: `pytest`, `black`, `ruff`

## Paigalduskäsud

### Eeldused

- Python 3.10–3.12
- Azure tellimus (valikuline, Azure AI teenuste jaoks)
- Internetiühendus LLM/Visioon API-dele (nt Azure OpenAI/OpenAI, Azure AI Vision)

### Variant A: Poetry (soovitatav)

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

## Lõppkasutaja kasutus

### Docker (avalik pilt)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Märkused:
- Vaikimisi sisendpunkt on `translate`. Lingimigratsiooni jaoks kasuta `--entrypoint migrate-links`.
- Veendu, et GHCR pakett oleks avalik, et anonüümsed tõmbamised toimiksid.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Keskkonna seadistamine

Loo `.env` fail repo juurkausta ja lisa valitud keelemudeli ning (soovi korral) visiooniteenuse mandaadid/endpointid. Pakkuja-põhise seadistuse kohta vaata `getting_started/set-up-azure-ai.md`.

### Vajalikud keskkonnamuutujad

Vähemalt üks LLM pakkuja peab olema seadistatud. Piltide tõlkimiseks peab olema seadistatud ka Azure AI Service.

- Azure OpenAI (teksttõlge):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (teksttõlke alternatiiv):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (valikuline)
  - `OPENAI_CHAT_MODEL_ID` (nõutav OpenAI pakkuja kasutamisel)
  - `OPENAI_BASE_URL` (valikuline; vaikimisi `https://api.openai.com/v1`)

- Azure AI Service piltidelt teksti eraldamiseks (nõutav `-img` kasutamisel):
  - `AZURE_AI_SERVICE_API_KEY` (soovitatav) või vana `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Näidis `.env` lõik:

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

Märkused:

- Tööriist tuvastab automaatselt saadaoleva LLM pakkuja; seadista kas Azure OpenAI või OpenAI.
- Piltide tõlkimiseks on vaja nii `AZURE_AI_SERVICE_API_KEY` kui ka `AZURE_AI_SERVICE_ENDPOINT`.
- CLI annab selge veateate, kui vajalikud muutujad puuduvad.

## Arendusvoog

- Lähtekood asub `src/co_op_translator` kaustas; testid `tests/` kaustas.
- Peamised CLI-d (paigaldatakse sisendpunktidena):

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

Vaata täiendavaid kasutusjuhendeid `getting_started/` kaustast.

## Testimise juhised

Käivita testid repo juurest. Mõned testid võivad vajada API mandaate; vajadusel jäta need vahele.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Valikuline katvus (vajab `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Koodistiili juhised

- Vormindaja: Black (`pyproject.toml` failis, rea pikkus 88)
- Linter: Ruff (`pyproject.toml` failis, rea pikkus 120)
- Tüübikontroll: mypy (konfiguratsioon olemas; lülita sisse, kui paigaldatud)

Käsud:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Paiguta Python allikad `src/` kausta, testid `tests/` kausta ja eelista selgeid imporditeid paketi nimeruumis (`co_op_translator.*`).

## Ehitamine ja juurutamine

Ehituse artefaktid avaldatakse `dist/` kausta.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatiseerimine GitHub Actions abil on toetatud; vaata:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Konteinerpilt (GHCR)

- Ametlik pilt: `ghcr.io/azure/co-op-translator:<tag>`
- Sildid: `latest` (main harul), semantilised sildid nagu `vX.Y.Z` ja `sha` silt
- Multi-arch: `linux/amd64, linux/arm64` toetatud Buildx abil
- Dockerfile muster: ehita sõltuvuste wheelid builderis (`build-essential` ja `python3-dev`) ning paigalda runtime'is lokaalsest wheelhouse'ist (`pip install --no-index --find-links=/wheels`)
- Töövoog: `.github/workflows/docker-publish.yml` ehitab ja lükkab GHCR-i

## Turvalisuse kaalutlused

- Hoia API võtmed ja endpointid `.env` failis või CI saladuste hoidlas; ära kunagi commiti saladusi.
- Piltide tõlkimiseks on vaja Azure AI Vision võtmeid/endpointi; muul juhul jäta `-img` kasutamata.
- Suurte tõlkepartiide puhul kontrolli pakkuja limiite/kvoote.

## Pull Requesti juhised

### Enne esitamist

1. **Testi oma muudatused:**
   - Käivita mõjutatud märkmikud täielikult
   - Veendu, et kõik lahtrid töötavad veavabalt
   - Kontrolli, et väljundid oleksid asjakohased

2. **Dokumentatsiooni uuendused:**
   - Uuenda `README.md`, kui lisad uusi mõisteid
   - Lisa keerukale koodile kommentaarid märkmikesse
   - Veendu, et markdown lahtrid selgitavad eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide commiteerimist (kasuta `.env.example`)
   - Ära commiti `venv/` või `__pycache__/` kaustu
   - Hoia märkmiku väljundeid, kui need illustreerivad mõisteid
   - Eemalda ajutised failid ja varukoopiad märkmikest (`*-backup.ipynb`)

4. **Stiil ja vormindus:**
   - Järgi stiili- ja vormindusjuhiseid
   - Käivita `poetry run black .` ja `poetry run ruff check .`, et kontrollida stiili ja vormindust

5. **Lisa/uuenda teste ja CLI abi:**
   - Lisa või uuenda teste käitumise muutmisel
   - Hoia CLI abi kooskõlas muudatustega


### Commiti sõnum ja liitmisstrateegia

Kasutame vaikimisi Squash and Merge. Lõplik squash commit'i sõnum peaks olema:

```bash
<type>: <description> (#<PR number>)
```

Lubatud tüübid:
- `Docs` — dokumentatsiooni uuendused
- `Build` — ehitussüsteem, sõltuvused, konfiguratsioon/CI
- `Core` — põhifunktsionaalsus ja omadused (nt `src/co_op_translator/core`)

Näited:
- `Docs: Uuenda paigaldusjuhiseid selguse huvides (#50)`
- `Core: Paranda piltide tõlkimise käsitlemist (#60)`

Märkused:
- PR pealkirjad saavad tihti automaatselt prefiksi siltide põhjal; kontrolli, et genereeritud prefiks oleks õige.

### PR pealkirja formaat

Kasuta selgeid, lühikesi pealkirju. Eelista sama struktuuri nagu lõplik squash commit:
- `Docs: Uuenda paigaldusjuhiseid selguse huvides`
- `Core: Paranda piltide tõlkimise käsitlemist`

## Silumine ja tõrkeotsing

- Levinumad probleemid ja lahendused: `getting_started/troubleshooting.md`
- Toetatud keeled ja märkused (sh fondid/tuntud probleemid): `getting_started/supported-languages.md`
- Märkmiku linkide probleemide korral käivita uuesti: `migrate-links -l "all" -y`

## Märkused agentidele

- Eelista Poetry't reprodutseeritavate keskkondade jaoks; muul juhul kasuta `requirements.txt`.
- CLI-de käivitamisel CI-s anna vajalikud saladused keskkonnamuutujate või `.env` süstimisega.
- Monorepo kasutajatele: see repo toimib iseseisva paketina; alam-pakettide koordineerimine pole vajalik.

- Multi-arch juhis: hoia `linux/arm64`, kui ARM kasutajad (Apple Silicon/ARM serverid) on sihtgrupp; muul juhul piisab lihtsuse huvides ainult `linux/amd64`.
- Suuna kasutajad Docker Quick Start juhendisse `README.md` failis, kui nad eelistavad konteinerkasutust; lisa Bash ja PowerShell variandid, kuna tsiteerimine erineb.

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaattõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või tõlgendamisvigade eest.