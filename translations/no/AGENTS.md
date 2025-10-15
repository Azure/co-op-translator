<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:29:03+00:00",
  "source_file": "AGENTS.md",
  "language_code": "no"
}
-->
## Prosjektoversikt

Co‑op Translator er et Python-kommandolinjeverktøy og en GitHub Actions-arbeidsflyt som oversetter Markdown-filer, Jupyter-notatbøker og bildetekst til flere språk. Den organiserer utdata under språkspesifikke mapper og holder oversettelser synkronisert med kildeinnholdet. Prosjektet er strukturert som et Poetry-administrert bibliotek med CLI-inngangspunkter.

### Arkitekturoversikt

- CLI-inngangspunkter (`translate`, `migrate-links`, `evaluate`) kaller et samlet CLI som sender videre til oversettelse, lenkemigrering og evalueringsflyter.
- Konfigurasjonslaster leser `.env` og autodetekterer LLM-leverandøren (Azure OpenAI eller OpenAI) og, hvis ønsket, visjonstjenesten (Azure AI Service) for tekstuttrekk fra bilder.
- Oversettelseskjernen håndterer Markdown og notatbøker; visjonspipelinen trekker ut tekst fra bilder når `-img` brukes.
- Utdata organiseres i `translations/<lang>/` for tekst og `translated_images/` for bilder, og bevarer den opprinnelige strukturen.

### Viktige teknologier og rammeverk

- Python 3.10–3.12, Poetry for pakking
- CLI: `click`
- LLM/AI SDKer: Azure OpenAI, OpenAI
- Visjon: Azure AI Service (Computer Vision)
- HTTP og data: `httpx`, `pydantic`
- Bildebehandling: `pillow`, `opencv-python`, `matplotlib`
- Verktøy: `pytest`, `black`, `ruff`

## Oppsettkommandoer

### Forutsetninger

- Python 3.10–3.12
- Azure-abonnement (valgfritt, for Azure AI-tjenester)
- Internett-tilgang for LLM/Visjon-APIer (f.eks. Azure OpenAI/OpenAI, Azure AI Vision)

### Alternativ A: Poetry (anbefalt)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Alternativ B: pip/venv

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

## Bruk for sluttbruker

### Docker (publisert image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Notater:
- Standard entrypoint er `translate`. Overstyr med `--entrypoint migrate-links` for lenkemigrering.
- Sørg for at GHCR-pakkesynlighet er satt til Public for anonyme nedlastinger.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Miljøkonfigurasjon

Lag en `.env`-fil i rotmappen til depotet og oppgi legitimasjon/endepunkter for valgt språkmodell og (valgfritt) visjonstjeneste. For leverandørspesifikk oppsett, se `getting_started/set-up-azure-ai.md`.

### Påkrevde miljøvariabler

Minst én LLM-leverandør må konfigureres. For bildeoversettelse må også Azure AI Service konfigureres.

- Azure OpenAI (tekstoversettelse):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativ for tekstoversettelse):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (valgfritt)
  - `OPENAI_CHAT_MODEL_ID` (påkrevd ved bruk av OpenAI-leverandør)
  - `OPENAI_BASE_URL` (valgfritt; standard er `https://api.openai.com/v1`)

- Azure AI Service for tekstuttrekk fra bilder (påkrevd ved bruk av `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (foretrukket) eller eldre `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Eksempel på `.env`-utdrag:

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

Notater:

- Verktøyet autodetekterer tilgjengelig LLM-leverandør; konfigurer enten Azure OpenAI eller OpenAI.
- Bildeoversettelse krever både `AZURE_AI_SERVICE_API_KEY` og `AZURE_AI_SERVICE_ENDPOINT`.
- CLI vil gi en tydelig feilmelding hvis nødvendige variabler mangler.

## Utviklingsflyt

- Kildekoden ligger under `src/co_op_translator`; tester under `tests/`.
- Primære CLI-er (installert via entry points):

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

Se mer brukerdokumentasjon i `getting_started/`.

## Testinstruksjoner

Kjør tester fra rotmappen til depotet. Noen tester kan kreve API-legitimasjon; hopp over disse ved behov.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Valgfri dekning (krever `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Retningslinjer for kodestil

- Formatter: Black (konfigurert i `pyproject.toml`, linjelengde 88)
- Linter: Ruff (konfigurert i `pyproject.toml`, linjelengde 120)
- Typekontroll: mypy (konfigurasjon tilstede; aktiver hvis installert)

Kommandoer:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organiser Python-kilde under `src/`, tester under `tests/`, og foretrekk eksplisitte importer innenfor pakkenavnet (`co_op_translator.*`).

## Bygg og distribusjon

Byggartefakter publiseres til `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatisering via GitHub Actions støttes; se:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container-image (GHCR)

- Offisielt image: `ghcr.io/azure/co-op-translator:<tag>`
- Tagger: `latest` (på main), semantiske tagger som `vX.Y.Z`, og en `sha`-tag
- Multi-arch: `linux/amd64, linux/arm64` støttes via Buildx
- Dockerfile-mønster: bygg avhengighetshjul i builder (med `build-essential` og `python3-dev`) og installer fra lokal wheelhouse i runtime (`pip install --no-index --find-links=/wheels`)
- Arbeidsflyt: `.github/workflows/docker-publish.yml` bygger og pusher til GHCR

## Sikkerhetsbetraktninger

- Hold API-nøkler og endepunkter i `.env` eller din CI-sekretlagring; aldri legg inn hemmeligheter i depotet.
- For bildeoversettelse kreves Azure AI Vision-nøkler/endepunkter; ellers utelat `-img`.
- Sjekk leverandørens kvoter/rate-limiter ved store oversettelsesjobber.

## Retningslinjer for Pull Request

### Før innsending

1. **Test endringene dine:**
   - Kjør berørte notatbøker helt ut
   - Sjekk at alle celler kjører uten feil
   - Kontroller at utdataene er riktige

2. **Dokumentasjonsoppdateringer:**
   - Oppdater `README.md` hvis du legger til nye konsepter
   - Legg til kommentarer i notatbøker for kompleks kode
   - Sørg for at markdown-celler forklarer hensikten

3. **Filendringer:**
   - Unngå å legge inn `.env`-filer (bruk `.env.example`)
   - Ikke legg inn `venv/` eller `__pycache__/`-mapper
   - Behold notatbokutdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notatbøker (`*-backup.ipynb`)

4. **Stil og formatering:**
   - Følg stil- og formateringsretningslinjene
   - Kjør `poetry run black .` og `poetry run ruff check .` for å sjekke stil og formatering

5. **Legg til/oppdater tester og CLI-hjelp:**
   - Legg til eller oppdater tester ved endret funksjonalitet
   - Hold CLI-hjelpen oppdatert med endringer


### Commit-melding og flettestrategi

Vi bruker Squash and Merge som standard. Den endelige squash-commit-meldingen skal følge:

```bash
<type>: <description> (#<PR number>)
```

Tillatte typer:
- `Docs` — dokumentasjonsoppdateringer
- `Build` — byggsystem, avhengigheter, konfigurasjon/CI
- `Core` — kjernefunksjonalitet og funksjoner (f.eks. `src/co_op_translator/core`)

Eksempler:
- `Docs: Oppdater installasjonsinstruksjoner for klarhet (#50)`
- `Core: Forbedre håndtering av bildeoversettelse (#60)`

Notater:
- PR-titler får ofte automatisk prefiks basert på etiketter; sjekk at generert prefiks er korrekt.

### PR-tittelformat

Bruk tydelige, konsise titler. Foretrekk samme struktur som den endelige squash-commit:
- `Docs: Oppdater installasjonsinstruksjoner for klarhet`
- `Core: Forbedre håndtering av bildeoversettelse`

## Feilsøking og problemløsning

- Vanlige problemer og løsninger: `getting_started/troubleshooting.md`
- Støttede språk og notater (inkludert fonter/kjente problemer): `getting_started/supported-languages.md`
- For lenkeproblemer i notatbøker, kjør på nytt: `migrate-links -l "all" -y`

## Notater for agenter

- Foretrekk Poetry for reproduserbare miljøer; bruk ellers `requirements.txt`.
- Når CLI-er kjøres i CI, oppgi nødvendige hemmeligheter via miljøvariabler eller `.env`-injeksjon.
- For monorepo-brukere fungerer dette depotet som en frittstående pakke; ingen koordinering av underpakker er nødvendig.

- Multi-arch-veiledning: behold `linux/arm64` når ARM-brukere (Apple Silicon/ARM-servere) er målgruppen; ellers er kun `linux/amd64` akseptabelt for enkelhetens skyld.
- Vis brukere til Docker Quick Start i `README.md` hvis de foretrekker containerbruk; inkluder både Bash- og PowerShell-varianter på grunn av forskjeller i anførselstegn.

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.