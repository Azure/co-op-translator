<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:27:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "no"
}
-->
# Bidra til Co-op Translator

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rettighetene til, og faktisk gir oss rett til å bruke ditt bidrag. For detaljer, besøk https://cla.opensource.microsoft.com.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere en CLA og merke PR-en deretter (f.eks. statuskontroll, kommentar). Følg bare instruksjonene fra boten. Du trenger bare å gjøre dette én gang for alle repos som bruker vår CLA.

## Oppsett av utviklingsmiljø

For å sette opp utviklingsmiljøet for dette prosjektet anbefaler vi å bruke Poetry for avhengighetsstyring. Vi bruker `pyproject.toml` for å håndtere prosjektavhengigheter, og derfor bør du bruke Poetry for å installere avhengigheter.

### Opprett et virtuelt miljø

#### Bruke pip

```bash
python -m venv .venv
```

#### Bruke Poetry

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

1. Opprett en testmappe i rotmappen:
    ```bash
    mkdir test_docs
    ```

2. Kopier noe markdown-dokumentasjon og bilder du ønsker å oversette inn i testmappen. For eksempel:
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
   - At metadata-kommentarene er korrekte
   - At den originale markdown-strukturen er bevart
   - At lenker og bilder fungerer som de skal

Denne manuelle testingen hjelper med å sikre at endringene dine fungerer godt i virkelige situasjoner.

### Miljøvariabler

1. Opprett en `.env`-fil i rotmappen ved å kopiere den medfølgende `.env.template`-filen.
1. Fyll inn miljøvariablene som angitt.

> [!TIP]
>
> ### Ytterligere alternativer for utviklingsmiljø
>
> I tillegg til å kjøre prosjektet lokalt, kan du også bruke GitHub Codespaces eller VS Code Dev Containers som alternative utviklingsmiljøer.
>
> #### GitHub Codespaces
>
> Du kan kjøre disse eksemplene virtuelt ved å bruke GitHub Codespaces, og ingen ekstra innstillinger eller oppsett kreves.
>
> Knappen åpner en nettbasert VS Code-instans i nettleseren din:
>
> 1. Åpne malen (dette kan ta noen minutter):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Kjøre lokalt med VS Code Dev Containers
>
> ⚠️ Dette alternativet fungerer bare hvis Docker Desktop har minst 16 GB RAM tilgjengelig. Hvis du har mindre enn 16 GB RAM, kan du prøve [GitHub Codespaces-alternativet](../..) eller [sette det opp lokalt](../..).
>
> Et relatert alternativ er VS Code Dev Containers, som åpner prosjektet i din lokale VS Code ved hjelp av [Dev Containers-utvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (installer det hvis det ikke allerede er installert)
> 2. Åpne prosjektet:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kodeformat

Vi bruker [Black](https://github.com/psf/black) som vår Python-kodeformatterer for å opprettholde en konsekvent kodeformat på tvers av prosjektet. Black er en kompromissløs formatterer som automatisk formaterer Python-kode for å følge Black sin stil.

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
> Vi anbefaler at du setter opp editoren din til å automatisk formatere kode med Black ved lagring. De fleste moderne editorer støtter dette via utvidelser eller plugins.

## Kjøre Co-op Translator

For å kjøre Co-op Translator med Poetry i ditt miljø, følg disse stegene:

1. Naviger til mappen der du vil utføre oversettelsestester, eller opprett en midlertidig mappe for testing.

2. Kjør følgende kommando. Bytt ut `-l ko` med språkkoden du ønsker å oversette til. `-d`-flagget angir debug-modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Sørg for at Poetry-miljøet ditt er aktivert (poetry shell) før du kjører kommandoen.

## Bidra med et nytt språk

Vi ønsker bidrag som legger til støtte for nye språk. Før du åpner en PR, vennligst fullfør stegene nedenfor for å sikre en smidig gjennomgang.

1. Legg til språket i font-mappingen
   - Rediger `src/co_op_translator/fonts/font_language_mappings.yml`
   - Legg til en oppføring med:
     - `code`: ISO-lignende språkkode (f.eks. `vi`)
     - `name`: Brukervennlig visningsnavn
     - `font`: En font som følger med i `src/co_op_translator/fonts/` som støtter skriptet
     - `rtl`: `true` hvis høyre-til-venstre, ellers `false`

2. Inkluder nødvendige fontfiler (om nødvendig)
   - Hvis en ny font kreves, sjekk lisenskompatibilitet for åpen kildekode-distribusjon
   - Legg fontfilen til `src/co_op_translator/fonts/`

3. Lokal verifisering
   - Kjør oversettelser for et lite utvalg (Markdown, bilder og notebooks etter behov)
   - Verifiser at output vises korrekt, inkludert fonter og eventuelt RTL-oppsett

4. Oppdater dokumentasjonen
   - Sørg for at språket vises i `getting_started/supported-languages.md`
   - Ingen endringer trengs i `getting_started/README_languages_template.md`; den genereres fra støttelisten

5. Åpne en PR
   - Beskriv språket som er lagt til og eventuelle font-/lisenshensyn
   - Legg ved skjermbilder av gjengitte resultater hvis mulig

Eksempel på YAML-oppføring:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Test det nye språket

Du kan teste det nye språket ved å kjøre følgende kommando:

```bash
# Opprett og aktiver et virtuelt miljø
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installer utviklingspakken
pip install -e .
# Kjør oversettelsen
translate -l "new_lang"
```

## Vedlikeholdere

### Commit-melding og Merge-strategi

For å sikre konsistens og klarhet i prosjektets commit-historikk, følger vi et spesifikt commit-meldingsformat **for den endelige commit-meldingen** når vi bruker **Squash and Merge**-strategien.

Når en pull request (PR) merges, blir de individuelle commitene slått sammen til én commit. Den endelige commit-meldingen bør følge formatet nedenfor for å opprettholde en ryddig og konsistent historikk.

#### Commit-meldingsformat (for squash and merge)

Vi bruker følgende format for commit-meldinger:

```bash
<type>: <description> (#<PR nummer>)
```

- **type**: Spesifiserer kategorien for commiten. Vi bruker følgende typer:
  - `Docs`: For dokumentasjonsoppdateringer.
  - `Build`: For endringer relatert til byggesystem eller avhengigheter, inkludert oppdateringer av konfigurasjonsfiler, CI-arbeidsflyter eller Dockerfile.
  - `Core`: For modifikasjoner av prosjektets kjernefunksjonalitet eller funksjoner, spesielt filer i `src/co_op_translator/core`-mappen.

- **description**: En kortfattet oppsummering av endringen.
- **PR-nummer**: Nummeret på pull requesten knyttet til commiten.

**Eksempler**:

- `Docs: Oppdater installasjonsinstruksjoner for klarhet (#50)`
- `Core: Forbedre håndtering av bildeoversettelse (#60)`

> [!NOTE]
> For øyeblikket legges **`Docs`**, **`Core`** og **`Build`** prefikser automatisk til PR-titler basert på etikettene som er brukt på den modifiserte kildekoden. Så lenge riktig etikett er brukt, trenger du vanligvis ikke å oppdatere PR-tittelen manuelt. Du må bare kontrollere at alt er korrekt og at prefikset er generert riktig.

#### Merge-strategi

Vi bruker **Squash and Merge** som standard strategi for pull requests. Denne strategien sikrer at commit-meldinger følger vårt format, selv om individuelle commits ikke gjør det.

**Grunner**:

- En ren, lineær prosjekt-historikk.
- Konsistens i commit-meldinger.
- Mindre støy fra små commits (f.eks. "fikse skrivefeil").

Når du merger, sørg for at den endelige commit-meldingen følger commit-meldingsformatet beskrevet ovenfor.

**Eksempel på Squash and Merge**
Hvis en PR inneholder følgende commits:

- `fikse skrivefeil`
- `oppdatere README`
- `justere formatering`

Skal de slås sammen til:
`Docs: Forbedre dokumentasjonsklarhet og formatering (#65)`

### Utgivelsesprosess

Denne seksjonen beskriver den enkleste måten for vedlikeholdere å publisere en ny utgivelse av Co-op Translator.

#### 1. Oppdater versjonen i `pyproject.toml`

1. Bestem neste versjonsnummer (vi følger semantisk versjonering: `MAJOR.MINOR.PATCH`).
2. Rediger `pyproject.toml` og oppdater `version`-feltet under `[tool.poetry]`.
3. Åpne en dedikert pull request som kun endrer versjonen (og eventuelle automatisk oppdaterte lock-/metadatafiler, hvis tilstede).
4. Etter gjennomgang, bruk **Squash and Merge** og sørg for at den endelige commit-meldingen følger formatet beskrevet ovenfor.

#### 2. Opprett en GitHub-utgivelse

1. Gå til GitHub-repositoriets side og åpne **Releases** → **Draft a new release**.
2. Lag en ny tag (for eksempel `v0.13.0`) fra `main`-grenen.
3. Sett utgivelsestittelen til samme versjon (for eksempel `v0.13.0`).
4. Klikk **Generate release notes** for å automatisk fylle ut endringsloggen.
5. Rediger eventuelt teksten (for eksempel for å fremheve nylig støttede språk eller viktige endringer).
6. Publiser utgivelsen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->