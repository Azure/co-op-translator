<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:26:25+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pl"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Przegląd
Microsoft Co-Op Translator to potężne narzędzie do płynnego tłumaczenia dokumentów Markdown. Ten przewodnik pomoże Ci rozwiązać typowe problemy napotykane podczas korzystania z narzędzia.

## Typowe problemy i rozwiązania

### 1. Problem z tagiem Markdown
**Problem:** Przetłumaczony dokument Markdown zawiera tag `markdown` na górze, co powoduje problemy z renderowaniem.

**Rozwiązanie:** Aby to naprawić, po prostu usuń tag `markdown` z góry pliku. Pozwoli to na poprawne wyświetlenie pliku Markdown.

**Kroki:**
1. Otwórz przetłumaczony plik Markdown (`.md`).
2. Znajdź tag `markdown` na początku dokumentu.
3. Usuń tag `markdown`.
4. Zapisz zmiany w pliku.
5. Ponownie otwórz plik, aby upewnić się, że wyświetla się poprawnie.

### 2. Problem z URL-ami osadzonych obrazów
**Problem:** URL-e osadzonych obrazów nie odpowiadają lokalizacji językowej, co prowadzi do błędnych lub brakujących obrazów.

**Rozwiązanie:** Sprawdź URL-e osadzonych obrazów i upewnij się, że odpowiadają lokalizacji językowej. Wszystkie obrazy znajdują się w folderze `translated_images`, każdy obraz ma tag lokalizacji językowej w nazwie pliku.

**Kroki:**
1. Otwórz przetłumaczony dokument Markdown.
2. Zidentyfikuj osadzone obrazy i ich URL-e.
3. Sprawdź, czy lokalizacja językowa w nazwie pliku obrazu odpowiada językowi dokumentu.
4. W razie potrzeby zaktualizuj URL-e.
5. Zapisz zmiany i ponownie otwórz dokument, aby potwierdzić poprawne wyświetlanie obrazów.

### 3. Dokładność tłumaczenia
**Problem:** Przetłumaczona treść nie jest dokładna lub wymaga dalszej edycji.

**Rozwiązanie:** Przejrzyj przetłumaczony dokument i dokonaj niezbędnych poprawek, aby poprawić dokładność i czytelność.

**Kroki:**
1. Otwórz przetłumaczony dokument.
2. Dokładnie przejrzyj zawartość.
3. Wprowadź potrzebne poprawki, aby poprawić dokładność tłumaczenia.
4. Zapisz zmiany.

### 4. Problemy z formatowaniem pliku
**Problem:** Formatowanie przetłumaczonego dokumentu jest niepoprawne. Może się to zdarzyć w przypadku tabel — dodatkowy ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` rozwiąże problemy z tabelami.

**Kroki:**
1. Otwórz przetłumaczony dokument.
2. Porównaj go z oryginalnym dokumentem, aby zidentyfikować problemy z formatowaniem.
3. Dostosuj formatowanie, aby odpowiadało oryginałowi.
4. Zapisz zmiany.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.