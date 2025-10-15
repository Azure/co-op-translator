<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:28:22+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sv"
}
-->
## Projektöversikt

Co‑op Translator är ett Python-verktyg för kommandoraden och ett GitHub Actions-arbetsflöde som översätter Markdown-filer, Jupyter-notebooks och bildtext till flera språk. Den organiserar utdata under språk‑specifika mappar och håller översättningarna synkroniserade med källinnehållet. Projektet är strukturerat som ett Poetry‑hanterat bibliotek med CLI-ingångspunkter.

### Arkitekturöversikt

- CLI-ingångspunkter (`translate`, `migrate-links`, `evaluate`) anropar ett enhetligt CLI som skickar vidare till översättning, länk-migrering och utvärderingsflöden.
- Konfigurationsläsaren läser `.env` och auto‑detekterar LLM-leverantören (Azure OpenAI eller OpenAI) och, om begärt, vision-leverantören (Azure AI Service) för bildtextutvinning.
- Översättningskärnan hanterar Markdown och notebooks; vision-pipelinen extraherar text från bilder när `-img` används.
- Utdata organiseras i `translations/<lang>/` för text och `translated_images/` för bilder, med bibehållen ursprungsstruktur.

### Viktiga teknologier och ramverk

- Python 3.10–3.12, Poetry för paketering
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP och data: `httpx`, `pydantic`
- Bildhantering: `pillow`, `opencv-python`, `matplotlib`
- Verktyg: `pytest`, `black`, `ruff`

## Installationskommandon

### Förutsättningar

- Python 3.10–3.12
- Azure-prenumeration (valfritt, för Azure AI-tjänster)
- Internetåtkomst för LLM/Vision API:er (t.ex. Azure OpenAI/OpenAI, Azure AI Vision)

### Alternativ A: Poetry (rekommenderas)

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

## Slutanvändaranvändning

### Docker (publicerad bild)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Noteringar:
- Standard-ingångspunkt är `translate`. Åsidosätt med `--entrypoint migrate-links` för länk-migrering.
- Kontrollera att GHCR-paketets synlighet är Public för anonyma hämtningar.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Miljökonfiguration

Skapa en `.env`-fil i rotmappen för repot och ange autentiseringsuppgifter/slutpunkter för din valda språkmodell och (valfritt) vision-tjänst. För leverantörsspecifik installation, se `getting_started/set-up-azure-ai.md`.

### Obligatoriska miljövariabler

Minst en LLM-leverantör måste konfigureras. För bildöversättning krävs även Azure AI Service.

- Azure OpenAI (textöversättning):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativ för textöversättning):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (valfritt)
  - `OPENAI_CHAT_MODEL_ID` (obligatorisk vid användning av OpenAI-leverantör)
  - `OPENAI_BASE_URL` (valfritt; standard är `https://api.openai.com/v1`)

- Azure AI Service för bildtextutvinning (krävs vid användning av `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (föredras) eller äldre `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Exempel på `.env`-utdrag:

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

Noteringar:

- Verktyget auto-detekterar tillgänglig LLM-leverantör; konfigurera antingen Azure OpenAI eller OpenAI.
- Bildöversättning kräver både `AZURE_AI_SERVICE_API_KEY` och `AZURE_AI_SERVICE_ENDPOINT`.
- CLI:n ger ett tydligt felmeddelande om obligatoriska variabler saknas.

## Utvecklingsflöde

- Källkod finns under `src/co_op_translator`; tester under `tests/`.
- Primära CLI:er (installeras via entry points):

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

Se ytterligare användardokumentation i `getting_started/`.

## Testinstruktioner

Kör tester från repots rot. Vissa tester kan kräva API-nycklar; hoppa över dessa vid behov.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Valfri täckning (kräver `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Kodstilriktlinjer

- Formatterare: Black (konfigurerad i `pyproject.toml`, radlängd 88)
- Linter: Ruff (konfigurerad i `pyproject.toml`, radlängd 120)
- Typkontroller: mypy (konfiguration finns; aktivera om installerad)

Kommandon:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organisera Python-källor under `src/`, tester under `tests/`, och föredra explicita importer inom paketnamnrymden (`co_op_translator.*`).

## Bygg och distribution

Byggda artefakter publiceras till `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatisering via GitHub Actions stöds; se:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Containerbild (GHCR)

- Officiell bild: `ghcr.io/azure/co-op-translator:<tag>`
- Taggar: `latest` (på main), semantiska taggar som `vX.Y.Z`, och en `sha`-tagg
- Multi-arch: `linux/amd64, linux/arm64` stöds via Buildx
- Dockerfile-mönster: bygg beroendehjul i builder (med `build-essential` och `python3-dev`) och installera från lokal wheelhouse i runtime (`pip install --no-index --find-links=/wheels`)
- Arbetsflöde: `.github/workflows/docker-publish.yml` bygger och pushar till GHCR

## Säkerhetsaspekter

- Förvara API-nycklar och slutpunkter i `.env` eller din CI-hemlighetslagring; checka aldrig in hemligheter.
- För bildöversättning krävs Azure AI Vision-nycklar/slutpunkter; annars utelämna `-img`.
- Kontrollera leverantörskvoter/gränser vid stora översättningsbatcher.

## Riktlinjer för Pull Requests

### Innan du skickar in

1. **Testa dina ändringar:**
   - Kör berörda notebooks helt
   - Kontrollera att alla celler körs utan fel
   - Kontrollera att utdata är lämpliga

2. **Dokumentationsuppdateringar:**
   - Uppdatera `README.md` om du lägger till nya koncept
   - Lägg till kommentarer i notebooks för komplex kod
   - Se till att markdown-celler förklarar syftet

3. **Filändringar:**
   - Undvik att checka in `.env`-filer (använd `.env.example`)
   - Checka inte in `venv/` eller `__pycache__/`-mappar
   - Behåll notebook-utdata när de visar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

4. **Stil och formatering:**
   - Följ stil- och formateringsriktlinjerna
   - Kör `poetry run black .` och `poetry run ruff check .` för att kontrollera stil och formatering

5. **Lägg till/uppdatera tester och CLI-hjälp:**
   - Lägg till eller uppdatera tester vid ändrat beteende
   - Håll CLI-hjälpen uppdaterad med ändringar


### Commit-meddelande och sammanslagningsstrategi

Vi använder Squash and Merge som standard. Det slutliga squash-commit-meddelandet ska följa:

```bash
<type>: <description> (#<PR number>)
```

Tillåtna typer:
- `Docs` — dokumentationsuppdateringar
- `Build` — byggsystem, beroenden, konfiguration/CI
- `Core` — kärnfunktionalitet och funktioner (t.ex. `src/co_op_translator/core`)

Exempel:
- `Docs: Uppdatera installationsinstruktioner för tydlighet (#50)`
- `Core: Förbättra hantering av bildöversättning (#60)`

Noteringar:
- PR-titlar får ofta automatiskt prefix baserat på etiketter; kontrollera att genererat prefix är korrekt.

### PR-titelformat

Använd tydliga, koncisa titlar. Föredra samma struktur som det slutliga squash-commitet:
- `Docs: Uppdatera installationsinstruktioner för tydlighet`
- `Core: Förbättra hantering av bildöversättning`

## Felsökning och problemlösning

- Vanliga problem och lösningar: `getting_started/troubleshooting.md`
- Stödda språk och noteringar (inklusive typsnitt/kända problem): `getting_started/supported-languages.md`
- För länkproblem i notebooks, kör om: `migrate-links -l "all" -y`

## Noteringar för agenter

- Föredra Poetry för reproducerbara miljöer; annars använd `requirements.txt`.
- Vid CLI-anrop i CI, ange nödvändiga hemligheter via miljövariabler eller `.env`-injektion.
- För monorepo-konsumenter fungerar detta repo som ett fristående paket; ingen sub‑paketkoordinering krävs.

- Multi-arch-råd: behåll `linux/arm64` när ARM-användare (Apple Silicon/ARM-servrar) är en målgrupp; annars är endast `linux/amd64` acceptabelt för enkelhetens skull.
- Hänvisa användare till Docker Quick Start i `README.md` om de föredrar containeranvändning; inkludera Bash- och PowerShell-varianter på grund av skillnader i citattecken.

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.