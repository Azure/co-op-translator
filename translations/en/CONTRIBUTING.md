<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:05:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "en"
}
-->
# Contributing to Co-op Translator

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) stating that you have the rights to, and actually do, grant us permission to use your contribution. For more details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically check if you need to sign a CLA and will update the PR accordingly (e.g., status check, comment). Just follow the instructions provided by the bot. You only need to do this once for all repositories using our CLA.

## Development environment setup

To set up the development environment for this project, we recommend using Poetry to manage dependencies. We use `pyproject.toml` for dependency management, so you should use Poetry to install dependencies.

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

Before submitting a PR, it's important to test the translation functionality with real documentation:

1. Create a test directory in the root directory:
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

1. Create an `.env` file in the root directory by copying the provided `.env.template` file.
1. Fill in the environment variables as guided.

> [!TIP]
>
> ### Additional development environment options
>
> Besides running the project locally, you can also use GitHub Codespaces or VS Code Dev Containers as alternative development environments.
>
> #### GitHub Codespaces
>
> You can run these samples virtually using GitHub Codespaces without any extra setup.
>
> The button below will open a web-based VS Code instance in your browser:
>
> 1. Open the template (this may take several minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Running Locally using VS Code Dev Containers
>
> ⚠️ This option only works if your Docker Desktop is allocated at least 16 GB of RAM. If you have less than 16 GB of RAM, try the [GitHub Codespaces option](../..) or [set it up locally](../..).
>
> Another option is VS Code Dev Containers, which opens the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install it if not already installed)
> 2. Open the project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

We use [Black](https://github.com/psf/black) as our Python code formatter to keep code style consistent across the project. Black is a strict code formatter that automatically reformats Python code to match its style.

#### Configuration

The Black configuration is set in our `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

You can install Black using either Poetry (recommended) or pip:

##### Using Poetry

Black is installed automatically when you set up the development environment:
```bash
poetry install
```

##### Using pip

If you use pip, you can install Black directly:
```bash
pip install black
```

#### Using Black

##### With Poetry

1. Format all Python files in the project:
    ```bash
    poetry run black .
    ```

2. Format a specific file or directory:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. Format all Python files in the project:
    ```bash
    black .
    ```

2. Format a specific file or directory:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> We recommend setting up your editor to automatically format code with Black on save. Most modern editors support this through extensions or plugins.

## Running Co-op Translator

To run Co-op Translator using Poetry in your environment, follow these steps:

1. Go to the directory where you want to run translation tests or create a temporary folder for testing.

2. Run the following command. Replace `-l ko` with the language code you want to translate into. The `-d` flag enables debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Make sure your Poetry environment is activated (poetry shell) before running the command.

## Contribute a new language

We welcome contributions that add support for new languages. Before opening a PR, please follow the steps below to help us review your changes smoothly.

1. Add the language to the font mapping
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Add an entry with:
     - `code`: ISO-like language code (e.g., `vi`)
     - `name`: Human-friendly display name
     - `font`: A font included in `src/co_op_translator/fonts/` that supports the script
     - `rtl`: `true` if right-to-left, otherwise `false`

2. Include required font files (if needed)
   - If a new font is needed, check that its license allows open source distribution
   - Add the font file to `src/co_op_translator/fonts/`

3. Local verification
   - Run translations for a small sample (Markdown, images, and notebooks as needed)
   - Check that the output renders correctly, including fonts and any RTL layout if needed

4. Update documentation
   - Make sure the language appears in `getting_started/supported-languages.md`
   - No changes to `README_languages_template.md` are needed; it is generated from the supported list

5. Open a PR
   - Describe the language added and any font/licensing considerations
   - Attach screenshots of rendered outputs if possible

Example YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainers

### Commit message and Merge strategy

To keep our project's commit history consistent and clear, we use a specific commit message format **for the final commit message** when using the **Squash and Merge** strategy.

When a pull request (PR) is merged, the individual commits are squashed into a single commit. The final commit message should follow the format below to keep the history clean and consistent.

#### Commit message format (for squash and merge)

We use the following format for commit messages:

```bash
<type>: <description> (#<PR number>)
```

- **type**: The category of the commit. We use these types:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For changes to the project's core functionality or features, especially those in the `src/co_op_translator/core` directory.

- **description**: A brief summary of the change.
- **PR number**: The number of the pull request for the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> The **`Docs`**, **`Core`**, and **`Build`** prefixes are currently added automatically to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you usually don't need to manually update the PR title. Just check that everything is correct and the prefix is generated properly.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This ensures commit messages follow our format, even if individual commits do not.

**Reasons**:

- A clean, linear project history.
- Consistent commit messages.
- Less noise from minor commits (e.g., "fix typo").

When merging, make sure the final commit message follows the format described above.

**Example of Squash and Merge**
If a PR contains these commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.