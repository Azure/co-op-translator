<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a28303d122bd8d1c19e63b74a3cbc8ed",
  "translation_date": "2025-11-06T17:29:30+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pcm"
}
-->
# Contributin to Co-op Translator

Dis project dey welcome contributions and suggestions. Most contributions go need make you agree to one Contributor License Agreement (CLA) wey go show say you get di right to, and you really dey give us di rights to use wetin you contribute. For more details, visit https://cla.opensource.microsoft.com.

When you submit pull request, one CLA bot go automatically check if you need to provide CLA and e go mark di PR well (e.g., status check, comment). Just follow di instructions wey di bot go give you. You go only need to do am once for all repos wey dey use our CLA.

## How to Set Up Development Environment

To set up di development environment for dis project, we dey recommend make you use Poetry to manage dependencies. We dey use `pyproject.toml` to manage project dependencies, so to install dependencies, you go need use Poetry.

### Create Virtual Environment

#### If you dey use pip

```bash
python -m venv .venv
```

#### If you dey use Poetry

```bash
poetry init
```

### Activate di Virtual Environment

#### For both pip and Poetry

- For Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- For Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### If you dey use Poetry

```bash
poetry shell
```

### Install di Package and di Required Packages

#### If you dey use Poetry (from pyproject.toml)

```bash
poetry install
```

### Manual Testing

Before you submit PR, e good make you test di translation functionality with real documentation:

1. Create one test folder for di root directory:
    ```bash
    mkdir test_docs
    ```

2. Copy some markdown documentation and images wey you wan translate put for di test folder. For example:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Install di package for your local machine:
    ```bash
    pip install -e .
    ```

4. Run Co-op Translator for your test documents:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Check di translated files for `test_docs/translations` and `test_docs/translated_images` to confirm say:
   - Di translation quality dey okay
   - Di metadata comments dey correct
   - Di original markdown structure no change
   - Links and images dey work well

Dis manual testing go help make sure say wetin you change dey work well for real-life situations.

### Environment Variables

1. Create `.env` file for di root directory by copying di `.env.template` file wey dem provide.
1. Fill di environment variables as dem guide you.

> [!TIP]
>
> ### Other Development Environment Options
>
> Apart from running di project for your local machine, you fit use GitHub Codespaces or VS Code Dev Containers as another way to set up di development environment.
>
> #### GitHub Codespaces
>
> You fit run dis samples online by using GitHub Codespaces and you no need any extra settings or setup.
>
> Di button go open one web-based VS Code for your browser:
>
> 1. Open di template (e fit take some minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Run Locally with VS Code Dev Containers
>
> ⚠️ Dis option go only work if your Docker Desktop get at least 16 GB RAM. If you no get up to 16 GB RAM, you fit try di [GitHub Codespaces option](../..) or [set am up locally](../..).
>
> Another option na VS Code Dev Containers, wey go open di project for your local VS Code using di [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install am if you never install am before)
> 2. Open di project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

We dey use [Black](https://github.com/psf/black) as our Python code formatter to make sure say di code style for di project dey consistent. Black na one kind code formatter wey no dey compromise and e dey automatically arrange Python code to match di Black code style.

#### Configuration

Di Black configuration dey for our `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### How to Install Black

You fit install Black by using Poetry (we recommend am) or pip:

##### If you dey use Poetry

Black go automatically install when you set up di development environment:
```bash
poetry install
```

##### If you dey use pip

If na pip you dey use, you fit install Black directly:
```bash
pip install black
```

#### How to Use Black

##### With Poetry

1. Format all di Python files for di project:
    ```bash
    poetry run black .
    ```

2. Format one specific file or folder:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. Format all di Python files for di project:
    ```bash
    black .
    ```

2. Format one specific file or folder:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> We dey recommend make you set your editor to dey automatically format code with Black anytime you save. Most modern editors get support for dis through extensions or plugins.

## How to Run Co-op Translator

To run Co-op Translator with Poetry for your environment, follow dis steps:

1. Go to di folder wey you wan use do translation tests or create one temporary folder for testing.

2. Run di command below. Replace `-l ko` with di language code wey you wan translate into. Di `-d` flag mean debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Make sure say your Poetry environment don activate (poetry shell) before you run di command.

## How to Add New Language

We dey welcome contributions wey go add support for new languages. Before you open PR, abeg complete di steps below to make di review process smooth.

1. Add di language to di font mapping
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Add one entry wey get:
     - `code`: ISO-like language code (e.g., `vi`)
     - `name`: Di name wey people go fit understand
     - `font`: One font wey dey for `src/co_op_translator/fonts/` wey fit support di script
     - `rtl`: `true` if na right-to-left, if no be, put `false`

2. Add di font files wey dem need (if e dey necessary)
   - If dem need new font, check say di license fit allow open source distribution
   - Add di font file to `src/co_op_translator/fonts/`

3. Test am for your local machine
   - Run translations for small sample (Markdown, images, and notebooks if e dey necessary)
   - Check say di output dey render well, including fonts and any RTL layout if e apply

4. Update documentation
   - Make sure say di language dey show for `getting_started/supported-languages.md`
   - No need to change `getting_started/README_languages_template.md`; e dey generate from di supported list

5. Open PR
   - Talk about di language wey you add and any font/licensing things wey dem suppose know
   - Add screenshots of di rendered outputs if you fit

Example YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainers

### Commit Message and Merge Strategy

To make sure say our project commit history dey consistent and clear, we dey follow one kind commit message format **for di final commit message** when we dey use di **Squash and Merge** strategy.

When we merge pull request (PR), di individual commits go join together as one commit. Di final commit message suppose follow di format below to keep di history clean and consistent.

#### Commit Message Format (for Squash and Merge)

We dey use dis format for commit messages:

```bash
<type>: <description> (#<PR number>)
```

- **type**: E dey show di category of di commit. We dey use di types below:
  - `Docs`: For updates to documentation.
  - `Build`: For changes wey concern di build system or dependencies, including updates to configuration files, CI workflows, or di Dockerfile.
  - `Core`: For changes to di main functionality or features of di project, especially di ones wey dey involve files for `src/co_op_translator/core` directory.

- **description**: One short summary of di change.
- **PR number**: Di number of di pull request wey join di commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> For now, di **`Docs`**, **`Core`**, and **`Build`** prefixes dey automatically add to PR titles based on di labels wey dem put for di modified source code. As long as di correct label dey, you no need to manually change di PR title. Just make sure say everything dey correct and di prefix dey okay.

#### Merge Strategy

We dey use **Squash and Merge** as di default strategy for pull requests. Dis strategy dey make sure say commit messages dey follow our format, even if di individual commits no follow.

**Why we dey use am**:

- E dey make di project history clean and straight.
- E dey make commit messages consistent.
- E dey reduce noise from small small commits (e.g., "fix typo").

When you wan merge, make sure say di final commit message follow di commit message format wey we describe above.

**Example of Squash and Merge**
If one PR get di commits below:

- `fix typo`
- `update README`
- `adjust formatting`

Dem go join as one:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.