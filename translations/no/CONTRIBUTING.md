<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:36:39+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "no"
}
-->
# Bidra til Co-op Translator

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godtar en
Contributor License Agreement (CLA) som erklærer at du har rett til, og faktisk gir oss
rettighetene til å bruke ditt bidrag. For detaljer, besøk https://cla.opensource.microsoft.com.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere
en CLA og merke PR-en deretter (f.eks. status-sjekk, kommentar). Følg bare instruksjonene
som boten gir. Du trenger bare å gjøre dette én gang på tvers av alle repoer som bruker vår CLA.

## Oppsett av utviklingsmiljø

For å sette opp utviklingsmiljøet for dette prosjektet anbefaler vi å bruke Poetry for å håndtere avhengigheter. Vi bruker `pyproject.toml` for å håndtere prosjektavhengigheter, og derfor bør du bruke Poetry for å installere avhengigheter.

### Opprette et virtuelt miljø

#### Bruke pip

```bash
python -m venv .venv
```

#### Bruke Poetry

```bash
poetry init
```

### Aktivere det virtuelle miljøet

#### For både pip og Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Bruke Poetry

```bash
poetry shell
```

### Installere pakken og nødvendige pakker

#### Bruke Poetry (fra pyproject.toml)

```bash
poetry install
```

### Manuell testing

Før du sender inn en PR, er det viktig å teste oversettelsesfunksjonaliteten med ekte dokumentasjon:

1. Lag en testmappe i rotmappen:
    ```bash
    mkdir test_docs
    ```

2. Kopier noe markdown-dokumentasjon og bilder du vil oversette til testmappen. For eksempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installer pakken lokalt:
    ```bash
    pip install -e .
    ```

4. Kjør Co-op Translator på testdokumentene dine:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Sjekk de oversatte filene i `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`-filen.
1. Fyll inn miljøvariablene som angitt.

> [!TIP]
>
> ### Ytterligere alternativer for utviklingsmiljø
>
> I tillegg til å kjøre prosjektet lokalt, kan du også bruke GitHub Codespaces eller VS Code Dev Containers som et alternativt utviklingsmiljø.
>
> #### GitHub Codespaces
>
> Du kan kjøre disse eksemplene virtuelt ved å bruke GitHub Codespaces uten behov for ekstra innstillinger eller oppsett.
>
> Knappen åpner en nettleserbasert VS Code-instans:
>
> 1. Åpne malen (dette kan ta noen minutter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kjøre lokalt med VS Code Dev Containers
>
> ⚠️ Dette alternativet fungerer bare hvis Docker Desktop har minst 16 GB RAM tilgjengelig. Har du mindre enn 16 GB RAM, kan du prøve [GitHub Codespaces-alternativet](../..) eller [sette det opp lokalt](../..).
>
> Et relatert alternativ er VS Code Dev Containers, som åpner prosjektet i din lokale VS Code ved hjelp av [Dev Containers-utvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det hvis det ikke allerede er installert)
> 2. Åpne prosjektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodeformat

Vi bruker [Black](https://github.com/psf/black) som vår Python-kodeformatterer for å opprettholde en konsekvent kodestil i hele prosjektet. Black er en kompromissløs kodeformatterer som automatisk formatterer Python-kode slik at den følger Blacks kodestil.

#### Konfigurasjon

Black-konfigurasjonen er spesifisert i vår `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installere Black

Du kan installere Black enten med Poetry (anbefalt) eller pip:

##### Bruke Poetry

Black installeres automatisk når du setter opp utviklingsmiljøet:
```bash
poetry install
```

##### Bruke pip

Hvis du bruker pip, kan du installere Black direkte:
```bash
pip install black
```

#### Bruke Black

##### Med Poetry

1. Formater alle Python-filer i prosjektet:
    ```bash
    poetry run black .
    ```

2. Formater en spesifikk fil eller mappe:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formater alle Python-filer i prosjektet:
    ```bash
    black .
    ```

2. Formater en spesifikk fil eller mappe:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi anbefaler å sette opp editoren din til å automatisk formatere kode med Black ved lagring. De fleste moderne editorer støtter dette via utvidelser eller plugins.

## Kjøre Co-op Translator

For å kjøre Co-op Translator med Poetry i ditt miljø, følg disse trinnene:

1. Gå til mappen der du vil utføre oversettelsestester, eller lag en midlertidig mappe for testing.

2. Kjør følgende kommando. Erstatt `-l ko` with the language code you wish to translate into. The `-d`-flagget som angir debug-modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for at Poetry-miljøet ditt er aktivert (poetry shell) før du kjører kommandoen.

## Vedlikeholdere

### Commit-melding og Merge-strategi

For å sikre konsistens og tydelighet i prosjektets commit-historikk følger vi et spesifikt format for commit-meldinger **for den endelige commit-meldingen** når vi bruker **Squash and Merge**-strategien.

Når en pull request (PR) merges, blir de individuelle committene slått sammen til én commit. Den endelige commit-meldingen skal følge formatet under for å opprettholde en ryddig og konsistent historikk.

#### Commit-meldingsformat (for squash and merge)

Vi bruker følgende format for commit-meldinger:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Spesifiserer kategorien for committen. Vi bruker følgende typer:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Oppdater installasjonsinstruksjoner for klarhet (#50)`
- `Core: Forbedre håndtering av bildeoversettelse (#60)`

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

- `rett skrivefeil`
- `oppdater README`
- `juster formatering`

They should be squashed into:
`Docs: Forbedre dokumentasjonsklarhet og formatering (#65)`

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.