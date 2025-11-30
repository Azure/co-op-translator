<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:55:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tl"
}
-->
# Pagsali sa Co-op Translator

Malugod na tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Karamihan sa mga kontribusyon ay nangangailangan na sumang-ayon ka sa isang Contributor License Agreement (CLA) na nagsasaad na may karapatan ka, at talagang binibigyan mo kami ng karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang https://cla.opensource.microsoft.com.

Kapag nagsumite ka ng pull request, awtomatikong tutukuyin ng CLA bot kung kailangan mong magbigay ng CLA at bibigyan ng angkop na dekorasyon ang PR (hal., status check, komento). Sundin lamang ang mga tagubiling ibibigay ng bot. Isang beses mo lang ito kailangang gawin sa lahat ng repos na gumagamit ng aming CLA.

## Pagsasaayos ng kapaligiran sa pag-develop

Para maayos ang kapaligiran sa pag-develop para sa proyektong ito, inirerekomenda naming gamitin ang Poetry para sa pamamahala ng mga dependencies. Ginagamit namin ang `pyproject.toml` para pamahalaan ang mga dependencies ng proyekto, kaya para mag-install ng dependencies, dapat mong gamitin ang Poetry.

### Gumawa ng virtual environment

#### Gamit ang pip

```bash
python -m venv .venv
```

#### Gamit ang Poetry

```bash
poetry init
```

### I-activate ang virtual environment

#### Para sa parehong pip at Poetry

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

### Pag-install ng Package at mga kinakailangang Package

#### Gamit ang Poetry (mula sa pyproject.toml)

```bash
poetry install
```

### Manwal na pagsubok

Bago magsumite ng PR, mahalagang subukan ang functionality ng pagsasalin gamit ang totoong dokumentasyon:

1. Gumawa ng test directory sa root directory:
    ```bash
    mkdir test_docs
    ```

2. Kopyahin ang ilang markdown na dokumentasyon at mga larawan na nais mong isalin sa test directory. Halimbawa:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. I-install ang package nang lokal:
    ```bash
    pip install -e .
    ```

4. Patakbuhin ang Co-op Translator sa iyong mga test na dokumento:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Suriin ang mga isinaling file sa `test_docs/translations` at `test_docs/translated_images` upang tiyakin:
   - Ang kalidad ng pagsasalin
   - Tama ang mga metadata comments
   - Nananatili ang orihinal na istruktura ng markdown
   - Gumagana nang maayos ang mga link at larawan

Nakakatulong ang manwal na pagsubok na ito upang matiyak na maayos ang iyong mga pagbabago sa totoong mga sitwasyon.

### Mga environment variable

1. Gumawa ng `.env` file sa root directory sa pamamagitan ng pagkopya ng ibinigay na `.env.template` file.
1. Punan ang mga environment variable ayon sa gabay.

> [!TIP]
>
> ### Karagdagang mga opsyon sa kapaligiran sa pag-develop
>
> Bukod sa pagpapatakbo ng proyekto nang lokal, maaari mo ring gamitin ang GitHub Codespaces o VS Code Dev Containers bilang alternatibong setup ng kapaligiran sa pag-develop.
>
> #### GitHub Codespaces
>
> Maaari mong patakbuhin ang mga sample na ito nang virtual gamit ang GitHub Codespaces at hindi na kailangan ng karagdagang mga setting o setup.
>
> Ang button ay magbubukas ng web-based na VS Code instance sa iyong browser:
>
> 1. Buksan ang template (maaaring tumagal ng ilang minuto):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Pagpapatakbo nang Lokal gamit ang VS Code Dev Containers
>
> ⚠️ Gagana lamang ang opsyong ito kung ang iyong Docker Desktop ay may nakalaan na hindi bababa sa 16 GB ng RAM. Kung mas mababa sa 16 GB ang RAM mo, maaari mong subukan ang [GitHub Codespaces option](../..) o [isetup ito nang lokal](../..).
>
> Isang kaugnay na opsyon ay ang VS Code Dev Containers, na magbubukas ng proyekto sa iyong lokal na VS Code gamit ang [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Simulan ang Docker Desktop (i-install ito kung hindi pa naka-install)
> 2. Buksan ang proyekto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Estilo ng Code

Gumagamit kami ng [Black](https://github.com/psf/black) bilang aming Python code formatter upang mapanatili ang pare-parehong estilo ng code sa buong proyekto. Ang Black ay isang mahigpit na code formatter na awtomatikong nire-reformat ang Python code upang sumunod sa estilo ng Black.

#### Konfigurasyon

Ang konfigurasyon ng Black ay tinukoy sa aming `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Pag-install ng Black

Maaari mong i-install ang Black gamit ang Poetry (inirerekomenda) o pip:

##### Gamit ang Poetry

Awtomatikong na-i-install ang Black kapag sinetup mo ang kapaligiran sa pag-develop:
```bash
poetry install
```

##### Gamit ang pip

Kung gumagamit ka ng pip, maaari mong direktang i-install ang Black:
```bash
pip install black
```

#### Paggamit ng Black

##### Sa Poetry

1. I-format ang lahat ng Python files sa proyekto:
    ```bash
    poetry run black .
    ```

2. I-format ang isang partikular na file o direktoryo:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Sa pip

1. I-format ang lahat ng Python files sa proyekto:
    ```bash
    black .
    ```

2. I-format ang isang partikular na file o direktoryo:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Inirerekomenda naming i-setup ang iyong editor upang awtomatikong i-format ang code gamit ang Black tuwing nagsa-save. Karamihan sa mga modernong editor ay sumusuporta dito sa pamamagitan ng mga extension o plugin.

## Pagpapatakbo ng Co-op Translator

Para patakbuhin ang Co-op Translator gamit ang Poetry sa iyong kapaligiran, sundin ang mga hakbang na ito:

1. Pumunta sa direktoryo kung saan mo nais magsagawa ng mga pagsubok sa pagsasalin o gumawa ng pansamantalang folder para sa mga layunin ng pagsubok.

2. Patakbuhin ang sumusunod na utos. Palitan ang `-l ko` ng code ng wikang nais mong isalin. Ang flag na `-d` ay nangangahulugang debug mode.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Siguraduhing naka-activate ang iyong Poetry environment (poetry shell) bago patakbuhin ang utos.

## Mag-ambag ng bagong wika

Malugod naming tinatanggap ang mga kontribusyon na nagdaragdag ng suporta para sa mga bagong wika. Bago magbukas ng PR, pakisunod ang mga hakbang sa ibaba upang matiyak ang maayos na pagsusuri.

1. Idagdag ang wika sa font mapping
   - I-edit ang `src/co_op_translator/fonts/font_language_mappings.yml`
   - Magdagdag ng entry na may:
     - `code`: ISO-like na code ng wika (hal., `vi`)
     - `name`: Pangalan na madaling maintindihan
     - `font`: Isang font na kasama sa `src/co_op_translator/fonts/` na sumusuporta sa script
     - `rtl`: `true` kung right-to-left, kung hindi ay `false`

2. Isama ang mga kinakailangang font files (kung kailangan)
   - Kung kinakailangan ng bagong font, tiyaking compatible ang lisensya para sa open source na distribusyon
   - Idagdag ang font file sa `src/co_op_translator/fonts/`

3. Lokal na beripikasyon
   - Patakbuhin ang mga pagsasalin para sa maliit na sample (Markdown, mga larawan, at notebooks kung naaangkop)
   - Suriin kung tama ang output, kasama ang mga font at anumang RTL layout kung mayroon

4. I-update ang dokumentasyon
   - Siguraduhing lumalabas ang wika sa `getting_started/supported-languages.md`
   - Hindi kailangan baguhin ang `getting_started/README_languages_template.md`; ito ay awtomatikong ginagawa mula sa listahan ng mga sinusuportahang wika

5. Magbukas ng PR
   - Ilahad ang idinagdag na wika at anumang font/licensing na konsiderasyon
   - Isama ang mga screenshot ng mga rendered output kung maaari

Halimbawa ng YAML entry:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Subukan ang bagong wika

Maaari mong subukan ang bagong wika sa pamamagitan ng pagpapatakbo ng sumusunod na utos:

```bash
# Gumawa at i-activate ang isang virtual na kapaligiran
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# I-install ang development package
pip install -e .
# Patakbuhin ang pagsasalin
translate -l "new_lang"
```

## Mga Tagapangalaga

### Mensahe ng commit at Estratehiya sa Merge

Para matiyak ang pagkakapare-pareho at kalinawan sa kasaysayan ng commit ng aming proyekto, sumusunod kami sa isang partikular na format ng mensahe ng commit **para sa panghuling mensahe ng commit** kapag ginagamit ang **Squash and Merge** na estratehiya.

Kapag na-merge ang isang pull request (PR), ang mga indibidwal na commit ay pagsasamahin sa isang commit. Ang panghuling mensahe ng commit ay dapat sumunod sa format sa ibaba upang mapanatili ang malinis at pare-parehong kasaysayan.

#### Format ng mensahe ng commit (para sa squash and merge)

Ginagamit namin ang sumusunod na format para sa mga mensahe ng commit:

```bash
<type>: <description> (#<PR numero>)
```

- **type**: Tinukoy ang kategorya ng commit. Ginagamit namin ang mga sumusunod na uri:
  - `Docs`: Para sa mga update sa dokumentasyon.
  - `Build`: Para sa mga pagbabago na may kinalaman sa build system o dependencies, kabilang ang mga update sa configuration files, CI workflows, o Dockerfile.
  - `Core`: Para sa mga pagbabago sa pangunahing functionality o mga tampok ng proyekto, lalo na sa mga file sa `src/co_op_translator/core` na direktoryo.

- **description**: Isang maikling buod ng pagbabago.
- **PR number**: Ang numero ng pull request na kaugnay ng commit.

**Mga halimbawa**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Sa kasalukuyan, ang mga prefix na **`Docs`**, **`Core`**, at **`Build`** ay awtomatikong idinadagdag sa mga pamagat ng PR base sa mga label na inilapat sa binagong source code. Hangga't tama ang label na inilapat, karaniwan ay hindi mo na kailangang mano-manong baguhin ang pamagat ng PR. Kailangan mo lamang tiyakin na tama ang lahat at na-generate nang maayos ang prefix.

#### Estratehiya sa Merge

Ginagamit namin ang **Squash and Merge** bilang default na estratehiya para sa mga pull request. Tinitiyak ng estratehiyang ito na sumusunod ang mga mensahe ng commit sa aming format, kahit na ang mga indibidwal na commit ay hindi.

**Mga dahilan**:

- Malinis at linear na kasaysayan ng proyekto.
- Pagkakapare-pareho sa mga mensahe ng commit.
- Nabawasang ingay mula sa maliliit na commit (hal., "fix typo").

Kapag nagme-merge, siguraduhing ang panghuling mensahe ng commit ay sumusunod sa format ng mensahe ng commit na inilarawan sa itaas.

**Halimbawa ng Squash and Merge**
Kung ang isang PR ay may mga sumusunod na commit:

- `fix typo`
- `update README`
- `adjust formatting`

Dapat itong pagsamahin sa:
`Docs: Improve documentation clarity and formatting (#65)`

### Proseso ng pag-release

Inilalarawan ng seksyong ito ang pinakasimpleng paraan para sa mga tagapangalaga na maglathala ng bagong release ng Co-op Translator.

#### 1. Itaas ang bersyon sa `pyproject.toml`

1. Piliin ang susunod na numero ng bersyon (sumusunod kami sa semantic versioning: `MAJOR.MINOR.PATCH`).
2. I-edit ang `pyproject.toml` at i-update ang `version` field sa ilalim ng `[tool.poetry]`.
3. Magbukas ng dedikadong pull request na nagbabago lamang ng bersyon (at anumang awtomatikong na-update na lock/metadata files, kung mayroon).
4. Pagkatapos ng pagsusuri, gamitin ang **Squash and Merge** at siguraduhing ang panghuling mensahe ng commit ay sumusunod sa format na inilarawan sa itaas.

#### 2. Gumawa ng GitHub Release

1. Pumunta sa pahina ng GitHub repository at buksan ang **Releases** → **Draft a new release**.
2. Gumawa ng bagong tag (halimbawa, `v0.13.0`) mula sa `main` branch.
3. Itakda ang pamagat ng release sa parehong bersyon (halimbawa, `v0.13.0`).
4. I-click ang **Generate release notes** para awtomatikong mapunan ang changelog.
5. Opsyonal na i-edit ang teksto (halimbawa, para i-highlight ang mga bagong sinusuportahang wika o mahahalagang pagbabago).
6. I-publish ang release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->