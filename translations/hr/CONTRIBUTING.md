<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:44:20+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hr"
}
-->
# Contributing to Co-op Translator

Ovaj projekt pozdravlja doprinose i prijedloge. Većina doprinosa zahtijeva da se složite s Contributor License Agreement (CLA) u kojem izjavljujete da imate pravo i zaista dajete nam prava za korištenje vašeg doprinosa. Za detalje posjetite https://cla.opensource.microsoft.com.

Kada pošaljete pull request, CLA bot će automatski provjeriti trebate li dostaviti CLA i označiti PR na odgovarajući način (npr. status check, komentar). Jednostavno slijedite upute koje vam bot daje. Ovo je potrebno napraviti samo jednom za sve repozitorije koji koriste naš CLA.

## Postavljanje razvojne okoline

Za postavljanje razvojne okoline za ovaj projekt preporučujemo korištenje Poetry za upravljanje ovisnostima. Koristimo `pyproject.toml` za upravljanje ovisnostima projekta, stoga za instalaciju ovisnosti trebate koristiti Poetry.

### Kreiranje virtualnog okruženja

#### Korištenje pip-a

```bash
python -m venv .venv
```

#### Korištenje Poetry-ja

```bash
poetry init
```

### Aktiviranje virtualnog okruženja

#### Za pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Korištenje Poetry-ja

```bash
poetry shell
```

### Instalacija paketa i potrebnih paketa

#### Korištenje Poetry-ja (iz pyproject.toml)

```bash
poetry install
```

### Ručno testiranje

Prije slanja PR-a važno je testirati funkcionalnost prijevoda s pravom dokumentacijom:

1. Kreirajte testni direktorij u root direktoriju:
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

4. Pokrenite Co-op Translator na vašim test dokumentima:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Provjerite prevedene datoteke u `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` datoteci.
1. Ispunite varijable okoline prema uputama.

> [!TIP]
>
> ### Dodatne opcije za razvojnu okolinu
>
> Osim pokretanja projekta lokalno, možete koristiti i GitHub Codespaces ili VS Code Dev Containers kao alternativni način postavljanja razvojne okoline.
>
> #### GitHub Codespaces
>
> Možete pokrenuti ove primjere virtualno koristeći GitHub Codespaces bez dodatnih postavki ili konfiguracija.
>
> Gumb će otvoriti web-bazirani VS Code u vašem pregledniku:
>
> 1. Otvorite predložak (ovo može potrajati nekoliko minuta):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokalno pokretanje koristeći VS Code Dev Containers
>
> ⚠️ Ova opcija radi samo ako vaš Docker Desktop ima dodijeljeno barem 16 GB RAM-a. Ako imate manje od 16 GB RAM-a, možete pokušati s [GitHub Codespaces opcijom](../..) ili [postaviti lokalno](../..).
>
> Srodna opcija su VS Code Dev Containers, koji otvaraju projekt u vašem lokalnom VS Code-u koristeći [Dev Containers ekstenziju](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Pokrenite Docker Desktop (ako nije instaliran, instalirajte ga)
> 2. Otvorite projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stil koda

Koristimo [Black](https://github.com/psf/black) kao formatir za Python kod kako bismo održali konzistentan stil koda kroz cijeli projekt. Black je nepopustljivi formatir koji automatski preformatira Python kod da bi odgovarao Black stilu koda.

#### Konfiguracija

Black konfiguracija je specificirana u našem `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacija Black-a

Black možete instalirati koristeći ili Poetry (preporučeno) ili pip:

##### Korištenje Poetry-ja

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
> Preporučujemo da postavite vaš editor da automatski formatira kod pomoću Black pri spremanju. Većina modernih editora to podržava kroz ekstenzije ili dodatke.

## Pokretanje Co-op Translatora

Za pokretanje Co-op Translatora koristeći Poetry u vašoj okolini, slijedite ove korake:

1. Idite u direktorij gdje želite testirati prijevode ili kreirajte privremenu mapu za testiranje.

2. Pokrenite sljedeću naredbu. Zamijenite `-l ko` with the language code you wish to translate into. The `-d` zastavicu koja označava debug način rada.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Provjerite je li vaša Poetry okolina aktivirana (poetry shell) prije pokretanja naredbe.

## Održavatelji

### Poruka commita i strategija spajanja

Kako bismo osigurali dosljednost i jasnoću u povijesti commit-a našeg projekta, koristimo određeni format poruke commita **za završnu poruku commita** pri korištenju **Squash and Merge** strategije.

Kada se pull request (PR) spoji, pojedinačni commit-i će se spojiti u jedan commit. Završna poruka commita treba slijediti donji format kako bi se održala čista i konzistentna povijest.

#### Format poruke commita (za squash and merge)

Koristimo sljedeći format za poruke commita:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Određuje kategoriju commita. Koristimo sljedeće tipove:
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

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.