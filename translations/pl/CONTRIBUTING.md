<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:06:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pl"
}
-->
# Współtworzenie Co-op Translator

Ten projekt zachęca do współtworzenia i zgłaszania sugestii. Większość kontrybucji wymaga zaakceptowania Umowy Licencyjnej Współtwórcy (CLA), w której oświadczasz, że masz prawo i faktycznie udzielasz nam praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na https://cla.opensource.microsoft.com.

Gdy zgłaszasz pull request, bot CLA automatycznie sprawdzi, czy musisz zaakceptować CLA i odpowiednio oznaczy PR (np. status, komentarz). Po prostu postępuj zgodnie z instrukcjami bota. Wystarczy to zrobić raz dla wszystkich repozytoriów korzystających z naszego CLA.

## Konfiguracja środowiska deweloperskiego

Aby skonfigurować środowisko deweloperskie dla tego projektu, zalecamy użycie Poetry do zarządzania zależnościami. Używamy `pyproject.toml` do zarządzania zależnościami projektu, dlatego do ich instalacji powinieneś użyć Poetry.

### Tworzenie środowiska wirtualnego

#### Z użyciem pip

```bash
python -m venv .venv
```

#### Z użyciem Poetry

```bash
poetry init
```

### Aktywacja środowiska wirtualnego

#### Zarówno dla pip, jak i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Z użyciem Poetry

```bash
poetry shell
```

### Instalacja pakietu i wymaganych zależności

#### Z użyciem Poetry (z pliku pyproject.toml)

```bash
poetry install
```

### Testowanie manualne

Przed zgłoszeniem PR ważne jest przetestowanie funkcjonalności tłumaczenia na prawdziwej dokumentacji:

1. Utwórz katalog testowy w katalogu głównym:
    ```bash
    mkdir test_docs
    ```

2. Skopiuj wybraną dokumentację markdown oraz obrazy, które chcesz przetłumaczyć, do katalogu testowego. Przykład:
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

5. Sprawdź przetłumaczone pliki w `test_docs/translations` oraz `test_docs/translated_images`, aby zweryfikować:
   - Jakość tłumaczenia
   - Poprawność komentarzy z metadanymi
   - Zachowanie oryginalnej struktury markdown
   - Poprawność działania linków i obrazów

To testowanie manualne pomaga upewnić się, że Twoje zmiany działają poprawnie w rzeczywistych scenariuszach.

### Zmienne środowiskowe

1. Utwórz plik `.env` w katalogu głównym, kopiując dostarczony plik `.env.template`.
1. Uzupełnij zmienne środowiskowe zgodnie z instrukcjami.

> [!TIP]
>
> ### Dodatkowe opcje środowiska deweloperskiego
>
> Oprócz uruchamiania projektu lokalnie, możesz także skorzystać z GitHub Codespaces lub VS Code Dev Containers jako alternatywnego środowiska deweloperskiego.
>
> #### GitHub Codespaces
>
> Możesz uruchomić te przykłady wirtualnie za pomocą GitHub Codespaces bez dodatkowej konfiguracji.
>
> Przycisk otworzy instancję VS Code w przeglądarce:
>
> 1. Otwórz szablon (może to potrwać kilka minut):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Uruchamianie lokalnie z użyciem VS Code Dev Containers
>
> ⚠️ Ta opcja działa tylko, jeśli Docker Desktop ma przydzielone co najmniej 16 GB RAM. Jeśli masz mniej niż 16 GB RAM, możesz skorzystać z [opcji GitHub Codespaces](../..) lub [skonfigurować lokalnie](../..).
>
> Powiązaną opcją są VS Code Dev Containers, które otwierają projekt w lokalnym VS Code z użyciem [rozszerzenia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Uruchom Docker Desktop (zainstaluj, jeśli nie masz)
> 2. Otwórz projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Styl kodu

Używamy [Black](https://github.com/psf/black) jako formatera kodu Python, aby zachować spójny styl kodowania w całym projekcie. Black to bezkompromisowy formatter, który automatycznie dostosowuje kod do ustalonego stylu.

#### Konfiguracja

Konfiguracja Black znajduje się w naszym pliku `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacja Black

Możesz zainstalować Black za pomocą Poetry (zalecane) lub pip:

##### Z użyciem Poetry

Black jest instalowany automatycznie podczas konfiguracji środowiska deweloperskiego:
```bash
poetry install
```

##### Z użyciem pip

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

2. Sformatuj wybrany plik lub katalog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Z pip

1. Sformatuj wszystkie pliki Python w projekcie:
    ```bash
    black .
    ```

2. Sformatuj wybrany plik lub katalog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Zalecamy skonfigurowanie edytora, aby automatycznie formatował kod Black przy zapisie. Większość nowoczesnych edytorów obsługuje to przez rozszerzenia lub wtyczki.

## Uruchamianie Co-op Translator

Aby uruchomić Co-op Translator z użyciem Poetry w swoim środowisku, wykonaj następujące kroki:

1. Przejdź do katalogu, w którym chcesz wykonać testy tłumaczenia lub utwórz tymczasowy folder do testów.

2. Wykonaj poniższe polecenie. Zamień `-l ko` na kod języka, na który chcesz tłumaczyć. Flaga `-d` oznacza tryb debugowania.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Upewnij się, że środowisko Poetry jest aktywne (poetry shell) przed uruchomieniem polecenia.

## Dodanie nowego języka

Chętnie przyjmujemy kontrybucje dodające obsługę nowych języków. Przed otwarciem PR wykonaj poniższe kroki, aby ułatwić proces recenzji.

1. Dodaj język do mapowania czcionek
   - Edytuj `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodaj wpis z:
     - `code`: kod języka w stylu ISO (np. `vi`)
     - `name`: przyjazna nazwa wyświetlana
     - `font`: czcionka dostępna w `src/co_op_translator/fonts/`, obsługująca dany alfabet
     - `rtl`: `true` jeśli język jest pisany od prawej do lewej, w przeciwnym razie `false`

2. Dodaj wymagane pliki czcionek (jeśli potrzeba)
   - Jeśli wymagana jest nowa czcionka, sprawdź zgodność licencji z otwartym oprogramowaniem
   - Dodaj plik czcionki do `src/co_op_translator/fonts/`

3. Weryfikacja lokalna
   - Przetłumacz małą próbkę (Markdown, obrazy, notatniki – w zależności od potrzeb)
   - Sprawdź, czy wynik renderuje się poprawnie, w tym czcionki i ewentualny układ RTL

4. Aktualizacja dokumentacji
   - Upewnij się, że język pojawia się w `getting_started/supported-languages.md`
   - Nie trzeba zmieniać `README_languages_template.md`; jest generowany automatycznie

5. Otwórz PR
   - Opisz dodany język oraz kwestie związane z czcionką/licencją
   - Jeśli to możliwe, dołącz zrzuty ekranu z renderowania wyników

Przykładowy wpis YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Utrzymujący projekt

### Format wiadomości commitów i strategia scalania

Aby zapewnić spójność i przejrzystość historii commitów, stosujemy określony format wiadomości commitów **dla końcowej wiadomości** przy użyciu strategii **Squash and Merge**.

Gdy pull request (PR) jest scalany, poszczególne commity są łączone w jeden. Końcowa wiadomość commita powinna mieć poniższy format, aby zachować czytelną i spójną historię.

#### Format wiadomości commita (dla squash and merge)

Używamy następującego formatu wiadomości commitów:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Określa kategorię commita. Używamy następujących typów:
  - `Docs`: Aktualizacje dokumentacji.
  - `Build`: Zmiany związane z systemem budowania lub zależnościami, w tym aktualizacje plików konfiguracyjnych, workflow CI lub Dockerfile.
  - `Core`: Modyfikacje głównej funkcjonalności projektu lub funkcji, szczególnie dotyczące plików w katalogu `src/co_op_translator/core`.

- **description**: Krótkie podsumowanie zmiany.
- **PR number**: Numer pull requestu powiązanego z commitem.

**Przykłady**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Obecnie prefiksy **`Docs`**, **`Core`** i **`Build`** są automatycznie dodawane do tytułów PR na podstawie etykiet przypisanych do zmodyfikowanego kodu źródłowego. Jeśli odpowiednia etykieta jest przypisana, zazwyczaj nie musisz ręcznie zmieniać tytułu PR. Wystarczy sprawdzić, czy wszystko jest poprawne i prefiks został wygenerowany prawidłowo.

#### Strategia scalania

Używamy **Squash and Merge** jako domyślnej strategii dla pull requestów. Ta strategia zapewnia, że wiadomości commitów są zgodne z naszym formatem, nawet jeśli poszczególne commity nie są.

**Powody**:

- Czysta, liniowa historia projektu.
- Spójność wiadomości commitów.
- Mniej "szumu" od drobnych commitów (np. "fix typo").

Podczas scalania upewnij się, że końcowa wiadomość commita jest zgodna z opisanym powyżej formatem.

**Przykład Squash and Merge**
Jeśli PR zawiera następujące commity:

- `fix typo`
- `update README`
- `adjust formatting`

Powinny zostać połączone w:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najdokładniejsze, należy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Za autorytatywne źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.