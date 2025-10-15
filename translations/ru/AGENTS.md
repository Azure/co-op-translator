<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:19:56+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ru"
}
-->
# AGENTS.md

## Обзор проекта

Co‑op Translator — это инструмент командной строки на Python и workflow для GitHub Actions, предназначенный для перевода Markdown-файлов, Jupyter-ноутбуков и текста на изображениях на разные языки. Переводы сохраняются в папках, соответствующих языкам, и синхронизируются с исходным содержимым. Проект оформлен как библиотека, управляемая Poetry, с CLI-точками входа.

### Обзор архитектуры

- Точки входа CLI (`translate`, `migrate-links`, `evaluate`) вызывают единый интерфейс, который распределяет задачи перевода, миграции ссылок и оценки.
- Загрузчик конфигурации читает `.env` и автоматически определяет поставщика LLM (Azure OpenAI или OpenAI), а при необходимости — поставщика vision (Azure AI Service) для извлечения текста с изображений.
- Ядро перевода работает с Markdown и ноутбуками; vision-пайплайн извлекает текст с изображений при использовании `-img`.
- Результаты сохраняются в `translations/<lang>/` для текста и `translated_images/` для изображений с сохранением исходной структуры.

### Основные технологии и фреймворки

- Python 3.10–3.12, Poetry для управления пакетами
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP и данные: `httpx`, `pydantic`
- Работа с изображениями: `pillow`, `opencv-python`, `matplotlib`
- Инструменты: `pytest`, `black`, `ruff`

## Команды для установки

### Необходимые условия

- Python 3.10–3.12
- Подписка Azure (опционально, для сервисов Azure AI)
- Доступ в интернет для LLM/Vision API (например, Azure OpenAI/OpenAI, Azure AI Vision)

### Вариант A: Poetry (рекомендуется)

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

## Использование для конечных пользователей

### Docker (публичный образ)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Примечания:
- По умолчанию запускается `translate`. Для миграции ссылок используйте `--entrypoint migrate-links`.
- Убедитесь, что пакет GHCR доступен публично для анонимных загрузок.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Конфигурация окружения

Создайте файл `.env` в корне репозитория и укажите в нем учетные данные/эндпоинты для выбранной языковой модели и (опционально) vision-сервиса. Для настройки конкретного провайдера смотрите `getting_started/set-up-azure-ai.md`.

### Обязательные переменные окружения

Должен быть настроен хотя бы один провайдер LLM. Для перевода изображений также требуется Azure AI Service.

- Azure OpenAI (перевод текста):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (альтернатива для перевода текста):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (опционально)
  - `OPENAI_CHAT_MODEL_ID` (обязательно при использовании OpenAI)
  - `OPENAI_BASE_URL` (опционально; по умолчанию `https://api.openai.com/v1`)

- Azure AI Service для извлечения текста с изображений (обязательно при использовании `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (предпочтительно) или устаревший `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Пример фрагмента `.env`:

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

Примечания:

- Инструмент автоматически определяет доступного провайдера LLM; настройте либо Azure OpenAI, либо OpenAI.
- Для перевода изображений необходимы оба параметра: `AZURE_AI_SERVICE_API_KEY` и `AZURE_AI_SERVICE_ENDPOINT`.
- CLI выдаст понятную ошибку, если обязательные переменные не заданы.

## Процесс разработки

- Исходный код находится в `src/co_op_translator`, тесты — в `tests/`.
- Основные CLI (устанавливаются через entry points):

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

Дополнительную документацию по использованию смотрите в `getting_started/`.

## Инструкции по тестированию

Запускайте тесты из корня репозитория. Для некоторых тестов нужны API-ключи; при необходимости пропускайте их.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Опционально покрытие (требуется `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Руководство по стилю кода

- Форматтер: Black (настройка в `pyproject.toml`, длина строки 88)
- Линтер: Ruff (настройка в `pyproject.toml`, длина строки 120)
- Проверка типов: mypy (конфигурация присутствует; включайте при наличии)

Команды:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Организуйте исходники Python в `src/`, тесты — в `tests/`, и используйте явные импорты внутри пространства имен пакета (`co_op_translator.*`).

## Сборка и деплой

Собранные артефакты публикуются в `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Автоматизация через GitHub Actions поддерживается; смотрите:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Контейнерный образ (GHCR)

- Официальный образ: `ghcr.io/azure/co-op-translator:<tag>`
- Теги: `latest` (для main), семантические теги типа `vX.Y.Z`, и тег `sha`
- Multi-arch: поддержка `linux/amd64, linux/arm64` через Buildx
- Шаблон Dockerfile: сборка wheel-зависимостей в builder (с `build-essential` и `python3-dev`), установка из локального wheelhouse в runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` собирает и пушит в GHCR

## Вопросы безопасности

- Храните API-ключи и эндпоинты в `.env` или в хранилище секретов CI; никогда не коммитьте секреты.
- Для перевода изображений нужны ключи/эндпоинты Azure AI Vision; иначе не используйте `-img`.
- Проверяйте квоты/лимиты провайдера при больших пакетах переводов.

## Правила для Pull Request

### Перед отправкой

1. **Проверьте изменения:**
   - Полностью выполните измененные ноутбуки
   - Убедитесь, что все ячейки выполняются без ошибок
   - Проверьте корректность результатов

2. **Обновление документации:**
   - Обновите `README.md` при добавлении новых концепций
   - Добавляйте комментарии в ноутбуках для сложного кода
   - Убедитесь, что markdown-ячейки объясняют назначение

3. **Изменения файлов:**
   - Не коммитьте `.env` (используйте `.env.example`)
   - Не коммитьте директории `venv/` или `__pycache__/`
   - Сохраняйте вывод ноутбуков, если он демонстрирует концепции
   - Удаляйте временные файлы и резервные ноутбуки (`*-backup.ipynb`)

4. **Стиль и форматирование:**
   - Следуйте правилам стиля и форматирования
   - Запустите `poetry run black .` и `poetry run ruff check .` для проверки стиля и форматирования

5. **Добавление/обновление тестов и справки CLI:**
   - Добавляйте или обновляйте тесты при изменении поведения
   - Обновляйте справку CLI в соответствии с изменениями


### Формат сообщения коммита и стратегия слияния

Используется Squash and Merge по умолчанию. Итоговое сообщение squash-коммита должно быть в формате:

```bash
<type>: <description> (#<PR number>)
```

Допустимые типы:
- `Docs` — обновления документации
- `Build` — сборка, зависимости, конфигурация/CI
- `Core` — основная функциональность и фичи (например, `src/co_op_translator/core`)

Примеры:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Примечания:
- Заголовки PR часто автоматически получают префикс по метке; проверьте, что он корректен.

### Формат заголовка PR

Используйте четкие, лаконичные заголовки. Предпочитайте ту же структуру, что и для squash-коммита:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Отладка и решение проблем

- Частые проблемы и их решения: `getting_started/troubleshooting.md`
- Поддерживаемые языки и примечания (включая шрифты/известные проблемы): `getting_started/supported-languages.md`
- Для проблем с ссылками в ноутбуках перезапустите: `migrate-links -l "all" -y`

## Заметки для агентов

- Для воспроизводимых окружений используйте Poetry; иначе — `requirements.txt`.
- При запуске CLI в CI передавайте секреты через переменные окружения или подмену `.env`.
- Для пользователей монорепозитория этот репозиторий — самостоятельный пакет; координация с подпакетами не требуется.

- Для multi-arch: сохраняйте `linux/arm64`, если нужны пользователи ARM (Apple Silicon/ARM-серверы); иначе можно ограничиться `linux/amd64` для простоты.
- Направляйте пользователей к Docker Quick Start в `README.md`, если они предпочитают контейнеры; приводите варианты для Bash и PowerShell из-за различий в кавычках.

---

**Отказ от ответственности**:
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.