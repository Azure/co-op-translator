<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T13:05:33+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pcm"
}
-->
# How to Contribute to Co-op Translator

Dis project dey welcome contributions and suggestions. Most contributions go require say you agree to one Contributor License Agreement (CLA) wey talk say you get right and you really dey give us permission to use your contribution. For details, check https://cla.opensource.microsoft.com.

When you submit pull request, one CLA bot go automatically check if you need provide CLA and e go put the correct status or comment for the PR. Just follow wetin the bot talk. You go only need do am once for all repos wey dey use our CLA.

## How to Set Up Development Environment

To set up development environment for dis project, we recommend say you use Poetry to manage dependencies. We dey use `pyproject.toml` to manage project dependencies, so to install dependencies, you suppose use Poetry.

### How to Create Virtual Environment

#### Using pip

```bash
python -m venv .venv
```


#### Using Poetry

```bash
poetry init
```


### How to Activate Virtual Environment

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


### How to Install Package and Required Packages

#### Using Poetry (from pyproject.toml)

```bash
poetry install
```


### Manual Testing

Before you submit PR, e important to test translation functionality with real documentation:

1. Create test directory for root directory:
    ```bash
    mkdir test_docs
    ```

2. Copy some markdown documentation and images wey you want translate enter the test directory. For example:
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

5. Check the translated files for `test_docs/translations` and `test_docs/translated_images` to confirm:
   - The translation quality
   - The metadata comments dey correct
   - The original markdown structure still dey
   - Links and images dey work well

Dis manual testing go help make sure say your changes dey work well for real-world situations.

### Environment Variables

1. Create `.env` file for root directory by copying the `.env.template` file wey dem provide.
2. Fill the environment variables as e take talk.

> [!TIP]
>
> ### Other Development Environment Options
>
> Besides running the project locally, you fit also use GitHub Codespaces or VS Code Dev Containers as alternative development environment setup.
>
> #### GitHub Codespaces
>
> You fit run dis samples virtually by using GitHub Codespaces and you no need do any extra settings or setup.
>
> The button go open web-based VS Code for your browser:
>
> 1. Open the template (e fit take small time):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Running Locally using VS Code Dev Containers
>
> ⚠️ Dis option go only work if your Docker Desktop get at least 16 GB RAM. If your RAM less than 16 GB, you fit try the [GitHub Codespaces option](../..) or [set am up locally](../..).
>
> Another option na VS Code Dev Containers, wey go open the project for your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install am if you never install)
> 2. Open the project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

### Code Style

We dey use [Black](https://github.com/psf/black) as our Python code formatter to keep code style consistent for the project. Black na strict code formatter wey automatically dey reformat Python code to follow Black code style.

#### Configuration

Black configuration dey for our `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```


#### How to Install Black

You fit install Black using Poetry (we recommend) or pip:

##### Using Poetry

Black go automatically install when you set up development environment:
```bash
poetry install
```


##### Using pip

If you dey use pip, you fit install Black directly:
```bash
pip install black
```


#### How to Use Black

##### With Poetry

1. Format all Python files for the project:
    ```bash
    poetry run black .
    ```

2. Format one specific file or directory:
    ```bash
    poetry run black path/to/file_or_directory
    ```


##### With pip

1. Format all Python files for the project:
    ```bash
    black .
    ```

2. Format one specific file or directory:
    ```bash
    black path/to/file_or_directory
    ```


> [!TIP]
> We recommend say you set your editor to automatically format code with Black when you save. Most modern editors support dis with extensions or plugins.

## How to Run Co-op Translator

To run Co-op Translator using Poetry for your environment, follow these steps:

1. Go the directory where you want do translation tests or create one temporary folder for testing.

2. Run this command. Change `-l ko` to the language code wey you want translate to. The `-d` flag mean debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```


> [!NOTE]
> Make sure say your Poetry environment dey activated (poetry shell) before you run the command.

## How to Contribute New Language

We dey welcome contributions wey add support for new languages. Before you open PR, please complete these steps to make review smooth.

1. Add the language to the font mapping
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Add entry with:
     - `code`: ISO-like language code (e.g., `vi`)
     - `name`: Human-friendly display name
     - `font`: Font wey dey `src/co_op_translator/fonts/` wey support the script
     - `rtl`: `true` if na right-to-left, otherwise `false`

2. Add required font files (if needed)
   - If new font dey needed, check license compatibility for open source distribution
   - Add the font file to `src/co_op_translator/fonts/`

3. Local verification
   - Run translations for small sample (Markdown, images, and notebooks as needed)
   - Check output to confirm e render well, including fonts and any RTL layout if e dey

4. Update documentation
   - Make sure the language dey for `getting_started/supported-languages.md`
   - No need change `getting_started/README_languages_template.md`; e dey generated from supported list

5. Open PR
   - Describe the language wey you add and any font/licensing info
   - Attach screenshots of rendered outputs if you fit

Example YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


### How to Test New Language

You fit test the new language by running this command:

```bash
# Make and start one virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install di development package
pip install -e .
# Run di translation
translate -l "new_lang"
```


## Maintainers

### Commit Message and Merge Strategy

To keep our project commit history consistent and clear, we dey follow one specific commit message format **for the final commit message** when we dey use **Squash and Merge** strategy.

When PR merge, the individual commits go squash into one commit. The final commit message suppose follow the format below to keep history clean and consistent.

#### Commit Message Format (for squash and merge)

We dey use this format for commit messages:

```bash
<type>: <description> (#<PR number>)
```


- **type**: This one specify the category of the commit. We get these types:
  - `Docs`: For documentation updates.
  - `Build`: For changes wey concern build system or dependencies, including config files, CI workflows, or Dockerfile updates.
  - `Core`: For changes to the project's core features or functionality, especially files inside `src/co_op_translator/core` directory.

- **description**: Short summary of the change.
- **PR number**: The pull request number wey relate to the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Right now, the **`Docs`**, **`Core`**, and **`Build`** prefixes dey automatically add to PR titles based on labels wey dem put for the modified source code. As long as the correct label dey, you no need manually update PR title. Just check say everything correct and the prefix don generate well.

#### Merge Strategy

We dey use **Squash and Merge** as our default strategy for pull requests. This strategy make sure say commit messages follow our format, even if individual commits no do so.

**Reasons**:

- Clean, linear project history.
- Consistent commit messages.
- Less noise from small commits (like "fix typo").

When you dey merge, make sure the final commit message follow the commit message format wey we talk about above.

**Example of Squash and Merge**

If PR get these commits:

- `fix typo`
- `update README`
- `adjust formatting`

Dem go squash am into:
`Docs: Improve documentation clarity and formatting (#65)`

### Release Process

Dis section dey explain the easiest way for maintainers to publish new release of Co-op Translator.

#### 1. Bump Version for `pyproject.toml`

1. Decide the next version number (we dey follow semantic versioning: `MAJOR.MINOR.PATCH`).
2. Edit `pyproject.toml` and update `version` field under `[tool.poetry]`.
3. Open one dedicated pull request wey only change the version (and any auto-updated lock/metadata files if e dey).
4. After review, use **Squash and Merge** and make sure the final commit message follow the format wey we talk about.

#### 2. Create GitHub Release

1. Go GitHub repo page and open **Releases** → **Draft a new release**.
2. Create new tag (for example, `v0.13.0`) from `main` branch.
3. Set release title to the same version (for example, `v0.13.0`).
4. Click **Generate release notes** to auto-fill changelog.
5. You fit edit the text if you want (for example, to highlight new supported languages or important changes).
6. Publish the release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some errors or wahala. Di original document wey dey im own language na di correct one. If na serious matter, e better make person wey sabi do professional human translation do am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->