# Конфигурация

Co-op Translator требует одного поставщика языковой модели. Для перевода изображений дополнительно требуется Azure AI Vision.

Конфигурация считывается из переменных окружения. Для локальных проектов поместите их в файл `.env` в корне проекта.

Для настройки ресурсов Azure смотрите [Настройка Azure AI](azure-ai-setup.md).

## Локальная настройка среды выполнения

Используйте виртуальное окружение перед запуском CLI локально. Co-op Translator поддерживает Python 3.10 через 3.12.

Для обычного использования CLI установите опубликованный пакет внутри виртуального окружения:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Для разработки репозитория вместо этого установите зависимости из корня проекта:

```bash
poetry install
poetry run translate --help
```

После того как CLI станет доступен, настройте одного поставщика языковой модели в `.env`.

## Выбор провайдера

Инструмент автоматически обнаруживает провайдеров в следующем порядке:

1. Azure OpenAI
2. OpenAI

Если ни один из провайдеров не настроен, `translate`, `evaluate`, `migrate-links`, и `run_translation` завершатся с ошибкой во время проверок конфигурации. `co-op-review` и `run_review` — детерминированные проверки обслуживания и не требуют учетных данных провайдера.

## Azure OpenAI

Используйте Azure OpenAI, если ваша модель развернута в Azure AI Foundry или Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Проверка подключения использует endpoint, API key, API version и имя развертывания перед началом перевода.

## OpenAI

Используйте OpenAI при обращении напрямую к OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # необязательно
OPENAI_BASE_URL="..."        # необязательно
```

`OPENAI_CHAT_MODEL_ID` обязателен, потому что переводчику нужна явная чат-модель для вызовов API.

## Azure AI Vision

Перевод изображений требует Azure AI Vision, чтобы инструмент мог извлечь текст из изображений перед переводом.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Если для перевода изображений выбран параметр `-img`, `images=True`, или отсутствует фильтр по типу содержимого, инструмент проверяет конфигурацию Vision перед началом перевода.

## Несколько наборов учетных данных

Слой конфигурации поддерживает несколько наборов учетных данных путем добавления суффикса с одинаковым индексом к переменным:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Каждый набор должен быть полным. Проверка работоспособности выбирает рабочий набор перед продолжением перевода.

## Требования к командам

| Команда или API | Требуется LLM | Требуется Vision | Примечания |
| --- | --- | --- | --- |
| `translate -md` | Да | Нет | Переводит только Markdown. |
| `translate -nb` | Да | Нет | Переводит только блокноты. |
| `translate -img` | Да | Да | Переводит только изображения. |
| `translate` with no type flags | Да | Да | Режим по умолчанию включает Markdown, блокноты и изображения. |
| `evaluate` | Да | Нет | Использует оценку LLM, если не выбран `--fast`. |
| `migrate-links` | Да | Нет | Выполняет миграцию ссылок, но по-прежнему запускает общие проверки конфигурации. |
| `co-op-review` | Нет | Нет | Выполняет детерминированные проверки структуры перевода, актуальности, Markdown, блокнотов и локальных ссылок. |
| `run_translation(markdown=True)` | Да | Нет | Программный перевод Markdown. |
| `run_translation(images=True)` | Да | Да | Программный перевод изображений. |
| `run_review(...)` | Нет | Нет | Программная детерминированная проверка. |

## Каталоги вывода

Вывод перевода текста по умолчанию:

```text
translations/<language-code>/<source-relative-path>
```

Вывод переведённых изображений по умолчанию:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API может переопределить эти каталоги с помощью `translations_dir` и `image_dir`.