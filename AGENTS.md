# AGENTS.md

## Project Overview

Co‑op Translator is a Python command‑line tool and GitHub Actions workflow that translates Markdown files, Jupyter notebooks, and image text into multiple languages. It organizes outputs under language‑specific folders and keeps translations synchronized with source content. The project is structured as a Poetry‑managed library with CLI entry points.

### Architecture overview
- CLI entry points (`translate`, `migrate-links`, `evaluate`) invoke a unified CLI that dispatches to translation, link migration, and evaluation flows.
- Configuration loader reads `.env` and auto‑detects the LLM provider (Azure OpenAI or OpenAI) and, if requested, the vision provider (Azure AI Service) for image text extraction.
- Translation core handles Markdown and notebooks; the vision pipeline extracts text from images when `-img` is used.
- Outputs are organized into `translations/<lang>/` for text and `translated_images/` for images, preserving original structure.

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

### Environment configuration
Create a `.env` file at the repository root and provide credentials/endpoints for your chosen language model and (optionally) vision service. For provider‑specific setup, see `getting_started/set-up-azure-ai.md`.

### Required Environment Variables

At least one LLM provider must be configured. For image translation, Azure AI Service must also be configured.

- Azure OpenAI (text translation):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (text translation alternative):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (optional)
  - `OPENAI_CHAT_MODEL_ID` (required when using OpenAI provider)
  - `OPENAI_BASE_URL` (optional; defaults to `https://api.openai.com/v1`)

- Azure AI Service for image text extraction (required when using `-img`):
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
- The tool auto-detects the available LLM provider; configure either Azure OpenAI or OpenAI.
- Image translation requires both `AZURE_AI_SERVICE_API_KEY` and `AZURE_AI_SERVICE_ENDPOINT`.
- The CLI will raise a clear error if required variables are missing.

## Development Workflow

- Source code lives under `src/co_op_translator`; tests under `tests/`.
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

See additional usage docs in `getting_started/`.

## Testing Instructions

Run tests from the repository root. Some tests may require API credentials; skip those when needed.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Optional coverage (requires `coverage`):
```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Code Style Guidelines

- Formatter: Black (configured in `pyproject.toml`, line length 88)
- Linter: Ruff (configured in `pyproject.toml`, line length 120)
- Type checks: mypy (configuration present; enable if installed)

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

Organize Python sources under `src/`, tests under `tests/`, and prefer explicit imports within the package namespace (`co_op_translator.*`).

## Build and Deployment

Build artifacts are published to `dist/`.
```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automation via GitHub Actions is supported; see:
- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

## Security Considerations

- Keep API keys and endpoints in `.env` or your CI secrets store; never commit secrets.
- For image translation, Azure AI Vision keys/endpoints are required; otherwise omit `-img`.
- Validate provider quotas/rate limits when running large translation batches.

## Pull Request Guidelines

- Title format: `[co-op-translator] Brief, actionable summary`
- Required checks before merge:
  - Lint/format: `ruff check .`, `black --check .`
  - Tests: `pytest` (or `pytest -m "not api_key_required"` if secrets unavailable)
- Add/update tests when changing behavior; keep CLI help consistent.

## Debugging and Troubleshooting

- Common issues and fixes: `getting_started/troubleshooting.md`
- Supported languages and notes (including fonts/known issues): `getting_started/supported-languages.md`
- For link issues in notebooks, re‑run: `migrate-links -l "all" -y`

## Notes for Agents

- Prefer Poetry for reproducible environments; otherwise use `requirements.txt`.
- When invoking CLIs in CI, provide required secrets via environment variables or `.env` injection.
- For monorepo consumers, this repo acts as a standalone package; no sub‑package coordination is required.
