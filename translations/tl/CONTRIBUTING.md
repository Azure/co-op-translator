<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:41:52+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tl"
}
-->
# Pagsali sa Co-op Translator

Malugod naming tinatanggap ang mga kontribusyon at suhestiyon sa proyektong ito. Karamihan sa mga kontribusyon ay nangangailangan ng pagsang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na may karapatan ka at aktwal na ibinibigay mo sa amin ang mga karapatan na gamitin ang iyong kontribusyon. Para sa detalye, bisitahin ang https://cla.opensource.microsoft.com.

Kapag nagsumite ka ng pull request, awtomatikong tutukuyin ng CLA bot kung kailangan mong magbigay ng CLA at lalagyan ng tamang status ang PR (hal. status check, komento). Sundin lang ang mga tagubilin ng bot. Isang beses mo lang kailangang gawin ito sa lahat ng repo na gumagamit ng aming CLA.

## Pag-set up ng Development Environment

Para sa pag-set up ng development environment ng proyektong ito, inirerekomenda naming gamitin ang Poetry para sa pag-manage ng dependencies. Ginagamit namin ang `pyproject.toml` para sa pag-manage ng dependencies ng proyekto, kaya para mag-install ng dependencies, dapat gamitin ang Poetry.

### Gumawa ng Virtual Environment

#### Gamit ang pip

```bash
python -m venv .venv
```

#### Gamit ang Poetry

```bash
poetry init
```

### I-activate ang Virtual Environment

#### Para sa pip at Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Gamit ang Poetry

```bash
poetry shell
```

### Pag-install ng Package at mga Kailangan na Package

#### Gamit ang Poetry (mula sa pyproject.toml)

```bash
poetry install
```

### Manwal na Pagsusuri

Bago magsumite ng PR, mahalagang subukan ang functionality ng translation gamit ang totoong dokumentasyon:

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

5. Suriin ang mga naisalin na file sa `test_docs/translations` at `test_docs/translated_images` para tiyakin:
   - Maganda ang kalidad ng salin
   - Tama ang metadata comments
   - Napanatili ang orihinal na markdown structure
   - Gumagana nang maayos ang mga link at larawan

Nakakatulong ang manwal na pagsusuri para matiyak na maayos ang iyong mga pagbabago sa totoong sitwasyon.

### Environment Variables

1. Gumawa ng `.env` file sa root directory sa pamamagitan ng pagkopya ng ibinigay na `.env.template` file.
1. Punan ang environment variables ayon sa gabay.

> [!TIP]
>
> ### Karagdagang Opsyon para sa Development Environment
>
> Bukod sa pagtakbo ng proyekto nang lokal, maaari mo ring gamitin ang GitHub Codespaces o VS Code Dev Containers bilang alternatibong paraan ng pag-set up ng development environment.
>
> #### GitHub Codespaces
>
> Maaari mong patakbuhin ang mga sample na ito nang virtual gamit ang GitHub Codespaces at wala nang karagdagang settings o setup na kailangan.
>
> Ang button ay magbubukas ng web-based na VS Code instance sa iyong browser:
>
> 1. Buksan ang template (maaaring tumagal ng ilang minuto):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Pagpatakbo nang Lokal gamit ang VS Code Dev Containers
>
> ⚠️ Gagana lang ang opsyong ito kung ang iyong Docker Desktop ay may at least 16 GB na RAM. Kung mas mababa sa 16 GB ang RAM mo, subukan ang [GitHub Codespaces option](../..) o [i-set up nang lokal](../..).
>
> Isa pang opsyon ay ang VS Code Dev Containers, na magbubukas ng proyekto sa iyong lokal na VS Code gamit ang [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. I-start ang Docker Desktop (i-install kung hindi pa naka-install)
> 2. Buksan ang proyekto:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### Code Style

Gamit namin ang [Black](https://github.com/psf/black) bilang Python code formatter para mapanatili ang consistent na code style sa buong proyekto. Ang Black ay isang code formatter na awtomatikong nire-reformat ang Python code para sumunod sa Black code style.

#### Configuration

Ang configuration ng Black ay nakasaad sa aming `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Pag-install ng Black

Pwede mong i-install ang Black gamit ang Poetry (inirerekomenda) o pip:

##### Gamit ang Poetry

Awtomatikong nai-install ang Black kapag sinet-up mo ang development environment:
```bash
poetry install
```

##### Gamit ang pip

Kung pip ang gamit mo, pwede mong i-install ang Black nang direkta:
```bash
pip install black
```

#### Paggamit ng Black

##### Gamit ang Poetry

1. I-format ang lahat ng Python files sa proyekto:
    ```bash
    poetry run black .
    ```

2. I-format ang partikular na file o directory:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Gamit ang pip

1. I-format ang lahat ng Python files sa proyekto:
    ```bash
    black .
    ```

2. I-format ang partikular na file o directory:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Inirerekomenda naming i-set up ang iyong editor para awtomatikong mag-format ng code gamit ang Black tuwing magse-save. Karamihan sa mga modernong editor ay may suporta dito sa pamamagitan ng extensions o plugins.

## Pagpatakbo ng Co-op Translator

Para patakbuhin ang Co-op Translator gamit ang Poetry sa iyong environment, sundin ang mga hakbang na ito:

1. Pumunta sa directory kung saan mo gustong magsagawa ng translation tests o gumawa ng temporary folder para sa testing.

2. I-execute ang sumusunod na command. Palitan ang `-l ko` ng language code na gusto mong gamitin. Ang `-d` flag ay para sa debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Tiyaking naka-activate ang iyong Poetry environment (poetry shell) bago patakbuhin ang command.

## Magdagdag ng Bagong Wika

Malugod naming tinatanggap ang mga kontribusyon para sa bagong wika. Bago magbukas ng PR, kumpletuhin muna ang mga hakbang sa ibaba para mas madali ang review.

1. Idagdag ang wika sa font mapping
   - I-edit ang `src/co_op_translator/fonts/font_language_mappings.yml`
   - Magdagdag ng entry na may:
     - `code`: ISO-like language code (hal. `vi`)
     - `name`: Pangalan ng wika na madaling maintindihan
     - `font`: Font na kasama sa `src/co_op_translator/fonts/` na sumusuporta sa script
     - `rtl`: `true` kung right-to-left, kung hindi `false`

2. Isama ang kinakailangang font files (kung kailangan)
   - Kung kailangan ng bagong font, tiyaking compatible ang license para sa open source distribution
   - Idagdag ang font file sa `src/co_op_translator/fonts/`

3. Lokal na beripikasyon
   - Patakbuhin ang translation para sa maliit na sample (Markdown, images, at notebooks kung naaangkop)
   - Tiyaking tama ang output, kasama ang fonts at RTL layout kung kailangan

4. I-update ang dokumentasyon
   - Tiyaking lumalabas ang wika sa `getting_started/supported-languages.md`
   - Walang kailangang baguhin sa `README_languages_template.md`; awtomatikong nabubuo ito mula sa supported list

5. Magbukas ng PR
   - Ilarawan ang wikang idinagdag at anumang font/licensing considerations
   - Mag-attach ng screenshots ng rendered outputs kung maaari

Halimbawa ng YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Mga Tagapangalaga

### Commit Message at Merge Strategy

Para sa consistency at kalinawan ng commit history ng proyekto, sinusunod namin ang partikular na format ng commit message **para sa final commit message** kapag gumagamit ng **Squash and Merge** strategy.

Kapag na-merge ang pull request (PR), pagsasamahin ang mga individual commits sa isang commit. Dapat sundin ng final commit message ang format sa ibaba para mapanatili ang malinis at consistent na history.

#### Format ng Commit Message (para sa squash and merge)

Ginagamit namin ang format na ito para sa commit messages:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Tumutukoy sa kategorya ng commit. Ginagamit namin ang mga sumusunod na type:
  - `Docs`: Para sa updates sa dokumentasyon.
  - `Build`: Para sa mga pagbabago sa build system o dependencies, kabilang ang updates sa configuration files, CI workflows, o Dockerfile.
  - `Core`: Para sa mga pagbabago sa core functionality o features ng proyekto, lalo na sa mga file sa `src/co_op_translator/core` directory.

- **description**: Maikling buod ng pagbabago.
- **PR number**: Numero ng pull request na kaugnay ng commit.

**Mga Halimbawa**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Sa kasalukuyan, ang **`Docs`**, **`Core`**, at **`Build`** na prefix ay awtomatikong idinadagdag sa PR titles base sa labels na naka-apply sa binagong source code. Basta tama ang label, kadalasan hindi mo na kailangang baguhin ang PR title. Kailangan mo lang tiyakin na tama ang lahat at na-generate nang maayos ang prefix.

#### Merge Strategy

Gamit namin ang **Squash and Merge** bilang default na strategy para sa pull requests. Tinitiyak ng strategy na ito na sumusunod ang commit messages sa aming format, kahit hindi pa ito nasunod sa individual commits.

**Mga Dahilan**:

- Malinis at linear na project history.
- Consistent na commit messages.
- Mas kaunting ingay mula sa maliliit na commits (hal. "fix typo").

Kapag nagme-merge, tiyaking sumusunod ang final commit message sa format na nakasaad sa itaas.

**Halimbawa ng Squash and Merge**
Kung ang PR ay may mga sumusunod na commits:

- `fix typo`
- `update README`
- `adjust formatting`

Dapat pagsamahin ito bilang:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.