<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:41:26+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Hozzájárulás a Co-op Translatorhoz

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement (CLA) licencszerződést, amelyben kijelented, hogy jogodban áll, és ténylegesen megadod számunkra a jogot a hozzájárulásod felhasználására. Részletekért látogass el a https://cla.opensource.microsoft.com oldalra.

Amikor pull request-et nyújtasz be, egy CLA bot automatikusan megállapítja, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően jelzi a PR-t (pl. állapot ellenőrzés, komment). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned az összes, CLA-t használó repóban.

## Fejlesztői környezet beállítása

A fejlesztői környezet beállításához ebben a projektben a Poetry használatát ajánljuk a függőségek kezelésére. A projekt függőségeit a `pyproject.toml` kezeli, ezért a függőségek telepítéséhez Poetry-t kell használnod.

### Virtuális környezet létrehozása

#### Pip használatával

```bash
python -m venv .venv
```

#### Poetry használatával

```bash
poetry init
```

### A virtuális környezet aktiválása

#### Pip és Poetry esetén is

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry használatával

```bash
poetry shell
```

### A csomag és a szükséges csomagok telepítése

#### Poetry használatával (pyproject.toml alapján)

```bash
poetry install
```

### Manuális tesztelés

PR benyújtása előtt fontos, hogy valós dokumentációval teszteld a fordítási funkciót:

1. Hozz létre egy teszt könyvtárat a gyökérkönyvtárban:
    ```bash
    mkdir test_docs
    ```

2. Másolj néhány fordítandó markdown dokumentumot és képet a teszt könyvtárba. Például:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Telepítsd a csomagot helyileg:
    ```bash
    pip install -e .
    ```

4. Futtasd a Co-op Translator-t a teszt dokumentumaidon:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Ellenőrizd a lefordított fájlokat a `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` fájlban.
1. Töltsd ki a környezeti változókat az útmutatás szerint.

> [!TIP]
>
> ### További fejlesztői környezeti lehetőségek
>
> A projekt helyi futtatása mellett használhatsz GitHub Codespaces-t vagy VS Code Dev Containers-t is alternatív fejlesztői környezetként.
>
> #### GitHub Codespaces
>
> Virtuálisan futtathatod a mintákat GitHub Codespaces segítségével, további beállítás vagy konfiguráció nélkül.
>
> A gomb megnyit egy böngészőben futó webes VS Code példányt:
>
> 1. Nyisd meg a sablont (ez néhány percet vehet igénybe):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Helyi futtatás VS Code Dev Containers használatával
>
> ⚠️ Ez a lehetőség csak akkor működik, ha Docker Desktop legalább 16 GB RAM-ot kapott. Ha kevesebb mint 16 GB RAM áll rendelkezésre, próbáld meg a [GitHub Codespaces lehetőséget](../..) vagy [állítsd be helyileg](../..).
>
> Egy kapcsolódó lehetőség a VS Code Dev Containers, amely megnyitja a projektet a helyi VS Code-ban a [Dev Containers bővítmény](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) használatával:
>
> 1. Indítsd el a Docker Desktop-ot (telepítsd, ha még nincs telepítve)
> 2. Nyisd meg a projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kódstílus

A projekt egységes kódstílusának fenntartásához a [Black](https://github.com/psf/black) Python kódformázót használjuk. A Black egy kompromisszumokat nem ismerő formázó, amely automatikusan átalakítja a Python kódot a Black kódstílusnak megfelelőre.

#### Konfiguráció

A Black konfigurációját a `pyproject.toml` fájlban adjuk meg:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black telepítése

Black telepíthető Poetry-vel (ajánlott) vagy pip-pel:

##### Poetry használatával

Black automatikusan települ a fejlesztői környezet beállításakor:
```bash
poetry install
```

##### Pip használatával

Ha pip-et használsz, közvetlenül telepítheted a Black-et:
```bash
pip install black
```

#### Black használata

##### Poetry-vel

1. Formázd az összes Python fájlt a projektben:
    ```bash
    poetry run black .
    ```

2. Formázz egy adott fájlt vagy könyvtárat:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Pip-pel

1. Formázd az összes Python fájlt a projektben:
    ```bash
    black .
    ```

2. Formázz egy adott fájlt vagy könyvtárat:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Ajánljuk, hogy állítsd be a szerkesztődet úgy, hogy mentéskor automatikusan formázza a kódot Black-kel. A legtöbb modern szerkesztő támogatja ezt bővítmények vagy pluginok segítségével.

## Co-op Translator futtatása

A Co-op Translator futtatásához a Poetry segítségével a következő lépéseket kövesd:

1. Navigálj abba a könyvtárba, ahol a fordítási teszteket szeretnéd végezni, vagy hozz létre egy ideiglenes mappát a teszteléshez.

2. Futtasd az alábbi parancsot. A `-l ko` with the language code you wish to translate into. The `-d` kapcsoló a hibakeresési módot jelzi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Győződj meg róla, hogy a Poetry környezeted aktiválva van (poetry shell), mielőtt futtatod a parancsot.

## Karbantartók

### Commit üzenet és Merge stratégia

A projektünk commit történetének következetessége és tisztasága érdekében egy meghatározott commit üzenet formátumot használunk **a végső commit üzenethez** a **Squash and Merge** stratégia alkalmazásakor.

Amikor egy pull request (PR) összeolvad, az egyes commitok összeolvadnak egyetlen commitba. A végső commit üzenetnek az alábbi formátumot kell követnie a tiszta és következetes történet érdekében.

#### Commit üzenet formátum (squash and merge esetén)

A commit üzenetekhez a következő formátumot használjuk:

```bash
<type>: <description> (#<PR number>)
```

- **type**: A commit kategóriáját határozza meg. A következő típusokat használjuk:
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

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.