<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:47:21+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Hozzájárulás a Co-op Translatorhoz

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájárulás esetén szükséges, hogy elfogadd a Contributor License Agreementet (CLA), amelyben kijelented, hogy jogodban áll, és ténylegesen meg is adod nekünk a jogokat a hozzájárulásod felhasználására. Részletekért látogass el ide: https://cla.opensource.microsoft.com.

Amikor pull requestet (PR) küldesz be, egy CLA bot automatikusan ellenőrzi, hogy szükséges-e CLA-t kitöltened, és ennek megfelelően jelöli a PR-t (pl. státuszellenőrzés, komment). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned minden olyan repóban, amely a mi CLA-nkat használja.

## Fejlesztői környezet beállítása

A fejlesztői környezet beállításához ehhez a projekthez a Poetry használatát javasoljuk a függőségek kezelésére. A projekt függőségeit a `pyproject.toml` fájlban kezeljük, ezért a telepítéshez is a Poetry-t használd.

### Virtuális környezet létrehozása

#### pip használatával

```bash
python -m venv .venv
```

#### Poetry használatával

```bash
poetry init
```

### A virtuális környezet aktiválása

#### pip és Poetry esetén is

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

Mielőtt PR-t küldesz be, fontos, hogy valós dokumentációval teszteld a fordítási funkciót:

1. Hozz létre egy teszt könyvtárat a gyökérkönyvtárban:
    ```bash
    mkdir test_docs
    ```

2. Másolj néhány markdown dokumentumot és képet, amit le szeretnél fordítani, ebbe a teszt könyvtárba. Például:
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

5. Ellenőrizd a lefordított fájlokat a `test_docs/translations` és `test_docs/translated_images` mappákban, hogy megbizonyosodj róla:
   - A fordítás minősége megfelelő
   - A metaadat kommentek helyesek
   - Az eredeti markdown szerkezet megmaradt
   - A linkek és képek megfelelően működnek

Ez a manuális tesztelés segít abban, hogy a módosításaid a valós helyzetekben is jól működjenek.

### Környezeti változók

1. Hozz létre egy `.env` fájlt a gyökérkönyvtárban a mellékelt `.env.template` fájl másolásával.
1. Töltsd ki a környezeti változókat az útmutató szerint.

> [!TIP]
>
> ### További fejlesztői környezet lehetőségek
>
> A projekt helyi futtatása mellett használhatod a GitHub Codespaces-t vagy a VS Code Dev Containers-t is alternatív fejlesztői környezetként.
>
> #### GitHub Codespaces
>
> A mintákat virtuálisan is futtathatod a GitHub Codespaces segítségével, további beállítások nélkül.
>
> A gomb megnyit egy böngészőben futó, webes VS Code példányt:
>
> 1. Nyisd meg a sablont (ez néhány percet igénybe vehet):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Helyi futtatás VS Code Dev Containers használatával
>
> ⚠️ Ez az opció csak akkor működik, ha a Docker Desktop legalább 16 GB RAM-ot kapott. Ha kevesebb, mint 16 GB RAM-od van, próbáld ki a [GitHub Codespaces opciót](../..) vagy [állítsd be helyileg](../..).
>
> Egy kapcsolódó lehetőség a VS Code Dev Containers, amely megnyitja a projektet a helyi VS Code-ban a [Dev Containers bővítmény](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) segítségével:
>
> 1. Indítsd el a Docker Desktopot (ha még nincs telepítve, telepítsd)
> 2. Nyisd meg a projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kódstílus

A [Black](https://github.com/psf/black) Python kódformázót használjuk, hogy egységes kódstílust tartsunk fenn a projektben. A Black egy kompromisszummentes kódformázó, amely automatikusan átalakítja a Python kódot a Black stílusának megfelelően.

#### Beállítás

A Black konfigurációját a `pyproject.toml` fájlban adjuk meg:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black telepítése

A Black-et telepítheted Poetry-vel (ajánlott) vagy pip-pel:

##### Poetry használatával

A Black automatikusan települ, amikor beállítod a fejlesztői környezetet:
```bash
poetry install
```

##### pip használatával

Ha pip-et használsz, közvetlenül is telepítheted a Black-et:
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

##### pip-pel

1. Formázd az összes Python fájlt a projektben:
    ```bash
    black .
    ```

2. Formázz egy adott fájlt vagy könyvtárat:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Javasoljuk, hogy állítsd be a szerkesztődet úgy, hogy mentéskor automatikusan formázza a kódot Black-kel. A legtöbb modern szerkesztő támogatja ezt bővítményekkel vagy pluginekkel.

## Co-op Translator futtatása

A Co-op Translator futtatásához Poetry használatával a következő lépéseket kövesd:

1. Navigálj abba a könyvtárba, ahol a fordítási teszteket szeretnéd elvégezni, vagy hozz létre egy ideiglenes mappát teszteléshez.

2. Futtasd az alábbi parancsot. Cseréld le a `-l ko` részt arra a nyelvkódra, amelyre fordítani szeretnél. A `-d` kapcsoló a debug módot jelzi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Győződj meg róla, hogy a Poetry környezeted aktív (poetry shell), mielőtt futtatod a parancsot.

## Új nyelv hozzáadása

Szívesen fogadunk olyan hozzájárulásokat, amelyek új nyelvek támogatását adják hozzá. Mielőtt PR-t nyitsz, kérjük, végezd el az alábbi lépéseket a gördülékeny átnézés érdekében.

1. Add hozzá a nyelvet a betűtípus-térképhez
   - Szerkeszd a `src/co_op_translator/fonts/font_language_mappings.yml` fájlt
   - Adj hozzá egy bejegyzést az alábbiakkal:
     - `code`: ISO-szerű nyelvkód (pl. `vi`)
     - `name`: Emberbarát megjelenítési név
     - `font`: Egy olyan betűtípus, amely a `src/co_op_translator/fonts/` mappában található, és támogatja a karakterkészletet
     - `rtl`: `true`, ha jobbról balra íródik, egyébként `false`

2. Szükséges betűtípusfájlok hozzáadása (ha szükséges)
   - Ha új betűtípus szükséges, ellenőrizd, hogy a licenc lehetővé teszi-e a nyílt forráskódú terjesztést
   - Add hozzá a betűtípusfájlt a `src/co_op_translator/fonts/` mappához

3. Helyi ellenőrzés
   - Futtass fordítást egy kis mintán (Markdown, képek, notebookok, ha szükséges)
   - Ellenőrizd, hogy a kimenet helyesen jelenik-e meg, beleértve a betűtípusokat és az esetleges RTL elrendezést

4. Dokumentáció frissítése
   - Győződj meg róla, hogy a nyelv megjelenik a `getting_started/supported-languages.md` fájlban
   - A `README_languages_template.md`-hez nem kell módosítás; ez automatikusan generálódik a támogatott listából

5. PR megnyitása
   - Írd le, milyen nyelvet adtál hozzá, és milyen betűtípus/licencelési szempontokat vettél figyelembe
   - Ha lehet, csatolj képernyőképeket a megjelenített kimenetekről

Példa YAML bejegyzés:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Karbantartók

### Commit üzenet és összevonási stratégia

A projekt commit történetének egységessége és átláthatósága érdekében egy meghatározott commit üzenet formátumot követünk **a végső commit üzenethez**, amikor a **Squash and Merge** stratégiát használjuk.

Amikor egy pull request (PR) összevonásra kerül, az egyes commitok egyetlen commitba lesznek összegyúrva. A végső commit üzenetnek az alábbi formátumot kell követnie, hogy a történet tiszta és egységes maradjon.

#### Commit üzenet formátum (squash and merge esetén)

Az alábbi formátumot használjuk a commit üzenetekhez:

```bash
<type>: <description> (#<PR number>)
```

- **type**: A commit kategóriáját jelöli. Az alábbi típusokat használjuk:
  - `Docs`: Dokumentációs frissítésekhez.
  - `Build`: A build rendszerhez vagy függőségekhez kapcsolódó változásokhoz, beleértve a konfigurációs fájlokat, CI workflow-kat vagy a Dockerfile-t.
  - `Core`: A projekt alapvető funkcióinak vagy szolgáltatásainak módosításaihoz, különösen a `src/co_op_translator/core` könyvtárban lévő fájlokat érintően.

- **description**: A változtatás rövid összefoglalása.
- **PR number**: A commithez tartozó pull request száma.

**Példák**:

- `Docs: Telepítési útmutató frissítése az érthetőség kedvéért (#50)`
- `Core: Képfeldolgozás javítása a fordítás során (#60)`

> [!NOTE]
> Jelenleg a **`Docs`**, **`Core`** és **`Build`** előtagokat automatikusan hozzáadjuk a PR címéhez a módosított forráskódhoz rendelt címkék alapján. Amíg a megfelelő címke ki van választva, általában nem kell manuálisan módosítanod a PR címét. Csak ellenőrizd, hogy minden helyes, és az előtag megfelelően generálódott.

#### Összevonási stratégia

Alapértelmezett stratégiánk a **Squash and Merge** a pull requestekhez. Ez biztosítja, hogy a commit üzenetek megfeleljenek a formátumunknak, még akkor is, ha az egyes commitok nem.

**Indokok**:

- Tiszta, lineáris projekt történet.
- Egységes commit üzenetek.
- Kevesebb zavaró, apró commit (pl. "fix typo").

Összevonáskor ügyelj rá, hogy a végső commit üzenet megfeleljen a fent leírt formátumnak.

**Squash and Merge példa**
Ha egy PR a következő commitokat tartalmazza:

- `fix typo`
- `update README`
- `adjust formatting`

Ezeket így kell összegyúrni:
`Docs: Dokumentáció érthetőségének és formázásának javítása (#65)`

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, eredeti nyelvű dokumentum tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.