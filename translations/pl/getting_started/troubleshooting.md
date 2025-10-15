<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:08:01+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pl"
}
-->
# Przewodnik rozwiązywania problemów Microsoft Co-op Translator

## Przegląd
Microsoft Co-Op Translator to zaawansowane narzędzie do płynnego tłumaczenia dokumentów Markdown. Ten przewodnik pomoże Ci rozwiązać najczęstsze problemy pojawiające się podczas korzystania z narzędzia.

## Najczęstsze problemy i rozwiązania

### 1. Problem z tagiem Markdown
**Problem:** Przetłumaczony dokument Markdown zawiera tag `markdown` na górze, co powoduje problemy z wyświetlaniem.

**Rozwiązanie:** Aby to naprawić, po prostu usuń tag `markdown` z początku pliku. Dzięki temu plik Markdown będzie się poprawnie wyświetlał.

**Kroki:**
1. Otwórz przetłumaczony plik Markdown (`.md`).
2. Znajdź tag `markdown` na górze dokumentu.
3. Usuń ten tag.
4. Zapisz zmiany w pliku.
5. Otwórz plik ponownie, aby upewnić się, że wyświetla się poprawnie.

### 2. Problem z URL obrazów osadzonych
**Problem:** Adresy URL osadzonych obrazów nie odpowiadają wersji językowej, przez co obrazy są nieprawidłowe lub ich brakuje.

**Rozwiązanie:** Sprawdź adresy URL obrazów i upewnij się, że odpowiadają wersji językowej dokumentu. Wszystkie obrazy znajdują się w folderze `translated_images`, a każdy plik obrazu ma oznaczenie języka w nazwie pliku.

**Kroki:**
1. Otwórz przetłumaczony dokument Markdown.
2. Zidentyfikuj osadzone obrazy i ich adresy URL.
3. Sprawdź, czy oznaczenie języka w nazwie pliku obrazu zgadza się z językiem dokumentu.
4. W razie potrzeby zaktualizuj adresy URL.
5. Zapisz zmiany i otwórz dokument ponownie, aby sprawdzić, czy obrazy wyświetlają się poprawnie.

### 3. Dokładność tłumaczenia
**Problem:** Przetłumaczona treść jest niedokładna lub wymaga dodatkowej edycji.

**Rozwiązanie:** Przejrzyj przetłumaczony dokument i wprowadź niezbędne poprawki, aby zwiększyć dokładność i czytelność.

**Kroki:**
1. Otwórz przetłumaczony dokument.
2. Dokładnie przejrzyj treść.
3. Wprowadź potrzebne poprawki, aby poprawić jakość tłumaczenia.
4. Zapisz zmiany.

## 4. Błąd uprawnień Redacted lub 404

Jeśli obrazy lub tekst nie są tłumaczone na właściwy język, a podczas uruchamiania w trybie debugowania (-d) pojawia się błąd 401, to klasyczny problem z autoryzacją — klucz jest nieprawidłowy, wygasł lub nie jest powiązany z regionem endpointu.

Uruchom co-op translator z [przełącznikiem -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md), aby lepiej zrozumieć przyczynę problemu.

- **Komunikat błędu**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Możliwe przyczyny**:
  - Klucz subskrypcji został ukryty lub jest nieprawidłowy w żądaniu.
  - Klucz AI Services lub Subscription Key należy do innego zasobu Azure (np. Translator lub OpenAI), zamiast do zasobu **Azure AI Vision**.

 **Typ zasobu**
  - Przejdź do [Azure Portal](https://portal.azure.com) lub [Azure AI Foundry](https://ai.azure.com) i upewnij się, że zasób ma typ `Azure AI services` → `Vision`.
  - Zweryfikuj klucze i upewnij się, że używasz właściwego klucza.

## 5. Błędy konfiguracji (nowe obsługiwanie błędów)

W nowym systemie selektywnego tłumaczenia Co-op Translator wyświetla teraz jasne komunikaty o błędach, gdy wymagane usługi nie są skonfigurowane.

### 5.1. Azure AI Service nie skonfigurowany do tłumaczenia obrazów

**Problem:** Poprosiłeś o tłumaczenie obrazów (flaga `-img`), ale Azure AI Service nie jest poprawnie skonfigurowany.

**Komunikat błędu:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Rozwiązanie:**
1. **Opcja 1**: Skonfiguruj Azure AI Service
   - Dodaj `AZURE_AI_SERVICE_API_KEY` do pliku `.env`
   - Dodaj `AZURE_AI_SERVICE_ENDPOINT` do pliku `.env`
   - Sprawdź, czy usługa jest dostępna

2. **Opcja 2**: Usuń żądanie tłumaczenia obrazów
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Brak wymaganej konfiguracji

**Problem:** Brakuje kluczowej konfiguracji LLM.

**Komunikat błędu:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Rozwiązanie:**
1. Upewnij się, że w pliku `.env` masz przynajmniej jedną z poniższych konfiguracji LLM:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Musisz skonfigurować Azure OpenAI LUB OpenAI, nie oba jednocześnie.

### 5.3. Zamieszanie z selektywnym tłumaczeniem

**Problem:** Żadne pliki nie zostały przetłumaczone, mimo że polecenie zakończyło się sukcesem.

**Możliwe przyczyny:**
- Nieprawidłowe flagi typów plików (`-md`, `-img`, `-nb`)
- Brak pasujących plików w projekcie
- Nieprawidłowa struktura katalogów

**Rozwiązanie:**
1. **Użyj trybu debugowania**, aby zobaczyć, co się dzieje:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Sprawdź typy plików** w projekcie:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Zweryfikuj kombinacje flag**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migracja ze starego systemu

### 6.1. Tryb tylko Markdown wycofany

**Problem:** Polecenia, które polegały na automatycznym trybie tylko Markdown, nie działają już jak wcześniej.

**Stare zachowanie:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nowe zachowanie:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Rozwiązanie:**
- **Bądź precyzyjny** w tym, co chcesz tłumaczyć:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Nieoczekiwane zachowanie linków

**Problem:** Linki w przetłumaczonych plikach prowadzą do nieoczekiwanych miejsc.

**Przyczyna:** Dynamiczne przetwarzanie linków zmienia się w zależności od wybranych typów plików.

**Rozwiązanie:**
1. **Poznaj nowe zasady linkowania**:
   - `-nb` włączone: Linki do notebooków prowadzą do przetłumaczonych wersji
   - `-nb` wyłączone: Linki do notebooków prowadzą do oryginalnych plików
   - `-img` włączone: Linki do obrazów prowadzą do przetłumaczonych wersji
   - `-img` wyłączone: Linki do obrazów prowadzą do oryginalnych plików

2. **Wybierz odpowiednią kombinację** dla swojego przypadku:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action uruchomiony, ale nie utworzono Pull Requesta (PR)

**Objaw:** Logi workflow dla `peter-evans/create-pull-request` pokazują:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Prawdopodobne przyczyny:**
- **Brak wykrytych zmian:** Krok tłumaczenia nie wygenerował różnic (repozytorium jest już aktualne).
- **Ignorowane pliki wyjściowe:** `.gitignore` wyklucza pliki, które chcesz dodać (np. `*.ipynb`, `translations/`, `translated_images/`).
- **Niezgodność add-paths:** Ścieżki podane do akcji nie odpowiadają rzeczywistym lokalizacjom plików wyjściowych.
- **Logika/warunki workflow:** Krok tłumaczenia zakończył się wcześniej lub zapisał pliki w nieoczekiwanych katalogach.

**Jak naprawić / sprawdzić:**
1. **Potwierdź, że pliki wyjściowe istnieją:** Po tłumaczeniu sprawdź, czy w workspace pojawiły się nowe/zaktualizowane pliki w `translations/` i/lub `translated_images/`.
   - Jeśli tłumaczysz notebooki, upewnij się, że pliki `.ipynb` są zapisane w `translations/<lang>/...`.
2. **Sprawdź `.gitignore`:** Nie ignoruj wygenerowanych plików wyjściowych. Upewnij się, że NIE ignorujesz:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (jeśli tłumaczysz notebooki)
3. **Upewnij się, że add-paths odpowiada plikom wyjściowym:** Użyj wartości wieloliniowej i uwzględnij oba foldery, jeśli to konieczne:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Wymuś PR do debugowania:** Tymczasowo zezwól na puste commity, aby sprawdzić, czy wszystko jest poprawnie skonfigurowane:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Uruchom z debugowaniem:** Dodaj `-d` do polecenia tłumaczenia, aby zobaczyć, jakie pliki zostały wykryte i zapisane.
6. **Uprawnienia (GITHUB_TOKEN):** Upewnij się, że workflow ma uprawnienia do zapisu, aby tworzyć commity i PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Szybka lista kontrolna debugowania

Podczas rozwiązywania problemów z tłumaczeniem:

1. **Użyj trybu debugowania:** Dodaj flagę `-d`, aby zobaczyć szczegółowe logi
2. **Sprawdź flagi:** Upewnij się, że `-md`, `-img`, `-nb` odpowiadają Twoim potrzebom
3. **Zweryfikuj konfigurację:** Sprawdź, czy w pliku `.env` są wymagane klucze
4. **Testuj stopniowo:** Zacznij od `-md`, potem dodawaj kolejne typy
5. **Sprawdź strukturę plików:** Upewnij się, że pliki źródłowe istnieją i są dostępne

Aby uzyskać więcej informacji o dostępnych poleceniach i flagach, zobacz [Command Reference](./command-reference.md).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za autorytatywne źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnych usług tłumacza. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.