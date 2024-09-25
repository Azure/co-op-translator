# Contributing to Co Op Translator

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

## Development environment setup

To set up the development environment for this project, we recommend using Poetry for managing dependencies. We use `pyproject.toml` to manage project dependencies, and therefore, to install dependencies, you should use Poetry.

### Create a virtual environment

#### Using pip

```bash
python -m venv venv
```

#### Using Poetry

```bash
poetry init
```

### Activate the virtual environment

#### For both pip and Poetry

- Windows:

    ```bash
    venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source venv/bin/activate
    ```

#### Using Poetry

```bash
poetry shell
```

### Installing the Package and required Packages

#### Using Poetry (from pyproject.toml)

```bash
poetry install
```

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` file.
1. Fill in the environment variables as guided.

## Running Co Op Translator

To run Co Op Translator using Poetry in your environment, follow these steps:

1. Navigate to the directory where you want to perform translation tests or create a temporary folder for testing purposes.

2. Execute the following command. Replace `-l ko` with the language code you wish to translate into. The `-d` flag indicates debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Ensure your Poetry environment is activated (poetry shell) before running the command.

