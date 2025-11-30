<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:04:23+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pl"
}
-->
# Referencja poleceń

CLI **Co-op Translator** oferuje kilka opcji pozwalających dostosować proces tłumaczenia:

Polecenie                                   | Opis
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | Tłumaczy projekt na określone języki. Przykład: translate -l "es fr de" tłumaczy na hiszpański, francuski i niemiecki. Użyj translate -l "all", aby przetłumaczyć na wszystkie obsługiwane języki.
translate -l "language_codes" -u            | Aktualizuje tłumaczenia, usuwając istniejące i tworząc je na nowo. Uwaga: spowoduje to usunięcie wszystkich obecnych tłumaczeń dla wskazanych języków.
translate -l "language_codes" -img          | Tłumaczy tylko pliki graficzne.
translate -l "language_codes" -md           | Tłumaczy tylko pliki Markdown.
translate -l "language_codes" -nb           | Tłumaczy tylko pliki Jupyter notebook (.ipynb).
translate -l "language_codes" --fix         | Ponownie tłumaczy pliki o niskim poziomie pewności na podstawie wcześniejszych wyników oceny.
translate -l "language_codes" -d            | Włącza tryb debugowania dla szczegółowego logowania.
translate -l "language_codes" --save-logs, -s | Zapisuje logi na poziomie DEBUG do plików w <root_dir>/logs/ (konsola pozostaje kontrolowana przez -d)
translate -l "language_codes" -r "root_dir" | Określa katalog główny projektu
translate -l "language_codes" -f            | Używa trybu szybkiego tłumaczenia obrazów (do 3x szybsze renderowanie kosztem nieznacznej jakości i wyrównania).
translate -l "language_codes" -y            | Automatycznie potwierdza wszystkie monity (przydatne w pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Włącza lub wyłącza dodawanie sekcji z zastrzeżeniem o tłumaczeniu maszynowym do przetłumaczonych plików markdown i notebooków (domyślnie włączone).
translate -l "language_codes" --help        | Szczegóły pomocy w CLI pokazujące dostępne polecenia
evaluate -l "language_code"                  | Ocena jakości tłumaczenia dla konkretnego języka i podanie poziomów pewności
evaluate -l "language_code" -c 0.8           | Ocena tłumaczeń z niestandardowym progiem pewności
evaluate -l "language_code" -f               | Szybka ocena (tylko reguły, bez LLM)
evaluate -l "language_code" -D               | Głęboka ocena (tylko LLM, dokładniejsza, ale wolniejsza)
evaluate -l "language_code" --save-logs, -s  | Zapisuje logi na poziomie DEBUG do plików w <root_dir>/logs/
migrate-links -l "language_codes"             | Ponowne przetworzenie przetłumaczonych plików Markdown w celu aktualizacji linków do notebooków (.ipynb). Preferuje przetłumaczone notebooki, jeśli są dostępne; w przeciwnym razie może użyć oryginalnych.
migrate-links -l "language_codes" -r          | Określa katalog główny projektu (domyślnie bieżący katalog).
migrate-links -l "language_codes" --dry-run   | Pokazuje, które pliki uległyby zmianie, bez zapisywania zmian.
migrate-links -l "language_codes" --no-fallback-to-original | Nie przepisuje linków do oryginalnych notebooków, gdy brak jest przetłumaczonych odpowiedników (aktualizuje tylko, gdy istnieje tłumaczenie).
migrate-links -l "language_codes" -d          | Włącza tryb debugowania dla szczegółowego logowania.
migrate-links -l "language_codes" --save-logs, -s | Zapisuje logi na poziomie DEBUG do plików w <root_dir>/logs/
migrate-links -l "all" -y                      | Przetwarza wszystkie języki i automatycznie potwierdza monit ostrzegawczy.

## Przykłady użycia

  1. Domyślne zachowanie (dodaj nowe tłumaczenia bez usuwania istniejących):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj tylko nowe tłumaczenia obrazów na koreański (nie usuwa istniejących tłumaczeń):    translate -l "ko" -img

  3. Aktualizuj wszystkie tłumaczenia koreańskie (Uwaga: usuwa wszystkie istniejące tłumaczenia koreańskie przed ponownym tłumaczeniem):    translate -l "ko" -u

  4. Aktualizuj tylko obrazy koreańskie (Uwaga: usuwa wszystkie istniejące obrazy koreańskie przed ponownym tłumaczeniem):    translate -l "ko" -img -u

  5. Dodaj nowe tłumaczenia markdown dla koreańskiego bez wpływu na inne tłumaczenia:    translate -l "ko" -md

  6. Napraw tłumaczenia o niskim poziomie pewności na podstawie wcześniejszych wyników oceny: translate -l "ko" --fix

  7. Napraw tłumaczenia o niskim poziomie pewności tylko dla wybranych plików (markdown): translate -l "ko" --fix -md

  8. Napraw tłumaczenia o niskim poziomie pewności tylko dla wybranych plików (obrazy): translate -l "ko" --fix -img

  9. Użyj trybu szybkiego tłumaczenia obrazów:    translate -l "ko" -img -f

  10. Napraw tłumaczenia o niskim poziomie pewności z niestandardowym progiem: translate -l "ko" --fix -c 0.8

  11. Przykład trybu debugowania: - translate -l "ko" -d: Włącz logowanie debugowania.
  12. Zapisz logi do plików: translate -l "ko" -s
  13. DEBUG w konsoli i w plikach: translate -l "ko" -d -s
  14. Tłumacz bez dodawania zastrzeżeń o tłumaczeniu maszynowym do wyników: translate -l "ko" --no-disclaimer

  15. Migracja linków do notebooków dla tłumaczeń koreańskich (aktualizacja linków do przetłumaczonych notebooków, jeśli dostępne):    migrate-links -l "ko"

  15. Migracja linków z trybem podglądu (bez zapisu zmian):    migrate-links -l "ko" --dry-run

  16. Aktualizuj linki tylko, gdy istnieją przetłumaczone notebooki (bez powrotu do oryginałów):    migrate-links -l "ko" --no-fallback-to-original

  17. Przetwórz wszystkie języki z monitami potwierdzającymi:    migrate-links -l "all"

  18. Przetwórz wszystkie języki i automatycznie potwierdź:    migrate-links -l "all" -y
  19. Zapisz logi do plików dla migrate-links:    migrate-links -l "ko ja" -s

### Przykłady oceny

> [!WARNING]  
> **Funkcja beta**: Funkcjonalność oceny jest obecnie w fazie beta. Ta funkcja została udostępniona do oceny przetłumaczonych dokumentów, a metody oceny oraz szczegóły implementacji są nadal rozwijane i mogą ulec zmianie.

  1. Oceń tłumaczenia koreańskie: evaluate -l "ko"

  2. Oceń z niestandardowym progiem pewności: evaluate -l "ko" -c 0.8

  3. Szybka ocena (tylko reguły): evaluate -l "ko" -f

  4. Głęboka ocena (tylko LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->