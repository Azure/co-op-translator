# Referencja CLI

Co-op Translator instaluje te punkty wejścia w wierszu poleceń:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Polecenia `translate`, `evaluate`, `migrate-links` i `co-op-review` przechodzą przez `co_op_translator.__main__`, który wybiera implementację polecenia na podstawie nazwy uruchomionego skryptu. Serwer MCP używa bezpośrednio `co_op_translator.mcp.server`.

Jeśli zastanawiasz się między CLI, Python API i MCP, zacznij od [Wybierz swój przepływ pracy](workflows.md).

## Wyjście konsoli

Interaktywne terminale używają formatowania Rich dla nagłówka polecenia, postępu i podsumowań. Wyjście w CI i w trybie nieinteraktywnym automatycznie przełącza się na zwykły tekst.

Ustaw `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain`, aby wymusić zwykłe wyjście, lub `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich`, aby wymusić wyjście Rich. Ustaw `CO_OP_TRANSLATOR_NO_PROGRESS=1`, aby zachować podsumowania, jednocześnie wyłączając animowane paski postępu.

Użyj `translate --json-events progress.ndjson`, gdy inny system potrzebuje
maszynowo czytelnego postępu. CLI nadal będzie renderować wyjście dla ludzi, podczas gdy
plik NDJSON otrzyma wersjonowane zdarzenia `co-op.translation.event.v1` ze
stabilnymi polami takimi jak `type`, `stage_key`, `completed`, `total` oraz
`current_path`.

## Pierwszy przebieg w CLI

Zacznij tutaj, jeśli używasz Co-op Translator z terminala:

1. Skonfiguruj dostawcę LLM zgodnie z opisem w [Konfiguracja](configuration.md).
2. Wybierz typ treści, który chcesz przetłumaczyć.
3. Najpierw uruchom ukierunkowane polecenie, na przykład tłumaczenie tylko Markdown.
4. Użyj `--dry-run` przed szerokimi zmianami w repozytorium.
5. Użyj `co-op-review` po tłumaczeniu, aby sprawdzić strukturę i aktualność.

| Cel | Polecenie początkowe |
| --- | --- |
| Tłumaczenie dokumentów Markdown | `translate -l "ko" -md` |
| Tłumaczenie notebooków | `translate -l "ko" -nb` |
| Tłumaczenie tekstu na obrazach | `translate -l "ko" -img` |
| Podgląd pracy bez zapisywania plików | `translate -l "ko" -md --dry-run` |
| Przegląd istniejących tłumaczeń | `co-op-review -l "ko"` |
| Aktualizacja linków w notebookach i Markdown | `migrate-links -l "ko" --dry-run` |
| Udostępnienie narzędzi klientowi MCP | Skonfiguruj [Serwer MCP](mcp.md) zamiast uruchamiać polecenia CLI bezpośrednio. |

## translate

Tłumaczy pliki Markdown, notebooki i tekst na obrazach na jeden lub więcej języków docelowych.

```bash
translate -l "ko ja fr"
```

### Przykłady ogólne

Tłumacz tylko Markdown:

```bash
translate -l "de" -md
```

Tłumacz tylko notebooki:

```bash
translate -l "zh-CN" -nb
```

Tłumacz Markdown i obrazy:

```bash
translate -l "pt-BR" -md -img
```

Zaktualizuj istniejące tłumaczenia, usuwając je i tworząc ponownie:

```bash
translate -l "ko" -u
```

Uruchom bez interaktywnych monitów:

```bash
translate -l "ko ja" -md -y
```

Zapisz logi:

```bash
translate -l "ko" -s
```

Zapisuj strukturalne zdarzenia postępu:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opcje

| Opcja | Wymagane | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Kody języków oddzielone spacją, na przykład `"es fr de"`, lub `"all"`. |
| `-r`, `--root-dir` | No | Katalog projektu. Domyślnie bieżący katalog. |
| `-u`, `--update` | No | Usuń istniejące tłumaczenia dla wybranych języków i utwórz je ponownie. |
| `-img`, `--images` | No | Tłumacz tylko pliki obrazów. |
| `-md`, `--markdown` | No | Tłumacz tylko pliki Markdown. |
| `-nb`, `--notebook` | No | Tłumacz tylko pliki Jupyter notebook. |
| `-d`, `--debug` | No | Włącz logowanie debugujące w konsoli. |
| `-s`, `--save-logs` | No | Zapisz logi poziomu DEBUG w `<root-dir>/logs/`. |
| `--json-events` | No | Zapisz maszynowo czytelne zdarzenia postępu tłumaczenia jako NDJSON. |
| `-x`, `--fix` | No | Ponownie przetłumacz pliki Markdown o niskim zaufaniu na podstawie poprzednich wyników ewaluacji. |
| `-c`, `--min-confidence` | No | Próg zaufania dla `--fix`. Domyślnie `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Dodaj lub stłum komunikaty zastrzegające dotyczące tłumaczenia maszynowego. Domyślnie w CLI włączone. |
| `-f`, `--fast` | No | Przestarzały tryb szybkiego tłumaczenia obrazów. |
| `-y`, `--yes` | No | Automatyczne potwierdzanie monitów, przydatne w CI. |
| `--repo-url` | No | URL repozytorium używany w tabeli języków README w poradach dotyczących sparse-checkout. |
| `--migrate-language-folders` | No | Zmień nazwy starszych aliasów folderów, takich jak `cn` lub `tw`, na kanoniczne foldery BCP 47. |
| `--dry-run` | No | Podgląd migracji folderów językowych i szacunków tłumaczenia bez zapisywania plików. |

Jeśli nie podano flagi typu, `translate` przetwarza Markdown, notebooki i obrazy. Tłumaczenie obrazów wymaga konfiguracji Azure AI Vision.

## evaluate

Ocenia jakość przetłumaczonego Markdown dla jednego języka.

!!! warning "Eksperymentalne"
    `evaluate` jest eksperymentalne. Może używać kontroli opartych na regułach i na LLM, zapisuje wyniki ewaluacji w metadanych tłumaczenia, a jego model punktacji i zachowanie dotyczące metadanych mogą ulec zmianie.

```bash
evaluate -l "ko"
```

### Przykłady ogólne

Użyj surowszego progu niskiego zaufania:

```bash
evaluate -l "es" -c 0.8
```

Uruchom tylko kontrole oparte na regułach:

```bash
evaluate -l "fr" -f
```

Uruchom tylko kontrole oparte na LLM:

```bash
evaluate -l "ja" -D
```

### Opcje

| Opcja | Wymagane | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Pojedynczy kod języka do ewaluacji. Aliasowe kody są normalizowane. |
| `-r`, `--root-dir` | No | Katalog projektu. Domyślnie bieżący katalog. |
| `-c`, `--min-confidence` | No | Próg używany przy wypisywaniu tłumaczeń o niskim zaufaniu. Domyślnie `0.7`. |
| `-d`, `--debug` | No | Włącz logowanie debugujące. |
| `-s`, `--save-logs` | No | Zapisz logi poziomu DEBUG w `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Tylko ewaluacja oparta na regułach. |
| `-D`, `--deep` | No | Tylko ewaluacja oparta na LLM. |

Domyślnie `evaluate` używa zarówno ewaluacji opartej na regułach, jak i na LLM. Wyniki są zapisywane w metadanych tłumaczenia i podsumowywane w konsoli.

## co-op-review

Uruchom deterministyczne kontrole konserwacji tłumaczeń bez poświadczeń do API.

!!! note "Beta"
    `co-op-review` to beta polecenie przeglądowe o charakterze deterministycznym. Nie wywołuje dostawców modeli ani nie zapisuje plików, ale jego kontrole i schemat wyjścia problemów mogą ewoluować.

```bash
co-op-review -l "ko"
```

### Przykłady ogólne

Przejrzyj tłumaczenia koreańskie i japońskie z bieżącego katalogu:

```bash
co-op-review -l "ko ja"
```

Przejrzyj konkretny katalog projektu:

```bash
co-op-review -l "fr" -r ./my-course
```

Przejrzyj tylko README po tłumaczeniu tylko README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignoruje inne dokumenty i zagnieżdżone README. Kończy się niepowodzeniem, jeśli główny
`README.md` w katalogu root jest brakujący. W połączeniu z `--changed-from`, przegląda tylko README
gdy ten plik źródłowy uległ zmianie. Tłumaczenie tylko README pozostawia oryginalne README
bez zmian, włącznie z wszelkimi znacznikami wspólnych sekcji.

Przejrzyj tylko pliki źródłowe zmienione względem bazowego refa:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Wydrukuj wyjście w Markdown zgodne z GitHub dla podsumowań CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opcje

| Opcja | Wymagane | Opis |
| --- | --- | --- |
| `-l`, `--language-code` | No | Kod języka do przeglądu. Można przekazać wielokrotnie lub jako wartość oddzieloną spacjami. Domyślnie wszystkie wykryte języki tłumaczeń. |
| `-r`, `--root-dir` | No | Katalog projektu. Domyślnie bieżący katalog. |
| `--changed-from` | No | Ref Git używany do ograniczenia przeglądu do zmienionych plików źródłowych. |
| `--readme-only` | No | Przeglądaj tylko tłumaczenie głównego `README.md`. |
| `--format` | No | Format wyjścia: `text` lub `github`. Domyślnie `text`. |

`co-op-review` obecnie sprawdza brakujące przetłumaczone pliki, brakujące lub przestarzałe metadane tłumaczeń, poprawność frontmatter Markdown i bloków kodu, nieprawidłowe przetłumaczone JSONy notebooków oraz brakujące lokalne cele linków w Markdown lub obrazach. Brakujące linki są domyślnie ostrzeżeniami; problemy ze strukturą i aktualnością powodują niepowodzenie polecenia.

## co-op-translator-mcp

Uruchom serwer Co-op Translator MCP dla agentów, redaktorów i klientów zgodnych z MCP.

```bash
co-op-translator-mcp
```

Domyślnym transportem jest `stdio`. Zobacz przewodnik [Serwer MCP](mcp.md) dotyczący konfiguracji klienta, narzędzi, zasobów i uwag dotyczących bezpieczeństwa.

### Opcje

| Opcja | Wymagane | Opis |
| --- | --- | --- |
| `--transport` | No | Transport MCP: `stdio`, `streamable-http` lub `sse`. Domyślnie `stdio`. |

## migrate-links

Ponownie przetwórz przetłumaczone pliki Markdown i zaktualizuj linki w notebookach tak, aby wskazywały na przetłumaczone notebooki, gdy są dostępne.

```bash
migrate-links -l "ko ja"
```

### Przykłady ogólne

Podgląd aktualizacji linków:

```bash
migrate-links -l "ko" --dry-run
```

Przetwórz wszystkie obsługiwane języki bez potwierdzenia:

```bash
migrate-links -l "all" -y
```

Przepisuj linki tylko wtedy, gdy istnieją przetłumaczone notebooki:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opcje

| Opcja | Wymagane | Opis |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Kody języków oddzielone spacją, lub `"all"`. |
| `-r`, `--root-dir` | No | Katalog projektu. Domyślnie bieżący katalog. |
| `--image-dir` | No | Katalog przetłumaczonych obrazów względem katalogu root. Domyślnie `translated_images`. |
| `--dry-run` | No | Pokaż pliki, które uległyby zmianie bez zapisywania aktualizacji. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Użyj oryginalnych linków do notebooków, gdy przetłumaczone notebooki są brakujące. Domyślnie włączone. |
| `-d`, `--debug` | No | Włącz logowanie debugujące. |
| `-s`, `--save-logs` | No | Zapisz logi poziomu DEBUG w `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Automatyczne potwierdzanie monitów przy przetwarzaniu wszystkich języków. |

## Środowisko

Gdy polecenie wymaga poświadczeń dostawcy, skonfiguruj jeden z tych zestawów dostawców. `translate --dry-run` i `co-op-review` nie wymagają poświadczeń dostawcy:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Lub OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Lub Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Tłumaczenie obrazów dodatkowo wymaga Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Układ wyjścia

Tłumaczenia tekstowe są zapisywane pod:

```text
translations/<language-code>/<original-path>
```

Wyjście przetłumaczonych obrazów jest zapisywane pod:

```text
translated_images/<language-code>/<original-path>
```

Na przykład tłumaczenie `README.md` i `docs/setup.md` na koreański daje:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Przykłady CLI do kopiowania i wklejania

Tłumacz Markdown na trzy języki:

```bash
translate -l "ko ja fr" -md
```

Tłumacz tylko notebooki:

```bash
translate -l "zh-CN" -nb
```

Tłumacz tylko obrazy:

```bash
translate -l "pt-BR" -img
```

Podgląd tłumaczenia Markdown bez zapisywania plików:

```bash
translate -l "de es" -md --dry-run
```

Napraw tłumaczenia Markdown o niskim zaufaniu:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Uruchom tłumaczenie Markdown przyjazne dla CI:

```bash
translate -l "ko ja" -md -y -s
```

Przejrzyj przetłumaczone wyjście:

```bash
co-op-review -l "ko ja"
```

Podgląd migracji linków:

```bash
migrate-links -l "ko" --dry-run
```