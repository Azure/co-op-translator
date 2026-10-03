# Konfiguracja

Co-op Translator wymaga jednego dostawcy modelu językowego. Tłumaczenie obrazów dodatkowo wymaga Azure AI Vision.

Konfiguracja odczytywana jest ze zmiennych środowiskowych. Dla projektów lokalnych umieść je w pliku `.env` w katalogu głównym projektu.

Aby skonfigurować zasoby Azure, zobacz [Konfiguracja Azure AI](azure-ai-setup.md).

## Lokalne środowisko uruchomieniowe

Przed uruchomieniem CLI lokalnie użyj wirtualnego środowiska. Co-op Translator obsługuje Pythona w wersjach od 3.11 do 3.14.

Dla normalnego użycia CLI zainstaluj opublikowany pakiet wewnątrz wirtualnego środowiska:

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

### Rozwój repozytorium

Dla rozwoju repozytorium zainstaluj zależności z katalogu głównego projektu zamiast tego:

```bash
poetry install
poetry run translate --help
```

Gdy CLI będzie dostępne, skonfiguruj jednego dostawcę modelu językowego w pliku `.env`.

## Wybór dostawcy

Narzędzie wykrywa dostawców automatycznie w następującej kolejności:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Tłumaczenie wymaga poświadczeń dostawcy, z wyjątkiem podglądów, takich jak `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` i `run_review` to deterministyczne operacje konserwacyjne i nie wymagają poświadczeń dostawcy.

## Backend klienta modelu

Począwszy od Co-op Translator 0.22.0, Azure OpenAI, OpenAI i Anthropic używają domyślnie Microsoft Agent Framework. Dla normalnego użycia nie jest wymagane ustawienie backendu.

Semantic Kernel pozostaje tymczasowo dostępny dla zgodności. Aby wybrać go eksplicytnie, ustaw:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Użycie Semantic Kernel powoduje wyświetlenie ostrzeżenia o przestarzałości. Planowane jest przeniesienie Semantic Kernel do zależności opcjonalnych w wersji 0.23.0 i usunięcie integracji w 0.24.0, w zależności od wyników zgodności i opinii użytkowników. Anthropic wymaga `agent-framework`; jawne wybranie `semantic-kernel` z Anthropic kończy się błędem konfiguracji. Nieprawidłowe wartości powodują błąd podczas inicjalizacji tłumacza korzystającego z dostawcy zamiast cichego przyjmowania domyślnych ustawień. Śledź wdrożenie i zgłaszaj blokery w [zgłoszeniu GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Użyj Azure OpenAI, gdy twój model jest wdrożony w Azure AI Foundry lub Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Sprawdzenie łączności wykorzystuje punkt końcowy, klucz API, wersję API i nazwę wdrożenia przed rozpoczęciem tłumaczenia.

## OpenAI

Użyj OpenAI, gdy wywołujesz bezpośrednio OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` jest wymagane, ponieważ tłumacz potrzebuje wyraźnego modelu czatu do wywołań API.

Pozostaw `OPENAI_ORG_ID` i `OPENAI_BASE_URL` nieustawione dla domyślnej konfiguracji. Dodaj identyfikator organizacji tylko jeśli twoje konto go wymaga, lub bazowy URL tylko przy użyciu niestandardowego punktu końcowego. Nie kopiuj wartości zastępczych dla ustawień opcjonalnych.

## Anthropic Claude

Użyj Anthropic, gdy wywołujesz bezpośrednio Claude API. Utwórz [klucz API Anthropic](https://platform.claude.com/docs/en/get-started) i wybierz obsługiwany [identyfikator modelu Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` i `ANTHROPIC_MODEL` są wymagane. Nie musisz ustawiać `CO_OP_TRANSLATOR_MODEL_CLIENT`; domyślnym backendem jest Agent Framework.

Pozostaw `ANTHROPIC_BASE_URL` nieustawione dla Anthropic API. Ustaw je tylko przy użyciu niestandardowego punktu końcowego.

`ANTHROPIC_MAX_TOKENS` domyślnie ustawione jest na `8192`, co pozostawia miejsce dla skryptów o dużej gęstości tokenów, takich jak Meitei Mayek. Zmniejsz tę wartość, jeśli twój model lub punkt końcowy zgodny z Anthropic ogranicza wyjście poniżej tej wartości.

## Azure AI Vision

Tłumaczenie obrazów wymaga Azure AI Vision, aby narzędzie mogło wyodrębnić tekst z obrazów przed przetłumaczeniem go przez skonfigurowany model językowy. Anthropic może przetłumaczyć wyodrębniony tekst tak samo jak Azure OpenAI lub OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jeśli wybrano tłumaczenie obrazów za pomocą `-img`, `images=True` lub bez filtra typu zawartości, narzędzie weryfikuje konfigurację Vision przed rozpoczęciem tłumaczenia.

## Wiele zestawów poświadczeń

Warstwa konfiguracji obsługuje wiele zestawów poświadczeń poprzez dopisywanie do zmiennych tego samego sufiksu indeksu:

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

Każdy zestaw musi być kompletny. Kontrola stanu wybiera działający zestaw przed przystąpieniem do tłumaczenia.

OpenAI i Anthropic obsługują tę samą konwencję sufiksów. Trzymaj każdą zmienną w zestawie poświadczeń na tym samym sufiksie, włączając wartości opcjonalne takie jak `OPENAI_BASE_URL_1` lub `ANTHROPIC_BASE_URL_1`.

## Wymagania dotyczące poleceń

| Polecenie lub API | Wymagane LLM | Wymagane Vision | Uwagi |
| --- | --- | --- | --- |
| `translate -md` | Tak | Nie | Tłumaczy tylko Markdown. |
| `translate -nb` | Tak | Nie | Tłumaczy tylko notebooki. |
| `translate -img` | Tak | Tak | Tłumaczy tylko obrazy. |
| `translate` bez flag typu | Tak | Tak | Tryb domyślny obejmuje Markdown, notebooki i obrazy. |
| `evaluate` | Tak | Nie | Wykorzystuje ocenę LLM chyba że wybrano `--fast`. |
| `migrate-links` | Nie | Nie | Wykonuje lokalną migrację linków bez wywołań do dostawcy. |
| `co-op-review` | Nie | Nie | Uruchamia deterministyczne sprawdzenia struktury tłumaczenia, świeżości, Markdown, notebooków i lokalnych linków. |
| `run_translation(markdown=True)` | Tak | Nie | Programistyczne tłumaczenie Markdown. |
| `run_translation(images=True)` | Tak | Tak | Programistyczne tłumaczenie obrazów. |
| `run_review(...)` | Nie | Nie | Programistyczne deterministyczne sprawdzenie. |

## Katalogi wyjściowe

Domyślny katalog wyjściowy tłumaczeń tekstu:

```text
translations/<language-code>/<source-relative-path>
```

Domyślny katalog wyjściowy przetłumaczonych obrazów:

```text
translated_images/<language-code>/<source-relative-path>
```

API Pythona może nadpisać te katalogi za pomocą `translations_dir` i `image_dir`.