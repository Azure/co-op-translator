# Configuration

Co-op Translator изисква един доставчик на езиков модел. За превод на изображения допълнително се изисква Azure AI Vision.

Конфигурацията се чете от променливи на средата. За локални проекти ги поставете в файл `.env` в корена на проекта.

За настройка на ресурси в Azure вижте [Настройка на Azure AI](azure-ai-setup.md).

## Local runtime setup

Използвайте виртуална среда преди да стартирате CLI локално. Co-op Translator поддържа Python 3.10 до 3.12.

За нормално използване на CLI инсталирайте публикувания пакет във виртуална среда:

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

За разработка на репозитория инсталирайте зависимостите от корена на проекта вместо това:

```bash
poetry install
poetry run translate --help
```

След като CLI е наличен, конфигурирайте един доставчик на езиков модел в `.env`.

## Provider selection

Инструментът автоматично открива доставчиците в следния ред:

1. Azure OpenAI
2. OpenAI

Ако нито един доставчик не е конфигуриран, `translate`, `evaluate`, `migrate-links`, и `run_translation` ще се провалят по време на проверките на конфигурацията. `co-op-review` и `run_review` са детерминистични проверки за поддръжка и не изискват идентификационни данни на доставчика.

## Azure OpenAI

Използвайте Azure OpenAI когато вашият модел е разположен в Azure AI Foundry или Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Проверката за свързаност използва крайната точка, API ключа, версията на API и името на разполагането преди да започне преводът.

## OpenAI

Използвайте OpenAI когато извиквате OpenAI API директно.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # по избор
OPENAI_BASE_URL="..."        # по избор
```

`OPENAI_CHAT_MODEL_ID` е задължителна, защото преводачът се нуждае от явен чат модел за извиквания към API-то.

## Azure AI Vision

Преводът на изображения изисква Azure AI Vision, за да може инструментът да извлича текст от изображенията преди да ги преведе.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ако е избран превод на изображения с `-img`, `images=True`, или липсва филтър за тип съдържание, инструментът валидира конфигурацията на Vision преди започване на превода.

## Multiple credential sets

Слойът за конфигурация поддържа множество комплекти от идентификационни данни чрез добавяне на индекс като суфикс към променливите:

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

Всеки комплект трябва да е пълен. Проверката на здравето избира работещ комплект преди да продължи преводът.

## Command requirements

| Команда или API | Нужен LLM | Нужен Vision | Забележки |
| --- | --- | --- | --- |
| `translate -md` | Да | Не | Превежда само Markdown. |
| `translate -nb` | Да | Не | Превежда само notebooks. |
| `translate -img` | Да | Да | Превежда само изображения. |
| `translate` with no type flags | Да | Да | По подразбиране режимът включва Markdown, notebooks и изображения. |
| `evaluate` | Да | Не | Използва LLM оценяване освен ако не е избран `--fast`. |
| `migrate-links` | Да | Не | Извършва миграция на връзки, но все пак изпълнява споделените проверки на конфигурацията. |
| `co-op-review` | Не | Не | Изпълнява детерминирани проверки на структурата на превода, актуалността, Markdown, notebooks и локалните връзки. |
| `run_translation(markdown=True)` | Да | Не | Програмен превод на Markdown. |
| `run_translation(images=True)` | Да | Да | Програмен превод на изображения. |
| `run_review(...)` | Не | Не | Програмен детерминистичен преглед. |

## Output directories

По подразбиране изход за текстов превод:

```text
translations/<language-code>/<source-relative-path>
```

По подразбиране изход за преведени изображения:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API може да замени тези директории с `translations_dir` и `image_dir`.