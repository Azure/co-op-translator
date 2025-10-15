<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:07:29+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pl"
}
-->
# Referencja poleceń

CLI **Co-op Translator** oferuje wiele opcji pozwalających dostosować proces tłumaczenia:

Polecenie                                      | Opis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "kody_języków"                   | Tłumaczy Twój projekt na wybrane języki. Przykład: translate -l "es fr de" tłumaczy na hiszpański, francuski i niemiecki. Użyj translate -l "all", aby przetłumaczyć na wszystkie obsługiwane języki.
translate -l "kody_języków" -u                | Aktualizuje tłumaczenia, usuwając istniejące i tworząc je na nowo. Uwaga: Spowoduje to usunięcie wszystkich obecnych tłumaczeń dla wybranych języków.
translate -l "kody_języków" -img              | Tłumaczy tylko pliki graficzne.
translate -l "kody_języków" -md               | Tłumaczy tylko pliki Markdown.
translate -l "kody_języków" -nb               | Tłumaczy tylko pliki Jupyter notebook (.ipynb).
translate -l "kody_języków" --fix             | Ponownie tłumaczy pliki z niskim poziomem pewności na podstawie wcześniejszych wyników oceny.
translate -l "kody_języków" -d                | Włącza tryb debugowania dla szczegółowego logowania.
translate -l "kody_języków" --save-logs, -s   | Zapisuje logi na poziomie DEBUG do plików w <root_dir>/logs/ (konsola pozostaje kontrolowana przez -d)
translate -l "kody_języków" -r "root_dir"     | Określa katalog główny projektu
translate -l "kody_języków" -f                | Używa szybkiego trybu tłumaczenia obrazów (do 3x szybsze generowanie wykresów, kosztem niewielkiej utraty jakości i wyrównania).
translate -l "kody_języków" -y                | Automatycznie potwierdza wszystkie zapytania (przydatne w pipeline'ach CI/CD)
translate -l "kody_języków" --help            | Szczegóły pomocy w CLI pokazujące dostępne polecenia
evaluate -l "kod_języka"                      | Ocena jakości tłumaczenia dla wybranego języka i podanie poziomu pewności
evaluate -l "kod_języka" -c 0.8               | Ocena tłumaczeń z niestandardowym progiem pewności
evaluate -l "kod_języka" -f                   | Szybka ocena (tylko reguły, bez LLM)
evaluate -l "kod_języka" -D                   | Głęboka ocena (tylko LLM, dokładniejsza, ale wolniejsza)
evaluate -l "kod_języka" --save-logs, -s      | Zapisuje logi na poziomie DEBUG do plików w <root_dir>/logs/
migrate-links -l "kody_języków"               | Przetwarza ponownie przetłumaczone pliki Markdown, aby zaktualizować linki do notebooków (.ipynb). Preferuje przetłumaczone notebooki, jeśli są dostępne; w przeciwnym razie może użyć oryginalnych.
migrate-links -l "kody_języków" -r            | Określa katalog główny projektu (domyślnie: bieżący katalog).
migrate-links -l "kody_języków" --dry-run     | Pokazuje, które pliki zostałyby zmienione, bez zapisywania zmian.
migrate-links -l "kody_języków" --no-fallback-to-original | Nie zmienia linków do oryginalnych notebooków, gdy brakuje przetłumaczonych odpowiedników (aktualizuje tylko, gdy tłumaczenie istnieje).
migrate-links -l "kody_języków" -d            | Włącza tryb debugowania dla szczegółowego logowania.
migrate-links -l "kody_języków" --save-logs, -s | Zapisuje logi na poziomie DEBUG do plików w <root_dir>/logs/
migrate-links -l "all" -y                      | Przetwarza wszystkie języki i automatycznie potwierdza ostrzeżenie.

## Przykłady użycia

  1. Domyślne działanie (dodaje nowe tłumaczenia bez usuwania istniejących):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj tylko nowe tłumaczenia obrazów na koreański (nie usuwa istniejących tłumaczeń):    translate -l "ko" -img

  3. Zaktualizuj wszystkie tłumaczenia na koreański (Uwaga: Usuwa wszystkie istniejące tłumaczenia na koreański przed ponownym tłumaczeniem):    translate -l "ko" -u

  4. Zaktualizuj tylko obrazy na koreański (Uwaga: Usuwa wszystkie istniejące obrazy na koreański przed ponownym tłumaczeniem):    translate -l "ko" -img -u

  5. Dodaj nowe tłumaczenia Markdown na koreański bez wpływu na inne tłumaczenia:    translate -l "ko" -md

  6. Popraw tłumaczenia o niskim poziomie pewności na podstawie wcześniejszych wyników oceny: translate -l "ko" --fix

  7. Popraw tłumaczenia o niskim poziomie pewności tylko dla wybranych plików (Markdown): translate -l "ko" --fix -md

  8. Popraw tłumaczenia o niskim poziomie pewności tylko dla wybranych plików (obrazy): translate -l "ko" --fix -img

  9. Użyj szybkiego trybu tłumaczenia obrazów:    translate -l "ko" -img -f

  10. Popraw tłumaczenia o niskim poziomie pewności z niestandardowym progiem: translate -l "ko" --fix -c 0.8

  11. Przykład trybu debugowania: - translate -l "ko" -d: Włącza logowanie debugowania.
  12. Zapisz logi do plików: translate -l "ko" -s
  13. DEBUG na konsoli i w plikach: translate -l "ko" -d -s

  14. Migruj linki do notebooków dla tłumaczeń na koreański (aktualizuje linki do przetłumaczonych notebooków, jeśli są dostępne):    migrate-links -l "ko"

  15. Migruj linki w trybie testowym (bez zapisu plików):    migrate-links -l "ko" --dry-run

  16. Aktualizuj linki tylko, gdy istnieją przetłumaczone notebooki (nie używaj oryginałów):    migrate-links -l "ko" --no-fallback-to-original

  17. Przetwarzaj wszystkie języki z potwierdzeniem:    migrate-links -l "all"

  18. Przetwarzaj wszystkie języki i automatycznie potwierdź:    migrate-links -l "all" -y
  19. Zapisz logi do plików dla migrate-links:    migrate-links -l "ko ja" -s

### Przykłady oceny

> [!WARNING]  
> **Funkcja beta**: Funkcjonalność oceny jest obecnie w fazie beta. Funkcja została udostępniona do oceny przetłumaczonych dokumentów, a metody oceny i szczegóły implementacji są wciąż rozwijane i mogą się zmienić.

  1. Oceń tłumaczenia na koreański: evaluate -l "ko"

  2. Oceń z niestandardowym progiem pewności: evaluate -l "ko" -c 0.8

  3. Szybka ocena (tylko reguły): evaluate -l "ko" -f

  4. Głęboka ocena (tylko LLM): evaluate -l "ko" -D

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było dokładne, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za źródło autorytatywne należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.