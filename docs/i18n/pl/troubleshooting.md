# Rozwiązywanie problemów

Użyj tej strony, gdy uruchomienie tłumaczenia zakończy się nieoczekiwanie sukcesem, nie powiodło się podczas konfiguracji lub wygenerowało wynik wymagający przeglądu.

## Zacznij tutaj

1. Najpierw uruchom skoncentrowane polecenie, na przykład `translate -l "ko" -md`.
2. Dodaj `-d`, aby uzyskać logi debugowania w konsoli.
3. Dodaj `-s`, aby zapisać logi debugowania w `<root-dir>/logs/`.
4. Uruchom `co-op-review` po tłumaczeniu, aby sprawdzić aktualność, strukturę i linki lokalne.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Błędy konfiguracji

### Brak dostawcy modelu językowego

Błąd:

```text
No language model configuration found.
```

Rozwiązanie:

- Skonfiguruj Azure OpenAI, OpenAI lub Anthropic.
- Sprawdź, czy zmienne znajdują się w środowisku, w którym uruchamiane jest polecenie.
- Dla lokalnego użycia umieść je w `.env` w katalogu głównym projektu.

Zobacz [Konfiguracja](configuration.md).

### Tłumaczenie obrazów bez Azure AI Vision

Błąd:

```text
Image translation requested but Azure AI Service is not configured.
```

Rozwiązanie:

- Dodaj `AZURE_AI_SERVICE_API_KEY`.
- Dodaj `AZURE_AI_SERVICE_ENDPOINT`.
- Lub uruchom polecenie tylko z tekstem, takie jak `translate -l "ko" -md`.

### Nieprawidłowy klucz lub punkt końcowy

Objawy mogą obejmować `401`, zacenzurowane błędy uprawnień lub błędy dostępu do punktu końcowego.

Rozwiązanie:

- Potwierdź, że klucz należy do tego samego zasobu Azure co punkt końcowy.
- Potwierdź, że zasób obsługuje Vision podczas używania `-img`.
- Potwierdź, że nazwa wdrożenia Azure OpenAI i wersja API pasują do twojego wdrożenia.
- Uruchom z logami debugowania: `translate -l "ko" -md -d -s`.

## Nie przetłumaczono żadnych plików

Typowe przyczyny:

- Wybrane flagi nie odpowiadają twoim plikom.
- Istnieją już przetłumaczone pliki.
- Pliki źródłowe znajdują się w wykluczonych katalogach.
- Polecenie jest uruchamiane z niewłaściwego katalogu głównego projektu.

Kontrole:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Użyj `--root-dir`, gdy polecenie jest uruchamiane poza katalogiem głównym projektu.

## Nieoczekiwane zachowanie linków

Przepisywanie linków zależy od wybranych typów zawartości:

- `-nb` włączone: linki do notebooków mogą wskazywać na przetłumaczone notebooki.
- `-nb` wyłączone: linki do notebooków mogą pozostać skierowane na źródłowe notebooki.
- `-img` włączone: linki do obrazów mogą wskazywać na przetłumaczone obrazy.
- `-img` wyłączone: linki do obrazów mogą pozostać skierowane na źródłowe obrazy.

Uruchom pełne tłumaczenie zawartości, gdy wszystkie linki wewnętrzne powinny preferować przetłumaczone wyniki:

```bash
translate -l "ko" -md -nb -img
```

Uruchom przegląd linków po tłumaczeniu:

```bash
co-op-review -l "ko"
```

## Problemy z renderowaniem Markdown

Jeśli przetłumaczony Markdown renderuje się nieprawidłowo:

- Sprawdź, czy frontmatter zaczyna się i kończy na `---`.
- Sprawdź, czy liczba ogrodzeń kodu (code fence) zgadza się między plikami źródłowymi a przetłumaczonymi.
- Uruchom `co-op-review`, aby wykryć typowe problemy ze strukturą.
- Ponownie przetłumacz konkretny plik, jeśli wynik został uszkodzony.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action uruchomiony, ale nie utworzono pull requesta

Jeśli `peter-evans/create-pull-request` raportuje, że gałąź nie jest przed bazową, workflow nie znalazł plików do zatwierdzenia.

Prawdopodobne przyczyny:

- Uruchomienie tłumaczenia nie wprowadziło żadnych zmian.
- `.gitignore` wyklucza `translations/`, `translated_images/` lub przetłumaczone notebooki.
- `add-paths` nie odpowiada generowanym katalogom wyjściowym.
- Krok tłumaczenia zakończył się przedwcześnie.

Rozwiązania:

1. Potwierdź, że wygenerowane pliki istnieją w `translations/` lub `translated_images/`.
2. Potwierdź, że `.gitignore` nie ignoruje wygenerowanych wyników.
3. Użyj dopasowanych `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Tymczasowo dodaj flagi debugowania do polecenia translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Potwierdź, że uprawnienia workflow obejmują:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Jakość tłumaczenia

Tłumaczenia maszynowe mogą wymagać przeglądu przez człowieka. Używaj `evaluate` tylko wtedy, gdy chcesz eksperymentalnego oceniania jakości i workflowów naprawczych dla niskiego zaufania.

!!! warning "Eksperymentalne"
    `evaluate` może używać kontroli opartych na regułach i LLM, a jego model oceny i zachowanie metadanych mogą ulec zmianie. Nie umieszczaj go w obowiązkowych bramach CI, chyba że twój workflow jest przygotowany na zmiany.

Dla deterministycznych kontroli CI użyj zamiast tego `co-op-review`.