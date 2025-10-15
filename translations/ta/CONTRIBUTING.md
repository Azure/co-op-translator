<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T04:38:20+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ta"
}
-->
# Co-op Translator-க்கு பங்களிப்பு செய்வது

இந்த திட்டம் பங்களிப்புகள் மற்றும் பரிந்துரைகளை வரவேற்கிறது. பெரும்பாலான பங்களிப்புகளுக்கு, நீங்கள் Contributor License Agreement (CLA) ஒன்றில் ஒப்புதல் அளிக்க வேண்டும். இதில், உங்கள் பங்களிப்பை பயன்படுத்துவதற்கான உரிமையை நமக்கு வழங்குகிறீர்கள் என்று உறுதி செய்ய வேண்டும். மேலும் விவரங்களுக்கு https://cla.opensource.microsoft.com-ஐ பார்வையிடவும்.

நீங்கள் pull request சமர்ப்பிக்கும்போது, CLA bot தானாகவே உங்களுக்கு CLA வழங்க வேண்டியதா என்பதை கண்டறிந்து, PR-ஐ சரியான முறையில் அலங்கரிக்கும் (உதாரணமாக, status check, comment). Bot வழங்கும் வழிகாட்டுதல்களை பின்பற்றுங்கள். எங்கள் CLA-ஐ பயன்படுத்தும் அனைத்து repos-களிலும் இதை ஒருமுறை மட்டும் செய்ய வேண்டும்.

## Development environment அமைத்தல்

இந்த திட்டத்திற்கு development environment அமைக்க, dependencies-ஐ நிர்வகிக்க Poetry-ஐ பயன்படுத்த பரிந்துரைக்கிறோம். Project dependencies-ஐ நிர்வகிக்க `pyproject.toml`-ஐ பயன்படுத்துகிறோம், எனவே dependencies-ஐ நிறுவ Poetry-ஐ பயன்படுத்த வேண்டும்.

### ஒரு virtual environment உருவாக்குதல்

#### pip பயன்படுத்தி

```bash
python -m venv .venv
```

#### Poetry பயன்படுத்தி

```bash
poetry init
```

### virtual environment-ஐ செயல்படுத்துதல்

#### pip மற்றும் Poetry இரண்டிற்கும்

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry பயன்படுத்தி

```bash
poetry shell
```

### Package மற்றும் தேவையான Packages-ஐ நிறுவுதல்

#### Poetry (pyproject.toml-இல் இருந்து) பயன்படுத்தி

```bash
poetry install
```

### கைமுறையாக சோதனை செய்தல்

PR சமர்ப்பிப்பதற்கு முன், translation செயல்பாடுகளை உண்மையான documentation-இல் சோதனை செய்வது முக்கியம்:

1. root directory-யில் test directory ஒன்றை உருவாக்கவும்:
    ```bash
    mkdir test_docs
    ```

2. நீங்கள் மொழிபெயர்க்க விரும்பும் markdown documentation மற்றும் images-ஐ test directory-யில் நகலெடுக்கவும். உதாரணமாக:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Package-ஐ உள்ளூரில் நிறுவவும்:
    ```bash
    pip install -e .
    ```

4. உங்கள் test documents-இல் Co-op Translator-ஐ இயக்கவும்:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` மற்றும் `test_docs/translated_images`-இல் மொழிபெயர்க்கப்பட்ட கோப்புகளை சரிபார்க்கவும்:
   - மொழிபெயர்ப்பு தரம்
   - metadata comments சரியாக உள்ளதா
   - original markdown அமைப்பு பாதுகாக்கப்பட்டுள்ளதா
   - Links மற்றும் images சரியாக வேலை செய்கிறதா

இந்த கைமுறை சோதனை உங்கள் மாற்றங்கள் உண்மையான சூழலில் நன்றாக வேலை செய்கின்றன என்பதை உறுதி செய்ய உதவுகிறது.

### Environment variables

1. Provided `.env.template`-ஐ copy செய்து, root directory-யில் `.env` file ஒன்றை உருவாக்கவும்.
1. வழிகாட்டப்பட்டபடி environment variables-ஐ நிரப்பவும்.

> [!TIP]
>
> ### கூடுதல் development environment விருப்பங்கள்
>
> Project-ஐ உள்ளூரில் இயக்குவதற்கு கூடுதலாக, GitHub Codespaces அல்லது VS Code Dev Containers-ஐ மாற்று development environment-ஆக பயன்படுத்தலாம்.
>
> #### GitHub Codespaces
>
> GitHub Codespaces-ஐ பயன்படுத்தி இந்த samples-ஐ virtually இயக்கலாம், எந்த கூடுதல் அமைப்பும் தேவையில்லை.
>
> இந்த button-ஐ கிளிக் செய்தால் உங்கள் browser-இல் web-based VS Code instance-ஐ திறக்கும்:
>
> 1. Template-ஐ திறக்கவும் (இதற்கு சில நிமிடங்கள் ஆகலாம்):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### உள்ளூரில் VS Code Dev Containers பயன்படுத்தி இயக்குதல்
>
> ⚠️ இந்த விருப்பம் உங்கள் Docker Desktop-க்கு குறைந்தது 16 GB RAM ஒதுக்கப்பட்டிருந்தால் மட்டுமே வேலை செய்யும். 16 GB-க்கும் குறைவாக RAM இருந்தால், [GitHub Codespaces விருப்பத்தை](../..) முயற்சிக்கலாம் அல்லது [உள்ளூரில் அமைக்கலாம்](../..).
>
> தொடர்புடைய விருப்பம் VS Code Dev Containers, இது [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)-ஐ பயன்படுத்தி உங்கள் உள்ளூர் VS Code-இல் project-ஐ திறக்கும்:
>
> 1. Docker Desktop-ஐ துவக்கவும் (இல்லையெனில் நிறுவவும்)
> 2. Project-ஐ திறக்கவும்:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Code Style

Project-இல் code style-ஐ ஒரே மாதிரியாக வைத்திருக்க [Black](https://github.com/psf/black)-ஐ Python code formatter-ஆக பயன்படுத்துகிறோம். Black என்பது Python code-ஐ Black code style-க்கு தானாக மாற்றும் uncompromising code formatter ஆகும்.

#### அமைப்புகள்

Black-இன் அமைப்புகள் எங்கள் `pyproject.toml`-இல் குறிப்பிடப்பட்டுள்ளது:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black-ஐ நிறுவுதல்

Poetry (பரிந்துரைக்கப்படுகிறது) அல்லது pip-ஐ பயன்படுத்தி Black-ஐ நிறுவலாம்:

##### Poetry பயன்படுத்தி

Development environment-ஐ அமைக்கும் போது Black தானாகவே நிறுவப்படும்:
```bash
poetry install
```

##### pip பயன்படுத்தி

pip பயன்படுத்தினால், Black-ஐ நேரடியாக நிறுவலாம்:
```bash
pip install black
```

#### Black-ஐ பயன்படுத்துதல்

##### Poetry-யுடன்

1. Project-இல் உள்ள அனைத்து Python கோப்புகளையும் format செய்ய:
    ```bash
    poetry run black .
    ```

2. குறிப்பிட்ட கோப்பு அல்லது directory-ஐ format செய்ய:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip-யுடன்

1. Project-இல் உள்ள அனைத்து Python கோப்புகளையும் format செய்ய:
    ```bash
    black .
    ```

2. குறிப்பிட்ட கோப்பு அல்லது directory-ஐ format செய்ய:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Code-ஐ save செய்யும் போது Black-ஐ editor-ல் தானாக format செய்ய அமைப்பதை பரிந்துரைக்கிறோம். பெரும்பாலான modern editors-ல் இது extension அல்லது plugin-கள் மூலம் செய்யலாம்.

## Co-op Translator-ஐ இயக்குதல்

உங்கள் environment-இல் Poetry-ஐ பயன்படுத்தி Co-op Translator-ஐ இயக்க, கீழ்காணும் படிகளை பின்பற்றவும்:

1. மொழிபெயர்ப்பு சோதனை செய்ய விரும்பும் directory-க்கு செல்லவும் அல்லது சோதனைக்காக temporary folder ஒன்றை உருவாக்கவும்.

2. கீழ்காணும் command-ஐ இயக்கவும். `-l ko`-ஐ நீங்கள் மொழிபெயர்க்க விரும்பும் language code-ஆக மாற்றவும். `-d` flag debug mode-ஐ குறிக்கிறது.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Command-ஐ இயக்கும் முன் உங்கள் Poetry environment (poetry shell) செயல்படுத்தப்பட்டுள்ளதா என்பதை உறுதி செய்யவும்.

## புதிய மொழியை பங்களிக்க

புதிய மொழிகளுக்கான ஆதரவை சேர்க்கும் பங்களிப்புகளை வரவேற்கிறோம். PR-ஐ திறக்கும் முன், கீழ்காணும் படிகளை முடிக்கவும், இது review-ஐ எளிதாக்கும்.

1. மொழியை font mapping-இல் சேர்க்கவும்
   - `src/co_op_translator/fonts/font_language_mappings.yml`-ஐ திருத்தவும்
   - கீழ்காணும் entry-ஐ சேர்க்கவும்:
     - `code`: ISO-போன்ற language code (உதா, `vi`)
     - `name`: மனிதர்களுக்கு எளிதாக புரியும் பெயர்
     - `font`: script-ஐ ஆதரிக்கும் `src/co_op_translator/fonts/`-இல் உள்ள font
     - `rtl`: right-to-left என்றால் `true`, இல்லையெனில் `false`

2. தேவையான font files-ஐ சேர்க்கவும் (தேவைப்பட்டால்)
   - புதிய font தேவைப்பட்டால், open source distribution-க்கு license-ஐ சரிபார்க்கவும்
   - Font file-ஐ `src/co_op_translator/fonts/`-இல் சேர்க்கவும்

3. உள்ளூர் சோதனை
   - சிறிய sample-க்கு (Markdown, images, notebooks) மொழிபெயர்ப்பு இயக்கவும்
   - Output fonts மற்றும் RTL layout (தேவைப்பட்டால்) சரியாக காட்டுகிறதா என்பதை உறுதி செய்யவும்

4. Documentation-ஐ புதுப்பிக்கவும்
   - மொழி `getting_started/supported-languages.md`-இல் காட்டப்படுகிறதா என்பதை உறுதி செய்யவும்
   - `README_languages_template.md`-இல் மாற்றம் தேவையில்லை; இது supported list-இல் இருந்து உருவாக்கப்படுகிறது

5. PR-ஐ திறக்கவும்
   - சேர்க்கப்பட்ட மொழி மற்றும் font/license விவரங்களை விளக்கவும்
   - Screenshot-களை output-இன் rendu-ஐ இணைக்கவும் (முடிந்தால்)

உதாரண YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainers

### Commit message மற்றும் Merge strategy

Project-இன் commit history-யை ஒரே மாதிரியாகவும் தெளிவாகவும் வைத்திருக்க, **Squash and Merge** strategy-யை பயன்படுத்தும் போது **final commit message**-க்கு குறிப்பிட்ட commit message format-ஐ பின்பற்றுகிறோம்.

Pull request (PR) merge செய்யும்போது, தனிப்பட்ட commits எல்லாம் ஒரு commit-ஆக squashed செய்யப்படும். Final commit message கீழ்காணும் format-ஐ பின்பற்ற வேண்டும், இது history-யை சுத்தமாகவும் ஒரே மாதிரியாகவும் வைத்திருக்க உதவும்.

#### Commit message format (squash and merge-க்கு)

Commit messages-க்கு கீழ்காணும் format-ஐ பயன்படுத்துகிறோம்:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Commit-இன் வகையை குறிப்பிடும். கீழ்காணும் வகைகளை பயன்படுத்துகிறோம்:
  - `Docs`: Documentation-இல் மாற்றங்கள்.
  - `Build`: Build system அல்லது dependencies-இல் மாற்றங்கள், configuration files, CI workflows, Dockerfile-ஐ உள்ளடக்கியவை.
  - `Core`: Project-இன் முக்கிய செயல்பாடுகள் அல்லது அம்சங்களில் மாற்றங்கள், குறிப்பாக `src/co_op_translator/core` directory-யில் உள்ள கோப்புகள்.

- **description**: மாற்றத்தின் சுருக்கமான விளக்கம்.
- **PR number**: Commit-இன் pull request எண்ணிக்கை.

**உதாரணங்கள்**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> தற்போது, **`Docs`**, **`Core`**, மற்றும் **`Build`** prefixes PR title-க்கு labels-ஐ பொருத்த source code-இல் தானாகவே சேர்க்கப்படும். சரியான label-ஐ பயன்படுத்தினால், PR title-ஐ கைமுறையாக மாற்ற தேவையில்லை. Prefix சரியாக உருவாக்கப்பட்டுள்ளதா என்பதை மட்டும் சரிபார்க்க வேண்டும்.

#### Merge strategy

Pull requests-க்கு **Squash and Merge**-ஐ default strategy-ஆக பயன்படுத்துகிறோம். இந்த strategy-யால் commit messages format-ஐ பின்பற்ற முடியும், தனிப்பட்ட commits format-இல் இல்லாவிட்டாலும்.

**காரணங்கள்**:

- Project history-யை சுத்தமாகவும் நேராகவும் வைத்திருக்க.
- Commit messages-இல் ஒரே மாதிரி.
- சிறிய commits-இன் (உதா, "fix typo") குழப்பம் குறைவு.

Merge செய்யும் போது, final commit message commit message format-ஐ பின்பற்றுகிறதா என்பதை உறுதி செய்யவும்.

**Squash and Merge-இன் உதாரணம்**
ஒரு PR-இல் கீழ்காணும் commits இருந்தால்:

- `fix typo`
- `update README`
- `adjust formatting`

இவை squashed ஆக:
`Docs: Improve documentation clarity and formatting (#65)`

---

**பொறுப்புத் தவிர்ப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்தாலும், தானாக மொழிபெயர்க்கப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை தயவுசெய்து கவனிக்கவும். மூல ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல் அல்லது தவறான விளக்கத்திற்கு நாங்கள் பொறுப்பல்ல.