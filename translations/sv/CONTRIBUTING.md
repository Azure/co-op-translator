<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:35:47+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sv"
}
-->
# Bidra till Co-op Translator

Det här projektet välkomnar bidrag och förslag. De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att, och faktiskt ger oss, rättigheterna att använda ditt bidrag. För detaljer, besök https://cla.opensource.microsoft.com.

När du skickar in en pull request kommer en CLA-bot automatiskt att avgöra om du behöver tillhandahålla en CLA och märka PR korrekt (t.ex. statuskontroll, kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vår CLA.

## Uppställning av utvecklingsmiljö

För att sätta upp utvecklingsmiljön för detta projekt rekommenderar vi att använda Poetry för att hantera beroenden. Vi använder `pyproject.toml` för att hantera projektets beroenden, och därför bör du använda Poetry för att installera beroenden.

### Skapa en virtuell miljö

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktivera den virtuella miljön

#### För både pip och Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Med Poetry

```bash
poetry shell
```

### Installera paketet och nödvändiga paket

#### Med Poetry (från pyproject.toml)

```bash
poetry install
```

### Manuell testning

Innan du skickar in en PR är det viktigt att testa översättningsfunktionen med verklig dokumentation:

1. Skapa en testkatalog i rotkatalogen:
    ```bash
    mkdir test_docs
    ```

2. Kopiera någon markdown-dokumentation och bilder som du vill översätta till testkatalogen. Till exempel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installera paketet lokalt:
    ```bash
    pip install -e .
    ```

4. Kör Co-op Translator på dina testdokument:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kontrollera de översatta filerna i `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`-filen.
1. Fyll i miljövariablerna enligt instruktionerna.

> [!TIP]
>
> ### Ytterligare alternativ för utvecklingsmiljö
>
> Förutom att köra projektet lokalt kan du också använda GitHub Codespaces eller VS Code Dev Containers som ett alternativ för att sätta upp utvecklingsmiljön.
>
> #### GitHub Codespaces
>
> Du kan köra dessa exempel virtuellt med GitHub Codespaces och inga extra inställningar eller konfigurationer krävs.
>
> Knappen öppnar en webbaserad VS Code-instans i din webbläsare:
>
> 1. Öppna mallen (det kan ta några minuter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Köra lokalt med VS Code Dev Containers
>
> ⚠️ Det här alternativet fungerar endast om din Docker Desktop har tilldelats minst 16 GB RAM. Om du har mindre än 16 GB RAM kan du prova [GitHub Codespaces-alternativet](../..) eller [sätta upp det lokalt](../..).
>
> Ett relaterat alternativ är VS Code Dev Containers, som öppnar projektet i din lokala VS Code med hjälp av [Dev Containers-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Starta Docker Desktop (installera det om det inte redan är installerat)
> 2. Öppna projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodstil

Vi använder [Black](https://github.com/psf/black) som vår Python-kodformatterare för att upprätthålla en konsekvent kodstil i hela projektet. Black är en kompromisslös kodformatterare som automatiskt formaterar om Python-kod för att följa Blacks kodstil.

#### Konfiguration

Black-konfigurationen anges i vår `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installera Black

Du kan installera Black med antingen Poetry (rekommenderas) eller pip:

##### Med Poetry

Black installeras automatiskt när du sätter upp utvecklingsmiljön:
```bash
poetry install
```

##### Med pip

Om du använder pip kan du installera Black direkt:
```bash
pip install black
```

#### Använda Black

##### Med Poetry

1. Formatera alla Python-filer i projektet:
    ```bash
    poetry run black .
    ```

2. Formatera en specifik fil eller katalog:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formatera alla Python-filer i projektet:
    ```bash
    black .
    ```

2. Formatera en specifik fil eller katalog:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi rekommenderar att du ställer in din editor så att koden formateras automatiskt med Black vid sparande. De flesta moderna editorer stöder detta via tillägg eller plugins.

## Köra Co-op Translator

För att köra Co-op Translator med Poetry i din miljö, följ dessa steg:

1. Navigera till den katalog där du vill utföra översättningstester eller skapa en temporär mapp för teständamål.

2. Kör följande kommando. Flaggan `-l ko` with the language code you wish to translate into. The `-d` anger debugläge.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Se till att din Poetry-miljö är aktiverad (poetry shell) innan du kör kommandot.

## Underhållare

### Commit-meddelande och merge-strategi

För att säkerställa konsekvens och tydlighet i vårt projekts commit-historik följer vi ett specifikt commit-meddelandeformat **för det slutgiltiga commit-meddelandet** när vi använder **Squash and Merge**-strategin.

När en pull request (PR) mergas kommer de individuella commits att slås ihop till en enda commit. Det slutgiltiga commit-meddelandet ska följa formatet nedan för att bibehålla en ren och konsekvent historik.

#### Commit-meddelandeformat (för squash and merge)

Vi använder följande format för commit-meddelanden:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specificerar kategorin för commit. Vi använder följande typer:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Uppdatera installationsinstruktioner för tydlighet (#50)`
- `Core: Förbättra hantering av bildöversättning (#60)`

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

- `fixa stavfel`
- `uppdatera README`
- `justera formatering`

They should be squashed into:
`Docs: Förbättra dokumentationens tydlighet och formatering (#65)`

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.