<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:40:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tl"
}
-->
# Contributing to Co-op Translator

Tinatanggap ng proyektong ito ang mga kontribusyon at suhestiyon. Karamihan sa mga kontribusyon ay nangangailangan na pumayag ka sa isang Contributor License Agreement (CLA) na nagsasaad na may karapatan ka, at talagang binibigyan mo kami ng pahintulot na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang https://cla.opensource.microsoft.com.

Kapag nagsumite ka ng pull request, awtomatikong malalaman ng CLA bot kung kailangan mong magbigay ng CLA at lalagyan ng angkop na dekorasyon ang PR (hal., status check, komento). Sundin lamang ang mga tagubiling ibibigay ng bot. Gagawin mo lang ito isang beses para sa lahat ng repos na gumagamit ng aming CLA.

## Development environment setup

Para ma-setup ang development environment para sa proyektong ito, inirerekomenda naming gamitin ang Poetry para sa pamamahala ng mga dependencies. Ginagamit namin ang `pyproject.toml` para i-manage ang mga project dependencies, kaya para mag-install ng dependencies, dapat gamitin ang Poetry.

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

Bago magsumite ng PR, mahalagang subukan ang translation functionality gamit ang totoong dokumentasyon:

1. Gumawa ng test directory sa root directory:
    ```bash
    mkdir test_docs
    ```

2. Kopyahin ang ilang markdown documentation at mga larawan na gusto mong isalin sa test directory. Halimbawa:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. I-install ang package nang lokal:
    ```bash
    pip install -e .
    ```

4. Patakbuhin ang Co-op Translator sa iyong test documents:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Tingnan ang mga naisaling files sa `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` file.
1. Punan ang mga environment variables ayon sa gabay.

> [!TIP]
>
> ### Karagdagang mga opsyon para sa development environment
>
> Bukod sa pagpapatakbo ng proyekto nang lokal, maaari mo ring gamitin ang GitHub Codespaces o VS Code Dev Containers bilang alternatibong setup ng development environment.
>
> #### GitHub Codespaces
>
> Maaari mong patakbuhin ang mga sample na ito virtually gamit ang GitHub Codespaces at walang karagdagang settings o setup na kinakailangan.
>
> Ang button ay magbubukas ng web-based na VS Code instance sa iyong browser:
>
> 1. Buksan ang template (maaari itong tumagal ng ilang minuto):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Pagpapatakbo nang Lokal gamit ang VS Code Dev Containers
>
> ⚠️ Gumagana lang ang opsyong ito kung ang Docker Desktop mo ay naka-allocate ng hindi bababa sa 16 GB ng RAM. Kung mas mababa sa 16 GB ng RAM, maaari mong subukan ang [GitHub Codespaces option](../..) o [i-setup ito nang lokal](../..).
>
> Isang kaugnay na opsyon ay ang VS Code Dev Containers, na magbubukas ng proyekto sa iyong lokal na VS Code gamit ang [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Simulan ang Docker Desktop (i-install kung hindi pa naka-install)
> 2. Buksan ang proyekto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

Gumagamit kami ng [Black](https://github.com/psf/black) bilang aming Python code formatter upang mapanatili ang pare-parehong estilo ng code sa buong proyekto. Ang Black ay isang mahigpit na code formatter na awtomatikong nire-reformat ang Python code upang sumunod sa Black code style.

#### Configuration

Ang configuration ng Black ay nakasaad sa aming `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

Maaari mong i-install ang Black gamit ang Poetry (inirerekomenda) o pip:

##### Using Poetry

Awtomatikong na-i-install ang Black kapag na-setup mo ang development environment:
```bash
poetry install
```

##### Using pip

Kung gumagamit ka ng pip, maaari mong direktang i-install ang Black:
```bash
pip install black
```

#### Using Black

##### With Poetry

1. I-format lahat ng Python files sa proyekto:
    ```bash
    poetry run black .
    ```

2. I-format ang isang partikular na file o directory:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. I-format lahat ng Python files sa proyekto:
    ```bash
    black .
    ```

2. I-format ang isang partikular na file o directory:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Inirerekomenda naming i-setup ang iyong editor upang awtomatikong i-format ang code gamit ang Black tuwing nagsa-save. Karamihan sa mga modernong editor ay sumusuporta rito sa pamamagitan ng mga extension o plugin.

## Running Co-op Translator

Para patakbuhin ang Co-op Translator gamit ang Poetry sa iyong environment, sundin ang mga hakbang na ito:

1. Pumunta sa directory kung saan gusto mong magsagawa ng translation tests o gumawa ng pansamantalang folder para sa testing.

2. Patakbuhin ang sumusunod na command. Ang flag na `-l ko` with the language code you wish to translate into. The `-d` ay nagpapahiwatig ng debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Siguraduhing naka-activate ang iyong Poetry environment (poetry shell) bago patakbuhin ang command.

## Maintainers

### Commit message and Merge strategy

Para masiguro ang pagkakapare-pareho at kalinawan sa kasaysayan ng commit ng aming proyekto, sumusunod kami sa isang partikular na format ng commit message **para sa huling commit message** kapag gumagamit ng **Squash and Merge** strategy.

Kapag na-merge ang isang pull request (PR), ang mga indibidwal na commit ay pagsasamahin sa isang commit lang. Ang huling commit message ay dapat sumunod sa format sa ibaba upang mapanatili ang malinis at pare-parehong kasaysayan.

#### Commit message format (for squash and merge)

Ginagamit namin ang sumusunod na format para sa mga commit message:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Tinukoy ang kategorya ng commit. Ginagamit namin ang mga sumusunod na uri:
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

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.