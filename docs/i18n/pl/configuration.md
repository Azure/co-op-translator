# Konfiguracja

Co-op Translator wymaga jednego dostawcy modelu językowego. Tłumaczenie obrazów dodatkowo wymaga Azure AI Vision.

Konfiguracja jest odczytywana z zmiennych środowiskowych. Dla projektów lokalnych umieść je w pliku `.env` w katalogu głównym projektu.

For Azure resource setup, see [Konfiguracja Azure AI](azure-ai-setup.md).

## Lokalna konfiguracja środowiska uruchomieniowego

Use a virtual environment before running the CLI locally. Co-op Translator supports Python 3.10 through 3.12.

For normal CLI usage, install the published package inside a virtual environment:

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

Dla pracy nad repozytorium zainstaluj zależności z katalogu głównego projektu:

```bash
poetry install
poetry run translate --help
```

Po udostępnieniu CLI skonfiguruj jednego dostawcę modelu językowego w `.env`.

## Wybór dostawcy

Narzędzie wykrywa dostawców automatycznie w następującej kolejności:

1. Azure OpenAI
2. OpenAI

Jeśli żaden dostawca nie jest skonfigurowany, `translate`, `evaluate`, `migrate-links`, i `run_translation` zakończą się niepowodzeniem podczas kontroli konfiguracji. `co-op-review` i `run_review` to deterministyczne testy konserwacyjne i nie wymagają poświadczeń dostawcy.

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

Użyj OpenAI, gdy wywołujesz API OpenAI bezpośrednio.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opcjonalny
OPENAI_BASE_URL="..."        # opcjonalny
```

`OPENAI_CHAT_MODEL_ID` jest wymagane, ponieważ tłumacz potrzebuje jawnego modelu czatowego do wywołań API.

## Azure AI Vision

Tłumaczenie obrazów wymaga Azure AI Vision, aby narzędzie mogło wydobyć tekst z obrazów przed ich przetłumaczeniem.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jeśli tłumaczenie obrazów zostanie wybrane za pomocą `-img`, `images=True` lub bez filtra typu treści, narzędzie weryfikuje konfigurację Vision przed rozpoczęciem tłumaczenia.

## Wiele zestawów poświadczeń

Warstwa konfiguracji obsługuje wiele zestawów poświadczeń poprzez sufiksowanie zmiennych tym samym indeksem:

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

Każdy zestaw musi być kompletny. Kontrola stanu wybiera działający zestaw przed kontynuacją tłumaczenia.

## Wymagania dotyczące poleceń

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Tak | Nie | Tłumaczy tylko Markdown. |
| `translate -nb` | Tak | Nie | Tłumaczy tylko notatniki. |
| `translate -img` | Tak | Tak | Tłumaczy tylko obrazy. |
| `translate` with no type flags | Tak | Tak | Tryb domyślny obejmuje Markdown, notatniki i obrazy. |
| `evaluate` | Tak | Nie | Używa oceny LLM, chyba że wybrano `--fast`. |
| `migrate-links` | Tak | Nie | Wykonuje migrację linków, ale nadal przeprowadza wspólne kontrole konfiguracji. |
| `co-op-review` | Nie | Nie | Przeprowadza deterministyczne kontrole struktury tłumaczenia, aktualności, Markdown, notatników i linków lokalnych. |
| `run_translation(markdown=True)` | Tak | Nie | Programatyczne tłumaczenie Markdown. |
| `run_translation(images=True)` | Tak | Tak | Programatyczne tłumaczenie obrazów. |
| `run_review(...)` | Nie | Nie | Programatyczny deterministyczny przegląd. |

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