<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:36:01+00:00",
  "source_file": "AGENTS.md",
  "language_code": "uk"
}
-->
# AGENTS.md

## Огляд проєкту

Co‑op Translator — це інструмент командного рядка на Python і workflow для GitHub Actions, який перекладає Markdown-файли, Jupyter-ноутбуки та текст на зображеннях на різні мови. Він організовує результати у папки для кожної мови та підтримує синхронізацію перекладів із вихідним контентом. Проєкт структурований як бібліотека під керуванням Poetry з CLI-інтерфейсами.

### Огляд архітектури

- Точки входу CLI (`translate`, `migrate-links`, `evaluate`) викликають єдиний CLI, який розподіляє потоки перекладу, міграції посилань та оцінки.
- Завантажувач конфігурації читає `.env` і автоматично визначає постачальника LLM (Azure OpenAI або OpenAI), а за потреби — постачальника vision (Azure AI Service) для витягу тексту із зображень.
- Ядро перекладу обробляє Markdown і ноутбуки; vision-пайплайн витягує текст із зображень при використанні `-img`.
- Результати організовуються у `translations/<lang>/` для тексту та `translated_images/` для зображень із збереженням оригінальної структури.

### Основні технології та фреймворки

- Python 3.10–3.12, Poetry для пакування
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP та дані: `httpx`, `pydantic`
- Обробка зображень: `pillow`, `opencv-python`, `matplotlib`
- Інструменти: `pytest`, `black`, `ruff`

## Команди для налаштування

### Необхідні умови

- Python 3.10–3.12
- Підписка Azure (необов’язково, для сервісів Azure AI)
- Доступ до інтернету для LLM/Vision API (наприклад, Azure OpenAI/OpenAI, Azure AI Vision)

### Варіант A: Poetry (рекомендовано)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Варіант B: pip/venv

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

## Використання для кінцевих користувачів

### Docker (опублікований образ)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Примітки:
- Стандартна точка входу — `translate`. Для міграції посилань використовуйте `--entrypoint migrate-links`.
- Переконайтеся, що пакет GHCR має статус Public для анонімного завантаження.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Налаштування середовища

Створіть файл `.env` у корені репозиторію та вкажіть облікові дані/ендпоінти для обраної вами мовної моделі та (за бажанням) сервісу vision. Для налаштування конкретного постачальника дивіться `getting_started/set-up-azure-ai.md`.

### Обов’язкові змінні середовища

Має бути налаштований хоча б один постачальник LLM. Для перекладу зображень також потрібен Azure AI Service.

- Azure OpenAI (переклад тексту):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (альтернатива для перекладу тексту):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (необов’язково)
  - `OPENAI_CHAT_MODEL_ID` (обов’язково при використанні OpenAI)
  - `OPENAI_BASE_URL` (необов’язково; стандартно `https://api.openai.com/v1`)

- Azure AI Service для витягу тексту із зображень (обов’язково при використанні `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (бажано) або застарілий `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Приклад фрагменту `.env`:

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

Примітки:

- Інструмент автоматично визначає доступного постачальника LLM; налаштуйте або Azure OpenAI, або OpenAI.
- Для перекладу зображень потрібні обидва: `AZURE_AI_SERVICE_API_KEY` і `AZURE_AI_SERVICE_ENDPOINT`.
- CLI видасть зрозумілу помилку, якщо обов’язкові змінні не задані.

## Робочий процес розробки

- Вихідний код знаходиться у `src/co_op_translator`, тести — у `tests/`.
- Основні CLI (встановлюються через entry points):

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

Дивіться додаткову документацію з використання у `getting_started/`.

## Інструкції з тестування

Запускайте тести з кореня репозиторію. Деякі тести можуть вимагати API-ключі; пропускайте їх за потреби.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Додатково покриття (потрібен `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Вимоги до стилю коду

- Форматер: Black (налаштовано у `pyproject.toml`, довжина рядка 88)
- Лінтер: Ruff (налаштовано у `pyproject.toml`, довжина рядка 120)
- Перевірка типів: mypy (конфігурація присутня; увімкніть, якщо встановлено)

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

Розміщуйте Python-код у `src/`, тести — у `tests/`, і надавайте перевагу явним імпортам у просторі імен пакета (`co_op_translator.*`).

## Збірка та деплой

Зібрані артефакти публікуються у `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Автоматизація через GitHub Actions підтримується; дивіться:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Контейнерний образ (GHCR)

- Офіційний образ: `ghcr.io/azure/co-op-translator:<tag>`
- Теги: `latest` (на main), семантичні теги типу `vX.Y.Z`, а також тег `sha`
- Multi-arch: `linux/amd64, linux/arm64` підтримуються через Buildx
- Шаблон Dockerfile: збірка wheel-залежностей у builder (з `build-essential` і `python3-dev`) та встановлення з локального wheelhouse у runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` збирає та пушить у GHCR

## Міркування щодо безпеки

- Зберігайте API-ключі та ендпоінти у `.env` або у сховищі секретів CI; ніколи не комітьте секрети.
- Для перекладу зображень потрібні ключі/ендпоінти Azure AI Vision; інакше не використовуйте `-img`.
- Перевіряйте квоти/ліміти постачальника при великих пакетах перекладу.

## Вимоги до Pull Request

### Перед відправкою

1. **Перевірте свої зміни:**
   - Повністю запустіть змінені ноутбуки
   - Переконайтеся, що всі комірки виконуються без помилок
   - Перевірте, що результати коректні

2. **Оновлення документації:**
   - Оновіть `README.md` при додаванні нових концепцій
   - Додавайте коментарі у ноутбуках для складного коду
   - Переконайтеся, що markdown-комірки пояснюють призначення

3. **Зміни у файлах:**
   - Не комітьте `.env` (використовуйте `.env.example`)
   - Не комітьте каталоги `venv/` або `__pycache__/`
   - Зберігайте результати ноутбуків, якщо вони демонструють концепції
   - Видаляйте тимчасові файли та резервні ноутбуки (`*-backup.ipynb`)

4. **Стиль і форматування:**
   - Дотримуйтесь вимог до стилю та форматування
   - Запустіть `poetry run black .` і `poetry run ruff check .` для перевірки стилю та форматування

5. **Додайте/оновіть тести та допомогу CLI:**
   - Додавайте або оновлюйте тести при зміні поведінки
   - Підтримуйте CLI-допомогу відповідно до змін


### Формат комітів і стратегія злиття

Використовується Squash and Merge за замовчуванням. Підсумкове повідомлення squash-коміту має відповідати формату:

```bash
<type>: <description> (#<PR number>)
```

Дозволені типи:
- `Docs` — оновлення документації
- `Build` — система збірки, залежності, конфігурація/CI
- `Core` — основна функціональність і фічі (наприклад, `src/co_op_translator/core`)

Приклади:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Примітки:
- Заголовки PR часто автоматично отримують префікс за лейблом; перевіряйте, чи префікс коректний.

### Формат заголовка PR

Використовуйте чіткі, лаконічні заголовки. Віддавайте перевагу структурі, як у фінальному squash-коміті:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Відлагодження та вирішення проблем

- Поширені проблеми та рішення: `getting_started/troubleshooting.md`
- Підтримувані мови та примітки (включно зі шрифтами/відомими проблемами): `getting_started/supported-languages.md`
- Для проблем із посиланнями у ноутбуках перезапустіть: `migrate-links -l "all" -y`

## Примітки для агентів

- Віддавайте перевагу Poetry для відтворюваних середовищ; інакше використовуйте `requirements.txt`.
- При запуску CLI у CI передавайте необхідні секрети через змінні середовища або ін’єкцію `.env`.
- Для користувачів монорепозиторіїв цей репозиторій є самостійним пакетом; координація із підпакетами не потрібна.

- Multi-arch: залишайте `linux/arm64`, якщо ціль — ARM-користувачі (Apple Silicon/ARM-сервери); інакше для простоти достатньо лише `linux/amd64`.
- Направляйте користувачів до Docker Quick Start у `README.md`, якщо вони віддають перевагу контейнерам; додавайте Bash і PowerShell варіанти через різницю у лапках.

---

**Застереження**:
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.