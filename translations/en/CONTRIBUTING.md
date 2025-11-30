<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T09:37:25+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "en"
}
-->
# Contributing to Co-op Translator

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and mark the PR accordingly (e.g., status check, comment). Just follow the instructions provided by the bot. You only need to do this once across all repos using our CLA.

## Development environment setup

To set up the development environment for this project, we recommend using Poetry to manage dependencies. We use `pyproject.toml` to manage project dependencies, so you should use Poetry to install them.

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

Before submitting a PR, it’s important to test the translation functionality with real documentation:

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
   - Links and images work properly

This manual testing helps ensure your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` file.
2. Fill in the environment variables as instructed.

> [!TIP]
>
> ### Additional development environment options
>
> Besides running the project locally, you can also use GitHub Codespaces or VS Code Dev Containers as alternative development environments.
>
> #### GitHub Codespaces
>
> You can run these samples virtually using GitHub Codespaces with no extra setup required.
>
> The button will open a web-based VS Code instance in your browser:
>
> 1. Open the template (this may take a few minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Running Locally using VS Code Dev Containers
>
> ⚠️ This option only works if your Docker Desktop is allocated at least 16 GB of RAM. If you have less than 16 GB, try the [GitHub Codespaces option](../..) or [set it up locally](../..).
>
> Another option is VS Code Dev Containers, which opens the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install it if not already installed)
> 2. Open the project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

We use [Black](https://github.com/psf/black) as our Python code formatter to keep a consistent code style across the project. Black is an uncompromising formatter that automatically reformats Python code to follow the Black style.

#### Configuration

The Black configuration is specified in our `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

You can install Black using Poetry (recommended) or pip:

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
> We recommend configuring your editor to automatically format code with Black on save. Most modern editors support this via extensions or plugins.

## Running Co-op Translator

To run Co-op Translator using Poetry in your environment, follow these steps:

1. Navigate to the directory where you want to test translations or create a temporary folder for testing.

2. Run the following command. Replace `-l ko` with the language code you want to translate into. The `-d` flag enables debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Make sure your Poetry environment is activated (poetry shell) before running the command.

## Contribute a new language

We welcome contributions that add support for new languages. Before opening a PR, please complete the steps below to ensure a smooth review.

1. Add the language to the font mapping
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Add an entry with:
     - `code`: ISO-like language code (e.g., `vi`)
     - `name`: Human-friendly display name
     - `font`: A font included in `src/co_op_translator/fonts/` that supports the script
     - `rtl`: `true` if right-to-left, otherwise `false`

2. Include required font files (if needed)
   - If a new font is required, verify license compatibility for open source distribution
   - Add the font file to `src/co_op_translator/fonts/`

3. Local verification
   - Run translations on a small sample (Markdown, images, and notebooks as appropriate)
   - Verify the output renders correctly, including fonts and any RTL layout if applicable

4. Update documentation
   - Ensure the language appears in `getting_started/supported-languages.md`
   - No changes to `getting_started/README_languages_template.md` are needed; it is generated from the supported list

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

### Test the new language

You can test the new language by running the following command:

```bash
# Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## Maintainers

### Commit message and Merge strategy

To keep our project’s commit history consistent and clear, we follow a specific commit message format **for the final commit message** when using the **Squash and Merge** strategy.

When a pull request (PR) is merged, the individual commits are squashed into a single commit. The final commit message should follow the format below to maintain a clean and consistent history.

#### Commit message format (for squash and merge)

We use the following format for commit messages:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specifies the category of the commit. We use these types:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to config files, CI workflows, or the Dockerfile.
  - `Core`: For changes to the project’s core functionality or features, especially files in `src/co_op_translator/core`.

- **description**: A concise summary of the change.
- **PR number**: The pull request number associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on labels applied to the modified source code. As long as the correct label is applied, you usually don’t need to manually update the PR title. Just verify everything is correct and the prefix has been generated properly.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This ensures commit messages follow our format, even if individual commits don’t.

**Reasons**:

- A clean, linear project history.
- Consistent commit messages.
- Less noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains these commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

### Release process

This section describes the simplest way for maintainers to publish a new release of Co-op Translator.

#### 1. Bump the version in `pyproject.toml`

1. Decide the next version number (we follow semantic versioning: `MAJOR.MINOR.PATCH`).
2. Edit `pyproject.toml` and update the `version` field under `[tool.poetry]`.
3. Open a dedicated pull request that only changes the version (and any automatically updated lock/metadata files, if present).
4. After review, use **Squash and Merge** and ensure the final commit message follows the format described above.

#### 2. Create a GitHub Release

1. Go to the GitHub repository page and open **Releases** → **Draft a new release**.
2. Create a new tag (e.g., `v0.13.0`) from the `main` branch.
3. Set the release title to the same version (e.g., `v0.13.0`).
4. Click **Generate release notes** to auto-populate the changelog.
5. Optionally edit the text (e.g., to highlight newly supported languages or important changes).
6. Publish the release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->