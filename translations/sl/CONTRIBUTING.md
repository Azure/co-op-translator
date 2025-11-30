<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T04:08:10+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Prispevanje k Co-op Translator

Ta projekt sprejema prispevke in predloge. Večina prispevkov zahteva, da se strinjate s Contributor License Agreement (CLA), s katero potrjujete, da imate pravico in dejansko podeljujete pravice za uporabo vašega prispevka. Več informacij najdete na https://cla.opensource.microsoft.com.

Ko oddate pull request, bo CLA bot samodejno preveril, ali morate podati CLA, in ustrezno označil PR (npr. status check, komentar). Preprosto sledite navodilom bota. To morate storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

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

Pred oddajo PR je pomembno, da funkcionalnost prevajanja preizkusite na dejanski dokumentaciji:

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

4. Zaženite Co-op Translator na svojih testnih dokumentih:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Preverite prevedene datoteke v `test_docs/translations` in `test_docs/translated_images` ter preverite:
   - Kakovost prevoda
   - Pravilnost metapodatkov v komentarjih
   - Ohranjeno izvorno markdown strukturo
   - Pravilno delovanje povezav in slik

To ročno testiranje pomaga zagotoviti, da vaše spremembe delujejo tudi v dejanskih primerih.

### Okoljske spremenljivke

1. Ustvarite datoteko `.env` v korenski mapi tako, da kopirate priloženo datoteko `.env.template`.
1. Izpolnite okoljske spremenljivke po navodilih.

> [!TIP]
>
> ### Dodatne možnosti za razvojno okolje
>
> Poleg lokalnega zagona projekta lahko uporabite tudi GitHub Codespaces ali VS Code Dev Containers kot alternativo za nastavitev razvojnega okolja.
>
> #### GitHub Codespaces
>
> Vzorce lahko zaženete virtualno z uporabo GitHub Codespaces brez dodatnih nastavitev.
>
> Gumb bo odprl spletno različico VS Code v vašem brskalniku:
>
> 1. Odprite predlogo (to lahko traja nekaj minut):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Lokalni zagon z VS Code Dev Containers
>
> ⚠️ Ta možnost deluje le, če je vašemu Docker Desktop dodeljenih vsaj 16 GB RAM-a. Če imate manj kot 16 GB RAM-a, lahko poskusite možnost [GitHub Codespaces](../..) ali [nastavite lokalno](../..).
>
> Sorodna možnost je VS Code Dev Containers, ki odpre projekt v vašem lokalnem VS Code z uporabo [Dev Containers razširitve](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Zaženite Docker Desktop (namestite, če še ni nameščen)
> 2. Odprite projekt:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Slog kode

Uporabljamo [Black](https://github.com/psf/black) kot formatirnik Python kode za ohranjanje enotnega sloga kode v projektu. Black je nepopustljiv formatirnik, ki samodejno preoblikuje Python kodo v skladu s slogom Black.

#### Konfiguracija

Konfiguracija za Black je določena v našem `pyproject.toml`:

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

##### S Poetry

1. Formatirajte vse Python datoteke v projektu:
    ```bash
    poetry run black .
    ```

2. Formatirajte določeno datoteko ali mapo:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### S pip

1. Formatirajte vse Python datoteke v projektu:
    ```bash
    black .
    ```

2. Formatirajte določeno datoteko ali mapo:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Priporočamo, da nastavite urejevalnik, da samodejno formatira kodo z Black ob shranjevanju. Večina sodobnih urejevalnikov to podpira z razširitvami ali vtičniki.

## Zagon Co-op Translator

Za zagon Co-op Translator z uporabo Poetry v vašem okolju sledite tem korakom:

1. Pomaknite se v mapo, kjer želite izvajati prevajalske teste ali ustvarite začasno mapo za testiranje.

2. Izvedite naslednji ukaz. Zamenjajte `-l ko` s kodo jezika, v katerega želite prevesti. Zastavica `-d` pomeni način razhroščevanja.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pred zagonom ukaza preverite, da je vaše Poetry okolje aktivirano (poetry shell).

## Prispevanje novega jezika

Veseli bomo prispevkov, ki dodajo podporo za nove jezike. Preden odprete PR, dokončajte spodnje korake za lažji pregled.

1. Dodajte jezik v mapiranje pisav
   - Uredite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodajte vnos z:
     - `code`: ISO-podobna koda jezika (npr. `vi`)
     - `name`: Prijazno prikazno ime
     - `font`: Pisava, ki je v `src/co_op_translator/fonts/` in podpira pisavo jezika
     - `rtl`: `true` če je desno-proti-levi, sicer `false`

2. Dodajte potrebne datoteke pisav (če je potrebno)
   - Če je potrebna nova pisava, preverite združljivost licence za odprtokodno distribucijo
   - Dodajte datoteko pisave v `src/co_op_translator/fonts/`

3. Lokalna preveritev
   - Zaženite prevode za majhen vzorec (Markdown, slike in zvezki po potrebi)
   - Preverite, da se izhod pravilno prikazuje, vključno s pisavami in morebitno RTL postavitvijo

4. Posodobite dokumentacijo
   - Preverite, da je jezik naveden v `getting_started/supported-languages.md`
   - Spremembe v `README_languages_template.md` niso potrebne; ta se generira iz seznama podprtih jezikov

5. Odprite PR
   - Opišite dodani jezik in morebitne pisave/licenčne podrobnosti
   - Priložite posnetke zaslona prikazanih rezultatov, če je mogoče

Primer YAML vnosa:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Skrbniki

### Sporočilo ob commit-u in strategija združevanja

Za doslednost in jasnost v zgodovini commit-ov projekta sledimo določenemu formatu sporočila commit-a **za končno sporočilo commit-a** pri uporabi strategije **Squash and Merge**.

Ko je pull request (PR) združen, se posamezni commiti združijo v en commit. Končno sporočilo commit-a naj sledi spodnjemu formatu za ohranjanje čiste in dosledne zgodovine.

#### Format sporočila commit-a (za squash and merge)

Uporabljamo naslednji format za sporočila commit-ov:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Določa kategorijo commit-a. Uporabljamo naslednje tipe:
  - `Docs`: Za posodobitve dokumentacije.
  - `Build`: Za spremembe, povezane z gradnjo ali odvisnostmi, vključno s konfiguracijskimi datotekami, CI workflow-i ali Dockerfile.
  - `Core`: Za spremembe v osnovni funkcionalnosti ali funkcijah projekta, zlasti v datotekah v mapi `src/co_op_translator/core`.

- **description**: Kratek povzetek spremembe.
- **PR number**: Številka pull request-a, povezanega s commit-om.

**Primeri**:

- `Docs: Posodobljena navodila za namestitev (#50)`
- `Core: Izboljšano obravnavanje prevajanja slik (#60)`

> [!NOTE]
> Trenutno se predpone **`Docs`**, **`Core`** in **`Build`** samodejno dodajo naslovom PR glede na oznake, ki so dodeljene spremenjeni izvorni kodi. Če je pravilna oznaka dodeljena, običajno ni treba ročno spreminjati naslova PR. Preverite le, da je vse pravilno in da je predpona ustrezno generirana.

#### Strategija združevanja

Uporabljamo **Squash and Merge** kot privzeto strategijo za pull request-e. Ta strategija zagotavlja, da sporočila commit-ov sledijo našemu formatu, tudi če posamezni commiti ne.

**Razlogi**:

- Čista, linearna zgodovina projekta.
- Doslednost v sporočilih commit-ov.
- Manj šuma zaradi manjših commit-ov (npr. "popravljena tipkarska napaka").

Pri združevanju poskrbite, da končno sporočilo commit-a sledi zgoraj opisanemu formatu.

**Primer Squash and Merge**
Če PR vsebuje naslednje commite:

- `popravljena tipkarska napaka`
- `posodobljen README`
- `prilagojeno oblikovanje`

Se združijo v:
`Docs: Izboljšana jasnost in oblikovanje dokumentacije (#65)`

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.