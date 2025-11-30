<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c49d37c6ca9589f4f711c57b0876b96",
  "translation_date": "2025-11-23T02:17:41+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ml"
}
-->
# Co-op Translator-ലേക്ക് സംഭാവന നൽകുന്നത്

ഈ പ്രോജക്റ്റ് സംഭാവനകളും നിർദ്ദേശങ്ങളും സ്വാഗതം ചെയ്യുന്നു. മിക്ക സംഭാവനകൾക്കും നിങ്ങൾക്ക് ഒരു Contributor License Agreement (CLA) അംഗീകരിക്കേണ്ടതുണ്ട്, ഇത് നിങ്ങൾക്ക് നിങ്ങളുടെ സംഭാവന ഉപയോഗിക്കാൻ അവകാശം നൽകുകയും അത് ചെയ്യുകയും ചെയ്യുന്നു എന്ന് പ്രഖ്യാപിക്കുന്നു. കൂടുതൽ വിവരങ്ങൾക്ക്, https://cla.opensource.microsoft.com സന്ദർശിക്കുക.

നിങ്ങൾ ഒരു pull request സമർപ്പിക്കുമ്പോൾ, CLA bot സ്വയം നിർണയിക്കും നിങ്ങൾ CLA നൽകേണ്ടതുണ്ടോ എന്ന്, PR-നെ അനുയോജ്യമായി അലങ്കരിക്കുകയും (ഉദാ, status check, comment) ചെയ്യും. bot നൽകുന്ന നിർദ്ദേശങ്ങൾ പാലിക്കുക. ഞങ്ങളുടെ CLA ഉപയോഗിക്കുന്ന എല്ലാ repos-ലും ഇത് നിങ്ങൾക്ക് ഒരിക്കൽ മാത്രം ചെയ്യേണ്ടതുണ്ട്.

## ഡെവലപ്മെന്റ് എൻവയോൺമെന്റ് സജ്ജമാക്കൽ

ഈ പ്രോജക്റ്റിന്റെ ഡെവലപ്മെന്റ് എൻവയോൺമെന്റ് സജ്ജമാക്കാൻ, dependency management-നായി Poetry ഉപയോഗിക്കാൻ ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു. `pyproject.toml` ഉപയോഗിച്ച് dependency-കൾ മാനേജുചെയ്യുന്നു, അതിനാൽ dependency-കൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ Poetry ഉപയോഗിക്കണം.

### ഒരു virtual environment സൃഷ്ടിക്കുക

#### pip ഉപയോഗിച്ച്

```bash
python -m venv .venv
```

#### Poetry ഉപയോഗിച്ച്

```bash
poetry init
```

### virtual environment സജീവമാക്കുക

#### pip-നും Poetry-ക്കും

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry ഉപയോഗിച്ച്

```bash
poetry shell
```

### പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക

#### Poetry ഉപയോഗിച്ച് (pyproject.toml-ൽ നിന്ന്)

```bash
poetry install
```

### മാനുവൽ ടെസ്റ്റിംഗ്

PR സമർപ്പിക്കുന്നതിന് മുമ്പ്, യഥാർത്ഥ ഡോക്യുമെന്റേഷൻ ഉപയോഗിച്ച് translation functionality ടെസ്റ്റ് ചെയ്യുന്നത് പ്രധാനമാണ്:

1. root directory-ൽ ഒരു test directory സൃഷ്ടിക്കുക:
    ```bash
    mkdir test_docs
    ```

2. translate ചെയ്യാൻ ആഗ്രഹിക്കുന്ന ചില markdown ഡോക്യുമെന്റേഷനും ചിത്രങ്ങളും test directory-ലേക്ക് കോപ്പി ചെയ്യുക. ഉദാഹരണത്തിന്:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. പാക്കേജ് ലോക്കലായി ഇൻസ്റ്റാൾ ചെയ്യുക:
    ```bash
    pip install -e .
    ```

4. നിങ്ങളുടെ test documents-ൽ Co-op Translator പ്രവർത്തിപ്പിക്കുക:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations`-ലും `test_docs/translated_images`-ലും translated ഫയലുകൾ പരിശോധിക്കുക:
   - translation ഗുണനിലവാരം
   - metadata comments ശരിയാണോ
   - യഥാർത്ഥ markdown ഘടന സംരക്ഷിക്കപ്പെട്ടിട്ടുണ്ടോ
   - links-ഉം images-ഉം ശരിയായി പ്രവർത്തിക്കുന്നുണ്ടോ

ഈ മാനുവൽ ടെസ്റ്റിംഗ് നിങ്ങളുടെ മാറ്റങ്ങൾ യഥാർത്ഥ ലോക സാഹചര്യങ്ങളിൽ നല്ലതായും പ്രവർത്തനക്ഷമവുമാണെന്ന് ഉറപ്പാക്കുന്നു.

### എൻവയോൺമെന്റ് വേരിയബിളുകൾ

1. `.env.template` ഫയൽ കോപ്പി ചെയ്ത് root directory-ൽ ഒരു `.env` ഫയൽ സൃഷ്ടിക്കുക.
1. environment variables നിർദ്ദേശിച്ച പ്രകാരം പൂരിപ്പിക്കുക.

> [!TIP]
>
> ### ഡെവലപ്മെന്റ് എൻവയോൺമെന്റിന്റെ അധിക ഓപ്ഷനുകൾ
>
> പ്രോജക്റ്റ് ലോക്കലായി പ്രവർത്തിപ്പിക്കുന്നതിനു പുറമേ, GitHub Codespaces അല്ലെങ്കിൽ VS Code Dev Containers ഉപയോഗിച്ച് ഒരു പാരമ്പര്യ ഡെവലപ്മെന്റ് എൻവയോൺമെന്റ് സജ്ജമാക്കാം.
>
> #### GitHub Codespaces
>
> GitHub Codespaces ഉപയോഗിച്ച് ഈ സാമ്പിളുകൾ വെർച്വലായി പ്രവർത്തിപ്പിക്കാം, അധിക ക്രമീകരണങ്ങൾ അല്ലെങ്കിൽ സജ്ജീകരണങ്ങൾ ആവശ്യമില്ല.
>
> ബട്ടൺ നിങ്ങളുടെ ബ്രൗസറിലെ web-based VS Code instance തുറക്കും:
>
> 1. ടെംപ്ലേറ്റ് തുറക്കുക (ഇത് കുറച്ച് മിനിറ്റുകൾ എടുക്കാം):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers ഉപയോഗിച്ച് ലോക്കലായി പ്രവർത്തിപ്പിക്കൽ
>
> ⚠️ ഈ ഓപ്ഷൻ നിങ്ങളുടെ Docker Desktop-ൽ കുറഞ്ഞത് 16 GB RAM അനുവദിച്ചിട്ടുണ്ടെങ്കിൽ മാത്രമേ പ്രവർത്തിക്കൂ. നിങ്ങൾക്ക് 16 GB RAM-ൽ കുറവാണെങ്കിൽ, [GitHub Codespaces ഓപ്ഷൻ](../..) പരീക്ഷിക്കാം അല്ലെങ്കിൽ [ലോക്കലായി സജ്ജമാക്കുക](../..).
>
> ബന്ധപ്പെട്ട ഓപ്ഷൻ VS Code Dev Containers ആണ്, ഇത് [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ഉപയോഗിച്ച് നിങ്ങളുടെ ലോക്കൽ VS Code-ൽ പ്രോജക്റ്റ് തുറക്കും:
>
> 1. Docker Desktop ആരംഭിക്കുക (ഇത് ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ ഇൻസ്റ്റാൾ ചെയ്യുക)
> 2. പ്രോജക്റ്റ് തുറക്കുക:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### കോഡ് സ്റ്റൈൽ

Python code formatter ആയി [Black](https://github.com/psf/black) ഉപയോഗിക്കുന്നു, ഇത് പ്രോജക്റ്റ് മുഴുവൻ consistent code style നിലനിർത്താൻ സഹായിക്കുന്നു. Black Python code reformats ചെയ്യുന്നതിൽ അനങ്ങാത്ത formatter ആണ്.

#### Configuration

Black configuration ഞങ്ങളുടെ `pyproject.toml`-ൽ വ്യക്തമാക്കിയിരിക്കുന്നു:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ഇൻസ്റ്റാൾ ചെയ്യുക

Poetry (ശുപാർശ ചെയ്യുന്നു) അല്ലെങ്കിൽ pip ഉപയോഗിച്ച് Black ഇൻസ്റ്റാൾ ചെയ്യാം:

##### Poetry ഉപയോഗിച്ച്

Black development environment സജ്ജമാക്കുമ്പോൾ സ്വയം ഇൻസ്റ്റാൾ ചെയ്യപ്പെടുന്നു:
```bash
poetry install
```

##### pip ഉപയോഗിച്ച്

pip ഉപയോഗിക്കുന്നവർക്ക് Black നേരിട്ട് ഇൻസ്റ്റാൾ ചെയ്യാം:
```bash
pip install black
```

#### Black ഉപയോഗിച്ച്

##### Poetry ഉപയോഗിച്ച്

1. പ്രോജക്റ്റിലെ എല്ലാ Python ഫയലുകളും format ചെയ്യുക:
    ```bash
    poetry run black .
    ```

2. ഒരു പ്രത്യേക ഫയൽ അല്ലെങ്കിൽ directory format ചെയ്യുക:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip ഉപയോഗിച്ച്

1. പ്രോജക്റ്റിലെ എല്ലാ Python ഫയലുകളും format ചെയ്യുക:
    ```bash
    black .
    ```

2. ഒരു പ്രത്യേക ഫയൽ അല്ലെങ്കിൽ directory format ചെയ്യുക:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> നിങ്ങളുടെ editor Black ഉപയോഗിച്ച് code save ചെയ്യുമ്പോൾ സ്വയം format ചെയ്യാൻ സജ്ജമാക്കാൻ ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു. മിക്ക modern editors-നും ഇത് extensions അല്ലെങ്കിൽ plugins വഴി പിന്തുണയുണ്ട്.

## Co-op Translator പ്രവർത്തിപ്പിക്കൽ

Poetry ഉപയോഗിച്ച് Co-op Translator പ്രവർത്തിപ്പിക്കാൻ, ഈ ഘട്ടങ്ങൾ പിന്തുടരുക:

1. നിങ്ങൾ translation tests നടത്താൻ ആഗ്രഹിക്കുന്ന directory-യിലേക്ക് പോകുക അല്ലെങ്കിൽ പരീക്ഷണത്തിനായി ഒരു താൽക്കാലിക ഫോൾഡർ സൃഷ്ടിക്കുക.

2. താഴെ കാണുന്ന command പ്രവർത്തിപ്പിക്കുക. `-l ko`-നെ നിങ്ങൾ translate ചെയ്യാൻ ആഗ്രഹിക്കുന്ന ഭാഷാ കോഡിൽ മാറ്റുക. `-d` flag debug mode സൂചിപ്പിക്കുന്നു.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> command പ്രവർത്തിപ്പിക്കുന്നതിന് മുമ്പ് നിങ്ങളുടെ Poetry environment സജീവമാക്കിയിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക (poetry shell).

## പുതിയ ഭാഷ സംഭാവന ചെയ്യുക

പുതിയ ഭാഷകൾക്ക് പിന്തുണ നൽകുന്ന സംഭാവനകൾ ഞങ്ങൾ സ്വാഗതം ചെയ്യുന്നു. PR തുറക്കുന്നതിന് മുമ്പ്, smoother review ഉറപ്പാക്കാൻ താഴെ കാണുന്ന ഘട്ടങ്ങൾ പൂർത്തിയാക്കുക.

1. ഭാഷ font mapping-ലേക്ക് ചേർക്കുക
   - `src/co_op_translator/fonts/font_language_mappings.yml` എഡിറ്റ് ചെയ്യുക
   - താഴെ കാണുന്ന entry ചേർക്കുക:
     - `code`: ISO-like ഭാഷാ കോഡ് (ഉദാ, `vi`)
     - `name`: Human-friendly display name
     - `font`: `src/co_op_translator/fonts/`-ൽ ഉൾപ്പെടുത്തിയിരിക്കുന്ന, script-നെ പിന്തുണയ്ക്കുന്ന font
     - `rtl`: right-to-left ആണെങ്കിൽ `true`, അല്ലെങ്കിൽ `false`

2. ആവശ്യമായ font files ഉൾപ്പെടുത്തുക (ആവശ്യമെങ്കിൽ)
   - പുതിയ font ആവശ്യമായാൽ, open source distribution-നുള്ള license compatibility സ്ഥിരീകരിക്കുക
   - font file `src/co_op_translator/fonts/`-ലേക്ക് ചേർക്കുക

3. ലോക്കൽ verification
   - ചെറിയ sample-ലേക്ക് translations പ്രവർത്തിപ്പിക്കുക (Markdown, images, notebooks എന്നിവ ആവശ്യമായ പോലെ)
   - output ശരിയായി render ചെയ്യുന്നതും fonts-ഉം RTL layout-ഉം ശരിയാണെന്ന് ഉറപ്പാക്കുക

4. ഡോക്യുമെന്റേഷൻ അപ്ഡേറ്റ് ചെയ്യുക
   - ഭാഷ `getting_started/supported-languages.md`-ൽ പ്രത്യക്ഷപ്പെടുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക
   - `getting_started/README_languages_template.md`-ൽ മാറ്റങ്ങൾ ആവശ്യമില്ല; ഇത് supported list-ൽ നിന്ന് സൃഷ്ടിക്കപ്പെടുന്നു

5. PR തുറക്കുക
   - ചേർത്ത ഭാഷയും font/licensing പരിഗണനകളും വിശദീകരിക്കുക
   - render ചെയ്ത output-ന്റെ screenshots (ശക്തമായാൽ) ചേർക്കുക

Example YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### പുതിയ ഭാഷ ടെസ്റ്റ് ചെയ്യുക

പുതിയ ഭാഷ ടെസ്റ്റ് ചെയ്യാൻ താഴെ കാണുന്ന command പ്രവർത്തിപ്പിക്കുക:

```bash
# ഒരു വെർച്വൽ പരിസ്ഥിതി സൃഷ്ടിച്ച് സജീവമാക്കുക
python -m venv .venv
# വിൻഡോസ്
.venv\Scripts\activate
# മാക്‌ഒഎസ്/ലിനക്സ്
source .venv/bin/activate
# ഡെവലപ്‌മെന്റ് പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക
pip install -e .
# വിവർത്തനം പ്രവർത്തിപ്പിക്കുക
translate -l "new_lang"
```

## Maintainers

### Commit message-യും Merge strategy-യും

ഞങ്ങളുടെ പ്രോജക്റ്റിന്റെ commit history consistent-ഉം വ്യക്തമായും ഉറപ്പാക്കാൻ, **Squash and Merge** strategy ഉപയോഗിച്ച് **final commit message**-ന്റെ പ്രത്യേക format പിന്തുടരുന്നു.

Pull request (PR) merge ചെയ്യുമ്പോൾ, individual commits ഒരു single commit-ലേക്ക് squash ചെയ്യപ്പെടും. Final commit message താഴെ കാണുന്ന format പിന്തുടരണം, history clean-ഉം consistent-ഉം നിലനിർത്താൻ.

#### Commit message format (squash and merge-ക്കായി)

Commit message-കൾക്കായി ഞങ്ങൾ താഴെ കാണുന്ന format ഉപയോഗിക്കുന്നു:

```bash
<type>: <description> (#<PR നമ്പർ>)
```

- **type**: commit-ന്റെ category വ്യക്തമാക്കുന്നു. ഞങ്ങൾ താഴെ കാണുന്ന types ഉപയോഗിക്കുന്നു:
  - `Docs`: ഡോക്യുമെന്റേഷൻ അപ്ഡേറ്റുകൾക്കായി.
  - `Build`: build system അല്ലെങ്കിൽ dependency-കളുമായി ബന്ധപ്പെട്ട മാറ്റങ്ങൾക്കായി, configuration files, CI workflows, Dockerfile എന്നിവ ഉൾപ്പെടെ.
  - `Core`: പ്രോജക്റ്റിന്റെ core functionality അല്ലെങ്കിൽ features-ൽ മാറ്റങ്ങൾക്കായി, പ്രത്യേകിച്ച് `src/co_op_translator/core` directory-യിലെ ഫയലുകൾ.

- **description**: മാറ്റത്തിന്റെ സംക്ഷിപ്തമായ സംഗ്രഹം.
- **PR number**: commit-നുമായി ബന്ധപ്പെട്ട pull request-ന്റെ നമ്പർ.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> നിലവിൽ, **`Docs`**, **`Core`**, **`Build`** prefixes PR titles-ൽ സ്വയം ചേർക്കപ്പെടുന്നു, source code-ൽ മാറ്റങ്ങൾക്കുള്ള labels അടിസ്ഥാനമാക്കി. ശരിയായ label പ്രയോഗിച്ചാൽ, PR title manually update ചെയ്യേണ്ടതില്ല. നിങ്ങൾക്ക് എല്ലാം ശരിയാണെന്ന് ഉറപ്പാക്കുകയും prefix ശരിയായി സൃഷ്ടിക്കപ്പെട്ടിട്ടുണ്ടെന്ന് പരിശോധിക്കുകയും ചെയ്യേണ്ടതുണ്ട്.

#### Merge strategy

Pull requests-ക്കായി **Squash and Merge** ഞങ്ങളുടെ default strategy ആയി ഉപയോഗിക്കുന്നു. ഈ strategy individual commits ശരിയല്ലെങ്കിൽ പോലും commit messages format പിന്തുടരുന്നു.

**കാരണങ്ങൾ**:

- ഒരു clean, linear project history.
- Commit messages-ൽ consistency.
- ചെറിയ commits-ൽ നിന്ന് (ഉദാ, "fix typo") ശബ്ദം കുറയ്ക്കുന്നു.

Merge ചെയ്യുമ്പോൾ, final commit message commit message format-നനുസരിച്ച് ഉറപ്പാക്കുക.

**Squash and Merge ഉദാഹരണം**
ഒരു PR താഴെ കാണുന്ന commits ഉൾക്കൊള്ളുന്നുവെങ്കിൽ:

- `fix typo`
- `update README`
- `adjust formatting`

അവയെ squash ചെയ്ത്:
`Docs: Improve documentation clarity and formatting (#65)`

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:  
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള മൂല രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->