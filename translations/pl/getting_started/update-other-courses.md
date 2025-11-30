<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:43:12+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "pl"
}
-->
# Aktualizacja sekcji "Inne kursy" (repozytoria Microsoft Beginners)

Ten przewodnik wyjaśnia, jak automatycznie synchronizować sekcję "Inne kursy" za pomocą Co-op Translator oraz jak zaktualizować globalny szablon dla wszystkich repozytoriów.

- Dotyczy: wyłącznie repozytoriów Microsoft Beginners
- Działa z: Co-op Translator CLI oraz GitHub Actions
- Źródło szablonu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Szybki start: Włącz automatyczną synchronizację w swoim repozytorium

Dodaj poniższe znaczniki wokół sekcji "Inne kursy" w swoim pliku README. Co-op Translator za każdym razem zastąpi wszystko, co znajduje się między tymi znacznikami.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Za każdym razem, gdy Co-op Translator jest uruchamiany — przez CLI (np. `translate -l "<language codes>"`) lub GitHub Actions — automatycznie aktualizuje sekcję "Inne kursy" otoczoną tymi znacznikami.

> [!NOTE]
> Jeśli masz już istniejącą listę, wystarczy, że otoczysz ją tymi samymi znacznikami. Przy następnym uruchomieniu zostanie zastąpiona najnowszą, ustandaryzowaną treścią.

---

## Jak zmienić globalną zawartość

Jeśli chcesz zaktualizować ustandaryzowaną zawartość, która pojawia się we wszystkich repozytoriach Beginners:

1. Edytuj szablon: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otwórz pull request do repozytorium Co-op Translator ze swoimi zmianami
3. Po zatwierdzeniu PR wersja Co-op Translator zostanie zaktualizowana
4. Przy następnym uruchomieniu Co-op Translator (CLI lub GitHub Action) w docelowym repozytorium, sekcja zostanie automatycznie zsynchronizowana

Dzięki temu zapewniasz jedno źródło prawdy dla zawartości sekcji "Inne kursy" we wszystkich repozytoriach Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->