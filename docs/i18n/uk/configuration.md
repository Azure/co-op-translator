# Конфігурація

Co-op Translator вимагає одного постачальника мовної моделі. Для перекладу зображень додатково потрібен Azure AI Vision.

Конфігурація читається з змінних оточення. Для локальних проєктів розмістіть їх у файлі `.env` у корені проєкту.

Для налаштування ресурсів Azure див. [Налаштування Azure AI](azure-ai-setup.md).

## Локальне налаштування середовища виконання

Використовуйте віртуальне середовище перед запуском CLI локально. Co-op Translator підтримує Python 3.11–3.14.

Для звичайного використання CLI встановіть опублікований пакет у віртуальному середовищі:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Розробка репозиторію

Для розробки репозиторію натомість встановіть залежності з кореня проєкту:

```bash
poetry install
poetry run translate --help
```

Після того як CLI стане доступним, налаштуйте одного постачальника мовної моделі в `.env`.

## Вибір постачальника

Інструмент автоматично виявляє постачальників у такому порядку:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Переклад вимагає облікових даних постачальника, за винятком попередніх переглядів, таких як `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` і `run_review` — це детерміновані операції з обслуговування й не вимагають облікових даних постачальника.

## Бекенд клієнта моделі

Починаючи з Co-op Translator 0.22.0, Azure OpenAI, OpenAI і Anthropic за замовчуванням використовують Microsoft Agent Framework. Для звичайного використання налаштування бекенду не потрібне.

Semantic Kernel тимчасово залишається доступним для сумісності. Щоб вибрати його явно, встановіть:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Використання Semantic Kernel спричиняє попередження про застарівання. Планується перевести Semantic Kernel у необов’язкову залежність у версії 0.23.0 і видалити інтеграцію у 0.24.0, залежно від результатів сумісності та відгуків користувачів. Anthropic вимагає `agent-framework`; явний вибір `semantic-kernel` для Anthropic призведе до помилки конфігурації. Неприпустимі значення призводять до збою під час ініціалізації перекладача з підтримкою постачальника, замість того щоб тихо повертатися до іншого варіанту. Слідкуйте за впровадженням і повідомляйте про блокуючі проблеми в [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Використовуйте Azure OpenAI, коли ваша модель розгорнута в Azure AI Foundry або Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Перевірка підключення використовує endpoint, ключ API, версію API та ім'я розгортання перед початком перекладу.

## OpenAI

Використовуйте OpenAI при прямому виклику OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` є обов'язковим, оскільки перекладачу потрібна явна чат-модель для викликів API.

Залиште `OPENAI_ORG_ID` та `OPENAI_BASE_URL` незаданими для типового налаштування. Додавайте ідентифікатор організації лише якщо ваш обліковий запис його потребує, або базову URL-адресу лише при використанні користувацького endpoint. Не копіюйте заповнювачі для необов'язкових налаштувань.

## Anthropic Claude

Використовуйте Anthropic при прямому виклику Claude API. Створіть [ключ Anthropic API](https://platform.claude.com/docs/en/get-started) і оберіть підтримуваний [ID моделі Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` та `ANTHROPIC_MODEL` є обов'язковими. Не потрібно встановлювати `CO_OP_TRANSLATOR_MODEL_CLIENT`; за замовчуванням використовується Agent Framework.

Залиште `ANTHROPIC_BASE_URL` незаданою для Anthropic API. Встановлюйте її лише при використанні користувацького endpoint.

`ANTHROPIC_MAX_TOKENS` за замовчуванням дорівнює `8192`, що залишає місце для сценаріїв із щільними токенами, таких як Meitei Mayek. Зменшіть його, якщо ваша модель або сумісний з Anthropic endpoint обмежує вивід нижче цього значення.

## Azure AI Vision

Переклад зображень вимагає Azure AI Vision, щоб інструмент міг витягти текст із зображень перед тим, як налаштована мовна модель його перекладе. Anthropic може перекладати витягнутий текст так само, як Azure OpenAI або OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Якщо для перекладу зображень вибрано `-img`, `images=True` або не встановлено фільтр типу контенту, інструмент перевіряє конфігурацію Vision перед початком перекладу.

## Кілька наборів облікових даних

Шар конфігурації підтримує кілька наборів облікових даних шляхом додавання суфікса з однаковим індексом до змінних:

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

Кожен набір має бути повним. Перевірка стану обирає робочий набір перед тим, як продовжиться переклад.

OpenAI та Anthropic підтримують ту саму конвенцію суфіксів. Тримайте кожну змінну в наборі облікових даних з тим самим суфіксом, включаючи необов'язкові значення, такі як `OPENAI_BASE_URL_1` або `ANTHROPIC_BASE_URL_1`.

## Вимоги до команд

| Команда або API | Потрібен LLM | Потрібен Vision | Примітки |
| --- | --- | --- | --- |
| `translate -md` | Так | Ні | Перекладає лише Markdown. |
| `translate -nb` | Так | Ні | Перекладає лише ноутбуки. |
| `translate -img` | Так | Так | Перекладає лише зображення. |
| `translate` без прапорців типу | Так | Так | Режим за замовчуванням включає Markdown, ноутбуки та зображення. |
| `evaluate` | Так | Ні | Використовує оцінювання LLM, якщо не вибрано `--fast`. |
| `migrate-links` | Ні | Ні | Виконує локальну міграцію посилань без викликів до постачальника. |
| `co-op-review` | Ні | Ні | Виконує детерміновані перевірки структури перекладу, актуальності, Markdown, ноутбуків та локальних посилань. |
| `run_translation(markdown=True)` | Так | Ні | Програмний переклад Markdown. |
| `run_translation(images=True)` | Так | Так | Програмний переклад зображень. |
| `run_review(...)` | Ні | Ні | Програмний детермінований огляд. |

## Каталоги виводу

Вихід за замовчуванням для текстового перекладу:

```text
translations/<language-code>/<source-relative-path>
```

Вихід за замовчуванням для перекладених зображень:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API може переозначити ці каталоги за допомогою `translations_dir` та `image_dir`.