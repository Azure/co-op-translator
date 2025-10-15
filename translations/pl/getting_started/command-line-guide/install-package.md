<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:08:23+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "pl"
}
-->
# Zainstaluj pakiet Co-op translator

**Co-op Translator** to narzędzie wiersza poleceń (CLI), które pomaga tłumaczyć wszystkie pliki markdown oraz obrazy w Twoim projekcie na wiele języków. Ten poradnik przeprowadzi Cię przez konfigurację translatora i uruchomienie go w różnych scenariuszach.

### Utwórz środowisko wirtualne

Możesz utworzyć środowisko wirtualne za pomocą `pip` lub `Poetry`. Wpisz jedno z poniższych poleceń w swoim terminalu.

#### Używając pip

```bash
python -m venv .venv
```

#### Używając Poetry

```bash
poetry init
```

### Aktywuj środowisko wirtualne

Po utworzeniu środowiska wirtualnego musisz je aktywować. Kroki różnią się w zależności od systemu operacyjnego. Wpisz poniższe polecenie w swoim terminalu.

#### Zarówno dla pip, jak i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Używając Poetry

1. Jeśli utworzyłeś środowisko za pomocą Poetry, wpisz poniższe polecenie w swoim terminalu, aby je aktywować.

    ```bash
    poetry shell
    ```

### Instalacja pakietu i wymaganych zależności

Gdy Twoje środowisko wirtualne jest już gotowe i aktywowane, kolejnym krokiem jest instalacja niezbędnych zależności.

### Szybka instalacja

Zainstaluj Co-Op Translator za pomocą pip

```
pip install co-op-translator
```
Lub

Zainstaluj za pomocą poetry
```
poetry add co-op-translator
```

#### Używając pip (z requirements.txt) jeśli sklonujesz to repozytorium

> [!NOTE]
> Proszę NIE robić tego, jeśli instalujesz co-op translator przez szybką instalację.

1. Jeśli używasz pip, wpisz poniższe polecenie w swoim terminalu. Automatycznie zainstaluje ono wymagane pakiety określone w pliku `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Używając Poetry (z pyproject.toml)

1. Jeśli używasz Poetry, wpisz poniższe polecenie w swoim terminalu. Automatycznie zainstaluje ono wymagane pakiety określone w pliku `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było dokładne, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za autorytatywne źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji o znaczeniu krytycznym zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.