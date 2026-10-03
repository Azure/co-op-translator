# Конфигурација

Co-op Translator захтева једног провајдера језичког модела. Превод слика додатно захтева Azure AI Vision.

Конфигурација се чита из променљивих окружења. За локалне пројекте поставите их у `.env` датотеку у корену пројекта.

За подешавање Azure ресурса, погледајте [Подешавање Azure AI](azure-ai-setup.md).

## Локално окружење за покретање

Пре локалног покретања CLI-а користите виртуелно окружење. Co-op Translator подржава Python 3.11 до 3.14.

За уобичајено коришћење CLI-а инсталирајте објављени пакет унутар виртуелног окружења:

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

### Развој репозиторијума

За развој репозиторијума, уместо тога инсталирајте зависности из корена пројекта:

```bash
poetry install
poetry run translate --help
```

Након што CLI постане доступан, у `.env` конфигуришите једног провајдера језичког модела.

## Избор провајдера

Алат аутоматски детектује провајдере у следећем редоследу:

1. Azure OpenAI
2. OpenAI
3. Anthropic

За превод су потребне акредитиве провајдера, осим за прегледе као што су `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, и `run_review` су детерминистичке одржавајуће операције и не захтевају акредитиве провајдера.

## Бекенд клијента модела

Почевши од Co-op Translator 0.22.0, Azure OpenAI, OpenAI и Anthropic подразумевано користе Microsoft Agent Framework. За уобичајену употребу није потребно подешавање бекенда.

Semantic Kernel остаје привремено доступан ради компатибилности. Да бисте га експлицитно одабрали, подесите:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Коришћење Semantic Kernel-а издаје упозорење о застаревању. Планирано је да се Semantic Kernel премести у опциону зависност у 0.23.0 и да се интеграција уклони у 0.24.0, у зависности од резултата компатибилности и повратних информација корисника. Anthropic захтева `agent-framework`; експлицитно одабирање `semantic-kernel` са Anthropic-ом не успева и даје грешку у конфигурацији. Неважеће вредности ће пропасти током иницијализације преводиоца заснованог на провајдеру уместо да тише падају на подразумевано. Пратите увођење и пријављујте блокаде у [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Користите Azure OpenAI када је ваш модел распоређен у Azure AI Foundry или Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Провера повезивања користи endpoint, API кључ, верзију API-ја и име deployment-а пре почетка превода.

## OpenAI

Користите OpenAI када директно позивате OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` је обавезан јер преводиоцу треба експлицитни чат модел за позиве API-ја.

Оставите `OPENAI_ORG_ID` и `OPENAI_BASE_URL` непостављеним за подразумевано подешавање. Додајте ID организације само ако ваш налог захтева, или базни URL само када користите прилагођени endpoint. Не копирајте примерне вредности за опционе поставке.

## Anthropic Claude

Користите Anthropic када директно позивате Claude API. Креирајте [Anthropic API кључ](https://platform.claude.com/docs/en/get-started) и изаберите подржани [ID Claude модела](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` и `ANTHROPIC_MODEL` су обавезни. Не морате да подешавате `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework је подразумевани бекенд.

Оставите `ANTHROPIC_BASE_URL` непостављеним за Anthropic API. Подесите га само када користите прилагођени endpoint.

`ANTHROPIC_MAX_TOKENS` подразумевано је `8192`, што оставља простор за скрипте густе токенима као што је Meitei Mayek. Смањите га ако ваш модел или Anthropic-компатибилан endpoint ограничава излаз испод тога.

## Azure AI Vision

Превод слика захтева Azure AI Vision како би алат могао да извуче текст из слика пре него што га конфигурисани језички модел преведе. Anthropic може превести издвојени текст исто као Azure OpenAI или OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ако је превод слика одабран помоћу `-img`, `images=True`, или без филтера типа садржаја, алат валида конфигурацију Vision пре почетка превода.

## Више сета акредитива

Слој конфигурације подржава више сета акредитива додавањем истог индекса као суфикса на променљиве:

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

Сваки сет мора бити потпун. Провера здравља (health check) бира радни сет пре него што превод настави.

OpenAI и Anthropic подржавају исту конвенцију суфикса. Држите сваку променљиву у сету акредитива на истом суфиксу, укључујући опционе вредности као `OPENAI_BASE_URL_1` или `ANTHROPIC_BASE_URL_1`.

## Захтеви за команде

| Команда или API | LLM потребан | Vision потребан | Напомене |
| --- | --- | --- | --- |
| `translate -md` | Да | Не | Преводи само Markdown. |
| `translate -nb` | Да | Не | Преводи само нотебуке. |
| `translate -img` | Да | Да | Преводи само слике. |
| `translate` без типских флага | Да | Да | Подразумевани режим обухвата Markdown, нотебуке и слике. |
| `evaluate` | Да | Не | Користи LLM евалуацију осим ако није одабран `--fast`. |
| `migrate-links` | Не | Не | Извршава локалну миграцију линкова без позива провајдеру. |
| `co-op-review` | Не | Не | Покреће детерминистичке провере структуре превода, свежине, Markdown-а, нотебука и локалних линкова. |
| `run_translation(markdown=True)` | Да | Не | Програмиран превод Markdown-а. |
| `run_translation(images=True)` | Да | Да | Програмиран превод слика. |
| `run_review(...)` | Не | Не | Програмирана детерминистичка ревизија. |

## Излазни директоријуми

Подразумевани излаз за превод текста:

```text
translations/<language-code>/<source-relative-path>
```

Подразумевани излаз за преведене слике:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API може да замени ове директоријуме помоћу `translations_dir` и `image_dir`.