<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-11-06T17:29:00+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pcm"
}
-->
# AGENTS.md

## Project Overview

Co‑op Translator na Python command‑line tool and GitHub Actions workflow wey dey translate Markdown files, Jupyter notebooks, and image text go plenty languages. E dey arrange di outputs under language‑specific folders and e dey make sure say di translations dey sync with di original content. Di project na Poetry‑managed library wey get CLI entry points.

### Architecture overview

- CLI entry points (`translate`, `migrate-links`, `evaluate`) dey call one unified CLI wey dey handle translation, link migration, and evaluation flows.
- Configuration loader dey read `.env` and e go auto‑detect di LLM provider (Azure OpenAI or OpenAI) and, if dem request am, di vision provider (Azure AI Service) for image text extraction.
- Translation core dey handle Markdown and notebooks; di vision pipeline dey extract text from images when you use `-img`.
- Outputs dey arranged inside `translations/<lang>/` for text and `translated_images/` for images, and e dey keep di original structure.

### Key technologies and frameworks

- Python 3.10–3.12, Poetry for packaging
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP and data: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## Setup Commands

### Prerequisites

- Python 3.10–3.12
- Azure subscription (optional, for Azure AI services)
- Internet access for LLM/Vision APIs (e.g., Azure OpenAI/OpenAI, Azure AI Vision)

### Option A: Poetry (recommended)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Option B: pip/venv

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

## End User Usage

### Docker (published image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Notes:
- Default entrypoint na `translate`. If you wan do link migration, use `--entrypoint migrate-links`.
- Make sure say GHCR package visibility dey Public so dat people fit pull am without login.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Environment configuration

Create `.env` file for di root of di repository and put di credentials/endpoints for di language model wey you wan use and (if you wan) vision service. For provider‑specific setup, check `getting_started/set-up-azure-ai.md`.

### Required Environment Variables

At least one LLM provider must dey configured. For image translation, Azure AI Service must dey configured too.

- Azure OpenAI (text translation):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (text translation alternative):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (optional)
  - `OPENAI_CHAT_MODEL_ID` (required when you dey use OpenAI provider)
  - `OPENAI_BASE_URL` (optional; defaults to `https://api.openai.com/v1`)

- Azure AI Service for image text extraction (required when you dey use `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferred) or legacy `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Example `.env` snippet:

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

Notes:

- Di tool go auto-detect di available LLM provider; configure either Azure OpenAI or OpenAI.
- Image translation need both `AZURE_AI_SERVICE_API_KEY` and `AZURE_AI_SERVICE_ENDPOINT`.
- Di CLI go show clear error if di required variables no dey.

## Development Workflow

- Source code dey inside `src/co_op_translator`; tests dey inside `tests/`.
- Primary CLIs (installed via entry points):

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

Check more usage docs for `getting_started/`.

## Testing Instructions

Run tests from di root of di repository. Some tests fit need API credentials; if you no get, skip dem.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Optional coverage (you go need `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Code Style Guidelines

- Formatter: Black (configured inside `pyproject.toml`, line length 88)
- Linter: Ruff (configured inside `pyproject.toml`, line length 120)
- Type checks: mypy (configuration dey; enable am if you install am)

Commands:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Arrange Python sources inside `src/`, tests inside `tests/`, and make sure say you dey use explicit imports within di package namespace (`co_op_translator.*`).

## Build and Deployment

Build artifacts dey published to `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automation via GitHub Actions dey supported; check:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- Official image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (on main), semantic tags like `vX.Y.Z`, and a `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` dey supported via Buildx
- Dockerfile pattern: build dependency wheels for builder (with `build-essential` and `python3-dev`) and install from local wheelhouse for runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` dey build and push to GHCR

## Security Considerations

- Keep API keys and endpoints inside `.env` or your CI secrets store; no ever commit secrets.
- For image translation, Azure AI Vision keys/endpoints dey required; if you no need am, no use `-img`.
- Check provider quotas/rate limits when you dey run large translation batches.

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run di notebooks wey you change completely
   - Make sure say all di cells dey run without errors
   - Check say di outputs dey correct

2. **Documentation updates:**
   - Update `README.md` if you add new concepts
   - Add comments for notebooks wey get complex code
   - Make sure markdown cells dey explain di purpose

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs if dem dey show concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

4. **Style and formatting:**
   - Follow di style and formatting guidelines
   - Run `poetry run black .` and `poetry run ruff check .` to check for style and formatting issues

5. **Add/update tests and CLI help:**
   - Add or update tests if you change behavior
   - Make sure CLI help dey consistent with di changes


### Commit message and merge strategy

We dey use Squash and Merge as di default. Di final squash commit message suppose follow:

```bash
<type>: <description> (#<PR number>)
```

Allowed types:
- `Docs` — documentation updates
- `Build` — build system, dependencies, configuration/CI
- `Core` — core functionality and features (e.g., `src/co_op_translator/core`)

Examples:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Notes:
- PR titles dey auto-prefixed based on labels; make sure say di generated prefix dey correct.

### PR Title Format

Use clear, short titles. Prefer di same structure as di final squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging and Troubleshooting

- Common issues and how to fix dem: `getting_started/troubleshooting.md`
- Supported languages and notes (including fonts/known issues): `getting_started/supported-languages.md`
- For link issues for notebooks, run again: `migrate-links -l "all" -y`

## Notes for Agents

- Prefer Poetry for reproducible environments; if you no fit, use `requirements.txt`.
- When you dey run CLIs for CI, provide di required secrets via environment variables or `.env` injection.
- For monorepo users, dis repo dey act as standalone package; no need sub‑package coordination.

- Multi-arch guidance: keep `linux/arm64` if ARM users (Apple Silicon/ARM servers) dey target; if no be so, `linux/amd64` only dey okay for simplicity.
- Tell users to check Docker Quick Start for `README.md` if dem prefer to use container; include Bash and PowerShell versions because of quoting differences.

---

**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.