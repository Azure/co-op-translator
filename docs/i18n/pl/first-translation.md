# Tłumacz, edytuj i przejrzyj mały projekt

Rozpocznij od dwóch krótkich plików Markdown i jednego języka docelowego. Zobaczysz, gdzie zapisywane są tłumaczenia, co się dzieje po zmianie źródła i jak sprawdzić wynik.

## Zarejestrowane wyniki

Przykład uruchomiono 19 września 2026 r. z Co-op Translator 0.21.0 i Azure OpenAI (`gpt-5-mini`). Niezmodyfikowane polecenia CLI zostały wywołane przy użyciu `CliRunner` z Click, korzystając ze zbudowanego pliku wheel i istniejących zależności Pythona.

| Krok | Wynik |
| --- | --- |
| Podgląd | Wyjście 0; nie wykonano tłumaczenia przez model |
| Początkowe tłumaczenie | Wyjście 0; 27.36 sek. |
| Wstępna recenzja | Wyjście 0 |
| Edycja README i przegląd | Wyjście 1; wykryto przestarzałe tłumaczenie |
| Aktualizacja tłumaczenia | Wyjście 0; 22.17 sek. |
| Przegląd po aktualizacji | Wyjście 0; brak błędów ani ostrzeżeń |
| Przewodnik bez zmian | Identyczne bajty przed i po aktualizacji README |
| Uruchom ponownie | Wyjście 0; identyczne hashe dla wszystkich plików tłumaczeń |

To są pomiary poszczególnych uruchomień, a nie gwarancje wydajności. Czas konfiguracji nie jest uwzględniony; rozliczenia dostawcy nie były mierzone. Uruchomienie bez zmian może nadal wykonać kontrolę stanu dostawcy.

Przejrzyj [początkowe tłumaczenie](../../assets/demo/before.txt), [zaktualizowane tłumaczenie](../../assets/demo/after.txt), [pełny diff tłumaczenia](../../assets/demo/update.diff), [przegląd przestarzały](../../assets/demo/review-stale.txt), [końcowy przegląd](../../assets/demo/review-after.txt) i [szczegóły uruchomienia](../../assets/demo/results.json). Tłumaczenie całego pliku może zmienić inne sformułowania, jak pokazuje przechwycony diff. Oba artefakty tekstowe zachowują wygenerowane zastrzeżenie.

Ręczna weryfikacja nadal ma znaczenie: przechwycona aktualizacja używa `[사용 가이드](guide.md)을`; partykuła koreańska powinna być `[사용 가이드](guide.md)를`. Artefakty tekstowe zachowują ten wynik bez zmian zamiast przedstawiać edytowane tłumaczenie jako wyjście modelu. Przegląd strukturalny przechodzi pomimo tego problemu ze sformułowaniem.

## 1. Przygotuj mały folder

Użyj Pythona 3.11–3.14 i [konfiguracji środowiska wirtualnego](configuration.md#local-runtime-setup). Zainstaluj wersję używaną w tym przykładzie:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Pobierz [README.txt](../../assets/demo/README.txt) i [guide.txt](../../assets/demo/guide.txt) do tego folderu, zapisując je jako `README.md` i `guide.md`. To małe fikcyjne dokumenty projektu; nie jest potrzebna instalacja aplikacji.

README zawiera blok kodu i link do `guide.md`. Jego ostatnie zdanie to:

```text
Notes are saved locally.
```

Zachowaj w tym folderze tylko te dwa dokumenty źródłowe. Wszystkie kolejne polecenia uruchamiane są wewnątrz `translation-demo` i działają w Bash oraz PowerShell.

## 2. Podgląd bez poświadczeń

```bash
translate -l "ko" -md --dry-run
```

Podgląd szacuje pracę tłumaczeniową bez wywoływania modelu ani zapisywania tłumaczeń. Szacunki tokenów nie stanowią wyceny rozliczeń. Pierwsze uruchomienie powinno zidentyfikować oba pliki Markdown jako nowe zadanie.

## 3. Wybierz dostawcę i przetłumacz

Skonfiguruj jednego dostawcę używając [przewodnika konfiguracji](configuration.md): Azure OpenAI, OpenAI lub Anthropic. Tłumaczenie tekstu z OpenAI i Anthropic nie wymaga konta Azure. Usługi obrazów nie są potrzebne w tym przykładzie.

Jeśli używasz lokalnego pliku `.env`, dodaj `.env` do `.gitignore` tego folderu. Wywołania tłumaczeń korzystają z konta dostawcy i mogą generować opłaty.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Otwórz `translations/ko/README.md` i `translations/ko/guide.md`. Sprawdź koreańskie sformułowania, blok kodu i link z przetłumaczonego README do przetłumaczonego przewodnika. Sformułowania wyjściowe różnią się w zależności od modelu.

`co-op-review` sprawdza aktualność, strukturę i linki lokalne. Pozytywny wynik nie gwarantuje poprawności językowej. Rozwiąż wszelkie zgłoszone błędy przed kontynuacją.

Zarejestruj pomyślną wersję bazową w Git (w razie potrzeby najpierw skonfiguruj swoją tożsamość w Git):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Zmień źródło

W `README.md` zastąp `Notes are saved locally.` przez:

```text
Notes are saved locally as Markdown files.
```

Pozostaw `guide.md` bez zmian. Następnie uruchom:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Przegląd powinien zgłosić tłumaczenie README jako przestarzałe i zakończyć się niepowodzeniem. To oczekiwany stan pośredni. Podgląd powinien zidentyfikować zadanie dla zmienionego README.

## 5. Zaktualizuj i przejrzyj różnice

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Sprawdź rzeczywisty diff: domyślne CLI ponownie tłumaczy zmieniony plik, więc model może także zmienić inne sformułowania w tym pliku. Niezmieniony przewodnik nie powinien mieć różnic. Przegląd nie powinien już zgłaszać README jako przestarzałego; zamiast ich ignorowania, zbadaj inne wykryte problemy.

Zachowanie zmian w Markdown na poziomie bloków wymaga opcjonalnego dostawcy stanu tłumaczeń w [Python API](api.md). Nie jest to włączone przez te polecenia CLI.

## 6. Uruchom ponownie bez zmian

Zatwierdź zaktualizowane źródło i tłumaczenie:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Przy obecnych tłumaczeniach i niezmienionej konfiguracji tłumacz pomija pliki. Końcowe polecenie Git nie powinno wygenerować różnic i powinno zakończyć się pomyślnie.

## Kolejne kroki

- [Przetłumacz tylko README i otwórz pull request](github-actions.md#your-first-readme-translation-pr).
- [Wybierz CLI, Python API lub MCP](workflows.md).
- [Zgłoś problem z tłumaczeniem bez kodowania](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).