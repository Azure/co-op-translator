<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:33:54+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bg"
}
-->
# AGENTS.md

## Преглед на проекта

Co‑op Translator е инструмент на Python за команден ред и GitHub Actions workflow, който превежда Markdown файлове, Jupyter тетрадки и текст от изображения на множество езици. Организира изходните файлове в папки за всеки език и поддържа синхронизация между преводите и оригиналното съдържание. Проектът е структуриран като библиотека, управлявана с Poetry, с CLI входни точки.

### Архитектурен преглед

- CLI входните точки (`translate`, `migrate-links`, `evaluate`) стартират унифициран CLI, който разпределя към потоци за превод, миграция на връзки и оценка.
- Зареждачът на конфигурация чете `.env` и автоматично разпознава LLM доставчика (Azure OpenAI или OpenAI) и, ако е поискано, доставчика за визуално разпознаване (Azure AI Service) за извличане на текст от изображения.
- Ядрото за превод обработва Markdown и тетрадки; визуалната верига извлича текст от изображения, когато се използва `-img`.
- Изходните файлове се организират в `translations/<lang>/` за текст и `translated_images/` за изображения, като се запазва оригиналната структура.

### Основни технологии и рамки

- Python 3.10–3.12, Poetry за пакетиране
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Визия: Azure AI Service (Computer Vision)
- HTTP и данни: `httpx`, `pydantic`
- Обработка на изображения: `pillow`, `opencv-python`, `matplotlib`
- Инструменти: `pytest`, `black`, `ruff`

## Команди за настройка

### Предварителни изисквания

- Python 3.10–3.12
- Абонамент за Azure (по избор, за Azure AI услуги)
- Интернет достъп за LLM/Vision API (напр. Azure OpenAI/OpenAI, Azure AI Vision)

### Вариант A: Poetry (препоръчително)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Вариант B: pip/venv

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

## Използване от крайни потребители

### Docker (публикуван образ)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Бележки:
- Стандартната входна точка е `translate`. Може да се промени с `--entrypoint migrate-links` за миграция на връзки.
- Уверете се, че видимостта на GHCR пакета е Public за анонимни изтегляния.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Конфигуриране на средата

Създайте `.env` файл в основната директория на репото и въведете данни за достъп/крайни точки за избрания от вас езиков модел и (по желание) за визуалната услуга. За настройка според доставчика вижте `getting_started/set-up-azure-ai.md`.

### Задължителни променливи на средата

Трябва да е конфигуриран поне един LLM доставчик. За превод на изображения трябва да е конфигуриран и Azure AI Service.

- Azure OpenAI (превод на текст):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (алтернатива за превод на текст):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (по избор)
  - `OPENAI_CHAT_MODEL_ID` (задължително при използване на OpenAI доставчик)
  - `OPENAI_BASE_URL` (по избор; по подразбиране е `https://api.openai.com/v1`)

- Azure AI Service за извличане на текст от изображения (задължително при използване на `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (препоръчително) или старо `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Примерен `.env` фрагмент:

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

Бележки:

- Инструментът автоматично разпознава наличния LLM доставчик; конфигурирайте или Azure OpenAI, или OpenAI.
- Превод на изображения изисква и `AZURE_AI_SERVICE_API_KEY`, и `AZURE_AI_SERVICE_ENDPOINT`.
- CLI ще даде ясно съобщение за грешка, ако липсват задължителни променливи.

## Работен процес за разработка

- Изходният код е в `src/co_op_translator`; тестовете са в `tests/`.
- Основни CLI (инсталирани чрез entry points):

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

Вижте допълнителна документация за използване в `getting_started/`.

## Инструкции за тестване

Стартирайте тестовете от основната директория на репото. Някои тестове изискват API ключове; пропуснете ги при нужда.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

По желание покритие (изисква `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Насоки за стил на кода

- Форматиране: Black (конфигуриран в `pyproject.toml`, дължина на ред 88)
- Линтер: Ruff (конфигуриран в `pyproject.toml`, дължина на ред 120)
- Проверка на типове: mypy (има конфигурация; активирайте ако е инсталиран)

Команди:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Организирайте Python изходния код в `src/`, тестовете в `tests/`, и предпочитайте явни импорти в пространството на пакета (`co_op_translator.*`).

## Създаване и публикуване

Генерираните артефакти се публикуват в `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Автоматизация чрез GitHub Actions се поддържа; вижте:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Контейнерен образ (GHCR)

- Официален образ: `ghcr.io/azure/co-op-translator:<tag>`
- Тагове: `latest` (на main), семантични тагове като `vX.Y.Z`, и `sha` таг
- Multi-arch: `linux/amd64, linux/arm64` се поддържат чрез Buildx
- Dockerfile модел: изгражда dependency wheels в builder (с `build-essential` и `python3-dev`) и инсталира от локален wheelhouse в runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` изгражда и качва в GHCR

## Съображения за сигурност

- Дръжте API ключовете и крайните точки в `.env` или в CI хранилището за тайни; никога не ги качвайте в репото.
- За превод на изображения са нужни ключове/крайни точки за Azure AI Vision; иначе пропуснете `-img`.
- Проверявайте квотите/лимитите на доставчика при големи партиди за превод.

## Насоки за Pull Request

### Преди изпращане

1. **Тествайте промените си:**
   - Стартирайте всички засегнати тетрадки докрай
   - Уверете се, че всички клетки се изпълняват без грешки
   - Проверете дали изходите са коректни

2. **Актуализации на документацията:**
   - Обновете `README.md` при добавяне на нови концепции
   - Добавете коментари в тетрадките за сложен код
   - Уверете се, че markdown клетките обясняват целта

3. **Промени по файлове:**
   - Не качвайте `.env` файлове (използвайте `.env.example`)
   - Не качвайте `venv/` или `__pycache__/` директории
   - Запазвайте изходите на тетрадките, когато показват концепции
   - Премахнете временни файлове и резервни тетрадки (`*-backup.ipynb`)

4. **Стил и форматиране:**
   - Следвайте насоките за стил и форматиране
   - Стартирайте `poetry run black .` и `poetry run ruff check .` за проверка на стил и форматиране

5. **Добавяне/актуализиране на тестове и CLI помощ:**
   - Добавете или обновете тестове при промяна на поведение
   - Поддържайте CLI помощта в синхрон с промените


### Формат на commit съобщенията и стратегия за сливане

Използваме Squash and Merge по подразбиране. Финалното squash commit съобщение трябва да следва:

```bash
<type>: <description> (#<PR number>)
```

Позволени типове:
- `Docs` — актуализации по документацията
- `Build` — build система, зависимости, конфигурация/CI
- `Core` — основна функционалност и нови възможности (напр. `src/co_op_translator/core`)

Примери:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Бележки:
- Заглавията на PR често се попълват автоматично според етикетите; проверете дали генерираният префикс е коректен.

### Формат на PR заглавията

Използвайте ясни, кратки заглавия. Предпочитайте същата структура като финалния squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Откриване и отстраняване на проблеми

- Чести проблеми и решения: `getting_started/troubleshooting.md`
- Поддържани езици и бележки (вкл. шрифтове/известни проблеми): `getting_started/supported-languages.md`
- За проблеми с връзки в тетрадки, стартирайте отново: `migrate-links -l "all" -y`

## Бележки за агентите

- Предпочитайте Poetry за възпроизводими среди; иначе използвайте `requirements.txt`.
- При стартиране на CLI в CI, подавайте нужните тайни чрез променливи на средата или `.env` файл.
- За потребители на монорепо, това репо е самостоятелен пакет; не се изисква координация с под‑пакети.

- Насоки за multi-arch: поддържайте `linux/arm64`, ако има ARM потребители (Apple Silicon/ARM сървъри); иначе само `linux/amd64` е достатъчно за простота.
- Насочвайте потребителите към Docker Quick Start в `README.md`, ако предпочитат контейнер; включете Bash и PowerShell варианти заради разликите в кавичките.

---

**Отказ от отговорност**:
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали от използването на този превод.