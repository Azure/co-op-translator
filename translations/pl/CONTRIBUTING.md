<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:01:53+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pl"
}
-->
# Współtworzenie Co-op Translator

Ten projekt zachęca do zgłaszania wkładów i sugestii. Większość wkładów wymaga zgody na
Umowę Licencyjną Współtwórcy (CLA), która potwierdza, że masz prawo i faktycznie udzielasz nam
praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na https://cla.opensource.microsoft.com.

Po przesłaniu pull requesta, bot CLA automatycznie sprawdzi, czy musisz dostarczyć
CLA i odpowiednio oznaczy PR (np. status, komentarz). Wystarczy, że wykonasz to raz dla wszystkich repozytoriów korzystających z naszej CLA.

## Konfiguracja środowiska deweloperskiego

Aby skonfigurować środowisko deweloperskie dla tego projektu, zalecamy użycie Poetry do zarządzania zależnościami. Używamy `pyproject.toml` do zarządzania zależnościami projektu, więc do instalacji zależności powinieneś użyć Poetry.

### Utworzenie wirtualnego środowiska

#### Za pomocą pip

```bash
python -m venv .venv
```

#### Za pomocą Poetry

```bash
poetry init
```

### Aktywacja wirtualnego środowiska

#### Dla pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Za pomocą Poetry

```bash
poetry shell
```

### Instalacja pakietu i wymaganych pakietów

#### Za pomocą Poetry (z pyproject.toml)

```bash
poetry install
```

### Testowanie ręczne

Przed przesłaniem PR ważne jest przetestowanie funkcji tłumaczenia na rzeczywistej dokumentacji:

1. Utwórz katalog testowy w katalogu głównym:
    ```bash
    mkdir test_docs
    ```

2. Skopiuj do katalogu testowego wybrane pliki markdown i obrazy, które chcesz przetłumaczyć. Na przykład:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Zainstaluj pakiet lokalnie:
    ```bash
    pip install -e .
    ```

4. Uruchom Co-op Translator na swoich dokumentach testowych:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Sprawdź przetłumaczone pliki w `test_docs/translations` i `test_docs/translated_images`, aby zweryfikować:
   - Jakość tłumaczenia
   - Poprawność komentarzy z metadanymi
   - Zachowanie oryginalnej struktury markdown
   - Poprawne działanie linków i obrazów

To ręczne testowanie pomaga upewnić się, że Twoje zmiany działają dobrze w rzeczywistych scenariuszach.

### Zmienne środowiskowe

1. Utwórz plik `.env` w katalogu głównym, kopiując dostarczony plik `.env.template`.
1. Wypełnij zmienne środowiskowe zgodnie z instrukcjami.

> [!TIP]
>
> ### Dodatkowe opcje środowiska deweloperskiego
>
> Oprócz uruchamiania projektu lokalnie, możesz także skorzystać z GitHub Codespaces lub VS Code Dev Containers jako alternatywnego środowiska deweloperskiego.
>
> #### GitHub Codespaces
>
> Możesz uruchomić te przykłady praktycznie, korzystając z GitHub Codespaces, bez konieczności dodatkowej konfiguracji.
>
> Przycisk otworzy instancję VS Code w przeglądarce:
>
> 1. Otwórz szablon (może to potrwać kilka minut):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Uruchamianie lokalne za pomocą VS Code Dev Containers
>
> ⚠️ Ta opcja zadziała tylko, jeśli Docker Desktop ma przydzielone co najmniej 16 GB RAM. Jeśli masz mniej niż 16 GB RAM, możesz spróbować opcji [GitHub Codespaces](../..) lub [ustawić środowisko lokalnie](../..).
>
> Powiązaną opcją są VS Code Dev Containers, które otworzą projekt w lokalnym VS Code z użyciem [rozszerzenia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Uruchom Docker Desktop (zainstaluj, jeśli jeszcze nie masz)
> 2. Otwórz projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Styl kodu

Używamy [Black](https://github.com/psf/black) jako formatera kodu Python, aby utrzymać spójny styl kodu w całym projekcie. Black to bezkompromisowy formater, który automatycznie formatuje kod Python zgodnie ze stylem Black.

#### Konfiguracja

Konfiguracja Black jest określona w naszym `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacja Black

Black możesz zainstalować za pomocą Poetry (zalecane) lub pip:

##### Za pomocą Poetry

Black jest automatycznie instalowany podczas konfiguracji środowiska deweloperskiego:
```bash
poetry install
```

##### Za pomocą pip

Jeśli używasz pip, możesz zainstalować Black bezpośrednio:
```bash
pip install black
```

#### Użycie Black

##### Z Poetry

1. Sformatuj wszystkie pliki Python w projekcie:
    ```bash
    poetry run black .
    ```

2. Sformatuj konkretny plik lub katalog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Z pip

1. Sformatuj wszystkie pliki Python w projekcie:
    ```bash
    black .
    ```

2. Sformatuj konkretny plik lub katalog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Zalecamy skonfigurowanie edytora tak, aby automatycznie formatował kod za pomocą Black przy zapisie. Większość nowoczesnych edytorów obsługuje to przez rozszerzenia lub wtyczki.

## Uruchamianie Co-op Translator

Aby uruchomić Co-op Translator za pomocą Poetry w swoim środowisku, wykonaj następujące kroki:

1. Przejdź do katalogu, w którym chcesz przeprowadzić testy tłumaczenia lub utwórz tymczasowy folder do testów.

2. Wykonaj poniższe polecenie. Zastąp `-l ko` kodem języka, na który chcesz tłumaczyć. Flaga `-d` oznacza tryb debugowania.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Upewnij się, że środowisko Poetry jest aktywne (poetry shell) przed uruchomieniem polecenia.

## Dodanie nowego języka

Zachęcamy do dodawania wsparcia dla nowych języków. Przed otwarciem PR wykonaj poniższe kroki, aby ułatwić przegląd.

1. Dodaj język do mapowania czcionek
   - Edytuj `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodaj wpis z:
     - `code`: kod języka w stylu ISO (np. `vi`)
     - `name`: przyjazna nazwa do wyświetlania
     - `font`: czcionka dołączona w `src/co_op_translator/fonts/`, która obsługuje dany skrypt
     - `rtl`: `true` jeśli język pisany jest od prawej do lewej, w przeciwnym razie `false`

2. Dołącz wymagane pliki czcionek (jeśli potrzebne)
   - Jeśli wymagana jest nowa czcionka, sprawdź zgodność licencji z dystrybucją open source
   - Dodaj plik czcionki do `src/co_op_translator/fonts/`

3. Weryfikacja lokalna
   - Uruchom tłumaczenia na małej próbce (Markdown, obrazy i notebooki, jeśli dotyczy)
   - Sprawdź, czy wynik jest poprawnie renderowany, w tym czcionki i ewentualny układ RTL

4. Aktualizacja dokumentacji
   - Upewnij się, że język pojawia się w `getting_started/supported-languages.md`
   - Nie trzeba zmieniać `getting_started/README_languages_template.md`; jest generowany z listy obsługiwanych języków

5. Otwórz PR
   - Opisz dodany język oraz kwestie licencyjne czcionek, jeśli dotyczy
   - Dołącz zrzuty ekranu z renderowanymi wynikami, jeśli to możliwe

Przykładowy wpis YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testowanie nowego języka

Nowy język możesz przetestować, uruchamiając następujące polecenie:

```bash
# Utwórz i aktywuj środowisko wirtualne
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Zainstaluj pakiet deweloperski
pip install -e .
# Uruchom tłumaczenie
translate -l "new_lang"
```

## Opiekunowie projektu

### Format wiadomości commit i strategia scalania

Aby zapewnić spójność i przejrzystość historii commitów w projekcie, stosujemy określony format wiadomości commit **dla ostatecznej wiadomości commit** przy użyciu strategii **Squash and Merge**.

Gdy pull request (PR) jest scalany, poszczególne commity są łączone w jeden. Ostateczna wiadomość commit powinna mieć poniższy format, aby utrzymać czystą i spójną historię.

#### Format wiadomości commit (dla squash and merge)

Używamy następującego formatu wiadomości commit:

```bash
<type>: <description> (#<numer PR>)
```

- **type**: Określa kategorię commita. Używamy następujących typów:
  - `Docs`: dla aktualizacji dokumentacji.
  - `Build`: dla zmian związanych z systemem budowania lub zależnościami, w tym aktualizacji plików konfiguracyjnych, workflow CI lub Dockerfile.
  - `Core`: dla modyfikacji podstawowej funkcjonalności lub cech projektu, szczególnie dotyczących plików w katalogu `src/co_op_translator/core`.

- **description**: Zwięzłe podsumowanie zmiany.
- **PR number**: Numer pull requesta powiązanego z commitem.

**Przykłady**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Obecnie prefiksy **`Docs`**, **`Core`** i **`Build`** są automatycznie dodawane do tytułów PR na podstawie etykiet przypisanych do zmodyfikowanego kodu źródłowego. Jeśli odpowiednia etykieta jest zastosowana, zwykle nie musisz ręcznie zmieniać tytułu PR. Wystarczy zweryfikować, czy wszystko jest poprawne i prefiks został wygenerowany prawidłowo.

#### Strategia scalania

Domyślną strategią scalania pull requestów jest **Squash and Merge**. Ta strategia zapewnia, że wiadomości commitów będą zgodne z naszym formatem, nawet jeśli pojedyncze commity nie są.

**Powody**:

- Czysta, liniowa historia projektu.
- Spójność wiadomości commit.
- Mniej szumu z drobnych commitów (np. "popraw literówkę").

Podczas scalania upewnij się, że ostateczna wiadomość commit spełnia opisany powyżej format.

**Przykład Squash and Merge**
Jeśli PR zawiera następujące commity:

- `fix typo`
- `update README`
- `adjust formatting`

Zostaną one połączone w:
`Docs: Improve documentation clarity and formatting (#65)`

### Proces wydania

Ta sekcja opisuje najprostszy sposób dla opiekunów projektu na opublikowanie nowej wersji Co-op Translator.

#### 1. Zwiększenie wersji w `pyproject.toml`

1. Wybierz kolejny numer wersji (stosujemy wersjonowanie semantyczne: `MAJOR.MINOR.PATCH`).
2. Edytuj `pyproject.toml` i zaktualizuj pole `version` w sekcji `[tool.poetry]`.
3. Otwórz dedykowany pull request, który zmienia tylko wersję (oraz ewentualne automatycznie aktualizowane pliki lock/metadata, jeśli występują).
4. Po przeglądzie użyj **Squash and Merge** i upewnij się, że ostateczna wiadomość commit spełnia opisany format.

#### 2. Utworzenie wydania na GitHub

1. Przejdź do strony repozytorium na GitHub i otwórz **Releases** → **Draft a new release**.
2. Utwórz nowy tag (np. `v0.13.0`) z gałęzi `main`.
3. Ustaw tytuł wydania na tę samą wersję (np. `v0.13.0`).
4. Kliknij **Generate release notes**, aby automatycznie wypełnić changelog.
5. Opcjonalnie edytuj tekst (np. aby wyróżnić nowo obsługiwane języki lub ważne zmiany).
6. Opublikuj wydanie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->