<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:36:19+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "da"
}
-->
# Bidrag til Co-op Translator

Dette projekt byder velkommen til bidrag og forslag. De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), hvor du erklærer, at du har ret til, og faktisk giver os, rettighederne til at bruge dit bidrag. For detaljer, besøg https://cla.opensource.microsoft.com.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal indsende en CLA og markere PR’en passende (f.eks. statuskontrol, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang for alle repos, der bruger vores CLA.

## Opsætning af udviklingsmiljø

For at sætte udviklingsmiljøet op til dette projekt anbefaler vi at bruge Poetry til at håndtere afhængigheder. Vi bruger `pyproject.toml` til at styre projektets afhængigheder, og derfor bør du bruge Poetry til at installere afhængigheder.

### Opret et virtuelt miljø

#### Brug af pip

```bash
python -m venv .venv
```

#### Brug af Poetry

```bash
poetry init
```

### Aktivér det virtuelle miljø

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Brug af Poetry

```bash
poetry shell
```

### Installation af pakken og nødvendige pakker

#### Brug af Poetry (fra pyproject.toml)

```bash
poetry install
```

### Manuel test

Før du indsender en PR, er det vigtigt at teste oversættelsesfunktionen med rigtig dokumentation:

1. Opret en testmappe i rodmappen:
    ```bash
    mkdir test_docs
    ```

2. Kopiér noget markdown-dokumentation og billeder, du vil oversætte, ind i testmappen. For eksempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installer pakken lokalt:
    ```bash
    pip install -e .
    ```

4. Kør Co-op Translator på dine testdokumenter:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Tjek de oversatte filer i `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` filen.
1. Udfyld miljøvariablerne som vejledt.

> [!TIP]
>
> ### Yderligere muligheder for udviklingsmiljø
>
> Ud over at køre projektet lokalt kan du også bruge GitHub Codespaces eller VS Code Dev Containers som alternative udviklingsmiljøer.
>
> #### GitHub Codespaces
>
> Du kan køre dette eksempel virtuelt ved at bruge GitHub Codespaces, og der kræves ingen yderligere opsætning.
>
> Knappen åbner en webbaseret VS Code i din browser:
>
> 1. Åbn skabelonen (det kan tage et par minutter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kørsel lokalt med VS Code Dev Containers
>
> ⚠️ Denne mulighed virker kun, hvis din Docker Desktop har mindst 16 GB RAM tildelt. Har du mindre end 16 GB RAM, kan du prøve [GitHub Codespaces-muligheden](../..) eller [sætte det op lokalt](../..).
>
> Et beslægtet alternativ er VS Code Dev Containers, som åbner projektet i din lokale VS Code ved hjælp af [Dev Containers-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det, hvis det ikke allerede er installeret)
> 2. Åbn projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodeformat

Vi bruger [Black](https://github.com/psf/black) som vores Python-kodeformatter for at sikre en ensartet kodestil i hele projektet. Black er en kompromisløs formatter, der automatisk formaterer Python-kode, så den overholder Black’s kodestandard.

#### Konfiguration

Black-konfigurationen er angivet i vores `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installation af Black

Du kan installere Black enten med Poetry (anbefalet) eller pip:

##### Brug af Poetry

Black installeres automatisk, når du sætter udviklingsmiljøet op:
```bash
poetry install
```

##### Brug af pip

Hvis du bruger pip, kan du installere Black direkte:
```bash
pip install black
```

#### Brug af Black

##### Med Poetry

1. Formater alle Python-filer i projektet:
    ```bash
    poetry run black .
    ```

2. Formater en bestemt fil eller mappe:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formater alle Python-filer i projektet:
    ```bash
    black .
    ```

2. Formater en bestemt fil eller mappe:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi anbefaler, at du sætter din editor op til automatisk at formatere kode med Black ved gem. De fleste moderne editorer understøtter dette via udvidelser eller plugins.

## Kørsel af Co-op Translator

For at køre Co-op Translator med Poetry i dit miljø, følg disse trin:

1. Gå til den mappe, hvor du vil teste oversættelser, eller opret en midlertidig mappe til test.

2. Kør følgende kommando. Flaget `-l ko` with the language code you wish to translate into. The `-d` angiver debug-tilstand.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for, at dit Poetry-miljø er aktiveret (poetry shell), inden du kører kommandoen.

## Vedligeholdere

### Commit-besked og Merge-strategi

For at sikre konsistens og klarhed i projektets commit-historik følger vi et bestemt commit-beskedformat **for den endelige commit-besked** ved brug af **Squash and Merge** strategien.

Når en pull request (PR) merges, bliver de enkelte commits samlet til én commit. Den endelige commit-besked skal følge formatet nedenfor for at bevare en ren og ensartet historik.

#### Commit-beskedformat (for squash and merge)

Vi bruger følgende format til commit-beskeder:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Angiver typen af commit. Vi bruger følgende typer:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Opdater installationsvejledning for klarhed (#50)`
- `Core: Forbedret håndtering af billedoversættelse (#60)`

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

- `ret rettelse af stavefejl`
- `opdater README`
- `juster formatering`

They should be squashed into:
`Docs: Forbedret dokumentationsklarhed og formatering (#65)`

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.