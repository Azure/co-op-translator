<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-11-24T06:33:38+00:00",
  "source_file": "AGENTS.md",
  "language_code": "kn"
}
-->
# AGENTS.md

## ಯೋಜನೆಯ ಅವಲೋಕನ

Co‑op Translator ಒಂದು Python ಆಧಾರಿತ ಕಮಾಂಡ್‑ಲೈನ್ ಸಾಧನ ಮತ್ತು GitHub Actions ಕಾರ್ಯಪ್ರವಾಹವಾಗಿದೆ, ಇದು Markdown ಫೈಲ್‌ಗಳು, Jupyter ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರ ಪಠ್ಯವನ್ನು ಹಲವಾರು ಭಾಷೆಗಳಿಗೆ ಅನುವಾದಿಸುತ್ತದೆ. ಇದು ಭಾಷಾ‑ನಿರ್ದಿಷ್ಟ ಫೋಲ್ಡರ್‌ಗಳ ಅಡಿಯಲ್ಲಿ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಸಂಘಟಿಸುತ್ತದೆ ಮತ್ತು ಮೂಲ ವಿಷಯದೊಂದಿಗೆ ಅನುವಾದಗಳನ್ನು ಸಮನ್ವಯಗೊಳಿಸುತ್ತದೆ. ಈ ಯೋಜನೆ CLI ಎಂಟ್ರಿ ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ Poetry‑ನಿಂದ ನಿರ್ವಹಿಸಲ್ಪಟ್ಟ ಲೈಬ್ರರಿ ರೂಪದಲ್ಲಿ ರಚಿಸಲಾಗಿದೆ.

### ಆರ್ಕಿಟೆಕ್ಚರ್ ಅವಲೋಕನ

- CLI ಎಂಟ್ರಿ ಪಾಯಿಂಟ್‌ಗಳು (`translate`, `migrate-links`, `evaluate`) ಏಕೀಕೃತ CLI ಅನ್ನು ಕರೆಸುತ್ತವೆ, ಇದು ಅನುವಾದ, ಲಿಂಕ್ ಮೈಗ್ರೇಶನ್ ಮತ್ತು ಮೌಲ್ಯಮಾಪನ ಪ್ರಕ್ರಿಯೆಗಳಿಗೆ ವಿತರಿಸುತ್ತದೆ.
- ಕಾನ್ಫಿಗರೇಶನ್ ಲೋಡರ್ `.env` ಅನ್ನು ಓದುತ್ತದೆ ಮತ್ತು LLM ಪೂರೈಕೆದಾರನನ್ನು (Azure OpenAI ಅಥವಾ OpenAI) ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ ಮತ್ತು, ಬೇಡಿಕೆಯಾದರೆ, ದೃಶ್ಯ ಪೂರೈಕೆದಾರನನ್ನು (Azure AI Service) ಚಿತ್ರ ಪಠ್ಯ ಹೊರತೆಗೆದುಕೊಳ್ಳಲು ಬಳಸುತ್ತದೆ.
- ಅನುವಾದ ಕೋರ್ Markdown ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ; ದೃಶ್ಯ ಪೈಪ್‌ಲೈನ್ `-img` ಬಳಸಿದಾಗ ಚಿತ್ರಗಳಿಂದ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.
- ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು `translations/<lang>/` (ಪಠ್ಯಕ್ಕಾಗಿ) ಮತ್ತು `translated_images/` (ಚಿತ್ರಗಳಿಗಾಗಿ) ಅಡಿಯಲ್ಲಿ ಸಂಘಟಿಸಲಾಗುತ್ತದೆ, ಮೂಲ ರಚನೆಯನ್ನು ಉಳಿಸುತ್ತದೆ.

### ಪ್ರಮುಖ ತಂತ್ರಜ್ಞಾನಗಳು ಮತ್ತು ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು

- Python 3.10–3.12, ಪ್ಯಾಕೇಜಿಂಗ್‌ಗಾಗಿ Poetry
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- ದೃಶ್ಯ: Azure AI Service (Computer Vision)
- HTTP ಮತ್ತು ಡೇಟಾ: `httpx`, `pydantic`
- ಇಮೇಜಿಂಗ್: `pillow`, `opencv-python`, `matplotlib`
- ಟೂಲಿಂಗ್: `pytest`, `black`, `ruff`

## ಸೆಟಪ್ ಕಮಾಂಡ್‌ಗಳು

### ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- Python 3.10–3.12
- Azure ಚಂದಾದಾರಿಕೆ (ಐಚ್ಛಿಕ, Azure AI ಸೇವೆಗಳಿಗೆ)
- LLM/ದೃಶ್ಯ APIಗಳಿಗೆ ಇಂಟರ್ನೆಟ್ ಪ್ರವೇಶ (ಉದಾ., Azure OpenAI/OpenAI, Azure AI Vision)

### ಆಯ್ಕೆ A: Poetry (ಶಿಫಾರಸು)

```bash
# ಸಂಗ್ರಹದ ಮೂಲದಿಂದ
pip install poetry
poetry install

# ಪೋಯಟ್ರಿ ಮೂಲಕ ಯಾವುದೇ ಆಜ್ಞೆಯನ್ನು ಚಲಾಯಿಸಿ
poetry run translate --help
```

### ಆಯ್ಕೆ B: pip/venv

```bash
# ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಿ
python -m venv .venv
# ವಿಂಡೋಸ್
.venv\\Scripts\\activate
# ಲಿನಕ್ಸ್/ಮ್ಯಾಕ್‌ಒಎಸ್
# source .venv/bin/activate

# ಅವಶ್ಯಕತೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
pip install -r requirements.txt

# (ಐಚ್ಛಿಕ) ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗಾಗಿ ಸಂಪಾದಿಸಬಹುದಾದ ಸ್ಥಾಪನೆ
pip install -e .
```

## ಅಂತಿಮ ಬಳಕೆದಾರರ ಬಳಕೆ

### Docker (ಪ್ರಕಟಿತ ಇಮೇಜ್)

```bash
# GHCR ನಿಂದ ಸಾರ್ವಜನಿಕ ಚಿತ್ರವನ್ನು ಎಳೆಯಿರಿ
docker pull ghcr.io/azure/co-op-translator:latest

# ಪ್ರಸ್ತುತ ಫೋಲ್ಡರ್ ಅನ್ನು ಮೌಂಟ್ ಮಾಡಲಾಗಿದ್ದು ಮತ್ತು .env ಒದಗಿಸಲಾಗಿದೆ (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# ಪವರ್ ಶೆಲ್
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

ಗಮನಿಸಿ:
- ಡೀಫಾಲ್ಟ್ ಎಂಟ್ರಿಪಾಯಿಂಟ್ `translate`. ಲಿಂಕ್ ಮೈಗ್ರೇಶನ್‌ಗಾಗಿ `--entrypoint migrate-links` ಅನ್ನು ಬದಲಾಯಿಸಿ.
- ಅನಾಮಧೇಯ ಡೌನ್‌ಲೋಡ್‌ಗಳಿಗೆ GHCR ಪ್ಯಾಕೇಜ್ ದೃಶ್ಯತೆ Public ಆಗಿರಬೇಕು.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### ಪರಿಸರ ಕಾನ್ಫಿಗರೇಶನ್

`.env` ಫೈಲ್ ಅನ್ನು ರೆಪೊಸಿಟರಿಯ ಮೂಲದಲ್ಲಿ ರಚಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಆಯ್ಕೆದ ಭಾಷಾ ಮಾದರಿಯು ಮತ್ತು (ಐಚ್ಛಿಕವಾಗಿ) ದೃಶ್ಯ ಸೇವೆಯುಗಾಗಿ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳು/ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಒದಗಿಸಿ. ಪೂರೈಕೆದಾರ‑ನಿರ್ದಿಷ್ಟ ಸೆಟಪ್‌ಗಾಗಿ, `getting_started/set-up-azure-ai.md` ನೋಡಿ.

### ಅಗತ್ಯವಿರುವ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳು

ಕನಿಷ್ಠ ಒಂದು LLM ಪೂರೈಕೆದಾರನನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕು. ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ, Azure AI Service ಅನ್ನು ಸಹ ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕು.

- Azure OpenAI (ಪಠ್ಯ ಅನುವಾದ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (ಪಠ್ಯ ಅನುವಾದ ಪರ್ಯಾಯ):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ಐಚ್ಛಿಕ)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI ಪೂರೈಕೆದಾರನನ್ನು ಬಳಸಿದಾಗ ಅಗತ್ಯವಿದೆ)
  - `OPENAI_BASE_URL` (ಐಚ್ಛಿಕ; ಡೀಫಾಲ್ಟ್ `https://api.openai.com/v1`)

- Azure AI Service ಚಿತ್ರ ಪಠ್ಯ ಹೊರತೆಗೆದುಕೊಳ್ಳಲು (ಅಗತ್ಯವಿದೆ `-img` ಬಳಸಿದಾಗ):
  - `AZURE_AI_SERVICE_API_KEY` (ಆಗತ್ಯವಿದೆ) ಅಥವಾ ಹಳೆಯ `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env` ಉದಾಹರಣೆ:

```bash
# ಆಜೂರ್ AI ಸೇವೆ (ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# ಆಜೂರ್ ಓಪನ್AI (ಪ್ರಾಥಮಿಕ ಆಯ್ಕೆ)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ಓಪನ್AI (ಪರ್ಯಾಯ ಆಯ್ಕೆ)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # ಐಚ್ಛಿಕ
OPENAI_CHAT_MODEL_ID="gpt-4o"   # ಓಪನ್AI ಬಳಸುವಾಗ ಅಗತ್ಯವಿದೆ
OPENAI_BASE_URL="https://api.openai.com/v1" # ಐಚ್ಛಿಕ
```

ಗಮನಿಸಿ:

- ಸಾಧನವು ಲಭ್ಯವಿರುವ LLM ಪೂರೈಕೆದಾರನನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ; Azure OpenAI ಅಥವಾ OpenAI ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ.
- ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ `AZURE_AI_SERVICE_API_KEY` ಮತ್ತು `AZURE_AI_SERVICE_ENDPOINT` ಎರಡೂ ಅಗತ್ಯವಿದೆ.
- ಅಗತ್ಯವಿರುವ ವ್ಯತ್ಯಾಸಗಳು ಇಲ್ಲದಿದ್ದರೆ CLI ಸ್ಪಷ್ಟವಾದ ದೋಷವನ್ನು ತೋರಿಸುತ್ತದೆ.

## ಅಭಿವೃದ್ಧಿ ಕಾರ್ಯಪ್ರವಾಹ

- ಮೂಲ ಕೋಡ್ `src/co_op_translator` ಅಡಿಯಲ್ಲಿ ಇರುತ್ತದೆ; ಪರೀಕ್ಷೆಗಳು `tests/` ಅಡಿಯಲ್ಲಿ.
- ಪ್ರಾಥಮಿಕ CLIಗಳು (ಎಂಟ್ರಿ ಪಾಯಿಂಟ್‌ಗಳ ಮೂಲಕ ಸ್ಥಾಪಿಸಲಾಗಿದೆ):

```bash
# ವಿಷಯವನ್ನು ಒಂದು ಅಥವಾ ಹೆಚ್ಚು ಭಾಷೆಗಳಿಗೆ ಅನುವಾದಿಸಿ (ಅಂತರದಿಂದ ಬೇರ್ಪಡಿಸಿದ ಕೋಡ್‌ಗಳು)
translate -l "fr es de"

# ವಿಷಯದ ಪ್ರಕಾರ ನಿರ್ಬಂಧಿಸಿ
translate -l "ja" -md            # ಮಾತ್ರ ಮಾರ್ಕ್‌ಡೌನ್
translate -l "ko" -nb            # ಮಾತ್ರ ನೋಟುಪುಸ್ತಕಗಳು
translate -l "zh" -md -img       # ಮಾರ್ಕ್‌ಡೌನ್ + ಚಿತ್ರಗಳು

# ಹಿಂದಿನ ಅನುವಾದಿತ ನೋಟುಪುಸ್ತಕಗಳು/ಮಾರ್ಕ್‌ಡೌನ್‌ನಲ್ಲಿ ಲಿಂಕ್‌ಗಳನ್ನು ನವೀಕರಿಸಿ
migrate-links -l "all" -y
```

ಹೆಚ್ಚುವರಿ ಬಳಕೆ ಡಾಕ್ಸ್‌ಗಳನ್ನು `getting_started/` ನಲ್ಲಿ ನೋಡಿ.

## ಪರೀಕ್ಷಾ ಸೂಚನೆಗಳು

ರೆಪೊಸಿಟರಿಯ ಮೂಲದಿಂದ ಪರೀಕ್ಷೆಗಳನ್ನು ಚಲಾಯಿಸಿ. ಕೆಲವು ಪರೀಕ್ಷೆಗಳಿಗೆ API ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳು ಅಗತ್ಯವಿರಬಹುದು; ಅವುಗಳನ್ನು ಅಗತ್ಯವಿದ್ದಾಗ ಬಿಟ್ಟುಬಿಡಿ.

```bash
# ಸಂಪೂರ್ಣ ಪರೀಕ್ಷಾ ಶ್ರೇಣಿಯನ್ನು ಚಲಾಯಿಸಿ
pytest

# ಲೈವ್ API ಕೀಗಳನ್ನು ಅಗತ್ಯವಿರುವ ಪರೀಕ್ಷೆಗಳನ್ನು ಬಿಟ್ಟುಬಿಡಿ
pytest -m "not api_key_required"

# ಉಪಸಮೂಹವನ್ನು ಚಲಾಯಿಸಿ
pytest tests/co_op_translator -k "name_substring"
```

ಐಚ್ಛಿಕ ಕವರೆಜ್ (ಅಗತ್ಯವಿದೆ `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # ./htmlcov ಗೆ ಔಟ್‌ಪುಟ್ ಮಾಡುತ್ತದೆ
```

## ಕೋಡ್ ಶೈಲಿ ಮಾರ್ಗಸೂಚಿಗಳು

- ಫಾರ್ಮ್ಯಾಟರ್: Black (`pyproject.toml` ನಲ್ಲಿ ಕಾನ್ಫಿಗರ್ ಮಾಡಲಾಗಿದೆ, ಸಾಲದ ಉದ್ದ 88)
- ಲಿಂಟರ್: Ruff (`pyproject.toml` ನಲ್ಲಿ ಕಾನ್ಫಿಗರ್ ಮಾಡಲಾಗಿದೆ, ಸಾಲದ ಉದ್ದ 120)
- ಪ್ರಕಾರ ಪರಿಶೀಲನೆ: mypy (ಕಾನ್ಫಿಗರೇಶನ್ ಇದೆ; ಸ್ಥಾಪಿತವಾದರೆ ಸಕ್ರಿಯಗೊಳಿಸಿ)

ಕಮಾಂಡ್‌ಗಳು:

```bash
# ಪೋಯಟ್ರಿ ಮೂಲಕ
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # ಸುರಕ್ಷಿತ ಸ್ವಯಂ‑ಸರಿಪಡಿಸುವಿಕೆಗಳು

# ಅಥವಾ ಜಾಗತಿಕ ಸಾಧನಗಳೊಂದಿಗೆ
black .
ruff check .
```

Python ಮೂಲಗಳನ್ನು `src/` ಅಡಿಯಲ್ಲಿ, ಪರೀಕ್ಷೆಗಳನ್ನು `tests/` ಅಡಿಯಲ್ಲಿ ಸಂಘಟಿಸಿ ಮತ್ತು ಪ್ಯಾಕೇಜ್ ನೆಮ್ಸ್‌ಪೇಸ್ (`co_op_translator.*`) ಒಳಗೆ ಸ್ಪಷ್ಟವಾದ ಇಂಪೋರ್ಟ್‌ಗಳನ್ನು ಪ್ರಾಧಾನ್ಯತೆ ನೀಡಿ.

## ನಿರ್ಮಾಣ ಮತ್ತು ನಿಯೋಜನೆ

ನಿರ್ಮಾಣ ಆರ್ಕ್ಟಿಫ್ಯಾಕ್ಟ್‌ಗಳನ್ನು `dist/` ಗೆ ಪ್ರಕಟಿಸಲಾಗುತ್ತದೆ.

```bash
# ನಿರ್ಮಾಣ (ಕಾವ್ಯ)
poetry build

# ನಿರ್ಮಿತ ಚಕ್ರದ ಸ್ಥಳೀಯ ಸ್ಥಾಪನೆ
pip install dist/*.whl
```

GitHub Actions ಮೂಲಕ ಸ್ವಯಂಚಾಲಿತ ವ್ಯವಸ್ಥೆ ಬೆಂಬಲಿತವಾಗಿದೆ; ನೋಡಿ:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### ಕಂಟೈನರ್ ಇಮೇಜ್ (GHCR)

- ಅಧಿಕೃತ ಇಮೇಜ್: `ghcr.io/azure/co-op-translator:<tag>`
- ಟ್ಯಾಗ್‌ಗಳು: `latest` (main ನಲ್ಲಿ), ಅರ್ಥಪೂರ್ಣ ಟ್ಯಾಗ್‌ಗಳು `vX.Y.Z`, ಮತ್ತು `sha` ಟ್ಯಾಗ್
- ಮಲ್ಟಿ-ಆರ್ಕ್: `linux/amd64, linux/arm64` Buildx ಮೂಲಕ ಬೆಂಬಲಿತವಾಗಿದೆ
- Dockerfile ಮಾದರಿ: ಬಿಲ್ಡ್ ಅವಶ್ಯಕತೆಗಳ ವೀಲ್‌ಗಳನ್ನು ಬಿಲ್ಡರ್‌ನಲ್ಲಿ ನಿರ್ಮಿಸಿ (`build-essential` ಮತ್ತು `python3-dev` ಸಹಿತ) ಮತ್ತು ರನ್‌ಟೈಮ್‌ನಲ್ಲಿ ಸ್ಥಳೀಯ ವೀಲ್‌ಹೌಸ್‌ನಿಂದ ಸ್ಥಾಪಿಸಿ (`pip install --no-index --find-links=/wheels`)
- ಕಾರ್ಯಪ್ರವಾಹ: `.github/workflows/docker-publish.yml` GHCR ಗೆ ನಿರ್ಮಿಸಿ ಮತ್ತು ಪುಷ್ ಮಾಡುತ್ತದೆ

## ಭದ್ರತಾ ಪರಿಗಣನೆಗಳು

- API ಕೀಗಳು ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು `.env` ಅಥವಾ ನಿಮ್ಮ CI ಸೀಕ್ರೆಟ್‌ ಸ್ಟೋರ್‌ನಲ್ಲಿ ಇಡಿ; ಸೀಕ್ರೆಟ್‌ಗಳನ್ನು ಎಂದಿಗೂ ಕಮಿಟ್ ಮಾಡಬೇಡಿ.
- ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ, Azure AI Vision ಕೀಗಳು/ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳು ಅಗತ್ಯವಿದೆ; ಇಲ್ಲದಿದ್ದರೆ `-img` ಅನ್ನು ಬಿಟ್ಟುಬಿಡಿ.
- ದೊಡ್ಡ ಅನುವಾದ ಬ್ಯಾಚ್‌ಗಳನ್ನು ಚಲಾಯಿಸುವಾಗ ಪೂರೈಕೆದಾರನ ಕೋಟಾ/ರೇಟ್ ಲಿಮಿಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.

## ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಮಾರ್ಗಸೂಚಿಗಳು

### ಸಲ್ಲಿಸುವ ಮೊದಲು

1. **ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ:**
   - ಪ್ರಭಾವಿತ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಚಲಾಯಿಸಿ
   - ಎಲ್ಲಾ ಸೆಲ್‌ಗಳು ದೋಷವಿಲ್ಲದೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ ಎಂದು ಖಚಿತಪಡಿಸಿ
   - ಔಟ್‌ಪುಟ್‌ಗಳು ಸೂಕ್ತವಾಗಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ

2. **ದಸ್ತಾವೇಜು ನವೀಕರಣಗಳು:**
   - ಹೊಸ ಪರಿಕಲ್ಪನೆಗಳನ್ನು ಸೇರಿಸುವಾಗ `README.md` ಅನ್ನು ನವೀಕರಿಸಿ
   - ಸಂಕೀರ್ಣ ಕೋಡಿಗಾಗಿ ನೋಟ್ಬುಕ್‌ಗಳಲ್ಲಿ ಕಾಮೆಂಟ್‌ಗಳನ್ನು ಸೇರಿಸಿ
   - Markdown ಸೆಲ್‌ಗಳು ಉದ್ದೇಶವನ್ನು ವಿವರಿಸುತ್ತವೆ ಎಂದು ಖಚಿತಪಡಿಸಿ

3. **ಫೈಲ್ ಬದಲಾವಣೆಗಳು:**
   - `.env` ಫೈಲ್‌ಗಳನ್ನು ಕಮಿಟ್ ಮಾಡಬೇಡಿ (`.env.example` ಬಳಸಿ)
   - `venv/` ಅಥವಾ `__pycache__/` ಡೈರೆಕ್ಟರಿಗಳನ್ನು ಕಮಿಟ್ ಮಾಡಬೇಡಿ
   - ಪರಿಕಲ್ಪನೆಗಳನ್ನು ತೋರಿಸುವಾಗ ನೋಟ್ಬುಕ್ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಉಳಿಸಿ
   - ತಾತ್ಕಾಲಿಕ ಫೈಲ್‌ಗಳು ಮತ್ತು ಬ್ಯಾಕಪ್ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು (`*-backup.ipynb`) ತೆಗೆದುಹಾಕಿ

4. **ಶೈಲಿ ಮತ್ತು ಫಾರ್ಮ್ಯಾಟಿಂಗ್:**
   - ಶೈಲಿ ಮತ್ತು ಫಾರ್ಮ್ಯಾಟಿಂಗ್ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಅನುಸರಿಸಿ
   - ಶೈಲಿ ಮತ್ತು ಫಾರ್ಮ್ಯಾಟಿಂಗ್ ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಶೀಲಿಸಲು `poetry run black .` ಮತ್ತು `poetry run ruff check .` ಅನ್ನು ಚಲಾಯಿಸಿ

5. **ಪರೀಕ್ಷೆಗಳನ್ನು ಮತ್ತು CLI ಸಹಾಯವನ್ನು ಸೇರಿಸಿ/ನವೀಕರಿಸಿ:**
   - ವರ್ತನೆ ಬದಲಾಯಿಸುವಾಗ ಪರೀಕ್ಷೆಗಳನ್ನು ಸೇರಿಸಿ ಅಥವಾ ನವೀಕರಿಸಿ
   - ಬದಲಾವಣೆಗಳೊಂದಿಗೆ CLI ಸಹಾಯವನ್ನು ಸತತವಾಗಿ ಇಡಿ

### ಕಮಿಟ್ ಸಂದೇಶ ಮತ್ತು ಮರ್ಜ್ ತಂತ್ರ

ನಾವು ಡೀಫಾಲ್ಟ್ ಆಗಿ Squash ಮತ್ತು Merge ಅನ್ನು ಬಳಸುತ್ತೇವೆ. ಅಂತಿಮ squash ಕಮಿಟ್ ಸಂದೇಶವು ಈ ರೀತಿ ಇರಬೇಕು:

```bash
<type>: <description> (#<ಪಿಆರ್ ಸಂಖ್ಯೆ>)
```

ಅನುಮತಿಸಿದ ಪ್ರಕಾರಗಳು:
- `Docs` — ದಸ್ತಾವೇಜು ನವೀಕರಣಗಳು
- `Build` — ಬಿಲ್ಡ್ ವ್ಯವಸ್ಥೆ, ಅವಲಂಬನೆಗಳು, ಕಾನ್ಫಿಗರೇಶನ್/CI
- `Core` — ಕೋರ್ ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ವೈಶಿಷ್ಟ್ಯಗಳು (ಉದಾ., `src/co_op_translator/core`)

ಉದಾಹರಣೆಗಳು:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

ಗಮನಿಸಿ:
- PR ಶೀರ್ಷಿಕೆಗಳು ಲೇಬಲ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪೂರ್ವಪ್ರತ್ಯಯವನ್ನು ಹೊಂದಿರುತ್ತವೆ; ತಯಾರಿಸಿದ ಪೂರ್ವಪ್ರತ್ಯಯವು ಸರಿಯಾಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.

### PR ಶೀರ್ಷಿಕೆ ಸ್ವರೂಪ

ಸ್ಪಷ್ಟ, ಸಂಕ್ಷಿಪ್ತ ಶೀರ್ಷಿಕೆಗಳನ್ನು ಬಳಸಿ. ಅಂತಿಮ squash ಕಮಿಟ್‌ನಂತೆಯೇ ರಚನೆಯನ್ನು ಪ್ರಾಧಾನ್ಯತೆ ನೀಡಿ:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## ಡಿಬಗಿಂಗ್ ಮತ್ತು ತೊಂದರೆ ಪರಿಹಾರ

- ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಪರಿಹಾರಗಳು: `getting_started/troubleshooting.md`
- ಬೆಂಬಲಿತ ಭಾಷೆಗಳು ಮತ್ತು ಟಿಪ್ಪಣಿಗಳು (ಫಾಂಟ್‌ಗಳು/ತಿಳಿದಿರುವ ಸಮಸ್ಯೆಗಳನ್ನು ಒಳಗೊಂಡಂತೆ): `getting_started/supported-languages.md`
- ನೋಟ್ಬುಕ್‌ಗಳಲ್ಲಿ ಲಿಂಕ್ ಸಮಸ್ಯೆಗಳಿಗೆ, ಪುನಃ ಚಲಾಯಿಸಿ: `migrate-links -l "all" -y`

## ಏಜೆಂಟ್‌ಗಳಿಗೆ ಟಿಪ್ಪಣಿಗಳು

- ಪುನರಾವೃತ್ತಿ ಪರಿಸರಗಳಿಗಾಗಿ Poetry ಅನ್ನು ಪ್ರಾಧಾನ್ಯತೆ ನೀಡಿ; ಇಲ್ಲದಿದ್ದರೆ `requirements.txt` ಬಳಸಿ.
- CIನಲ್ಲಿ CLIಗಳನ್ನು ಕರೆಸುವಾಗ, ಅಗತ್ಯವಿರುವ ಸೀಕ್ರೆಟ್‌ಗಳನ್ನು ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳ ಮೂಲಕ ಅಥವಾ `.env` ಇಂಜೆಕ್ಷನ್ ಮೂಲಕ ಒದಗಿಸಿ.
- Monorepo ಬಳಕೆದಾರರಿಗಾಗಿ, ಈ ರೆಪೊ ಸ್ವತಂತ್ರ ಪ್ಯಾಕೇಜ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ; ಯಾವುದೇ ಉಪ‑ಪ್ಯಾಕೇಜ್ ಸಮನ್ವಯ ಅಗತ್ಯವಿಲ್ಲ.

- ಮಲ್ಟಿ-ಆರ್ಕ್ ಮಾರ್ಗಸೂಚಿ: ARM ಬಳಕೆದಾರರು (Apple Silicon/ARM ಸರ್ವರ್‌ಗಳು) ಗುರಿಯಾಗಿದ್ದಾಗ `linux/arm64` ಅನ್ನು ಇಡಿ; ಇಲ್ಲದಿದ್ದರೆ ಸರಳತೆಗೆ `linux/amd64` ಮಾತ್ರ ಸಾಕಷ್ಟು.
- ಬಳಕೆದಾರರನ್ನು `README.md` ನಲ್ಲಿ Docker Quick Start ಗೆ ಸೂಚಿಸಿ, ಅವರು ಕಂಟೈನರ್ ಬಳಕೆಯನ್ನು ಪ್ರಾಧಾನ್ಯತೆ ನೀಡಿದಾಗ; Bash ಮತ್ತು PowerShell ರೂಪಾಂತರಗಳನ್ನು ಸೇರಿಸಿ, ಉಲ್ಲೇಖದ ವ್ಯತ್ಯಾಸಗಳ ಕಾರಣದಿಂದ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->