# Конфигурация

Co-op Translator требует одного поставщика языковой модели. Для перевода изображений дополнительно требуется Azure AI Vision.

Конфигурация считывается из переменных окружения. Для локальных проектов поместите их в файл `.env` в корне проекта.

Для настройки ресурсов Azure см. [Настройка Azure AI](azure-ai-setup.md).

## Локальная настройка среды выполнения

Перед запуском CLI локально используйте виртуальное окружение. Co-op Translator поддерживает Python 3.11–3.14.

Для обычного использования CLI установите опубликованный пакет внутри виртуального окружения:

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

### Разработка репозитория

Для разработки репозитория установите зависимости из корня проекта вместо этого:

```bash
poetry install
poetry run translate --help
```

После того как CLI станет доступным, настройте одного поставщика языковой модели в файле `.env`.

## Выбор поставщика

Инструмент автоматически определяет поставщиков в следующем порядке:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Для перевода требуются учётные данные поставщика, за исключением предварительных просмотров, таких как `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, и `run_review` — это детерминированные операции обслуживания и не требуют учётных данных поставщика.

## Бэкенд клиентской модели

Начиная с Co-op Translator 0.22.0, Azure OpenAI, OpenAI и Anthropic по умолчанию используют Microsoft Agent Framework. Для обычного использования настройка бэкенда не требуется.

Semantic Kernel остаётся доступным временно для совместимости. Чтобы выбрать его явно, установите:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Использование Semantic Kernel вызывает предупреждение об устаревании. Планируется перевести Semantic Kernel в опциональную зависимость в версии 0.23.0 и удалить интеграцию в 0.24.0, в зависимости от результатов совместимости и отзывов пользователей. Anthropic требует `agent-framework`; явный выбор `semantic-kernel` для Anthropic приведёт к ошибке конфигурации. Неверные значения приводят к отказу при инициализации переводчика с поддержкой провайдера, вместо тихого отката. Следите за внедрением и сообщайте о блокирующих проблемах в [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Используйте Azure OpenAI, когда ваша модель развернута в Azure AI Foundry или Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Проверка подключения использует конечную точку, ключ API, версию API и имя развертывания перед началом перевода.

## OpenAI

Используйте OpenAI при непосредственном обращении к OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` обязателен, потому что переводчику нужна явная модель чата для вызовов API.

Оставьте `OPENAI_ORG_ID` и `OPENAI_BASE_URL` неустановленными для настройки по умолчанию. Добавляйте идентификатор организации только если он требуется вашей учётной записи, а базовый URL — только при использовании пользовательского конечного пункта. Не копируйте значения-заполнители для необязательных настроек.

## Anthropic Claude

Используйте Anthropic при непосредственном обращении к Claude API. Создайте [ключ Anthropic API](https://platform.claude.com/docs/en/get-started) и выберите поддерживаемый [ID модели Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` и `ANTHROPIC_MODEL` обязательны. Устанавливать `CO_OP_TRANSLATOR_MODEL_CLIENT` не нужно; по умолчанию используется Agent Framework.

Оставьте `ANTHROPIC_BASE_URL` неустановленным для Anthropic API. Устанавливайте его только при использовании пользовательского конечного пункта.

`ANTHROPIC_MAX_TOKENS` по умолчанию равен `8192`, что оставляет место для скриптов с плотным распределением токенов, таких как Meitei Mayek. Уменьшите его, если ваша модель или совместимый с Anthropic endpoint ограничивает вывод ниже этого значения.

## Azure AI Vision

Перевод изображений требует Azure AI Vision, чтобы инструмент мог извлечь текст из изображений до того, как настроенная языковая модель выполнит перевод. Anthropic может переводить извлечённый текст так же, как Azure OpenAI или OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Если для перевода изображений выбран параметр `-img`, `images=True` или отсутствует фильтр типа содержимого, инструмент проверяет конфигурацию Vision перед началом перевода.

## Несколько наборов учётных данных

Слой конфигурации поддерживает несколько наборов учётных данных путём добавления суффикса с одинаковым индексом к переменным:

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

Каждый набор должен быть полным. Проверка состояния выбирает рабочий набор перед продолжением перевода.

OpenAI и Anthropic поддерживают ту же конвенцию суффиксов. Сохраняйте у всех переменных в наборе учётных данных один и тот же суффикс, включая необязательные значения, такие как `OPENAI_BASE_URL_1` или `ANTHROPIC_BASE_URL_1`.

## Требования к командам

| Команда или API | Требуется LLM | Требуется Vision | Примечания |
| --- | --- | --- | --- |
| `translate -md` | Да | Нет | Переводит только Markdown. |
| `translate -nb` | Да | Нет | Переводит только ноутбуки. |
| `translate -img` | Да | Да | Переводит только изображения. |
| `translate` без флагов типа | Да | Да | Режим по умолчанию включает Markdown, ноутбуки и изображения. |
| `evaluate` | Да | Нет | Использует оценку LLM, если не выбран `--fast`. |
| `migrate-links` | Нет | Нет | Выполняет локальную миграцию ссылок без вызовов провайдера. |
| `co-op-review` | Нет | Нет | Выполняет детерминированные проверки структуры перевода, актуальности, Markdown, ноутбуков и локальных ссылок. |
| `run_translation(markdown=True)` | Да | Нет | Программный перевод Markdown. |
| `run_translation(images=True)` | Да | Да | Программный перевод изображений. |
| `run_review(...)` | Нет | Нет | Программная детерминированная проверка. |

## Каталоги вывода

Каталог вывода текстовых переводов по умолчанию:

```text
translations/<language-code>/<source-relative-path>
```

Каталог вывода переведённых изображений по умолчанию:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API может переопределить эти каталоги с помощью `translations_dir` и `image_dir`.