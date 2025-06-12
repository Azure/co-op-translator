<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:28:08+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pl"
}
-->
# Command reference
CLI **Co-op Translator** oferuje kilka opcji dostosowania procesu tłumaczenia:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Tłumaczy Twój projekt na wskazane języki. Przykład: translate -l "es fr de" tłumaczy na hiszpański, francuski i niemiecki. Użyj translate -l "all", aby przetłumaczyć na wszystkie obsługiwane języki.
translate -l "language_codes" -u              | Aktualizuje tłumaczenia, usuwając istniejące i tworząc je na nowo. Uwaga: spowoduje to usunięcie wszystkich aktualnych tłumaczeń dla wskazanych języków.
translate -l "language_codes" -img            | Tłumaczy tylko pliki graficzne.
translate -l "language_codes" -md             | Tłumaczy tylko pliki Markdown.
translate -l "language_codes" -chk            | Sprawdza przetłumaczone pliki pod kątem błędów i w razie potrzeby ponawia tłumaczenie.
translate -l "language_codes" -d              | Włącza tryb debugowania dla szczegółowego logowania.
translate -l "language_codes" -r "root_dir"   | Określa katalog główny projektu.
translate -l "language_codes" -f              | Używa trybu szybkiego tłumaczenia obrazów (do 3x szybsze renderowanie kosztem nieznacznej jakości i wyrównania).
translate -l "language_codes" -y              | Automatycznie potwierdza wszystkie monity (przydatne w pipeline CI/CD).
translate -l "language_codes" --help          | Szczegóły pomocy w CLI pokazujące dostępne polecenia.

### Przykłady użycia:

  1. Domyślne działanie (dodawanie nowych tłumaczeń bez usuwania istniejących):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj tylko nowe tłumaczenia obrazów na koreański (istniejące tłumaczenia nie są usuwane):    translate -l "ko" -img

  3. Aktualizuj wszystkie tłumaczenia na koreański (Uwaga: spowoduje to usunięcie wszystkich istniejących tłumaczeń koreańskich przed ponownym tłumaczeniem):    translate -l "ko" -u

  4. Aktualizuj tylko obrazy na koreański (Uwaga: spowoduje to usunięcie wszystkich istniejących obrazów koreańskich przed ponownym tłumaczeniem):    translate -l "ko" -img -u

  5. Dodaj nowe tłumaczenia markdown na koreański bez wpływu na inne tłumaczenia:    translate -l "ko" -md

  6. Sprawdź przetłumaczone pliki pod kątem błędów i w razie potrzeby ponów tłumaczenia: translate -l "ko" -chk

  7. Sprawdź przetłumaczone pliki pod kątem błędów i ponów tłumaczenia (tylko markdown): translate -l "ko" -chk -md

  8. Sprawdź przetłumaczone pliki pod kątem błędów i ponów tłumaczenia (tylko obrazy): translate -l "ko" -chk -img

  9. Użyj trybu szybkiego tłumaczenia obrazów:    translate -l "ko" -img -f

  10. Przykład trybu debugowania: - translate -l "ko" -d: Włącz szczegółowe logowanie.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.