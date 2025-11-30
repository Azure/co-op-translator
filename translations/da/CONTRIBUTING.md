<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:23:37+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "da"
}
-->
# Bidrag til Co-op Translator

Dette projekt byder velkommen til bidrag og forslag. De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til, og faktisk giver os rettighederne til at bruge dit bidrag. For detaljer, besøg https://cla.opensource.microsoft.com.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal levere en CLA og markere PR'en passende (f.eks. statuskontrol, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

## Opsætning af udviklingsmiljø

For at sætte udviklingsmiljøet op til dette projekt anbefaler vi at bruge Poetry til håndtering af afhængigheder. Vi bruger `pyproject.toml` til at styre projektets afhængigheder, og derfor bør du bruge Poetry til at installere afhængigheder.

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

5. Tjek de oversatte filer i `test_docs/translations` og `test_docs/translated_images` for at bekræfte:
   - Oversættelseskvaliteten
   - At metadata-kommentarerne er korrekte
   - At den oprindelige markdown-struktur er bevaret
   - At links og billeder fungerer korrekt

Denne manuelle test sikrer, at dine ændringer fungerer godt i virkelige scenarier.

### Miljøvariabler

1. Opret en `.env`-fil i rodmappen ved at kopiere den medfølgende `.env.template`-fil.
1. Udfyld miljøvariablerne som angivet.

> [!TIP]
>
> ### Yderligere muligheder for udviklingsmiljø
>
> Ud over at køre projektet lokalt kan du også bruge GitHub Codespaces eller VS Code Dev Containers som alternative udviklingsmiljøer.
>
> #### GitHub Codespaces
>
> Du kan køre disse eksempler virtuelt ved at bruge GitHub Codespaces, og der kræves ingen yderligere indstillinger eller opsætning.
>
> Knappen åbner en webbaseret VS Code-forekomst i din browser:
>
> 1. Åbn skabelonen (det kan tage flere minutter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kørsel lokalt med VS Code Dev Containers
>
> ⚠️ Denne mulighed virker kun, hvis din Docker Desktop har tildelt mindst 16 GB RAM. Hvis du har mindre end 16 GB RAM, kan du prøve [GitHub Codespaces-muligheden](../..) eller [opsætte det lokalt](../..).
>
> En relateret mulighed er VS Code Dev Containers, som åbner projektet i din lokale VS Code ved hjælp af [Dev Containers-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det, hvis det ikke allerede er installeret)
> 2. Åbn projektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodeformat

Vi bruger [Black](https://github.com/psf/black) som vores Python-kodeformatter for at opretholde en ensartet kodestil i hele projektet. Black er en kompromisløs kodeformatter, der automatisk omformaterer Python-kode, så den følger Black-kodestilen.

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

2. Formater en specifik fil eller mappe:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Med pip

1. Formater alle Python-filer i projektet:
    ```bash
    black .
    ```

2. Formater en specifik fil eller mappe:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Vi anbefaler, at du sætter din editor op til automatisk at formatere kode med Black ved gemning. De fleste moderne editorer understøtter dette via udvidelser eller plugins.

## Kørsel af Co-op Translator

For at køre Co-op Translator med Poetry i dit miljø, følg disse trin:

1. Naviger til den mappe, hvor du vil udføre oversættelsestests, eller opret en midlertidig mappe til testformål.

2. Kør følgende kommando. Erstat `-l ko` med det sprogkode, du ønsker at oversætte til. `-d`-flaget angiver debug-tilstand.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for, at dit Poetry-miljø er aktiveret (poetry shell), før du kører kommandoen.

## Bidrag med et nyt sprog

Vi byder velkommen til bidrag, der tilføjer support for nye sprog. Før du åbner en PR, bedes du gennemføre nedenstående trin for at sikre en glat gennemgang.

1. Tilføj sproget til font-mappingen
   - Rediger `src/co_op_translator/fonts/font_language_mappings.yml`
   - Tilføj en post med:
     - `code`: ISO-lignende sprogkode (f.eks. `vi`)
     - `name`: Bruger-venligt visningsnavn
     - `font`: En font, der leveres i `src/co_op_translator/fonts/`, som understøtter skriftsystemet
     - `rtl`: `true` hvis højre-til-venstre, ellers `false`

2. Inkluder nødvendige fontfiler (hvis nødvendigt)
   - Hvis en ny font kræves, skal du verificere licenskompatibilitet for open source-distribution
   - Tilføj fontfilen til `src/co_op_translator/fonts/`

3. Lokal verifikation
   - Kør oversættelser for et lille eksempel (Markdown, billeder og notebooks efter behov)
   - Bekræft, at output vises korrekt, inklusive fonte og eventuel RTL-layout

4. Opdater dokumentationen
   - Sørg for, at sproget vises i `getting_started/supported-languages.md`
   - Der er ikke behov for ændringer i `getting_started/README_languages_template.md`; den genereres fra den understøttede liste

5. Åbn en PR
   - Beskriv det tilføjede sprog og eventuelle font-/licenshensyn
   - Vedhæft screenshots af gengivne output, hvis muligt

Eksempel på YAML-post:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Test det nye sprog

Du kan teste det nye sprog ved at køre følgende kommando:

```bash
# Opret og aktiver et virtuelt miljø
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installer udviklingspakken
pip install -e .
# Kør oversættelsen
translate -l "new_lang"
```

## Vedligeholdere

### Commit-besked og Merge-strategi

For at sikre konsistens og klarhed i vores projekts commit-historik følger vi et specifikt commit-beskedformat **for den endelige commit-besked** ved brug af **Squash and Merge**-strategien.

Når en pull request (PR) merges, bliver de enkelte commits samlet til én enkelt commit. Den endelige commit-besked skal følge formatet nedenfor for at bevare en ren og ensartet historik.

#### Commit-beskedformat (for squash and merge)

Vi bruger følgende format til commit-beskeder:

```bash
<type>: <description> (#<PR nummer>)
```

- **type**: Angiver kategorien for committet. Vi bruger følgende typer:
  - `Docs`: Til opdateringer af dokumentation.
  - `Build`: Til ændringer relateret til build-systemet eller afhængigheder, inklusive opdateringer af konfigurationsfiler, CI-workflows eller Dockerfile.
  - `Core`: Til ændringer i projektets kernefunktionalitet eller features, især filer i `src/co_op_translator/core`-mappen.

- **description**: En kortfattet opsummering af ændringen.
- **PR nummer**: Nummeret på den pull request, der er knyttet til committet.

**Eksempler**:

- `Docs: Opdater installationsvejledning for klarhed (#50)`
- `Core: Forbedret håndtering af billedoversættelse (#60)`

> [!NOTE]
> I øjeblikket tilføjes præfikserne **`Docs`**, **`Core`** og **`Build`** automatisk til PR-titler baseret på de labels, der er anvendt på den ændrede kildekode. Så længe den korrekte label er sat, behøver du normalt ikke manuelt at opdatere PR-titlen. Du skal blot sikre, at alt er korrekt, og at præfikset er genereret passende.

#### Merge-strategi

Vi bruger **Squash and Merge** som vores standardstrategi for pull requests. Denne strategi sikrer, at commit-beskeder følger vores format, selvom de enkelte commits ikke gør det.

**Årsager**:

- En ren, lineær projekthistorik.
- Konsistens i commit-beskeder.
- Mindre støj fra mindre commits (f.eks. "fix typo").

Når du merger, skal du sikre, at den endelige commit-besked følger det beskrevne commit-beskedformat.

**Eksempel på Squash and Merge**
Hvis en PR indeholder følgende commits:

- `fix typo`
- `update README`
- `adjust formatting`

Skal de samles til:
`Docs: Forbedret dokumentationsklarhed og formatering (#65)`

### Udgivelsesproces

Dette afsnit beskriver den nemmeste måde for vedligeholdere at udgive en ny version af Co-op Translator.

#### 1. Opdater versionen i `pyproject.toml`

1. Beslut det næste versionsnummer (vi følger semantisk versionering: `MAJOR.MINOR.PATCH`).
2. Rediger `pyproject.toml` og opdater `version`-feltet under `[tool.poetry]`.
3. Åbn en dedikeret pull request, der kun ændrer versionen (og eventuelle automatisk opdaterede lock-/metadatafiler, hvis de findes).
4. Efter gennemgang, brug **Squash and Merge** og sørg for, at den endelige commit-besked følger det beskrevne format.

#### 2. Opret en GitHub Release

1. Gå til GitHub-repositoriets side og åbn **Releases** → **Draft a new release**.
2. Opret et nyt tag (for eksempel `v0.13.0`) fra `main`-grenen.
3. Sæt udgivelsestitlen til samme version (for eksempel `v0.13.0`).
4. Klik på **Generate release notes** for automatisk at udfylde changeloggen.
5. Rediger eventuelt teksten (f.eks. for at fremhæve nyligt understøttede sprog eller vigtige ændringer).
6. Udgiv releasen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->