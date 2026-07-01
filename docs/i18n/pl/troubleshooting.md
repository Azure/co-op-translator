# Rozwiązywanie problemów

Użyj tej strony, gdy uruchomienie tłumaczenia zakończy się nieoczekiwanym powodzeniem, nie powiedzie się podczas konfiguracji lub wygeneruje wynik wymagający przeglądu.

## Zacznij tutaj

1. Najpierw uruchom ukierunkowane polecenie, na przykład `translate -l "ko" -md`.
2. Dodaj `-d` dla logów debugowania w konsoli.
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

- Skonfiguruj Azure OpenAI lub OpenAI.
- Sprawdź, czy zmienne znajdują się w środowisku, w którym uruchamiane jest polecenie.
- W przypadku użycia lokalnego umieść je w pliku `.env` w katalogu głównym projektu.

Zobacz [Konfiguracja](configuration.md).

### Tłumaczenie obrazów bez Azure AI Vision

Błąd:

```text
Image translation requested but Azure AI Service is not configured.
```

Rozwiązanie:

- Dodaj `AZURE_AI_SERVICE_API_KEY`.
- Dodaj `AZURE_AI_SERVICE_ENDPOINT`.
- Lub uruchom polecenie tylko dla tekstu, na przykład `translate -l "ko" -md`.

### Nieprawidłowy klucz lub punkt końcowy

Objawy mogą obejmować `401`, zredagowane błędy uprawnień lub błędy dostępu do punktu końcowego.

Rozwiązanie:

- Potwierdź, że klucz należy do tego samego zasobu Azure co punkt końcowy.
- Potwierdź, że zasób obsługuje Vision podczas używania `-img`.
- Potwierdź, że nazwa wdrożenia Azure OpenAI oraz wersja API pasują do Twojego wdrożenia.
- Uruchom z logami debugowania: `translate -l "ko" -md -d -s`.

## Żadne pliki nie zostały przetłumaczone

Typowe przyczyny:

- Wybrane flagi nie odpowiadają Twoim plikom.
- Istnieją już przetłumaczone pliki.
- Pliki źródłowe znajdują się w wykluczonych katalogach.
- Polecenie jest uruchamiane z niewłaściwego katalogu głównego projektu.

Kontrole:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Użyj `--root-dir`, gdy polecenie jest uruchamiane spoza głównego katalogu projektu.

## Nieoczekiwane zachowanie linków

Przepisywanie linków zależy od wybranych typów treści:

- `-nb` włączone: linki do notatników mogą wskazywać na przetłumaczone notatniki.
- `-nb` wyłączone: linki do notatników mogą pozostać skierowane do oryginalnych notatników.
- `-img` włączone: linki do obrazów mogą wskazywać na przetłumaczone obrazy.
- `-img` wyłączone: linki do obrazów mogą pozostać skierowane do oryginalnych obrazów.

Uruchom pełne tłumaczenie treści, gdy wszystkie linki wewnętrzne powinny preferować przetłumaczone wersje:

```bash
translate -l "ko" -md -nb -img
```

Przeprowadź przegląd linków po tłumaczeniu:

```bash
co-op-review -l "ko"
```

## Problemy z renderowaniem Markdown

Jeśli przetłumaczony Markdown renderuje się niepoprawnie:

- Sprawdź, czy frontmatter zaczyna się i kończy na `---`.
- Sprawdź, czy liczba ograniczników bloków kodu (code fences) zgadza się między plikiem źródłowym a przetłumaczonym.
- Uruchom `co-op-review`, aby wykryć powszechne problemy strukturalne.
- Przetłumacz ponownie konkretny plik, jeśli wynik został uszkodzony.

```bash
co-op-review -l "ko" --format github
```

## Akcja GitHub uruchomiona, ale nie utworzono Pull Requesta

Jeśli `peter-evans/create-pull-request` raportuje, że gałąź nie jest przed bazą, workflow nie znalazł plików do zatwierdzenia.

Prawdopodobne przyczyny:

- Uruchomienie tłumaczenia nie wygenerowało żadnych zmian.
- Plik `.gitignore` wyklucza `translations/`, `translated_images/` lub przetłumaczone notatniki.
- `add-paths` nie pasuje do wygenerowanych katalogów wyjściowych.
- Krok tłumaczenia zakończył się wcześniej.

Rozwiązania:

1. Potwierdź, że wygenerowane pliki istnieją w `translations/` lub `translated_images/`.
2. Potwierdź, że `.gitignore` nie ignoruje wygenerowanych wyników.
3. Użyj pasujących `add-paths`:

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

Tłumaczenia maszynowe mogą wymagać przeglądu przez człowieka. Używaj `evaluate` tylko wtedy, gdy chcesz eksperymentalnego oceniania jakości i przepływów naprawczych dla niskiego zaufania.

!!! warning "Experimental"
    `evaluate` może korzystać z kontroli opartych na regułach oraz na LLM, a jego model oceniania i zachowanie dotyczące metadanych mogą ulec zmianie. Nie stosuj go w obowiązkowych bramach CI, chyba że twój workflow jest przygotowany na zmiany.

Dla deterministycznych kontroli CI użyj zamiast tego `co-op-review`.