<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:44:33+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sw"
}
-->
# Kuchangia kwenye Co-op Translator

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji ukubali Mkataba wa Leseni ya Mchangiaji (CLA) unaothibitisha kuwa una haki ya, na kweli unatoa, haki ya sisi kutumia mchango wako. Kwa maelezo zaidi, tembelea https://cla.opensource.microsoft.com.

Unapowasilisha pull request, bot ya CLA itatambua moja kwa moja kama unahitaji kutoa CLA na itaweka alama kwenye PR ipasavyo (mfano, status check, maoni). Fuata tu maelekezo yatakayotolewa na bot. Utahitaji kufanya hili mara moja tu kwenye repos zote zinazotumia CLA yetu.

## Kuandaa Mazingira ya Maendeleo

Ili kuandaa mazingira ya maendeleo kwa mradi huu, tunapendekeza utumie Poetry kusimamia utegemezi. Tunatumia `pyproject.toml` kusimamia utegemezi wa mradi, hivyo ili kusakinisha utegemezi, tumia Poetry.

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

#### Kwa pip na Poetry zote

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

### Kusakinisha Package na Packages zinazohitajika

#### Kutumia Poetry (kutoka pyproject.toml)

```bash
poetry install
```

### Kupima kwa mkono

Kabla ya kuwasilisha PR, ni muhimu kupima uwezo wa kutafsiri kwa kutumia nyaraka halisi:

1. Tengeneza folda ya majaribio kwenye mzizi wa mradi:
    ```bash
    mkdir test_docs
    ```

2. Nakili baadhi ya nyaraka za markdown na picha unazotaka kutafsiri kwenye folda ya majaribio. Kwa mfano:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Sakinisha package kwa njia ya ndani:
    ```bash
    pip install -e .
    ```

4. Endesha Co-op Translator kwenye nyaraka zako za majaribio:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Angalia faili zilizotafsiriwa kwenye `test_docs/translations` na `test_docs/translated_images` ili kuthibitisha:
   - Ubora wa tafsiri
   - Maoni ya metadata ni sahihi
   - Muundo wa asili wa markdown umehifadhiwa
   - Viungo na picha vinafanya kazi vizuri

Majaribio haya ya mkono husaidia kuhakikisha mabadiliko yako yanafanya kazi vizuri kwenye mazingira halisi.

### Vigezo vya mazingira

1. Tengeneza faili `.env` kwenye mzizi wa mradi kwa kunakili faili `.env.template` iliyopo.
1. Jaza vigezo vya mazingira kama ulivyoelekezwa.

> [!TIP]
>
> ### Chaguo za ziada za mazingira ya maendeleo
>
> Mbali na kuendesha mradi kwa njia ya ndani, unaweza pia kutumia GitHub Codespaces au VS Code Dev Containers kama njia mbadala ya kuandaa mazingira ya maendeleo.
>
> #### GitHub Codespaces
>
> Unaweza kuendesha sampuli hizi kwa njia ya mtandao kwa kutumia GitHub Codespaces bila mipangilio au maandalizi ya ziada.
>
> Kitufe kitafungua toleo la VS Code kwenye kivinjari chako:
>
> 1. Fungua template (hii inaweza kuchukua dakika kadhaa):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Kuendesha kwa ndani kwa kutumia VS Code Dev Containers
>
> ⚠️ Chaguo hili litafanya kazi tu kama Docker Desktop yako imetengewa angalau 16 GB ya RAM. Kama una RAM chini ya 16 GB, unaweza kujaribu [chaguo la GitHub Codespaces](../..) au [kuandaa kwa ndani](../..).
>
> Chaguo lingine ni VS Code Dev Containers, ambayo itafungua mradi kwenye VS Code yako ya ndani kwa kutumia [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Anzisha Docker Desktop (sakinisha kama bado haijasakinishwa)
> 2. Fungua mradi:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Mtindo wa Kuandika Code

Tunatumia [Black](https://github.com/psf/black) kama formatter ya Python ili kudumisha mtindo wa code ulio sawa kwenye mradi. Black ni formatter isiyokubali maelewano ambayo inarekebisha code ya Python moja kwa moja kufuata mtindo wa Black.

#### Mpangilio

Mpangilio wa Black umeainishwa kwenye `pyproject.toml` yetu:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Kusakinisha Black

Unaweza kusakinisha Black kwa kutumia Poetry (inapendekezwa) au pip:

##### Kutumia Poetry

Black inasakinishwa moja kwa moja unapoweka mazingira ya maendeleo:
```bash
poetry install
```

##### Kutumia pip

Kama unatumia pip, unaweza kusakinisha Black moja kwa moja:
```bash
pip install black
```

#### Kutumia Black

##### Kwa Poetry

1. Rekebisha faili zote za Python kwenye mradi:
    ```bash
    poetry run black .
    ```

2. Rekebisha faili au folda maalum:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Kwa pip

1. Rekebisha faili zote za Python kwenye mradi:
    ```bash
    black .
    ```

2. Rekebisha faili au folda maalum:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Tunapendekeza uweke editor yako iwe inarekebisha code moja kwa moja kwa Black kila unapohifadhi. Editors nyingi za kisasa zinaunga mkono hili kupitia extensions au plugins.

## Kuendesha Co-op Translator

Ili kuendesha Co-op Translator kwa kutumia Poetry kwenye mazingira yako, fuata hatua hizi:

1. Nenda kwenye folda unayotaka kufanya majaribio ya tafsiri au tengeneza folda ya muda kwa ajili ya majaribio.

2. Tekeleza amri ifuatayo. Badilisha `-l ko` na msimbo wa lugha unayotaka kutafsiri. Bendera ya `-d` inaashiria hali ya debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Hakikisha mazingira yako ya Poetry yamewashwa (poetry shell) kabla ya kuendesha amri.

## Changia lugha mpya

Tunakaribisha michango ya kuongeza msaada kwa lugha mpya. Kabla ya kufungua PR, tafadhali kamilisha hatua zilizo hapa chini ili kurahisisha ukaguzi.

1. Ongeza lugha kwenye font mapping
   - Hariri `src/co_op_translator/fonts/font_language_mappings.yml`
   - Ongeza kipengele chenye:
     - `code`: Msimbo wa lugha wa ISO (mfano, `vi`)
     - `name`: Jina la lugha linaloeleweka kirahisi
     - `font`: Fonti iliyopo kwenye `src/co_op_translator/fonts/` inayounga mkono maandishi ya lugha hiyo
     - `rtl`: `true` kama ni maandishi ya kulia kwenda kushoto, vinginevyo `false`

2. Jumuisha faili za fonti zinazohitajika (ikibidi)
   - Kama fonti mpya inahitajika, hakikisha leseni yake inaruhusu usambazaji wa open source
   - Ongeza faili ya fonti kwenye `src/co_op_translator/fonts/`

3. Hakiki kwa ndani
   - Endesha tafsiri kwa sampuli ndogo (Markdown, picha, na notebooks inapofaa)
   - Hakikisha matokeo yanaonekana vizuri, ikiwemo fonti na mpangilio wa RTL kama inahitajika

4. Sasisha nyaraka
   - Hakikisha lugha inaonekana kwenye `getting_started/supported-languages.md`
   - Hakuna mabadiliko yanayohitajika kwenye `README_languages_template.md`; inatengenezwa kutoka orodha ya lugha zinazoungwa mkono

5. Fungua PR
   - Eleza lugha iliyoongezwa na masuala yoyote ya fonti/leseni
   - Ambatanisha picha za matokeo yaliyotafsiriwa kama inawezekana

Mfano wa kipengele cha YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Walezi wa Mradi

### Muundo wa ujumbe wa commit na mkakati wa kuunganisha

Ili kuhakikisha historia ya commit ya mradi wetu ina uwazi na mpangilio, tunafuata muundo maalum wa ujumbe wa commit **kwa ujumbe wa mwisho wa commit** tunapotumia mkakati wa **Squash and Merge**.

PR inapounganishwa, commits zote za ndani zitaunganishwa kuwa commit moja. Ujumbe wa mwisho wa commit unapaswa kufuata muundo ulio hapa chini ili kudumisha historia safi na yenye mpangilio.

#### Muundo wa ujumbe wa commit (kwa squash and merge)

Tunatumia muundo huu kwa ujumbe wa commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Inaonyesha aina ya commit. Tunatumia aina zifuatazo:
  - `Docs`: Kwa masasisho ya nyaraka.
  - `Build`: Kwa mabadiliko yanayohusiana na mfumo wa kujenga au utegemezi, ikiwemo masasisho ya faili za mpangilio, CI workflows, au Dockerfile.
  - `Core`: Kwa mabadiliko kwenye utendaji wa msingi wa mradi, hasa yanayohusisha faili kwenye folda ya `src/co_op_translator/core`.

- **description**: Muhtasari mfupi wa mabadiliko.
- **PR number**: Namba ya pull request inayohusiana na commit.

**Mifano**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Kwa sasa, vianzio vya **`Docs`**, **`Core`**, na **`Build`** vinaongezwa moja kwa moja kwenye vichwa vya PR kulingana na lebo zilizowekwa kwenye source code iliyobadilishwa. Mradi lebo sahihi imewekwa, mara nyingi huhitaji kubadilisha kichwa cha PR mwenyewe. Unachotakiwa ni kuthibitisha kila kitu kiko sawa na kianzio kimeundwa ipasavyo.

#### Mkakati wa kuunganisha

Tunatumia **Squash and Merge** kama mkakati chaguo-msingi wa pull requests. Mkakati huu unahakikisha ujumbe wa commit unafuata muundo wetu, hata kama commits za ndani hazifanyi hivyo.

**Sababu**:

- Historia safi na ya mstari mmoja wa mradi.
- Ujumbe wa commit wenye mpangilio.
- Kupunguza kelele za commits ndogo (mfano, "fix typo").

Unapounganisha, hakikisha ujumbe wa mwisho wa commit unafuata muundo wa ujumbe wa commit ulioelezwa hapo juu.

**Mfano wa Squash and Merge**
Kama PR ina commits zifuatazo:

- `fix typo`
- `update README`
- `adjust formatting`

Zinapaswa kuunganishwa kuwa:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa binadamu wa kitaalamu. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.