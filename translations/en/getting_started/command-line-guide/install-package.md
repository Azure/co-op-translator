<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:55:46+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "en"
}
-->
# Install the Co-op translator package

The **Co-op Translator** is a command-line interface (CLI) tool designed to help you translate all the markdown files and images in your project into multiple languages. This tutorial will guide you through setting up the translator and running it for different scenarios.

### Create a virtual environment

You can create a virtual environment using either `pip` or `Poetry`. Enter one of the following commands in your terminal.

#### Using pip

```bash
python -m venv .venv
```

#### Using Poetry

```bash
poetry init
```

### Activate the virtual environment

After creating the virtual environment, you need to activate it. The steps vary depending on your operating system. Enter the following command in your terminal.

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

1. If you created the environment with Poetry, enter the following command in your terminal to activate it.

    ```bash
    poetry shell
    ```

### Installing the Package and required Packages

Once your virtual environment is ready and activated, the next step is to install the necessary dependencies.

### Quick install

Install Co-op Translator via pip

```
pip install co-op-translator
```
Or 

Install via Poetry
```
poetry add co-op-translator
```

#### Using pip (from requirements.txt) if you clone this repo 

![NOTE] Please do NOT do this if you install co-op translator via the quick install.

1. If you're using pip, enter the following command in your terminal. It will automatically install the required packages listed in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

#### Using Poetry (from pyproject.toml)

1. If you're using Poetry, enter the following command in your terminal. It will automatically install the required packages listed in the `pyproject.toml` file:

    ```bash
    poetry install
    ```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.