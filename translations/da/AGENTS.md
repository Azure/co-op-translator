<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:28:41+00:00",
  "source_file": "AGENTS.md",
  "language_code": "da"
}
-->
# AGENTS.md

## Projektoversigt

Co‑op Translator er et Python-kommandolinjeværktøj og en GitHub Actions workflow, der oversætter Markdown-filer, Jupyter-notebooks og billedtekst til flere sprog. Den organiserer output i sprog-specifikke mapper og holder oversættelser synkroniseret med kildeindholdet. Projektet er struktureret som et Poetry-administreret bibliotek med CLI-entry points.

### Arkitektur-oversigt

- CLI-entry points (`translate`, `migrate-links`, `evaluate`) kalder en samlet CLI, der fordeler til oversættelse, link-migrering og evalueringsflows.
- Konfigurationsindlæser læser `.env` og autodetekterer LLM-udbyderen (Azure OpenAI eller OpenAI) og, hvis ønsket, vision-udbyderen (Azure AI Service) til billedtekst-udtræk.
- Oversættelseskernen håndterer Markdown og notebooks; vision-pipelinen udtrækker tekst fra billeder, når `-img` bruges.
- Output organiseres i `translations/<lang>/` for tekst og `translated_images/` for billeder, hvor den oprindelige struktur bevares.

### Centrale teknologier og frameworks

- Python 3.10–3.12, Poetry til pakkehåndtering
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP og data: `httpx`, `pydantic`
- Billedbehandling: `pillow`, `opencv-python`, `matplotlib`
- Værktøjer: `pytest`, `black`, `ruff`

## Opsætningskommandoer

### Forudsætninger

- Python 3.10–3.12
- Azure-abonnement (valgfrit, til Azure AI-tjenester)
- Internetadgang til LLM/Vision-API'er (fx Azure OpenAI/OpenAI, Azure AI Vision)

### Mulighed A: Poetry (anbefalet)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Mulighed B: pip/venv

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

## Slutbruger-brug

### Docker (officielt image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Bemærkninger:
- Standard-entrypoint er `translate`. Brug `--entrypoint migrate-links` for link-migrering.
- Sørg for, at GHCR-pakkens synlighed er Public for anonyme pulls.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Miljøkonfiguration

Opret en `.env`-fil i roden af repoet og angiv credentials/endpoints til din valgte sprogmodel og (valgfrit) vision-tjeneste. For udbyderspecifik opsætning, se `getting_started/set-up-azure-ai.md`.

### Påkrævede miljøvariabler

Mindst én LLM-udbyder skal konfigureres. Til billedoversættelse skal Azure AI Service også konfigureres.

- Azure OpenAI (tekstoversættelse):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativ til tekstoversættelse):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (valgfri)
  - `OPENAI_CHAT_MODEL_ID` (påkrævet ved brug af OpenAI-udbyder)
  - `OPENAI_BASE_URL` (valgfri; standard er `https://api.openai.com/v1`)

- Azure AI Service til billedtekst-udtræk (påkrævet ved brug af `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (foretrukket) eller ældre `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Eksempel på `.env`-udsnit:

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

Bemærkninger:

- Værktøjet autodetekterer den tilgængelige LLM-udbyder; konfigurer enten Azure OpenAI eller OpenAI.
- Billedoversættelse kræver både `AZURE_AI_SERVICE_API_KEY` og `AZURE_AI_SERVICE_ENDPOINT`.
- CLI'en vil give en tydelig fejl, hvis påkrævede variabler mangler.

## Udviklingsworkflow

- Kildekoden ligger under `src/co_op_translator`; tests under `tests/`.
- Primære CLI'er (installeret via entry points):

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

Se yderligere brugervejledninger i `getting_started/`.

## Testvejledning

Kør tests fra roden af repoet. Nogle tests kræver API-credentials; spring dem over efter behov.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Valgfri coverage (kræver `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Kodestil-retningslinjer

- Formatter: Black (konfigureret i `pyproject.toml`, linjelængde 88)
- Linter: Ruff (konfigureret i `pyproject.toml`, linjelængde 120)
- Typechecks: mypy (konfiguration til stede; aktiver hvis installeret)

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

Organisér Python-kilde under `src/`, tests under `tests/`, og foretræk eksplicitte imports inden for pakkenavnerummet (`co_op_translator.*`).

## Build og deployment

Build-artifacts udgives til `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatisering via GitHub Actions understøttes; se:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container-image (GHCR)

- Officielt image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (på main), semantiske tags som `vX.Y.Z`, og et `sha`-tag
- Multi-arch: `linux/amd64, linux/arm64` understøttes via Buildx
- Dockerfile-mønster: byg afhængighedshjul i builder (med `build-essential` og `python3-dev`) og installer fra lokal wheelhouse i runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` bygger og pusher til GHCR

## Sikkerhedsovervejelser

- Opbevar API-nøgler og endpoints i `.env` eller din CI-sekretlager; commit aldrig secrets.
- Til billedoversættelse kræves Azure AI Vision-nøgler/endpoints; ellers undlad `-img`.
- Tjek udbyderens kvoter/rate limits ved store oversættelsesbatcher.

## Pull Request-retningslinjer

### Før du indsender

1. **Test dine ændringer:**
   - Kør de berørte notebooks helt igennem
   - Tjek at alle celler kører uden fejl
   - Kontroller at output er passende

2. **Opdater dokumentation:**
   - Opdater `README.md` hvis du tilføjer nye koncepter
   - Tilføj kommentarer i notebooks for kompleks kode
   - Sørg for at markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at committe `.env`-filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/`-mapper
   - Behold notebook-output når de demonstrerer koncepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

4. **Stil og formattering:**
   - Følg stil- og formatteringsretningslinjerne
   - Kør `poetry run black .` og `poetry run ruff check .` for at tjekke stil og formattering

5. **Tilføj/opdater tests og CLI-hjælp:**
   - Tilføj eller opdater tests ved ændret funktionalitet
   - Hold CLI-hjælpen opdateret i forhold til ændringer


### Commit-besked og merge-strategi

Vi bruger Squash and Merge som standard. Den endelige squash-commit-besked skal følge:

```bash
<type>: <description> (#<PR number>)
```

Tilladte typer:
- `Docs` — opdateringer af dokumentation
- `Build` — buildsystem, afhængigheder, konfiguration/CI
- `Core` — kernefunktionalitet og features (fx `src/co_op_translator/core`)

Eksempler:
- `Docs: Opdater installationsvejledning for klarhed (#50)`
- `Core: Forbedr håndtering af billedoversættelse (#60)`

Bemærkninger:
- PR-titler får ofte automatisk præfiks baseret på labels; tjek at det genererede præfiks er korrekt.

### PR-titelformat

Brug klare, præcise titler. Foretræk samme struktur som den endelige squash-commit:
- `Docs: Opdater installationsvejledning for klarhed`
- `Core: Forbedr håndtering af billedoversættelse`

## Fejlfinding og troubleshooting

- Almindelige problemer og løsninger: `getting_started/troubleshooting.md`
- Understøttede sprog og noter (inkl. skrifttyper/kendte problemer): `getting_started/supported-languages.md`
- For linkproblemer i notebooks, kør: `migrate-links -l "all" -y` igen

## Noter til agenter

- Foretræk Poetry for reproducerbare miljøer; brug ellers `requirements.txt`.
- Når CLI'er køres i CI, angiv nødvendige secrets via miljøvariabler eller `.env`-injektion.
- For monorepo-brugere fungerer dette repo som en selvstændig pakke; ingen sub-package koordinering kræves.

- Multi-arch vejledning: behold `linux/arm64` når ARM-brugere (Apple Silicon/ARM-servere) er målgruppen; ellers er kun `linux/amd64` acceptabelt for enkelhedens skyld.
- Henvis brugere til Docker Quick Start i `README.md`, hvis de foretrækker container-brug; inkluder både Bash- og PowerShell-varianter pga. forskelle i citationstegn.

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.