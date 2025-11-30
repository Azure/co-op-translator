<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:59:34+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sw"
}
-->
# Kuchangia kwa Co-op Translator

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji ukakubali Mkataba wa Leseni ya Mchangiaji (CLA) unaothibitisha kuwa una haki, na kwa kweli unatuwezesha kutumia mchango wako. Kwa maelezo zaidi, tembelea https://cla.opensource.microsoft.com.

Unapowasilisha ombi la pull request, bot ya CLA itagundua moja kwa moja kama unahitaji kutoa CLA na kuandaa PR ipasavyo (mfano, ukaguzi wa hali, maoni). Fuata tu maelekezo yanayotolewa na bot. Hii unahitaji kufanya mara moja tu kwa repos zote zinazotumia CLA yetu.

## Kuanzisha mazingira ya maendeleo

Ili kuanzisha mazingira ya maendeleo kwa mradi huu, tunapendekeza kutumia Poetry kusimamia utegemezi. Tunatumia `pyproject.toml` kusimamia utegemezi wa mradi, kwa hivyo, kusakinisha utegemezi, unapaswa kutumia Poetry.

### Tengeneza mazingira ya virtual

#### Kutumia pip

```bash
python -m venv .venv
```

#### Kutumia Poetry

```bash
poetry init
```

### Washa mazingira ya virtual

#### Kwa pip na Poetry zote mbili

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Kutumia Poetry

```bash
poetry shell
```

### Kusakinisha Pakiti na Pakiti zinazohitajika

#### Kutumia Poetry (kutoka pyproject.toml)

```bash
poetry install
```

### Kupima kwa mkono

Kabla ya kuwasilisha PR, ni muhimu kupima utendaji wa tafsiri kwa kutumia nyaraka halisi:

1. Tengeneza saraka ya majaribio kwenye saraka kuu:
    ```bash
    mkdir test_docs
    ```

2. Nakili baadhi ya nyaraka za markdown na picha unazotaka kutafsiri kwenye saraka ya majaribio. Kwa mfano:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Sakinisha pakiti kwa ndani:
    ```bash
    pip install -e .
    ```

4. Endesha Co-op Translator kwenye nyaraka zako za majaribio:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Angalia faili zilizotafsiriwa katika `test_docs/translations` na `test_docs/translated_images` kuthibitisha:
   - Ubora wa tafsiri
   - Maoni ya metadata ni sahihi
   - Muundo wa awali wa markdown umehifadhiwa
   - Viungo na picha vinafanya kazi vizuri

Kupima kwa mkono husaidia kuhakikisha mabadiliko yako yanafanya kazi vizuri katika hali halisi.

### Mabadiliko ya mazingira

1. Tengeneza faili `.env` kwenye saraka kuu kwa kunakili faili `.env.template` iliyotolewa.
1. Jaza mabadiliko ya mazingira kama ilivyoelekezwa.

> [!TIP]
>
> ### Chaguzi za ziada za mazingira ya maendeleo
>
> Mbali na kuendesha mradi kwa ndani, unaweza pia kutumia GitHub Codespaces au VS Code Dev Containers kama mbadala wa mazingira ya maendeleo.
>
> #### GitHub Codespaces
>
> Unaweza kuendesha sampuli hizi kwa mtandao kwa kutumia GitHub Codespaces na hakuna mipangilio au usanidi wa ziada unaohitajika.
>
> Kitufe kitafungua toleo la VS Code la mtandao kwenye kivinjari chako:
>
> 1. Fungua kiolezo (hii inaweza kuchukua dakika kadhaa):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kuendesha kwa ndani kwa kutumia VS Code Dev Containers
>
> ⚠️ Chaguo hili litafanya kazi tu ikiwa Docker Desktop yako imepewa angalau GB 16 za RAM. Ikiwa una chini ya GB 16 za RAM, unaweza jaribu [chaguo la GitHub Codespaces](../..) au [kuandaa kwa ndani](../..).
>
> Chaguo linalohusiana ni VS Code Dev Containers, ambalo litaifungua mradi kwenye VS Code yako ya ndani kwa kutumia [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Anzisha Docker Desktop (sakinisha ikiwa bado haijasakinishwa)
> 2. Fungua mradi:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Mtindo wa Msimbo

Tunatumia [Black](https://github.com/psf/black) kama mpangaji msimbo wa Python ili kudumisha mtindo thabiti wa msimbo katika mradi. Black ni mpangaji msimbo usio na msamaha unaobadilisha msimbo wa Python moja kwa moja ili uendane na mtindo wa Black.

#### Usanidi

Usanidi wa Black umeainishwa katika `pyproject.toml` yetu:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Kusakinisha Black

Unaweza kusakinisha Black kwa kutumia Poetry (inapendekezwa) au pip:

##### Kutumia Poetry

Black husakinishwa moja kwa moja unapoanzisha mazingira ya maendeleo:
```bash
poetry install
```

##### Kutumia pip

Ikiwa unatumia pip, unaweza kusakinisha Black moja kwa moja:
```bash
pip install black
```

#### Kutumia Black

##### Kwa Poetry

1. Panga faili zote za Python katika mradi:
    ```bash
    poetry run black .
    ```

2. Panga faili au saraka maalum:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Kwa pip

1. Panga faili zote za Python katika mradi:
    ```bash
    black .
    ```

2. Panga faili au saraka maalum:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Tunapendekeza kuweka mhariri wako upange msimbo kiotomatiki kwa Black unapoihifadhi. Wahariri wengi wa kisasa wanaunga mkono hili kupitia nyongeza au programu-jalizi.

## Kuendesha Co-op Translator

Ili kuendesha Co-op Translator kwa kutumia Poetry katika mazingira yako, fuata hatua hizi:

1. Nenda kwenye saraka unayotaka kufanya majaribio ya tafsiri au tengeneza folda ya muda kwa madhumuni ya majaribio.

2. Endesha amri ifuatayo. Badilisha `-l ko` na msimbo wa lugha unayotaka kutafsiri. Bendera `-d` inaonyesha hali ya debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Hakikisha mazingira yako ya Poetry yamewashwa (poetry shell) kabla ya kuendesha amri.

## Changia lugha mpya

Tunakaribisha michango inayoongeza msaada kwa lugha mpya. Kabla ya kufungua PR, tafadhali kamilisha hatua zilizo hapa chini ili kuhakikisha ukaguzi mzuri.

1. Ongeza lugha kwenye ramani ya fonti
   - Hariri `src/co_op_translator/fonts/font_language_mappings.yml`
   - Ongeza kipengee chenye:
     - `code`: msimbo wa lugha unaofanana na ISO (mfano, `vi`)
     - `name`: Jina la kuonyesha linaloeleweka na watu
     - `font`: Fonti iliyopo `src/co_op_translator/fonts/` inayounga mkono maandishi
     - `rtl`: `true` ikiwa ni kutoka kulia kwenda kushoto, vinginevyo `false`

2. Jumuisha faili za fonti zinazohitajika (ikiwa zinahitajika)
   - Ikiwa fonti mpya inahitajika, hakikisha leseni inaruhusu usambazaji wa chanzo wazi
   - Ongeza faili ya fonti kwenye `src/co_op_translator/fonts/`

3. Thibitisha kwa ndani
   - Endesha tafsiri kwa sampuli ndogo (Markdown, picha, na daftari kama inavyofaa)
   - Hakikisha matokeo yanaonyeshwa vizuri, ikijumuisha fonti na mpangilio wa RTL ikiwa unahitajika

4. Sasisha nyaraka
   - Hakikisha lugha inaonekana katika `getting_started/supported-languages.md`
   - Hakuna mabadiliko yanayohitajika kwenye `getting_started/README_languages_template.md`; inatengenezwa kutoka kwa orodha ya lugha zinazotegemewa

5. Fungua PR
   - Eleza lugha iliyoongezwa na masuala yoyote ya fonti/leseni
   - Ambatisha picha za skrini za matokeo ikiwa inawezekana

Mfano wa kipengee cha YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Jaribu lugha mpya

Unaweza kujaribu lugha mpya kwa kuendesha amri ifuatayo:

```bash
# Unda na wezesha mazingira pepe
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Sakinisha kifurushi cha maendeleo
pip install -e .
# Endesha tafsiri
translate -l "new_lang"
```

## Watunzaji

### Ujumbe wa commit na Mkakati wa Kuunganisha

Ili kuhakikisha muendelezo na uwazi katika historia ya commit ya mradi wetu, tunafuata muundo maalum wa ujumbe wa commit **kwa ujumbe wa commit wa mwisho** tunapotumia mkakati wa **Squash and Merge**.

Wakati pull request (PR) inapounganishwa, commits binafsi zitachanganywa kuwa commit moja. Ujumbe wa commit wa mwisho unapaswa kufuata muundo ulio hapa chini ili kudumisha historia safi na thabiti.

#### Muundo wa ujumbe wa commit (kwa squash and merge)

Tunatumia muundo ufuatao kwa ujumbe wa commit:

```bash
<type>: <description> (#<Nambari ya PR>)
```

- **type**: Inaelezea aina ya commit. Tunatumia aina zifuatazo:
  - `Docs`: Kwa masasisho ya nyaraka.
  - `Build`: Kwa mabadiliko yanayohusiana na mfumo wa kujenga au utegemezi, ikiwa ni pamoja na masasisho ya faili za usanidi, michakato ya CI, au Dockerfile.
  - `Core`: Kwa mabadiliko ya kazi kuu au vipengele vya mradi, hasa zile zinazohusisha faili katika saraka `src/co_op_translator/core`.

- **description**: Muhtasari mfupi wa mabadiliko.
- **PR number**: Nambari ya pull request inayohusiana na commit.

**Mifano**:

- `Docs: Sasisha maelekezo ya usakinishaji kwa uwazi (#50)`
- `Core: Boresha usimamizi wa tafsiri ya picha (#60)`

> [!NOTE]
> Kwa sasa, viambatanisho vya **`Docs`**, **`Core`**, na **`Build`** vinaongezwa moja kwa moja kwenye vichwa vya PR kulingana na lebo zilizowekwa kwenye msimbo uliobadilishwa. Mradi lebo sahihi imewekwa, kawaida huna haja ya kubadilisha kichwa cha PR kwa mkono. Unahitaji tu kuthibitisha kila kitu kiko sawa na kiambatanisho kimeundwa ipasavyo.

#### Mkakati wa kuunganisha

Tunatumia **Squash and Merge** kama mkakati wetu wa kawaida kwa pull requests. Mkakati huu unahakikisha ujumbe wa commit unafuata muundo wetu, hata kama commits binafsi hazifuatilii.

**Sababu**:

- Historia safi, ya mstari wa mradi.
- Muendelezo katika ujumbe wa commit.
- Kupunguza kelele kutoka kwa commits ndogo (mfano, "rekebisha typo").

Unapounganisha, hakikisha ujumbe wa commit wa mwisho unafuata muundo wa ujumbe wa commit ulioelezwa hapo juu.

**Mfano wa Squash and Merge**
Ikiwa PR ina commits zifuatazo:

- `rekebisha typo`
- `sasisha README`
- `rekebisha muundo`

Zitachanganywa kuwa:
`Docs: Boresha uwazi na muundo wa nyaraka (#65)`

### Mchakato wa kutolewa kwa toleo

Sehemu hii inaelezea njia rahisi kwa watunzaji kuchapisha toleo jipya la Co-op Translator.

#### 1. Ongeza toleo katika `pyproject.toml`

1. Amua nambari ya toleo lijalo (tunafuata semantic versioning: `MAJOR.MINOR.PATCH`).
2. Hariri `pyproject.toml` na sasisha sehemu ya `version` chini ya `[tool.poetry]`.
3. Fungua pull request maalum inayobadilisha toleo tu (na faili zozote za lock/metadata zilizosasishwa moja kwa moja, ikiwa zipo).
4. Baada ya ukaguzi, tumia **Squash and Merge** na hakikisha ujumbe wa commit wa mwisho unafuata muundo ulioelezwa hapo juu.

#### 2. Tengeneza Toleo la GitHub

1. Nenda kwenye ukurasa wa hifadhi ya GitHub na fungua **Releases** → **Draft a new release**.
2. Tengeneza tag mpya (kwa mfano, `v0.13.0`) kutoka tawi la `main`.
3. Weka kichwa cha toleo kuwa toleo lile lile (kwa mfano, `v0.13.0`).
4. Bonyeza **Generate release notes** ili kujaza kiotomatiki kumbukumbu za mabadiliko.
5. Hiari, hariri maandishi (kwa mfano, kuonyesha lugha mpya zinazotegemewa au mabadiliko muhimu).
6. Chapisha toleo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kukataa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->