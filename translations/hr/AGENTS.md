<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:34:44+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hr"
}
-->
# AGENTS.md

## Pregled projekta

Co‑op Translator je Python alat za komandnu liniju i GitHub Actions workflow koji prevodi Markdown datoteke, Jupyter bilježnice i tekst sa slika na više jezika. Organizira izlazne podatke u mape po jezicima i održava prijevode usklađenima s izvornim sadržajem. Projekt je strukturiran kao knjižnica pod upravljanjem Poetryja s CLI ulaznim točkama.

### Pregled arhitekture

- CLI ulazne točke (`translate`, `migrate-links`, `evaluate`) pozivaju objedinjeni CLI koji usmjerava na tokove za prijevod, migraciju linkova i evaluaciju.
- Loader konfiguracije učitava `.env` i automatski detektira LLM pružatelja (Azure OpenAI ili OpenAI) te, ako je zatraženo, vision pružatelja (Azure AI Service) za ekstrakciju teksta sa slika.
- Jezgra za prijevod obrađuje Markdown i bilježnice; vision pipeline izvlači tekst sa slika kad se koristi `-img`.
- Izlazni podaci organizirani su u `translations/<lang>/` za tekst i `translated_images/` za slike, uz očuvanje izvorne strukture.

### Ključne tehnologije i okviri

- Python 3.10–3.12, Poetry za pakiranje
- CLI: `click`
- LLM/AI SDK-ovi: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP i podaci: `httpx`, `pydantic`
- Obrada slika: `pillow`, `opencv-python`, `matplotlib`
- Alati: `pytest`, `black`, `ruff`

## Instalacijske naredbe

### Preduvjeti

- Python 3.10–3.12
- Azure pretplata (opcionalno, za Azure AI servise)
- Pristup internetu za LLM/Vision API-je (npr. Azure OpenAI/OpenAI, Azure AI Vision)

### Opcija A: Poetry (preporučeno)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opcija B: pip/venv

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

## Korištenje za krajnje korisnike

### Docker (objavljena slika)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Napomene:
- Zadana ulazna točka je `translate`. Za migraciju linkova koristite `--entrypoint migrate-links`.
- Provjerite da je vidljivost GHCR paketa postavljena na Public za anonimno povlačenje.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfiguracija okruženja

Kreirajte `.env` datoteku u korijenu repozitorija i upišite vjerodajnice/endpointove za odabrani jezični model i (opcionalno) vision servis. Za postavke po pružatelju pogledajte `getting_started/set-up-azure-ai.md`.

### Potrebne varijable okruženja

Najmanje jedan LLM pružatelj mora biti konfiguriran. Za prijevod slika potrebno je konfigurirati i Azure AI Service.

- Azure OpenAI (prijevod teksta):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa za prijevod teksta):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opcionalno)
  - `OPENAI_CHAT_MODEL_ID` (obavezno kod korištenja OpenAI pružatelja)
  - `OPENAI_BASE_URL` (opcionalno; zadano je `https://api.openai.com/v1`)

- Azure AI Service za ekstrakciju teksta sa slika (obavezno kod korištenja `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preporučeno) ili staro `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Primjer `.env` isječka:

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

Napomene:

- Alat automatski detektira dostupnog LLM pružatelja; konfigurirajte Azure OpenAI ili OpenAI.
- Prijevod slika zahtijeva i `AZURE_AI_SERVICE_API_KEY` i `AZURE_AI_SERVICE_ENDPOINT`.
- CLI će jasno prijaviti grešku ako nedostaju potrebne varijable.

## Razvojni workflow

- Izvorni kod se nalazi pod `src/co_op_translator`; testovi pod `tests/`.
- Glavne CLI naredbe (instalirane putem entry points):

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

Dodatnu dokumentaciju o korištenju pronađite u `getting_started/`.

## Upute za testiranje

Pokrenite testove iz korijena repozitorija. Neki testovi zahtijevaju API vjerodajnice; preskočite ih po potrebi.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Opcionalno izvještavanje o pokrivenosti (zahtijeva `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Smjernice za stil koda

- Formatter: Black (konfiguriran u `pyproject.toml`, duljina linije 88)
- Linter: Ruff (konfiguriran u `pyproject.toml`, duljina linije 120)
- Provjera tipova: mypy (konfiguracija postoji; omogućite ako je instaliran)

Naredbe:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizirajte Python izvore pod `src/`, testove pod `tests/`, i preferirajte eksplicitne uvoze unutar package namespace-a (`co_op_translator.*`).

## Izgradnja i objava

Izgradbeni artefakti objavljuju se u `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatizacija putem GitHub Actions je podržana; pogledajte:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Kontejnerska slika (GHCR)

- Službena slika: `ghcr.io/azure/co-op-translator:<tag>`
- Tagovi: `latest` (na mainu), semantički tagovi poput `vX.Y.Z`, te `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` podržano putem Buildx
- Dockerfile obrazac: gradnja dependency wheelova u builderu (s `build-essential` i `python3-dev`) i instalacija iz lokalnog wheelhouse-a u runtimeu (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` gradi i šalje na GHCR

## Sigurnosne napomene

- API ključeve i endpointove držite u `.env` ili CI secrets storeu; nikad ne komitirajte tajne.
- Za prijevod slika potrebni su Azure AI Vision ključevi/endpointi; inače izostavite `-img`.
- Provjerite kvote/pragove pružatelja kod velikih batch prijevoda.

## Smjernice za Pull Requestove

### Prije slanja

1. **Testirajte promjene:**
   - Pokrenite sve relevantne bilježnice do kraja
   - Provjerite da se sve ćelije izvršavaju bez grešaka
   - Provjerite da su izlazi prikladni

2. **Ažuriranje dokumentacije:**
   - Ažurirajte `README.md` ako dodajete nove koncepte
   - Dodajte komentare u bilježnice za složen kod
   - Osigurajte da markdown ćelije objašnjavaju svrhu

3. **Promjene datoteka:**
   - Izbjegavajte komitiranje `.env` datoteka (koristite `.env.example`)
   - Ne komitirajte `venv/` ili `__pycache__/` direktorije
   - Zadržite izlaze iz bilježnica kad demonstriraju koncepte
   - Uklonite privremene datoteke i backup bilježnice (`*-backup.ipynb`)

4. **Stil i formatiranje:**
   - Pridržavajte se smjernica za stil i formatiranje
   - Pokrenite `poetry run black .` i `poetry run ruff check .` za provjeru stila i formatiranja

5. **Dodajte/ažurirajte testove i CLI help:**
   - Dodajte ili ažurirajte testove kod promjene ponašanja
   - Održavajte CLI help u skladu s promjenama


### Format commit poruke i strategija spajanja

Koristimo Squash and Merge kao zadano. Završna squash commit poruka treba slijediti:

```bash
<type>: <description> (#<PR number>)
```

Dozvoljeni tipovi:
- `Docs` — ažuriranja dokumentacije
- `Build` — build sustav, ovisnosti, konfiguracija/CI
- `Core` — osnovna funkcionalnost i značajke (npr. `src/co_op_translator/core`)

Primjeri:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Napomene:
- Naslovi PR-a često se automatski prefiksiraju prema labelama; provjerite da je generirani prefiks ispravan.

### Format naslova PR-a

Koristite jasne, sažete naslove. Preferirajte isti format kao završni squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging i rješavanje problema

- Uobičajeni problemi i rješenja: `getting_started/troubleshooting.md`
- Podržani jezici i napomene (uključujući fontove/poznate probleme): `getting_started/supported-languages.md`
- Za probleme s linkovima u bilježnicama, ponovno pokrenite: `migrate-links -l "all" -y`

## Napomene za agente

- Preferirajte Poetry za reproducibilna okruženja; inače koristite `requirements.txt`.
- Kod pokretanja CLI-a u CI-u, osigurajte potrebne tajne putem varijabli okruženja ili `.env` injekcije.
- Za korisnike monorepoa, ovaj repo je samostalni paket; nije potrebna koordinacija podpaketa.

- Multi-arch smjernice: zadržite `linux/arm64` kad su ARM korisnici (Apple Silicon/ARM serveri) cilj; inače je samo `linux/amd64` prihvatljivo radi jednostavnosti.
- Uputite korisnike na Docker Quick Start u `README.md` ako preferiraju korištenje kontejnera; uključite Bash i PowerShell varijante zbog razlika u navodnicima.

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.