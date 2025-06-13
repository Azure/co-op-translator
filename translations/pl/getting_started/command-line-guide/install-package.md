<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:34:17+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "pl"
}
-->
# Instalacja pakietu Co-op translator

**Co-op Translator** to narzędzie wiersza poleceń (CLI) stworzone, aby pomóc Ci przetłumaczyć wszystkie pliki markdown oraz obrazy w Twoim projekcie na wiele języków. Ten przewodnik pokaże Ci, jak skonfigurować translator i uruchomić go w różnych scenariuszach.

### Utwórz środowisko wirtualne

Możesz utworzyć środowisko wirtualne za pomocą `pip` lub `Poetry`. Wpisz jedną z poniższych komend w terminalu.

#### Korzystając z pip

```bash
python -m venv .venv
```

#### Korzystając z Poetry

```bash
poetry init
```

### Aktywuj środowisko wirtualne

Po utworzeniu środowiska wirtualnego musisz je aktywować. Kroki różnią się w zależności od systemu operacyjnego. Wpisz następującą komendę w terminalu.

#### Dla pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Korzystając z Poetry

1. Jeśli utworzyłeś środowisko za pomocą Poetry, wpisz w terminalu poniższą komendę, aby je aktywować.

    ```bash
    poetry shell
    ```

### Instalacja pakietu i wymaganych zależności

Gdy środowisko wirtualne jest już gotowe i aktywne, kolejnym krokiem jest instalacja niezbędnych zależności.

### Szybka instalacja

Zainstaluj Co-Op Translator za pomocą pip

```
pip install co-op-translator
```
Lub

Zainstaluj za pomocą Poetry
```
poetry add co-op-translator
```

#### Korzystając z pip (z pliku requirements.txt), jeśli sklonujesz to repozytorium

![NOTE] Proszę NIE rób tego, jeśli instalujesz co-op translator przez szybki instalator.

1. Jeśli używasz pip, wpisz w terminalu następującą komendę. Automatycznie zainstaluje wymagane pakiety określone w pliku `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Korzystając z Poetry (z pliku pyproject.toml)

1. Jeśli używasz Poetry, wpisz w terminalu następującą komendę. Automatycznie zainstaluje wymagane pakiety określone w pliku `pyproject.toml`:

    ```bash
    poetry install
    ```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.