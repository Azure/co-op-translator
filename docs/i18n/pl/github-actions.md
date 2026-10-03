# GitHub Actions

Użyj GitHub Actions, gdy chcesz, aby repozytorium automatycznie tłumaczyło zmienioną dokumentację i otwierało pull request z wygenerowanymi wynikami.

Zacznij od standardowej konfiguracji `GITHUB_TOKEN`, także dla repozytoriów organizacji, gdy polityka na to pozwala. Zobacz [Konfiguracja aplikacji GitHub](#github-app-setup) gdy Twoja organizacja wymaga tożsamości aplikacji lub potrzebujesz automatycznego uruchamiania kolejnych workflowów.

**Ręczne edycje:** te workflowy przetłumaczą ponownie zmienione pliki źródłowe w całości i mogą nadpisać sformułowania edytowane w ich tłumaczeniach. Przejrzyj każdy PR przed scaleniem. Zachowanie bloków Markdown wymaga niestandardowej integracji z [dostawcą stanu tłumaczenia Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Twój pierwszy PR z tłumaczeniem README

Zacznij od jednego głównego pliku `README.md` i jednego języka docelowego. Ten workflow tłumaczy tylko Markdown, więc Azure AI Vision nie jest wymagane.

1. Sklonuj [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([zobacz szablon na GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) do `.github/workflows/translate-readme.yml` w repozytorium, które chcesz tłumaczyć, i zatwierdź go do domyślnej gałęzi tego repozytorium. Szablon używa głównego Action `Azure/co-op-translator@main`, który instaluje CLI z tego samego refa źródłowego. Przypnij zweryfikowany commit dla powtarzalnych uruchomień.
2. Otwórz **Actions > Translate README > Run workflow**, wybierz język i pozostaw zaznaczone **Preview only**. Sprawdź szacowane użycie tokenów w kroku podglądu. Podgląd nie wywołuje dostawców modeli, nie zapisuje tłumaczeń ani nie tworzy PR.
3. Dodaj sekrety dla jednego [dostawcy tekstu](#prerequisites) i włącz **Zezwól GitHub Actions na tworzenie i zatwierdzanie pull requestów** w **Ustawienia > Akcje > Ogólne**. Szablon żąda `contents: write` i `pull-requests: write` dla swojej pracy; nie musisz zmieniać domyślnych uprawnień dla każdego workflowu. Jeśli polityka organizacji blokuje te uprawnienia lub to ustawienie, zapytaj administratora o zatwierdzoną [aplikację GitHub](#github-app-setup).
4. Uruchom workflow ponownie z odznaczonym **Preview only**. Wtedy wykona podgląd, przetłumaczy, uruchomi `co-op-review --readme-only` i utworzy lub zaktualizuje PR z tłumaczeniem tylko po pomyślnym zakończeniu tłumaczenia i przeglądu. Podsumowanie workflow zawiera link do PR.
5. Przejrzyj sformułowania i zmiany plików w PR, a następnie scal, gdy będziesz gotowy. Workflow nie scala automatycznie.

PR zawiera tylko `translations/<language>/README.md` oraz jego plik metadanych języka. Źródłowy README pozostaje niezmieniony, a linki do innych dokumentów nadal wskazują na dokumenty źródłowe. Treść PR wymienia zmienione pliki i wyniki przeglądu strukturalnego. Jeśli tłumaczenie lub przegląd się nie powiodą, sprawdź podsumowanie workflow i logi nieudanych kroków; PR nie zostanie utworzony. Jeśli nie ma zmian, nowy PR nie jest potrzebny.

**Uwaga dotycząca organizacji i CI:** GitHub App jest opcjonalny, a nie wymagany przy własności organizacyjnej. Z `GITHUB_TOKEN`, workflowy dotyczące pull requestów (otwieranie, aktualizowanie lub ponowne otwieranie PR) wymagają, aby użytkownik z uprawnieniami zapisu wybrał **Approve workflows to run**. Workflowy uruchamiane przez push nie są wyzwalane przez ten token. Dla bezobsługowego CI downstream zobacz [Konfiguracja aplikacji GitHub](#github-app-setup) oraz zasady wyzwalania workflowów GitHub ([workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Wymagania wstępne

Przed utworzeniem workflow skonfiguruj sekrety usługi AI, których będzie potrzebować uruchomienie tłumaczenia.

Tłumaczenie tekstu wymaga jednego dostawcy modeli językowych:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, oraz opcjonalnie `OPENAI_ORG_ID` i `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, oraz opcjonalnie `ANTHROPIC_BASE_URL`

Tłumaczenie obrazów dodatkowo wymaga Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Zobacz [Konfiguracja](configuration.md) i [Konfiguracja Azure AI](azure-ai-setup.md) w sprawie szczegółów konfiguracji lokalnej.

## Standardowa konfiguracja

Po wypróbowaniu workflowu dla README użyj tej konfiguracji, aby przetłumaczyć pliki Markdown w repozytorium na kilka języków. Uruchamia ona przegląd Markdown przed otwarciem PR i nie wymaga Azure AI Vision.

### Krok 1: Dodaj sekrety repozytorium

W docelowym repozytorium otwórz **Settings** > **Secrets and variables** > **Actions**, a następnie dodaj sekrety dostawcy, których będzie używać workflow.

![Wybierz sekrety Akcji](../../assets/github-actions/select-setting-action.png)

### Krok 2: Włącz uprawnienia workflow

Otwórz **Settings** > **Actions** > **General**.

W sekcji **Workflow permissions**:

1. Włącz **Zezwól GitHub Actions na tworzenie i zatwierdzanie pull requestów**.
2. Zapisz ustawienie.

Poniższa praca żąda jawnie `contents: write` i `pull-requests: write`. Pozostaw domyślne uprawnienia workflow repozytorium bez zmian. Jeśli polityka organizacji blokuje tworzenie PR, zapytaj administratora o zatwierdzoną [aplikację GitHub](#github-app-setup).

### Krok 3: Dodaj workflow

Utwórz `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Zmień `TARGET_LANGUAGES` na języki, których potrzebuje Twój projekt. Przegląd używa Python API do sprawdzania tylko Markdown, zgodnie z krokiem tłumaczenia. Błąd tłumaczenia lub przeglądu zatrzymuje zadanie przed utworzeniem PR. Workflow nie scala PR automatycznie. Dla dużych repozytoriów dodaj filtr `paths:` pod `on.push`, aby workflow uruchamiał się tylko przy zmianach dokumentacji.

### Opcjonalnie: notebooki i obrazy

Dla notebooków dodaj `-nb` do polecenia tłumaczenia i ustaw `notebook=True` w kroku przeglądu. Dla tekstu na obrazach skonfiguruj dwie [sekrety Azure AI Vision](#prerequisites), przekaż je w `env` kroku tłumaczenia, dodaj `-img` do polecenia i dodaj `translated_images/` do `add-paths` kroku PR. Przeglądaj przetłumaczone obrazy wizualnie; przegląd deterministyczny nie potwierdza tekstu na obrazie ani poprawności językowej.

## Konfiguracja aplikacji GitHub

Użyj zatwierdzonej aplikacji GitHub, gdy Twoja organizacja wymaga tożsamości aplikacji, lub gdy wygenerowany PR musi wyzwolić downstream CI bez kroku zatwierdzania `GITHUB_TOKEN`. Aplikacja nie omija polityki organizacji; administratorzy nadal kontrolują jej instalację i uprawnienia.

### Krok 1: Utwórz lub zainstaluj aplikację GitHub

Użyj istniejącej aplikacji dostarczonej przez organizację, jeśli jest dostępna, lub utwórz taką z dostępem odczytu/zapisu do **Contents** i **Pull requests**. Zainstaluj ją w docelowym repozytorium z wymaganą zgodą organizacji.

Zanotuj:

- ID aplikacji
- Zawartość klucza prywatnego

Przechowuj je jako sekrety repozytorium:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Krok 2: Wygeneruj token aplikacji

Dodaj ten krok bezpośrednio przed istniejącym krokiem pull request. Dla szablonu README użyj tego samego warunku sukcesu, aby podglądy i nieudane tłumaczenia nie żądały tokena aplikacji:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Następnie zmień tylko parametr `token` w istniejącym kroku pull request na `${{ steps.generate_token.outputs.token }}`. Pozostaw niezmienione jego warunki sukcesu, gałąź, treść PR i `add-paths`. Token jest domyślnie ograniczony do bieżącego repozytorium. Przy dostosowywaniu standardowej konfiguracji zamiast szablonu README pomiń powyższe `if`: ten workflow używa domyślnego warunku sukcesu, więc tworzenie tokena i tworzenie PR uruchamiają się dopiero po pomyślnym zakończeniu tłumaczenia i przeglądu.

Zobacz oficjalny [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) w sprawie instalacji i uprawnień tokena.

## Ograniczenia runnerów

Runnery hostowane przez GitHub mają maksymalny czas trwania zadania. Duże repozytoria lub wiele języków docelowych mogą przekroczyć ten limit.

Dla dużych zadań tłumaczeniowych:

- Tłumacz mniej języków na jedno uruchomienie.
- Użyj flag zawartości takich jak `-md`, `-nb` lub `-img`.
- Użyj self-hosted runnera, gdy rozmiar repozytorium lub opóźnienia modelu sprawiają, że hostowane runnery są zawodliwe.

## Przegląd w CI

Użyj `co-op-review`, gdy pull request ma walidować wygenerowane tłumaczenia bez wywoływania dostawców LLM lub Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` to beta-narzędzie do deterministycznego przeglądu. Jego sprawdzenia i schemat wyjścia mogą ewoluować, ale jest zaprojektowane jako bezpieczne dla CI, ponieważ nie zapisuje plików ani nie wywołuje dostawców modeli.