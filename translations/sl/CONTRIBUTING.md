<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-13T01:26:15+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Prispevanje k Co-op Translator

Ta projekt pozdravlja prispevke in predloge. Večina prispevkov zahteva, da se strinjate s Pogodbo o prispevanju (CLA), ki navaja, da imate pravico in dejansko podeljujete pravice za uporabo vašega prispevka. Za podrobnosti obiščite https://cla.opensource.microsoft.com.

Ko oddate zahtevo za združitev (pull request), bo bot CLA samodejno določil, ali morate zagotoviti CLA in ustrezno okrasil PR (npr. preverjanje stanja, komentar). Preprosto sledite navodilom, ki jih zagotavlja bot. To boste morali storiti le enkrat v vseh repozitorijih, ki uporabljajo naš CLA.

## Nastavitev razvojnega okolja

Za nastavitev razvojnega okolja za ta projekt priporočamo uporabo Poetry za upravljanje odvisnosti. Uporabljamo `pyproject.toml` za upravljanje projektnih odvisnosti, zato za namestitev odvisnosti uporabite Poetry.

### Ustvarjanje virtualnega okolja

#### Uporaba pip

```bash
python -m venv .venv
```

#### Uporaba Poetry

```bash
poetry init
```

### Aktiviranje virtualnega okolja

#### Za pip in Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Uporaba Poetry

```bash
poetry shell
```

### Namestitev paketa in potrebnih paketov

#### Uporaba Poetry (iz pyproject.toml)

```bash
poetry install
```

### Ročno testiranje

Pred oddajo PR je pomembno testirati funkcionalnost prevajanja z resnično dokumentacijo:

1. Ustvarite testni imenik v korenskem imeniku:
    ```bash
    mkdir test_docs
    ```

2. Kopirajte nekaj markdown dokumentacije in slik, ki jih želite prevesti, v testni imenik. Na primer:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Namestite paket lokalno:
    ```bash
    pip install -e .
    ```

4. Zaženite Co-op Translator na vaših testnih dokumentih:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Preverite prevedene datoteke v `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` datoteki.
1. Izpolnite okoljske spremenljivke, kot je navedeno.

> [!TIP]
>
> ### Dodatne možnosti razvojnega okolja
>
> Poleg lokalnega zagona projekta lahko uporabite tudi GitHub Codespaces ali VS Code Dev Containers za alternativno nastavitev razvojnega okolja.
>
> #### GitHub Codespaces
>
> Te vzorce lahko virtualno zaženete z uporabo GitHub Codespaces, brez dodatnih nastavitev ali konfiguracij.
>
> Gumb bo odprl spletno različico VS Code v vašem brskalniku:
>
> 1. Odprite predlogo (to lahko traja nekaj minut):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokalno zaganjanje z uporabo VS Code Dev Containers
>
> ⚠️ Ta možnost bo delovala le, če je vašemu Docker Desktop dodeljenih vsaj 16 GB RAM-a. Če imate manj kot 16 GB RAM-a, lahko poskusite možnost [GitHub Codespaces](../..) ali [nastavite lokalno](../..).
>
> Sorodna možnost je VS Code Dev Containers, ki bo odprla projekt v vašem lokalnem VS Code z uporabo [Dev Containers razširitve](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Zaženite Docker Desktop (namestite ga, če še ni nameščen)
> 2. Odprite projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

### Slog kode

Uporabljamo [Black](https://github.com/psf/black) kot naš Python oblikovalnik kode za ohranjanje doslednega sloga kode v projektu. Black je nepopustljiv oblikovalnik kode, ki samodejno preoblikuje Python kodo, da ustreza slogu kode Black.

#### Konfiguracija

Konfiguracija Black je določena v našem `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Namestitev Black

Black lahko namestite z uporabo Poetry (priporočeno) ali pip:

##### Uporaba Poetry

Black se samodejno namesti, ko nastavite razvojno okolje:
```bash
poetry install
```

##### Uporaba pip

Če uporabljate pip, lahko Black namestite neposredno:
```bash
pip install black
```

#### Uporaba Black

##### Z Poetry

1. Oblikujte vse Python datoteke v projektu:
    ```bash
    poetry run black .
    ```

2. Oblikujte določeno datoteko ali imenik:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Z pip

1. Oblikujte vse Python datoteke v projektu:
    ```bash
    black .
    ```

2. Oblikujte določeno datoteko ali imenik:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Priporočamo nastavitev vašega urejevalnika, da samodejno oblikuje kodo z Black ob shranjevanju. Večina sodobnih urejevalnikov to podpira preko razširitev ali vtičnikov.

## Zagon Co-op Translator

Za zagon Co-op Translator z uporabo Poetry v vašem okolju sledite tem korakom:

1. Pomaknite se do imenika, kjer želite izvesti teste prevajanja ali ustvarite začasno mapo za testne namene.

2. Izvedite naslednji ukaz. Zamenjajte `-l ko` with the language code you wish to translate into. The `-d` zastavica označuje način odpravljanja napak.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pred izvajanjem ukaza poskrbite, da je vaše Poetry okolje aktivirano (poetry shell).

## Vzdrževalci

### Sporočilo o potrditvi in strategija združevanja

Da zagotovimo doslednost in jasnost v zgodovini potrditev našega projekta, sledimo specifičnemu formatu sporočila o potrditvi **za končno sporočilo o potrditvi** pri uporabi strategije **Squash and Merge**.

Ko je zahteva za združitev (PR) združena, bodo posamezne potrditve združene v eno samo potrditev. Končno sporočilo o potrditvi naj sledi spodnjemu formatu za ohranjanje čiste in dosledne zgodovine.

#### Format sporočila o potrditvi (za squash and merge)

Uporabljamo naslednji format za sporočila o potrditvi:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Določa kategorijo potrditve. Uporabljamo naslednje tipe:
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

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.