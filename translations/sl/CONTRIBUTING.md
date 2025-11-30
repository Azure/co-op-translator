<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:35:19+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Prispevanje k Co-op Translator

Ta projekt sprejema prispevke in predloge. Večina prispevkov zahteva, da se strinjate z
Contributor License Agreement (CLA), s katerim izjavite, da imate pravico in dejansko dovolite,
da uporabljamo vaš prispevek. Za podrobnosti obiščite https://cla.opensource.microsoft.com.

Ko oddate pull request, bo CLA bot samodejno ugotovil, ali morate predložiti
CLA in ustrezno označil PR (npr. statusni pregled, komentar). Preprosto sledite navodilom,
ki jih poda bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

## Nastavitev razvojnega okolja

Za nastavitev razvojnega okolja za ta projekt priporočamo uporabo Poetry za upravljanje odvisnosti. Uporabljamo `pyproject.toml` za upravljanje odvisnosti projekta, zato za namestitev odvisnosti uporabite Poetry.

### Ustvarjanje virtualnega okolja

#### Z uporabo pip

```bash
python -m venv .venv
```

#### Z uporabo Poetry

```bash
poetry init
```

### Aktivacija virtualnega okolja

#### Za pip in Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Z uporabo Poetry

```bash
poetry shell
```

### Namestitev paketa in potrebnih paketov

#### Z uporabo Poetry (iz pyproject.toml)

```bash
poetry install
```

### Ročno testiranje

Pred oddajo PR je pomembno, da preizkusite funkcionalnost prevajanja z resnično dokumentacijo:

1. Ustvarite testno mapo v korenski mapi:
    ```bash
    mkdir test_docs
    ```

2. Kopirajte nekaj markdown dokumentacije in slik, ki jih želite prevesti, v testno mapo. Na primer:
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

5. Preverite prevedene datoteke v `test_docs/translations` in `test_docs/translated_images`, da potrdite:
   - Kakovost prevoda
   - Da so metapodatkovni komentarji pravilni
   - Da je izvirna struktura markdowna ohranjena
   - Da povezave in slike delujejo pravilno

To ročno testiranje pomaga zagotoviti, da vaše spremembe dobro delujejo v resničnih primerih.

### Okoljske spremenljivke

1. Ustvarite `.env` datoteko v korenski mapi tako, da kopirate priloženo `.env.template` datoteko.
1. Izpolnite okoljske spremenljivke po navodilih.

> [!TIP]
>
> ### Dodatne možnosti za razvojno okolje
>
> Poleg lokalnega zagona projekta lahko uporabite tudi GitHub Codespaces ali VS Code Dev Containers kot alternativno razvojno okolje.
>
> #### GitHub Codespaces
>
> Ta vzorce lahko zaženete virtualno z uporabo GitHub Codespaces brez dodatnih nastavitev.
>
> Gumb bo odprl spletno različico VS Code v vašem brskalniku:
>
> 1. Odprite predlogo (to lahko traja nekaj minut):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokalni zagon z VS Code Dev Containers
>
> ⚠️ Ta možnost deluje le, če ima vaš Docker Desktop dodeljenih vsaj 16 GB RAM-a. Če imate manj kot 16 GB RAM-a, lahko poskusite [GitHub Codespaces](../..) ali [lokalno nastavitev](../..).
>
> Sorodna možnost so VS Code Dev Containers, ki odprejo projekt v lokalnem VS Code z uporabo [Dev Containers razširitve](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Zaženite Docker Desktop (namestite ga, če še ni nameščen)
> 2. Odprite projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Slog kode

Za ohranjanje enotnega sloga kode v projektu uporabljamo [Black](https://github.com/psf/black) kot formatirnik Python kode. Black je nepopustljiv formatirnik, ki samodejno preoblikuje Python kodo, da ustreza Black slogu.

#### Konfiguracija

Black konfiguracija je določena v `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Namestitev Black

Black lahko namestite z uporabo Poetry (priporočeno) ali pip:

##### Z uporabo Poetry

Black se samodejno namesti ob nastavitvi razvojnega okolja:
```bash
poetry install
```

##### Z uporabo pip

Če uporabljate pip, lahko Black namestite neposredno:
```bash
pip install black
```

#### Uporaba Black

##### Z uporabo Poetry

1. Formatirajte vse Python datoteke v projektu:
    ```bash
    poetry run black .
    ```

2. Formatirajte določeno datoteko ali mapo:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Z uporabo pip

1. Formatirajte vse Python datoteke v projektu:
    ```bash
    black .
    ```

2. Formatirajte določeno datoteko ali mapo:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Priporočamo, da nastavite urejevalnik, da samodejno formatira kodo z Black ob shranjevanju. Večina sodobnih urejevalnikov to podpira preko razširitev ali vtičnikov.

## Zagon Co-op Translator

Za zagon Co-op Translator z uporabo Poetry v vašem okolju sledite tem korakom:

1. Pomaknite se v mapo, kjer želite izvajati prevajalske teste, ali ustvarite začasno mapo za testiranje.

2. Zaženite naslednji ukaz. Zamenjajte `-l ko` z jezikovno kodo, v kateri želite prevajati. Preklopnik `-d` pomeni način za odpravljanje napak.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pred zagonom ukaza poskrbite, da je vaše Poetry okolje aktivirano (poetry shell).

## Prispevajte nov jezik

Veselimo se prispevkov, ki dodajo podporo za nove jezike. Preden odprete PR, prosimo, da opravite spodnje korake za nemoten pregled.

1. Dodajte jezik v preslikavo pisav
   - Uredite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodajte vnos z:
     - `code`: ISO-podobna jezikovna koda (npr. `vi`)
     - `name`: Prijazno ime za prikaz
     - `font`: Pisava, ki je vključena v `src/co_op_translator/fonts/` in podpira pisavo
     - `rtl`: `true`, če je jezik desno-levo, sicer `false`

2. Vključite potrebne datoteke pisav (če je potrebno)
   - Če je potrebna nova pisava, preverite licenčno združljivost za odprtokodno distribucijo
   - Dodajte datoteko pisave v `src/co_op_translator/fonts/`

3. Lokalna verifikacija
   - Zaženite prevode za majhen vzorec (Markdown, slike in zvezke, kot je primerno)
   - Preverite, da se izhod pravilno prikaže, vključno s pisavami in morebitno RTL postavitvijo

4. Posodobite dokumentacijo
   - Prepričajte se, da je jezik naveden v `getting_started/supported-languages.md`
   - Spremembe v `getting_started/README_languages_template.md` niso potrebne; ta se generira iz seznama podprtih jezikov

5. Odprite PR
   - Opišite dodani jezik in morebitne posebnosti glede pisav/licenc
   - Priložite posnetke zaslona prevedenih izhodov, če je mogoče

Primer vnosa v YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testiranje novega jezika

Novi jezik lahko preizkusite z naslednjim ukazom:

```bash
# Ustvari in aktiviraj virtualno okolje
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Namesti razvojni paket
pip install -e .
# Zaženi prevajanje
translate -l "new_lang"
```

## Vzdrževalci

### Sporočilo commita in strategija združevanja

Za zagotovitev doslednosti in jasnosti v zgodovini commita projekta sledimo določenemu formatu sporočila commita **za končno sporočilo commita** pri uporabi strategije **Squash and Merge**.

Ko je pull request (PR) združen, se posamezni commiti združijo v en sam commit. Končno sporočilo commita naj sledi spodnjemu formatu za ohranjanje čiste in dosledne zgodovine.

#### Format sporočila commita (za squash and merge)

Uporabljamo naslednji format sporočil commita:

```bash
<type>: <description> (#<Številka PR>)
```

- **type**: Določa kategorijo commita. Uporabljamo naslednje tipe:
  - `Docs`: Za posodobitve dokumentacije.
  - `Build`: Za spremembe, povezane z gradbenim sistemom ali odvisnostmi, vključno z nastavitvenimi datotekami, CI poteki ali Dockerfile.
  - `Core`: Za spremembe jedra projekta ali funkcionalnosti, zlasti datotek v `src/co_op_translator/core` mapi.

- **description**: Kratek povzetek spremembe.
- **PR number**: Številka pull requesta, povezane s commitom.

**Primeri**:

- `Docs: Posodobitev navodil za namestitev za večjo jasnost (#50)`
- `Core: Izboljšano upravljanje prevajanja slik (#60)`

> [!NOTE]
> Trenutno se predpone **`Docs`**, **`Core`** in **`Build`** samodejno dodajo naslovom PR glede na oznake, uporabljene na spremenjeni kodi. Dokler je pravilna oznaka uporabljena, običajno ni potrebno ročno spreminjati naslova PR. Preverite le, da je vse pravilno in da je predpona ustrezno ustvarjena.

#### Strategija združevanja

Kot privzeto strategijo za pull requeste uporabljamo **Squash and Merge**. Ta strategija zagotavlja, da sporočila commitov sledijo našemu formatu, tudi če posamezni commiti tega ne storijo.

**Razlogi**:

- Čista, linearna zgodovina projekta.
- Doslednost v sporočilih commitov.
- Manj hrupa zaradi manjših commitov (npr. "popravek tipkarske napake").

Pri združevanju poskrbite, da končno sporočilo commita sledi zgoraj opisanemu formatu.

**Primer Squash and Merge**
Če PR vsebuje naslednje commite:

- `popravek tipkarske napake`
- `posodobitev README`
- `prilagoditev oblikovanja`

Naj bodo združeni v:
`Docs: Izboljšanje jasnosti in oblikovanja dokumentacije (#65)`

### Postopek izdaje

Ta razdelek opisuje najpreprostejši način za vzdrževalce, da objavijo novo izdajo Co-op Translatorja.

#### 1. Povišajte različico v `pyproject.toml`

1. Odločite se za naslednjo številko različice (sledimo semantičnemu verzioniranju: `MAJOR.MINOR.PATCH`).
2. Uredite `pyproject.toml` in posodobite polje `version` pod `[tool.poetry]`.
3. Odprite namenski pull request, ki spremeni samo različico (in morebitne samodejno posodobljene zaklenjene/metapodatkovne datoteke, če obstajajo).
4. Po pregledu uporabite **Squash and Merge** in poskrbite, da končno sporočilo commita sledi zgoraj opisanemu formatu.

#### 2. Ustvarite GitHub izdajo

1. Pojdite na stran repozitorija na GitHubu in odprite **Releases** → **Draft a new release**.
2. Ustvarite nov tag (npr. `v0.13.0`) iz veje `main`.
3. Nastavite naslov izdaje na isto različico (npr. `v0.13.0`).
4. Kliknite **Generate release notes**, da samodejno izpolnite dnevnik sprememb.
5. Po želji uredite besedilo (npr. za poudarjanje novo podprtih jezikov ali pomembnih sprememb).
6. Objavite izdajo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->