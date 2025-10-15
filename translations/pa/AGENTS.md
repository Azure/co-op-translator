<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:25:19+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pa"
}
-->
## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

Co‑op Translator ਇੱਕ Python ਕਮਾਂਡ-ਲਾਈਨ ਟੂਲ ਅਤੇ GitHub Actions ਵਰਕਫਲੋ ਹੈ ਜੋ Markdown ਫਾਈਲਾਂ, Jupyter ਨੋਟਬੁੱਕ ਅਤੇ ਚਿੱਤਰਾਂ ਵਿੱਚ ਲਿਖੀ ਟੈਕਸਟ ਨੂੰ ਕਈ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ। ਇਹ ਨਤੀਜਿਆਂ ਨੂੰ ਭਾਸ਼ਾ-ਵਾਰ ਫੋਲਡਰਾਂ ਵਿੱਚ ਰੱਖਦਾ ਹੈ ਅਤੇ ਅਨੁਵਾਦਾਂ ਨੂੰ ਸਰੋਤ ਸਮੱਗਰੀ ਨਾਲ ਸਿੰਕ ਕਰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ Poetry-ਮੈਨੇਜਡ ਲਾਇਬ੍ਰੇਰੀ ਵਜੋਂ ਬਣਾਇਆ ਗਿਆ ਹੈ ਜਿਸ ਵਿੱਚ CLI ਐਂਟਰੀ ਪੌਇੰਟ ਹਨ।

### ਆਰਕੀਟੈਕਚਰ ਝਲਕ

- CLI ਐਂਟਰੀ ਪੌਇੰਟ (`translate`, `migrate-links`, `evaluate`) ਇੱਕ統 CLI ਨੂੰ ਚਲਾਉਂਦੇ ਹਨ ਜੋ ਅਨੁਵਾਦ, ਲਿੰਕ ਮਾਈਗ੍ਰੇਸ਼ਨ ਅਤੇ ਮੁਲਾਂਕਣ ਵਾਲੇ ਫਲੋਜ਼ ਨੂੰ ਚਲਾਉਂਦਾ ਹੈ।
- Configuration ਲੋਡਰ `.env` ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ LLM ਪ੍ਰੋਵਾਈਡਰ (Azure OpenAI ਜਾਂ OpenAI) ਨੂੰ ਆਟੋ-ਡਿਟੈਕਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਵਿਜ਼ਨ ਪ੍ਰੋਵਾਈਡਰ (Azure AI Service) ਨੂੰ ਵੀ ਚਿੱਤਰ ਟੈਕਸਟ ਐਕਸਟ੍ਰੈਕਸ਼ਨ ਲਈ।
- Translation ਕੋਰ Markdown ਅਤੇ ਨੋਟਬੁੱਕਾਂ ਨੂੰ ਹੈਂਡਲ ਕਰਦਾ ਹੈ; ਵਿਜ਼ਨ ਪਾਈਪਲਾਈਨ `-img` ਵਰਤਣ 'ਤੇ ਚਿੱਤਰਾਂ ਤੋਂ ਟੈਕਸਟ ਕੱਢਦਾ ਹੈ।
- ਨਤੀਜੇ `translations/<lang>/` ਵਿੱਚ ਟੈਕਸਟ ਲਈ ਅਤੇ `translated_images/` ਵਿੱਚ ਚਿੱਤਰਾਂ ਲਈ ਰੱਖੇ ਜਾਂਦੇ ਹਨ, ਅਸਲ ਬਣਤਰ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦੇ ਹੋਏ।

### ਮੁੱਖ ਟੈਕਨੋਲੋਜੀਆਂ ਅਤੇ ਫਰੇਮਵਰਕ

- Python 3.10–3.12, Poetry ਪੈਕੇਜਿੰਗ ਲਈ
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP ਅਤੇ ਡਾਟਾ: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## ਸੈਟਅੱਪ ਕਮਾਂਡ

### ਲੋੜੀਂਦੇ ਪੂਰਵ-ਸ਼ਰਤਾਂ

- Python 3.10–3.12
- Azure subscription (ਚੋਣਵੀਂ, Azure AI services ਲਈ)
- LLM/Vision APIs ਲਈ ਇੰਟਰਨੈੱਟ ਐਕਸੈੱਸ (ਜਿਵੇਂ Azure OpenAI/OpenAI, Azure AI Vision)

### ਵਿਕਲਪ A: Poetry (ਸਿਫਾਰਸ਼ੀ)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### ਵਿਕਲਪ B: pip/venv

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

## ਆਖਰੀ ਯੂਜ਼ਰ ਵਰਤੋਂ

### Docker (ਪਬਲਿਸ਼ਡ ਇਮੇਜ)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

ਨੋਟਸ:
- ਡਿਫਾਲਟ ਐਂਟਰੀਪੌਇੰਟ `translate` ਹੈ। ਲਿੰਕ ਮਾਈਗ੍ਰੇਸ਼ਨ ਲਈ `--entrypoint migrate-links` ਨਾਲ ਓਵਰਰਾਈਡ ਕਰੋ।
- Anonymous pulls ਲਈ GHCR ਪੈਕੇਜ ਵਿਜ਼ੀਬਿਲਟੀ Public ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Environment configuration

`.env` ਫਾਈਲ ਰਿਪੋ ਰੂਟ 'ਤੇ ਬਣਾਓ ਅਤੇ ਆਪਣੀ ਚੁਣੀ ਹੋਈ language model ਅਤੇ (ਚੋਣਵੀਂ) vision service ਲਈ credentials/endpoints ਦਿਓ। ਪ੍ਰੋਵਾਈਡਰ-ਵਾਰ ਸੈਟਅੱਪ ਲਈ `getting_started/set-up-azure-ai.md` ਵੇਖੋ।

### ਲੋੜੀਂਦੇ Environment Variables

ਘੱਟੋ-ਘੱਟ ਇੱਕ LLM ਪ੍ਰੋਵਾਈਡਰ ਕਨਫਿਗਰ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ Azure AI Service ਵੀ ਲੋੜੀਂਦੀ ਹੈ।

- Azure OpenAI (ਟੈਕਸਟ ਅਨੁਵਾਦ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (ਟੈਕਸਟ ਅਨੁਵਾਦ ਵਿਕਲਪ):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ਚੋਣਵੀਂ)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI ਪ੍ਰੋਵਾਈਡਰ ਵਰਤਣ 'ਤੇ ਲੋੜੀਂਦਾ)
  - `OPENAI_BASE_URL` (ਚੋਣਵੀਂ; ਡਿਫਾਲਟ `https://api.openai.com/v1`)

- Azure AI Service ਚਿੱਤਰ ਟੈਕਸਟ ਐਕਸਟ੍ਰੈਕਸ਼ਨ ਲਈ (`-img` ਵਰਤਣ 'ਤੇ ਲੋੜੀਂਦਾ):
  - `AZURE_AI_SERVICE_API_KEY` (preferred) ਜਾਂ legacy `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env` ਉਦਾਹਰਨ:

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

ਨੋਟਸ:

- ਟੂਲ ਉਪਲਬਧ LLM ਪ੍ਰੋਵਾਈਡਰ ਨੂੰ ਆਟੋ-ਡਿਟੈਕਟ ਕਰਦਾ ਹੈ; Azure OpenAI ਜਾਂ OpenAI ਵਿੱਚੋਂ ਇੱਕ ਕਨਫਿਗਰ ਕਰੋ।
- ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ `AZURE_AI_SERVICE_API_KEY` ਅਤੇ `AZURE_AI_SERVICE_ENDPOINT` ਦੋਵੇਂ ਲੋੜੀਂਦੇ ਹਨ।
- CLI ਜੇ ਲੋੜੀਂਦੇ variables ਨਾ ਹੋਣ ਤਾਂ ਸਾਫ਼ error ਦਿੰਦਾ ਹੈ।

## ਡਿਵੈਲਪਮੈਂਟ ਵਰਕਫਲੋ

- ਸਰੋਤ ਕੋਡ `src/co_op_translator` ਹੇਠ ਹੈ; ਟੈਸਟਾਂ `tests/` ਹੇਠ।
- ਮੁੱਖ CLI (entry points ਰਾਹੀਂ ਇੰਸਟਾਲ):

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

ਹੋਰ ਵਰਤੋਂ ਦਸਤਾਵੇਜ਼ `getting_started/` ਵਿੱਚ ਵੇਖੋ।

## ਟੈਸਟਿੰਗ ਹਦਾਇਤਾਂ

ਟੈਸਟਾਂ ਰਿਪੋ ਰੂਟ ਤੋਂ ਚਲਾਓ। ਕੁਝ ਟੈਸਟਾਂ ਲਈ API credentials ਲੋੜੀਂਦੇ ਹੋ ਸਕਦੇ ਹਨ; ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਉਹ ਸਕਿਪ ਕਰੋ।

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

ਚੋਣਵੀਂ coverage (ਲੋੜ `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## ਕੋਡ ਸਟਾਈਲ ਹਦਾਇਤਾਂ

- Formatter: Black (`pyproject.toml` ਵਿੱਚ ਕਨਫਿਗਰ, line length 88)
- Linter: Ruff (`pyproject.toml` ਵਿੱਚ ਕਨਫਿਗਰ, line length 120)
- Type checks: mypy (configuration ਮੌਜੂਦ; ਇੰਸਟਾਲ ਹੋਣ 'ਤੇ enable ਕਰੋ)

ਕਮਾਂਡ:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python ਸਰੋਤ `src/` ਹੇਠ, ਟੈਸਟਾਂ `tests/` ਹੇਠ ਰੱਖੋ, ਅਤੇ ਪੈਕੇਜ namespace (`co_op_translator.*`) ਵਿੱਚ explicit imports ਨੂੰ ਤਰਜੀਹ ਦਿਓ।

## ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ

Build artifacts `dist/` ਵਿੱਚ ਪਬਲਿਸ਼ ਹੁੰਦੇ ਹਨ।

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automation GitHub Actions ਰਾਹੀਂ supported ਹੈ; ਵੇਖੋ:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- Official image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (main 'ਤੇ), semantic tags ਜਿਵੇਂ `vX.Y.Z`, ਅਤੇ `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` Buildx ਰਾਹੀਂ supported
- Dockerfile pattern: builder ਵਿੱਚ dependency wheels ਬਣਾਓ (`build-essential` ਅਤੇ `python3-dev` ਨਾਲ) ਅਤੇ runtime ਵਿੱਚ local wheelhouse ਤੋਂ install ਕਰੋ (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` GHCR 'ਤੇ build/push ਕਰਦਾ ਹੈ

## ਸੁਰੱਖਿਆ ਸੰਬੰਧੀ ਗੱਲਾਂ

- API keys ਅਤੇ endpoints `.env` ਜਾਂ CI secrets store ਵਿੱਚ ਰੱਖੋ; secrets ਕਦੇ commit ਨਾ ਕਰੋ।
- ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ Azure AI Vision keys/endpoints ਲੋੜੀਂਦੇ ਹਨ; ਨਹੀਂ ਤਾਂ `-img` ਨਾ ਵਰਤੋ।
- ਵੱਡੇ translation batch ਚਲਾਉਣ 'ਤੇ provider quotas/rate limits ਚੈੱਕ ਕਰੋ।

## Pull Request ਹਦਾਇਤਾਂ

### Submit ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

1. **ਆਪਣੀਆਂ ਤਬਦੀਲੀਆਂ ਟੈਸਟ ਕਰੋ:**
   - ਪ੍ਰਭਾਵਿਤ ਨੋਟਬੁੱਕ ਪੂਰੀ ਤਰ੍ਹਾਂ ਚਲਾਓ
   - ਸਾਰੇ cell ਬਿਨਾਂ error ਦੇ ਚਲਣ
   - Outputs ਠੀਕ ਹਨ ਜਾਂ ਨਹੀਂ ਚੈੱਕ ਕਰੋ

2. **ਦਸਤਾਵੇਜ਼ ਅੱਪਡੇਟ:**
   - ਨਵੇਂ concepts ਜੋੜਣ 'ਤੇ `README.md` ਅੱਪਡੇਟ ਕਰੋ
   - ਜਟਿਲ ਕੋਡ ਲਈ ਨੋਟਬੁੱਕ ਵਿੱਚ comments ਜੋੜੋ
   - Markdown cells ਵਿੱਚ purpose ਸਪਸ਼ਟ ਕਰੋ

3. **ਫਾਈਲ ਤਬਦੀਲੀਆਂ:**
   - `.env` files commit ਨਾ ਕਰੋ (`.env.example` ਵਰਤੋ)
   - `venv/` ਜਾਂ `__pycache__/` directories commit ਨਾ ਕਰੋ
   - Notebook outputs ਰੱਖੋ ਜੇ ਉਹ concepts ਦਿਖਾਉਂਦੇ ਹਨ
   - Temporary files ਅਤੇ backup notebooks (`*-backup.ipynb`) ਹਟਾਓ

4. **ਸਟਾਈਲ ਅਤੇ ਫਾਰਮੈਟਿੰਗ:**
   - Style ਅਤੇ formatting ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
   - `poetry run black .` ਅਤੇ `poetry run ruff check .` ਚਲਾਕੇ style/formatting issues ਚੈੱਕ ਕਰੋ

5. **ਟੈਸਟਾਂ ਅਤੇ CLI help ਜੋੜੋ/ਅੱਪਡੇਟ ਕਰੋ:**
   - Behavior ਬਦਲਣ 'ਤੇ ਟੈਸਟਾਂ ਜੋੜੋ ਜਾਂ ਅੱਪਡੇਟ ਕਰੋ
   - CLI help ਨੂੰ ਤਬਦੀਲੀਆਂ ਨਾਲ consistent ਰੱਖੋ


### Commit message ਅਤੇ merge strategy

ਅਸੀਂ Squash and Merge default ਵਜੋਂ ਵਰਤਦੇ ਹਾਂ। Final squash commit message ਇਹ following structure 'ਚ ਹੋਣਾ ਚਾਹੀਦਾ:

```bash
<type>: <description> (#<PR number>)
```

Allowed types:
- `Docs` — ਦਸਤਾਵੇਜ਼ ਅੱਪਡੇਟ
- `Build` — build system, dependencies, configuration/CI
- `Core` — core functionality ਅਤੇ features (ਜਿਵੇਂ `src/co_op_translator/core`)

Examples:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

ਨੋਟਸ:
- PR titles ਅਕਸਰ labels ਦੇ ਆਧਾਰ 'ਤੇ auto-prefixed ਹੁੰਦੇ ਹਨ; generated prefix ਠੀਕ ਹੈ ਜਾਂ ਨਹੀਂ ਚੈੱਕ ਕਰੋ।

### PR Title Format

ਸਪਸ਼ਟ, ਸੰਖੇਪ titles ਵਰਤੋ। Final squash commit ਵਾਲੀ structure ਨੂੰ ਤਰਜੀਹ ਦਿਓ:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging ਅਤੇ Troubleshooting

- ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ: `getting_started/troubleshooting.md`
- Supported languages ਅਤੇ ਨੋਟਸ (fonts/known issues ਸਮੇਤ): `getting_started/supported-languages.md`
- Notebook ਵਿੱਚ link issues ਲਈ, ਦੁਬਾਰਾ ਚਲਾਓ: `migrate-links -l "all" -y`

## Agents ਲਈ ਨੋਟਸ

- Reproducible environment ਲਈ Poetry ਨੂੰ ਤਰਜੀਹ ਦਿਓ; ਨਹੀਂ ਤਾਂ `requirements.txt` ਵਰਤੋ।
- CI ਵਿੱਚ CLI invoke ਕਰਦੇ ਸਮੇਂ ਲੋੜੀਂਦੇ secrets environment variables ਜਾਂ `.env` injection ਰਾਹੀਂ ਦਿਓ।
- Monorepo consumers ਲਈ, ਇਹ repo standalone package ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ; sub-package coordination ਦੀ ਲੋੜ ਨਹੀਂ।

- Multi-arch ਹਦਾਇਤ: ਜੇ ARM users (Apple Silicon/ARM servers) target ਹਨ ਤਾਂ `linux/arm64` ਰੱਖੋ; ਨਹੀਂ ਤਾਂ ਸਧਾਰਨਤਾ ਲਈ `linux/amd64` ਹੀ acceptable ਹੈ।
- Container ਵਰਤੋਂ ਪਸੰਦ ਕਰਨ ਵਾਲਿਆਂ ਨੂੰ Docker Quick Start `README.md` ਵਿੱਚ point ਕਰੋ; quoting differences ਕਰਕੇ Bash ਅਤੇ PowerShell ਦੋਵੇਂ variants ਸ਼ਾਮਲ ਕਰੋ।

---

**ਅਸਵੀਕਰਨ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜੇਕਰ ਜਾਣਕਾਰੀ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਤਾਂ ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।