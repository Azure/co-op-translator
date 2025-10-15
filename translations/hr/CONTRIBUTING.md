<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T04:05:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hr"
}
-->
# Doprinos projektu Co-op Translator

Ovaj projekt otvoren je za doprinose i prijedloge. Većina doprinosa zahtijeva da prihvatite Contributor License Agreement (CLA) kojim potvrđujete da imate pravo i zapravo dajete dozvolu za korištenje vašeg doprinosa. Više informacija možete pronaći na https://cla.opensource.microsoft.com.

Kada pošaljete pull request, CLA bot će automatski provjeriti trebate li prihvatiti CLA i označiti PR na odgovarajući način (npr. statusna provjera, komentar). Slijedite upute koje vam bot daje. Ovo trebate napraviti samo jednom za sve repozitorije koji koriste naš CLA.

## Postavljanje razvojne okoline

Za postavljanje razvojne okoline preporučujemo korištenje Poetry za upravljanje ovisnostima. Koristimo `pyproject.toml` za upravljanje ovisnostima projekta, pa za instalaciju ovisnosti trebate koristiti Poetry.

### Kreiranje virtualnog okruženja

#### Korištenje pip-a

```bash
python -m venv .venv
```

#### Korištenje Poetry

```bash
poetry init
```

### Aktivacija virtualnog okruženja

#### Za pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Korištenje Poetry

```bash
poetry shell
```

### Instalacija paketa i potrebnih ovisnosti

#### Korištenje Poetry (iz pyproject.toml)

```bash
poetry install
```

### Ručno testiranje

Prije slanja PR-a važno je testirati funkcionalnost prevođenja na stvarnoj dokumentaciji:

1. Kreirajte testni direktorij u korijenskom direktoriju:
    ```bash
    mkdir test_docs
    ```

2. Kopirajte neku markdown dokumentaciju i slike koje želite prevesti u testni direktorij. Na primjer:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instalirajte paket lokalno:
    ```bash
    pip install -e .
    ```

4. Pokrenite Co-op Translator na vašim testnim dokumentima:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Provjerite prevedene datoteke u `test_docs/translations` i `test_docs/translated_images` kako biste provjerili:
   - Kvalitetu prijevoda
   - Ispravnost metapodataka u komentarima
   - Očuvanu originalnu markdown strukturu
   - Ispravnost linkova i slika

Ovo ručno testiranje pomaže da budete sigurni da vaše promjene dobro funkcioniraju u stvarnim situacijama.

### Varijable okoline

1. Kreirajte `.env` datoteku u korijenskom direktoriju kopiranjem predloška `.env.template`.
1. Popunite varijable okoline prema uputama.

> [!TIP]
>
> ### Dodatne opcije za razvojnu okolinu
>
> Osim lokalnog pokretanja projekta, možete koristiti i GitHub Codespaces ili VS Code Dev Containers kao alternativne opcije za razvojnu okolinu.
>
> #### GitHub Codespaces
>
> Ove primjere možete pokrenuti virtualno koristeći GitHub Codespaces bez dodatnih postavki ili instalacija.
>
> Gumb će otvoriti VS Code u vašem pregledniku:
>
> 1. Otvorite predložak (može potrajati nekoliko minuta):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Lokalno pokretanje pomoću VS Code Dev Containers
>
> ⚠️ Ova opcija radi samo ako je vašem Docker Desktopu dodijeljeno najmanje 16 GB RAM-a. Ako imate manje od 16 GB RAM-a, možete koristiti [GitHub Codespaces opciju](../..) ili [postaviti lokalno](../..).
>
> Srodna opcija je VS Code Dev Containers, koja otvara projekt u vašem lokalnom VS Code-u koristeći [Dev Containers ekstenziju](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Pokrenite Docker Desktop (instalirajte ga ako već nije instaliran)
> 2. Otvorite projekt:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Stil koda

Koristimo [Black](https://github.com/psf/black) kao formatirač Python koda kako bismo održali dosljedan stil kroz cijeli projekt. Black je beskompromisan alat koji automatski preformatira Python kod prema Black standardu.

#### Konfiguracija

Black konfiguracija definirana je u našem `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacija Black-a

Black možete instalirati pomoću Poetry-a (preporučeno) ili pip-a:

##### Korištenje Poetry-a

Black se automatski instalira prilikom postavljanja razvojne okoline:
```bash
poetry install
```

##### Korištenje pip-a

Ako koristite pip, Black možete instalirati direktno:
```bash
pip install black
```

#### Korištenje Black-a

##### S Poetry-em

1. Formatirajte sve Python datoteke u projektu:
    ```bash
    poetry run black .
    ```

2. Formatirajte određenu datoteku ili direktorij:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### S pip-om

1. Formatirajte sve Python datoteke u projektu:
    ```bash
    black .
    ```

2. Formatirajte određenu datoteku ili direktorij:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Preporučujemo da postavite svoj editor da automatski formatira kod s Black-om prilikom spremanja. Većina modernih editora to podržava putem ekstenzija ili dodataka.

## Pokretanje Co-op Translatora

Za pokretanje Co-op Translatora pomoću Poetry-a u vašoj okolini, slijedite ove korake:

1. Idite u direktorij u kojem želite testirati prijevod ili kreirajte privremenu mapu za testiranje.

2. Pokrenite sljedeću naredbu. Zamijenite `-l ko` kodom jezika na koji želite prevesti. Oznaka `-d` označava debug način rada.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Prije pokretanja naredbe provjerite da je vaš Poetry okoliš aktiviran (poetry shell).

## Dodavanje novog jezika

Otvoreni smo za doprinose koji dodaju podršku za nove jezike. Prije otvaranja PR-a, molimo vas da dovršite korake u nastavku radi lakše recenzije.

1. Dodajte jezik u mapiranje fontova
   - Uredite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodajte unos s:
     - `code`: ISO-sličan kod jezika (npr. `vi`)
     - `name`: Prikazno ime za ljude
     - `font`: Font koji se nalazi u `src/co_op_translator/fonts/` i podržava pismo
     - `rtl`: `true` ako je desno-na-lijevo, inače `false`

2. Dodajte potrebne font datoteke (ako je potrebno)
   - Ako je potreban novi font, provjerite licencu za open source distribuciju
   - Dodajte font datoteku u `src/co_op_translator/fonts/`

3. Lokalna provjera
   - Pokrenite prijevod na malom uzorku (Markdown, slike i bilježnice po potrebi)
   - Provjerite da se izlaz ispravno prikazuje, uključujući fontove i RTL raspored ako je primjenjivo

4. Ažurirajte dokumentaciju
   - Provjerite da se jezik pojavljuje u `getting_started/supported-languages.md`
   - Nema potrebe mijenjati `README_languages_template.md`; on se generira iz popisa podržanih jezika

5. Otvorite PR
   - Opišite dodani jezik i sve font/licencne napomene
   - Priložite snimke zaslona prikazanih rezultata ako je moguće

Primjer YAML unosa:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Održavatelji

### Format poruke prilikom commita i strategija spajanja

Radi dosljednosti i jasnoće u povijesti commita projekta, koristimo određeni format poruke **za završni commit** prilikom korištenja strategije **Squash and Merge**.

Kada se pull request (PR) spoji, pojedinačni commiti se spajaju u jedan commit. Završna poruka commita treba slijediti format u nastavku radi uredne i dosljedne povijesti.

#### Format poruke commita (za squash and merge)

Koristimo sljedeći format za poruke commita:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Određuje kategoriju commita. Koristimo sljedeće tipove:
  - `Docs`: Za ažuriranja dokumentacije.
  - `Build`: Za promjene vezane uz build sustav ili ovisnosti, uključujući ažuriranja konfiguracijskih datoteka, CI workflowa ili Dockerfile-a.
  - `Core`: Za izmjene temeljne funkcionalnosti projekta, posebno onih u `src/co_op_translator/core` direktoriju.

- **description**: Kratki sažetak promjene.
- **PR number**: Broj pull requesta povezanog s commitom.

**Primjeri**:

- `Docs: Ažurirane upute za instalaciju radi jasnoće (#50)`
- `Core: Poboljšano rukovanje prijevodom slika (#60)`

> [!NOTE]
> Trenutno se **`Docs`**, **`Core`** i **`Build`** prefiksi automatski dodaju naslovima PR-a na temelju oznaka primijenjenih na izmijenjeni izvorni kod. Dok je ispravna oznaka primijenjena, obično ne trebate ručno mijenjati naslov PR-a. Samo provjerite da je sve ispravno i da je prefiks generiran kako treba.

#### Strategija spajanja

Koristimo **Squash and Merge** kao zadanu strategiju za pull requestove. Ova strategija osigurava da poruke commita slijede naš format, čak i ako pojedinačni commiti to ne čine.

**Razlozi**:

- Čista, linearna povijest projekta.
- Dosljednost u porukama commita.
- Manje "šuma" od manjih commitova (npr. "ispravljen tipfeler").

Prilikom spajanja, provjerite da završna poruka commita slijedi gore opisani format.

**Primjer Squash and Merge**
Ako PR sadrži sljedeće commitove:

- `ispravljen tipfeler`
- `ažuriran README`
- `prilagođen format`

Treba ih spojiti u:
`Docs: Poboljšana jasnoća i formatiranje dokumentacije (#65)`

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.