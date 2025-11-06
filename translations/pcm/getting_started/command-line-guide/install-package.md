<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-11-06T17:31:49+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "pcm"
}
-->
# Install di Co-op translator package

Di **Co-op Translator** na command-line interface (CLI) tool wey go help you translate all di markdown files and images wey dey your project into plenty languages. Dis tutorial go show you how you go fit configure di translator and use am for different cases.

### Create virtual environment

You fit create virtual environment using `pip` or `Poetry`. Type one of di commands wey dey below for your terminal.

#### Using pip

```bash
python -m venv .venv
```

#### Using Poetry

```bash
poetry init
```

### Activate di virtual environment

After you don create di virtual environment, you go need activate am. Di steps dey different based on di operating system wey you dey use. Type di command wey dey below for your terminal.

#### For both pip and Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Using Poetry

1. If you use Poetry create di environment, type di command wey dey below for your terminal to activate am.

    ```bash
    poetry shell
    ```

### Install di Package and di required Packages

After you don set up and activate your virtual environment, di next step na to install di dependencies wey you need.

### Quick install

Install Co-Op Translator using pip

```
pip install co-op-translator
```
Or 

Install am using poetry
```
poetry add co-op-translator
```

#### Using pip (from requirements.txt) if you clone dis repo 

> [!NOTE]
> No try do dis one if you install co-op translator using di quick install.

1. If you dey use pip, type di command wey dey below for your terminal. E go automatically install di required packages wey dey di `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

#### Using Poetry (from pyproject.toml)

1. If you dey use Poetry, type di command wey dey below for your terminal. E go automatically install di required packages wey dey di `pyproject.toml` file:

    ```bash
    poetry install
    ```

---

**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important information, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.