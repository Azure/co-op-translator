# Конфігурація

Co-op Translator вимагає одного провайдера мовної моделі. Для перекладу зображень додатково потрібен Azure AI Vision.

Налаштування зчитуються з змінних оточення. Для локальних проєктів помістіть їх у файл `.env` в корені проєкту.

Для налаштування ресурсів Azure див. [Налаштування Azure AI](azure-ai-setup.md).

## Локальне середовище виконання

Перед запуском CLI локально використовуйте віртуальне середовище. Co-op Translator підтримує Python 3.10–3.12.

Для звичайного використання CLI встановіть опублікований пакет у віртуальному середовищі:

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

Для розробки репозиторію встановіть залежності з кореня проєкту замість цього:

```bash
poetry install
poetry run translate --help
```

Після того, як CLI стане доступним, налаштуйте одного провайдера мовної моделі в `.env`.

## Вибір провайдера

Інструмент автоматично визначає провайдерів у такому порядку:

1. Azure OpenAI
2. OpenAI

Якщо жоден з провайдерів не налаштований, `translate`, `evaluate`, `migrate-links`, і `run_translation` зазнають невдачі під час перевірок конфігурації. `co-op-review` і `run_review` — це детерміністичні перевірки обслуговування і не потребують облікових даних провайдера.

## Azure OpenAI

Використовуйте Azure OpenAI, коли ваша модель розгорнута в Azure AI Foundry або Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Перевірка підключення використовує endpoint, API key, API version, і deployment name перед початком перекладу.

## OpenAI

Використовуйте OpenAI, коли викликаєте OpenAI API безпосередньо.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # необов'язковий
OPENAI_BASE_URL="..."        # необов'язковий
```

`OPENAI_CHAT_MODEL_ID` обов'язковий, оскільки перекладачу потрібна явна чат-модель для викликів API.

## Azure AI Vision

Переклад зображень вимагає Azure AI Vision, щоб інструмент міг витягнути текст із зображень перед їх перекладом.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Якщо для перекладу зображень вибрано `-img`, `images=True`, або відсутній фільтр типу вмісту, інструмент перевіряє конфігурацію Vision перед початком перекладу.

## Кілька наборів облікових даних

Шар конфігурації підтримує кілька наборів облікових даних шляхом додавання однакового індексу до змінних:

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

Кожен набір має бути повним. Перевірка стану обирає робочий набір перед початком перекладу.

## Вимоги до команд

| Команда або API | Потрібен LLM | Потрібен Vision | Примітки |
| --- | --- | --- | --- |
| `translate -md` | Так | Ні | Перекладає лише Markdown. |
| `translate -nb` | Так | Ні | Перекладає лише ноутбуки. |
| `translate -img` | Так | Так | Перекладає лише зображення. |
| `translate` без прапорців типу | Так | Так | Режим за замовчуванням включає Markdown, ноутбуки та зображення. |
| `evaluate` | Так | Ні | Використовує оцінювання LLM, якщо не вибрано `--fast`. |
| `migrate-links` | Так | Ні | Виконує міграцію посилань, але все одно запускає спільні перевірки конфігурації. |
| `co-op-review` | Ні | Ні | Запускає детерміністичні перевірки структури перекладу, актуальності, Markdown, ноутбуків і локальних посилань. |
| `run_translation(markdown=True)` | Так | Ні | Програмний переклад Markdown. |
| `run_translation(images=True)` | Так | Так | Програмний переклад зображень. |
| `run_review(...)` | Ні | Ні | Програмний детерміністичний огляд. |

## Каталоги виводу

Каталог за замовчуванням для текстових перекладів:

```text
translations/<language-code>/<source-relative-path>
```

Каталог за замовчуванням для перекладених зображень:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API може перевизначити ці каталоги за допомогою `translations_dir` і `image_dir`.