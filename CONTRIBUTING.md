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

> [!TIP]
>
> ### Additional development environment options
>
> In addition to running the project locally, you can also use GitHub Codespaces or VS Code Dev Containers for an alternative development environment setup.
>
> #### GitHub Codespaces
>
> You can run this samples virtually by using GitHub Codespaces and no additional settings or setup are required. 
>
> The button will open a web-based VS Code instance in your browser:
>
> 1. Open the template (this may take several minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Running Locally using VS Code Dev Containers
>
> ⚠️ This option will only work if your Docker Desktop is allocated at least 16 GB of RAM. If you have less than 16 GB of RAM, you can try the [GitHub Codespaces option](#github-codespaces) or [set it up locally](#development-environment-setup).
>
> A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install it if not already installed)
> 2. Open the project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

## Running Co Op Translator

To run Co Op Translator using Poetry in your environment, follow these steps:

1. Navigate to the directory where you want to perform translation tests or create a temporary folder for testing purposes.

2. Execute the following command. Replace `-l ko` with the language code you wish to translate into. The `-d` flag indicates debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Ensure your Poetry environment is activated (poetry shell) before running the command.
