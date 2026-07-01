# Конфигурација

Co-op Translator захтева једног провајдера језичког модела. Превод слика додатно захтева Azure AI Vision.

Конфигурација се чита из променљивих окружења. За локалне пројекте, поставите их у `.env` фајл у корену пројекта.

За подешавање Azure ресурса, погледајте [Azure AI подешавање](azure-ai-setup.md).

## Локално подешавање окружења

Користите виртуелно окружење пре покретања CLI локално. Co-op Translator подржава Python 3.10 до 3.12.

За уобичајену употребу CLI-а, инсталирајте објављени пакет унутар виртуелног окружења:

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

За развој репозиторијума, уместо тога инсталирајте зависности из корена пројекта:

```bash
poetry install
poetry run translate --help
```

Након што је CLI доступан, конфигуришите једног провајдера језичког модела у `.env`.

## Избор провајдера

Алат аутоматски открива провајдере у следећем редоследу:

1. Azure OpenAI
2. OpenAI

Ако ни један провајдер није конфигурисан, `translate`, `evaluate`, `migrate-links`, и `run_translation` неће проћи током провера конфигурације. `co-op-review` и `run_review` су детерминистичке провере одржавања и не захтевају акредитације провајдера.

## Azure OpenAI

Користите Azure OpenAI када је ваш модел распоређен у Azure AI Foundry или Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Провера повезивости користи endpoint, API key, API version и deployment name пре него што превођење започне.

## OpenAI

Користите OpenAI када позивате OpenAI API директно.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # опционо
OPENAI_BASE_URL="..."        # опционо
```

`OPENAI_CHAT_MODEL_ID` је обавезан јер преводилац треба експлицитан chat модел за позиве API-ја.

## Azure AI Vision

Превод слика захтева Azure AI Vision да би алат могао да извуче текст из слика пре него што га преведе.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ако је превод слика одабран са `-img`, `images=True`, или без филтера типа садржаја, алат валида конфигурацију Vision-а пре почетка превођења.

## Више сета акредитива

Слоj конфигурације подржава више сета акредитива додавањем истог индекса на крај променљивих:

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

Сваки сет мора бити потпун. Провера здравља бира радни сет пре него што превођење настави.

## Захтеви за команде

| Команда или API | Потребан LLM | Потребан Vision | Напомене |
| --- | --- | --- | --- |
| `translate -md` | Да | Не | Преводи само Markdown. |
| `translate -nb` | Да | Не | Преводи само нотебуке. |
| `translate -img` | Да | Да | Преводи само слике. |
| `translate` with no type flags | Да | Да | Подразумевани режим укључује Markdown, нотебуке и слике. |
| `evaluate` | Да | Не | Користи LLM евалуацију осим ако није изабран `--fast`. |
| `migrate-links` | Да | Не | Извршава миграцију линкова, али ипак покреће заједничке провере конфигурације. |
| `co-op-review` | Не | Не | Извршава детерминистичке провере структуре превода, свежине, Markdown-а, нотебука и локалних линкова. |
| `run_translation(markdown=True)` | Да | Не | Програмско превођење Markdown-а. |
| `run_translation(images=True)` | Да | Да | Програмско превођење слика. |
| `run_review(...)` | Не | Не | Програмски детерминистички преглед. |

## Излазни директоријуми

Подразумевани излаз за текстуални превод:

```text
translations/<language-code>/<source-relative-path>
```

Подразумевани излаз за преведене слике:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API може надјачати ове директоријуме помоћу `translations_dir` и `image_dir`.