<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:35:28+00:00",
  "source_file": "AGENTS.md",
  "language_code": "my"
}
-->
## Project Overview

Co‑op Translator သည် Python command‑line tool တစ်ခုဖြစ်ပြီး GitHub Actions workflow ဖြင့် Markdown ဖိုင်များ၊ Jupyter notebooks များနှင့် ပုံထဲရှိစာသားများကို ဘာသာစကားအမျိုးမျိုးသို့ ဘာသာပြန်ပေးနိုင်သည်။ Output များကို ဘာသာစကားအလိုက် ဖိုလ်ဒါခွဲထားပြီး မူရင်းအကြောင်းအရာနှင့် အမြဲတမ်း sync ဖြစ်အောင် ထိန်းသိမ်းပေးသည်။ ဒီ project ကို Poetry ဖြင့် စီမံထားသော library အဖြစ် ဖွဲ့စည်းထားပြီး CLI entry point များပါဝင်သည်။

### Architecture overview

- CLI entry point များ (`translate`, `migrate-links`, `evaluate`) သည် တစ်ခုတည်းသော CLI ကို ခေါ်သုံးပြီး ဘာသာပြန်ခြင်း၊ link ပြောင်းခြင်း၊ အကဲဖြတ်ခြင်း စသည့် လုပ်ငန်းစဉ်များသို့ ခွဲဝေပေးသည်။
- Configuration loader သည် `.env` ကို ဖတ်ပြီး LLM provider (Azure OpenAI သို့မဟုတ် OpenAI) ကို အလိုအလျောက် ရွေးချယ်ပေးသည်။ ပုံထဲမှစာသားထုတ်ယူရန် vision provider (Azure AI Service) ကိုလည်း တောင်းဆိုပါက ရွေးချယ်ပေးနိုင်သည်။
- Translation core သည် Markdown နှင့် notebook များကို ကိုင်တွယ်သည်။ `-img` ကို သုံးပါက vision pipeline သည် ပုံထဲမှ စာသားကို ထုတ်ယူပေးသည်။
- Output များကို `translations/<lang>/` (စာသားများအတွက်) နှင့် `translated_images/` (ပုံများအတွက်) ထဲတွင် မူရင်းဖိုင်ဖွဲ့စည်းပုံအတိုင်း စုစည်းထားသည်။

### Key technologies and frameworks

- Python 3.10–3.12, Poetry (package စီမံမှု)
- CLI: `click`
- LLM/AI SDK များ: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP နှင့် data: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## Setup Commands

### မလိုအပ်မီ ပြင်ဆင်ရန်

- Python 3.10–3.12
- Azure subscription (optional, Azure AI services အတွက်)
- LLM/Vision API များသုံးရန် အင်တာနက်လိုအပ် (ဥပမာ - Azure OpenAI/OpenAI, Azure AI Vision)

### Option A: Poetry (အကြံပြုသည်)

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

### Docker (ထုတ်ဝေထားသော image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

မှတ်ချက်များ -
- မူရင်း entrypoint သည် `translate` ဖြစ်သည်။ Link ပြောင်းရန် `--entrypoint migrate-links` ဖြင့် override လုပ်နိုင်သည်။
- GHCR package visibility ကို Public ထားရန်လိုအပ်သည် (anonymous pull များအတွက်)။

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း

Repository root တွင် `.env` ဖိုင်တစ်ခု ဖန်တီးပြီး သင်ရွေးချယ်ထားသော language model နှင့် (လိုအပ်ပါက) vision service အတွက် credentials/endpoints ထည့်ပေးပါ။ Provider အလိုက် ပြင်ဆင်နည်းအတွက် `getting_started/set-up-azure-ai.md` ကိုကြည့်ပါ။

### လိုအပ်သော Environment Variables

အနည်းဆုံး LLM provider တစ်ခုကို ပြင်ဆင်ထားရမည်။ ပုံဘာသာပြန်ရန်အတွက် Azure AI Service ကိုလည်း ပြင်ဆင်ထားရမည်။

- Azure OpenAI (စာသားဘာသာပြန်ခြင်း) အတွက် -
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (စာသားဘာသာပြန်ခြင်း အစားထိုး) အတွက် -
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (optional)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI provider သုံးပါက လိုအပ်သည်)
  - `OPENAI_BASE_URL` (optional; မသတ်မှတ်ပါက `https://api.openai.com/v1`)

- ပုံထဲမှစာသားထုတ်ယူရန် Azure AI Service ( `-img` သုံးပါက လိုအပ်သည်) -
  - `AZURE_AI_SERVICE_API_KEY` (အကြံပြုသည်) သို့မဟုတ် အဟောင်း `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

ဥပမာ `.env` snippet -

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

မှတ်ချက်များ -

- Tool သည် ရရှိနိုင်သော LLM provider ကို အလိုအလျောက် ရွေးချယ်သည်။ Azure OpenAI သို့မဟုတ် OpenAI တစ်ခုခုကို ပြင်ဆင်ပါ။
- ပုံဘာသာပြန်ရန် `AZURE_AI_SERVICE_API_KEY` နှင့် `AZURE_AI_SERVICE_ENDPOINT` နှစ်ခုလုံးလိုအပ်သည်။
- လိုအပ်သော variable များ မရှိပါက CLI သည် error message တစ်ခု ထုတ်ပေးပါမည်။

## Development Workflow

- Source code ကို `src/co_op_translator` ထဲတွင်၊ test များကို `tests/` ထဲတွင် ထားပါ။
- အဓိက CLI များ (entry point များဖြင့် install လုပ်ထားသည်) -

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

အသေးစိတ် အသုံးပြုနည်းများကို `getting_started/` ထဲတွင် ကြည့်နိုင်သည်။

## Testing Instructions

Repository root မှ test များ run ပါ။ API credentials လိုအပ်သော test များရှိနိုင်သည်။ မလိုအပ်ပါက skip လုပ်နိုင်သည်။

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Optional coverage ( `coverage` လိုအပ်သည်) -

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Code Style Guidelines

- Formatter: Black (`pyproject.toml` ထဲတွင် configure ပြုလုပ်ထားသည်၊ line length 88)
- Linter: Ruff (`pyproject.toml` ထဲတွင် configure ပြုလုပ်ထားသည်၊ line length 120)
- Type checks: mypy (configuration ရှိပြီး၊ install လုပ်ထားပါက အသုံးပြုနိုင်သည်)

Commands -

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python source များကို `src/` ထဲတွင်၊ test များကို `tests/` ထဲတွင် ထားပါ။ Package namespace (`co_op_translator.*`) အတွင်း explicit import များကို ဦးစားပေးသုံးပါ။

## Build and Deployment

Build artifacts များကို `dist/` ထဲတွင် ထုတ်ထားသည်။

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions ဖြင့် အလိုအလျောက်လုပ်ဆောင်နိုင်သည်။ ကြည့်ရန် -

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- တရားဝင် image - `ghcr.io/azure/co-op-translator:<tag>`
- Tags - `latest` (main branch), semantic tags (`vX.Y.Z`), `sha` tag
- Multi-arch - `linux/amd64, linux/arm64` ကို Buildx ဖြင့် ထောက်ပံ့သည်
- Dockerfile pattern - builder တွင် dependency wheel များ build လုပ်ပြီး runtime တွင် local wheelhouse မှ install (`pip install --no-index --find-links=/wheels`)
- Workflow - `.github/workflows/docker-publish.yml` သည် GHCR သို့ build/push လုပ်သည်

## Security Considerations

- API key များနှင့် endpoint များကို `.env` သို့မဟုတ် CI secrets store ထဲတွင်သာ ထားပါ။ secrets များကို မည်သည့် commit မှာမဆို မထည့်ပါနှင့်။
- ပုံဘာသာပြန်ရန် Azure AI Vision key/endpoint များလိုအပ်သည်။ မသုံးပါက `-img` ကို မထည့်ပါနှင့်။
- Translation batch ကြီးများ run လုပ်မည်ဆိုပါက provider quota/rate limit များကို စစ်ဆေးပါ။

## Pull Request Guidelines

### တင်သွင်းမီ ပြင်ဆင်ရန်

1. **သင်ပြင်ဆင်ထားသောအရာများကို စမ်းသပ်ပါ -**
   - သက်ဆိုင်ရာ notebook များကို အပြည့်အစုံ run ပါ
   - Cell များ error မရှိဘဲ အကုန် run ပြီးကြောင်း စစ်ဆေးပါ
   - Output များ သင့်တော်ကြောင်း စစ်ဆေးပါ

2. **Documentation ပြင်ဆင်မှုများ -**
   - Concept အသစ်ထည့်ပါက `README.md` ကို update လုပ်ပါ
   - Code ရှုပ်ထွေးသောနေရာများတွင် notebook မှာ comment ထည့်ပါ
   - Markdown cell များတွင် ရည်ရွယ်ချက်ကို ရှင်းပြပါ

3. **File ပြောင်းလဲမှုများ -**
   - `.env` ဖိုင်များ commit မလုပ်ပါနှင့် (`.env.example` သုံးပါ)
   - `venv/` သို့မဟုတ် `__pycache__/` directory များ commit မလုပ်ပါနှင့်
   - Concept ပြသရန် notebook output များထားပါ
   - ယာယီဖိုင်များနှင့် backup notebook များ (`*-backup.ipynb`) ဖယ်ရှားပါ

4. **Style နှင့် formatting -**
   - Style နှင့် formatting guideline များကို လိုက်နာပါ
   - `poetry run black .` နှင့် `poetry run ruff check .` ကို run လုပ်၍ style/formatting ပြဿနာများစစ်ပါ

5. **Test နှင့် CLI help များ ထည့်/ပြင်ပါ -**
   - Behavior ပြောင်းလဲပါက test များ ထည့်/ပြင်ပါ
   - CLI help ကို ပြောင်းလဲမှုနှင့် ကိုက်ညီအောင် ထိန်းသိမ်းပါ

### Commit message နှင့် merge strategy

Squash and Merge ကို မူရင်းအနေနဲ့ သုံးသည်။ Final squash commit message သည် အောက်ပါပုံစံအတိုင်း ဖြစ်ရမည် -

```bash
<type>: <description> (#<PR number>)
```

ခွင့်ပြုသော type များ -
- `Docs` — documentation ပြင်ဆင်မှုများ
- `Build` — build system, dependency, configuration/CI
- `Core` — core လုပ်ဆောင်ချက်နှင့် feature များ (ဥပမာ - `src/co_op_translator/core`)

ဥပမာများ -
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

မှတ်ချက်များ -
- PR title များသည် label အပေါ်မူတည်၍ auto-prefix ဖြစ်နိုင်သည်။ ထုတ်ပေးသော prefix မှန်ကန်ကြောင်း စစ်ဆေးပါ။

### PR Title Format

ရှင်းလင်းပြတ်သားသော title များသုံးပါ။ Final squash commit ပုံစံအတိုင်း သုံးရန် ဦးစားပေးပါ -
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging and Troubleshooting

- ပုံမှန်ပြဿနာများနှင့် ဖြေရှင်းနည်းများ - `getting_started/troubleshooting.md`
- ထောက်ပံ့သောဘာသာစကားများနှင့် မှတ်ချက်များ (font/ပြဿနာများပါဝင်သည်) - `getting_started/supported-languages.md`
- Notebook များတွင် link ပြဿနာရှိပါက `migrate-links -l "all" -y` ဖြင့် ပြန်လည် run လုပ်ပါ

## Notes for Agents

- Reproducible environment များအတွက် Poetry ကို ဦးစားပေးသုံးပါ။ မသုံးနိုင်ပါက `requirements.txt` သုံးပါ။
- CI တွင် CLI များ run လုပ်ပါက လိုအပ်သော secrets များကို environment variable သို့မဟုတ် `.env` ဖြင့် ထည့်ပေးပါ။
- Monorepo သုံးသူများအတွက် ဒီ repo သည် standalone package အဖြစ်သာ သုံးနိုင်သည်။ sub-package coordination မလိုအပ်ပါ။

- Multi-arch အတွက် - ARM user (Apple Silicon/ARM server) များကို ဦးစားပေးပါက `linux/arm64` ထည့်ပါ။ မဟုတ်ပါက `linux/amd64` သာ ထည့်ထားလည်း ရသည်။
- Container သုံးလိုသူများအတွက် `README.md` ထဲရှိ Docker Quick Start ကို ညွှန်ပြပါ။ Bash နှင့် PowerShell အတွက် ကွဲပြားမှုရှိသဖြင့် နှစ်မျိုးလုံးပါဝင်အောင် ပြပါ။

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် ၎င်း၏ မူလဘာသာစကားတွင် အာဏာရှိသော ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များ၏ ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။