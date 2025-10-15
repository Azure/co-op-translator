<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:31:34+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tl"
}
-->
## Pangkalahatang-ideya ng Proyekto

Ang Co‑op Translator ay isang Python command‑line tool at GitHub Actions workflow na nagta-translate ng mga Markdown file, Jupyter notebook, at text mula sa mga larawan papunta sa iba’t ibang wika. Inaayos nito ang mga output sa ilalim ng mga folder na nakalaan para sa bawat wika at pinapanatiling naka-synchronize ang mga translation sa source content. Ang proyekto ay nakaayos bilang isang library na pinamamahalaan ng Poetry na may CLI entry points.

### Pangkalahatang-ideya ng Arkitektura

- Ang mga CLI entry point (`translate`, `migrate-links`, `evaluate`) ay tumatawag sa isang unified CLI na nagdi-dispatch sa translation, link migration, at evaluation flows.
- Ang configuration loader ay nagbabasa ng `.env` at awtomatikong nade-detect ang LLM provider (Azure OpenAI o OpenAI) at, kung kinakailangan, ang vision provider (Azure AI Service) para sa pagkuha ng text mula sa mga larawan.
- Ang translation core ang bahala sa Markdown at notebook; ang vision pipeline ay kumukuha ng text mula sa mga larawan kapag ginamit ang `-img`.
- Ang mga output ay inaayos sa `translations/<lang>/` para sa text at `translated_images/` para sa mga larawan, pinapanatili ang orihinal na istruktura.

### Pangunahing teknolohiya at framework

- Python 3.10–3.12, Poetry para sa packaging
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP at data: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## Mga Command para sa Setup

### Mga Kailangan

- Python 3.10–3.12
- Azure subscription (opsyonal, para sa Azure AI services)
- Internet access para sa LLM/Vision APIs (hal. Azure OpenAI/OpenAI, Azure AI Vision)

### Opsyon A: Poetry (inirerekomenda)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opsyon B: pip/venv

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

## Paggamit para sa End User

### Docker (published image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Mga Tala:
- Ang default entrypoint ay `translate`. Palitan gamit ang `--entrypoint migrate-links` para sa link migration.
- Siguraduhing naka-public ang visibility ng GHCR package para sa anonymous pulls.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Environment configuration

Gumawa ng `.env` file sa root ng repository at ilagay ang credentials/endpoints para sa napiling language model at (opsyonal) vision service. Para sa provider‑specific setup, tingnan ang `getting_started/set-up-azure-ai.md`.

### Mga Kailangan na Environment Variable

Kailangan na may nakakonfig na kahit isang LLM provider. Para sa image translation, kailangan ding nakakonfig ang Azure AI Service.

- Azure OpenAI (text translation):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatibo para sa text translation):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opsyonal)
  - `OPENAI_CHAT_MODEL_ID` (kailangan kapag OpenAI provider ang gamit)
  - `OPENAI_BASE_URL` (opsyonal; default ay `https://api.openai.com/v1`)

- Azure AI Service para sa pagkuha ng text mula sa larawan (kailangan kapag gamit ang `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (mas mainam) o legacy `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Halimbawa ng `.env` snippet:

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

Mga Tala:

- Awtomatikong nade-detect ng tool ang available na LLM provider; mag-configure ng Azure OpenAI o OpenAI.
- Ang image translation ay nangangailangan ng parehong `AZURE_AI_SERVICE_API_KEY` at `AZURE_AI_SERVICE_ENDPOINT`.
- Magbibigay ang CLI ng malinaw na error kung may kulang na variable.

## Workflow para sa Development

- Ang source code ay nasa ilalim ng `src/co_op_translator`; ang mga test ay nasa `tests/`.
- Pangunahing CLIs (na-install sa pamamagitan ng entry points):

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

Tingnan ang karagdagang dokumentasyon sa paggamit sa `getting_started/`.

## Mga Tagubilin sa Pagsusuri

Patakbuhin ang mga test mula sa root ng repository. May ilang test na nangangailangan ng API credentials; laktawan ang mga iyon kung kinakailangan.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Opsyonal na coverage (kailangan ng `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Mga Gabay sa Code Style

- Formatter: Black (nakakonfig sa `pyproject.toml`, line length 88)
- Linter: Ruff (nakakonfig sa `pyproject.toml`, line length 120)
- Type checks: mypy (may configuration; i-enable kung naka-install)

Mga Command:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Ayusin ang mga Python source sa ilalim ng `src/`, mga test sa ilalim ng `tests/`, at mas mainam ang explicit imports sa loob ng package namespace (`co_op_translator.*`).

## Build at Deployment

Ang mga build artifact ay inilalathala sa `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

May automation gamit ang GitHub Actions; tingnan:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- Opisyal na image: `ghcr.io/azure/co-op-translator:<tag>`
- Mga tag: `latest` (sa main), semantic tags tulad ng `vX.Y.Z`, at isang `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` suportado gamit ang Buildx
- Dockerfile pattern: bumuo ng dependency wheels sa builder (may `build-essential` at `python3-dev`) at i-install mula sa local wheelhouse sa runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` ang nagbu-build at nag-pu-push sa GHCR

## Mga Dapat Isaalang-alang sa Seguridad

- Ilagay ang API keys at endpoints sa `.env` o sa CI secrets store; huwag kailanman i-commit ang secrets.
- Para sa image translation, kailangan ang Azure AI Vision keys/endpoints; kung hindi, huwag gamitin ang `-img`.
- I-validate ang provider quotas/rate limits kapag magpapatakbo ng malalaking batch ng translation.

## Mga Gabay sa Pull Request

### Bago Mag-submit

1. **I-test ang mga pagbabago:**
   - Patakbuhin nang buo ang mga apektadong notebook
   - Siguraduhing walang error sa lahat ng cell
   - Tiyaking tama ang mga output

2. **Pag-update ng dokumentasyon:**
   - I-update ang `README.md` kung may bagong konsepto
   - Magdagdag ng comments sa notebook para sa komplikadong code
   - Siguraduhing may paliwanag ang mga markdown cell

3. **Pagbabago sa file:**
   - Iwasang i-commit ang `.env` files (gamitin ang `.env.example`)
   - Huwag i-commit ang `venv/` o `__pycache__/` directories
   - Panatilihin ang notebook outputs kung nagpapakita ng konsepto
   - Alisin ang temporary files at backup notebook (`*-backup.ipynb`)

4. **Style at formatting:**
   - Sundin ang style at formatting guidelines
   - Patakbuhin ang `poetry run black .` at `poetry run ruff check .` para i-check ang style at formatting issues

5. **Magdagdag/mag-update ng tests at CLI help:**
   - Magdagdag o mag-update ng tests kapag may binago sa behavior
   - Panatilihing consistent ang CLI help sa mga pagbabago


### Commit message at merge strategy

Gamit namin ang Squash and Merge bilang default. Ang final squash commit message ay dapat sumunod sa:

```bash
<type>: <description> (#<PR number>)
```

Mga pinapayagang uri:
- `Docs` — update sa dokumentasyon
- `Build` — build system, dependencies, configuration/CI
- `Core` — pangunahing functionality at features (hal. `src/co_op_translator/core`)

Mga halimbawa:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Mga Tala:
- Madalas na auto-prefixed ang PR titles base sa labels; siguraduhing tama ang generated prefix.

### Format ng PR Title

Gumamit ng malinaw at maikling title. Mas mainam na sundan ang parehong structure ng final squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging at Troubleshooting

- Mga karaniwang isyu at solusyon: `getting_started/troubleshooting.md`
- Mga suportadong wika at tala (kasama ang fonts/kilalang isyu): `getting_started/supported-languages.md`
- Para sa link issues sa notebook, i-re-run: `migrate-links -l "all" -y`

## Mga Tala para sa Agents

- Mas mainam ang Poetry para sa reproducible environments; kung hindi, gamitin ang `requirements.txt`.
- Kapag tumatawag ng CLIs sa CI, ibigay ang mga kinakailangang secrets sa pamamagitan ng environment variables o `.env` injection.
- Para sa monorepo consumers, standalone package ang repo na ito; hindi kailangan ng sub‑package coordination.

- Para sa multi-arch: panatilihin ang `linux/arm64` kung target ang ARM users (Apple Silicon/ARM servers); kung hindi, sapat na ang `linux/amd64` para sa pagiging simple.
- I-refer ang users sa Docker Quick Start sa `README.md` kung mas gusto nila ang container usage; isama ang Bash at PowerShell variants dahil sa pagkakaiba ng quoting.

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.