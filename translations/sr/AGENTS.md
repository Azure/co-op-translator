<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:34:19+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sr"
}
-->
## Преглед пројекта

Co‑op Translator је Python алат за командну линију и GitHub Actions workflow који преводи Markdown фајлове, Jupyter свеске и текст са слика на више језика. Излазе организује у фасцикле специфичне за језик и одржава синхронизацију превода са изворним садржајем. Пројекат је структуриран као библиотека којом управља Poetry са CLI улазним тачкама.

### Преглед архитектуре

- CLI улазне тачке (`translate`, `migrate-links`, `evaluate`) позивају јединствени CLI који распоређује на процесе превођења, миграције линкова и евалуације.
- Лоудер конфигурације чита `.env` и аутоматски детектује LLM провајдера (Azure OpenAI или OpenAI) и, ако је затражено, vision провајдера (Azure AI Service) за екстракцију текста са слика.
- Језгро за превођење обрађује Markdown и свеске; vision pipeline екстрахује текст са слика када се користи `-img`.
- Излази се организују у `translations/<lang>/` за текст и `translated_images/` за слике, уз очување оригиналне структуре.

### Кључне технологије и оквири

- Python 3.10–3.12, Poetry за паковање
- CLI: `click`
- LLM/AI SDK-ови: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP и подаци: `httpx`, `pydantic`
- Обрада слика: `pillow`, `opencv-python`, `matplotlib`
- Алатке: `pytest`, `black`, `ruff`

## Команде за подешавање

### Предуслови

- Python 3.10–3.12
- Azure претплата (опционо, за Azure AI сервисе)
- Приступ интернету за LLM/Vision API-је (нпр. Azure OpenAI/OpenAI, Azure AI Vision)

### Опција А: Poetry (препоручено)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Опција Б: pip/venv

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

## Коришћење за крајње кориснике

### Docker (објављена слика)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Напомене:
- Подразумевани entrypoint је `translate`. Промените са `--entrypoint migrate-links` за миграцију линкова.
- Проверите да је GHCR пакет видљив као Public за анонимно преузимање.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Конфигурисање окружења

Креирајте `.env` фајл у корену репозиторијума и унесите креденцијале/ендпоинте за изабрани модел језика и (опционо) vision сервис. За подешавање специфично за провајдера, погледајте `getting_started/set-up-azure-ai.md`.

### Обавезне променљиве окружења

Мора бити конфигурисан бар један LLM провајдер. За превођење слика, мора бити конфигурисан и Azure AI Service.

- Azure OpenAI (превођење текста):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (алтернатива за превођење текста):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (опционо)
  - `OPENAI_CHAT_MODEL_ID` (обавезно када се користи OpenAI провајдер)
  - `OPENAI_BASE_URL` (опционо; подразумевано је `https://api.openai.com/v1`)

- Azure AI Service за екстракцију текста са слика (обавезно када се користи `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (препоручено) или застарело `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Пример `.env` исечка:

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

Напомене:

- Алат аутоматски детектује доступног LLM провајдера; конфигуришите или Azure OpenAI или OpenAI.
- Превођење слика захтева и `AZURE_AI_SERVICE_API_KEY` и `AZURE_AI_SERVICE_ENDPOINT`.
- CLI ће пријавити јасну грешку ако недостају обавезне променљиве.

## Развојни ток

- Изворни код се налази у `src/co_op_translator`; тестови у `tests/`.
- Главни CLI-ји (инсталирани преко entry points):

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

Погледајте додатну документацију о коришћењу у `getting_started/`.

## Упутство за тестирање

Покрените тестове из корена репозиторијума. Неки тестови захтевају API креденцијале; прескочите их по потреби.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Опциона покривеност (захтева `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Водич за стил кода

- Форматер: Black (подешен у `pyproject.toml`, дужина линије 88)
- Линтер: Ruff (подешен у `pyproject.toml`, дужина линије 120)
- Провера типова: mypy (конфигурација постоји; омогућите ако је инсталиран)

Команде:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Организујте Python изворе у `src/`, тестове у `tests/`, и преферирајте експлицитне увозе унутар package namespace-а (`co_op_translator.*`).

## Градња и деплојмент

Артефакти градње се објављују у `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Аутоматизација преко GitHub Actions је подржана; погледајте:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Слика контејнера (GHCR)

- Званична слика: `ghcr.io/azure/co-op-translator:<tag>`
- Тагови: `latest` (на main), семантички тагови као `vX.Y.Z`, и `sha` таг
- Multi-arch: `linux/amd64, linux/arm64` подржано преко Buildx
- Dockerfile шаблон: градите dependency wheel-ове у builder-у (са `build-essential` и `python3-dev`) и инсталирајте из локалног wheelhouse-а у runtime-у (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` гради и шаље на GHCR

## Безбедносна разматрања

- Чувајте API кључеве и ендпоинте у `.env` или у CI secrets store-у; никада не комитујте тајне.
- За превођење слика, потребни су Azure AI Vision кључеви/ендпоинти; у супротном изоставите `-img`.
- Проверите квоте/лимите провајдера када покрећете велике серије превода.

## Водич за Pull Request-ове

### Пре слања

1. **Тестирајте измене:**
   - Покрените све релевантне свеске до краја
   - Проверите да све ћелије раде без грешке
   - Проверите да су излази одговарајући

2. **Ажурирање документације:**
   - Ажурирајте `README.md` ако додајете нове концепте
   - Додајте коментаре у свеске за сложен код
   - Обезбедите да markdown ћелије објашњавају сврху

3. **Измене фајлова:**
   - Избегавајте комитовање `.env` фајлова (користите `.env.example`)
   - Не комитујте `venv/` или `__pycache__/` директоријуме
   - Задржите излазе у свескама када илуструју концепте
   - Уклоните привремене фајлове и backup свеске (`*-backup.ipynb`)

4. **Стил и форматирање:**
   - Пратите смернице за стил и форматирање
   - Покрените `poetry run black .` и `poetry run ruff check .` да проверите стил и формат

5. **Додајте/ажурирајте тестове и CLI help:**
   - Додајте или ажурирајте тестове када мењате понашање
   - Држите CLI help усклађен са изменама


### Формат поруке комита и стратегија спајања

Користимо Squash and Merge као подразумевано. Коначна squash порука комита треба да прати:

```bash
<type>: <description> (#<PR number>)
```

Дозвољени типови:
- `Docs` — ажурирања документације
- `Build` — build систем, зависности, конфигурација/CI
- `Core` — основна функционалност и карактеристике (нпр. `src/co_op_translator/core`)

Примери:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Напомене:
- Наслови PR-ова се често аутоматски префиксирају на основу label-а; проверите да је генерисани префикс исправан.

### Формат наслова PR-а

Користите јасне, концизне наслове. Преферирајте исту структуру као и коначни squash комит:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Отклањање грешака и решавање проблема

- Чести проблеми и решења: `getting_started/troubleshooting.md`
- Подржани језици и напомене (укључујући фонтове/познате проблеме): `getting_started/supported-languages.md`
- За проблеме са линковима у свескама, поново покрените: `migrate-links -l "all" -y`

## Напомене за агенте

- Преферирајте Poetry за репродуцибилна окружења; у супротном користите `requirements.txt`.
- Када покрећете CLI-је у CI-ју, обезбедите потребне тајне преко променљивих окружења или `.env` injection-а.
- За кориснике у монорепо окружењима, овај репо делује као самостални пакет; није потребна координација са под‑пакетима.

- Multi-arch смернице: задржите `linux/arm64` када су ARM корисници (Apple Silicon/ARM сервери) циљ; у супротном је само `linux/amd64` прихватљиво ради једноставности.
- Упутите кориснике на Docker Quick Start у `README.md` ако преферирају коришћење контејнера; укључите Bash и PowerShell варијанте због разлика у наводницима.

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала употребом овог превода.