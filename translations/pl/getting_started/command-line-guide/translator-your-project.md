<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:08:32+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "pl"
}
-->
# Przetłumacz swój projekt za pomocą Co-op Translator

**Co-op Translator** to narzędzie wiersza poleceń (CLI), które pomaga tłumaczyć pliki markdown oraz obrazy w Twoim projekcie na wiele języków. W tej sekcji wyjaśniamy, jak korzystać z narzędzia, omawiamy dostępne opcje CLI i podajemy przykłady dla różnych scenariuszy użycia.

> [!NOTE]
> Pełną listę poleceń i ich szczegółowe opisy znajdziesz w sekcji [Command reference](./command-reference.md).

---

## Przykładowe scenariusze i polecenia

Oto kilka typowych przypadków użycia **Co-op Translator** wraz z odpowiednimi poleceniami.

### 1. Podstawowe tłumaczenie (jeden język)

Aby przetłumaczyć cały projekt (pliki markdown i obrazy) na jeden język, np. koreański, użyj poniższego polecenia:

```bash
translate -l "ko"
```

To polecenie przetłumaczy wszystkie pliki markdown i obrazy na język koreański, dodając nowe tłumaczenia bez usuwania już istniejących.

> [!TIP]
>
> Chcesz sprawdzić, jakie kody języków są dostępne w **Co-op Translator**? Zajrzyj do sekcji [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) w repozytorium, aby uzyskać więcej informacji.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** użyłem poniższej metody, aby dodać tłumaczenie na język koreański dla istniejących plików markdown i obrazów.

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

To polecenie przetłumaczy projekt na hiszpański, francuski i niemiecki, dodając nowe tłumaczenia bez nadpisywania już istniejących.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook**, po pobraniu najnowszych zmian odzwierciedlających ostatnie commity, użyłem poniższej metody, aby przetłumaczyć nowo dodane pliki markdown i obrazy.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Zazwyczaj zaleca się tłumaczenie na jeden język naraz, ale w sytuacjach takich jak ta, gdy trzeba dodać konkretne zmiany, tłumaczenie na wiele języków jednocześnie może być efektywne.

### 3. Aktualizacja tłumaczeń (usuwa istniejące tłumaczenia)

Aby zaktualizować istniejące tłumaczenia (czyli usunąć obecne tłumaczenia i zastąpić je nowymi), użyj opcji `-u`. Spowoduje to usunięcie wszystkich istniejących tłumaczeń dla wybranych języków i ponowne ich przetłumaczenie.

```bash
translate -l "ko" -u
```

Uwaga: To polecenie poprosi o potwierdzenie przed usunięciem istniejących tłumaczeń.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** użyłem tej metody, aby zaktualizować wszystkie przetłumaczone pliki na język hiszpański. Polecam tę metodę, gdy w oryginalnej treści zaszły znaczące zmiany w wielu dokumentach markdown. Jeśli do zaktualizowania jest tylko kilka przetłumaczonych plików markdown, bardziej efektywne jest ręczne usunięcie tych konkretnych plików, a następnie użycie metody `-a`, aby dodać zaktualizowane tłumaczenia.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Tłumaczenie tylko obrazów

Aby przetłumaczyć tylko pliki obrazów w projekcie, użyj opcji `-img`:

```bash
translate -l "ko" -img
```

To polecenie przetłumaczy tylko obrazy na język koreański, nie zmieniając żadnych plików markdown.

### 6. Tłumaczenie tylko plików markdown

Aby przetłumaczyć tylko pliki markdown w projekcie, użyj opcji `-md`:

```bash
translate -l "ko" -md
```

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** użyłem tej metody, aby sprawdzić błędy tłumaczenia w plikach koreańskich i automatycznie ponowić tłumaczenie dla plików, w których wykryto problemy.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ta opcja sprawdza błędy tłumaczenia. Obecnie, jeśli różnica w liczbie łamań linii między oryginałem a tłumaczeniem przekracza sześć, plik jest oznaczany jako zawierający błąd tłumaczenia. Planuję w przyszłości ulepszyć to kryterium, aby było bardziej elastyczne.

Na przykład ta metoda jest przydatna do wykrywania brakujących fragmentów lub uszkodzonych tłumaczeń i automatycznie ponowi tłumaczenie tych plików.

Jeśli jednak już wiesz, które pliki są problematyczne, bardziej efektywne jest ręczne usunięcie tych plików i użycie opcji `-a`, aby je ponownie przetłumaczyć.

### 8. Tryb debugowania

Aby włączyć szczegółowe logowanie do rozwiązywania problemów, użyj opcji `-d`:

```bash
translate -l "ko" -d
```

To polecenie uruchomi tłumaczenie w trybie debugowania, dostarczając dodatkowych informacji w logach, które mogą pomóc w identyfikacji problemów podczas procesu tłumaczenia.

#### Przykład na Phi-3 CookBook

W **Phi-3 CookBook** napotkałem problem, w którym tłumaczenia z wieloma linkami w plikach markdown powodowały błędy formatowania, takie jak uszkodzone tłumaczenia i pomijane łamania linii. Aby zdiagnozować ten problem, użyłem opcji `-d`, aby zobaczyć, jak przebiegał proces tłumaczenia.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tłumaczenie na wszystkie języki

Jeśli chcesz przetłumaczyć projekt na wszystkie obsługiwane języki, użyj słowa kluczowego all.

> [!WARNING]
> Tłumaczenie na wszystkie języki naraz może zająć dużo czasu w zależności od wielkości projektu. Na przykład tłumaczenie **Phi-3 CookBook** na hiszpański zajęło około 2 godzin. Przy takiej skali nie jest praktyczne, aby jedna osoba obsługiwała 20 języków. Zaleca się podzielenie pracy między kilku współtwórców, z których każdy zajmuje się jednym lub dwoma językami, i stopniowe aktualizowanie tłumaczeń.

```bash
translate -l "all"
```

To polecenie przetłumaczy projekt na wszystkie dostępne języki. Jeśli zdecydujesz się kontynuować, tłumaczenie może zająć dużo czasu w zależności od rozmiaru projektu.

> [!TIP]
>
> ### Ręczne usuwanie przetłumaczonych plików (opcjonalnie)
> Przetłumaczone pliki są teraz automatycznie wykrywane i czyszczone, gdy plik źródłowy zostanie zaktualizowany.
>
> Jeśli jednak chcesz ręcznie zaktualizować tłumaczenie – na przykład, aby ponownie przetłumaczyć konkretny plik lub nadpisać zachowanie systemu – możesz użyć poniższego polecenia, aby usunąć wszystkie wersje pliku w folderach językowych.
>
> ### Na Windows:
> 1. **Używając Command Prompt**:
>    - Otwórz Command Prompt.
>    - Przejdź do folderu, w którym znajdują się pliki, używając polecenia `cd`.
>    - Użyj poniższego polecenia, aby usunąć pliki:
>      ```
>      del /s *filename*
>      ```
>      Zamień `filename` na konkretną część nazwy pliku, której szukasz. Opcja `/s` przeszukuje podfoldery.
>
> 2. **Używając PowerShell**:
>    - Otwórz PowerShell.
>    - Uruchom to polecenie:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Zamień `"C:\YourPath"` na ścieżkę do folderu, a `filename` na konkretną nazwę.
>
> ### Na macOS/Linux:
> 1. **Używając Terminala**:
>   - Otwórz Terminal.
>   - Przejdź do katalogu za pomocą `cd`.
>   - Użyj polecenia `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Zamień `filename` na konkretną nazwę.
>
> Zawsze dokładnie sprawdź pliki przed usunięciem, aby uniknąć przypadkowej utraty danych.
>
> Po usunięciu plików, które chcesz zastąpić, po prostu ponownie uruchom polecenie `translate -l`, aby zaktualizować najnowsze zmiany w plikach.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najdokładniejsze, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za autorytatywne źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.