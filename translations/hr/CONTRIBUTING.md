<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T12:30:28+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hr"
}
-->
# Doprinos projektu Co-op Translator

Ovaj projekt pozdravlja doprinose i prijedloge. Većina doprinosa zahtijeva da se složite s Ugovorom o licenci za doprinositelje (CLA) kojim izjavljujete da imate pravo i doista nam dajete prava za korištenje vašeg doprinosa. Za detalje posjetite https://cla.opensource.microsoft.com.

Kada pošaljete pull request, CLA bot će automatski utvrditi trebate li dostaviti CLA i odgovarajuće označiti PR (npr. status provjere, komentar). Jednostavno slijedite upute koje daje bot. Ovo je potrebno napraviti samo jednom za sve repozitorije koji koriste naš CLA.

## Postavljanje razvojne okoline

Za postavljanje razvojne okoline za ovaj projekt preporučujemo korištenje Poetry za upravljanje ovisnostima. Koristimo `pyproject.toml` za upravljanje ovisnostima projekta, stoga za instalaciju ovisnosti trebate koristiti Poetry.

### Kreiranje virtualnog okruženja

#### Korištenje pip-a

```bash
python -m venv .venv
```

#### Korištenje Poetry-a

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

#### Korištenje Poetry-a

```bash
poetry shell
```

### Instalacija paketa i potrebnih ovisnosti

#### Korištenje Poetry-a (iz pyproject.toml)

```bash
poetry install
```

### Ručno testiranje

Prije slanja PR-a važno je testirati funkcionalnost prijevoda s pravom dokumentacijom:

1. Kreirajte direktorij za testiranje u korijenskom direktoriju:
    ```bash
    mkdir test_docs
    ```

2. Kopirajte neke markdown dokumente i slike koje želite prevesti u testni direktorij. Na primjer:
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

5. Provjerite prevedene datoteke u `test_docs/translations` i `test_docs/translated_images` kako biste potvrdili:
   - Kvalitetu prijevoda
   - Ispravnost komentara s metapodacima
   - Očuvanje originalne markdown strukture
   - Ispravan rad linkova i slika

Ovo ručno testiranje pomaže osigurati da vaše promjene dobro funkcioniraju u stvarnim scenarijima.

### Varijable okoline

1. Kreirajte `.env` datoteku u korijenskom direktoriju kopiranjem predloška `.env.template`.
1. Ispunite varijable okoline prema uputama.

> [!TIP]
>
> ### Dodatne opcije za razvojnu okolinu
>
> Osim lokalnog pokretanja projekta, možete koristiti i GitHub Codespaces ili VS Code Dev Containers kao alternativne razvojne okoline.
>
> #### GitHub Codespaces
>
> Ove primjere možete pokrenuti virtualno koristeći GitHub Codespaces bez dodatnih postavki.
>
> Gumb će otvoriti VS Code u web pregledniku:
>
> 1. Otvorite predložak (može potrajati nekoliko minuta):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokalno pokretanje koristeći VS Code Dev Containers
>
> ⚠️ Ova opcija radi samo ako vaš Docker Desktop ima dodijeljeno barem 16 GB RAM-a. Ako imate manje od 16 GB RAM-a, možete isprobati [GitHub Codespaces opciju](../..) ili [postaviti lokalno](../..).
>
> Srodna opcija su VS Code Dev Containers, koji otvaraju projekt u vašem lokalnom VS Code-u koristeći [Dev Containers ekstenziju](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Pokrenite Docker Desktop (ako nije instaliran, instalirajte ga)
> 2. Otvorite projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stil kodiranja

Koristimo [Black](https://github.com/psf/black) kao formatter za Python kod kako bismo održali dosljedan stil koda u projektu. Black je nepopustljiv formatter koji automatski preformatira Python kod da zadovolji Black stil.

#### Konfiguracija

Black konfiguracija je definirana u našem `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacija Black-a

Black možete instalirati koristeći Poetry (preporučeno) ili pip:

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

##### S Poetry-jem

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
> Preporučujemo da postavite vaš editor da automatski formatira kod s Black prilikom spremanja. Većina modernih editora to podržava kroz ekstenzije ili dodatke.

## Pokretanje Co-op Translatora

Za pokretanje Co-op Translatora koristeći Poetry u vašoj okolini, slijedite ove korake:

1. Idite u direktorij u kojem želite testirati prijevode ili kreirajte privremeni folder za testiranje.

2. Pokrenite sljedeću naredbu. Zamijenite `-l ko` s kodom jezika na koji želite prevesti. Zastavica `-d` označava debug način rada.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Provjerite je li vaša Poetry okolina aktivirana (poetry shell) prije pokretanja naredbe.

## Doprinos novom jeziku

Pozdravljamo doprinose koji dodaju podršku za nove jezike. Prije otvaranja PR-a, molimo dovršite sljedeće korake za glatku recenziju.

1. Dodajte jezik u mapiranje fontova
   - Uredite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Dodajte unos s:
     - `code`: ISO-slični kod jezika (npr. `vi`)
     - `name`: Prikazni naziv za ljude
     - `font`: Font koji dolazi s `src/co_op_translator/fonts/` i podržava taj skript
     - `rtl`: `true` ako je pisanje s desna na lijevo, inače `false`

2. Uključite potrebne font datoteke (ako je potrebno)
   - Ako je potreban novi font, provjerite licencnu kompatibilnost za open source distribuciju
   - Dodajte font datoteku u `src/co_op_translator/fonts/`

3. Lokalna provjera
   - Pokrenite prijevode na malom uzorku (Markdown, slike i bilježnice prema potrebi)
   - Provjerite ispravno prikazivanje, uključujući fontove i RTL raspored ako je primjenjivo

4. Ažurirajte dokumentaciju
   - Provjerite da je jezik naveden u `getting_started/supported-languages.md`
   - Nema potrebe za izmjenama u `getting_started/README_languages_template.md`; on se generira iz liste podržanih jezika

5. Otvorite PR
   - Opisajte dodani jezik i eventualne napomene o fontovima/licencama
   - Po mogućnosti priložite snimke zaslona prevedenih rezultata

Primjer YAML unosa:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testiranje novog jezika

Novu jezičnu podršku možete testirati pokretanjem sljedeće naredbe:

```bash
# Kreirajte i aktivirajte virtualno okruženje
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalirajte razvojni paket
pip install -e .
# Pokrenite prijevod
translate -l "new_lang"
```

## Održavatelji

### Poruka commita i strategija spajanja

Kako bismo osigurali dosljednost i jasnoću u povijesti commita projekta, koristimo specifičan format poruke commita **za konačnu poruku commita** prilikom korištenja **Squash and Merge** strategije.

Kada se pull request spoji, pojedinačni commit-i se spajaju u jedan commit. Konačna poruka commita treba slijediti format ispod radi uredne i dosljedne povijesti.

#### Format poruke commita (za squash and merge)

Koristimo sljedeći format za poruke commita:

```bash
<type>: <description> (#<PR broj>)
```

- **type**: Kategorija commita. Koristimo sljedeće tipove:
  - `Docs`: Za izmjene u dokumentaciji.
  - `Build`: Za promjene vezane uz build sustav ili ovisnosti, uključujući konfiguracijske datoteke, CI workflow-e ili Dockerfile.
  - `Core`: Za izmjene u osnovnoj funkcionalnosti ili značajkama projekta, posebno one u `src/co_op_translator/core` direktoriju.

- **description**: Kratki sažetak promjene.
- **PR number**: Broj pull requesta povezanog s commitom.

**Primjeri**:

- `Docs: Ažuriraj upute za instalaciju radi jasnoće (#50)`
- `Core: Poboljšaj rukovanje prijevodom slika (#60)`

> [!NOTE]
> Trenutno se prefiksi **`Docs`**, **`Core`** i **`Build`** automatski dodaju naslovima PR-ova na temelju oznaka primijenjenih na izmijenjeni izvorni kod. Dok god je ispravna oznaka primijenjena, obično nije potrebno ručno mijenjati naslov PR-a. Samo provjerite da je sve ispravno i da je prefiks generiran.

#### Strategija spajanja

Kao zadanu strategiju za pull requestove koristimo **Squash and Merge**. Ova strategija osigurava da poruke commita slijede naš format, čak i ako pojedinačni commit-i to ne čine.

**Razlozi**:

- Čista, linearna povijest projekta.
- Dosljednost u porukama commita.
- Smanjenje buke od manjih commit-a (npr. "popravi tipfeler").

Prilikom spajanja, osigurajte da konačna poruka commita slijedi gore opisani format.

**Primjer Squash and Merge**
Ako PR sadrži sljedeće commit-e:

- `popravi tipfeler`
- `ažuriraj README`
- `prilagodi formatiranje`

Treba ih spojiti u:
`Docs: Poboljšaj jasnoću i formatiranje dokumentacije (#65)`

### Proces izdavanja verzije

Ovaj odjeljak opisuje najjednostavniji način za održavatelje da objave novu verziju Co-op Translatora.

#### 1. Povećajte verziju u `pyproject.toml`

1. Odlučite sljedeći broj verzije (pratimo semantičko verzioniranje: `MAJOR.MINOR.PATCH`).
2. Uredite `pyproject.toml` i ažurirajte polje `version` pod `[tool.poetry]`.
3. Otvorite poseban pull request koji mijenja samo verziju (i eventualne automatski ažurirane lock/metapodatke, ako postoje).
4. Nakon pregleda, koristite **Squash and Merge** i osigurajte da konačna poruka commita slijedi gore opisani format.

#### 2. Kreirajte GitHub izdanje (Release)

1. Idite na GitHub stranicu repozitorija i otvorite **Releases** → **Draft a new release**.
2. Kreirajte novi tag (npr. `v0.13.0`) iz `main` grane.
3. Postavite naslov izdanja na isti broj verzije (npr. `v0.13.0`).
4. Kliknite **Generate release notes** za automatsko popunjavanje promjena.
5. Po želji uredite tekst (npr. istaknite novo podržane jezike ili važne promjene).
6. Objavite izdanje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->