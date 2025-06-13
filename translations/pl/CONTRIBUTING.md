<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:33:50+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pl"
}
-->
# Contributing to Co-op Translator

Ten projekt zachęca do zgłaszania wkładów i sugestii. Większość wkładów wymaga, abyś zgodził się na  
Contributor License Agreement (CLA), w którym oświadczasz, że masz prawo i faktycznie udzielasz nam  
praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na https://cla.opensource.microsoft.com.

Gdy zgłaszasz pull request, bot CLA automatycznie sprawdzi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. status check, komentarz). Po prostu postępuj zgodnie z instrukcjami bota. Musisz to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

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

Przed zgłoszeniem PR ważne jest przetestowanie funkcji tłumaczenia na rzeczywistej dokumentacji:

1. Utwórz katalog testowy w katalogu głównym:  
    ```bash
    mkdir test_docs
    ```

2. Skopiuj wybraną dokumentację markdown i obrazy, które chcesz przetłumaczyć, do katalogu testowego. Na przykład:  
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

5. Sprawdź przetłumaczone pliki w `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.  
1. Wypełnij zmienne środowiskowe zgodnie z instrukcjami.

> [!TIP]
>
> ### Dodatkowe opcje środowiska deweloperskiego
>
> Oprócz uruchamiania projektu lokalnie, możesz także użyć GitHub Codespaces lub VS Code Dev Containers jako alternatywnego środowiska deweloperskiego.
>
> #### GitHub Codespaces
>
> Możesz uruchomić te przykłady praktycznie, korzystając z GitHub Codespaces, bez konieczności dodatkowych ustawień.
>
> Przycisk otworzy webową wersję VS Code w Twojej przeglądarce:
>
> 1. Otwórz szablon (może to zająć kilka minut):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Uruchamianie lokalnie za pomocą VS Code Dev Containers
>
> ⚠️ Ta opcja zadziała tylko, jeśli Docker Desktop ma przydzielone co najmniej 16 GB RAM. Jeśli masz mniej niż 16 GB RAM, możesz wypróbować [opcję GitHub Codespaces](../..) lub [skonfigurować lokalnie](../..).
>
> Powiązaną opcją są VS Code Dev Containers, które otworzą projekt w lokalnym VS Code za pomocą [rozszerzenia Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Uruchom Docker Desktop (zainstaluj, jeśli jeszcze nie masz)
> 2. Otwórz projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Styl kodu

Do formatowania kodu Python używamy [Black](https://github.com/psf/black), aby utrzymać spójny styl w całym projekcie. Black to bezkompromisowy formatator kodu, który automatycznie formatuje kod Python zgodnie ze stylem Black.

#### Konfiguracja

Konfiguracja Black znajduje się w naszym `pyproject.toml`:

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
> Zalecamy skonfigurowanie edytora tak, aby automatycznie formatował kod Black podczas zapisu. Większość nowoczesnych edytorów wspiera to przez rozszerzenia lub wtyczki.

## Uruchamianie Co-op Translator

Aby uruchomić Co-op Translator za pomocą Poetry w swoim środowisku, wykonaj następujące kroki:

1. Przejdź do katalogu, w którym chcesz przeprowadzać testy tłumaczeń lub utwórz tymczasowy folder do testów.

2. Wykonaj poniższe polecenie. Flaga `-l ko` with the language code you wish to translate into. The `-d` oznacza tryb debugowania.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Upewnij się, że Twoje środowisko Poetry jest aktywne (poetry shell) przed uruchomieniem polecenia.

## Maintainers

### Komunikaty commitów i strategia scalania

Aby zapewnić spójność i czytelność historii commitów w naszym projekcie, stosujemy określony format komunikatów commitów **dla ostatecznego komunikatu** przy użyciu strategii **Squash and Merge**.

Gdy pull request (PR) zostanie scalony, poszczególne commity zostaną złączone w jeden commit. Ostateczny komunikat commita powinien mieć poniższy format, aby zachować czystą i spójną historię.

#### Format komunikatu commita (dla squash and merge)

Używamy następującego formatu komunikatów:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Określa kategorię commita. Używamy następujących typów:  
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być traktowany jako źródło wiarygodne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.