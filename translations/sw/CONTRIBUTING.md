<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:40:54+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sw"
}
-->
# Kuchangia Co-op Translator

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji ukakubali
Mkataba wa Leseni ya Mchango (CLA) unaothibitisha kuwa una haki, na kwa kweli unaturuhusu
kutumia mchango wako. Kwa maelezo, tembelea https://cla.opensource.microsoft.com.

Unapowasilisha pull request, bot ya CLA itagundua moja kwa moja kama unahitaji kutoa
CLA na itaweka alama inayofaa kwenye PR (mfano, ukaguzi wa hali, maoni). Fuata tu maelekezo
yanayotolewa na bot. Hii unahitaji kufanya mara moja tu kwa repos zote zinazotumia CLA yetu.

## Kuandaa Mazingira ya Maendeleo

Ili kuandaa mazingira ya maendeleo kwa mradi huu, tunapendekeza kutumia Poetry kusimamia utegemezi. Tunatumia `pyproject.toml` kusimamia utegemezi wa mradi, hivyo basi, kusanidi utegemezi, unapaswa kutumia Poetry.

### Unda mazingira ya virtual

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

### Kusakinisha Package na Package zinazohitajika

#### Kutumia Poetry (kutoka pyproject.toml)

```bash
poetry install
```

### Kupima kwa mikono

Kabla ya kuwasilisha PR, ni muhimu kupima utendakazi wa tafsiri kwa nyaraka halisi:

1. Unda saraka ya majaribio kwenye saraka kuu:
    ```bash
    mkdir test_docs
    ```

2. Nakili baadhi ya nyaraka za markdown na picha unazotaka kutafsiri kwenye saraka ya majaribio. Kwa mfano:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Sakinisha package eneo lako:
    ```bash
    pip install -e .
    ```

4. Endesha Co-op Translator kwenye nyaraka zako za majaribio:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Angalia faili zilizotafsiriwa katika `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` faili.
1. Jaza mabadiliko ya mazingira kama inavyoelekezwa.

> [!TIP]
>
> ### Chaguzi za ziada za mazingira ya maendeleo
>
> Mbali na kuendesha mradi eneo lako, unaweza pia kutumia GitHub Codespaces au VS Code Dev Containers kama njia mbadala ya kuandaa mazingira ya maendeleo.
>
> #### GitHub Codespaces
>
> Unaweza kuendesha sampuli hizi kwa njia ya mtandao kwa kutumia GitHub Codespaces bila haja ya mipangilio au usanidi wa ziada.
>
> Kitufe kitafungua toleo la VS Code lililo kwenye kivinjari chako:
>
> 1. Fungua templeti (hii inaweza kuchukua dakika kadhaa):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kuendesha Eneo Lako Ukitumia VS Code Dev Containers
>
> ⚠️ Chaguo hili litafanya kazi tu ikiwa Docker Desktop yako imetengwa angalau GB 16 ya RAM. Ukipata chini ya GB 16 ya RAM, unaweza jaribu [chaguo la GitHub Codespaces](../..) au [kuandaa eneo lako](../..).
>
> Chaguo linalohusiana ni VS Code Dev Containers, ambalo litaifungua mradi katika VS Code yako ya eneo lako kwa kutumia [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Anzisha Docker Desktop (iisakinishe kama bado haijasakinishwa)
> 2. Fungua mradi:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Mtindo wa Msimbo

Tunatumia [Black](https://github.com/psf/black) kama mpangiliaji wa msimbo wa Python ili kudumisha mtindo thabiti wa msimbo katika mradi. Black ni mpangiliaji msimbo usio na huruma unaobadilisha msimbo wa Python moja kwa moja ili uendane na mtindo wa Black.

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

Black husakinishwa moja kwa moja unapoandaa mazingira ya maendeleo:
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

1. Panga faili zote za Python kwenye mradi:
    ```bash
    poetry run black .
    ```

2. Panga faili au saraka maalum:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Kwa pip

1. Panga faili zote za Python kwenye mradi:
    ```bash
    black .
    ```

2. Panga faili au saraka maalum:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Tunapendekeza kuanzisha mhariri wako kufomati msimbo kiotomatiki kwa Black unapoihifadhi. Wahariri wengi wa kisasa wanaunga mkono hili kupitia nyongeza au programu-jalizi.

## Kuendesha Co-op Translator

Ili kuendesha Co-op Translator kwa kutumia Poetry katika mazingira yako, fuata hatua hizi:

1. Nenda kwenye saraka unayotaka kufanya majaribio ya tafsiri au unda folda ya muda kwa madhumuni ya majaribio.

2. Endesha amri ifuatayo. Bendera `-l ko` with the language code you wish to translate into. The `-d` inaonyesha hali ya ufuatiliaji hitilafu.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Hakikisha mazingira yako ya Poetry yamewashwa (poetry shell) kabla ya kuendesha amri.

## Watunzaji

### Ujumbe wa commit na Mkakati wa Kuunganisha

Ili kuhakikisha muendelezo na uwazi katika historia ya commit ya mradi wetu, tunafuata muundo maalum wa ujumbe wa commit **kwa ujumbe wa mwisho wa commit** tunapotumia mkakati wa **Squash and Merge**.

Unapounganisha pull request (PR), commits binafsi zitachanganywa kuwa commit moja. Ujumbe wa mwisho wa commit unapaswa kufuata muundo ulio hapa chini ili kudumisha historia safi na thabiti.

#### Muundo wa ujumbe wa commit (kwa squash and merge)

Tunatumia muundo ufuatao kwa ujumbe wa commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Inaeleza aina ya commit. Tunatumia aina zifuatazo:
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

**Kiarifu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuna dhamana kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.