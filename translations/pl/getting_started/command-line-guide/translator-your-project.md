<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:48:04+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "pl"
}
-->
# Tłumacz swój projekt za pomocą Co-op Translator

**Co-op Translator** to narzędzie wiersza poleceń (CLI), które pomaga tłumaczyć pliki markdown i obrazy w Twoim projekcie na wiele języków. Ta sekcja wyjaśnia, jak korzystać z narzędzia, opisuje różne opcje CLI oraz zawiera przykłady dla różnych scenariuszy.

> [!NOTE]
> Aby uzyskać pełną listę poleceń wraz ze szczegółowymi opisami, zapoznaj się z sekcją [Command reference](./command-reference.md).

---

## Przykładowe scenariusze i polecenia

Oto kilka typowych zastosowań **Co-op Translator** wraz z odpowiednimi poleceniami do uruchomienia.

### 1. Podstawowe tłumaczenie (jeden język)

Aby przetłumaczyć cały projekt (pliki markdown i obrazy) na jeden język, na przykład koreański, użyj następującego polecenia:

```bash
translate -l "ko"
```

To polecenie przetłumaczy wszystkie pliki markdown i obrazy na język koreański, dodając nowe tłumaczenia bez usuwania istniejących.

> [!TIP]
>
> Chcesz zobaczyć, jakie kody języków są dostępne w **Co-op Translator**? Odwiedź sekcję [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) w repozytorium, aby uzyskać więcej informacji.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** użyłem następującej metody, aby dodać tłumaczenie na koreański dla istniejących plików markdown i obrazów.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Tłumaczenie na wiele języków

Aby przetłumaczyć projekt na kilka języków (np. hiszpański, francuski i niemiecki), użyj tego polecenia:

```bash
translate -l "es fr de"
```

To polecenie przetłumaczy projekt na hiszpański, francuski i niemiecki, dodając nowe tłumaczenia bez nadpisywania istniejących.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook**, po pobraniu najnowszych zmian, aby odzwierciedlić najnowsze commity, użyłem następującej metody do tłumaczenia nowo dodanych plików markdown i obrazów.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Choć zazwyczaj zaleca się tłumaczenie jednego języka na raz, w sytuacjach takich jak ta, gdzie trzeba dodać konkretne zmiany, tłumaczenie wielu języków jednocześnie może być efektywne.

### 3. Aktualizacja tłumaczeń (usuwa istniejące tłumaczenia)

Aby zaktualizować istniejące tłumaczenia (czyli usunąć obecne i zastąpić je nowymi), użyj opcji `-u`. Usunie ona wszystkie istniejące tłumaczenia dla wskazanych języków i przetłumaczy je ponownie.

```bash
translate -l "ko" -u
```

Uwaga: To polecenie poprosi o potwierdzenie przed usunięciem istniejących tłumaczeń.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** użyłem tej metody, aby zaktualizować wszystkie przetłumaczone pliki w języku hiszpańskim. Zalecam tę metodę, gdy w oryginalnej treści wielu dokumentów markdown zaszły istotne zmiany. Jeśli do aktualizacji jest tylko kilka plików, bardziej efektywne jest ręczne usunięcie tych konkretnych plików, a następnie użycie metody `-a` do dodania zaktualizowanych tłumaczeń.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Tłumaczenie tylko obrazów

Aby przetłumaczyć tylko pliki graficzne w projekcie, użyj opcji `-img`:

```bash
translate -l "ko" -img
```

To polecenie przetłumaczy tylko obrazy na język koreański, nie wpływając na pliki markdown.

### 6. Tłumaczenie tylko plików markdown

Aby przetłumaczyć tylko pliki markdown w projekcie, użyj opcji `-md`:

```bash
translate -l "ko" -md
```

### 7. Sprawdzanie błędów w przetłumaczonych plikach

Jeśli chcesz sprawdzić przetłumaczone pliki pod kątem błędów i w razie potrzeby ponowić tłumaczenie, użyj opcji `-chk`:

```bash
translate -l "ko" -chk
```

To polecenie przeskanuje przetłumaczone pliki markdown i spróbuje ponownie przetłumaczyć te, w których wykryto błędy.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** zastosowałem tę metodę, aby sprawdzić błędy tłumaczeń w plikach koreańskich i automatycznie ponowić tłumaczenie dla plików z wykrytymi problemami.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ta opcja sprawdza błędy tłumaczenia. Obecnie, jeśli różnica w liczbie znaków nowej linii między oryginalnym a przetłumaczonym plikiem przekracza sześć, plik jest oznaczany jako zawierający błąd tłumaczenia. Planuję w przyszłości poprawić ten warunek, aby był bardziej elastyczny.

Na przykład ta metoda jest przydatna do wykrywania brakujących fragmentów lub uszkodzonych tłumaczeń i automatycznie ponawia tłumaczenie tych plików.

Jeśli jednak wiesz już, które pliki są problematyczne, bardziej efektywne jest ręczne usunięcie tych plików i użycie opcji `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

To polecenie uruchomi tłumaczenie w trybie debugowania, dostarczając dodatkowe informacje w logach, które mogą pomóc zidentyfikować problemy podczas procesu tłumaczenia.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** napotkałem problem, gdzie tłumaczenia z wieloma linkami w plikach markdown powodowały błędy formatowania, takie jak uszkodzone tłumaczenia i ignorowane łamanie linii. Aby zdiagnozować ten problem, użyłem opcji `-d`, aby zobaczyć, jak działa proces tłumaczenia.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tłumaczenie na wszystkie języki

Jeśli chcesz przetłumaczyć projekt na wszystkie obsługiwane języki, użyj słowa kluczowego all.

> [!WARNING]
> Tłumaczenie wszystkich języków naraz może zająć dużo czasu w zależności od rozmiaru projektu. Na przykład przetłumaczenie **Phi-3 CookBook** na hiszpański zajęło około 2 godzin. Biorąc pod uwagę skalę, nie jest praktyczne, aby jedna osoba obsługiwała 20 języków. Zaleca się rozdzielenie pracy między kilku współpracowników, z których każdy zajmie się jednym lub dwoma językami i stopniowo będzie aktualizował tłumaczenia.

```bash
translate -l "all"
```

To polecenie przetłumaczy projekt na wszystkie dostępne języki. Jeśli zdecydujesz się kontynuować, tłumaczenie może zająć dużo czasu w zależności od rozmiaru projektu.

> [!TIP]
>
> ### Ręczne usuwanie przetłumaczonych plików (opcjonalnie)
> Przetłumaczone pliki są teraz automatycznie wykrywane i usuwane, gdy źródłowy plik zostanie zaktualizowany.
>
> Jednak jeśli chcesz ręcznie zaktualizować tłumaczenie – na przykład, aby powtórzyć tłumaczenie konkretnego pliku lub wymusić zachowanie systemu – możesz użyć poniższego polecenia, aby usunąć wszystkie wersje pliku we wszystkich folderach językowych.
>
> ### Na Windows:
> 1. **Korzystając z Command Prompt**:
>    - Otwórz Command Prompt.
>    - Przejdź do folderu, w którym znajdują się pliki, używając polecenia `cd`.
>    - Użyj następującego polecenia, aby usunąć pliki:
>      ```
>      del /s *filename*
>      ```
>      Opcja `/s` przeszukuje także podkatalogi.
>
> 2. **Korzystając z PowerShell**:
>    - Otwórz PowerShell.
>    - Uruchom to polecenie:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Zamień `"C:\YourPath"` na ścieżkę do folderu.
>
> 3. **Korzystając z polecenia `cd` i `find`**:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Zamień `filename` na nazwę pliku do usunięcia.
>
> 4. **Aktualizacja najnowszych zmian plików za pomocą `translate -l`**:
>    @@CODE_BLOCK_16@@

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.