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
- Default entrypoint is `translate`. Override with `--entrypoint migrate-links` for link migration.
- Ensure GHCR package visibility is Public for anonymous pulls.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
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

### Container Image (GHCR)

- Official image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (on main), semantic tags like `vX.Y.Z`, and a `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` supported via Buildx
- Dockerfile pattern: build dependency wheels in builder (with `build-essential` and `python3-dev`) and install from local wheelhouse in runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` builds and pushes to GHCR

## Security Considerations

- Keep API keys and endpoints in `.env` or your CI secrets store; never commit secrets.
- For image translation, Azure AI Vision keys/endpoints are required; otherwise omit `-img`.
- Validate provider quotas/rate limits when running large translation batches.

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run affected notebooks completely
   - Verify all cells execute without errors
   - Check that outputs are appropriate

2. **Documentation updates:**
   - Update `README.md` if adding new concepts
   - Add comments in notebooks for complex code
   - Ensure markdown cells explain the purpose

3. **File changes:**
   - Avoid committing `.env` files (use `.env.example`)
   - Don't commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs when they demonstrate concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

4. **Style and formatting:**
   - Follow the style and formatting guidelines
   - Run `poetry run black .` and `poetry run ruff check .` to check for style and formatting issues

5. **Add/update tests and CLI help:**
   - Add or update tests when changing behavior
   - Keep CLI help consistent with changes


### Commit message and merge strategy

We use Squash and Merge as the default. The final squash commit message should follow:

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
- PR titles are often auto-prefixed based on labels; verify the generated prefix is correct.

### PR Title Format

Use clear, concise titles. Prefer the same structure as the final squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging and Troubleshooting

- Common issues and fixes: `getting_started/troubleshooting.md`
- Supported languages and notes (including fonts/known issues): `getting_started/supported-languages.md`
- For link issues in notebooks, re‑run: `migrate-links -l "all" -y`

## Notes for Agents

- Prefer Poetry for reproducible environments; otherwise use `requirements.txt`.
- When invoking CLIs in CI, provide required secrets via environment variables or `.env` injection.
- For monorepo consumers, this repo acts as a standalone package; no sub‑package coordination is required.

- Multi-arch guidance: keep `linux/arm64` when ARM users (Apple Silicon/ARM servers) are a target; otherwise `linux/amd64` only is acceptable for simplicity.
- Point users to Docker Quick Start in `README.md` when they prefer container usage; include Bash and PowerShell variants due to quoting differences.
