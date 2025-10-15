<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:26:41+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pl"
}
-->
## Przegląd projektu

Co‑op Translator to narzędzie wiersza poleceń w Pythonie oraz workflow GitHub Actions, które tłumaczy pliki Markdown, notatniki Jupyter oraz tekst z obrazów na wiele języków. Organizuje wyniki w folderach językowych i utrzymuje synchronizację tłumaczeń z treścią źródłową. Projekt jest zbudowany jako biblioteka zarządzana przez Poetry z punktami wejścia CLI.

### Przegląd architektury

- Punkty wejścia CLI (`translate`, `migrate-links`, `evaluate`) uruchamiają wspólny interfejs CLI, który przekierowuje do procesów tłumaczenia, migracji linków i ewaluacji.
- Loader konfiguracji czyta plik `.env` i automatycznie wykrywa dostawcę LLM (Azure OpenAI lub OpenAI), a jeśli jest to wymagane, także dostawcę vision (Azure AI Service) do ekstrakcji tekstu z obrazów.
- Rdzeń tłumaczenia obsługuje pliki Markdown i notatniki; pipeline vision wyodrębnia tekst z obrazów, gdy użyto opcji `-img`.
- Wyniki są organizowane w `translations/<lang>/` dla tekstu oraz `translated_images/` dla obrazów, z zachowaniem oryginalnej struktury.

### Kluczowe technologie i frameworki

- Python 3.10–3.12, Poetry do zarządzania pakietami
- CLI: `click`
- SDK LLM/AI: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP i dane: `httpx`, `pydantic`
- Obrazowanie: `pillow`, `opencv-python`, `matplotlib`
- Narzędzia: `pytest`, `black`, `ruff`

## Komendy instalacyjne

### Wymagania wstępne

- Python 3.10–3.12
- Subskrypcja Azure (opcjonalnie, dla usług Azure AI)
- Dostęp do internetu dla API LLM/Vision (np. Azure OpenAI/OpenAI, Azure AI Vision)

### Opcja A: Poetry (zalecane)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opcja B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Użytkowanie końcowe

### Docker (opublikowany obraz)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Uwagi:
- Domyślny entrypoint to `translate`. Zmień na `--entrypoint migrate-links` dla migracji linków.
- Upewnij się, że widoczność pakietu GHCR jest ustawiona na Public, aby umożliwić anonimowe pobieranie.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfiguracja środowiska

Utwórz plik `.env` w głównym katalogu repozytorium i podaj dane uwierzytelniające/punkty końcowe dla wybranego modelu językowego oraz (opcjonalnie) usługi vision. Szczegóły konfiguracji dla dostawców znajdziesz w `getting_started/set-up-azure-ai.md`.

### Wymagane zmienne środowiskowe

Musi być skonfigurowany co najmniej jeden dostawca LLM. Do tłumaczenia obrazów wymagane jest także skonfigurowanie Azure AI Service.

- Azure OpenAI (tłumaczenie tekstu):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatywa dla tłumaczenia tekstu):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opcjonalnie)
  - `OPENAI_CHAT_MODEL_ID` (wymagane przy użyciu OpenAI)
  - `OPENAI_BASE_URL` (opcjonalnie; domyślnie `https://api.openai.com/v1`)

- Azure AI Service do ekstrakcji tekstu z obrazów (wymagane przy użyciu `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (zalecane) lub starsze `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Przykładowy fragment `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Uwagi:

- Narzędzie automatycznie wykrywa dostępnego dostawcę LLM; skonfiguruj Azure OpenAI lub OpenAI.
- Tłumaczenie obrazów wymaga zarówno `AZURE_AI_SERVICE_API_KEY`, jak i `AZURE_AI_SERVICE_ENDPOINT`.
- CLI zgłosi czytelny błąd, jeśli brakuje wymaganych zmiennych.

## Workflow deweloperski

- Kod źródłowy znajduje się w `src/co_op_translator`; testy w `tests/`.
- Główne CLI (instalowane przez entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Dodatkowe instrukcje użycia znajdziesz w `getting_started/`.

## Instrukcje testowania

Uruchamiaj testy z głównego katalogu repozytorium. Niektóre testy mogą wymagać danych API; pomiń je w razie potrzeby.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Opcjonalnie pokrycie (wymaga `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Wytyczne dotyczące stylu kodu

- Formatowanie: Black (konfiguracja w `pyproject.toml`, długość linii 88)
- Linter: Ruff (konfiguracja w `pyproject.toml`, długość linii 120)
- Sprawdzanie typów: mypy (konfiguracja obecna; włącz, jeśli zainstalowane)

Komendy:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizuj źródła Pythona w `src/`, testy w `tests/`, preferuj jawne importy w przestrzeni nazw pakietu (`co_op_translator.*`).

## Budowanie i wdrażanie

Artefakty budowania publikowane są do `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatyzacja przez GitHub Actions jest wspierana; zobacz:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Obraz kontenera (GHCR)

- Oficjalny obraz: `ghcr.io/azure/co-op-translator:<tag>`
- Tagi: `latest` (na main), tagi semantyczne typu `vX.Y.Z` oraz tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` wspierane przez Buildx
- Wzorzec Dockerfile: buduj dependency wheels w builderze (z `build-essential` i `python3-dev`) i instaluj z lokalnego wheelhouse w runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` buduje i publikuje do GHCR

## Uwagi dotyczące bezpieczeństwa

- Przechowuj klucze API i punkty końcowe w `.env` lub w sekretnym magazynie CI; nigdy nie commituj sekretów.
- Do tłumaczenia obrazów wymagane są klucze/punkty końcowe Azure AI Vision; w przeciwnym razie pomiń `-img`.
- Sprawdź limity/kwoty dostawcy przy dużych partiach tłumaczeń.

## Wytyczne dotyczące Pull Requestów

### Przed wysłaniem

1. **Przetestuj zmiany:**
   - Uruchom zmienione notatniki w całości
   - Sprawdź, czy wszystkie komórki wykonują się bez błędów
   - Upewnij się, że wyniki są odpowiednie

2. **Aktualizacje dokumentacji:**
   - Zaktualizuj `README.md` przy dodawaniu nowych zagadnień
   - Dodaj komentarze w notatnikach do złożonego kodu
   - Upewnij się, że komórki markdown wyjaśniają cel

3. **Zmiany w plikach:**
   - Nie commituj plików `.env` (użyj `.env.example`)
   - Nie commituj katalogów `venv/` ani `__pycache__/`
   - Zachowaj wyniki notatników, gdy pokazują koncepcje
   - Usuń pliki tymczasowe i kopie zapasowe notatników (`*-backup.ipynb`)

4. **Styl i formatowanie:**
   - Przestrzegaj wytycznych dotyczących stylu i formatowania
   - Uruchom `poetry run black .` oraz `poetry run ruff check .`, aby sprawdzić styl i formatowanie

5. **Dodaj/aktualizuj testy i pomoc CLI:**
   - Dodaj lub zaktualizuj testy przy zmianie zachowania
   - Utrzymuj pomoc CLI zgodną ze zmianami


### Format wiadomości commit i strategia merge

Stosujemy Squash and Merge jako domyślną strategię. Ostateczna wiadomość squash commit powinna mieć format:

```bash
<type>: <description> (#<PR number>)
```

Dozwolone typy:
- `Docs` — aktualizacje dokumentacji
- `Build` — system budowania, zależności, konfiguracja/CI
- `Core` — główna funkcjonalność i nowe funkcje (np. `src/co_op_translator/core`)

Przykłady:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Uwagi:
- Tytuły PR są często automatycznie poprzedzane na podstawie etykiet; sprawdź, czy wygenerowany prefiks jest poprawny.

### Format tytułu PR

Używaj jasnych, zwięzłych tytułów. Preferuj ten sam format co ostateczny squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugowanie i rozwiązywanie problemów

- Typowe problemy i rozwiązania: `getting_started/troubleshooting.md`
- Obsługiwane języki i uwagi (w tym czcionki/znane problemy): `getting_started/supported-languages.md`
- W przypadku problemów z linkami w notatnikach, uruchom ponownie: `migrate-links -l "all" -y`

## Uwagi dla agentów

- Preferuj Poetry dla powtarzalnych środowisk; w przeciwnym razie użyj `requirements.txt`.
- Przy uruchamianiu CLI w CI, podawaj wymagane sekrety przez zmienne środowiskowe lub wstrzykiwanie `.env`.
- Dla konsumentów monorepo, to repozytorium działa jako samodzielny pakiet; nie jest wymagana koordynacja subpakietów.

- Wskazówki multi-arch: zachowaj `linux/arm64`, gdy celem są użytkownicy ARM (Apple Silicon/serwery ARM); w przeciwnym razie dla prostoty wystarczy `linux/amd64`.
- Kieruj użytkowników do Docker Quick Start w `README.md`, jeśli preferują użycie kontenera; uwzględnij warianty Bash i PowerShell ze względu na różnice w cudzysłowach.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było dokładne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za autorytatyczne źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecamy skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.