<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:43:47+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sr"
}
-->
# Doprinos Co-op Translator-u

Ovaj projekat pozdravlja doprinose i sugestije. Većina doprinosa zahteva da se složite sa  
Contributor License Agreement (CLA) koji potvrđuje da imate pravo i zaista nam dajete  
prava za korišćenje vašeg doprinosa. Za detalje, posetite https://cla.opensource.microsoft.com.

Kada pošaljete pull request, CLA bot će automatski utvrditi da li treba da dostavite  
CLA i odgovarajuće označiti PR (npr. status provera, komentar). Jednostavno pratite uputstva  
koja daje bot. Ovo je potrebno uraditi samo jednom za sve repozitorijume koji koriste naš CLA.

## Podešavanje razvojne sredine

Za podešavanje razvojne sredine za ovaj projekat, preporučujemo korišćenje Poetry za upravljanje zavisnostima. Koristimo `pyproject.toml` za upravljanje zavisnostima projekta, pa je za instalaciju zavisnosti potrebno koristiti Poetry.

### Kreiranje virtuelnog okruženja

#### Korišćenje pip-a

```bash
python -m venv .venv
```

#### Korišćenje Poetry-ja

```bash
poetry init
```

### Aktiviranje virtuelnog okruženja

#### Za pip i Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Korišćenje Poetry-ja

```bash
poetry shell
```

### Instalacija paketa i potrebnih zavisnosti

#### Korišćenje Poetry-ja (iz pyproject.toml)

```bash
poetry install
```

### Ručno testiranje

Pre nego što pošaljete PR, važno je da testirate funkcionalnost prevoda na stvarnoj dokumentaciji:

1. Kreirajte test direktorijum u korenskom direktorijumu:
    ```bash
    mkdir test_docs
    ```

2. Kopirajte markdown dokumentaciju i slike koje želite da prevedete u test direktorijum. Na primer:
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

5. Proverite prevedene fajlove u `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` fajlu.
1. Popunite promenljive okruženja prema uputstvu.

> [!TIP]
>
> ### Dodatne opcije za razvojnu sredinu
>
> Pored pokretanja projekta lokalno, možete koristiti i GitHub Codespaces ili VS Code Dev Containers kao alternativno rešenje za razvojnu sredinu.
>
> #### GitHub Codespaces
>
> Možete virtuelno pokrenuti ove primere koristeći GitHub Codespaces bez potrebe za dodatnim podešavanjima.
>
> Dugme će otvoriti VS Code instancu u vašem pregledaču:
>
> 1. Otvorite šablon (može potrajati nekoliko minuta):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokalno pokretanje koristeći VS Code Dev Containers
>
> ⚠️ Ova opcija funkcioniše samo ako vaš Docker Desktop ima dodeljeno najmanje 16 GB RAM-a. Ako imate manje od 16 GB RAM-a, možete probati [GitHub Codespaces opciju](../..) ili [podesiti lokalno](../..).
>
> Srodna opcija su VS Code Dev Containers, koji otvaraju projekat u vašem lokalnom VS Code koristeći [Dev Containers ekstenziju](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Pokrenite Docker Desktop (instalirajte ako već nije instaliran)
> 2. Otvorite projekat:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stil koda

Koristimo [Black](https://github.com/psf/black) kao Python formatter da bismo održali konzistentan stil koda u projektu. Black je rigorozan formatter koji automatski preformatira Python kod da bude u skladu sa Black stilom.

#### Konfiguracija

Black konfiguracija je definisana u našem `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalacija Black-a

Black možete instalirati koristeći Poetry (preporučeno) ili pip:

##### Korišćenje Poetry-ja

Black se automatski instalira kada podesite razvojnu sredinu:
```bash
poetry install
```

##### Korišćenje pip-a

Ako koristite pip, Black možete instalirati direktno:
```bash
pip install black
```

#### Korišćenje Black-a

##### Sa Poetry-jem

1. Formatirajte sve Python fajlove u projektu:
    ```bash
    poetry run black .
    ```

2. Formatirajte određeni fajl ili direktorijum:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Sa pip-om

1. Formatirajte sve Python fajlove u projektu:
    ```bash
    black .
    ```

2. Formatirajte određeni fajl ili direktorijum:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Preporučujemo da podesite vaš editor da automatski formatira kod sa Black prilikom čuvanja. Većina modernih editora podržava ovo preko ekstenzija ili plugina.

## Pokretanje Co-op Translator-a

Da biste pokrenuli Co-op Translator koristeći Poetry u vašem okruženju, pratite sledeće korake:

1. Pređite u direktorijum gde želite da obavite testove prevoda ili napravite privremeni folder za testiranje.

2. Pokrenite sledeću komandu. Zamena `-l ko` with the language code you wish to translate into. The `-d` zastavica označava debug režim.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Proverite da li je vaše Poetry okruženje aktivirano (poetry shell) pre pokretanja komande.

## Održavaoci

### Poruka komita i strategija spajanja

Da bismo osigurali doslednost i jasnoću u istoriji komita našeg projekta, koristimo specifičan format poruke komita **za finalnu poruku komita** pri korišćenju **Squash and Merge** strategije.

Kada se pull request (PR) spoji, pojedinačni komiti se spajaju u jedan komit. Finalna poruka komita treba da prati format ispod kako bismo održali urednu i doslednu istoriju.

#### Format poruke komita (za squash and merge)

Koristimo sledeći format za poruke komita:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Određuje kategoriju komita. Koristimo sledeće tipove:
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

**Одрицање од одговорности**:  
Овај документ је преведен помоћу AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране стручног људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала употребом овог превода.