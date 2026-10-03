# Конфигурация

Co-op Translator изисква един доставчик на езикови модели. За превод на изображения допълнително е необходим Azure AI Vision.

Конфигурацията се чете от системните променливи на средата. За локални проекти ги поставете в `.env` файл в корена на проекта.

За настройка на Azure ресурси вижте [Настройка на Azure AI](azure-ai-setup.md).

## Локална настройка на средата

Използвайте виртуална среда преди да стартирате CLI локално. Co-op Translator поддържа Python 3.11 до 3.14.

За нормална употреба на CLI инсталирайте публикувания пакет във виртуална среда:

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

### Разработка на репозитория

За разработка на репозитория инсталирайте зависимостите от корена на проекта вместо това:

```bash
poetry install
poetry run translate --help
```

След като CLI е наличен, конфигурирайте един доставчик на езиков модел в `.env`.

## Избор на доставчик

Инструментът автоматично разпознава доставчиците в следния ред:

1. Azure OpenAI
2. OpenAI
3. Anthropic

За превод са необходими идентификационни данни на доставчика, с изключение на визуализации като `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, и `run_review` са детерминистични операции за поддръжка и не изискват идентификационни данни на доставчика.

## Модул за клиентски бекенд

От версия Co-op Translator 0.22.0 нататък, Azure OpenAI, OpenAI и Anthropic използват Microsoft Agent Framework по подразбиране. Не е необходимо да задавате бекенд за нормална употреба.

Semantic Kernel остава временно наличен за съвместимост. За да го изберете явно, задайте:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Използването на Semantic Kernel генерира предупреждение за остаряване. Планирано е пакетът да премести Semantic Kernel като опционална зависимост в 0.23.0 и да премахне интеграцията в 0.24.0, в зависимост от резултатите от съвместимостта и обратната връзка от потребителите. Anthropic изисква `agent-framework`; явно задаване на `semantic-kernel` с Anthropic ще доведе до грешка в конфигурацията. Невалидните стойности ще доведат до грешка по време на инициализацията на преводача, поддържан от доставчик, вместо да се прави тихо резервно превключване. Следете разгръщането и докладвайте блокиращи проблеми в [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Използвайте Azure OpenAI когато вашият модел е разположен в Azure AI Foundry или Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Проверката за свързаност използва endpoint, API ключ, версия на API и име на деплоймънт преди започване на превода.

## OpenAI

Използвайте OpenAI при директни извиквания на OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` е задължителен, тъй като преводачът се нуждае от явен чат модел за API извиквания.

Оставете `OPENAI_ORG_ID` и `OPENAI_BASE_URL` незададени за подразбиращата се конфигурация. Добавете идентификатор на организация само ако акаунтът ви го изисква, или базов URL само когато използвате персонализиран endpoint. Не копирайте примерните стойности за опционалните настройки.

## Anthropic Claude

Използвайте Anthropic при директни извиквания на Claude API. Създайте [Anthropic API ключ](https://platform.claude.com/docs/en/get-started) и изберете поддържан [ID на модела Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` и `ANTHROPIC_MODEL` са задължителни. Не е необходимо да задавате `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework е стандартният бекенд.

Оставете `ANTHROPIC_BASE_URL` незададена за Anthropic API. Задавайте го само когато използвате персонализиран endpoint.

`ANTHROPIC_MAX_TOKENS` по подразбиране е `8192`, което оставя място за скриптове с плътност на токените като Meitei Mayek. Намалете го, ако вашият модел или Anthropic-съвместим endpoint ограничава изхода под тази стойност.

## Azure AI Vision

Преводът на изображения изисква Azure AI Vision, така че инструментът да може да извлече текст от изображението преди конфигурираният езиков модел да го преведе. Anthropic може да преведе извлечения текст, както правят Azure OpenAI или OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ако преводът на изображения е избран с `-img`, `images=True` или липса на филтър за тип съдържание, инструментът валидира конфигурацията на Vision преди да започне превода.

## Няколко набора от идентификационни данни

Слойът за конфигурация поддържа няколко набора от идентификационни данни чрез добавяне на един и същ индекс като суфикс към променливите:

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

Всеки набор трябва да е пълен. Проверката на здравето (health check) избира работещ набор преди да продължи преводът.

OpenAI и Anthropic поддържат същата конвенция за суфикси. Дръжте всяка променлива в набор от идентификационни данни със същия суфикс, включително опционални стойности като `OPENAI_BASE_URL_1` или `ANTHROPIC_BASE_URL_1`.

## Изисквания за командите

| Команда или API | Изисква LLM | Изисква Vision | Бележки |
| --- | --- | --- | --- |
| `translate -md` | Да | Не | Превежда само Markdown. |
| `translate -nb` | Да | Не | Превежда само notebooks. |
| `translate -img` | Да | Да | Превежда само изображения. |
| `translate` без флагове за тип | Да | Да | По подразбиране режимът включва Markdown, notebooks и изображения. |
| `evaluate` | Да | Не | Използва LLM оценяване, освен ако не е избран `--fast`. |
| `migrate-links` | Не | Не | Извършва локална миграция на връзки без повиквания към доставчици. |
| `co-op-review` | Не | Не | Изпълнява детерминистични проверки за структура на превода, актуалност, Markdown, notebook и локални връзки. |
| `run_translation(markdown=True)` | Да | Не | Програмен превод на Markdown. |
| `run_translation(images=True)` | Да | Да | Програмен превод на изображения. |
| `run_review(...)` | Не | Не | Програмна детерминистична проверка. |

## Изходни директории

По подразбиране изход за текстов превод:

```text
translations/<language-code>/<source-relative-path>
```

По подразбиране изход за преведени изображения:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API може да презапише тези директории с `translations_dir` и `image_dir`.