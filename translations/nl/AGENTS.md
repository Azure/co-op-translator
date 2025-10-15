<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:29:50+00:00",
  "source_file": "AGENTS.md",
  "language_code": "nl"
}
-->
# AGENTS.md

## Projectoverzicht

Co‑op Translator is een Python command-line tool en GitHub Actions workflow die Markdown-bestanden, Jupyter-notebooks en afbeeldings­tekst vertaalt naar meerdere talen. Uitvoer wordt georganiseerd in taalspecifieke mappen en vertalingen blijven gesynchroniseerd met de broninhoud. Het project is opgezet als een Poetry‑beheerde bibliotheek met CLI-entrypoints.

### Architectuuroverzicht

- CLI-entrypoints (`translate`, `migrate-links`, `evaluate`) roepen een uniforme CLI aan die vertaalt, links migreert en evaluatieprocessen start.
- Configuratielader leest `.env` en detecteert automatisch de LLM-provider (Azure OpenAI of OpenAI) en, indien gevraagd, de vision-provider (Azure AI Service) voor tekstextractie uit afbeeldingen.
- Vertaalcore verwerkt Markdown en notebooks; de vision-pijplijn haalt tekst uit afbeeldingen wanneer `-img` wordt gebruikt.
- Uitvoer wordt georganiseerd in `translations/<lang>/` voor tekst en `translated_images/` voor afbeeldingen, waarbij de originele structuur behouden blijft.

### Belangrijke technologieën en frameworks

- Python 3.10–3.12, Poetry voor packaging
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP en data: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tools: `pytest`, `black`, `ruff`

## Installatiecommando's

### Vereisten

- Python 3.10–3.12
- Azure-abonnement (optioneel, voor Azure AI-diensten)
- Internettoegang voor LLM/Vision API's (zoals Azure OpenAI/OpenAI, Azure AI Vision)

### Optie A: Poetry (aanbevolen)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Optie B: pip/venv

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

## Gebruik door eindgebruikers

### Docker (gepubliceerd image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Opmerkingen:
- Standaard entrypoint is `translate`. Overschrijf met `--entrypoint migrate-links` voor linkmigratie.
- Zorg dat de GHCR-pakketzichtbaarheid op Openbaar staat voor anonieme pulls.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Omgevingsconfiguratie

Maak een `.env`-bestand in de hoofdmap van de repository en geef de benodigde credentials/endpoints op voor het gekozen taalmodel en (optioneel) de vision-service. Voor provider-specifieke setup, zie `getting_started/set-up-azure-ai.md`.

### Vereiste omgevingsvariabelen

Minimaal één LLM-provider moet geconfigureerd zijn. Voor vertaling van afbeeldingen moet Azure AI Service ook geconfigureerd zijn.

- Azure OpenAI (tekstvertaling):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatief voor tekstvertaling):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (optioneel)
  - `OPENAI_CHAT_MODEL_ID` (vereist bij gebruik van OpenAI-provider)
  - `OPENAI_BASE_URL` (optioneel; standaard `https://api.openai.com/v1`)

- Azure AI Service voor tekstextractie uit afbeeldingen (vereist bij gebruik van `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (voorkeur) of legacy `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Voorbeeld `.env`-fragment:

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

Opmerkingen:

- De tool detecteert automatisch de beschikbare LLM-provider; configureer Azure OpenAI of OpenAI.
- Voor vertaling van afbeeldingen zijn zowel `AZURE_AI_SERVICE_API_KEY` als `AZURE_AI_SERVICE_ENDPOINT` nodig.
- De CLI geeft een duidelijke foutmelding als vereiste variabelen ontbreken.

## Ontwikkelworkflow

- Broncode staat onder `src/co_op_translator`; tests onder `tests/`.
- Primaire CLI's (geïnstalleerd via entrypoints):

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

Zie extra gebruiksdocumentatie in `getting_started/`.

## Testinstructies

Voer tests uit vanuit de hoofdmap van de repository. Sommige tests vereisen API-credentials; sla deze over indien nodig.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Optionele coverage (vereist `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Richtlijnen voor code-stijl

- Formatter: Black (geconfigureerd in `pyproject.toml`, regellengte 88)
- Linter: Ruff (geconfigureerd in `pyproject.toml`, regellengte 120)
- Typechecks: mypy (configuratie aanwezig; inschakelen indien geïnstalleerd)

Commando's:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organiseer Python-bronnen onder `src/`, tests onder `tests/`, en geef de voorkeur aan expliciete imports binnen de pakketnamespace (`co_op_translator.*`).

## Build en deployment

Build-artifacten worden gepubliceerd naar `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatisering via GitHub Actions wordt ondersteund; zie:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Containerimage (GHCR)

- Officieel image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (op main), semantische tags zoals `vX.Y.Z`, en een `sha`-tag
- Multi-arch: `linux/amd64, linux/arm64` ondersteund via Buildx
- Dockerfile-patroon: bouw dependency wheels in builder (met `build-essential` en `python3-dev`) en installeer uit lokale wheelhouse in runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` bouwt en pusht naar GHCR

## Veiligheidsoverwegingen

- Bewaar API-sleutels en endpoints in `.env` of je CI-secrets store; commit nooit secrets.
- Voor vertaling van afbeeldingen zijn Azure AI Vision-sleutels/endpoints vereist; anders `-img` weglaten.
- Controleer providerquota/ratelimieten bij grote vertaalbatches.

## Richtlijnen voor pull requests

### Voor het indienen

1. **Test je wijzigingen:**
   - Voer de betreffende notebooks volledig uit
   - Controleer dat alle cellen zonder fouten draaien
   - Kijk of de uitvoer correct is

2. **Documentatie-updates:**
   - Werk `README.md` bij als je nieuwe concepten toevoegt
   - Voeg commentaar toe in notebooks bij complexe code
   - Zorg dat markdown-cellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Commit geen `.env`-bestanden (gebruik `.env.example`)
   - Commit geen `venv/` of `__pycache__/`-mappen
   - Houd notebook-uitvoer als deze concepten demonstreert
   - Verwijder tijdelijke bestanden en backup-notebooks (`*-backup.ipynb`)

4. **Stijl en opmaak:**
   - Volg de stijl- en opmaakrichtlijnen
   - Voer `poetry run black .` en `poetry run ruff check .` uit om stijl- en opmaakproblemen te controleren

5. **Tests en CLI-help toevoegen/bijwerken:**
   - Voeg tests toe of werk ze bij bij gedragswijzigingen
   - Houd CLI-help consistent met wijzigingen


### Commitbericht en merge-strategie

We gebruiken standaard Squash and Merge. Het uiteindelijke squash-commitbericht moet het volgende format hebben:

```bash
<type>: <description> (#<PR number>)
```

Toegestane types:
- `Docs` — documentatie-updates
- `Build` — build­systeem, dependencies, configuratie/CI
- `Core` — kernfunctionaliteit en features (zoals `src/co_op_translator/core`)

Voorbeelden:
- `Docs: Installatie-instructies verduidelijkt (#50)`
- `Core: Verbeterde verwerking van afbeeldingvertaling (#60)`

Opmerkingen:
- PR-titels krijgen vaak automatisch een prefix op basis van labels; controleer of de gegenereerde prefix klopt.

### PR-titel format

Gebruik duidelijke, beknopte titels. Geef de voorkeur aan dezelfde structuur als het uiteindelijke squash-commit:
- `Docs: Installatie-instructies verduidelijkt`
- `Core: Verbeterde verwerking van afbeeldingvertaling`

## Debuggen en probleemoplossing

- Veelvoorkomende problemen en oplossingen: `getting_started/troubleshooting.md`
- Ondersteunde talen en opmerkingen (inclusief fonts/bekende issues): `getting_started/supported-languages.md`
- Voor linkproblemen in notebooks, opnieuw uitvoeren: `migrate-links -l "all" -y`

## Notities voor agents

- Geef de voorkeur aan Poetry voor reproduceerbare omgevingen; anders gebruik `requirements.txt`.
- Geef bij het aanroepen van CLI's in CI de vereiste secrets via omgevingsvariabelen of `.env`-injectie.
- Voor monorepo-gebruikers fungeert deze repo als een zelfstandig pakket; geen subpakket-coördinatie nodig.

- Multi-arch advies: houd `linux/arm64` aan als ARM-gebruikers (Apple Silicon/ARM-servers) een doelgroep zijn; anders is alleen `linux/amd64` voldoende voor eenvoud.
- Verwijs gebruikers naar Docker Quick Start in `README.md` als ze containers willen gebruiken; neem Bash- en PowerShell-varianten op vanwege verschillen in aanhalingstekens.

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.