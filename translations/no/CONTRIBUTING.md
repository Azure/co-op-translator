<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:23:24+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "no"
}
-->
# Bidra til Co-op Translator

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godkjenner en Contributor License Agreement (CLA) som bekrefter at du har rett til, og faktisk gir oss, rettighetene til å bruke bidraget ditt. For mer informasjon, se https://cla.opensource.microsoft.com.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må signere en CLA og merke PR-en deretter (f.eks. status-sjekk, kommentar). Følg bare instruksjonene fra boten. Du trenger kun å gjøre dette én gang for alle repoer som bruker vår CLA.

## Sette opp utviklingsmiljø

For å sette opp utviklingsmiljøet for dette prosjektet anbefaler vi å bruke Poetry for å håndtere avhengigheter. Vi bruker `pyproject.toml` for å administrere prosjektavhengigheter, så for å installere avhengigheter bør du bruke Poetry.

### Opprett et virtuelt miljø

#### Med pip

```bash
python -m venv .venv
```

#### Med Poetry

```bash
poetry init
```

### Aktiver det virtuelle miljøet

#### For både pip og Poetry

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

### Installere pakken og nødvendige pakker

#### Med Poetry (fra pyproject.toml)

```bash
poetry install
```

### Manuell testing

Før du sender inn en PR, er det viktig å teste oversettelsesfunksjonaliteten med ekte dokumentasjon:

1. Lag en testmappe i rotmappen:
    ```bash
    mkdir test_docs
    ```

2. Kopier noen markdown-dokumenter og bilder du vil oversette inn i testmappen. For eksempel:
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

5. Sjekk de oversatte filene i `test_docs/translations` og `test_docs/translated_images` for å verifisere:
   - Kvaliteten på oversettelsen
   - At metadata-kommentarene er riktige
   - At den opprinnelige markdown-strukturen er bevart
   - At lenker og bilder fungerer som de skal

Denne manuelle testingen hjelper deg å sikre at endringene dine fungerer godt i praksis.

### Miljøvariabler

1. Lag en `.env`-fil i rotmappen ved å kopiere den medfølgende `.env.template`-filen.
1. Fyll inn miljøvariablene som angitt.

> [!TIP]
>
> ### Flere alternativer for utviklingsmiljø
>
> I tillegg til å kjøre prosjektet lokalt, kan du også bruke GitHub Codespaces eller VS Code Dev Containers som alternative utviklingsmiljøer.
>
> #### GitHub Codespaces
>
> Du kan kjøre disse eksemplene virtuelt ved å bruke GitHub Codespaces, uten ekstra oppsett eller innstillinger.
>
> Knappen åpner en nettbasert VS Code-instans i nettleseren din:
>
> 1. Åpne malen (dette kan ta noen minutter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kjør lokalt med VS Code Dev Containers
>
> ⚠️ Dette alternativet fungerer kun hvis Docker Desktop er tildelt minst 16 GB RAM. Hvis du har mindre enn 16 GB RAM, kan du prøve [GitHub Codespaces-alternativet](../..) eller [sette det opp lokalt](../..).
>
> Et beslektet alternativ er VS Code Dev Containers, som åpner prosjektet i din lokale VS Code med [Dev Containers-utvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det hvis det ikke allerede er installert)
> 2. Åpne prosjektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kode-stil

Vi bruker [Black](https://github.com/psf/black) som formatteringsverktøy for Python-kode for å sikre en konsekvent stil i hele prosjektet. Black er en kompromissløs formatterer som automatisk omformaterer Python-kode til å følge Black sin stil.

#### Konfigurasjon

Black-konfigurasjonen er spesifisert i vår `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installere Black

Du kan installere Black med enten Poetry (anbefalt) eller pip:

##### Med Poetry

Black installeres automatisk når du setter opp utviklingsmiljøet:
```bash
poetry install
```

##### Med pip

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

For å kjøre Co-op Translator med Poetry i ditt miljø, følg disse stegene:

1. Gå til mappen der du vil utføre oversettelsestester, eller lag en midlertidig mappe for testing.

2. Kjør følgende kommando. Bytt ut `-l ko` med språkkoden du ønsker å oversette til. `-d`-flagget aktiverer debug-modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for at Poetry-miljøet ditt er aktivert (poetry shell) før du kjører kommandoen.

## Bidra med et nytt språk

Vi ønsker bidrag som legger til støtte for nye språk velkommen. Før du åpner en PR, vennligst fullfør stegene under for å gjøre gjennomgangen enklere.

1. Legg til språket i font-mappingen
   - Rediger `src/co_op_translator/fonts/font_language_mappings.yml`
   - Legg til en oppføring med:
     - `code`: ISO-lignende språkkode (f.eks. `vi`)
     - `name`: Brukervennlig visningsnavn
     - `font`: En font som ligger i `src/co_op_translator/fonts/` og støtter skriftsystemet
     - `rtl`: `true` hvis høyre-til-venstre, ellers `false`

2. Inkluder nødvendige fontfiler (om nødvendig)
   - Hvis en ny font trengs, sjekk at lisensen tillater åpen kildekode-distribusjon
   - Legg fontfilen til i `src/co_op_translator/fonts/`

3. Lokal verifisering
   - Kjør oversettelser på et lite utvalg (Markdown, bilder og notatbøker etter behov)
   - Sjekk at utdata vises riktig, inkludert fonter og eventuell RTL-layout

4. Oppdater dokumentasjonen
   - Sørg for at språket vises i `getting_started/supported-languages.md`
   - Ingen endringer i `README_languages_template.md` er nødvendig; den genereres fra listen over støttede språk

5. Åpne en PR
   - Beskriv hvilket språk som er lagt til og eventuelle font-/lisenshensyn
   - Legg gjerne ved skjermbilder av hvordan utdata ser ut

Eksempel på YAML-oppføring:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Vedlikeholdere

### Commit-melding og flette-strategi

For å sikre konsistens og tydelighet i prosjektets commit-historikk, følger vi et spesifikt format for commit-meldinger **for den endelige commit-meldingen** når vi bruker **Squash and Merge**-strategien.

Når en pull request (PR) flettes, vil de individuelle commitene slås sammen til én commit. Den endelige commit-meldingen skal følge formatet under for å holde historikken ryddig og konsekvent.

#### Commit-meldingsformat (for squash and merge)

Vi bruker følgende format for commit-meldinger:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Angir kategorien for commiten. Vi bruker følgende typer:
  - `Docs`: For oppdateringer i dokumentasjonen.
  - `Build`: For endringer relatert til byggesystemet eller avhengigheter, inkludert oppdateringer av konfigurasjonsfiler, CI-workflows eller Dockerfile.
  - `Core`: For endringer i prosjektets kjernefunksjonalitet eller funksjoner, spesielt de som gjelder filer i `src/co_op_translator/core`-mappen.

- **description**: En kort oppsummering av endringen.
- **PR number**: Nummeret på pull requesten som hører til commiten.

**Eksempler**:

- `Docs: Oppdater installasjonsinstruksjoner for klarhet (#50)`
- `Core: Forbedre håndtering av bildeoversettelse (#60)`

> [!NOTE]
> For øyeblikket blir **`Docs`**, **`Core`** og **`Build`**-prefiksene automatisk lagt til PR-titler basert på etikettene som brukes på endret kildekode. Så lenge riktig etikett er brukt, trenger du vanligvis ikke å endre PR-tittelen manuelt. Du må bare sjekke at alt er riktig og at prefikset er generert som det skal.

#### Flette-strategi

Vi bruker **Squash and Merge** som standard strategi for pull requests. Denne strategien sikrer at commit-meldinger følger vårt format, selv om de individuelle commitene ikke gjør det.

**Grunner**:

- En ryddig, lineær prosjekt-historikk.
- Konsistens i commit-meldinger.
- Mindre støy fra små commits (f.eks. "fikset skrivefeil").

Når du fletter, sørg for at den endelige commit-meldingen følger formatet beskrevet over.

**Eksempel på Squash and Merge**
Hvis en PR inneholder følgende commits:

- `fikset skrivefeil`
- `oppdatert README`
- `justert formatering`

Skal de slås sammen til:
`Docs: Forbedre dokumentasjonsklarhet og formatering (#65)`

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.