<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:44:41+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Contributing to Co-op Translator

This project accepts contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) confirming that you have the rights to grant us permission to use your contribution. For more details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically check if you need to provide a CLA and will label the PR accordingly (e.g., status check, comment). Just follow the bot’s instructions. You only need to do this once for all repos using our CLA.

## Development environment setup

To prepare the development environment for this project, we recommend using Poetry to manage dependencies. We use `pyproject.toml` to handle project dependencies, so you should use Poetry to install them.

### Create a virtual environment

#### Using pip

```bash
python -m venv .venv
```

#### Using Poetry

```bash
poetry init
```

### Activate the virtual environment

#### For both pip and Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
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

### Manual testing

Before submitting a PR, it’s important to test the translation feature with actual documentation:

1. Create a test directory at the root:
    ```bash
    mkdir test_docs
    ```

2. Copy some markdown documentation and images you want to translate into the test directory. For example:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Install the package locally:
    ```bash
    pip install -e .
    ```

4. Run Co-op Translator on your test documents:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Check the translated files in `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Fill in the environment variables as instructed.

> [!TIP]
>
> ### Additional development environment options
>
> Besides running the project locally, you can also use GitHub Codespaces or VS Code Dev Containers as alternative development environments.
>
> #### GitHub Codespaces
>
> You can run this sample virtually using GitHub Codespaces without any extra setup.
>
> The button will open a web-based VS Code instance in your browser:
>
> 1. Open the template (this might take a few minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Running Locally using VS Code Dev Containers
>
> ⚠️ This option only works if your Docker Desktop has at least 16 GB of RAM allocated. If you have less, try the [GitHub Codespaces option](../..) or [set it up locally](../..).
>
> Another option is VS Code Dev Containers, which opens the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install it if you haven’t yet)
> 2. Open the project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

We use [Black](https://github.com/psf/black) as our Python code formatter to keep a consistent style throughout the project. Black is an opinionated formatter that automatically reformats Python code to fit its style.

#### Configuration

The Black configuration is set in our `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

You can install Black via Poetry (recommended) or pip:

##### Using Poetry

Black is installed automatically when setting up the development environment:
```bash
poetry install
```

##### Using pip

If you use pip, install Black directly:
```bash
pip install black
```

#### Using Black

##### With Poetry

1. Format all Python files in the project:
    ```bash
    poetry run black .
    ```

2. Format a specific file or folder:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. Format all Python files in the project:
    ```bash
    black .
    ```

2. Format a specific file or folder:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> We recommend configuring your editor to format code with Black automatically on save. Most modern editors support this via extensions or plugins.

## Running Co-op Translator

To run Co-op Translator using Poetry in your environment, follow these steps:

1. Go to the folder where you want to run translation tests or create a temporary folder for testing.

2. Run the following command. The `-l ko` with the language code you wish to translate into. The `-d` flag enables debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Make sure your Poetry environment is activated (`poetry shell`) before running the command.

## Maintainers

### Commit message and Merge strategy

To keep our commit history consistent and clear, we follow a specific commit message format **for the final commit message** when using the **Squash and Merge** strategy.

When a pull request (PR) is merged, all commits are squashed into one. The final commit message should follow the format below to keep the history clean and uniform.

#### Commit message format (for squash and merge)

We use this format for commit messages:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Defines the commit category. We use these types:
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

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvorni jezikovni različici velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.