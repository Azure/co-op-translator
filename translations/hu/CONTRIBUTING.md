<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:03:58+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Hozzájárulás a Co-op Translatorhoz

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement (CLA) licencszerződést, amelyben kijelented, hogy jogod van a hozzájárulásod használatára, és ténylegesen meg is adod nekünk a felhasználási jogokat. Részletekért látogass el a https://cla.opensource.microsoft.com oldalra.

Amikor pull requestet nyújtasz be, egy CLA bot automatikusan megállapítja, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően jelöli meg a PR-t (pl. státusz ellenőrzés, komment). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned az összes CLA-t használó repóban.

## Fejlesztői környezet beállítása

A fejlesztői környezet beállításához ezt a projektet ajánlott Poetry-vel kezelni a függőségeket. A projekt függőségeit a `pyproject.toml` fájlban kezeljük, ezért a függőségek telepítéséhez Poetry-t kell használnod.

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

#### Pip és Poetry esetén egyaránt

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

#### Poetry használatával (a pyproject.toml alapján)

```bash
poetry install
```

### Manuális tesztelés

PR beküldése előtt fontos, hogy valós dokumentációval teszteld a fordítási funkciót:

1. Hozz létre egy teszt könyvtárat a gyökérkönyvtárban:
    ```bash
    mkdir test_docs
    ```

2. Másolj néhány markdown dokumentációt és képet, amelyeket le szeretnél fordítani a teszt könyvtárba. Például:
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

5. Ellenőrizd a lefordított fájlokat a `test_docs/translations` és `test_docs/translated_images` mappákban, hogy meggyőződj:
   - A fordítás minőségéről
   - A metaadat kommentek helyességéről
   - Az eredeti markdown szerkezet megőrzéséről
   - A linkek és képek megfelelő működéséről

Ez a manuális tesztelés segít biztosítani, hogy a változtatásaid jól működnek valós környezetben.

### Környezeti változók

1. Hozz létre egy `.env` fájlt a gyökérkönyvtárban a mellékelt `.env.template` fájl másolásával.
2. Töltsd ki a környezeti változókat az útmutatás szerint.

> [!TIP]
>
> ### További fejlesztői környezet opciók
>
> A projekt helyi futtatása mellett használhatsz GitHub Codespaces-t vagy VS Code Dev Containers-t is alternatív fejlesztői környezetként.
>
> #### GitHub Codespaces
>
> Virtuálisan futtathatod ezt a mintaprojektet GitHub Codespaces segítségével, további beállítás vagy konfiguráció nélkül.
>
> A gomb megnyit egy böngészőben futó webes VS Code példányt:
>
> 1. Nyisd meg a sablont (ez néhány percet igénybe vehet):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Helyi futtatás VS Code Dev Containers használatával
>
> ⚠️ Ez az opció csak akkor működik, ha a Docker Desktop legalább 16 GB RAM-ot kapott. Ha kevesebb mint 16 GB RAM áll rendelkezésre, próbáld meg a [GitHub Codespaces opciót](../..) vagy [állítsd be helyileg](../..).
>
> Egy kapcsolódó lehetőség a VS Code Dev Containers, amely megnyitja a projektet a helyi VS Code-ban a [Dev Containers kiterjesztés](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) segítségével:
>
> 1. Indítsd el a Docker Desktopot (ha még nincs telepítve, telepítsd)
> 2. Nyisd meg a projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kódstílus

A projektben a [Black](https://github.com/psf/black) Python kódformázót használjuk, hogy egységes kódstílust tartsunk fenn. A Black egy kompromisszummentes kódformázó, amely automatikusan átalakítja a Python kódot a Black kódstílusnak megfelelően.

#### Konfiguráció

A Black konfigurációját a `pyproject.toml` fájlban adjuk meg:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black telepítése

Black-et telepítheted Poetry-vel (ajánlott) vagy pip-pel:

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
> Ajánlott beállítani a szerkesztődet úgy, hogy mentéskor automatikusan formázza a kódot Black-kel. A legtöbb modern szerkesztő támogatja ezt bővítmények vagy pluginok segítségével.

## Co-op Translator futtatása

A Co-op Translator futtatásához Poetry használatával a környezetedben, kövesd az alábbi lépéseket:

1. Navigálj abba a könyvtárba, ahol a fordítási teszteket szeretnéd végezni, vagy hozz létre egy ideiglenes mappát teszteléshez.

2. Futtasd a következő parancsot. Cseréld le a `-l ko` részt arra a nyelvkódra, amelyre fordítani szeretnél. A `-d` kapcsoló a hibakeresési módot jelzi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Győződj meg róla, hogy a Poetry környezeted aktiválva van (poetry shell), mielőtt futtatod a parancsot.

## Új nyelv hozzáadása

Szívesen fogadunk hozzájárulásokat új nyelvek támogatásához. PR megnyitása előtt kérjük, végezd el az alábbi lépéseket a gördülékeny átvizsgálás érdekében.

1. Add hozzá a nyelvet a betűtípus leképezéshez
   - Szerkeszd a `src/co_op_translator/fonts/font_language_mappings.yml` fájlt
   - Adj hozzá egy bejegyzést az alábbi adatokkal:
     - `code`: ISO-szerű nyelvkód (pl. `vi`)
     - `name`: Emberbarát megjelenítési név
     - `font`: Egy olyan betűtípus, amely a `src/co_op_translator/fonts/` mappában található, és támogatja az adott írást
     - `rtl`: `true`, ha jobbról balra íródó, különben `false`

2. Szükséges betűtípus fájlok hozzáadása (ha kell)
   - Ha új betűtípus szükséges, ellenőrizd a licenc kompatibilitását nyílt forrású terjesztéshez
   - Add hozzá a betűtípus fájlt a `src/co_op_translator/fonts/` mappához

3. Helyi ellenőrzés
   - Futtass fordítást egy kis mintán (Markdown, képek és notebookok a szükség szerint)
   - Ellenőrizd, hogy a kimenet helyesen jelenik meg, beleértve a betűtípusokat és az esetleges jobbról balra írást

4. Dokumentáció frissítése
   - Győződj meg róla, hogy a nyelv szerepel a `getting_started/supported-languages.md` fájlban
   - A `getting_started/README_languages_template.md` fájlt nem kell módosítani, mert az a támogatott listából generálódik

5. PR megnyitása
   - Írd le a hozzáadott nyelvet és a betűtípus/licenc megfontolásokat
   - Ha lehet, csatolj képernyőképeket a megjelenített eredményekről

Példa YAML bejegyzés:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Az új nyelv tesztelése

Az új nyelvet az alábbi paranccsal tesztelheted:

```bash
# Hozzon létre és aktiváljon egy virtuális környezetet
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Telepítse a fejlesztői csomagot
pip install -e .
# Futtassa a fordítást
translate -l "new_lang"
```

## Karbantartók

### Commit üzenet és Merge stratégia

A projekt konzisztens és átlátható commit történetének biztosítása érdekében egy meghatározott commit üzenet formátumot követünk **a végső commit üzenethez** a **Squash and Merge** stratégia használatakor.

Amikor egy pull request (PR) összeolvad, az egyes commitok egyetlen commitba lesznek összesűrítve. A végső commit üzenetnek az alábbi formátumot kell követnie a tiszta és egységes történet érdekében.

#### Commit üzenet formátum (squash and merge esetén)

A commit üzenetekhez a következő formátumot használjuk:

```bash
<type>: <description> (#<PR szám>)
```

- **type**: A commit kategóriáját jelöli. A következő típusokat használjuk:
  - `Docs`: Dokumentáció frissítésekhez.
  - `Build`: A build rendszerrel vagy függőségekkel kapcsolatos változtatásokhoz, beleértve a konfigurációs fájlokat, CI munkafolyamatokat vagy a Dockerfile-t.
  - `Core`: A projekt alapvető funkcióinak vagy jellemzőinek módosításához, különösen a `src/co_op_translator/core` könyvtárban lévő fájlok esetén.

- **description**: A változtatás tömör összefoglalása.
- **PR szám**: A commithoz kapcsolódó pull request száma.

**Példák**:

- `Docs: Telepítési útmutató frissítése a jobb érthetőségért (#50)`
- `Core: Képfordítás kezelési javítása (#60)`

> [!NOTE]
> Jelenleg a **`Docs`**, **`Core`** és **`Build`** előtagokat automatikusan hozzáadja a PR címéhez a módosított forráskódhoz rendelt címkék alapján. Amennyiben a megfelelő címke fel van véve, általában nem kell manuálisan módosítanod a PR címet. Csak ellenőrizd, hogy minden helyes és az előtag megfelelően generálódott.

#### Merge stratégia

Alapértelmezettként a **Squash and Merge** stratégiát használjuk a pull requestekhez. Ez a stratégia biztosítja, hogy a commit üzenetek megfeleljenek a formátumnak, még akkor is, ha az egyes commitok nem.

**Előnyök**:

- Tiszta, lineáris projekt történet.
- Konzisztens commit üzenetek.
- Kevesebb zaj a kisebb commitokból (pl. "elírás javítása").

Merge során győződj meg róla, hogy a végső commit üzenet megfelel a fent leírt commit üzenet formátumnak.

**Példa Squash and Merge-re**
Ha egy PR a következő commitokat tartalmazza:

- `elírás javítása`
- `README frissítése`
- `formázás igazítása`

Ezek összevonva így néznek ki:
`Docs: Dokumentáció érthetőségének és formázásának javítása (#65)`

### Kiadási folyamat

Ez a rész a legegyszerűbb módját írja le a Co-op Translator új kiadásának közzétételéhez karbantartók számára.

#### 1. Verziószám növelése a `pyproject.toml`-ban

1. Döntsd el a következő verziószámot (szemantikus verziózást követünk: `MAJOR.MINOR.PATCH`).
2. Szerkeszd a `pyproject.toml` fájlt, és frissítsd a `[tool.poetry]` szekcióban a `version` mezőt.
3. Nyiss egy külön pull requestet, amely csak a verziószámot (és esetlegesen automatikusan frissített lock/meta fájlokat) módosítja.
4. Átvizsgálás után használd a **Squash and Merge**-t, és győződj meg róla, hogy a végső commit üzenet megfelel a fent leírt formátumnak.

#### 2. GitHub Release létrehozása

1. Lépj a GitHub repó oldalára, és nyisd meg a **Releases** → **Draft a new release** menüpontot.
2. Hozz létre egy új taget (például `v0.13.0`) a `main` ágról.
3. Állítsd be a kiadás címét ugyanarra a verzióra (például `v0.13.0`).
4. Kattints a **Generate release notes** gombra, hogy automatikusan kitöltse a változásnaplót.
5. Szükség szerint szerkeszd a szöveget (például kiemelve az újonnan támogatott nyelveket vagy fontos változásokat).
6. Tedd közzé a kiadást.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->